from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.llm.gemini import (  # noqa: E402
    FACTS_ONLY_SYSTEM_SUFFIX,
    _is_quota_error,
    _is_search_fallback_error,
    _is_transient_error,
    _parse_generate_content,
)


class FakeRateLimitError(Exception):
    pass


class FakeAuthError(Exception):
    pass


class APIConnectionError(Exception):
    pass


class GeminiAdapterTests(unittest.TestCase):
    def test_quota_error_detection_allows_rate_limit_fallback(self) -> None:
        quota = FakeRateLimitError("429 too_many_requests: exceeded your current quota")
        auth = FakeAuthError("401 invalid API key")
        self.assertTrue(_is_quota_error(quota))
        self.assertFalse(_is_quota_error(auth))

    def test_transient_connection_error_can_fall_back_but_auth_cannot(self) -> None:
        transport = APIConnectionError("Server disconnected without sending a response")
        auth = FakeAuthError("401 invalid API key")
        self.assertTrue(_is_transient_error(transport))
        self.assertTrue(_is_search_fallback_error(transport))
        self.assertFalse(_is_transient_error(auth))
        self.assertFalse(_is_search_fallback_error(auth))

    def test_generate_content_grounding_metadata_is_preserved(self) -> None:
        response = SimpleNamespace(
            text="Verified report text",
            response_id="resp-123",
            usage_metadata={"prompt_token_count": 10, "candidates_token_count": 20},
            candidates=[
                SimpleNamespace(
                    grounding_metadata=SimpleNamespace(
                        web_search_queries=["Cisco FMC CVE advisory"],
                        grounding_chunks=[
                            SimpleNamespace(
                                web=SimpleNamespace(
                                    uri="https://example.com/advisory",
                                    title="Vendor advisory",
                                )
                            )
                        ],
                        grounding_supports=[
                            SimpleNamespace(
                                segment=SimpleNamespace(
                                    start_index=0,
                                    end_index=8,
                                    text="Verified",
                                ),
                                grounding_chunk_indices=[0],
                            )
                        ],
                    )
                )
            ],
        )

        parsed = _parse_generate_content(
            response=response,
            model="gemini-test",
            grounding_mode="google_search",
            fallback_reason="interactions_transport_unavailable",
            api_mode="generate_content_search",
        )

        self.assertEqual(parsed.text, "Verified report text")
        self.assertEqual(parsed.interaction_id, "resp-123")
        self.assertEqual(parsed.api_mode, "generate_content_search")
        self.assertEqual(parsed.search_queries, ["Cisco FMC CVE advisory"])
        self.assertEqual(parsed.citations[0]["url"], "https://example.com/advisory")
        self.assertEqual(parsed.citations[0]["cited_text"], "Verified")

    def test_facts_only_generate_content_may_have_no_grounding_metadata(self) -> None:
        response = SimpleNamespace(
            text="Facts-only report",
            response_id=None,
            usage_metadata=None,
            candidates=[SimpleNamespace(grounding_metadata=None)],
        )
        parsed = _parse_generate_content(
            response=response,
            model="gemini-test",
            grounding_mode="verified_facts_only",
            fallback_reason="google_search_quota_unavailable",
            api_mode="generate_content_facts_only",
        )
        self.assertEqual(parsed.citations, [])
        self.assertEqual(parsed.search_queries, [])
        self.assertEqual(parsed.grounding_mode, "verified_facts_only")

    def test_facts_only_instruction_forbids_model_memory_for_recent_facts(self) -> None:
        self.assertIn("不得使用模型既有知識", FACTS_ONLY_SYSTEM_SUFFIX)
        self.assertIn("只能重述與分析 VERIFIED_FACTS", FACTS_ONLY_SYSTEM_SUFFIX)
        self.assertIn("未確認", FACTS_ONLY_SYSTEM_SUFFIX)
        self.assertIn("不得暗示本次已進行即時網路搜尋", FACTS_ONLY_SYSTEM_SUFFIX)


if __name__ == "__main__":
    unittest.main()
