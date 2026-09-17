#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.llm.cve_translation import translate_cve_batch  # noqa: E402


def load_json(path: Path) -> dict:
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def source_fingerprint(item: dict) -> str:
    facts = item.get("facts") or {}
    payload = {
        "cve": str(item.get("cve") or facts.get("cve") or "").upper(),
        "title": facts.get("title"),
        "description": facts.get("description"),
    }
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def main() -> None:
    intelligence_path = Path(os.getenv("INTELLIGENCE_PATH", "data/intelligence.json"))
    events_path = Path(os.getenv("EVENTS_PATH", "data/events.json"))
    output_path = Path(os.getenv("CVE_ZH_PATH", "data/cve_enrichment_zh.json"))

    intelligence = load_json(intelligence_path)
    events = load_json(events_path)
    previous = load_json(output_path)

    linked_cves = {
        str(cve).upper()
        for event in events.get("items", []) or []
        for cve in (event.get("related_cves") or [])
        if cve
    }
    selected = [
        item
        for item in intelligence.get("items", []) or []
        if str(item.get("cve") or (item.get("facts") or {}).get("cve") or "").upper() in linked_cves
    ]

    previous_by_cve = {
        str(item.get("cve") or "").upper(): item
        for item in previous.get("items", []) or []
        if item.get("cve")
    }
    cached_by_cve: dict[str, dict] = {}
    pending: list[dict] = []
    fingerprints: dict[str, str] = {}
    for item in selected:
        facts = item.get("facts") or {}
        cve = str(item.get("cve") or facts.get("cve") or "").upper()
        fingerprint = source_fingerprint(item)
        fingerprints[cve] = fingerprint
        old = previous_by_cve.get(cve)
        if (
            old
            and old.get("source_fingerprint") == fingerprint
            and old.get("title_zh")
            and "description_zh" in old
        ):
            cached_by_cve[cve] = old
        else:
            pending.append(item)

    model = os.getenv("GEMINI_CVE_TRANSLATION_MODEL") or os.getenv("GEMINI_TRANSLATION_MODEL") or "gemini-3.6-flash"
    fallback_raw = os.getenv("GEMINI_CVE_TRANSLATION_FALLBACK_MODELS", "")
    fallback_models = [value.strip() for value in fallback_raw.split(",") if value.strip()]
    timeout_ms = int(os.getenv("GEMINI_CVE_TRANSLATION_TIMEOUT_MS", "90000"))
    batch_size = max(1, int(os.getenv("CVE_TRANSLATION_BATCH_SIZE", "5")))

    translated_by_cve: dict[str, dict] = {}
    rejected: set[str] = set()
    reasons: list[str] = []
    models_used: list[str] = []

    for start in range(0, len(pending), batch_size):
        batch = pending[start : start + batch_size]
        result = translate_cve_batch(
            batch,
            api_key=os.getenv("GEMINI_API_KEY"),
            model=model,
            fallback_models=fallback_models,
            timeout_ms=max(timeout_ms, 1000),
        )
        for row in result.get("items") or []:
            cve = str(row.get("cve") or "").upper()
            row = dict(row)
            row["source_fingerprint"] = fingerprints.get(cve)
            translated_by_cve[cve] = row
        rejected.update(result.get("rejected_cves") or [])
        if result.get("model") and result.get("model") not in models_used:
            models_used.append(str(result["model"]))
        if result.get("fallback_reason"):
            reasons.append(str(result["fallback_reason"]))

    combined_by_cve = {**cached_by_cve, **translated_by_cve}
    combined = []
    for item in selected:
        facts = item.get("facts") or {}
        cve = str(item.get("cve") or facts.get("cve") or "").upper()
        if cve in combined_by_cve:
            combined.append(combined_by_cve[cve])

    translated_count = len(combined)
    attempted_count = len(pending)
    cached_count = len(cached_by_cve)
    output = {
        "schema_version": "1.1-cve-zh-enrichment",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "language": "zh-Hant-TW",
        "selection": {
            "rule": "Translate only CVEs referenced by current security events and present in intelligence.json; reuse translations only when source title/description fingerprints are unchanged.",
            "linked_cve_count": len(linked_cves),
            "matched_intelligence_cves": len(selected),
        },
        "items": combined,
        "translation": {
            "provider": "gemini" if translated_count else None,
            "model": models_used[-1] if models_used else None,
            "models_used": models_used,
            "cached_items": cached_count,
            "attempted_items": attempted_count,
            "newly_translated_items": len(translated_by_cve),
            "translated_items": translated_count,
            "pending_items": max(0, len(selected) - translated_count),
            "batch_size": batch_size,
            "rejected_cves": sorted(rejected),
            "fallback_reason": None if translated_count == len(selected) else ("partial_translation" if translated_count else (reasons[0] if reasons else None)),
            "batch_fallback_reasons": reasons,
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        "OK: CVE zh enrichment "
        f"translated={translated_count}/{len(selected)} "
        f"cached={cached_count} attempted={attempted_count} "
        f"batch_size={batch_size} model={output['translation']['model']} "
        f"fallback_reason={output['translation']['fallback_reason']}"
    )


if __name__ == "__main__":
    main()
