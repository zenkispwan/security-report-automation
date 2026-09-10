from __future__ import annotations

from typing import Any

from security_intel.http import HttpClient

CISA_KEV_URL = (
    "https://www.cisa.gov/sites/default/files/feeds/"
    "known_exploited_vulnerabilities.json"
)
CISA_KEV_MIRROR = (
    "https://raw.githubusercontent.com/cisagov/kev-data/develop/"
    "known_exploited_vulnerabilities.json"
)


class CisaKevCollector:
    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def collect(self) -> tuple[dict[str, Any], str]:
        errors: list[str] = []
        for url in (CISA_KEV_URL, CISA_KEV_MIRROR):
            try:
                payload = self.client.get_json(url)
                vulnerabilities = payload.get("vulnerabilities")
                if not isinstance(vulnerabilities, list):
                    raise ValueError("missing vulnerabilities[]")
                if (
                    payload.get("count") is not None
                    and payload["count"] != len(vulnerabilities)
                ):
                    raise ValueError("catalog count mismatch")
                return payload, url
            except Exception as exc:
                errors.append(f"{url}: {exc}")
        raise RuntimeError("CISA KEV collection failed: " + " | ".join(errors))
