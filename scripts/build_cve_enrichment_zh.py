#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.llm.cve_translation import translate_cve_batch  # noqa: E402


def main() -> None:
    intelligence_path = Path(os.getenv("INTELLIGENCE_PATH", "data/intelligence.json"))
    events_path = Path(os.getenv("EVENTS_PATH", "data/events.json"))
    output_path = Path(os.getenv("CVE_ZH_PATH", "data/cve_enrichment_zh.json"))

    intelligence = json.loads(intelligence_path.read_text(encoding="utf-8"))
    events = json.loads(events_path.read_text(encoding="utf-8"))

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

    model = os.getenv("GEMINI_CVE_TRANSLATION_MODEL") or os.getenv("GEMINI_TRANSLATION_MODEL") or "gemini-3.6-flash"
    fallback_raw = os.getenv("GEMINI_CVE_TRANSLATION_FALLBACK_MODELS", "")
    fallback_models = [value.strip() for value in fallback_raw.split(",") if value.strip()]
    timeout_ms = int(os.getenv("GEMINI_CVE_TRANSLATION_TIMEOUT_MS", "90000"))
    batch_size = max(1, int(os.getenv("CVE_TRANSLATION_BATCH_SIZE", "5")))

    translated: list[dict] = []
    rejected: set[str] = set()
    reasons: list[str] = []
    models_used: list[str] = []

    for start in range(0, len(selected), batch_size):
        batch = selected[start : start + batch_size]
        result = translate_cve_batch(
            batch,
            api_key=os.getenv("GEMINI_API_KEY"),
            model=model,
            fallback_models=fallback_models,
            timeout_ms=max(timeout_ms, 1000),
        )
        translated.extend(result.get("items") or [])
        rejected.update(result.get("rejected_cves") or [])
        if result.get("model") and result.get("model") not in models_used:
            models_used.append(str(result["model"]))
        if result.get("fallback_reason"):
            reasons.append(str(result["fallback_reason"]))

    output = {
        "schema_version": "1.0-cve-zh-enrichment",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "language": "zh-Hant-TW",
        "selection": {
            "rule": "Translate only CVEs referenced by current security events and present in intelligence.json.",
            "linked_cve_count": len(linked_cves),
            "matched_intelligence_cves": len(selected),
        },
        "items": translated,
        "translation": {
            "provider": "gemini" if translated else None,
            "model": models_used[-1] if models_used else None,
            "models_used": models_used,
            "attempted_items": len(selected),
            "translated_items": len(translated),
            "batch_size": batch_size,
            "rejected_cves": sorted(rejected),
            "fallback_reason": None if len(translated) == len(selected) else ("partial_translation" if translated else (reasons[0] if reasons else None)),
            "batch_fallback_reasons": reasons,
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        "OK: CVE zh enrichment "
        f"translated={len(translated)}/{len(selected)} "
        f"batch_size={batch_size} model={output['translation']['model']} "
        f"fallback_reason={output['translation']['fallback_reason']}"
    )


if __name__ == "__main__":
    main()
