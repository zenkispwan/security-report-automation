from __future__ import annotations

import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.normalize import normalize_record  # noqa: E402


class NormalizeTests(unittest.TestCase):
    def test_high_epss_does_not_mean_exploited(self) -> None:
        start = datetime(2026, 9, 9, tzinfo=timezone.utc)
        end = datetime(2026, 9, 10, tzinfo=timezone.utc)
        row = normalize_record(
            nvd_wrapper={"cve": {"id": "CVE-2026-12345"}},
            kev_entry=None,
            epss_entry={"cve": "CVE-2026-12345", "epss": "0.99", "percentile": "0.999"},
            collected_at=end,
            window_start=start,
            window_end=end,
        )
        self.assertFalse(row["cisa_kev"]["listed"])
        self.assertEqual(row["exploitation_status"]["status"], "unconfirmed")

    def test_kev_is_known_exploited(self) -> None:
        start = datetime(2026, 9, 9, tzinfo=timezone.utc)
        end = datetime(2026, 9, 10, 23, 59, tzinfo=timezone.utc)
        row = normalize_record(
            nvd_wrapper={"cve": {"id": "CVE-2026-54321"}},
            kev_entry={
                "cveID": "CVE-2026-54321",
                "vendorProject": "Vendor",
                "product": "Product",
                "dateAdded": "2026-09-10",
            },
            epss_entry=None,
            collected_at=end,
            window_start=start,
            window_end=end,
        )
        self.assertTrue(row["cisa_kev"]["listed"])
        self.assertEqual(row["exploitation_status"]["status"], "known_exploited")

    def test_cvss_prefers_v4(self) -> None:
        now = datetime(2026, 9, 10, tzinfo=timezone.utc)
        row = normalize_record(
            nvd_wrapper={"cve": {
                "id": "CVE-2026-11111",
                "metrics": {
                    "cvssMetricV31": [{"type": "Primary", "cvssData": {"version": "3.1", "baseScore": 9.8, "baseSeverity": "CRITICAL"}}],
                    "cvssMetricV40": [{"type": "Primary", "cvssData": {"version": "4.0", "baseScore": 8.7, "baseSeverity": "HIGH"}}],
                },
            }},
            kev_entry=None,
            epss_entry=None,
            collected_at=now,
            window_start=now,
            window_end=now,
        )
        self.assertEqual(row["cvss"]["version"], "4.0")
        self.assertEqual(row["cvss"]["score"], 8.7)

    def test_nvd_2026_affected_data_is_flattened(self) -> None:
        now = datetime(2026, 9, 10, tzinfo=timezone.utc)
        row = normalize_record(
            nvd_wrapper={"cve": {
                "id": "CVE-2026-22222",
                "affected": [{
                    "source": "vendor@example.com",
                    "affectedData": [{
                        "vendor": "Example Vendor",
                        "product": "Example Product",
                        "versions": [{"version": "1.0", "status": "affected"}],
                    }],
                }],
            }},
            kev_entry=None,
            epss_entry=None,
            collected_at=now,
            window_start=now,
            window_end=now,
        )
        self.assertEqual(row["vendor"], "Example Vendor")
        self.assertEqual(row["product"], "Example Product")
        self.assertEqual(row["affected"][0]["source"], "vendor@example.com")


if __name__ == "__main__":
    unittest.main()
