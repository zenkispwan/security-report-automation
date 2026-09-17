from __future__ import annotations

import unittest
from unittest.mock import patch

from scripts.enrich_events_zh import enrich_in_batches


class EventEnrichmentBatchTests(unittest.TestCase):
    def test_translates_entire_feed_in_batches(self):
        payload = {
            "items": [
                {"id": f"event-{i}", "title": f"Title {i}", "summary": f"Summary {i}"}
                for i in range(7)
            ]
        }

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

        with patch("scripts.enrich_events_zh.translate_events", side_effect=fake_translate) as mocked:
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
        self.assertEqual(result["translation"]["attempted_items"], 7)
        self.assertEqual(result["translation"]["status"], "translated")
        self.assertTrue(all(item.get("title_zh") for item in result["items"]))


if __name__ == "__main__":
    unittest.main()
