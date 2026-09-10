#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


COPIES = {
    Path("data/intelligence.json"): Path("data/intelligence.json"),
    Path("data/delta.json"): Path("data/delta.json"),
    Path("reports/security_report_metadata.json"): Path("data/report_metadata.json"),
    Path("reports/security_report_latest.md"): Path("security_report_latest.md"),
    Path("web/_headers"): Path("_headers"),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path) -> None:
    required = [root / "index.html", root / "styles.css", root / "app.js", root / "_headers"]
    required += [root / target for target in COPIES.values()]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing built web-report files: {', '.join(missing)}")

    for source, relative_target in COPIES.items():
        built = root / relative_target
        if digest(source) != digest(built):
            raise SystemExit(f"Built file differs from verified source: {relative_target}")

    intelligence = json.loads((root / "data/intelligence.json").read_text(encoding="utf-8"))
    delta = json.loads((root / "data/delta.json").read_text(encoding="utf-8"))
    metadata = json.loads((root / "data/report_metadata.json").read_text(encoding="utf-8"))

    if not isinstance(intelligence.get("items"), list):
        raise SystemExit("Invalid web intelligence payload")
    if not isinstance(delta.get("items"), list):
        raise SystemExit("Invalid web delta payload")
    if not metadata.get("generated_at"):
        raise SystemExit("Missing report metadata generated_at")

    index = (root / "index.html").read_text(encoding="utf-8")
    app = (root / "app.js").read_text(encoding="utf-8")
    headers = (root / "_headers").read_text(encoding="utf-8")
    if "./styles.css" not in index or "./app.js" not in index:
        raise SystemExit("Static shell is missing local assets")
    if "./data/intelligence.json" not in app or "./data/delta.json" not in app or "./data/report_metadata.json" not in app:
        raise SystemExit("Web app is not wired to verified compact inputs")
    if "https://" in index.replace("https://github.com/zenkispwan/security-report-automation", ""):
        raise SystemExit("Unexpected external resource in web shell")
    if "<script src=\"http" in index or "<link rel=\"stylesheet\" href=\"http" in index:
        raise SystemExit("External executable/style dependency is not allowed")
    if "Content-Security-Policy:" not in headers or "Cache-Control: no-cache" not in headers:
        raise SystemExit("Cloudflare Pages security/cache headers are missing")

    print(
        "OK: Cloudflare Pages web report "
        f"intelligence={len(intelligence['items'])} "
        f"delta={len(delta['items'])} "
        f"renderer={metadata.get('renderer')} "
        f"llm_body_used={metadata.get('llm_body_used')}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the static Security Intelligence web report.")
    parser.add_argument("--root", default="_site", help="Built site root (default: _site)")
    args = parser.parse_args()
    validate(Path(args.root))


if __name__ == "__main__":
    main()
