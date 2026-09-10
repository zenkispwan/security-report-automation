#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def load(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        raise SystemExit(f"Missing output: {path}")
    return json.loads(p.read_text(encoding="utf-8"))


def main() -> int:
    state = load("data/state.json")
    delta = load("data/delta.json")
    intelligence = load("data/intelligence.json")

    if state.get("tracked_count") != len(state.get("items", {})):
        raise SystemExit("state tracked_count mismatch")
    if state.get("tracked_count", 0) > 1000:
        raise SystemExit("state exceeds 1000 tracked CVEs")

    delta_items = delta.get("items", [])
    intel_items = intelligence.get("items", [])
    if len(delta_items) > 200:
        raise SystemExit("delta exceeds 200 included items")
    if len(intel_items) > 30:
        raise SystemExit("intelligence exceeds 30 selected items")

    seen = set()
    for row in intel_items:
        cve = row.get("cve")
        if not cve or cve in seen:
            raise SystemExit(f"invalid or duplicate intelligence CVE: {cve}")
        seen.add(cve)
        risk = row.get("risk", {})
        score = risk.get("score")
        if not isinstance(score, int) or not 0 <= score <= 100:
            raise SystemExit(f"invalid risk score for {cve}: {score}")
        if risk.get("priority") not in {"P1", "P2", "P3", "WATCH"}:
            raise SystemExit(f"invalid priority for {cve}")

    print(
        f"OK: state={state.get('tracked_count')} "
        f"delta={len(delta_items)} intelligence={len(intel_items)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
