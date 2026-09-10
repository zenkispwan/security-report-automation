from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.reporting import (  # noqa: E402
    build_report_prompt,
    render_source_appendix,
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
                    "description": "Verified description",
                    "cvss": {"version": "3.1", "score": 10.0, "severity": "CRITICAL"},
                    "epss": 0.35,
                    "epss_percentile": 0.98,
                    "cisa_kev": {
                        "listed": True,
                        "date_added": "2026-09-09",
                        "due_date": "2026-09-12",
                        "required_action": "Apply vendor mitigations",
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


class ReportingTests(unittest.TestCase):
    def test_prompt_preserves_fact_boundary_and_zero_delta(self) -> None:
        intelligence = sample_intelligence()
        delta = {
            "generated_at": intelligence["generated_at"],
            "baseline": {"available": True},
            "summary": {"meaningful_change_count": 0},
            "items": [],
        }
        prompt = build_report_prompt(intelligence, delta)
        self.assertIn("VERIFIED_FACTS", prompt)
        self.assertIn("meaningful_change_count", prompt)
        self.assertIn("CVE-2026-20079", prompt)
        self.assertIn("未偵測到符合門檻的重大 Daily Delta", prompt)

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
