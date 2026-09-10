#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.collectors.epss import EpssCollector  # noqa: E402
from security_intel.http import HttpClient  # noqa: E402
from security_intel.intelligence import build_outputs, state_epss_watch_ids  # noqa: E402


def read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build deterministic daily security intelligence delta.")
    parser.add_argument("--current", default="data/latest.json")
    parser.add_argument("--state", default="data/state.json")
    parser.add_argument("--previous-snapshot", default="data/previous.json")
    parser.add_argument("--delta-output", default="data/delta.json")
    parser.add_argument("--intelligence-output", default="data/intelligence.json")
    parser.add_argument("--state-output", default="data/state.json")
    parser.add_argument("--raw-dir", default="data/raw/latest")
    args = parser.parse_args()

    current = read_json(Path(args.current))
    if not current:
        raise SystemExit(f"Current snapshot not found: {args.current}")

    previous_state = read_json(Path(args.state))
    previous_snapshot = read_json(Path(args.previous_snapshot))

    refreshed_epss: dict[str, dict[str, Any]] = {}
    watch_ids = state_epss_watch_ids(previous_state, current)
    if watch_ids:
        refreshed_epss, raw = EpssCollector(HttpClient()).collect(watch_ids)
        write_json(Path(args.raw_dir) / "epss_watchlist.json", {
            "requested_count": len(watch_ids),
            "matched_count": len(refreshed_epss),
            "batches": raw,
        })

    state, delta, intelligence = build_outputs(
        current,
        previous_state=previous_state,
        previous_snapshot=previous_snapshot,
        refreshed_epss=refreshed_epss,
    )

    write_json(Path(args.state_output), state)
    write_json(Path(args.delta_output), delta)
    write_json(Path(args.intelligence_output), intelligence)

    print(json.dumps({
        "baseline": delta["baseline"],
        "delta_summary": delta["summary"],
        "intelligence_summary": intelligence["summary"],
        "selected": intelligence["selection"],
        "tracked_state": state["tracked_count"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
