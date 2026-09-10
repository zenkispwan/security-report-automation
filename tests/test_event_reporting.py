from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.event_reporting import (  # noqa: E402
    build_event_report_prompt,
    render_event_first_verified_report,
)


def events_payload(*, bootstrap: bool = False) -> dict:
    return {
        "schema_version": "2.5-events",
        "generated_at": "2026-09-10T15:00:00+00:00",
        "window": {
            "hours": 24,
            "start": "2026-09-09T15:00:00+00:00",
            "end": "2026-09-10T15:00:00+00:00",
        },
        "baseline": {
            "available": not bootstrap,
            "type": "bootstrap" if bootstrap else "event_state",
            "generated_at": None if bootstrap else "2026-09-10T03:00:00+00:00",
        },
        "profile": {
            "name": "test",
            "technology_keywords_configured": 0,
            "industry_keywords_configured": 0,
        },
        "summary": {
            "discovered_articles": 4,
            "eligible_articles": 3,
            "excluded_unknown_time": 1,
            "excluded_outside_window": 0,
            "cluster_count": 2,
            "selected_count": 2,
            "p1": 1,
            "p2": 0,
            "p3": 0,
            "watch": 1,
        },
        "items": [
            {
                "event_id": "evt-a",
                "title": "Vendor confirms active exploitation of CVE-2026-12345",
                "summary": "Vendor is actively tracking exploitation.",
                "event_type": "active_exploitation",
                "signals": ["active_exploitation", "vulnerability"],
                "priority": "P1",
                "score": 85,
                "is_new": True,
                "first_seen": "2026-09-10T12:00:00+00:00",
                "last_seen": "2026-09-10T14:00:00+00:00",
                "confirmed_cves": ["CVE-2026-12345"],
                "unverified_cve_mentions": [],
                "linked_vulnerabilities": [],
                "verification": {
                    "status": "official_confirmed",
                    "confidence": "high",
                    "source_count": 1,
                },
                "relevance": {
                    "level": "medium",
                    "scope": "general_enterprise",
                    "reasons": [{"code": "ASSET_CLASS_MATCH", "detail": "network_edge"}],
                },
                "sources": [
                    {
                        "title": "Vendor confirms active exploitation of CVE-2026-12345",
                        "url": "https://example-vendor.com/advisory",
                        "publisher": "Example Vendor",
                        "domain": "example-vendor.com",
                        "authority": "official",
                        "published_time": "2026-09-10T12:00:00+00:00",
                    }
                ],
            },
            {
                "event_id": "evt-b",
                "title": "Report claims CVE-2026-99999 exploitation",
                "summary": "Unconfirmed discovery item.",
                "event_type": "active_exploitation",
                "signals": ["active_exploitation"],
                "priority": "WATCH",
                "score": 60,
                "is_new": True,
                "first_seen": "2026-09-10T13:00:00+00:00",
                "last_seen": "2026-09-10T13:00:00+00:00",
                "confirmed_cves": [],
                "unverified_cve_mentions": ["CVE-2026-99999"],
                "linked_vulnerabilities": [],
                "verification": {
                    "status": "discovery_only",
                    "confidence": "low",
                    "source_count": 1,
                },
                "relevance": {"level": "low", "scope": "unconfirmed", "reasons": []},
                "sources": [
                    {
                        "title": "Report claims CVE-2026-99999 exploitation",
                        "url": "https://unknown.example/a",
                        "publisher": "unknown.example",
                        "domain": "unknown.example",
                        "authority": "discovery",
                        "published_time": "2026-09-10T13:00:00+00:00",
                    }
                ],
            },
        ],
    }


def event_delta(*, bootstrap: bool = False) -> dict:
    source = events_payload(bootstrap=bootstrap)
    return {
        "schema_version": "2.5-event-delta",
        "generated_at": source["generated_at"],
        "baseline": source["baseline"],
        "mode": "bootstrap" if bootstrap else "delta",
        "summary": {"new_notable_count": 0 if bootstrap else 1},
        "items": [] if bootstrap else [source["items"][0]],
    }


def vulnerability_intelligence() -> dict:
    return {
        "generated_at": "2026-09-10T15:00:00+00:00",
        "summary": {"p1": 1, "p2": 0, "p3": 0},
        "selection": {"selected_count": 1},
        "items": [
            {
                "cve": "CVE-2026-12345",
                "risk": {"priority": "P1", "score": 100},
                "facts": {
                    "cve": "CVE-2026-12345",
                    "vendor": "Example Vendor",
                    "product": "Gateway",
                    "cvss": {"score": 9.8, "severity": "CRITICAL"},
                    "epss": 0.75,
                    "cisa_kev": {"listed": True},
                    "exploitation_status": {"status": "known_exploited"},
                },
            }
        ],
    }


class EventReportingTests(unittest.TestCase):
    def test_deterministic_report_is_event_first(self):
        report = render_event_first_verified_report(
            events_payload(), event_delta(), vulnerability_intelligence(), {"items": []}
        )
        self.assertTrue(report.startswith("# 每日資安事件情報簡報"))
        self.assertLess(report.index("## 今日重要資安事件"), report.index("## 關聯漏洞與處理優先級"))
        self.assertIn("Vendor confirms active exploitation", report)
        self.assertIn("official_confirmed", report)
        self.assertIn("CVE-2026-12345", report)
        self.assertIn("不代表組織已確認受影響", report)

    def test_bootstrap_is_not_reported_as_daily_new_events(self):
        report = render_event_first_verified_report(
            events_payload(bootstrap=True),
            event_delta(bootstrap=True),
            vulnerability_intelligence(),
            {"items": []},
        )
        self.assertIn("Event State bootstrap", report)
        self.assertIn("不把整個視窗中的事件誤稱為", report)

    def test_grounded_prompt_excludes_discovery_only_event_and_masks_unverified_cve(self):
        prompt = build_event_report_prompt(
            events_payload(), event_delta(), vulnerability_intelligence(), {"items": []}
        )
        self.assertIn("CVE-2026-12345", prompt)
        self.assertNotIn("CVE-2026-99999", prompt)
        self.assertNotIn("Unconfirmed discovery item", prompt)
        self.assertIn("VERIFIED_EVENT_FACTS", prompt)

    def test_deterministic_report_labels_unverified_source_cve_as_unverified(self):
        report = render_event_first_verified_report(
            events_payload(), event_delta(), vulnerability_intelligence(), {"items": []}
        )
        self.assertIn("CVE-2026-99999", report)
        self.assertIn("尚未驗證", report)


if __name__ == "__main__":
    unittest.main()
