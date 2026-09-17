from __future__ import annotations

import json
import re
from copy import deepcopy
from typing import Any, Sequence

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.IGNORECASE)


def _cves(*values: str | None) -> set[str]:
    found: set[str] = set()
    for value in values:
        for match in CVE_RE.findall(value or ""):
            found.add(match.upper())
    return found


def _model_candidates(primary: str, fallback_models: Sequence[str]) -> list[str]:
    out: list[str] = []
    for raw in (primary, *fallback_models):
        value = str(raw or "").strip()
        if value and value not in out:
            out.append(value)
    if not out:
        raise ValueError("at least one Gemini translation model is required")
    return out


def build_translation_prompt(payload: dict[str, Any]) -> str:
    items = []
    for item in payload.get("items", []) or []:
        items.append(
            {
                "id": item.get("id"),
                "title": item.get("title"),
                "summary": item.get("summary"),
                "related_cves": item.get("related_cves", []),
            }
        )

    return (
        "Translate the following verified cybersecurity event text into natural Traditional Chinese "
        "for readers in Taiwan. Return JSON only with the shape "
        '{"items":[{"id":"...","title_zh":"...","summary_zh":"..."}]}. '
        "Rules: translate only; do not add, infer, remove, or update facts. Preserve every CVE identifier "
        "exactly. Keep vendor, product, malware, threat actor, and protocol names in their official form when "
        "appropriate. Do not add remediation advice unless it exists in the source text. Keep title_zh concise. "
        "summary_zh should faithfully reflect only the supplied summary; if summary is empty, return an empty "
        "summary_zh. Return one item for every input id.\n\nINPUT:\n"
        + json.dumps(items, ensure_ascii=False, separators=(",", ":"))
    )


def merge_translations(
    payload: dict[str, Any],
    translated: dict[str, Any],
    *,
    model: str | None,
) -> tuple[dict[str, Any], int, list[str]]:
    result = deepcopy(payload)
    source_items = {str(item.get("id")): item for item in result.get("items", []) or [] if item.get("id")}
    translated_rows = translated.get("items") if isinstance(translated, dict) else None
    if not isinstance(translated_rows, list):
        raise ValueError("translation response must contain an items list")

    accepted = 0
    rejected: list[str] = []
    seen: set[str] = set()

    for row in translated_rows:
        if not isinstance(row, dict):
            continue
        item_id = str(row.get("id") or "")
        source = source_items.get(item_id)
        if not source or item_id in seen:
            continue
        seen.add(item_id)

        title_zh = row.get("title_zh")
        summary_zh = row.get("summary_zh")
        if not isinstance(title_zh, str) or not title_zh.strip():
            rejected.append(item_id)
            continue
        if not isinstance(summary_zh, str):
            rejected.append(item_id)
            continue
        if not (source.get("summary") or "").strip() and summary_zh.strip():
            rejected.append(item_id)
            continue

        source_cves = _cves(source.get("title"), source.get("summary"))
        translated_cves = _cves(title_zh, summary_zh)
        if source_cves != translated_cves:
            rejected.append(item_id)
            continue

        source["title_zh"] = title_zh.strip()
        source["summary_zh"] = summary_zh.strip()
        accepted += 1

    missing = [item_id for item_id in source_items if item_id not in seen]
    rejected.extend(missing)
    result["translation"] = {
        "language": "zh-Hant-TW",
        "status": "translated" if accepted else "source_only",
        "provider": "gemini" if accepted else None,
        "model": model if accepted else None,
        "translated_items": accepted,
        "total_items": len(source_items),
        "rejected_item_ids": sorted(set(rejected)),
        "fallback_reason": None if accepted else "no_valid_translations",
    }
    return result, accepted, sorted(set(rejected))


def _source_only(payload: dict[str, Any], reason: str) -> dict[str, Any]:
    result = deepcopy(payload)
    result["translation"] = {
        "language": "zh-Hant-TW",
        "status": "source_only",
        "provider": None,
        "model": None,
        "translated_items": 0,
        "total_items": len(result.get("items", []) or []),
        "rejected_item_ids": [],
        "fallback_reason": reason,
    }
    return result


def translate_events(
    payload: dict[str, Any],
    *,
    api_key: str | None,
    model: str,
    fallback_models: Sequence[str] = (),
    timeout_ms: int = 30_000,
) -> dict[str, Any]:
    items = payload.get("items", []) or []
    if not items:
        return _source_only(payload, "no_events")
    if not api_key:
        return _source_only(payload, "missing_api_key")

    from google import genai
    from google.genai import types

    prompt = build_translation_prompt(payload)
    client = genai.Client(api_key=api_key, http_options={"timeout": timeout_ms})
    last_error: Exception | None = None

    for candidate in _model_candidates(model, fallback_models):
        try:
            response = client.models.generate_content(
                model=candidate,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "You are a translation layer in a verified cybersecurity intelligence pipeline. "
                        "Translate faithfully into Traditional Chinese (Taiwan). Never introduce facts."
                    ),
                    response_mime_type="application/json",
                ),
            )
            raw = (getattr(response, "text", None) or "").strip()
            if not raw:
                raise RuntimeError("Gemini returned an empty translation response")
            translated = json.loads(raw)
            merged, accepted, _ = merge_translations(payload, translated, model=candidate)
            if accepted:
                return merged
            last_error = RuntimeError("Gemini returned no valid translations")
        except Exception as exc:  # translation is optional; preserve verified source text on failure
            last_error = exc

    reason = "translation_failed"
    if last_error is not None:
        name = last_error.__class__.__name__.lower()
        text = str(last_error).lower()
        if "429" in text or "quota" in text or "resource_exhausted" in text:
            reason = "translation_quota_unavailable"
        elif "timeout" in name or "timed out" in text:
            reason = "translation_timeout"
        elif "temperature" in text or "top_p" in text or "top_k" in text:
            reason = "translation_config_incompatible"
    return _source_only(payload, reason)
