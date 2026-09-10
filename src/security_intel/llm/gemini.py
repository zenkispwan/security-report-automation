from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class GroundedResponse:
    text: str
    model: str
    interaction_id: str | None
    citations: list[dict[str, Any]]
    search_queries: list[str]
    usage: dict[str, Any] | None


def generate_grounded_markdown(
    *,
    api_key: str,
    model: str,
    prompt: str,
    system_instruction: str,
) -> GroundedResponse:
    """Generate a grounded report through Gemini Interactions API.

    Import google-genai lazily so collector/unit-test code does not depend on
    the reporting SDK.
    """
    from google import genai

    client = genai.Client(api_key=api_key)
    interaction = client.interactions.create(
        model=model,
        input=prompt,
        system_instruction=system_instruction,
        tools=[{"type": "google_search"}],
        generation_config={"temperature": 0.2},
        store=False,
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
