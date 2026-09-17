#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.collectors.news import DEFAULT_NEWS_SOURCES, NewsCollector  # noqa: E402


def load_json(path: Path) -> dict:
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def tracked_cves(intelligence: dict, delta: dict) -> set[str]:
    values: set[str] = set()
    for payload in (intelligence, delta):
        for item in payload.get("items", []) or []:
            cve = item.get("cve") or (item.get("facts") or {}).get("cve")
            if cve:
                values.add(str(cve).upper())
    return values


def preserve_event_translations(previous: dict, current_items: list[dict]) -> int:
    previous_by_id = {
        str(item.get("id")): item
        for item in previous.get("items", []) or []
        if item.get("id")
    }
    preserved = 0
    for item in current_items:
        old = previous_by_id.get(str(item.get("id") or ""))
        if not old:
            continue
        # Only reuse a translation when the exact source text is unchanged.
        if old.get("title") != item.get("title") or old.get("summary") != item.get("summary"):
            continue
        if old.get("title_zh"):
            item["title_zh"] = old["title_zh"]
        if "summary_zh" in old:
            item["summary_zh"] = old.get("summary_zh")
        if item.get("title_zh") and (not item.get("summary") or "summary_zh" in item):
            preserved += 1
    return preserved


def build_events(
    *,
    output: Path,
    intelligence_path: Path,
    delta_path: Path,
    window_days: int,
    max_items: int,
) -> dict:
    intelligence = load_json(intelligence_path)
    delta = load_json(delta_path)
    previous = load_json(output)
    tracked = tracked_cves(intelligence, delta)

    collector = NewsCollector()
    result = collector.collect(
        sources=DEFAULT_NEWS_SOURCES,
        window_days=window_days,
        max_items=max_items,
        tracked_cves=tracked,
    )

    if result.successful_sources == 0 and output.is_file():
        print("WARNING: all news sources failed; preserving previous data/events.json")
        return previous

    current_items = result.items
    preserved_translations = preserve_event_translations(previous, current_items)
    payload = {
        "schema_version": "1.1-security-events",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "selection": {
            "window_days": window_days,
            "max_items": max_items,
            "rule": "Homepage events come from current RSS/advisory sources. CVEs are shown only when the source article/advisory mentions them.",
            "tracked_cve_count": len(tracked),
        },
        "sources": [
            {
                "name": source["name"],
                "url": source["url"],
                "source_type": source["source_type"],
            }
            for source in DEFAULT_NEWS_SOURCES
        ],
        "summary": {
            "fetched_entries": result.fetched_entries,
            "included_items": len(current_items),
            "linked_cve_items": sum(1 for item in current_items if item.get("related_cves")),
            "matched_intelligence_items": sum(1 for item in current_items if item.get("matched_intelligence_cves")),
            "successful_sources": result.successful_sources,
            "source_errors": result.source_errors,
            "preserved_translations": preserved_translations,
        },
        "items": current_items,
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the current security news/events feed.")
    parser.add_argument("--output", default="data/events.json")
    parser.add_argument("--intelligence", default="data/intelligence.json")
    parser.add_argument("--delta", default="data/delta.json")
    parser.add_argument("--window-days", type=int, default=7)
    parser.add_argument("--max-items", type=int, default=20)
    args = parser.parse_args()

    payload = build_events(
        output=Path(args.output),
        intelligence_path=Path(args.intelligence),
        delta_path=Path(args.delta),
        window_days=max(1, args.window_days),
        max_items=max(1, args.max_items),
    )
    print(
        "OK: security events "
        f"items={len(payload.get('items', []))} "
        f"preserved_zh={(payload.get('summary') or {}).get('preserved_translations', 0)} "
        f"generated_at={payload.get('generated_at')}"
    )


if __name__ == "__main__":
    main()
