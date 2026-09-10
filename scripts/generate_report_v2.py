#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.event_reporting import (  # noqa: E402
    EVENT_SYSTEM_INSTRUCTION,
    build_event_report_prompt,
    confirmed_event_cves,
    render_event_first_verified_report,
)
from security_intel.llm.gemini import generate_grounded_markdown  # noqa: E402
from security_intel.reporting import (  # noqa: E402
    render_source_appendix,
    sha256_file,
    unknown_report_cves,
)

INTELLIGENCE_PATH = ROOT / "data" / "intelligence.json"
DELTA_PATH = ROOT / "data" / "delta.json"
EVENTS_PATH = ROOT / "data" / "events.json"
EVENT_DELTA_PATH = ROOT / "data" / "event_delta.json"
REPORT_DIR = ROOT / "reports"
REPORT_PATH = REPORT_DIR / "security_report_latest.md"
METADATA_PATH = REPORT_DIR / "security_report_metadata.json"
DEFAULT_FALLBACK_MODELS = "gemini-3.7-flash,gemini-3.6-flash"


def main() -> int:
    provider = os.getenv("REPORT_PROVIDER", "gemini").strip().lower()
    if provider != "gemini":
        print(f"ERROR: unsupported REPORT_PROVIDER={provider!r}", file=sys.stderr)
        return 2

    model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()
    fallback_models = _env_csv("GEMINI_FALLBACK_MODELS", DEFAULT_FALLBACK_MODELS)
    search_mode = os.getenv("GEMINI_SEARCH_MODE", "auto").strip().lower()
    search_timeout_ms = _env_int("GEMINI_SEARCH_TIMEOUT_MS", 45_000)
    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    if search_mode not in {"auto", "required", "off"}:
        print(f"ERROR: unsupported GEMINI_SEARCH_MODE={search_mode!r}", file=sys.stderr)
        return 2
    if search_mode != "off" and not api_key:
        print("ERROR: GEMINI_API_KEY is not configured", file=sys.stderr)
        return 2

    intelligence = _load_json(INTELLIGENCE_PATH)
    delta = _load_json(DELTA_PATH)
    events = _load_json(EVENTS_PATH)
    event_delta = _load_json(EVENT_DELTA_PATH)
    if not intelligence.get("items"):
        print("ERROR: data/intelligence.json has no vulnerability items", file=sys.stderr)
        return 2
    if events.get("schema_version") != "2.5-events":
        print("ERROR: data/events.json is not V2.5 event intelligence", file=sys.stderr)
        return 2

    confirmed_scope = _verified_scope(intelligence, delta, events, include_source_mentions=False)
    source_scope = _verified_scope(intelligence, delta, events, include_source_mentions=True)
    prompt = build_event_report_prompt(events, event_delta, intelligence, delta)
    print(
        json.dumps(
            {
                "provider": provider,
                "model": model,
                "fallback_models": fallback_models,
                "search_mode": search_mode,
                "search_timeout_ms": search_timeout_ms,
                "security_events": len(events.get("items") or []),
                "new_event_delta": len(event_delta.get("items") or []),
                "vulnerability_items": len(intelligence.get("items") or []),
                "vulnerability_delta": len(delta.get("items") or []),
            },
            ensure_ascii=False,
        )
    )

    response = generate_grounded_markdown(
        api_key=api_key,
        model=model,
        fallback_models=fallback_models,
        prompt=prompt,
        system_instruction=EVENT_SYSTEM_INSTRUCTION,
        search_mode=search_mode,
        search_timeout_ms=search_timeout_ms,
    )

    if response.api_mode == "deterministic_facts_only":
        body = render_event_first_verified_report(events, event_delta, intelligence, delta).rstrip()
        report_scope = source_scope
        print(
            "WARNING: Google Search grounding unavailable; rendering deterministic "
            f"event-first verified-facts report ({response.grounding_fallback_reason})",
            file=sys.stderr,
        )
    else:
        body = response.text.rstrip()
        report_scope = confirmed_scope
        if response.grounding_fallback_reason:
            print(
                "INFO: Google Search grounding preserved through alternate API transport "
                f"({response.grounding_fallback_reason})",
                file=sys.stderr,
            )
        if response.model_fallback_reason:
            print(
                "WARNING: requested Gemini model was transiently unavailable; "
                f"selected {response.model} after attempts {response.attempted_models}",
                file=sys.stderr,
            )
        exposed_unverified = sorted(cve for cve in _unverified_event_cves(events) if cve in body.upper())
        if exposed_unverified:
            print(
                "ERROR: grounded report exposed source-mentioned but unverified CVEs: "
                + ", ".join(exposed_unverified),
                file=sys.stderr,
            )
            return 3

    unknown = unknown_report_cves(body, report_scope)
    if unknown:
        print(
            "ERROR: report introduced CVEs outside allowed event/vulnerability scope: "
            + ", ".join(unknown),
            file=sys.stderr,
        )
        return 3

    appendix = render_source_appendix(body, report_scope, response.citations)
    report_text = body + "\n" + appendix

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_text, encoding="utf-8")

    llm_body_used = response.api_mode != "deterministic_facts_only"
    metadata = {
        "schema_version": "2.5-report-metadata",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "provider": provider,
        "report_mode": "event_first",
        "renderer": "llm" if llm_body_used else "deterministic",
        "llm_body_used": llm_body_used,
        "requested_model": response.requested_model,
        "model": response.model,
        "model_fallback": {
            "used": bool(response.model and response.model != response.requested_model),
            "attempted_models": response.attempted_models,
            "reason": response.model_fallback_reason,
        },
        "api_mode": response.api_mode,
        "interaction_id": response.interaction_id,
        "input": {
            "events_generated_at": events.get("generated_at"),
            "event_delta_generated_at": event_delta.get("generated_at"),
            "intelligence_generated_at": intelligence.get("generated_at"),
            "delta_generated_at": delta.get("generated_at"),
            "events_sha256": sha256_file(EVENTS_PATH),
            "event_delta_sha256": sha256_file(EVENT_DELTA_PATH),
            "intelligence_sha256": sha256_file(INTELLIGENCE_PATH),
            "delta_sha256": sha256_file(DELTA_PATH),
            "event_items": len(events.get("items") or []),
            "event_delta_items": len(event_delta.get("items") or []),
            "intelligence_items": len(intelligence.get("items") or []),
            "delta_items": len(delta.get("items") or []),
            "confirmed_event_cves": len(confirmed_event_cves(events)),
            "unverified_event_cve_mentions": len(_unverified_event_cves(events)),
        },
        "grounding": {
            "requested_mode": search_mode,
            "mode": response.grounding_mode,
            "fallback_reason": response.grounding_fallback_reason,
            "search_queries": response.search_queries,
            "citations": response.citations,
        },
        "timeouts_ms": {"search": search_timeout_ms},
        "usage": response.usage,
    }
    METADATA_PATH.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"OK: wrote {REPORT_PATH.relative_to(ROOT)}")
    print(f"OK: wrote {METADATA_PATH.relative_to(ROOT)}")
    print(f"Report mode: {metadata['report_mode']}")
    print(f"Renderer: {metadata['renderer']}")
    print(f"Gemini model: {response.model or 'not used for report body'}")
    print(f"API mode: {response.api_mode}")
    print(f"Grounding mode: {response.grounding_mode}")
    print(f"Grounding citations: {len(response.citations)}")
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


def _env_csv(name: str, default: str) -> list[str]:
    raw = os.getenv(name, default)
    return list(dict.fromkeys(x.strip() for x in raw.split(",") if x.strip()))


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer, got {raw!r}") from exc
    if value < 1_000:
        raise ValueError(f"{name} must be at least 1000 ms")
    return value


def _load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
