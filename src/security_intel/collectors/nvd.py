from __future__ import annotations

import os
import time
from datetime import datetime
from typing import Any

from security_intel.http import HttpClient

NVD_CVE_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"
NVD_DETAIL_URL = "https://nvd.nist.gov/vuln/detail/{cve_id}"


class NvdCollector:
    def __init__(self, client: HttpClient, api_key: str | None = None) -> None:
        self.client = client
        self.api_key = api_key or os.getenv("NVD_API_KEY")
        self.delay = 0.7 if self.api_key else 6.5
        self.last_request = 0.0

    def collect_recent_changes(self, start: datetime, end: datetime) -> dict[str, Any]:
        params: dict[str, Any] = {
            "lastModStartDate": start.isoformat(timespec="milliseconds"),
            "lastModEndDate": end.isoformat(timespec="milliseconds"),
            "resultsPerPage": 2000,
            "startIndex": 0,
        }
        rows: list[dict[str, Any]] = []

        while True:
            payload = self._request(params)
            page = payload.get("vulnerabilities", [])
            if not isinstance(page, list):
                raise ValueError("NVD response missing vulnerabilities[]")
            rows.extend(page)
            total = int(payload.get("totalResults", len(rows)))
            if not page or len(rows) >= total:
                break
            params["startIndex"] = len(rows)

        return {
            "format": "NVD_CVE",
            "version": "2.0",
            "totalResults": len(rows),
            "vulnerabilities": rows,
        }

    def fetch_cve(self, cve_id: str) -> dict[str, Any] | None:
        payload = self._request({"cveId": cve_id})
        rows = payload.get("vulnerabilities", [])
        return rows[0] if rows else None

    def _request(self, params: dict[str, Any]) -> dict[str, Any]:
        elapsed = time.monotonic() - self.last_request
        if self.last_request and elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        headers = {"apiKey": self.api_key} if self.api_key else None
        payload = self.client.get_json(NVD_CVE_API, params=params, headers=headers)
        self.last_request = time.monotonic()
        return payload
