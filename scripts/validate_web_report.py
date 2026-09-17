#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


COPIES = {
    Path("data/events.json"): Path("data/events.json"),
    Path("data/cve_enrichment_zh.json"): Path("data/cve_enrichment_zh.json"),
    Path("data/intelligence.json"): Path("data/intelligence.json"),
    Path("data/delta.json"): Path("data/delta.json"),
    Path("reports/security_report_metadata.json"): Path("data/report_metadata.json"),
    Path("reports/security_report_latest.md"): Path("security_report_latest.md"),
    Path("web/_headers"): Path("_headers"),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path) -> None:
    required = [
        root / "index.html",
        root / "events.html",
        root / "cve.html",
        root / "styles.css",
        root / "events.css",
        root / "cve.css",
        root / "app.js",
        root / "events.js",
        root / "cve.js",
        root / "_headers",
    ]
    required += [root / target for target in COPIES.values()]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing built web-report files: {', '.join(missing)}")

    for source, relative_target in COPIES.items():
        built = root / relative_target
        if digest(source) != digest(built):
            raise SystemExit(f"Built file differs from verified source: {relative_target}")

    events_payload = json.loads((root / "data/events.json").read_text(encoding="utf-8"))
    cve_zh = json.loads((root / "data/cve_enrichment_zh.json").read_text(encoding="utf-8"))
    intelligence = json.loads((root / "data/intelligence.json").read_text(encoding="utf-8"))
    delta = json.loads((root / "data/delta.json").read_text(encoding="utf-8"))
    metadata = json.loads((root / "data/report_metadata.json").read_text(encoding="utf-8"))

    if not isinstance(events_payload.get("items"), list):
        raise SystemExit("Invalid web security events payload")
    if not isinstance(cve_zh.get("items"), list):
        raise SystemExit("Invalid CVE Traditional Chinese enrichment payload")
    if not isinstance(intelligence.get("items"), list):
        raise SystemExit("Invalid web intelligence payload")
    if not isinstance(delta.get("items"), list):
        raise SystemExit("Invalid web delta payload")
    if not metadata.get("generated_at"):
        raise SystemExit("Missing report metadata generated_at")

    for item in events_payload.get("items", []):
        if not item.get("title") or not item.get("source_url") or not item.get("source_name"):
            raise SystemExit("Security event is missing title/source provenance")
        if not isinstance(item.get("related_cves", []), list):
            raise SystemExit("Security event related_cves must be a list")
    for item in cve_zh.get("items", []):
        if not item.get("cve") or not item.get("title_zh") or "description_zh" not in item:
            raise SystemExit("CVE translation enrichment is missing required fields")

    index = (root / "index.html").read_text(encoding="utf-8")
    events_page = (root / "events.html").read_text(encoding="utf-8")
    cve_page = (root / "cve.html").read_text(encoding="utf-8")
    app = (root / "app.js").read_text(encoding="utf-8")
    events_js = (root / "events.js").read_text(encoding="utf-8")
    cve_js = (root / "cve.js").read_text(encoding="utf-8")
    headers = (root / "_headers").read_text(encoding="utf-8")

    if "./styles.css" not in index or "./events.css" not in index or "./app.js" not in index or "./events.js" not in index:
        raise SystemExit("Static shell is missing local assets")
    if "securityEventList" not in index or "securityEventCount" not in index or "./events.html" not in index:
        raise SystemExit("Homepage is missing security event containers or full-feed navigation")
    if "technical-panel" not in index:
        raise SystemExit("Technical CVE data is not collapsed behind the event-first homepage")
    if "allSecurityEventList" not in events_page or "allEventTypeFilters" not in events_page or "allEventSource" not in events_page:
        raise SystemExit("Full events page is missing event list or filters")
    if "./styles.css" not in events_page or "./events.css" not in events_page or "./events.js" not in events_page:
        raise SystemExit("Full events page is missing local assets")
    if "cveSummaryCard" not in cve_page or "cveRelatedEvents" not in cve_page:
        raise SystemExit("CVE detail page is missing verified-facts or related-event containers")
    if "./styles.css" not in cve_page or "./events.css" not in cve_page or "./cve.css" not in cve_page or "./cve.js" not in cve_page:
        raise SystemExit("CVE detail page is missing local assets")
    if "./data/events.json" not in app or "./data/intelligence.json" not in app or "./data/delta.json" not in app or "./data/report_metadata.json" not in app:
        raise SystemExit("Web app is not wired to verified compact inputs")
    if "./data/events.json" not in events_js or "allSecurityEventList" not in events_js or "./cve.html?cve=" not in events_js:
        raise SystemExit("Security event views are not wired to generated events.json and CVE details")
    if "./data/intelligence.json" not in cve_js or "./data/events.json" not in cve_js or "./data/cve_enrichment_zh.json" not in cve_js:
        raise SystemExit("CVE detail page is not wired to facts, events, and translation enrichment")

    for shell in (index, events_page, cve_page):
        if "https://" in shell.replace("https://github.com/zenkispwan/security-report-automation", ""):
            raise SystemExit("Unexpected external resource in web shell")
        if "<script src=\"http" in shell or "<link rel=\"stylesheet\" href=\"http" in shell:
            raise SystemExit("External executable/style dependency is not allowed")
    if "Content-Security-Policy:" not in headers or "Cache-Control: no-cache" not in headers:
        raise SystemExit("Cloudflare Workers Static Assets security/cache headers are missing")

    print(
        "OK: Cloudflare Workers Static Assets web report "
        f"events={len(events_payload['items'])} "
        f"cve_zh={len(cve_zh['items'])} "
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
