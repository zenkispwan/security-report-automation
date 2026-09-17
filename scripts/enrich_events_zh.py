#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.llm.event_translation import translate_events  # noqa: E402


def main() -> None:
    path = Path(os.getenv("EVENTS_PATH", "data/events.json"))
    payload = json.loads(path.read_text(encoding="utf-8"))

    model = os.getenv("GEMINI_TRANSLATION_MODEL") or os.getenv("GEMINI_MODEL") or "gemini-3.8-flash"
    fallback_raw = os.getenv("GEMINI_TRANSLATION_FALLBACK_MODELS") or os.getenv("GEMINI_FALLBACK_MODELS") or ""
    fallback_models = [value.strip() for value in fallback_raw.split(",") if value.strip()]
    timeout_ms = int(os.getenv("GEMINI_TRANSLATION_TIMEOUT_MS", "30000"))

    enriched = translate_events(
        payload,
        api_key=os.getenv("GEMINI_API_KEY"),
        model=model,
        fallback_models=fallback_models,
        timeout_ms=max(timeout_ms, 1000),
    )
    path.write_text(json.dumps(enriched, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    meta = enriched.get("translation") or {}
    print(
        "OK: event translation "
        f"status={meta.get('status')} "
        f"translated={meta.get('translated_items', 0)}/{meta.get('total_items', 0)} "
        f"model={meta.get('model')} "
        f"fallback_reason={meta.get('fallback_reason')}"
    )


if __name__ == "__main__":
    main()
