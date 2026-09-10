from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_intel.llm.gemini import (  # noqa: E402
    _deterministic_facts_only_response,
    _generate_content_with_model_fallback,
    _is_quota_error,
    _is_search_fallback_error,
    _is_transient_error,
    _model_candidates,
    _parse_generate_content,
    generate_grounded_markdown,
)


class FakeRateLimitError(Exception):
    pass


class FakeAuthError(Exception):
    pass


class APIConnectionError(Exception):
    pass


class FakeServerError(Exception):
    def __init__(self, message: str, status_code: int = 503) -> None:
        super().__init__(message)
        self.status_code = status_code


class FakeConfig:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs


class FakeTypes:
    GenerateContentConfig = FakeConfig

    class GoogleSearch:
        pass

    class Tool:
        def __init__(self, **kwargs) -> None:
            self.kwargs = kwargs


class FakeModels:
    def __init__(self, behavior: dict[str, object]) -> None:
        self.behavior = behavior
        self.calls: list[str] = []

    def generate_content(self, *, model, contents, config):
        self.calls.append(model)
        result = self.behavior[model]
        if isinstance(result, Exception):
            raise result
        return result


class GeminiAdapterTests(unittest.TestCase):
    def test_search_off_returns_deterministic_decision_without_llm_body(self) -> None:
        response = generate_grounded_markdown(
            api_key="",
            model="gemini-3.8-flash",
            fallback_models=["gemini-3.7-flash"],
            prompt="verified facts",
            system_instruction="strict",
            search_mode="off",
        )
        self.assertEqual(response.api_mode, "deterministic_facts_only")
        self.assertEqual(response.grounding_mode, "verified_facts_only")
        self.assertEqual(response.grounding_fallback_reason, "google_search_disabled")
        self.assertEqual(response.text, "")
        self.assertIsNone(response.model)
        self.assertEqual(response.attempted_models, [])
        self.assertIsNone(response.usage)
        self.assertIsNone(response.interaction_id)

    def test_deterministic_response_never_contains_model_generated_text(self) -> None:
        response = _deterministic_facts_only_response(
            requested_model="gemini-3.8-flash",
            attempted_models=["gemini-3.8-flash"],
            fallback_reason="google_search_quota_unavailable",
        )
        self.assertEqual(response.text, "")
        self.assertIsNone(response.model)
        self.assertIsNone(response.usage)
        self.assertEqual(response.attempted_models, ["gemini-3.8-flash"])
        self.assertEqual(response.api_mode, "deterministic_facts_only")

    def test_quota_error_detection_allows_search_fallback(self) -> None:
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

    def test_model_candidates_are_ordered_and_deduplicated(self) -> None:
        self.assertEqual(
            _model_candidates(
                "gemini-3.8-flash",
                ["gemini-3.7-flash", "gemini-3.8-flash", "gemini-3.6-flash"],
            ),
            ["gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.6-flash"],
        )

    def test_transient_search_503_moves_to_next_model(self) -> None:
        success = SimpleNamespace(text="grounded fallback succeeded")
        models = FakeModels(
            {
                "gemini-3.8-flash": FakeServerError("503 UNAVAILABLE: high demand"),
                "gemini-3.7-flash": success,
            }
        )
        client = SimpleNamespace(models=models)

        response, selected, attempted = _generate_content_with_model_fallback(
            client=client,
            types=FakeTypes,
            models=["gemini-3.8-flash", "gemini-3.7-flash"],
            prompt="search",
            system_instruction="strict",
            use_search=True,
            fallback_on_quota=False,
        )

        self.assertIs(response, success)
        self.assertEqual(selected, "gemini-3.7-flash")
        self.assertEqual(attempted, ["gemini-3.8-flash", "gemini-3.7-flash"])
        self.assertEqual(models.calls, attempted)

    def test_auth_error_does_not_try_next_model(self) -> None:
        auth = FakeAuthError("401 invalid API key")
        auth.status_code = 401
        models = FakeModels(
            {
                "gemini-3.8-flash": auth,
                "gemini-3.7-flash": SimpleNamespace(text="must not run"),
            }
        )
        client = SimpleNamespace(models=models)

        with self.assertRaises(FakeAuthError):
            _generate_content_with_model_fallback(
                client=client,
                types=FakeTypes,
                models=["gemini-3.8-flash", "gemini-3.7-flash"],
                prompt="search",
                system_instruction="strict",
                use_search=True,
                fallback_on_quota=False,
            )
        self.assertEqual(models.calls, ["gemini-3.8-flash"])

    def test_search_quota_does_not_rotate_models(self) -> None:
        quota = FakeRateLimitError("429 too_many_requests: exceeded your current quota")
        quota.status_code = 429
        models = FakeModels(
            {
                "gemini-3.8-flash": quota,
                "gemini-3.7-flash": SimpleNamespace(text="must not run"),
            }
        )
        client = SimpleNamespace(models=models)

        with self.assertRaises(FakeRateLimitError):
            _generate_content_with_model_fallback(
                client=client,
                types=FakeTypes,
                models=["gemini-3.8-flash", "gemini-3.7-flash"],
                prompt="search",
                system_instruction="strict",
                use_search=True,
                fallback_on_quota=False,
            )
        self.assertEqual(models.calls, ["gemini-3.8-flash"])

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
            model="gemini-3.7-flash",
            requested_model="gemini-3.8-flash",
            attempted_models=["gemini-3.8-flash", "gemini-3.7-flash"],
            model_fallback_reason="transient_model_unavailable",
            grounding_mode="google_search",
            fallback_reason="interactions_transport_unavailable",
            api_mode="generate_content_search",
        )

        self.assertEqual(parsed.text, "Verified report text")
        self.assertEqual(parsed.interaction_id, "resp-123")
        self.assertEqual(parsed.model, "gemini-3.7-flash")
        self.assertEqual(parsed.requested_model, "gemini-3.8-flash")
        self.assertEqual(parsed.attempted_models, ["gemini-3.8-flash", "gemini-3.7-flash"])
        self.assertEqual(parsed.api_mode, "generate_content_search")
        self.assertEqual(parsed.search_queries, ["Cisco FMC CVE advisory"])
        self.assertEqual(parsed.citations[0]["url"], "https://example.com/advisory")
        self.assertEqual(parsed.citations[0]["cited_text"], "Verified")


if __name__ == "__main__":
    unittest.main()
