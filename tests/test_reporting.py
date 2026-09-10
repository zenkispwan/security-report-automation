from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.reporting import (  # noqa: E402
    build_report_prompt,
    render_source_appendix,
    render_verified_facts_report,
    unknown_report_cves,
)


def sample_intelligence() -> dict:
    return {
        "generated_at": "2026-09-10T05:19:44+00:00",
        "risk_version": "1.1",
        "summary": {"p1": 1, "p2": 0, "p3": 0, "with_delta": 0},
        "selection": {"selected_count": 1},
        "items": [
            {
                "cve": "CVE-2026-20079",
                "events": [],
                "risk": {
                    "score": 100,
                    "priority": "P1",
                    "reasons": [{"code": "CISA_KEV", "points": 45}],
                },
                "facts": {
                    "cve": "CVE-2026-20079",
                    "vendor": "Cisco",
                    "product": "FMC",
                    "title": "Authentication bypass",
                    "description": "Verified official description; prose mentions before version 9.9 but no structured affected data is present.",
                    "cvss": {"version": "3.1", "score": 10.0, "severity": "CRITICAL"},
                    "epss": 0.35,
                    "epss_percentile": 0.98,
                    "cisa_kev": {
                        "listed": True,
                        "date_added": "2026-09-09",
                        "due_date": "2026-09-12",
                        "required_action": "Apply vendor mitigations exactly as published.",
                        "known_ransomware_campaign_use": "Unknown",
                        "notes": "https://sec.cloudapps.cisco.com/security/advisory/example",
                    },
                    "exploitation_status": {"status": "known_exploited", "source": "cisa_kev"},
                    "published_time": "2026-03-04T18:16:24+00:00",
                    "updated_time": "2026-09-10T04:17:50+00:00",
                    "source_url": "https://nvd.nist.gov/vuln/detail/CVE-2026-20079",
                    "provenance": {
                        "nvd": "https://nvd.nist.gov/vuln/detail/CVE-2026-20079",
                        "cisa_kev": "https://www.cisa.gov/known-exploited-vulnerabilities-catalog",
                        "epss": "https://api.first.org/data/v1/epss?cve=CVE-2026-20079",
                    },
                },
            }
        ],
    }


def zero_delta(generated_at: str) -> dict:
    return {
        "generated_at": generated_at,
        "baseline": {
            "type": "state",
            "generated_at": "2026-09-09T05:19:44+00:00",
            "available": True,
        },
        "summary": {"meaningful_change_count": 0, "events": {}},
        "items": [],
    }


class ReportingTests(unittest.TestCase):
    def test_prompt_preserves_fact_boundary_and_zero_delta(self) -> None:
        intelligence = sample_intelligence()
        prompt = build_report_prompt(intelligence, zero_delta(intelligence["generated_at"]))
        self.assertIn("VERIFIED_FACTS", prompt)
        self.assertIn("meaningful_change_count", prompt)
        self.assertIn("CVE-2026-20079", prompt)
        self.assertIn("本次沒有符合門檻的重大變化", prompt)

    def test_deterministic_renderer_uses_verified_values_and_zero_delta(self) -> None:
        intelligence = sample_intelligence()
        report = render_verified_facts_report(
            intelligence,
            zero_delta(intelligence["generated_at"]),
        )
        self.assertIn("Verified facts only（deterministic）", report)
        self.assertIn("沒有使用 LLM model memory 產生正文", report)
        self.assertIn("本次未偵測到符合門檻的重大 Daily Delta", report)
        self.assertIn("CVE-2026-20079", report)
        self.assertIn("v3.1 10.0 (CRITICAL)", report)
        self.assertIn("0.35 / percentile=0.98", report)
        self.assertIn("Apply vendor mitigations exactly as published.", report)
        self.assertIn("Verified official description", report)

    def test_deterministic_renderer_does_not_infer_versions_from_description(self) -> None:
        intelligence = sample_intelligence()
        report = render_verified_facts_report(
            intelligence,
            zero_delta(intelligence["generated_at"]),
        )
        affected_line = next(
            line for line in report.splitlines() if line.startswith("- **受影響版本**：")
        )
        self.assertIn("未確認", affected_line)
        self.assertNotIn("9.9", affected_line)

    def test_deterministic_renderer_does_not_add_model_memory_patch_language(self) -> None:
        intelligence = sample_intelligence()
        report = render_verified_facts_report(
            intelligence,
            zero_delta(intelligence["generated_at"]),
        )
        self.assertNotIn("Patch Tuesday", report)
        self.assertNotIn("官方 Hotfix", report)
        self.assertNotIn("常被勒索軟體作為", report)

    def test_deterministic_renderer_renders_delta_events_directly(self) -> None:
        intelligence = sample_intelligence()
        item = intelligence["items"][0]
        delta = {
            "generated_at": intelligence["generated_at"],
            "baseline": {"type": "state", "available": True},
            "summary": {"meaningful_change_count": 1, "events": {"NEW_KEV": 1}},
            "items": [
                {
                    **item,
                    "events": [
                        {"type": "NEW_KEV", "from": False, "to": True},
                    ],
                }
            ],
        }
        report = render_verified_facts_report(intelligence, delta)
        self.assertIn("NEW_KEV=1", report)
        self.assertIn("NEW_KEV (from=false; to=true)", report)

    def test_unknown_cve_is_rejected(self) -> None:
        intelligence = sample_intelligence()
        report = "CVE-2026-20079 is verified. CVE-2026-99999 is not in input."
        self.assertEqual(unknown_report_cves(report, intelligence), ["CVE-2026-99999"])

    def test_source_appendix_uses_deterministic_fact_sources(self) -> None:
        intelligence = sample_intelligence()
        appendix = render_source_appendix(
            "## P1\nCVE-2026-20079",
            intelligence,
            [{"title": "Cisco advisory", "url": "https://example.com/current-advisory"}],
        )
        self.assertIn("https://nvd.nist.gov/vuln/detail/CVE-2026-20079", appendix)
        self.assertIn("https://www.cisa.gov/known-exploited-vulnerabilities-catalog", appendix)
        self.assertIn("https://api.first.org/data/v1/epss?cve=CVE-2026-20079", appendix)
        self.assertIn("https://sec.cloudapps.cisco.com/security/advisory/example", appendix)
        self.assertIn("https://example.com/current-advisory", appendix)


if __name__ == "__main__":
    unittest.main()
