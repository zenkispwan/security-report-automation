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


def _is_translated(item: dict) -> bool:
    if not str(item.get("title_zh") or "").strip():
        return False
    source_summary = str(item.get("summary") or "").strip()
    if not source_summary:
        return "summary_zh" in item
    return isinstance(item.get("summary_zh"), str) and bool(str(item.get("summary_zh") or "").strip())


def _merge_batch(result: dict, translated_batch: dict) -> int:
    translated_by_id = {
        str(item.get("id")): item
        for item in translated_batch.get("items", []) or []
        if item.get("id") and (item.get("title_zh") or item.get("summary_zh"))
    }
    merged = 0
    for item in result.get("items", []) or []:
        translated = translated_by_id.get(str(item.get("id") or ""))
        if not translated:
            continue
        if translated.get("title_zh"):
            item["title_zh"] = translated["title_zh"]
        if translated.get("summary_zh") is not None:
            item["summary_zh"] = translated["summary_zh"]
        if _is_translated(item):
            merged += 1
    return merged


def enrich_in_batches(
    payload: dict,
    *,
    api_key: str | None,
    model: str,
    fallback_models: list[str],
    timeout_ms: int,
    max_items: int,
    batch_size: int,
) -> dict:
    result = deepcopy(payload)
    source_items = payload.get("items", []) or []
    pending_items = [item for item in source_items if not _is_translated(item)]
    selected_items = pending_items if max_items <= 0 else pending_items[:max_items]

    cached_items = len(source_items) - len(pending_items)
    attempted = 0
    translated_total = cached_items
    rejected_ids: set[str] = set()
    fallback_reasons: list[str] = []
    models_used: list[str] = []

    for start in range(0, len(selected_items), batch_size):
        batch_items = selected_items[start : start + batch_size]
        batch_payload = deepcopy(payload)
        batch_payload["items"] = batch_items
        translated_batch = translate_events(
            batch_payload,
            api_key=api_key,
            model=model,
            fallback_models=fallback_models,
            timeout_ms=max(timeout_ms, 1000),
        )
        attempted += len(batch_items)
        translated_total += _merge_batch(result, translated_batch)

        meta = translated_batch.get("translation") or {}
        rejected_ids.update(meta.get("rejected_item_ids") or [])
        if meta.get("model") and meta.get("model") not in models_used:
            models_used.append(str(meta["model"]))
        if meta.get("fallback_reason"):
            fallback_reasons.append(str(meta["fallback_reason"]))

    total_items = len(source_items)
    if translated_total == total_items and total_items:
        status = "translated"
        fallback_reason = None
    elif translated_total:
        status = "partial"
        fallback_reason = "partial_translation" if selected_items else None
    else:
        status = "source_only"
        fallback_reason = fallback_reasons[0] if fallback_reasons else ("no_events" if not source_items else "translation_failed")

    result["translation"] = {
        "language": "zh-Hant-TW",
        "status": status,
        "provider": "gemini" if translated_total else None,
        "model": models_used[-1] if models_used else None,
        "models_used": models_used,
        "translated_items": translated_total,
        "cached_items": cached_items,
        "pending_items": max(0, total_items - translated_total),
        "total_items": total_items,
        "attempted_items": attempted,
        "batch_size": batch_size,
        "rejected_item_ids": sorted(rejected_ids),
        "fallback_reason": fallback_reason,
        "batch_fallback_reasons": fallback_reasons,
    }
    return result


def main() -> None:
    path = Path(os.getenv("EVENTS_PATH", "data/events.json"))
    payload = json.loads(path.read_text(encoding="utf-8"))

    model = os.getenv("GEMINI_TRANSLATION_MODEL") or "gemini-3.6-flash"
    fallback_raw = os.getenv("GEMINI_TRANSLATION_FALLBACK_MODELS", "")
    fallback_models = [value.strip() for value in fallback_raw.split(",") if value.strip()]
    timeout_ms = int(os.getenv("GEMINI_TRANSLATION_TIMEOUT_MS", "90000"))
    max_items = int(os.getenv("EVENT_TRANSLATION_MAX_ITEMS", "0"))
    batch_size = max(1, int(os.getenv("EVENT_TRANSLATION_BATCH_SIZE", "5")))

    enriched = enrich_in_batches(
        payload,
        api_key=os.getenv("GEMINI_API_KEY"),
        model=model,
        fallback_models=fallback_models,
        timeout_ms=timeout_ms,
        max_items=max_items,
        batch_size=batch_size,
    )
    path.write_text(json.dumps(enriched, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    meta = enriched.get("translation") or {}
    print(
        "OK: event translation "
        f"status={meta.get('status')} "
        f"translated={meta.get('translated_items', 0)}/{meta.get('total_items', 0)} "
        f"cached={meta.get('cached_items', 0)} "
        f"attempted={meta.get('attempted_items', 0)} "
        f"batch_size={meta.get('batch_size')} "
        f"model={meta.get('model')} "
        f"fallback_reason={meta.get('fallback_reason')}"
    )


if __name__ == "__main__":
    main()
