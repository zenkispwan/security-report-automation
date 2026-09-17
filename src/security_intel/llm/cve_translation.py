from __future__ import annotations

import json
import re
from typing import Any, Sequence

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.IGNORECASE)

CVE_TRANSLATION_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "cve": {"type": "string"},
                    "title_zh": {"type": "string"},
                    "description_zh": {"type": "string"},
                },
                "required": ["cve", "title_zh", "description_zh"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["items"],
    "additionalProperties": False,
}


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
        raise ValueError("at least one Gemini CVE translation model is required")
    return out


def build_cve_translation_prompt(items: list[dict[str, Any]]) -> str:
    rows = []
    for item in items:
        facts = item.get("facts") or {}
        rows.append(
            {
                "cve": item.get("cve") or facts.get("cve"),
                "title": facts.get("title"),
                "description": facts.get("description"),
            }
        )
    return (
        "Translate the following verified CVE title and description into natural Traditional Chinese "
        "for cybersecurity readers in Taiwan. Translate only the supplied text. Do not add, infer, "
        "remove, or update facts. Keep vendor, product, protocol, malware, and standard names in their "
        "official form where appropriate. Preserve any CVE identifier that appears inside the supplied "
        "title or description exactly, and do not introduce a CVE identifier that is absent from those "
        "fields. If description is empty, return an empty description_zh. Return one row for every CVE.\n\n"
        + json.dumps(rows, ensure_ascii=False, separators=(",", ":"))
    )


def validate_cve_translations(
    source_items: list[dict[str, Any]],
    translated: dict[str, Any],
) -> tuple[list[dict[str, str]], list[str]]:
    sources: dict[str, dict[str, Any]] = {}
    for item in source_items:
        facts = item.get("facts") or {}
        cve = str(item.get("cve") or facts.get("cve") or "").upper()
        if cve:
            sources[cve] = item

    rows = translated.get("items") if isinstance(translated, dict) else None
    if not isinstance(rows, list):
        raise ValueError("CVE translation response must contain an items list")

    accepted: list[dict[str, str]] = []
    rejected: list[str] = []
    seen: set[str] = set()

    for row in rows:
        if not isinstance(row, dict):
            continue
        cve = str(row.get("cve") or "").upper()
        source = sources.get(cve)
        if not source or cve in seen:
            continue
        seen.add(cve)
        facts = source.get("facts") or {}
        title_zh = row.get("title_zh")
        description_zh = row.get("description_zh")
        if not isinstance(title_zh, str) or not title_zh.strip() or not isinstance(description_zh, str):
            rejected.append(cve)
            continue
        if not str(facts.get("description") or "").strip() and description_zh.strip():
            rejected.append(cve)
            continue
        source_cves = _cves(facts.get("title"), facts.get("description"))
        translated_cves = _cves(title_zh, description_zh)
        if source_cves != translated_cves:
            rejected.append(cve)
            continue
        accepted.append(
            {
                "cve": cve,
                "title_zh": title_zh.strip(),
                "description_zh": description_zh.strip(),
            }
        )

    for cve in sources:
        if cve not in seen:
            rejected.append(cve)
    return accepted, sorted(set(rejected))


def translate_cve_batch(
    items: list[dict[str, Any]],
    *,
    api_key: str | None,
    model: str,
    fallback_models: Sequence[str] = (),
    timeout_ms: int = 90_000,
) -> dict[str, Any]:
    if not items:
        return {"items": [], "model": None, "fallback_reason": "no_cves", "rejected_cves": []}
    if not api_key:
        return {"items": [], "model": None, "fallback_reason": "missing_api_key", "rejected_cves": []}

    from google import genai

    prompt = build_cve_translation_prompt(items)
    client = genai.Client(api_key=api_key, http_options={"timeout": timeout_ms})
    last_error: Exception | None = None
    last_rejected: list[str] = []

    for candidate in _model_candidates(model, fallback_models):
        try:
            interaction = client.interactions.create(
                model=candidate,
                input=prompt,
                system_instruction=(
                    "You are a translation layer in a verified CVE intelligence pipeline. "
                    "Translate faithfully into Traditional Chinese (Taiwan). Never introduce facts."
                ),
                generation_config={"thinking_level": "low"},
                response_format={
                    "type": "text",
                    "mime_type": "application/json",
                    "schema": CVE_TRANSLATION_RESPONSE_SCHEMA,
                },
                store=False,
            )
            raw = (getattr(interaction, "output_text", None) or "").strip()
            if not raw:
                raise RuntimeError("Gemini returned an empty CVE translation response")
            parsed = json.loads(raw)
            accepted, rejected = validate_cve_translations(items, parsed)
            if accepted:
                return {
                    "items": accepted,
                    "model": candidate,
                    "fallback_reason": None,
                    "rejected_cves": rejected,
                }
            last_rejected = rejected
            last_error = RuntimeError("Gemini returned no valid CVE translations")
        except Exception as exc:
            last_error = exc

    reason = "translation_failed"
    if last_error is not None:
        name = last_error.__class__.__name__.lower()
        text = str(last_error).lower()
        if "429" in text or "quota" in text or "resource_exhausted" in text:
            reason = "translation_quota_unavailable"
        elif "timeout" in name or "timed out" in text:
            reason = "translation_timeout"
        elif last_rejected:
            reason = "translation_validation_rejected"
    return {"items": [], "model": None, "fallback_reason": reason, "rejected_cves": last_rejected}
