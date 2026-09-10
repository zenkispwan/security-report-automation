#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.reporting import (  # noqa: E402
    render_source_appendix,
    render_verified_facts_report,
    sha256_file,
    unknown_report_cves,
)

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
    delta = json.loads(DELTA.read_text(encoding="utf-8"))
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

    if metadata.get("schema_version") != "2.3-report-metadata":
        errors.append("unexpected report metadata schema_version")
    if metadata.get("provider") != "gemini":
        errors.append("unexpected report provider")

    input_meta = metadata.get("input") or {}
    if input_meta.get("intelligence_sha256") != sha256_file(INTELLIGENCE):
        errors.append("metadata intelligence hash does not match current input")
    if input_meta.get("delta_sha256") != sha256_file(DELTA):
        errors.append("metadata delta hash does not match current input")
    if input_meta.get("intelligence_items") != len(intelligence.get("items") or []):
        errors.append("metadata intelligence item count does not match current input")
    if input_meta.get("delta_items") != len(delta.get("items") or []):
        errors.append("metadata delta item count does not match current input")

    requested_model = metadata.get("requested_model")
    actual_model = metadata.get("model")
    model_fallback = metadata.get("model_fallback") or {}
    attempted_models = model_fallback.get("attempted_models") or []
    fallback_used = model_fallback.get("used")
    fallback_reason = model_fallback.get("reason")
    renderer = metadata.get("renderer")
    llm_body_used = metadata.get("llm_body_used")
    api_mode = metadata.get("api_mode")
    grounding = metadata.get("grounding") or {}
    grounding_mode = grounding.get("mode")
    citations = grounding.get("citations") or []
    queries = grounding.get("search_queries") or []

    if not requested_model:
        errors.append("metadata is missing requested Gemini model")
    if attempted_models and attempted_models[0] != requested_model:
        errors.append("attempted_models does not start with requested Gemini model")

    if api_mode == "deterministic_facts_only":
        if renderer != "deterministic" or llm_body_used is not False:
            errors.append("deterministic mode must declare renderer=deterministic and llm_body_used=false")
        if actual_model is not None:
            errors.append("deterministic report must not record an actual Gemini body model")
        if fallback_used is not False or fallback_reason is not None:
            errors.append("deterministic report must not claim Gemini model fallback for the body")
        if metadata.get("interaction_id") is not None:
            errors.append("deterministic report must not record a model response id")
        if metadata.get("usage") is not None:
            errors.append("deterministic report must not record LLM body token usage")
        if grounding_mode != "verified_facts_only":
            errors.append("deterministic report must use verified_facts_only grounding mode")
        if citations or queries:
            errors.append("deterministic report must not contain Google Search citations or queries")
        if "資料來源模式：Verified facts only（deterministic）" not in report:
            errors.append("deterministic report is missing the transparent renderer notice")

        deterministic_body = render_verified_facts_report(intelligence, delta).rstrip()
        expected_report = deterministic_body + "\n" + render_source_appendix(
            deterministic_body,
            intelligence,
            [],
        )
        if report != expected_report:
            errors.append(
                "deterministic report does not exactly match renderer output; "
                "unexpected text may have been introduced"
            )
    else:
        if renderer != "llm" or llm_body_used is not True:
            errors.append("grounded LLM mode must declare renderer=llm and llm_body_used=true")
        if not actual_model:
            errors.append("grounded LLM report is missing actual Gemini model")
        if actual_model and actual_model not in attempted_models:
            errors.append("actual Gemini model is not present in attempted_models")
        expected_fallback = bool(
            requested_model and actual_model and requested_model != actual_model
        )
        if fallback_used is not expected_fallback:
            errors.append("model_fallback.used does not match requested/actual model")
        if expected_fallback and fallback_reason != "transient_model_unavailable":
            errors.append("model fallback is missing transient_model_unavailable reason")
        if not expected_fallback and fallback_reason:
            errors.append("model fallback reason is present although requested model was used")
        if api_mode not in {"interactions", "generate_content_search"}:
            errors.append(f"unsupported grounded LLM api_mode: {api_mode!r}")
        if grounding_mode != "google_search":
            errors.append("LLM body is only allowed when Google Search grounding succeeded")
        if not citations:
            errors.append("Google Search mode captured no grounding citations")

    if errors:
        return _fail(errors)

    print(
        f"OK: report chars={len(report)} intelligence={len(intelligence.get('items') or [])} "
        f"renderer={renderer} llm_body_used={llm_body_used} model={actual_model} "
        f"grounding_mode={grounding_mode} grounding_citations={len(citations)}"
    )
    return 0


def _fail(errors: list[str]) -> int:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
