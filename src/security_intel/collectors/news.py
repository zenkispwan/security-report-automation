from __future__ import annotations

import hashlib
import html
import re
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from typing import Iterable

import requests

from security_intel.http import USER_AGENT

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.IGNORECASE)
TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")

DEFAULT_NEWS_SOURCES = (
    {
        "name": "BleepingComputer",
        "url": "https://www.bleepingcomputer.com/feed/",
        "source_type": "security_media",
    },
    {
        "name": "SecurityWeek",
        "url": "https://www.securityweek.com/feed/",
        "source_type": "security_media",
    },
    {
        "name": "CISA Advisories",
        "url": "https://www.cisa.gov/cybersecurity-advisories/all.xml",
        "source_type": "official_advisory",
    },
    {
        "name": "CISA News",
        "url": "https://www.cisa.gov/news.xml",
        "source_type": "official_news",
    },
)

EVENT_KEYWORDS = {
    "RANSOMWARE": (
        "ransomware",
        "encryptor",
    ),
    "SUPPLY_CHAIN": (
        "supply chain",
        "supply-chain",
        "malicious update",
        "compromised maintainer",
        "third-party breach",
        "third party breach",
    ),
    "DATA_BREACH": (
        "data breach",
        "breach",
        "stolen data",
        "data stolen",
        "data leak",
        "leaked data",
    ),
    "ACTIVE_EXPLOITATION": (
        "actively exploited",
        "active exploitation",
        "exploited in attacks",
        "exploited in the wild",
        "under active attack",
        "zero-day",
        "zero day",
        "0-day",
    ),
    "THREAT_ACTIVITY": (
        "malware",
        "backdoor",
        "espionage",
        "threat actor",
        "threat actors",
        "hackers",
        "campaign",
        "phishing",
    ),
}

PRIORITY_ORDER = {"CRITICAL": 3, "HIGH": 2, "MEDIUM": 1}
EVENT_WEIGHT = {
    "RANSOMWARE": 100,
    "ACTIVE_EXPLOITATION": 95,
    "SUPPLY_CHAIN": 90,
    "DATA_BREACH": 85,
    "THREAT_ACTIVITY": 75,
    "VULNERABILITY_NEWS": 70,
}


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = TAG_RE.sub(" ", value)
    value = html.unescape(value)
    return SPACE_RE.sub(" ", value).strip()


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    raw = value.strip()
    try:
        parsed = parsedate_to_datetime(raw)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError, OverflowError):
        pass

    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def extract_cves(*values: str) -> list[str]:
    found: set[str] = set()
    for value in values:
        for match in CVE_RE.findall(value or ""):
            found.add(match.upper())
    return sorted(found)


def classify_event(text: str, related_cves: Iterable[str]) -> str | None:
    lowered = text.lower()
    for event_type in ("RANSOMWARE", "SUPPLY_CHAIN", "DATA_BREACH", "ACTIVE_EXPLOITATION", "THREAT_ACTIVITY"):
        if any(keyword in lowered for keyword in EVENT_KEYWORDS[event_type]):
            return event_type
    if any(related_cves):
        return "VULNERABILITY_NEWS"
    return None


def priority_for(event_type: str, text: str) -> str:
    lowered = text.lower()
    if event_type in {"RANSOMWARE", "ACTIVE_EXPLOITATION"}:
        return "CRITICAL"
    if "critical" in lowered or "zero-day" in lowered or "zero day" in lowered:
        return "CRITICAL"
    if event_type in {"SUPPLY_CHAIN", "DATA_BREACH", "VULNERABILITY_NEWS"}:
        return "HIGH"
    return "MEDIUM"


def _child_text(node: ET.Element, names: set[str]) -> str:
    for child in node:
        if local_name(child.tag) in names and child.text:
            return child.text
    return ""


def _entry_link(node: ET.Element) -> str:
    for child in node:
        if local_name(child.tag) != "link":
            continue
        href = child.attrib.get("href")
        rel = child.attrib.get("rel", "alternate")
        if href and rel in {"alternate", ""}:
            return href.strip()
        if child.text:
            return child.text.strip()
    return ""


def parse_feed(xml_text: str, source: dict[str, str]) -> list[dict[str, str]]:
    root = ET.fromstring(xml_text)
    rows: list[dict[str, str]] = []

    for node in root.iter():
        node_name = local_name(node.tag)
        if node_name not in {"item", "entry"}:
            continue

        title = clean_text(_child_text(node, {"title"}))
        link = _entry_link(node)
        description = clean_text(_child_text(node, {"description", "summary", "content", "encoded"}))
        published_raw = _child_text(node, {"pubdate", "published", "updated", "date"})
        if not title or not link:
            continue
        rows.append(
            {
                "title": title,
                "url": link,
                "summary": description,
                "published_raw": published_raw,
                "source_name": source["name"],
                "source_type": source["source_type"],
            }
        )
    return rows


@dataclass
class NewsCollectionResult:
    items: list[dict]
    fetched_entries: int
    source_errors: list[dict[str, str]]
    successful_sources: int


class NewsCollector:
    def __init__(self, timeout: int = 30, retries: int = 2, article_limit: int = 40) -> None:
        self.timeout = timeout
        self.retries = retries
        self.article_limit = article_limit
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": USER_AGENT,
                "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, text/html;q=0.8,*/*;q=0.5",
            }
        )

    def _get_text(self, url: str) -> str:
        for attempt in range(self.retries + 1):
            response = self.session.get(url, timeout=self.timeout)
            if response.status_code == 429 or 500 <= response.status_code < 600:
                if attempt == self.retries:
                    response.raise_for_status()
                retry_after = response.headers.get("Retry-After")
                delay = float(retry_after) if retry_after and retry_after.isdigit() else min(2 ** (attempt + 1), 10)
                time.sleep(delay)
                continue
            response.raise_for_status()
            return response.text
        raise RuntimeError(f"Failed to fetch {url}")

    def collect(
        self,
        *,
        sources: Iterable[dict[str, str]] = DEFAULT_NEWS_SOURCES,
        window_days: int = 7,
        max_items: int = 20,
        tracked_cves: Iterable[str] = (),
        now: datetime | None = None,
    ) -> NewsCollectionResult:
        now = now or datetime.now(timezone.utc)
        cutoff = now - timedelta(days=max(window_days, 1))
        tracked = {cve.upper() for cve in tracked_cves}
        entries: list[dict[str, str]] = []
        errors: list[dict[str, str]] = []
        successful_sources = 0

        for source in sources:
            try:
                xml_text = self._get_text(source["url"])
                entries.extend(parse_feed(xml_text, source))
                successful_sources += 1
            except Exception as exc:  # noqa: BLE001 - source-level isolation is deliberate
                errors.append({"source": source.get("name", "unknown"), "error": str(exc)[:240]})

        seen_urls: set[str] = set()
        candidates: list[dict] = []
        article_fetches = 0

        for entry in entries:
            url = entry["url"]
            if url in seen_urls or not url.startswith("https://"):
                continue
            seen_urls.add(url)

            published = parse_time(entry.get("published_raw"))
            if published and published < cutoff:
                continue

            base_text = f"{entry['title']} {entry.get('summary', '')}".strip()
            related_cves = extract_cves(base_text)
            preliminary_type = classify_event(base_text, related_cves)
            looks_relevant = preliminary_type is not None or any(token in base_text.lower() for token in ("vulnerability", "exploit", "attack", "cyber"))

            article_text = ""
            if looks_relevant and article_fetches < self.article_limit:
                try:
                    article_text = self._get_text(url)
                    article_fetches += 1
                except Exception:  # noqa: BLE001 - feed metadata remains usable
                    article_text = ""

            all_text = f"{base_text} {article_text}"
            related_cves = extract_cves(all_text)
            event_type = classify_event(base_text + " " + clean_text(article_text[:12000]), related_cves)
            if not event_type:
                continue

            matched_cves = sorted(set(related_cves) & tracked)
            priority = priority_for(event_type, base_text)
            score = EVENT_WEIGHT[event_type] + min(len(matched_cves) * 5, 15)
            if published:
                age_hours = max(0.0, (now - published).total_seconds() / 3600)
                score += max(0, 12 - int(age_hours / 12))

            summary = entry.get("summary", "")
            if len(summary) > 360:
                summary = summary[:357].rstrip() + "..."

            candidates.append(
                {
                    "id": hashlib.sha256(url.encode("utf-8")).hexdigest()[:16],
                    "event_type": event_type,
                    "priority": priority,
                    "published_at": published.isoformat() if published else None,
                    "title": entry["title"],
                    "summary": summary or None,
                    "source_name": entry["source_name"],
                    "source_type": entry["source_type"],
                    "source_url": url,
                    "related_cves": related_cves,
                    "matched_intelligence_cves": matched_cves,
                    "score": score,
                }
            )

        candidates.sort(
            key=lambda item: (
                PRIORITY_ORDER.get(item["priority"], 0),
                item["score"],
                item.get("published_at") or "",
            ),
            reverse=True,
        )

        return NewsCollectionResult(
            items=candidates[:max_items],
            fetched_entries=len(entries),
            source_errors=errors,
            successful_sources=successful_sources,
        )
