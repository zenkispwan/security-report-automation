#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.llm.event_translation import translate_events  # noqa: E402


def _merge_translation_subset(
    payload: dict,
    translated_subset: dict,
    *,
    attempted_items: int,
) -> dict:
    result = deepcopy(payload)
    translated_by_id = {
        str(item.get("id")): item
        for item in translated_subset.get("items", []) or []
        if item.get("id") and (item.get("title_zh") or item.get("summary_zh"))
    }

    for item in result.get("items", []) or []:
        translated = translated_by_id.get(str(item.get("id") or ""))
        if not translated:
            continue
        if translated.get("title_zh"):
            item["title_zh"] = translated["title_zh"]
        if translated.get("summary_zh") is not None:
            item["summary_zh"] = translated["summary_zh"]

    meta = deepcopy(translated_subset.get("translation") or {})
    translated_items = int(meta.get("translated_items") or 0)
    total_items = len(result.get("items", []) or [])
    meta["attempted_items"] = attempted_items
    meta["total_items"] = total_items
    if translated_items and translated_items < total_items:
        meta["status"] = "partial"
    result["translation"] = meta
    return result


def main() -> None:
    path = Path(os.getenv("EVENTS_PATH", "data/events.json"))
    payload = json.loads(path.read_text(encoding="utf-8"))

    model = os.getenv("GEMINI_TRANSLATION_MODEL") or os.getenv("GEMINI_MODEL") or "gemini-3.8-flash"
    # Translation is optional and latency-sensitive. Do not inherit the report's
    # multi-model fallback chain unless a dedicated translation fallback list is
    # explicitly configured.
    fallback_raw = os.getenv("GEMINI_TRANSLATION_FALLBACK_MODELS", "")
    fallback_models = [value.strip() for value in fallback_raw.split(",") if value.strip()]
    timeout_ms = int(os.getenv("GEMINI_TRANSLATION_TIMEOUT_MS", "90000"))
    max_items = max(1, int(os.getenv("EVENT_TRANSLATION_MAX_ITEMS", "6")))

    source_items = payload.get("items", []) or []
    selected_items = source_items[:max_items]
    translation_payload = deepcopy(payload)
    translation_payload["items"] = selected_items

    translated_subset = translate_events(
        translation_payload,
        api_key=os.getenv("GEMINI_API_KEY"),
        model=model,
        fallback_models=fallback_models,
        timeout_ms=max(timeout_ms, 1000),
    )
    enriched = _merge_translation_subset(
        payload,
        translated_subset,
        attempted_items=len(selected_items),
    )
    path.write_text(json.dumps(enriched, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    meta = enriched.get("translation") or {}
    print(
        "OK: event translation "
        f"status={meta.get('status')} "
        f"translated={meta.get('translated_items', 0)}/{meta.get('total_items', 0)} "
        f"attempted={meta.get('attempted_items', 0)} "
        f"model={meta.get('model')} "
        f"fallback_reason={meta.get('fallback_reason')}"
    )


if __name__ == "__main__":
    main()
