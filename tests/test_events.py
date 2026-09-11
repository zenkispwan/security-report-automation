from __future__ import annotations

import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.events import (  # noqa: E402
    build_event_outputs,
    canonical_url,
    cluster_articles,
    normalize_article,
    priority_for,
    verification_status,
)


PROFILE = {
    "profile_name": "test",
    "lookback_hours": 24,
    "geographies": ["Taiwan", "APAC"],
    "technology_keywords": ["Cisco"],
    "industry_keywords": [],
    "priority_event_types": ["active_exploitation", "ransomware", "supply_chain", "data_breach"],
    "asset_classes": {"network_edge": ["firewall", "vpn"]},
    "source_policy": {
        "official_domains": ["example-vendor.com", "twcert.org.tw"],
        "trusted_media_domains": ["news-a.example", "news-b.example"],
    },
}
NOW = datetime(2026, 9, 10, 15, 0, tzinfo=timezone.utc)


class EventIntelligenceTests(unittest.TestCase):
    def test_same_cve_articles_cluster(self):
        rows = [
            normalize_article({
                "title": "Vendor confirms active exploitation of CVE-2026-12345",
                "url": "https://example-vendor.com/advisory",
                "published_time": "2026-09-10T12:00:00+00:00",
                "authority": "official",
            }, PROFILE),
            normalize_article({
                "title": "Attackers exploit CVE-2026-12345 in the wild",
                "url": "https://news-a.example/story",
                "published_time": "2026-09-10T13:00:00+00:00",
                "authority": "trusted_media",
            }, PROFILE),
        ]
        clusters = cluster_articles([x for x in rows if x])
        self.assertEqual(1, len(clusters))
        self.assertEqual(2, len(clusters[0]))

    def test_official_source_confirms_event(self):
        status = verification_status([
            {"domain": "example-vendor.com", "authority": "official"},
        ])
        self.assertEqual("official_confirmed", status["status"])
        self.assertEqual("high", status["confidence"])

    def test_two_trusted_domains_are_corroborated(self):
        status = verification_status([
            {"domain": "news-a.example", "authority": "trusted_media"},
            {"domain": "news-b.example", "authority": "trusted_media"},
        ])
        self.assertEqual("corroborated", status["status"])

    def test_discovery_only_event_can_never_be_actionable_priority(self):
        self.assertEqual("WATCH", priority_for(100, "discovery_only"))
        _, events, delta = build_event_outputs([
            {
                "title": "Cisco firewall under active exploitation in Taiwan",
                "url": "https://unknown-source.example/a",
                "published_time": "2026-09-10T14:30:00+00:00",
                "authority": "discovery",
            }
        ], PROFILE, vulnerability_intelligence={"items": []}, previous_state={"generated_at": "2026-09-10T12:00:00+00:00", "items": {}}, now=NOW)
        self.assertEqual("WATCH", events["items"][0]["priority"])
        self.assertEqual([], delta["items"])

    def test_single_trusted_source_is_capped_at_p3(self):
        self.assertEqual("P3", priority_for(100, "single_trusted_source"))

    def test_bootstrap_builds_event_list_but_not_false_daily_delta(self):
        _, events, delta = build_event_outputs([
            {
                "title": "Vendor confirms ransomware incident",
                "url": "https://example-vendor.com/a",
                "published_time": "2026-09-10T14:00:00+00:00",
                "authority": "official",
            }
        ], PROFILE, vulnerability_intelligence={"items": []}, previous_state=None, now=NOW)
        self.assertEqual(1, len(events["items"]))
        self.assertTrue(events["items"][0]["is_new"])
        self.assertEqual("bootstrap", delta["mode"])
        self.assertFalse(delta["baseline"]["available"])
        self.assertEqual(0, delta["summary"]["new_notable_count"])
        self.assertEqual([], delta["items"])

    def test_unverified_cve_mention_is_not_linked(self):
        _, events, _ = build_event_outputs([
            {
                "title": "CVE-2026-99999 reportedly used in attack",
                "url": "https://news-a.example/a",
                "published_time": "2026-09-10T14:00:00+00:00",
                "authority": "trusted_media",
            }
        ], PROFILE, vulnerability_intelligence={"items": []}, verified_cves=set(), now=NOW)
        item = events["items"][0]
        self.assertEqual(["CVE-2026-99999"], item["unverified_cve_mentions"])
        self.assertEqual([], item["confirmed_cves"])
        self.assertEqual([], item["linked_vulnerabilities"])

    def test_profile_match_changes_relevance_without_claiming_asset_presence(self):
        _, events, _ = build_event_outputs([
            {
                "title": "Cisco firewall under active exploitation in Taiwan",
                "url": "https://example-vendor.com/a",
                "published_time": "2026-09-10T14:30:00+00:00",
                "authority": "official",
            }
        ], PROFILE, vulnerability_intelligence={"items": []}, now=NOW)
        relevance = events["items"][0]["relevance"]
        self.assertEqual("high", relevance["level"])
        self.assertEqual("profile_matched", relevance["scope"])
        self.assertIn("Cisco", relevance["technology_matches"])
        self.assertIn("Taiwan", relevance["geography_matches"])

    def test_previous_fingerprint_prevents_repeat_new_event(self):
        _, first_events, _ = build_event_outputs([
            {
                "title": "Vendor confirms ransomware incident",
                "url": "https://example-vendor.com/a",
                "published_time": "2026-09-10T14:00:00+00:00",
                "authority": "official",
            }
        ], PROFILE, vulnerability_intelligence={"items": []}, now=NOW)
        item = first_events["items"][0]
        previous_state = {
            "generated_at": "2026-09-10T14:05:00+00:00",
            "items": {
                item["fingerprint"]: {
                    "event_id": item["event_id"],
                    "first_seen": item["first_seen"],
                    "last_seen": item["last_seen"],
                    "event_type": item["event_type"],
                    "cves": item["cves"],
                    "title": item["title"],
                }
            }
        }
        _, second_events, second_delta = build_event_outputs([
            {
                "title": "Vendor confirms ransomware incident",
                "url": "https://example-vendor.com/a?utm_source=x",
                "published_time": "2026-09-10T14:30:00+00:00",
                "authority": "official",
            }
        ], PROFILE, vulnerability_intelligence={"items": []}, previous_state=previous_state, now=NOW)
        self.assertFalse(second_events["items"][0]["is_new"])
        self.assertEqual("delta", second_delta["mode"])
        self.assertEqual(0, second_delta["summary"]["new_notable_count"])

    def test_tracking_parameters_are_removed(self):
        self.assertEqual(
            "https://example.com/a?id=1",
            canonical_url("https://example.com/a?utm_source=x&id=1#fragment"),
        )


if __name__ == "__main__":
    unittest.main()
