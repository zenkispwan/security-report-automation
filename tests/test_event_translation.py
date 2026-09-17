from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.llm.event_translation import (  # noqa: E402
    build_translation_prompt,
    merge_translations,
    translate_events,
)


class EventTranslationTests(unittest.TestCase):
    def setUp(self):
        self.payload = {
            "items": [
                {
                    "id": "event-1",
                    "title": "Critical ScreenConnect flaw actively exploited in attacks",
                    "summary": "CISA says CVE-2026-84869 is exploited in the wild.",
                    "related_cves": ["CVE-2026-84869"],
                    "source_name": "Example",
                    "source_url": "https://example.com/story",
                }
            ]
        }

    def test_prompt_requires_translation_without_new_facts(self):
        prompt = build_translation_prompt(self.payload)
        self.assertIn("do not add, infer, remove, or update facts", prompt)
        self.assertIn("CVE-2026-84869", prompt)
        self.assertIn("Traditional Chinese", prompt)

    def test_valid_translation_is_added_without_overwriting_source(self):
        translated = {
            "items": [
                {
                    "id": "event-1",
                    "title_zh": "ConnectWise ScreenConnect 重大漏洞遭實際利用",
                    "summary_zh": "CISA 表示 CVE-2026-84869 已在野外遭到利用。",
                }
            ]
        }
        result, accepted, rejected = merge_translations(self.payload, translated, model="test-model")
        item = result["items"][0]
        self.assertEqual(accepted, 1)
        self.assertEqual(rejected, [])
        self.assertEqual(item["title"], self.payload["items"][0]["title"])
        self.assertEqual(item["summary"], self.payload["items"][0]["summary"])
        self.assertEqual(item["title_zh"], "ConnectWise ScreenConnect 重大漏洞遭實際利用")
        self.assertEqual(result["translation"]["status"], "translated")

    def test_translation_with_changed_cve_is_rejected(self):
        translated = {
            "items": [
                {
                    "id": "event-1",
                    "title_zh": "ConnectWise ScreenConnect 重大漏洞遭實際利用",
                    "summary_zh": "CISA 表示 CVE-2026-99999 已在野外遭到利用。",
                }
            ]
        }
        result, accepted, rejected = merge_translations(self.payload, translated, model="test-model")
        self.assertEqual(accepted, 0)
        self.assertEqual(rejected, ["event-1"])
        self.assertNotIn("title_zh", result["items"][0])
        self.assertEqual(result["translation"]["status"], "source_only")

    def test_empty_source_summary_cannot_gain_generated_summary(self):
        payload = {"items": [{"id": "event-2", "title": "Vendor advisory", "summary": None}]}
        translated = {
            "items": [
                {
                    "id": "event-2",
                    "title_zh": "廠商公告",
                    "summary_zh": "模型自行加入了不存在的摘要。",
                }
            ]
        }
        result, accepted, _ = merge_translations(payload, translated, model="test-model")
        self.assertEqual(accepted, 0)
        self.assertNotIn("summary_zh", result["items"][0])

    def test_missing_api_key_falls_back_to_source_text(self):
        result = translate_events(self.payload, api_key=None, model="test-model")
        self.assertEqual(result["translation"]["status"], "source_only")
        self.assertEqual(result["translation"]["fallback_reason"], "missing_api_key")
        self.assertNotIn("title_zh", result["items"][0])


if __name__ == "__main__":
    unittest.main()
