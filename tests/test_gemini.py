from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.llm.gemini import (  # noqa: E402
    FACTS_ONLY_SYSTEM_SUFFIX,
    _is_quota_error,
)


class FakeRateLimitError(Exception):
    pass


class FakeAuthError(Exception):
    pass


class GeminiAdapterTests(unittest.TestCase):
    def test_quota_error_detection_allows_only_rate_limit_fallback(self) -> None:
        quota = FakeRateLimitError("429 too_many_requests: exceeded your current quota")
        auth = FakeAuthError("401 invalid API key")
        self.assertTrue(_is_quota_error(quota))
        self.assertFalse(_is_quota_error(auth))

    def test_facts_only_instruction_forbids_model_memory_for_recent_facts(self) -> None:
        self.assertIn("不得使用模型既有知識", FACTS_ONLY_SYSTEM_SUFFIX)
        self.assertIn("只能重述與分析 VERIFIED_FACTS", FACTS_ONLY_SYSTEM_SUFFIX)
        self.assertIn("未確認", FACTS_ONLY_SYSTEM_SUFFIX)
        self.assertIn("不得暗示本次已進行即時網路搜尋", FACTS_ONLY_SYSTEM_SUFFIX)


if __name__ == "__main__":
    unittest.main()
