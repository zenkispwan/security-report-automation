#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


STATIC_FILES = {
    Path("web/index.html"): Path("index.html"),
    Path("web/styles.css"): Path("styles.css"),
    Path("web/app.js"): Path("app.js"),
    Path("data/intelligence.json"): Path("data/intelligence.json"),
    Path("data/delta.json"): Path("data/delta.json"),
    Path("reports/security_report_metadata.json"): Path("data/report_metadata.json"),
    Path("reports/security_report_latest.md"): Path("security_report_latest.md"),
}


def build(output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    missing = [str(source) for source in STATIC_FILES if not source.is_file()]
    if missing:
        raise SystemExit(f"Missing required web-report inputs: {', '.join(missing)}")

    for source, relative_target in STATIC_FILES.items():
        target = output / relative_target
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)

    (output / ".nojekyll").write_text("", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the static Security Intelligence web report.")
    parser.add_argument("--output", default="_site", help="Output directory (default: _site)")
    args = parser.parse_args()
    output = Path(args.output)
    build(output)
    print(f"OK: built static web report at {output}/index.html")


if __name__ == "__main__":
    main()
