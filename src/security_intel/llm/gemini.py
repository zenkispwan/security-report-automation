from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

_TRANSIENT_STATUS_CODES = {408, 425, 429, 500, 502, 503, 504}


@dataclass
class GroundedResponse:
    text: str
    model: str | None
    requested_model: str
    attempted_models: list[str]
    model_fallback_reason: str | None
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
    fallback_models: Sequence[str] | None = None,
    search_timeout_ms: int = 45_000,
) -> GroundedResponse:
    """Try to generate a Google-Search-grounded Gemini report.

    The adapter never asks an ungrounded LLM to invent a fallback report.
    When Search cannot be used in ``auto`` mode, it returns an explicit
    ``deterministic_facts_only`` decision. The caller then renders directly
    from verified ``delta.json`` / ``intelligence.json`` facts.

    Search transport strategy:
      1. Interactions API + Google Search using the requested model.
      2. On transient Interactions transport failure, try GenerateContent +
         Google Search. Transient 5xx/high-demand model errors may rotate
         through the configured stable model chain while preserving Search.
      3. If Search is unavailable because of quota or exhausted transient
         transport failures, return deterministic-facts-only mode.

    Authentication, authorization, malformed requests and other non-transient
    failures are never hidden by fallback.
    """
    from google import genai
    from google.genai import types

    mode = (search_mode or "auto").strip().lower()
    if mode not in {"auto", "required", "off"}:
        raise ValueError(f"unsupported Gemini search mode: {search_mode!r}")
    if search_timeout_ms < 1_000:
        raise ValueError("Gemini search timeout must be at least 1000 ms")

    models = _model_candidates(model, fallback_models or [])

    if mode == "off":
        return _deterministic_facts_only_response(
            requested_model=model,
            attempted_models=[],
            fallback_reason="google_search_disabled",
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
            return _deterministic_facts_only_response(
                requested_model=model,
                attempted_models=[model],
                fallback_reason="google_search_quota_unavailable",
            )

        if not _is_transient_error(interaction_exc):
            raise

        # Keep grounding if possible by trying the fully-supported
        # GenerateContent endpoint. Search quota 429 is not rotated through
        # models; high-demand 5xx/network errors may use fallback models.
        legacy_search_client = _make_client(genai, api_key, search_timeout_ms)
        attempted_search: list[str] = []
        try:
            response, selected_model, attempted = _generate_content_with_model_fallback(
                client=legacy_search_client,
                types=types,
                models=models,
                prompt=prompt,
                system_instruction=system_instruction,
                use_search=True,
                fallback_on_quota=False,
                attempted_out=attempted_search,
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
            return _deterministic_facts_only_response(
                requested_model=model,
                attempted_models=_merge_models([model], attempted_search),
                fallback_reason=reason,
            )

        attempted_all = _merge_models([model], attempted)
        return _parse_generate_content(
            response=response,
            model=selected_model,
            requested_model=model,
            attempted_models=attempted_all,
            model_fallback_reason=_model_fallback_reason(model, selected_model),
            grounding_mode="google_search",
            fallback_reason="interactions_transport_unavailable",
            api_mode="generate_content_search",
        )

    return _parse_interaction(
        interaction=interaction,
        model=model,
        requested_model=model,
        attempted_models=[model],
    )


def _deterministic_facts_only_response(
    *,
    requested_model: str,
    attempted_models: Sequence[str],
    fallback_reason: str,
) -> GroundedResponse:
    return GroundedResponse(
        text="",
        model=None,
        requested_model=requested_model,
        attempted_models=_merge_models(attempted_models),
        model_fallback_reason=None,
        interaction_id=None,
        citations=[],
        search_queries=[],
        usage=None,
        grounding_mode="verified_facts_only",
        grounding_fallback_reason=fallback_reason,
        api_mode="deterministic_facts_only",
    )


def _make_client(genai: Any, api_key: str, timeout_ms: int) -> Any:
    # Bound transient SDK retries; explicit transport fallback decides what to
    # do after two short attempts.
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
        config_kwargs["tools"] = [types.Tool(google_search=types.GoogleSearch())]
    return client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(**config_kwargs),
    )


def _generate_content_with_model_fallback(
    *,
    client: Any,
    types: Any,
    models: Sequence[str],
    prompt: str,
    system_instruction: str,
    use_search: bool,
    fallback_on_quota: bool,
    attempted_out: list[str] | None = None,
) -> tuple[Any, str, list[str]]:
    """Try models in order, crossing models only for transient failures."""
    attempted = attempted_out if attempted_out is not None else []
    last_exc: Exception | None = None

    for candidate in models:
        attempted.append(candidate)
        try:
            response = _generate_content(
                client=client,
                types=types,
                model=candidate,
                prompt=prompt,
                system_instruction=system_instruction,
                use_search=use_search,
            )
            return response, candidate, list(attempted)
        except Exception as exc:
            if _is_quota_error(exc) and not fallback_on_quota:
                raise
            if not _is_transient_error(exc):
                raise
            last_exc = exc

    if last_exc is not None:
        raise last_exc
    raise RuntimeError("Gemini model candidate list is empty")


def _parse_interaction(
    *,
    interaction: Any,
    model: str,
    requested_model: str,
    attempted_models: list[str],
) -> GroundedResponse:
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
        requested_model=requested_model,
        attempted_models=attempted_models,
        model_fallback_reason=_model_fallback_reason(requested_model, model),
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
    requested_model: str | None = None,
    attempted_models: list[str] | None = None,
    model_fallback_reason: str | None = None,
    grounding_mode: str,
    fallback_reason: str | None,
    api_mode: str,
) -> GroundedResponse:
    text = (getattr(response, "text", None) or "").strip()
    if not text:
        raise RuntimeError("Gemini returned an empty report")

    requested_model = requested_model or model
    attempted_models = attempted_models or [model]
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
        requested_model=requested_model,
        attempted_models=attempted_models,
        model_fallback_reason=model_fallback_reason,
        interaction_id=str(response_id) if response_id else None,
        citations=_dedupe_citations(citations),
        search_queries=list(dict.fromkeys(search_queries)),
        usage=_to_dict(usage_obj) if usage_obj is not None else None,
        grounding_mode=grounding_mode,
        grounding_fallback_reason=fallback_reason,
        api_mode=api_mode,
    )


def _model_candidates(primary: str, fallback_models: Sequence[str]) -> list[str]:
    ordered: list[str] = []
    for value in (primary, *fallback_models):
        candidate = str(value).strip()
        if candidate and candidate not in ordered:
            ordered.append(candidate)
    if not ordered:
        raise ValueError("at least one Gemini model is required")
    return ordered


def _model_fallback_reason(requested_model: str, selected_model: str) -> str | None:
    return None if requested_model == selected_model else "transient_model_unavailable"


def _merge_models(*groups: Sequence[str]) -> list[str]:
    out: list[str] = []
    for group in groups:
        for value in group:
            if value and value not in out:
                out.append(value)
    return out


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
        or "503 unavailable" in text
        or "high demand" in text
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
