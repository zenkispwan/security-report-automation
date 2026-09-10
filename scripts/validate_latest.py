#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = {
    "cve", "vendor", "product", "title", "description", "cvss",
    "epss", "epss_percentile", "cisa_kev", "exploitation_status",
    "published_time", "updated_time", "collected_time", "source_url", "source_type",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="data/latest.json")
    args = parser.parse_args()

    payload = json.loads(Path(args.path).read_text(encoding="utf-8"))
    if payload.get("schema_version") != "2.0":
        raise ValueError("schema_version must be 2.0")
    items = payload.get("items")
    if not isinstance(items, list):
        raise ValueError("items must be a list")

    seen = set()
    for i, item in enumerate(items):
        missing = REQUIRED - set(item)
        if missing:
            raise ValueError(f"items[{i}] missing {sorted(missing)}")
        cve = item["cve"]
        if not isinstance(cve, str) or not cve.startswith("CVE-"):
            raise ValueError(f"invalid CVE at items[{i}]")
        if cve in seen:
            raise ValueError(f"duplicate CVE: {cve}")
        seen.add(cve)
        if item["epss"] is not None and not 0 <= item["epss"] <= 1:
            raise ValueError(f"{cve}: invalid EPSS")
        if item["epss_percentile"] is not None and not 0 <= item["epss_percentile"] <= 1:
            raise ValueError(f"{cve}: invalid EPSS percentile")
        if item["cisa_kev"].get("listed") and item["exploitation_status"].get("status") != "known_exploited":
            raise ValueError(f"{cve}: KEV must be known_exploited")

    print(f"OK: {len(items)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
