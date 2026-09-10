#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.llm.gemini import generate_grounded_markdown  # noqa: E402
from security_intel.reporting import (  # noqa: E402
    SYSTEM_INSTRUCTION,
    build_report_prompt,
    render_source_appendix,
    render_verified_facts_report,
    sha256_file,
    unknown_report_cves,
)

INTELLIGENCE_PATH = ROOT / "data" / "intelligence.json"
DELTA_PATH = ROOT / "data" / "delta.json"
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
    if not intelligence.get("items"):
        print("ERROR: data/intelligence.json has no items", file=sys.stderr)
        return 2

    prompt = build_report_prompt(intelligence, delta)
    print(
        json.dumps(
            {
                "provider": provider,
                "model": model,
                "fallback_models": fallback_models,
                "search_mode": search_mode,
                "search_timeout_ms": search_timeout_ms,
                "intelligence_items": len(intelligence.get("items") or []),
                "delta_items": len(delta.get("items") or []),
            },
            ensure_ascii=False,
        )
    )

    response = generate_grounded_markdown(
        api_key=api_key,
        model=model,
        fallback_models=fallback_models,
        prompt=prompt,
        system_instruction=SYSTEM_INSTRUCTION,
        search_mode=search_mode,
        search_timeout_ms=search_timeout_ms,
    )

    if response.api_mode == "deterministic_facts_only":
        body = render_verified_facts_report(intelligence, delta).rstrip()
        print(
            "WARNING: Google Search grounding unavailable; rendering deterministic "
            f"verified-facts-only report ({response.grounding_fallback_reason})",
            file=sys.stderr,
        )
    else:
        body = response.text.rstrip()
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

    unknown = unknown_report_cves(body, intelligence)
    if unknown:
        print(
            "ERROR: report introduced CVEs outside verified intelligence: " + ", ".join(unknown),
            file=sys.stderr,
        )
        return 3

    appendix = render_source_appendix(body, intelligence, response.citations)
    report_text = body + "\n" + appendix

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_text, encoding="utf-8")

    llm_body_used = response.api_mode != "deterministic_facts_only"
    metadata = {
        "schema_version": "2.3-report-metadata",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "provider": provider,
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
            "intelligence_generated_at": intelligence.get("generated_at"),
            "delta_generated_at": delta.get("generated_at"),
            "intelligence_sha256": sha256_file(INTELLIGENCE_PATH),
            "delta_sha256": sha256_file(DELTA_PATH),
            "intelligence_items": len(intelligence.get("items") or []),
            "delta_items": len(delta.get("items") or []),
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
    print(f"Renderer: {metadata['renderer']}")
    print(f"Gemini model: {response.model or 'not used for report body'}")
    print(f"API mode: {response.api_mode}")
    print(f"Grounding mode: {response.grounding_mode}")
    print(f"Grounding citations: {len(response.citations)}")
    return 0


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
