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

_TRANSIENT_STATUS_CODES = {408, 425, 429, 500, 502, 503, 504}


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
    api_mode: str


def generate_grounded_markdown(
    *,
    api_key: str,
    model: str,
    prompt: str,
    system_instruction: str,
    search_mode: str = "auto",
    search_timeout_ms: int = 45_000,
    facts_timeout_ms: int = 120_000,
) -> GroundedResponse:
    """Generate a Gemini report while keeping the fact boundary deterministic.

    Search transport strategy:
      1. Interactions API + Google Search (preferred current API).
      2. If Interactions has a transient transport failure, retry Search once
         through the fully-supported GenerateContent API.
      3. In ``auto`` mode, if Search is unavailable because of quota or a
         second transient failure, generate from VERIFIED_FACTS only through
         GenerateContent without tools.

    ``required`` always requires a successful Search-grounded result. ``off``
    skips Search and uses VERIFIED_FACTS_ONLY directly.
    """
    from google import genai
    from google.genai import types

    mode = (search_mode or "auto").strip().lower()
    if mode not in {"auto", "required", "off"}:
        raise ValueError(f"unsupported Gemini search mode: {search_mode!r}")
    if search_timeout_ms < 1_000 or facts_timeout_ms < 1_000:
        raise ValueError("Gemini timeouts must be at least 1000 ms")

    facts_prompt = _facts_only_prompt(prompt)

    if mode == "off":
        client = _make_client(genai, api_key, facts_timeout_ms)
        response = _generate_content(
            client=client,
            types=types,
            model=model,
            prompt=facts_prompt,
            system_instruction=system_instruction + FACTS_ONLY_SYSTEM_SUFFIX,
            use_search=False,
        )
        return _parse_generate_content(
            response=response,
            model=model,
            grounding_mode="verified_facts_only",
            fallback_reason="google_search_disabled",
            api_mode="generate_content_facts_only",
        )

    search_client = _make_client(genai, api_key, search_timeout_ms)
    try:
        interaction = _create_interaction(
            client=search_client,
            model=model,
            prompt=prompt,
            system_instruction=system_instruction,
        )
    except Exception as interaction_exc:
        if _is_quota_error(interaction_exc):
            if mode == "required":
                raise
            return _generate_facts_only(
                genai=genai,
                types=types,
                api_key=api_key,
                model=model,
                prompt=facts_prompt,
                system_instruction=system_instruction,
                timeout_ms=facts_timeout_ms,
                fallback_reason="google_search_quota_unavailable",
            )

        if not _is_transient_error(interaction_exc):
            raise

        # Interactions transport failed. Keep Search if possible by trying the
        # still-supported GenerateContent endpoint before dropping grounding.
        legacy_search_client = _make_client(genai, api_key, search_timeout_ms)
        try:
            response = _generate_content(
                client=legacy_search_client,
                types=types,
                model=model,
                prompt=prompt,
                system_instruction=system_instruction,
                use_search=True,
            )
        except Exception as search_exc:
            if mode == "required":
                raise
            if not _is_search_fallback_error(search_exc):
                raise
            reason = (
                "google_search_quota_unavailable"
                if _is_quota_error(search_exc)
                else "google_search_transport_unavailable"
            )
            return _generate_facts_only(
                genai=genai,
                types=types,
                api_key=api_key,
                model=model,
                prompt=facts_prompt,
                system_instruction=system_instruction,
                timeout_ms=facts_timeout_ms,
                fallback_reason=reason,
            )

        return _parse_generate_content(
            response=response,
            model=model,
            grounding_mode="google_search",
            fallback_reason="interactions_transport_unavailable",
            api_mode="generate_content_search",
        )

    return _parse_interaction(interaction=interaction, model=model)


def _make_client(genai: Any, api_key: str, timeout_ms: int) -> Any:
    # The SDK defaults to several exponential retries. Keep the report bounded:
    # two total attempts with short delays, then let our explicit fallback
    # strategy decide what to do next.
    return genai.Client(
        api_key=api_key,
        http_options={
            "timeout": timeout_ms,
            "retry_options": {
                "attempts": 2,
                "initial_delay": 1.0,
                "max_delay": 3.0,
            },
        },
    )


def _create_interaction(
    *,
    client: Any,
    model: str,
    prompt: str,
    system_instruction: str,
) -> Any:
    return client.interactions.create(
        model=model,
        input=prompt,
        system_instruction=system_instruction,
        tools=[{"type": "google_search"}],
        generation_config={"temperature": 0.2},
        store=False,
    )


def _generate_content(
    *,
    client: Any,
    types: Any,
    model: str,
    prompt: str,
    system_instruction: str,
    use_search: bool,
) -> Any:
    config_kwargs: dict[str, Any] = {
        "system_instruction": system_instruction,
        "temperature": 0.2,
    }
    if use_search:
        config_kwargs["tools"] = [
            types.Tool(google_search=types.GoogleSearch())
        ]
    return client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(**config_kwargs),
    )


def _generate_facts_only(
    *,
    genai: Any,
    types: Any,
    api_key: str,
    model: str,
    prompt: str,
    system_instruction: str,
    timeout_ms: int,
    fallback_reason: str,
) -> GroundedResponse:
    client = _make_client(genai, api_key, timeout_ms)
    response = _generate_content(
        client=client,
        types=types,
        model=model,
        prompt=prompt,
        system_instruction=system_instruction + FACTS_ONLY_SYSTEM_SUFFIX,
        use_search=False,
    )
    return _parse_generate_content(
        response=response,
        model=model,
        grounding_mode="verified_facts_only",
        fallback_reason=fallback_reason,
        api_mode="generate_content_facts_only",
    )


def _parse_interaction(*, interaction: Any, model: str) -> GroundedResponse:
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
            arguments = getattr(step, "arguments", None)
            argument_queries = getattr(arguments, "queries", None) if arguments else None
            if argument_queries:
                search_queries.extend(str(x) for x in argument_queries if x)

    usage_obj = getattr(interaction, "usage", None)
    return GroundedResponse(
        text=text,
        model=model,
        interaction_id=getattr(interaction, "id", None),
        citations=_dedupe_citations(citations),
        search_queries=list(dict.fromkeys(search_queries)),
        usage=_to_dict(usage_obj) if usage_obj is not None else None,
        grounding_mode="google_search",
        grounding_fallback_reason=None,
        api_mode="interactions",
    )


def _parse_generate_content(
    *,
    response: Any,
    model: str,
    grounding_mode: str,
    fallback_reason: str | None,
    api_mode: str,
) -> GroundedResponse:
    text = (getattr(response, "text", None) or "").strip()
    if not text:
        raise RuntimeError("Gemini returned an empty report")

    citations: list[dict[str, Any]] = []
    search_queries: list[str] = []
    candidates = getattr(response, "candidates", None) or []
    candidate = candidates[0] if candidates else None
    grounding = getattr(candidate, "grounding_metadata", None) if candidate else None

    if grounding is not None:
        queries = getattr(grounding, "web_search_queries", None) or []
        search_queries.extend(str(x) for x in queries if x)
        chunks = getattr(grounding, "grounding_chunks", None) or []
        supports = getattr(grounding, "grounding_supports", None) or []

        for support in supports:
            segment = getattr(support, "segment", None)
            cited_text = getattr(segment, "text", None) if segment else None
            start = getattr(segment, "start_index", None) if segment else None
            end = getattr(segment, "end_index", None) if segment else None
            for index in getattr(support, "grounding_chunk_indices", None) or []:
                if not isinstance(index, int) or index < 0 or index >= len(chunks):
                    continue
                web = getattr(chunks[index], "web", None)
                url = getattr(web, "uri", None) if web else None
                if not url:
                    continue
                citations.append(
                    {
                        "title": getattr(web, "title", None),
                        "url": str(url),
                        "start_index": start,
                        "end_index": end,
                        "cited_text": cited_text,
                    }
                )

        # Some responses may provide grounding chunks without support ranges.
        if not citations:
            for chunk in chunks:
                web = getattr(chunk, "web", None)
                url = getattr(web, "uri", None) if web else None
                if url:
                    citations.append(
                        {
                            "title": getattr(web, "title", None),
                            "url": str(url),
                            "start_index": None,
                            "end_index": None,
                            "cited_text": None,
                        }
                    )

    usage_obj = getattr(response, "usage_metadata", None)
    response_id = getattr(response, "response_id", None)
    return GroundedResponse(
        text=text,
        model=model,
        interaction_id=str(response_id) if response_id else None,
        citations=_dedupe_citations(citations),
        search_queries=list(dict.fromkeys(search_queries)),
        usage=_to_dict(usage_obj) if usage_obj is not None else None,
        grounding_mode=grounding_mode,
        grounding_fallback_reason=fallback_reason,
        api_mode=api_mode,
    )


def _facts_only_prompt(prompt: str) -> str:
    return (
        "VERIFIED_FACTS_ONLY 模式已啟用。忽略任何要求你進行搜尋的指示；"
        "只可根據提供的 VERIFIED_FACTS 產生報告。\n\n" + prompt
    )


def _is_quota_error(exc: Exception) -> bool:
    status = getattr(exc, "status_code", None)
    code = getattr(exc, "code", None)
    text = str(exc).lower()
    return (
        status == 429
        or code == 429
        or exc.__class__.__name__ == "RateLimitError"
        or "too_many_requests" in text
        or "resource_exhausted" in text
        or "exceeded your current quota" in text
    )


def _is_transient_error(exc: Exception) -> bool:
    status = getattr(exc, "status_code", None)
    code = getattr(exc, "code", None)
    numeric = status if isinstance(status, int) else code if isinstance(code, int) else None
    name = exc.__class__.__name__.lower()
    text = str(exc).lower()
    return (
        numeric in _TRANSIENT_STATUS_CODES
        or _is_quota_error(exc)
        or "apiconnectionerror" in name
        or "timeout" in name
        or "remoteprotocolerror" in name
        or "server disconnected" in text
        or "connection reset" in text
        or "connection aborted" in text
        or "timed out" in text
        or "temporarily unavailable" in text
    )


def _is_search_fallback_error(exc: Exception) -> bool:
    return _is_quota_error(exc) or _is_transient_error(exc)


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
