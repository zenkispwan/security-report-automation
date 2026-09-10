from __future__ import annotations

import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.intelligence import build_outputs, detect_events, score_item  # noqa: E402


def item(
    cve: str,
    *,
    published: str = "2026-09-10T02:00:00+00:00",
    cvss: float | None = 9.8,
    epss: float | None = 0.1,
    percentile: float | None = 0.9,
    kev: bool = False,
    exploit: str = "unconfirmed",
    ransomware: str | None = None,
) -> dict:
    return {
        "cve": cve,
        "vendor": "Example",
        "product": "Widget",
        "title": None,
        "description": "Example vulnerability",
        "cvss": None if cvss is None else {
            "version": "3.1",
            "score": cvss,
            "severity": "CRITICAL" if cvss >= 9 else "HIGH",
            "vector": None,
            "source": "nvd@nist.gov",
            "type": "Primary",
        },
        "epss": epss,
        "epss_percentile": percentile,
        "cisa_kev": {
            "listed": kev,
            "known_ransomware_campaign_use": ransomware,
        },
        "exploitation_status": {"status": exploit, "source": "test"},
        "published_time": published,
        "updated_time": published,
        "source_url": f"https://nvd.nist.gov/vuln/detail/{cve}",
        "source_type": ["nvd"],
        "cwes": [],
        "provenance": {},
        "change_flags": {
            "newly_published": True,
            "recently_modified": True,
            "new_kev": kev,
        },
    }


class IntelligenceTests(unittest.TestCase):
    def test_new_kev_is_p1(self) -> None:
        current = item("CVE-2026-10001", kev=True, exploit="known_exploited")
        previous = item("CVE-2026-10001", published="2026-09-08T00:00:00+00:00", kev=False)
        events = detect_events(
            current,
            previous,
            datetime(2026, 9, 9, tzinfo=timezone.utc),
        )
        self.assertIn("NEW_KEV", {x["type"] for x in events})
        risk = score_item(current, events)
        self.assertEqual(risk["priority"], "P1")
        self.assertGreaterEqual(risk["score"], 85)

    def test_epss_jump_is_detected(self) -> None:
        current = item("CVE-2026-10002", epss=0.42)
        previous = item("CVE-2026-10002", epss=0.05)
        events = detect_events(
            current,
            previous,
            datetime(2026, 9, 10, 1, tzinfo=timezone.utc),
        )
        epss_events = [x for x in events if x["type"] == "EPSS_INCREASED"]
        self.assertEqual(len(epss_events), 1)
        self.assertAlmostEqual(epss_events[0]["delta"], 0.37)

    def test_missing_current_item_is_not_reported_as_resolved(self) -> None:
        previous_state = {
            "generated_at": "2026-09-09T01:00:00+00:00",
            "items": {
                "CVE-2026-10003": item(
                    "CVE-2026-10003",
                    published="2026-09-08T00:00:00+00:00",
                    cvss=8.0,
                )
            },
        }
        current_snapshot = {
            "generated_at": "2026-09-10T01:00:00+00:00",
            "items": [],
        }
        _, delta, _ = build_outputs(current_snapshot, previous_state=previous_state)
        self.assertEqual(delta["summary"]["meaningful_change_count"], 0)
        self.assertEqual(delta["items"], [])

    def test_intelligence_is_capped_at_30(self) -> None:
        current_snapshot = {
            "generated_at": "2026-09-10T03:00:00+00:00",
            "items": [item(f"CVE-2026-{20000+i}", epss=0.6) for i in range(60)],
        }
        previous = {
            "generated_at": "2026-09-10T01:00:00+00:00",
            "items": [],
        }
        state, delta, intelligence = build_outputs(
            current_snapshot,
            previous_snapshot=previous,
        )
        self.assertLessEqual(state["tracked_count"], 1000)
        self.assertLessEqual(len(delta["items"]), 200)
        self.assertEqual(len(intelligence["items"]), 30)


if __name__ == "__main__":
    unittest.main()
