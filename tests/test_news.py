from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.collectors.news import (  # noqa: E402
    classify_event,
    extract_cves,
    parse_feed,
    priority_for,
)


RSS = """<?xml version=\"1.0\"?>
<rss version=\"2.0\">
  <channel>
    <title>Example</title>
    <item>
      <title>Critical ScreenConnect flaw actively exploited in attacks</title>
      <link>https://example.com/story</link>
      <pubDate>Wed, 16 Sep 2026 07:14:00 +0000</pubDate>
      <description><![CDATA[Attackers exploit CVE-2026-84869 in the wild.]]></description>
    </item>
  </channel>
</rss>
"""


class NewsCollectorTests(unittest.TestCase):
    def test_extract_cves_normalizes_and_deduplicates(self):
        self.assertEqual(
            extract_cves("cve-2026-84869 and CVE-2026-84869 CVE-2026-20079"),
            ["CVE-2026-20079", "CVE-2026-84869"],
        )

    def test_parse_feed_reads_rss_item(self):
        rows = parse_feed(
            RSS,
            {"name": "Example", "source_type": "security_media", "url": "https://example.com/feed"},
        )
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["title"], "Critical ScreenConnect flaw actively exploited in attacks")
        self.assertEqual(rows[0]["source_name"], "Example")
        self.assertIn("CVE-2026-84869", rows[0]["summary"])

    def test_active_exploitation_has_priority_over_generic_threat_activity(self):
        text = "Hackers are actively exploited in attacks using CVE-2026-84869"
        event_type = classify_event(text, ["CVE-2026-84869"])
        self.assertEqual(event_type, "ACTIVE_EXPLOITATION")
        self.assertEqual(priority_for(event_type, text), "CRITICAL")

    def test_cve_article_without_attack_keywords_is_vulnerability_news(self):
        event_type = classify_event("Vendor publishes patch for CVE-2026-12345", ["CVE-2026-12345"])
        self.assertEqual(event_type, "VULNERABILITY_NEWS")

    def test_unrelated_article_is_not_event(self):
        self.assertIsNone(classify_event("Product release notes and feature updates", []))


if __name__ == "__main__":
    unittest.main()
