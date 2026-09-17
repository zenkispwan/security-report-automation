from __future__ import annotations

import unittest

from scripts.build_daily_brief import build_daily_brief
from scripts.validate_daily_brief import validate


class DailyBriefTests(unittest.TestCase):
    def test_builds_event_first_daily_brief_without_inventing_facts(self):
        events = {
            "generated_at": "2026-09-17T00:00:00+00:00",
            "sources": [{"name": "Vendor", "url": "https://example.com", "source_type": "official_advisory"}],
            "summary": {"successful_sources": 1, "source_errors": []},
            "translation": {"translated_items": 1},
            "items": [
                {
                    "id": "event-1",
                    "event_type": "ACTIVE_EXPLOITATION",
                    "priority": "CRITICAL",
                    "score": 110,
                    "published_at": "2026-09-17T01:00:00+00:00",
                    "title": "Actively exploited vulnerability",
                    "title_zh": "已遭積極利用的漏洞",
                    "summary": "Source summary",
                    "summary_zh": "來源摘要",
                    "source_name": "Vendor",
                    "source_type": "official_advisory",
                    "source_url": "https://example.com/advisory",
                    "related_cves": ["CVE-2026-12345"],
                    "matched_intelligence_cves": ["CVE-2026-12345"],
                }
            ],
        }
        intelligence = {
            "generated_at": "2026-09-17T00:00:00+00:00",
            "items": [
                {
                    "cve": "CVE-2026-12345",
                    "risk": {"priority": "P1", "score": 100, "reasons": [{"code": "CISA_KEV", "points": 45}]},
                    "facts": {
                        "cve": "CVE-2026-12345",
                        "vendor": "Vendor",
                        "product": "Product",
                        "title": "Original title",
                        "description": "Original description",
                        "cvss": {"version": "3.1", "score": 9.8, "severity": "CRITICAL"},
                        "epss": 0.9,
                        "epss_percentile": 0.99,
                        "cisa_kev": {"listed": True},
                        "exploitation_status": {"status": "known_exploited", "source": "cisa_kev"},
                        "published_time": "2026-09-16T00:00:00Z",
                        "updated_time": "2026-09-17T00:00:00Z",
                        "source_url": "https://nvd.nist.gov/vuln/detail/CVE-2026-12345",
                        "source_type": ["nvd", "cisa_kev", "epss"],
                        "provenance": {"nvd": "https://nvd.nist.gov/vuln/detail/CVE-2026-12345"},
                    },
                }
            ],
        }
        delta = {
            "generated_at": "2026-09-17T00:00:00+00:00",
            "items": [
                {
                    "cve": "CVE-2026-12345",
                    "events": [{"type": "NEW_KEV", "from": False, "to": True}],
                    "risk": {"priority": "P1", "score": 100, "reasons": []},
                    "facts": intelligence["items"][0]["facts"],
                }
            ],
        }
        cve_zh = {
            "generated_at": "2026-09-17T00:00:00+00:00",
            "items": [
                {
                    "cve": "CVE-2026-12345",
                    "title_zh": "漏洞中文標題",
                    "description_zh": "漏洞中文說明",
                }
            ],
            "translation": {"translated_items": 1},
        }

        payload = build_daily_brief(
            events=events,
            intelligence=intelligence,
            delta=delta,
            cve_zh=cve_zh,
            generated_at="2026-09-17T02:00:00+00:00",
        )

        self.assertEqual(payload["summary"]["event_count"], 1)
        self.assertEqual(payload["summary"]["active_exploitation_events"], 1)
        self.assertEqual(payload["summary"]["new_kev_count"], 1)
        self.assertEqual(payload["summary"]["p1_cve_count"], 1)
        self.assertEqual(payload["headline_events"][0]["title_zh"], "已遭積極利用的漏洞")
        self.assertEqual(payload["priority_cves"][0]["description_zh"], "漏洞中文說明")
        self.assertEqual(payload["priority_cves"][0]["cvss"]["score"], 9.8)
        self.assertEqual(payload["priority_cves"][0]["source_url"], "https://nvd.nist.gov/vuln/detail/CVE-2026-12345")
        self.assertNotIn("affected_versions", payload["priority_cves"][0])

        payload["inputs"] = {
            name: {"path": f"data/{name}.json", "sha256": "0" * 64}
            for name in ("events", "intelligence", "delta", "cve_zh")
        }
        validate(payload)

    def test_priority_cves_are_sorted_by_priority_then_risk(self):
        intelligence = {
            "items": [
                {"cve": "CVE-2026-0001", "risk": {"priority": "P3", "score": 99}, "facts": {"cve": "CVE-2026-0001", "source_url": "https://example.com/1", "source_type": []}},
                {"cve": "CVE-2026-0002", "risk": {"priority": "P1", "score": 80}, "facts": {"cve": "CVE-2026-0002", "source_url": "https://example.com/2", "source_type": []}},
                {"cve": "CVE-2026-0003", "risk": {"priority": "P1", "score": 100}, "facts": {"cve": "CVE-2026-0003", "source_url": "https://example.com/3", "source_type": []}},
            ]
        }
        payload = build_daily_brief(events={"items": []}, intelligence=intelligence, delta={"items": []}, cve_zh={"items": []})
        self.assertEqual([row["cve"] for row in payload["priority_cves"]], ["CVE-2026-0003", "CVE-2026-0002", "CVE-2026-0001"])


if __name__ == "__main__":
    unittest.main()
