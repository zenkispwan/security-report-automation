from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from security_intel.http import HttpClient

GDELT_DOC_API = "https://api.gdeltproject.org/api/v2/doc/doc"


def collect_gdelt_articles(
    queries: list[str],
    *,
    lookback_hours: int = 24,
    max_records_per_query: int = 75,
    client: HttpClient | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    client = client or HttpClient(timeout=45, retries=2)
    collected_at = datetime.now(timezone.utc).isoformat()
    rows: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []

    for query in queries:
        try:
            payload = client.get_json(
                GDELT_DOC_API,
                params={
                    "query": query,
                    "mode": "artlist",
                    "maxrecords": max_records_per_query,
                    "timespan": f"{lookback_hours}h",
                    "sort": "datedesc",
                    "format": "json",
                },
                headers={"Accept": "application/json"},
            )
        except Exception as exc:  # one discovery query must not break the whole brief
            errors.append({"query": query, "error": f"{type(exc).__name__}: {exc}"})
            continue

        for article in payload.get("articles") or []:
            if not isinstance(article, dict):
                continue
            url = article.get("url")
            title = article.get("title")
            if not url or not title:
                continue
            rows.append(
                {
                    "title": title,
                    "url": url,
                    "domain": article.get("domain"),
                    "published_time": _gdelt_time(article.get("seendate")),
                    "language": article.get("language"),
                    "source_country": article.get("sourcecountry"),
                    "source_name": article.get("domain") or "GDELT discovery",
                    "source_type": "news_search",
                    "authority": "discovery",
                    "discovery_query": query,
                    "collected_time": collected_at,
                }
            )

    return rows, errors


def _gdelt_time(value: Any) -> str | None:
    if not value:
        return None
    raw = str(value).strip()
    for fmt in ("%Y%m%dT%H%M%SZ", "%Y%m%d%H%M%S"):
        try:
            return datetime.strptime(raw, fmt).replace(tzinfo=timezone.utc).isoformat()
        except ValueError:
            pass
    return raw
