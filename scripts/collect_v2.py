#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.pipeline import CollectionPipeline  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect official vulnerability intelligence.")
    parser.add_argument("--lookback-hours", type=int, default=48)
    parser.add_argument("--output", default="data/latest.json")
    parser.add_argument("--raw-dir", default="data/raw/latest")
    args = parser.parse_args()

    result = CollectionPipeline(
        lookback_hours=args.lookback_hours,
        output_path=args.output,
        raw_dir=args.raw_dir,
    ).run()
    print(json.dumps({"generated_at": result["generated_at"], "summary": result["summary"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
