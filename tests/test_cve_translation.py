from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.llm.cve_translation import (  # noqa: E402
    build_cve_translation_prompt,
    translate_cve_batch,
    validate_cve_translations,
)


class CveTranslationTests(unittest.TestCase):
    def setUp(self):
        self.items = [
            {
                "cve": "CVE-2026-76460",
                "facts": {
                    "cve": "CVE-2026-76460",
                    "title": "Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability",
                    "description": "Cisco Identity Services Engine contains an incorrect use of privileged APIs vulnerability.",
                },
            }
        ]

    def test_prompt_is_translation_only(self):
        prompt = build_cve_translation_prompt(self.items)
        self.assertIn("do not add, infer", prompt.lower())
        self.assertIn("Traditional Chinese", prompt)
        self.assertIn("CVE-2026-76460", prompt)
        self.assertIn("Cisco Identity Services Engine", prompt)

    def test_valid_translation_keeps_source_cve_identity(self):
        translated = {
            "items": [
                {
                    "cve": "CVE-2026-76460",
                    "title_zh": "Cisco Identity Services Engine 特權 API 使用不當漏洞",
                    "description_zh": "Cisco Identity Services Engine 存在特權 API 使用不當漏洞。",
                }
            ]
        }
        accepted, rejected = validate_cve_translations(self.items, translated)
        self.assertEqual(len(accepted), 1)
        self.assertEqual(accepted[0]["cve"], "CVE-2026-76460")
        self.assertEqual(rejected, [])

    def test_translation_that_invents_cve_in_text_is_rejected(self):
        translated = {
            "items": [
                {
                    "cve": "CVE-2026-76460",
                    "title_zh": "Cisco Identity Services Engine 漏洞 CVE-2026-99999",
                    "description_zh": "Cisco Identity Services Engine 存在漏洞。",
                }
            ]
        }
        accepted, rejected = validate_cve_translations(self.items, translated)
        self.assertEqual(accepted, [])
        self.assertEqual(rejected, ["CVE-2026-76460"])

    def test_missing_api_key_falls_back_without_generated_text(self):
        result = translate_cve_batch(self.items, api_key=None, model="test-model")
        self.assertEqual(result["items"], [])
        self.assertEqual(result["fallback_reason"], "missing_api_key")


if __name__ == "__main__":
    unittest.main()
