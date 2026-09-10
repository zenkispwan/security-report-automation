from __future__ import annotations

from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import html
import re
from typing import Any
from urllib.parse import urljoin
import xml.etree.ElementTree as ET

from security_intel.http import HttpClient

TAG_RE = re.compile(r"<[^>]+>")


def collect_feed_articles(
    feeds: list[dict[str, Any]],
    *,
    client: HttpClient | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    client = client or HttpClient(timeout=45, retries=2)
    collected_at = datetime.now(timezone.utc).isoformat()
    rows: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []

    for feed in feeds:
        url = str(feed.get("url") or "").strip()
        if not url:
            continue
        try:
            text = client.get_text(
                url,
                headers={"Accept": "application/rss+xml, application/atom+xml, text/xml, application/xml, */*"},
            )
            root = ET.fromstring(text)
            parsed = _parse_feed(root, base_url=url)
        except Exception as exc:  # a vendor feed outage must not break all event discovery
            errors.append({"feed": url, "error": f"{type(exc).__name__}: {exc}"})
            continue

        for item in parsed:
            if not item.get("title") or not item.get("url"):
                continue
            item.update(
                {
                    "source_name": feed.get("publisher") or feed.get("name") or url,
                    "source_type": "official_feed",
                    "authority": feed.get("authority") or "official",
                    "feed_url": url,
                    "collected_time": collected_at,
                }
            )
            rows.append(item)

    return rows, errors


def _parse_feed(root: ET.Element, *, base_url: str) -> list[dict[str, Any]]:
    tag = _local(root.tag)
    if tag == "rss" or root.find("channel") is not None:
        return [_rss_item(x, base_url) for x in root.findall(".//item")]

    if tag == "feed":
        return [_atom_entry(x, base_url) for x in list(root) if _local(x.tag) == "entry"]

    return []


def _rss_item(item: ET.Element, base_url: str) -> dict[str, Any]:
    title = _text_child(item, "title")
    link = _text_child(item, "link") or _text_child(item, "guid")
    published = (
        _text_child(item, "pubDate")
        or _text_child(item, "published")
        or _text_child(item, "date")
    )
    summary = _text_child(item, "description") or _text_child(item, "summary")
    return {
        "title": _clean(title),
        "url": urljoin(base_url, link.strip()) if link else None,
        "published_time": _date(published),
        "summary": _clean(summary),
    }


def _atom_entry(entry: ET.Element, base_url: str) -> dict[str, Any]:
    title = _text_child(entry, "title")
    link = None
    for child in list(entry):
        if _local(child.tag) != "link":
            continue
        href = child.attrib.get("href")
        rel = child.attrib.get("rel", "alternate")
        if href and rel in {"alternate", ""}:
            link = href
            break
        if href and link is None:
            link = href
    published = _text_child(entry, "published") or _text_child(entry, "updated")
    summary = _text_child(entry, "summary") or _text_child(entry, "content")
    return {
        "title": _clean(title),
        "url": urljoin(base_url, link) if link else None,
        "published_time": _date(published),
        "summary": _clean(summary),
    }


def _text_child(parent: ET.Element, local_name: str) -> str | None:
    for child in list(parent):
        if _local(child.tag) == local_name:
            text = "".join(child.itertext()).strip()
            return text or None
    return None


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _clean(value: Any) -> str | None:
    if value is None:
        return None
    text = html.unescape(TAG_RE.sub(" ", str(value)))
    text = re.sub(r"\s+", " ", text).strip()
    return text or None


def _date(value: Any) -> str | None:
    if not value:
        return None
    raw = str(value).strip()
    try:
        dt = parsedate_to_datetime(raw)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat()
    except (TypeError, ValueError, OverflowError):
        pass
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat()
    except ValueError:
        return raw
