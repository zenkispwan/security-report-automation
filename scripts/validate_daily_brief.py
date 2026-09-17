#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_SUMMARY_KEYS = {
    "event_count",
    "critical_events",
    "high_events",
    "active_exploitation_events",
    "ransomware_events",
    "linked_cve_count",
    "daily_change_count",
    "new_cve_count",
    "new_kev_count",
    "epss_increase_count",
    "exploitation_change_count",
    "new_critical_cve_count",
    "p1_cve_count",
}


def validate(payload: dict) -> None:
    if payload.get("schema_version") != "1.0-daily-security-brief":
        raise SystemExit("Invalid daily brief schema_version")
    if not payload.get("generated_at"):
        raise SystemExit("Daily brief generated_at is required")
    if payload.get("timezone") != "Asia/Taipei":
        raise SystemExit("Daily brief timezone must be Asia/Taipei")

    summary = payload.get("summary") or {}
    missing_summary = sorted(REQUIRED_SUMMARY_KEYS - set(summary))
    if missing_summary:
        raise SystemExit("Daily brief summary missing: " + ", ".join(missing_summary))

    for section in ("headline_events", "daily_changes", "priority_cves"):
        if not isinstance(payload.get(section), list):
            raise SystemExit(f"Daily brief {section} must be a list")

    for event in payload.get("headline_events", []):
        if not event.get("title") or not event.get("source_name") or not event.get("source_url"):
            raise SystemExit("Headline event missing source provenance")
        if not isinstance(event.get("related_cves", []), list):
            raise SystemExit("Headline event related_cves must be a list")

    for change in payload.get("daily_changes", []):
        if not change.get("cve"):
            raise SystemExit("Daily change missing CVE")
        if not isinstance(change.get("events"), list):
            raise SystemExit("Daily change events must be a list")
        facts = change.get("facts") or {}
        if facts.get("cve") != change.get("cve"):
            raise SystemExit("Daily change CVE does not match facts CVE")

    for row in payload.get("priority_cves", []):
        if not row.get("cve"):
            raise SystemExit("Priority CVE missing CVE identifier")
        if row.get("priority") not in {"P1", "P2", "P3", "WATCH"}:
            raise SystemExit(f"Unexpected priority for {row.get('cve')}: {row.get('priority')}")
        if not row.get("source_url"):
            raise SystemExit(f"Priority CVE missing source URL: {row.get('cve')}")

    trust = payload.get("trust_boundary") or {}
    if not trust.get("facts") or not trust.get("intelligence") or not trust.get("unknown_policy"):
        raise SystemExit("Daily brief trust boundary is incomplete")

    inputs = payload.get("inputs") or {}
    for name in ("events", "intelligence", "delta", "cve_zh"):
        source = inputs.get(name) or {}
        if not source.get("path") or not source.get("sha256"):
            raise SystemExit(f"Daily brief input provenance missing for {name}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate data/daily_brief.json")
    parser.add_argument("--path", default="data/daily_brief.json")
    args = parser.parse_args()
    path = Path(args.path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    validate(payload)
    print(
        "OK: daily security brief validated "
        f"events={payload['summary']['event_count']} "
        f"changes={payload['summary']['daily_change_count']} "
        f"priority_cves={len(payload['priority_cves'])}"
    )


if __name__ == "__main__":
    main()
