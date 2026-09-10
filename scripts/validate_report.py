#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.reporting import sha256_file, unknown_report_cves  # noqa: E402

INTELLIGENCE = ROOT / "data" / "intelligence.json"
DELTA = ROOT / "data" / "delta.json"
REPORT = ROOT / "reports" / "security_report_latest.md"
METADATA = ROOT / "reports" / "security_report_metadata.json"


def main() -> int:
    errors: list[str] = []
    for path in (INTELLIGENCE, DELTA, REPORT, METADATA):
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
    if errors:
        return _fail(errors)

    intelligence = json.loads(INTELLIGENCE.read_text(encoding="utf-8"))
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    if len(report.strip()) < 1000:
        errors.append("report is unexpectedly short")
    for required in ("Daily Delta", "P1", "建議行動", "資料品質", "可驗證資料來源"):
        if required not in report:
            errors.append(f"report missing required section marker: {required}")
    if "基於 AI 模型知識生成" in report:
        errors.append("legacy AI-knowledge disclaimer is present")

    unknown = unknown_report_cves(report, intelligence)
    if unknown:
        errors.append("report contains unverified CVEs: " + ", ".join(unknown))

    input_meta = metadata.get("input") or {}
    if input_meta.get("intelligence_sha256") != sha256_file(INTELLIGENCE):
        errors.append("metadata intelligence hash does not match current input")
    if input_meta.get("delta_sha256") != sha256_file(DELTA):
        errors.append("metadata delta hash does not match current input")

    grounding = metadata.get("grounding") or {}
    mode = grounding.get("mode")
    citations = grounding.get("citations") or []
    if mode == "google_search":
        if not citations:
            errors.append("Google Search mode captured no grounding citations")
    elif mode == "verified_facts_only":
        if "資料來源模式：Verified facts only" not in report:
            errors.append("facts-only report is missing the transparent fallback notice")
        if grounding.get("search_queries"):
            errors.append("facts-only report unexpectedly contains Google Search queries")
    else:
        errors.append(f"unsupported grounding mode in metadata: {mode!r}")

    if errors:
        return _fail(errors)

    print(
        f"OK: report chars={len(report)} intelligence={len(intelligence.get('items') or [])} "
        f"grounding_mode={mode} grounding_citations={len(citations)}"
    )
    return 0


def _fail(errors: list[str]) -> int:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
