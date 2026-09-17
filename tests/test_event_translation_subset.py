from __future__ import annotations

import sys
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from enrich_events_zh import _merge_batch  # noqa: E402


class EventTranslationSubsetTests(unittest.TestCase):
    def test_only_translated_batch_is_merged_into_full_event_list(self):
        payload = {
            "items": [
                {"id": "event-1", "title": "English one", "summary": "Summary one"},
                {"id": "event-2", "title": "English two", "summary": "Summary two"},
                {"id": "event-3", "title": "English three", "summary": "Summary three"},
            ]
        }
        translated_batch = {
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
            ]
        }

        result = deepcopy(payload)
        merged = _merge_batch(result, translated_batch)

        self.assertEqual(merged, 2)
        self.assertEqual(result["items"][0]["title_zh"], "中文一")
        self.assertEqual(result["items"][1]["summary_zh"], "摘要二")
        self.assertNotIn("title_zh", result["items"][2])


if __name__ == "__main__":
    unittest.main()
