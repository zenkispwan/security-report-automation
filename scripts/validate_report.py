#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.event_reporting import (  # noqa: E402
    confirmed_event_cves,
    render_event_first_verified_report,
)
from security_intel.reporting import (  # noqa: E402
    render_source_appendix,
    sha256_file,
    unknown_report_cves,
)

INTELLIGENCE = ROOT / "data" / "intelligence.json"
DELTA = ROOT / "data" / "delta.json"
EVENTS = ROOT / "data" / "events.json"
EVENT_DELTA = ROOT / "data" / "event_delta.json"
REPORT = ROOT / "reports" / "security_report_latest.md"
METADATA = ROOT / "reports" / "security_report_metadata.json"


def main() -> int:
    errors: list[str] = []
    for path in (INTELLIGENCE, DELTA, EVENTS, EVENT_DELTA, REPORT, METADATA):
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
    if errors:
        return _fail(errors)

    intelligence = _load(INTELLIGENCE)
    delta = _load(DELTA)
    events = _load(EVENTS)
    event_delta = _load(EVENT_DELTA)
    metadata = _load(METADATA)
    report = REPORT.read_text(encoding="utf-8")

    if events.get("schema_version") != "2.5-events":
        errors.append("unexpected events schema_version")
    if event_delta.get("schema_version") != "2.5-event-delta":
        errors.append("unexpected event delta schema_version")

    if len(report.strip()) < 1000:
        errors.append("report is unexpectedly short")
    for required in (
        "24 小時態勢摘要",
        "今日重要資安事件",
        "24 小時新事件",
        "關聯漏洞與處理優先級",
        "建議行動",
        "資料品質",
        "可驗證事件來源",
        "可驗證資料來源",
    ):
        if required not in report:
            errors.append(f"report missing required section marker: {required}")
    if "基於 AI 模型知識生成" in report:
        errors.append("legacy AI-knowledge disclaimer is present")

    if metadata.get("schema_version") != "2.5-report-metadata":
        errors.append("unexpected report metadata schema_version")
    if metadata.get("provider") != "gemini":
        errors.append("unexpected report provider")
    if metadata.get("report_mode") != "event_first":
        errors.append("report_mode must be event_first")

    input_meta = metadata.get("input") or {}
    expected_hashes = {
        "events_sha256": sha256_file(EVENTS),
        "event_delta_sha256": sha256_file(EVENT_DELTA),
        "intelligence_sha256": sha256_file(INTELLIGENCE),
        "delta_sha256": sha256_file(DELTA),
    }
    for key, expected in expected_hashes.items():
        if input_meta.get(key) != expected:
            errors.append(f"metadata {key} does not match current input")

    expected_counts = {
        "event_items": len(events.get("items") or []),
        "event_delta_items": len(event_delta.get("items") or []),
        "intelligence_items": len(intelligence.get("items") or []),
        "delta_items": len(delta.get("items") or []),
    }
    for key, expected in expected_counts.items():
        if input_meta.get(key) != expected:
            errors.append(f"metadata {key} does not match current input")

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

    confirmed_scope = _verified_scope(intelligence, delta, events, include_source_mentions=False)
    source_scope = _verified_scope(intelligence, delta, events, include_source_mentions=True)

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

        unknown = unknown_report_cves(report, source_scope)
        if unknown:
            errors.append("deterministic report contains CVEs not present in verified/source event inputs: " + ", ".join(unknown))

        deterministic_body = render_event_first_verified_report(
            events, event_delta, intelligence, delta
        ).rstrip()
        expected_report = deterministic_body + "\n" + render_source_appendix(
            deterministic_body,
            source_scope,
            [],
        )
        if report != expected_report:
            errors.append(
                "deterministic event-first report does not exactly match renderer output; "
                "unexpected text may have been introduced"
            )
    else:
        if renderer != "llm" or llm_body_used is not True:
            errors.append("grounded LLM mode must declare renderer=llm and llm_body_used=true")
        if not actual_model:
            errors.append("grounded LLM report is missing actual Gemini model")
        if actual_model and actual_model not in attempted_models:
            errors.append("actual Gemini model is not present in attempted_models")
        expected_fallback = bool(requested_model and actual_model and requested_model != actual_model)
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

        unknown = unknown_report_cves(report, confirmed_scope)
        if unknown:
            errors.append("grounded report contains CVEs outside confirmed event/vulnerability scope: " + ", ".join(unknown))
        for cve in _unverified_event_cves(events):
            if cve in report.upper():
                errors.append(f"grounded report exposed source-mentioned but unverified CVE: {cve}")

    if errors:
        return _fail(errors)

    print(
        f"OK: event-first report chars={len(report)} events={len(events.get('items') or [])} "
        f"event_delta={len(event_delta.get('items') or [])} vulnerabilities={len(intelligence.get('items') or [])} "
        f"renderer={renderer} llm_body_used={llm_body_used} model={actual_model} "
        f"grounding_mode={grounding_mode} grounding_citations={len(citations)}"
    )
    return 0


def _verified_scope(
    intelligence: dict,
    delta: dict,
    events: dict,
    *,
    include_source_mentions: bool,
) -> dict:
    items = [*(intelligence.get("items") or []), *(delta.get("items") or [])]
    existing = {
        str((x.get("facts") or {}).get("cve") or x.get("cve") or "").upper()
        for x in items
    }
    event_cves = set(confirmed_event_cves(events))
    if include_source_mentions:
        event_cves.update(_unverified_event_cves(events))
    for cve in sorted(event_cves):
        if cve and cve not in existing:
            items.append({"cve": cve, "facts": {"cve": cve}})
            existing.add(cve)
    return {"items": items}


def _unverified_event_cves(events: dict) -> set[str]:
    return {
        str(cve).upper()
        for event in events.get("items") or []
        for cve in event.get("unverified_cve_mentions") or []
    }


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _fail(errors: list[str]) -> int:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
