#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse

CVE_RE = re.compile(r"^CVE-\d{4}-\d{4,7}$")
ALLOWED_TYPES = {
    "RANSOMWARE",
    "ACTIVE_EXPLOITATION",
    "SUPPLY_CHAIN",
    "DATA_BREACH",
    "THREAT_ACTIVITY",
    "VULNERABILITY_NEWS",
}
ALLOWED_PRIORITIES = {"CRITICAL", "HIGH", "MEDIUM"}


def validate(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != "1.1-security-events":
        raise SystemExit("Unexpected security events schema_version")
    if not isinstance(payload.get("items"), list):
        raise SystemExit("Security events items must be a list")

    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    for index, item in enumerate(payload["items"]):
        item_id = item.get("id")
        if not item_id or item_id in seen_ids:
            raise SystemExit(f"Invalid/duplicate event id at index {index}")
        seen_ids.add(item_id)

        if item.get("event_type") not in ALLOWED_TYPES:
            raise SystemExit(f"Invalid event_type at index {index}: {item.get('event_type')}")
        if item.get("priority") not in ALLOWED_PRIORITIES:
            raise SystemExit(f"Invalid priority at index {index}: {item.get('priority')}")
        if not item.get("title") or not item.get("source_name"):
            raise SystemExit(f"Missing title/source at index {index}")

        url = item.get("source_url")
        parsed = urlparse(url or "")
        if parsed.scheme != "https" or not parsed.netloc:
            raise SystemExit(f"Invalid source_url at index {index}")
        if url in seen_urls:
            raise SystemExit(f"Duplicate source_url at index {index}")
        seen_urls.add(url)

        cves = item.get("related_cves", [])
        if not isinstance(cves, list):
            raise SystemExit(f"related_cves must be a list at index {index}")
        for cve in cves:
            if not CVE_RE.match(str(cve)):
                raise SystemExit(f"Invalid CVE at index {index}: {cve}")

    print(
        "OK: security events "
        f"items={len(payload['items'])} "
        f"generated_at={payload.get('generated_at')}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate data/events.json")
    parser.add_argument("path", nargs="?", default="data/events.json")
    args = parser.parse_args()
    validate(Path(args.path))


if __name__ == "__main__":
    main()
