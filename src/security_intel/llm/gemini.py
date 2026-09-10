from __future__ import annotations

from dataclasses import dataclass
from typing import Any

FACTS_ONLY_SYSTEM_SUFFIX = """

目前進入 VERIFIED_FACTS_ONLY 模式，Google Search 工具不可用。此模式的限制優先於其他指示：
- 不得使用模型既有知識新增任何近期漏洞事實、受影響版本、修補版本、攻擊事件、攻擊手法、勒索軟體歸因或 vendor 公告內容。
- 只能重述與分析 VERIFIED_FACTS 中已有的事實。
- 處置建議只能引用 VERIFIED_FACTS 內的 required_action，或提供不依賴特定未驗證版本/公告的一般性防禦建議。
- 不知道的資訊一律寫「未確認」。
- 不得暗示本次已進行即時網路搜尋。
"""


@dataclass
class GroundedResponse:
    text: str
    model: str
    interaction_id: str | None
    citations: list[dict[str, Any]]
    search_queries: list[str]
    usage: dict[str, Any] | None
    grounding_mode: str
    grounding_fallback_reason: str | None


def generate_grounded_markdown(
    *,
    api_key: str,
    model: str,
    prompt: str,
    system_instruction: str,
    search_mode: str = "auto",
) -> GroundedResponse:
    """Generate a report through Gemini Interactions API.

    search_mode:
      - auto: try Google Search grounding, then fall back to verified-facts-only
        when the API returns a quota/rate-limit error.
      - required: require Google Search grounding and propagate any failure.
      - off: never request Google Search and use verified-facts-only mode.

    Import google-genai lazily so collector/unit-test code does not depend on
    the reporting SDK.
    """
    from google import genai

    mode = (search_mode or "auto").strip().lower()
    if mode not in {"auto", "required", "off"}:
        raise ValueError(f"unsupported Gemini search mode: {search_mode!r}")

    client = genai.Client(api_key=api_key)
    grounding_mode = "google_search"
    fallback_reason: str | None = None

    if mode == "off":
        grounding_mode = "verified_facts_only"
        fallback_reason = "google_search_disabled"
        interaction = _create_interaction(
            client=client,
            model=model,
            prompt=prompt,
            system_instruction=system_instruction + FACTS_ONLY_SYSTEM_SUFFIX,
            use_search=False,
        )
    else:
        try:
            interaction = _create_interaction(
                client=client,
                model=model,
                prompt=prompt,
                system_instruction=system_instruction,
                use_search=True,
            )
        except Exception as exc:
            if mode != "auto" or not _is_quota_error(exc):
                raise
            grounding_mode = "verified_facts_only"
            fallback_reason = "google_search_quota_unavailable"
            interaction = _create_interaction(
                client=client,
                model=model,
                prompt=(
                    "VERIFIED_FACTS_ONLY 模式已啟用。忽略任何要求你進行搜尋的指示；"
                    "只可根據提供的 VERIFIED_FACTS 產生報告。\n\n" + prompt
                ),
                system_instruction=system_instruction + FACTS_ONLY_SYSTEM_SUFFIX,
                use_search=False,
            )

    text = (getattr(interaction, "output_text", None) or "").strip()
    if not text:
        raise RuntimeError("Gemini returned an empty report")

    citations: list[dict[str, Any]] = []
    search_queries: list[str] = []

    for step in getattr(interaction, "steps", None) or []:
        step_type = getattr(step, "type", None)
        if step_type == "model_output":
            for block in getattr(step, "content", None) or []:
                if getattr(block, "type", None) != "text":
                    continue
                block_text = getattr(block, "text", None) or ""
                for annotation in getattr(block, "annotations", None) or []:
                    if getattr(annotation, "type", None) != "url_citation":
                        continue
                    start = getattr(annotation, "start_index", None)
                    end = getattr(annotation, "end_index", None)
                    cited_text = None
                    if isinstance(start, int) and isinstance(end, int):
                        try:
                            cited_text = block_text[start:end]
                        except Exception:
                            cited_text = None
                    citations.append(
                        {
                            "title": getattr(annotation, "title", None),
                            "url": getattr(annotation, "url", None),
                            "start_index": start,
                            "end_index": end,
                            "cited_text": cited_text,
                        }
                    )
        elif step_type == "google_search_call":
            query = getattr(step, "query", None)
            if query:
                search_queries.append(str(query))
            queries = getattr(step, "queries", None)
            if queries:
                search_queries.extend(str(x) for x in queries if x)

    citations = _dedupe_citations(citations)
    search_queries = list(dict.fromkeys(search_queries))

    usage_obj = getattr(interaction, "usage", None)
    usage = _to_dict(usage_obj) if usage_obj is not None else None

    return GroundedResponse(
        text=text,
        model=model,
        interaction_id=getattr(interaction, "id", None),
        citations=citations,
        search_queries=search_queries,
        usage=usage,
        grounding_mode=grounding_mode,
        grounding_fallback_reason=fallback_reason,
    )


def _create_interaction(
    *,
    client: Any,
    model: str,
    prompt: str,
    system_instruction: str,
    use_search: bool,
) -> Any:
    kwargs: dict[str, Any] = {
        "model": model,
        "input": prompt,
        "system_instruction": system_instruction,
        "generation_config": {"temperature": 0.2},
        "store": False,
    }
    if use_search:
        kwargs["tools"] = [{"type": "google_search"}]
    return client.interactions.create(**kwargs)


def _is_quota_error(exc: Exception) -> bool:
    status = getattr(exc, "status_code", None)
    code = getattr(exc, "code", None)
    text = str(exc).lower()
    return (
        status == 429
        or code == 429
        or exc.__class__.__name__ == "RateLimitError"
        or "too_many_requests" in text
        or "exceeded your current quota" in text
    )


def _dedupe_citations(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[tuple[str | None, str | None]] = set()
    out: list[dict[str, Any]] = []
    for row in rows:
        key = (row.get("url"), row.get("cited_text"))
        if not row.get("url") or key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def _to_dict(value: Any) -> dict[str, Any]:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if isinstance(value, dict):
        return value
    return {"value": str(value)}
