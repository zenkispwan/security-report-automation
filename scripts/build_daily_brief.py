#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PRIORITY_ORDER = {"P1": 0, "P2": 1, "P3": 2, "WATCH": 3}


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def event_types(rows: list[dict]) -> Counter:
    counts: Counter = Counter()
    for row in rows:
        event_type = str(row.get("event_type") or "UNKNOWN")
        counts[event_type] += 1
    return counts


def delta_types(rows: list[dict]) -> Counter:
    counts: Counter = Counter()
    for row in rows:
        for event in row.get("events", []) or []:
            kind = str(event.get("type") or "UNKNOWN")
            counts[kind] += 1
    return counts


def cve_translation_map(payload: dict) -> dict[str, dict]:
    return {
        str(item.get("cve") or "").upper(): item
        for item in payload.get("items", []) or []
        if item.get("cve")
    }


def compact_cve(row: dict, translations: dict[str, dict]) -> dict:
    facts = row.get("facts") or {}
    risk = row.get("risk") or {}
    cve = str(row.get("cve") or facts.get("cve") or "").upper()
    translation = translations.get(cve) or {}
    return {
        "cve": cve,
        "vendor": facts.get("vendor"),
        "product": facts.get("product"),
        "title": facts.get("title"),
        "title_zh": translation.get("title_zh"),
        "description": facts.get("description"),
        "description_zh": translation.get("description_zh"),
        "priority": risk.get("priority"),
        "risk_score": risk.get("score"),
        "risk_reasons": risk.get("reasons") or [],
        "cvss": facts.get("cvss"),
        "epss": facts.get("epss"),
        "epss_percentile": facts.get("epss_percentile"),
        "cisa_kev": facts.get("cisa_kev"),
        "exploitation_status": facts.get("exploitation_status"),
        "published_time": facts.get("published_time"),
        "updated_time": facts.get("updated_time"),
        "source_url": facts.get("source_url"),
        "source_type": facts.get("source_type") or [],
        "provenance": facts.get("provenance") or {},
    }


def build_daily_brief(
    *,
    events: dict,
    intelligence: dict,
    delta: dict,
    cve_zh: dict,
    generated_at: str | None = None,
    headline_limit: int = 6,
    change_limit: int = 10,
    priority_cve_limit: int = 10,
) -> dict:
    event_rows = list(events.get("items", []) or [])
    intel_rows = list(intelligence.get("items", []) or [])
    delta_rows = list(delta.get("items", []) or [])
    translations = cve_translation_map(cve_zh)

    event_counts = event_types(event_rows)
    delta_counts = delta_types(delta_rows)
    priority_counts = Counter(
        str((row.get("risk") or {}).get("priority") or "UNKNOWN") for row in intel_rows
    )

    headline_events = []
    for item in event_rows[: max(0, headline_limit)]:
        headline_events.append(
            {
                "id": item.get("id"),
                "event_type": item.get("event_type"),
                "priority": item.get("priority"),
                "score": item.get("score"),
                "published_at": item.get("published_at"),
                "title": item.get("title"),
                "title_zh": item.get("title_zh"),
                "summary": item.get("summary"),
                "summary_zh": item.get("summary_zh"),
                "source_name": item.get("source_name"),
                "source_type": item.get("source_type"),
                "source_url": item.get("source_url"),
                "related_cves": item.get("related_cves") or [],
                "matched_intelligence_cves": item.get("matched_intelligence_cves") or [],
            }
        )

    daily_changes = []
    for row in delta_rows[: max(0, change_limit)]:
        daily_changes.append(
            {
                "cve": row.get("cve") or (row.get("facts") or {}).get("cve"),
                "events": row.get("events") or [],
                "risk": row.get("risk") or {},
                "facts": compact_cve(row, translations),
            }
        )

    sorted_intelligence = sorted(
        intel_rows,
        key=lambda row: (
            PRIORITY_ORDER.get(str((row.get("risk") or {}).get("priority") or "WATCH"), 9),
            -float((row.get("risk") or {}).get("score") or 0),
            str(row.get("cve") or ""),
        ),
    )
    priority_cves = [
        compact_cve(row, translations)
        for row in sorted_intelligence[: max(0, priority_cve_limit)]
    ]

    linked_cves = {
        str(cve).upper()
        for item in event_rows
        for cve in (item.get("related_cves") or [])
        if cve
    }
    translated_events = sum(
        1 for item in event_rows if item.get("title_zh") or item.get("summary_zh")
    )

    return {
        "schema_version": "1.0-daily-security-brief",
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "timezone": "Asia/Taipei",
        "purpose": "Single deterministic input model for the daily security event brief, website, Markdown report, and future email delivery.",
        "summary": {
            "event_count": len(event_rows),
            "critical_events": sum(1 for item in event_rows if item.get("priority") == "CRITICAL"),
            "high_events": sum(1 for item in event_rows if item.get("priority") == "HIGH"),
            "active_exploitation_events": event_counts.get("ACTIVE_EXPLOITATION", 0),
            "ransomware_events": event_counts.get("RANSOMWARE", 0),
            "supply_chain_events": event_counts.get("SUPPLY_CHAIN", 0),
            "data_breach_events": event_counts.get("DATA_BREACH", 0),
            "threat_activity_events": event_counts.get("THREAT_ACTIVITY", 0),
            "linked_cve_count": len(linked_cves),
            "translated_event_count": translated_events,
            "daily_change_count": len(delta_rows),
            "new_cve_count": delta_counts.get("NEW_CVE", 0),
            "new_kev_count": delta_counts.get("NEW_KEV", 0),
            "epss_increase_count": delta_counts.get("EPSS_INCREASED", 0),
            "exploitation_change_count": delta_counts.get("EXPLOITATION_CHANGED", 0),
            "ransomware_use_change_count": delta_counts.get("RANSOMWARE_USE_CHANGED", 0),
            "new_critical_cve_count": sum(
                1
                for row in delta_rows
                if any(event.get("type") == "NEW_CVE" for event in row.get("events", []) or [])
                and str((((row.get("facts") or {}).get("cvss") or {}).get("severity") or "")).upper() == "CRITICAL"
            ),
            "p1_cve_count": priority_counts.get("P1", 0),
            "p2_cve_count": priority_counts.get("P2", 0),
            "p3_cve_count": priority_counts.get("P3", 0),
            "watch_cve_count": priority_counts.get("WATCH", 0),
        },
        "headline_events": headline_events,
        "daily_changes": daily_changes,
        "priority_cves": priority_cves,
        "source_health": {
            "event_sources": events.get("sources") or [],
            "successful_event_sources": (events.get("summary") or {}).get("successful_sources"),
            "event_source_errors": (events.get("summary") or {}).get("source_errors") or [],
            "event_translation": events.get("translation") or {},
            "cve_translation": cve_zh.get("translation") or {},
        },
        "trust_boundary": {
            "facts": "CISA KEV, NVD, FIRST EPSS, vendor/security news feeds and deterministic collectors provide facts.",
            "intelligence": "LLM may translate, summarize and analyze only collected source text and verified facts; it must not invent CVE, CVSS, EPSS, KEV, exploitation status, dates or affected versions.",
            "unknown_policy": "Missing or unsupported facts remain unconfirmed rather than inferred.",
        },
        "outputs": {
            "website": "/",
            "events": "/events.html",
            "markdown_report": "/security_report_latest.md",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the deterministic daily security intelligence brief model.")
    parser.add_argument("--events", default="data/events.json")
    parser.add_argument("--intelligence", default="data/intelligence.json")
    parser.add_argument("--delta", default="data/delta.json")
    parser.add_argument("--cve-zh", default="data/cve_enrichment_zh.json")
    parser.add_argument("--output", default="data/daily_brief.json")
    parser.add_argument("--headline-limit", type=int, default=6)
    parser.add_argument("--change-limit", type=int, default=10)
    parser.add_argument("--priority-cve-limit", type=int, default=10)
    args = parser.parse_args()

    input_paths = {
        "events": Path(args.events),
        "intelligence": Path(args.intelligence),
        "delta": Path(args.delta),
        "cve_zh": Path(args.cve_zh),
    }
    payload = build_daily_brief(
        events=load_json(input_paths["events"]),
        intelligence=load_json(input_paths["intelligence"]),
        delta=load_json(input_paths["delta"]),
        cve_zh=load_json(input_paths["cve_zh"]),
        headline_limit=max(0, args.headline_limit),
        change_limit=max(0, args.change_limit),
        priority_cve_limit=max(0, args.priority_cve_limit),
    )
    payload["inputs"] = {
        name: {
            "path": str(path),
            "sha256": sha256_file(path),
            "generated_at": load_json(path).get("generated_at"),
        }
        for name, path in input_paths.items()
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        "OK: daily security brief "
        f"events={payload['summary']['event_count']} "
        f"changes={payload['summary']['daily_change_count']} "
        f"priority_cves={len(payload['priority_cves'])} "
        f"output={output}"
    )


if __name__ == "__main__":
    main()
