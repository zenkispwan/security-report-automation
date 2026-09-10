from __future__ import annotations

from datetime import datetime, timedelta, timezone
import hashlib
import re
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,}\b", re.IGNORECASE)
WORD_RE = re.compile(r"[a-z0-9][a-z0-9+._/-]{1,}", re.IGNORECASE)
TRACKING_PREFIXES = ("utm_", "ref", "source", "campaign")

STOPWORDS = {
    "about", "after", "again", "against", "attack", "attacks", "been", "being",
    "could", "from", "have", "into", "latest", "more", "new", "news", "over",
    "security", "than", "that", "their", "this", "through", "using", "with", "zero",
}

EVENT_RULES: list[tuple[str, tuple[str, ...]]] = [
    ("active_exploitation", ("actively exploited", "active exploitation", "exploited in the wild", "ongoing exploitation", "actively tracking the exploitation", "遭積極利用", "已遭利用", "發動攻擊")),
    ("zero_day", ("zero-day", "zero day", "0-day", "0day", "零日", "零時差")),
    ("ransomware", ("ransomware", "勒索軟體", "勒贖", "extortion group")),
    ("supply_chain", ("supply chain", "software supply chain", "malicious package", "npm", "pypi", "供應鏈")),
    ("data_breach", ("data breach", "data stolen", "customer data stolen", "records exposed", "資料外洩", "資料遭竊", "個資外洩")),
    ("malware_campaign", ("malware campaign", "malware", "infostealer", "stealer", "backdoor", "trojan", "惡意軟體", "竊密")),
    ("phishing", ("phishing", "credential theft", "credential stealing", "釣魚", "憑證竊取")),
    ("ddos_disruption", ("ddos", "denial of service", "service disruption", "outage", "服務中斷", "癱瘓")),
    ("vulnerability", ("vulnerability", "vulnerabilities", "cve-", "漏洞")),
]

EVENT_BASE_SCORE = {
    "active_exploitation": 45,
    "zero_day": 40,
    "ransomware": 35,
    "supply_chain": 35,
    "data_breach": 30,
    "malware_campaign": 25,
    "ddos_disruption": 20,
    "phishing": 15,
    "vulnerability": 15,
    "general": 5,
}


def build_event_outputs(
    articles: list[dict[str, Any]],
    profile: dict[str, Any],
    *,
    vulnerability_intelligence: dict[str, Any] | None = None,
    previous_state: dict[str, Any] | None = None,
    verified_cves: set[str] | None = None,
    now: datetime | None = None,
    max_events: int = 20,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    now = now or datetime.now(timezone.utc)
    lookback_hours = int(profile.get("lookback_hours") or 24)
    cutoff = now - timedelta(hours=lookback_hours)
    verified_cves = {x.upper() for x in (verified_cves or set())}

    normalized: list[dict[str, Any]] = []
    seen_urls: set[str] = set()
    excluded_unknown_time = 0
    excluded_old = 0

    for article in articles:
        row = normalize_article(article, profile)
        if not row:
            continue
        url = row["url"]
        if url in seen_urls:
            continue
        seen_urls.add(url)
        published = _parse_dt(row.get("published_time"))
        if published is None:
            excluded_unknown_time += 1
            continue
        if published < cutoff or published > now + timedelta(minutes=10):
            excluded_old += 1
            continue
        normalized.append(row)

    clusters = cluster_articles(normalized)
    vuln_by_cve = _vulnerability_index(vulnerability_intelligence or {})
    previous_items = (previous_state or {}).get("items") or {}

    events: list[dict[str, Any]] = []
    state_items: dict[str, Any] = {}
    for cluster in clusters:
        event = build_event(
            cluster,
            profile,
            vuln_by_cve=vuln_by_cve,
            verified_cves=verified_cves,
            previous_items=previous_items,
            now=now,
        )
        events.append(event)
        state_items[event["fingerprint"]] = {
            "event_id": event["event_id"],
            "first_seen": event["first_seen"],
            "last_seen": event["last_seen"],
            "event_type": event["event_type"],
            "cves": event["cves"],
            "title": event["title"],
        }

    # Retain recently seen fingerprints so repeated stories are not labelled new tomorrow.
    retention_cutoff = now - timedelta(days=7)
    for fingerprint, previous in previous_items.items():
        if fingerprint in state_items or not isinstance(previous, dict):
            continue
        last_seen = _parse_dt(previous.get("last_seen"))
        if last_seen and last_seen >= retention_cutoff:
            state_items[fingerprint] = previous

    events.sort(key=_event_sort_key, reverse=True)
    selected = events[:max_events]
    new_events = [x for x in selected if x.get("is_new") and x["priority"] != "WATCH"]

    generated_at = now.isoformat()
    event_state = {
        "schema_version": "2.5-event-state",
        "generated_at": generated_at,
        "retention_days": 7,
        "items": state_items,
    }
    output = {
        "schema_version": "2.5-events",
        "generated_at": generated_at,
        "window": {"hours": lookback_hours, "start": cutoff.isoformat(), "end": generated_at},
        "profile": {
            "name": profile.get("profile_name"),
            "geographies": profile.get("geographies") or [],
            "technology_keywords_configured": len(profile.get("technology_keywords") or []),
            "industry_keywords_configured": len(profile.get("industry_keywords") or []),
        },
        "summary": {
            "discovered_articles": len(articles),
            "eligible_articles": len(normalized),
            "excluded_unknown_time": excluded_unknown_time,
            "excluded_outside_window": excluded_old,
            "cluster_count": len(events),
            "selected_count": len(selected),
            "new_notable_count": len(new_events),
            "p1": sum(x["priority"] == "P1" for x in selected),
            "p2": sum(x["priority"] == "P2" for x in selected),
            "p3": sum(x["priority"] == "P3" for x in selected),
            "watch": sum(x["priority"] == "WATCH" for x in selected),
        },
        "items": selected,
    }
    delta = {
        "schema_version": "2.5-event-delta",
        "generated_at": generated_at,
        "summary": {
            "new_notable_count": len(new_events),
            "by_type": _count_by(new_events, "event_type"),
            "by_priority": _count_by(new_events, "priority"),
        },
        "items": new_events,
    }
    return event_state, output, delta


def normalize_article(article: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any] | None:
    title = _clean_text(article.get("title"))
    raw_url = str(article.get("url") or "").strip()
    if not title or not raw_url:
        return None
    url = canonical_url(raw_url)
    domain = (article.get("domain") or urlparse(url).netloc).lower().removeprefix("www.")
    summary = _clean_text(article.get("summary"))
    source_policy = profile.get("source_policy") or {}
    authority = article.get("authority") or source_authority(domain, source_policy)
    if authority == "discovery":
        authority = source_authority(domain, source_policy)
    combined = f"{title} {summary or ''}".lower()
    signals = [name for name, phrases in EVENT_RULES if any(p in combined for p in phrases)]
    event_type = signals[0] if signals else "general"
    cves = sorted({x.upper() for x in CVE_RE.findall(combined)})
    return {
        "title": title,
        "summary": summary,
        "url": url,
        "domain": domain,
        "published_time": article.get("published_time"),
        "collected_time": article.get("collected_time"),
        "source_name": article.get("source_name") or domain,
        "source_type": article.get("source_type") or "web",
        "authority": authority,
        "language": article.get("language"),
        "source_country": article.get("source_country"),
        "discovery_query": article.get("discovery_query"),
        "event_type": event_type,
        "signals": signals,
        "cves": cves,
        "tokens": sorted(_title_tokens(title)),
    }


def source_authority(domain: str, policy: dict[str, Any]) -> str:
    if _domain_in(domain, policy.get("official_domains") or []):
        return "official"
    if _domain_in(domain, policy.get("trusted_media_domains") or []):
        return "trusted_media"
    return "discovery"


def cluster_articles(rows: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    clusters: list[list[dict[str, Any]]] = []
    for row in sorted(rows, key=lambda x: x.get("published_time") or ""):
        placed = False
        for cluster in clusters:
            if _same_story(row, cluster):
                cluster.append(row)
                placed = True
                break
        if not placed:
            clusters.append([row])
    return clusters


def build_event(
    cluster: list[dict[str, Any]],
    profile: dict[str, Any],
    *,
    vuln_by_cve: dict[str, dict[str, Any]],
    verified_cves: set[str],
    previous_items: dict[str, Any],
    now: datetime,
) -> dict[str, Any]:
    representative = sorted(cluster, key=_source_rank, reverse=True)[0]
    cves = sorted({cve for row in cluster for cve in row.get("cves") or []})
    event_type = _cluster_event_type(cluster)
    fingerprint = event_fingerprint(event_type, representative["title"], cves)
    previous = previous_items.get(fingerprint) if isinstance(previous_items, dict) else None
    published_times = [x for x in (_parse_dt(row.get("published_time")) for row in cluster) if x]
    first_seen_now = min(published_times).isoformat() if published_times else now.isoformat()
    last_seen = max(published_times).isoformat() if published_times else now.isoformat()
    first_seen = (previous or {}).get("first_seen") or first_seen_now

    sources = [
        {
            "title": row["title"],
            "url": row["url"],
            "domain": row["domain"],
            "publisher": row.get("source_name"),
            "authority": row.get("authority"),
            "source_type": row.get("source_type"),
            "published_time": row.get("published_time"),
        }
        for row in sorted(cluster, key=_source_rank, reverse=True)
    ]
    verification = verification_status(sources)
    confirmed_cves = [x for x in cves if x in verified_cves or x in vuln_by_cve]
    unverified_cves = [x for x in cves if x not in confirmed_cves]
    linked = [vuln_by_cve[x] for x in confirmed_cves if x in vuln_by_cve]
    combined = " ".join(f"{x['title']} {x.get('summary') or ''}" for x in cluster).lower()
    relevance = relevance_for(combined, event_type, profile)
    score, reasons = event_score(event_type, verification, relevance, linked, last_seen, now)
    priority = "P1" if score >= 75 else "P2" if score >= 55 else "P3" if score >= 35 else "WATCH"

    return {
        "event_id": f"evt-{fingerprint[:16]}",
        "fingerprint": fingerprint,
        "title": representative["title"],
        "summary": representative.get("summary"),
        "event_type": event_type,
        "signals": sorted({signal for row in cluster for signal in row.get("signals") or []}),
        "priority": priority,
        "score": score,
        "score_reasons": reasons,
        "is_new": previous is None,
        "first_seen": first_seen,
        "last_seen": last_seen,
        "cves": cves,
        "confirmed_cves": confirmed_cves,
        "unverified_cve_mentions": unverified_cves,
        "linked_vulnerabilities": [_linked_vulnerability(x) for x in linked],
        "verification": verification,
        "relevance": relevance,
        "sources": sources,
    }


def verification_status(sources: list[dict[str, Any]]) -> dict[str, Any]:
    authorities = {x.get("authority") for x in sources}
    distinct_domains = {x.get("domain") for x in sources if x.get("domain")}
    trusted_domains = {
        x.get("domain") for x in sources
        if x.get("authority") in {"official", "trusted_media"} and x.get("domain")
    }
    if "official" in authorities:
        status, confidence = "official_confirmed", "high"
    elif len(trusted_domains) >= 2:
        status, confidence = "corroborated", "high"
    elif "trusted_media" in authorities:
        status, confidence = "single_trusted_source", "medium"
    else:
        status, confidence = "discovery_only", "low"
    return {
        "status": status,
        "confidence": confidence,
        "source_count": len(sources),
        "distinct_domain_count": len(distinct_domains),
    }


def relevance_for(text: str, event_type: str, profile: dict[str, Any]) -> dict[str, Any]:
    reasons: list[dict[str, str]] = []
    technology_matches = _matches(text, profile.get("technology_keywords") or [])
    industry_matches = _matches(text, profile.get("industry_keywords") or [])
    asset_matches: dict[str, list[str]] = {}
    for asset_class, keywords in (profile.get("asset_classes") or {}).items():
        matched = _matches(text, keywords)
        if matched:
            asset_matches[asset_class] = matched

    geography_matches: list[str] = []
    if any(x in text for x in ("taiwan", "taiwanese", "台灣", "臺灣")):
        geography_matches.append("Taiwan")
    if any(x in text for x in ("asia-pacific", "asia pacific", "apac", "east asia", "southeast asia", "亞太", "亞洲")):
        geography_matches.append("APAC")

    if technology_matches:
        reasons.append({"code": "TECHNOLOGY_PROFILE_MATCH", "detail": ", ".join(technology_matches)})
    if industry_matches:
        reasons.append({"code": "INDUSTRY_PROFILE_MATCH", "detail": ", ".join(industry_matches)})
    if geography_matches:
        reasons.append({"code": "GEOGRAPHY_MATCH", "detail": ", ".join(geography_matches)})
    for asset_class in asset_matches:
        reasons.append({"code": "ASSET_CLASS_MATCH", "detail": asset_class})
    if event_type in set(profile.get("priority_event_types") or []):
        reasons.append({"code": "PRIORITY_EVENT_TYPE", "detail": event_type})

    exact = bool(technology_matches or industry_matches or geography_matches)
    level = "high" if technology_matches or "Taiwan" in geography_matches else "medium" if exact or asset_matches else "low"
    scope = "profile_matched" if exact else "general_enterprise" if asset_matches else "unconfirmed"
    return {
        "level": level,
        "scope": scope,
        "technology_matches": technology_matches,
        "industry_matches": industry_matches,
        "geography_matches": geography_matches,
        "asset_class_matches": asset_matches,
        "reasons": reasons,
    }


def event_score(
    event_type: str,
    verification: dict[str, Any],
    relevance: dict[str, Any],
    linked_vulnerabilities: list[dict[str, Any]],
    last_seen: str,
    now: datetime,
) -> tuple[int, list[dict[str, Any]]]:
    score = EVENT_BASE_SCORE.get(event_type, 5)
    reasons: list[dict[str, Any]] = [{"code": f"EVENT_{event_type.upper()}", "points": score}]

    verify_points = {
        "official_confirmed": 20,
        "corroborated": 15,
        "single_trusted_source": 8,
        "discovery_only": 0,
    }.get(verification.get("status"), 0)
    if verify_points:
        score += verify_points
        reasons.append({"code": "SOURCE_VERIFICATION", "points": verify_points})

    relevance_points = 20 if relevance.get("level") == "high" else 10 if relevance.get("level") == "medium" else 0
    if relevance_points:
        score += relevance_points
        reasons.append({"code": "RELEVANCE", "points": relevance_points})

    best_priority = min(
        (_priority_rank((x.get("risk") or {}).get("priority")) for x in linked_vulnerabilities),
        default=9,
    )
    vuln_points = {0: 20, 1: 12, 2: 6}.get(best_priority, 0)
    if vuln_points:
        score += vuln_points
        reasons.append({"code": "LINKED_VULNERABILITY_PRIORITY", "points": vuln_points})

    seen = _parse_dt(last_seen)
    if seen and now - seen <= timedelta(hours=6):
        score += 5
        reasons.append({"code": "RECENT_6H", "points": 5})

    return min(score, 100), reasons


def event_fingerprint(event_type: str, title: str, cves: list[str]) -> str:
    if cves:
        seed = f"{event_type}|{'|'.join(sorted(cves))}"
    else:
        tokens = sorted(_title_tokens(title))[:16]
        seed = f"{event_type}|{'|'.join(tokens) or _clean_text(title).lower()}"
    return hashlib.sha256(seed.encode("utf-8")).hexdigest()


def canonical_url(value: str) -> str:
    parsed = urlparse(value.strip())
    query = [
        (k, v) for k, v in parse_qsl(parsed.query, keep_blank_values=True)
        if not k.lower().startswith(TRACKING_PREFIXES)
    ]
    return urlunparse((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path, "", urlencode(query), ""))


def _same_story(row: dict[str, Any], cluster: list[dict[str, Any]]) -> bool:
    row_cves = set(row.get("cves") or [])
    row_tokens = set(row.get("tokens") or [])
    for existing in cluster:
        other_cves = set(existing.get("cves") or [])
        if row_cves and other_cves and row_cves.intersection(other_cves):
            return True
        other_tokens = set(existing.get("tokens") or [])
        union = row_tokens.union(other_tokens)
        if union:
            similarity = len(row_tokens.intersection(other_tokens)) / len(union)
            if similarity >= 0.45 and len(row_tokens.intersection(other_tokens)) >= 3:
                return True
    return False


def _cluster_event_type(cluster: list[dict[str, Any]]) -> str:
    types = [x.get("event_type") or "general" for x in cluster]
    return max(types, key=lambda x: EVENT_BASE_SCORE.get(x, 0))


def _source_rank(row: dict[str, Any]) -> tuple[int, str]:
    authority = {"official": 3, "trusted_media": 2, "discovery": 1}.get(row.get("authority"), 0)
    return authority, row.get("published_time") or ""


def _event_sort_key(event: dict[str, Any]) -> tuple[int, int, str]:
    priority = {"P1": 4, "P2": 3, "P3": 2, "WATCH": 1}.get(event.get("priority"), 0)
    return priority, int(event.get("score") or 0), event.get("last_seen") or ""


def _vulnerability_index(intelligence: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(x.get("cve")).upper(): x
        for x in intelligence.get("items") or []
        if isinstance(x, dict) and x.get("cve")
    }


def _linked_vulnerability(row: dict[str, Any]) -> dict[str, Any]:
    facts = row.get("facts") or {}
    return {
        "cve": row.get("cve"),
        "risk": row.get("risk") or {},
        "cvss": facts.get("cvss"),
        "epss": facts.get("epss"),
        "cisa_kev": facts.get("cisa_kev"),
        "exploitation_status": facts.get("exploitation_status"),
        "vendor": facts.get("vendor"),
        "product": facts.get("product"),
    }


def _title_tokens(title: str) -> set[str]:
    return {
        token.lower().strip("._/-")
        for token in WORD_RE.findall(title.lower())
        if len(token) >= 3 and token.lower() not in STOPWORDS and not token.lower().startswith("cve-")
    }


def _matches(text: str, keywords: list[str]) -> list[str]:
    return sorted({str(x) for x in keywords if str(x).strip() and str(x).lower() in text})


def _domain_in(domain: str, allowed: list[str]) -> bool:
    return any(domain == item.lower() or domain.endswith("." + item.lower()) for item in allowed)


def _clean_text(value: Any) -> str | None:
    if value is None:
        return None
    return re.sub(r"\s+", " ", str(value)).strip() or None


def _parse_dt(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return None


def _priority_rank(priority: Any) -> int:
    return {"P1": 0, "P2": 1, "P3": 2, "WATCH": 3}.get(str(priority), 9)


def _count_by(items: list[dict[str, Any]], key: str) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in items:
        value = str(item.get(key) or "unknown")
        result[value] = result.get(value, 0) + 1
    return dict(sorted(result.items()))
