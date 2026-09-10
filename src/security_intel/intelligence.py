from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

RISK_VERSION = "1.1"
EPSS_JUMP_THRESHOLD = 0.10
MAX_TRACKED = 1000
MAX_DELTA_ITEMS = 200
MAX_INTELLIGENCE_ITEMS = 30


def build_outputs(
    current_snapshot: dict[str, Any],
    *,
    previous_state: dict[str, Any] | None = None,
    previous_snapshot: dict[str, Any] | None = None,
    refreshed_epss: dict[str, dict[str, Any]] | None = None,
    max_tracked: int = MAX_TRACKED,
    max_delta_items: int = MAX_DELTA_ITEMS,
    max_intelligence_items: int = MAX_INTELLIGENCE_ITEMS,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    current_items = {
        x["cve"]: x
        for x in current_snapshot.get("items", [])
        if isinstance(x, dict) and x.get("cve")
    }

    previous_items, previous_generated_at, baseline_type = _previous_items(
        previous_state, previous_snapshot
    )
    previous_time = _parse_dt(previous_generated_at)

    refreshed_epss = refreshed_epss or {}
    monitored_items = 0
    for cve_id, previous in previous_items.items():
        if cve_id in current_items:
            continue
        epss = refreshed_epss.get(cve_id)
        if not epss:
            continue
        current_items[cve_id] = _synthetic_monitor_item(previous, epss)
        monitored_items += 1

    scored: list[dict[str, Any]] = []
    event_counts: dict[str, int] = {}

    for cve_id, item in current_items.items():
        prev = previous_items.get(cve_id)
        events = detect_events(item, prev, previous_time)
        for event in events:
            event_counts[event["type"]] = event_counts.get(event["type"], 0) + 1
        risk = score_item(item, events)
        scored.append({
            "cve": cve_id,
            "events": events,
            "risk": risk,
            "facts": compact_facts(item),
        })

    scored.sort(key=_sort_key, reverse=True)

    delta_candidates = [x for x in scored if x["events"]]
    delta_items = delta_candidates[:max_delta_items]
    intelligence_candidates = [x for x in scored if _include_intelligence(x)]
    intelligence_items = intelligence_candidates[:max_intelligence_items]

    generated_at = current_snapshot.get("generated_at") or datetime.now(timezone.utc).isoformat()
    state_items = _select_state_items(scored, max_tracked)

    state = {
        "schema_version": "2.1-state",
        "risk_version": RISK_VERSION,
        "generated_at": generated_at,
        "tracked_count": len(state_items),
        "items": {x["cve"]: x["facts"] for x in state_items},
    }

    delta = {
        "schema_version": "2.1-delta",
        "generated_at": generated_at,
        "baseline": {
            "type": baseline_type,
            "generated_at": previous_generated_at,
            "available": baseline_type != "none",
        },
        "summary": {
            "current_snapshot_count": len(current_snapshot.get("items", [])),
            "tracked_previous_count": len(previous_items),
            "epss_monitored_count": monitored_items,
            "meaningful_change_count": len(delta_candidates),
            "included_count": len(delta_items),
            "truncated": len(delta_candidates) > len(delta_items),
            "events": dict(sorted(event_counts.items())),
        },
        "items": delta_items,
    }

    intelligence = {
        "schema_version": "2.1-intelligence",
        "risk_version": RISK_VERSION,
        "generated_at": generated_at,
        "selection": {
            "max_items": max_intelligence_items,
            "candidate_count": len(intelligence_candidates),
            "selected_count": len(intelligence_items),
        },
        "summary": {
            "p1": sum(x["risk"]["priority"] == "P1" for x in intelligence_items),
            "p2": sum(x["risk"]["priority"] == "P2" for x in intelligence_items),
            "p3": sum(x["risk"]["priority"] == "P3" for x in intelligence_items),
            "with_delta": sum(bool(x["events"]) for x in intelligence_items),
        },
        "items": intelligence_items,
    }
    return state, delta, intelligence


def detect_events(
    current: dict[str, Any],
    previous: dict[str, Any] | None,
    previous_generated_at: datetime | None,
) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    curr_kev = bool((current.get("cisa_kev") or {}).get("listed"))
    curr_status = _exploit_status(current)
    curr_ransomware = _ransomware_value(current)

    if previous_generated_at:
        published = _parse_dt(current.get("published_time"))
        if published and published > previous_generated_at and _important_new_cve(current):
            events.append({"type": "NEW_CVE", "from": None, "to": current.get("published_time")})

    if previous is None:
        if curr_kev and (current.get("change_flags") or {}).get("new_kev"):
            events.append({"type": "NEW_KEV", "from": False, "to": True})
        return events

    prev_kev = bool((previous.get("cisa_kev") or {}).get("listed"))
    if curr_kev and not prev_kev:
        events.append({"type": "NEW_KEV", "from": False, "to": True})

    prev_epss = _as_float(previous.get("epss"))
    curr_epss = _as_float(current.get("epss"))
    if prev_epss is not None and curr_epss is not None:
        delta = curr_epss - prev_epss
        if delta >= EPSS_JUMP_THRESHOLD:
            events.append({
                "type": "EPSS_INCREASED",
                "from": round(prev_epss, 5),
                "to": round(curr_epss, 5),
                "delta": round(delta, 5),
            })

    prev_status = _exploit_status(previous)
    if curr_status != prev_status:
        events.append({
            "type": "EXPLOITATION_CHANGED",
            "from": prev_status,
            "to": curr_status,
            "escalated": _exploit_rank(curr_status) > _exploit_rank(prev_status),
        })

    prev_cvss = _cvss_score(previous)
    curr_cvss = _cvss_score(current)
    if prev_cvss is not None and curr_cvss is not None and curr_cvss != prev_cvss:
        events.append({
            "type": "CVSS_CHANGED",
            "from": prev_cvss,
            "to": curr_cvss,
            "delta": round(curr_cvss - prev_cvss, 1),
        })

    prev_ransomware = _ransomware_value(previous)
    if curr_ransomware != prev_ransomware and curr_ransomware is not None:
        events.append({
            "type": "RANSOMWARE_USE_CHANGED",
            "from": prev_ransomware,
            "to": curr_ransomware,
        })

    return events


def score_item(item: dict[str, Any], events: Iterable[dict[str, Any]] = ()) -> dict[str, Any]:
    reasons: list[dict[str, Any]] = []
    score = 0

    def add(code: str, points: int) -> None:
        nonlocal score
        score += points
        reasons.append({"code": code, "points": points})

    kev = bool((item.get("cisa_kev") or {}).get("listed"))
    exploit = _exploit_status(item)
    ransomware = (_ransomware_value(item) or "").strip().lower()
    cvss = _cvss_score(item)
    epss = _as_float(item.get("epss"))
    percentile = _as_float(item.get("epss_percentile"))
    flags = item.get("change_flags") or {}

    if kev:
        add("CISA_KEV", 45)
    if exploit in {"active", "known_exploited"}:
        add("ACTIVE_OR_KNOWN_EXPLOITATION", 25)
    elif exploit == "poc":
        add("POC_AVAILABLE", 10)

    if ransomware in {"known", "yes", "true"}:
        add("KNOWN_RANSOMWARE_USE", 20)

    if cvss is not None:
        if cvss >= 9.0:
            add("CVSS_CRITICAL", 20)
        elif cvss >= 7.0:
            add("CVSS_HIGH", 12)
        elif cvss >= 4.0:
            add("CVSS_MEDIUM", 4)

    if epss is not None:
        if epss >= 0.50:
            add("EPSS_VERY_HIGH", 20)
        elif epss >= 0.20:
            add("EPSS_HIGH", 14)
        elif epss >= 0.05:
            add("EPSS_ELEVATED", 8)
    if percentile is not None and percentile >= 0.95:
        add("EPSS_TOP_5_PERCENT", 5)

    if flags.get("newly_published"):
        add("RECENTLY_PUBLISHED", 8)

    for event in events:
        event_type = event.get("type")
        if event_type == "NEW_KEV":
            add("DELTA_NEW_KEV", 15)
        elif event_type == "EPSS_INCREASED":
            add("DELTA_EPSS_JUMP", 15)
        elif event_type == "EXPLOITATION_CHANGED" and event.get("escalated"):
            add("DELTA_EXPLOIT_ESCALATION", 15)
        elif event_type == "CVSS_CHANGED" and (event.get("delta") or 0) > 0:
            add("DELTA_CVSS_INCREASE", 8)
        elif event_type == "RANSOMWARE_USE_CHANGED" and str(event.get("to", "")).lower() in {"known", "yes", "true"}:
            add("DELTA_RANSOMWARE_USE", 15)

    score = min(score, 100)
    if kev or exploit in {"active", "known_exploited"} or score >= 85:
        priority = "P1"
    elif score >= 70:
        priority = "P2"
    elif score >= 35:
        priority = "P3"
    else:
        priority = "WATCH"

    return {"score": score, "priority": priority, "reasons": reasons}


def compact_facts(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "cve": item.get("cve"),
        "vendor": item.get("vendor"),
        "product": item.get("product"),
        "title": item.get("title"),
        "description": item.get("description"),
        "cvss": item.get("cvss"),
        "epss": _as_float(item.get("epss")),
        "epss_percentile": _as_float(item.get("epss_percentile")),
        "cisa_kev": item.get("cisa_kev") or {"listed": False},
        "exploitation_status": item.get("exploitation_status") or {"status": "unconfirmed", "source": None},
        "published_time": item.get("published_time"),
        "updated_time": item.get("updated_time"),
        "source_url": item.get("source_url"),
        "source_type": item.get("source_type") or [],
        "cwes": item.get("cwes") or [],
        "provenance": item.get("provenance") or {},
    }


def state_epss_watch_ids(state: dict[str, Any] | None, current_snapshot: dict[str, Any]) -> list[str]:
    if not state:
        return []
    current_ids = {
        x.get("cve") for x in current_snapshot.get("items", [])
        if isinstance(x, dict) and x.get("cve")
    }
    return sorted(
        cve_id
        for cve_id in (state.get("items") or {})
        if cve_id and cve_id not in current_ids
    )


def _previous_items(
    previous_state: dict[str, Any] | None,
    previous_snapshot: dict[str, Any] | None,
) -> tuple[dict[str, dict[str, Any]], str | None, str]:
    if previous_state and isinstance(previous_state.get("items"), dict):
        return (
            {k: v for k, v in previous_state["items"].items() if isinstance(v, dict)},
            previous_state.get("generated_at"),
            "state",
        )

    if previous_snapshot:
        rows = [
            {"cve": x["cve"], "facts": compact_facts(x), "risk": score_item(x), "events": []}
            for x in previous_snapshot.get("items", [])
            if isinstance(x, dict) and x.get("cve")
        ]
        selected = _select_state_items(rows, MAX_TRACKED)
        return (
            {x["cve"]: x["facts"] for x in selected},
            previous_snapshot.get("generated_at"),
            "snapshot_bootstrap",
        )

    return {}, None, "none"


def _select_state_items(scored: list[dict[str, Any]], max_tracked: int) -> list[dict[str, Any]]:
    candidates = [
        x for x in scored
        if _trackworthy(x["facts"], x["risk"])
    ]
    candidates.sort(key=_sort_key, reverse=True)
    return candidates[:max_tracked]


def _trackworthy(facts: dict[str, Any], risk: dict[str, Any]) -> bool:
    if risk.get("score", 0) >= 35:
        return True
    if bool((facts.get("cisa_kev") or {}).get("listed")):
        return True
    if _exploit_status(facts) in {"poc", "active", "known_exploited"}:
        return True
    return False


def _include_intelligence(row: dict[str, Any]) -> bool:
    priority = row["risk"]["priority"]
    return bool(row["events"]) or priority in {"P1", "P2", "P3"}


def _sort_key(row: dict[str, Any]) -> tuple[int, int, int, str]:
    event_types = {x.get("type") for x in row.get("events", [])}
    event_priority = 0
    if "NEW_KEV" in event_types:
        event_priority = 5
    elif "EXPLOITATION_CHANGED" in event_types:
        event_priority = 4
    elif "RANSOMWARE_USE_CHANGED" in event_types:
        event_priority = 3
    elif "EPSS_INCREASED" in event_types:
        event_priority = 2
    elif "NEW_CVE" in event_types:
        event_priority = 1

    priority_rank = {"P1": 4, "P2": 3, "P3": 2, "WATCH": 1}.get(
        row.get("risk", {}).get("priority"), 0
    )
    return (
        1 if row.get("events") else 0,
        event_priority,
        priority_rank * 100 + int(row.get("risk", {}).get("score", 0)),
        row.get("cve", ""),
    )


def _important_new_cve(item: dict[str, Any]) -> bool:
    cvss = _cvss_score(item)
    epss = _as_float(item.get("epss"))
    percentile = _as_float(item.get("epss_percentile"))
    if bool((item.get("cisa_kev") or {}).get("listed")):
        return True
    if _exploit_status(item) in {"poc", "active", "known_exploited"}:
        return True
    if cvss is not None and cvss >= 9.0:
        return True
    if epss is not None and epss >= 0.05:
        return True
    return percentile is not None and percentile >= 0.90


def _synthetic_monitor_item(previous: dict[str, Any], epss_row: dict[str, Any]) -> dict[str, Any]:
    out = dict(previous)
    out["epss"] = _as_float(epss_row.get("epss"))
    out["epss_percentile"] = _as_float(epss_row.get("percentile"))
    out["change_flags"] = {
        "newly_published": False,
        "recently_modified": False,
        "new_kev": False,
    }
    source_type = list(out.get("source_type") or [])
    if "first_epss" not in source_type:
        source_type.append("first_epss")
    out["source_type"] = source_type
    return out


def _cvss_score(item: dict[str, Any]) -> float | None:
    return _as_float((item.get("cvss") or {}).get("score"))


def _exploit_status(item: dict[str, Any]) -> str:
    value = (item.get("exploitation_status") or {}).get("status")
    return str(value or "unconfirmed").lower()


def _exploit_rank(value: str) -> int:
    return {
        "unconfirmed": 0,
        "none": 1,
        "poc": 2,
        "active": 3,
        "known_exploited": 4,
    }.get(str(value).lower(), 0)


def _ransomware_value(item: dict[str, Any]) -> str | None:
    value = (item.get("cisa_kev") or {}).get("known_ransomware_campaign_use")
    return str(value) if value not in (None, "") else None


def _parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def _as_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
