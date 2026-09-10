from __future__ import annotations

import os
import time
from typing import Any

import requests

USER_AGENT = (
    "security-report-automation/2.0 "
    "(+https://github.com/zenkispwan/security-report-automation)"
)


class HttpClient:
    def __init__(self, timeout: int = 45, retries: int = 4) -> None:
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "User-Agent": os.getenv("SECURITY_INTEL_USER_AGENT", USER_AGENT),
            }
        )

    def get_json(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        for attempt in range(self.retries + 1):
            response = self.session.get(
                url, params=params, headers=headers, timeout=self.timeout
            )
            if response.status_code == 429 or 500 <= response.status_code < 600:
                if attempt == self.retries:
                    response.raise_for_status()
                retry_after = response.headers.get("Retry-After")
                delay = (
                    float(retry_after)
                    if retry_after and retry_after.isdigit()
                    else min(2 ** (attempt + 1), 30)
                )
                time.sleep(delay)
                continue

            response.raise_for_status()
            payload = response.json()
            if not isinstance(payload, dict):
                raise ValueError(f"Expected JSON object from {url}")
            return payload

        raise RuntimeError(f"Failed to fetch {url}")
