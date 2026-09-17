from __future__ import annotations

import unittest

from scripts.build_cve_enrichment_zh import source_fingerprint
from scripts.build_events import preserve_event_translations


class TranslationCacheTests(unittest.TestCase):
    def test_event_translation_is_preserved_only_when_source_text_is_unchanged(self):
        previous = {
            "items": [
                {
                    "id": "event-1",
                    "title": "Original title",
                    "summary": "Original summary",
                    "title_zh": "原始標題",
                    "summary_zh": "原始摘要",
                }
            ]
        }
        current = [
            {"id": "event-1", "title": "Original title", "summary": "Original summary"},
            {"id": "event-2", "title": "New title", "summary": "New summary"},
        ]

        preserved = preserve_event_translations(previous, current)

        self.assertEqual(preserved, 1)
        self.assertEqual(current[0]["title_zh"], "原始標題")
        self.assertEqual(current[0]["summary_zh"], "原始摘要")
        self.assertNotIn("title_zh", current[1])

    def test_event_translation_is_not_preserved_when_source_summary_changes(self):
        previous = {
            "items": [
                {
                    "id": "event-1",
                    "title": "Original title",
                    "summary": "Old summary",
                    "title_zh": "舊標題",
                    "summary_zh": "舊摘要",
                }
            ]
        }
        current = [{"id": "event-1", "title": "Original title", "summary": "Updated summary"}]

        preserved = preserve_event_translations(previous, current)

        self.assertEqual(preserved, 0)
        self.assertNotIn("title_zh", current[0])
        self.assertNotIn("summary_zh", current[0])

    def test_cve_source_fingerprint_is_stable_for_same_verified_text(self):
        item = {
            "cve": "CVE-2026-76460",
            "facts": {
                "title": "Cisco Identity Services Engine Vulnerability",
                "description": "Verified NVD description.",
            },
        }
        same = {
            "cve": "CVE-2026-76460",
            "facts": {
                "title": "Cisco Identity Services Engine Vulnerability",
                "description": "Verified NVD description.",
                "cvss": {"score": 10.0},
            },
        }

        self.assertEqual(source_fingerprint(item), source_fingerprint(same))

    def test_cve_source_fingerprint_changes_when_description_changes(self):
        before = {
            "cve": "CVE-2026-76460",
            "facts": {"title": "Title", "description": "Description A"},
        }
        after = {
            "cve": "CVE-2026-76460",
            "facts": {"title": "Title", "description": "Description B"},
        }

        self.assertNotEqual(source_fingerprint(before), source_fingerprint(after))


if __name__ == "__main__":
    unittest.main()
