from __future__ import annotations

import unittest
from unittest.mock import patch

from scripts.enrich_events_zh import enrich_in_batches


class EventEnrichmentBatchTests(unittest.TestCase):
    @staticmethod
    def fake_translate(batch_payload, **_kwargs):
        items = []
        for item in batch_payload["items"]:
            items.append(
                {
                    **item,
                    "title_zh": f"中文 {item['title']}",
                    "summary_zh": f"中文 {item['summary']}",
                }
            )
        return {
            "items": items,
            "translation": {
                "status": "translated",
                "provider": "gemini",
                "model": "test-model",
                "translated_items": len(items),
                "total_items": len(items),
                "rejected_item_ids": [],
                "fallback_reason": None,
            },
        }

    def test_translates_entire_feed_in_batches(self):
        payload = {
            "items": [
                {"id": f"event-{i}", "title": f"Title {i}", "summary": f"Summary {i}"}
                for i in range(7)
            ]
        }

        with patch("scripts.enrich_events_zh.translate_events", side_effect=self.fake_translate) as mocked:
            result = enrich_in_batches(
                payload,
                api_key="key",
                model="test-model",
                fallback_models=[],
                timeout_ms=1000,
                max_items=0,
                batch_size=3,
            )

        self.assertEqual(mocked.call_count, 3)
        self.assertEqual(result["translation"]["translated_items"], 7)
        self.assertEqual(result["translation"]["cached_items"], 0)
        self.assertEqual(result["translation"]["attempted_items"], 7)
        self.assertEqual(result["translation"]["status"], "translated")
        self.assertTrue(all(item.get("title_zh") for item in result["items"]))

    def test_cached_translations_are_not_sent_to_model_again(self):
        payload = {
            "items": [
                {
                    "id": f"event-{i}",
                    "title": f"Title {i}",
                    "summary": f"Summary {i}",
                    **(
                        {
                            "title_zh": f"中文 Title {i}",
                            "summary_zh": f"中文 Summary {i}",
                        }
                        if i < 5
                        else {}
                    ),
                }
                for i in range(7)
            ]
        }

        with patch("scripts.enrich_events_zh.translate_events", side_effect=self.fake_translate) as mocked:
            result = enrich_in_batches(
                payload,
                api_key="key",
                model="test-model",
                fallback_models=[],
                timeout_ms=1000,
                max_items=0,
                batch_size=3,
            )

        self.assertEqual(mocked.call_count, 1)
        sent_items = mocked.call_args.args[0]["items"]
        self.assertEqual([item["id"] for item in sent_items], ["event-5", "event-6"])
        self.assertEqual(result["translation"]["cached_items"], 5)
        self.assertEqual(result["translation"]["attempted_items"], 2)
        self.assertEqual(result["translation"]["translated_items"], 7)
        self.assertEqual(result["translation"]["pending_items"], 0)


if __name__ == "__main__":
    unittest.main()
