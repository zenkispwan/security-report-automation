#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVENTS_PATH = ROOT / "data" / "events.json"
DELTA_PATH = ROOT / "data" / "event_delta.json"
STATE_PATH = ROOT / "data" / "event_state.json"


def main() -> int:
    events = _load(EVENTS_PATH)
    delta = _load(DELTA_PATH)
    state = _load(STATE_PATH)

    if events.get("schema_version") != "2.5-events":
        return _fail("unexpected events schema")
    if delta.get("schema_version") != "2.5-event-delta":
        return _fail("unexpected event delta schema")
    if state.get("schema_version") != "2.5-event-state":
        return _fail("unexpected event state schema")
    if not isinstance(events.get("items"), list):
        return _fail("events.items must be a list")
    if not isinstance(delta.get("items"), list):
        return _fail("event_delta.items must be a list")
    if not isinstance(state.get("items"), dict):
        return _fail("event_state.items must be an object")

    event_ids: set[str] = set()
    for event in events["items"]:
        event_id = event.get("event_id")
        if not event_id or event_id in event_ids:
            return _fail(f"invalid or duplicate event_id: {event_id!r}")
        event_ids.add(event_id)
        if event.get("priority") not in {"P1", "P2", "P3", "WATCH"}:
            return _fail(f"invalid priority for {event_id}")
        if not isinstance(event.get("score"), int) or not 0 <= event["score"] <= 100:
            return _fail(f"invalid score for {event_id}")
        if not event.get("title") or not event.get("event_type"):
            return _fail(f"missing title/event_type for {event_id}")
        sources = event.get("sources") or []
        if not sources:
            return _fail(f"event has no sources: {event_id}")
        for source in sources:
            url = str(source.get("url") or "")
            if not url.startswith("https://"):
                return _fail(f"non-HTTPS source for {event_id}: {url}")
            if not _valid_time(source.get("published_time")):
                return _fail(f"source missing parseable published_time for {event_id}")

        verification = event.get("verification") or {}
        status = verification.get("status")
        authorities = {x.get("authority") for x in sources}
        trusted_domains = {
            x.get("domain") for x in sources
            if x.get("authority") in {"official", "trusted_media"} and x.get("domain")
        }
        if status == "official_confirmed" and "official" not in authorities:
            return _fail(f"official_confirmed without official source: {event_id}")
        if status == "corroborated" and len(trusted_domains) < 2:
            return _fail(f"corroborated without two trusted domains: {event_id}")
        if status not in {"official_confirmed", "corroborated", "single_trusted_source", "discovery_only"}:
            return _fail(f"invalid verification status: {event_id}")

        confirmed = set(event.get("confirmed_cves") or [])
        unverified = set(event.get("unverified_cve_mentions") or [])
        if confirmed.intersection(unverified):
            return _fail(f"CVE cannot be both confirmed and unverified: {event_id}")
        linked = {x.get("cve") for x in event.get("linked_vulnerabilities") or []}
        if not linked.issubset(confirmed):
            return _fail(f"linked vulnerability is not a confirmed CVE: {event_id}")

    delta_ids = {x.get("event_id") for x in delta["items"]}
    if not delta_ids.issubset(event_ids):
        return _fail("event_delta contains event outside selected events")
    for event in delta["items"]:
        if not event.get("is_new") or event.get("priority") == "WATCH":
            return _fail(f"event_delta contains non-new/non-notable item: {event.get('event_id')}")

    summary = events.get("summary") or {}
    if summary.get("selected_count") != len(events["items"]):
        return _fail("selected_count does not match items")
    if (delta.get("summary") or {}).get("new_notable_count") != len(delta["items"]):
        return _fail("new_notable_count does not match event delta items")

    print(
        "OK: events "
        f"articles={summary.get('eligible_articles')} "
        f"clusters={summary.get('cluster_count')} "
        f"selected={len(events['items'])} "
        f"new_notable={len(delta['items'])}"
    )
    return 0


def _valid_time(value: object) -> bool:
    if not value:
        return False
    try:
        datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def _load(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
