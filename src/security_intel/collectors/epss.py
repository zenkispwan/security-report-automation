from __future__ import annotations

from typing import Any, Iterable

from security_intel.http import HttpClient

EPSS_API = "https://api.first.org/data/v1/epss"
MAX_PARAM_LENGTH = 1800


class EpssCollector:
    def __init__(self, client: HttpClient) -> None:
        self.client = client

    def collect(
        self, cve_ids: Iterable[str]
    ) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
        ids = sorted({x for x in cve_ids if x})
        scores: dict[str, dict[str, Any]] = {}
        raw: list[dict[str, Any]] = []

        for batch in self._chunks(ids):
            payload = self.client.get_json(EPSS_API, params={"cve": ",".join(batch)})
            raw.append(payload)
            rows = payload.get("data", [])
            if not isinstance(rows, list):
                raise ValueError("EPSS response missing data[]")
            for row in rows:
                if row.get("cve"):
                    scores[row["cve"]] = row

        return scores, raw

    @staticmethod
    def _chunks(ids: list[str]) -> list[list[str]]:
        out: list[list[str]] = []
        current: list[str] = []
        length = 0
        for cve_id in ids:
            extra = len(cve_id) + (1 if current else 0)
            if current and length + extra > MAX_PARAM_LENGTH:
                out.append(current)
                current, length = [], 0
            current.append(cve_id)
            length += extra
        if current:
            out.append(current)
        return out
