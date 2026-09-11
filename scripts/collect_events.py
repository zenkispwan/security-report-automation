#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.collectors.events_gdelt import collect_gdelt_articles  # noqa: E402
from security_intel.collectors.events_rss import collect_feed_articles  # noqa: E402
from security_intel.collectors.nvd import NvdCollector  # noqa: E402
from security_intel.events import CVE_RE, build_event_outputs  # noqa: E402
from security_intel.http import HttpClient  # noqa: E402

PROFILE_PATH = ROOT / "config" / "event_profile.json"
INTELLIGENCE_PATH = ROOT / "data" / "intelligence.json"
STATE_PATH = ROOT / "data" / "event_state.json"
EVENTS_PATH = ROOT / "data" / "events.json"
DELTA_PATH = ROOT / "data" / "event_delta.json"
RAW_DIR = ROOT / "data" / "raw" / "events" / "latest"
MAX_EXTRA_NVD_VERIFICATIONS = 10


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect and cluster security events from the last 24 hours.")
    parser.add_argument("--lookback-hours", type=int, default=None)
    parser.add_argument("--max-events", type=int, default=20)
    args = parser.parse_args()

    profile = _load(PROFILE_PATH)
    if args.lookback_hours is not None:
        profile["lookback_hours"] = args.lookback_hours
    intelligence = _load(INTELLIGENCE_PATH)
    previous_state = _load(STATE_PATH) if STATE_PATH.exists() else None
    if previous_state and previous_state.get("baseline_ready") is not True:
        previous_state = None

    gdelt_rows, gdelt_errors = collect_gdelt_articles(
        profile.get("discovery_queries") or [],
        lookback_hours=int(profile.get("lookback_hours") or 24),
    )
    feed_rows, feed_errors = collect_feed_articles(profile.get("official_feeds") or [])
    articles = [*gdelt_rows, *feed_rows]

    source_health = {
        "gdelt": {
            "queries": len(profile.get("discovery_queries") or []),
            "articles": len(gdelt_rows),
            "errors": gdelt_errors,
        },
        "official_feeds": {
            "configured": len(profile.get("official_feeds") or []),
            "articles": len(feed_rows),
            "errors": feed_errors,
        },
    }
    if not articles and (gdelt_errors or feed_errors):
        print("ERROR: all event discovery sources returned no usable articles", file=sys.stderr)
        print(json.dumps(source_health, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2

    vulnerability_intel_cves = {
        str(row.get("cve")).upper()
        for row in intelligence.get("items") or []
        if isinstance(row, dict) and row.get("cve")
    }
    verified_cves = set(vulnerability_intel_cves)
    mentioned = sorted({
        cve.upper()
        for article in articles
        for cve in CVE_RE.findall(f"{article.get('title') or ''} {article.get('summary') or ''}")
    })
    extra_candidates = [x for x in mentioned if x not in verified_cves][:MAX_EXTRA_NVD_VERIFICATIONS]
    nvd_verified: list[str] = []
    nvd_errors: list[dict[str, str]] = []
    if extra_candidates:
        nvd = NvdCollector(HttpClient(timeout=45, retries=2), api_key=os.getenv("NVD_API_KEY"))
        for cve in extra_candidates:
            try:
                if nvd.fetch_cve(cve):
                    verified_cves.add(cve)
                    nvd_verified.append(cve)
            except Exception as exc:
                nvd_errors.append({"cve": cve, "error": f"{type(exc).__name__}: {exc}"})

    now = datetime.now(timezone.utc)
    state, events, event_delta = build_event_outputs(
        articles,
        profile,
        vulnerability_intelligence=intelligence,
        previous_state=previous_state,
        verified_cves=verified_cves,
        now=now,
        max_events=args.max_events,
    )
    state["baseline_ready"] = True
    events["sources"] = source_health
    events["cve_verification"] = {
        "mentioned": mentioned,
        "verified_from_vulnerability_intelligence": sorted(set(mentioned).intersection(vulnerability_intel_cves)),
        "verified_live_nvd": nvd_verified,
        "nvd_errors": nvd_errors,
        "verification_cap": MAX_EXTRA_NVD_VERIFICATIONS,
    }

    _write(STATE_PATH, state)
    _write(EVENTS_PATH, events)
    _write(DELTA_PATH, event_delta)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    _write(
        RAW_DIR / "discovery.json",
        {
            "generated_at": now.isoformat(),
            "profile": profile,
            "source_health": source_health,
            "articles": articles,
            "mentioned_cves": mentioned,
            "verified_cves": sorted(verified_cves),
            "nvd_errors": nvd_errors,
        },
    )

    print(json.dumps({
        "articles": len(articles),
        "clusters": events["summary"]["cluster_count"],
        "selected": events["summary"]["selected_count"],
        "event_delta_mode": event_delta.get("mode"),
        "new_notable": event_delta["summary"]["new_notable_count"],
        "p1": events["summary"]["p1"],
        "p2": events["summary"]["p2"],
        "p3": events["summary"]["p3"],
        "watch": events["summary"]["watch"],
    }, ensure_ascii=False))
    return 0


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
