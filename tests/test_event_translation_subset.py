from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from enrich_events_zh import _merge_translation_subset  # noqa: E402


class EventTranslationSubsetTests(unittest.TestCase):
    def test_only_translated_subset_is_merged_into_full_event_list(self):
        payload = {
            "items": [
                {"id": "event-1", "title": "English one", "summary": "Summary one"},
                {"id": "event-2", "title": "English two", "summary": "Summary two"},
                {"id": "event-3", "title": "English three", "summary": "Summary three"},
            ]
        }
        translated_subset = {
            "items": [
                {
                    "id": "event-1",
                    "title": "English one",
                    "summary": "Summary one",
                    "title_zh": "中文一",
                    "summary_zh": "摘要一",
                },
                {
                    "id": "event-2",
                    "title": "English two",
                    "summary": "Summary two",
                    "title_zh": "中文二",
                    "summary_zh": "摘要二",
                },
            ],
            "translation": {
                "language": "zh-Hant-TW",
                "status": "translated",
                "provider": "gemini",
                "model": "test-model",
                "translated_items": 2,
                "total_items": 2,
                "rejected_item_ids": [],
                "fallback_reason": None,
            },
        }

        result = _merge_translation_subset(payload, translated_subset, attempted_items=2)

        self.assertEqual(result["items"][0]["title_zh"], "中文一")
        self.assertEqual(result["items"][1]["summary_zh"], "摘要二")
        self.assertNotIn("title_zh", result["items"][2])
        self.assertEqual(result["translation"]["status"], "partial")
        self.assertEqual(result["translation"]["attempted_items"], 2)
        self.assertEqual(result["translation"]["translated_items"], 2)
        self.assertEqual(result["translation"]["total_items"], 3)


if __name__ == "__main__":
    unittest.main()
