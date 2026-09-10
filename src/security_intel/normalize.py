from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Any, Iterable

from security_intel.collectors.nvd import NVD_DETAIL_URL


def normalize_record(
    *,
    nvd_wrapper: dict[str, Any] | None,
    kev_entry: dict[str, Any] | None,
    epss_entry: dict[str, Any] | None,
    collected_at: datetime,
    window_start: datetime,
    window_end: datetime,
) -> dict[str, Any]:
    cve = (nvd_wrapper or {}).get("cve", {})
    cve_id = cve.get("id") or (kev_entry or {}).get("cveID")
    if not cve_id:
        raise ValueError("CVE ID is required")

    affected = _affected(cve)
    vendor, product = _vendor_product(affected, kev_entry)
    ssvc = _ssvc(cve)

    if kev_entry:
        exploitation = {"status": "known_exploited", "source": "cisa_kev", "ssvc": ssvc}
    elif ssvc and ssvc.get("exploitation"):
        exploitation = {"status": ssvc["exploitation"], "source": "nvd_ssvc", "ssvc": ssvc}
    else:
        exploitation = {"status": "unconfirmed", "source": None, "ssvc": ssvc}

    source_type = []
    if nvd_wrapper:
        source_type.append("nvd")
    if kev_entry:
        source_type.append("cisa_kev")
    if epss_entry:
        source_type.append("first_epss")

    return {
        "cve": cve_id,
        "vendor": vendor,
        "product": product,
        "title": (kev_entry or {}).get("vulnerabilityName"),
        "description": (kev_entry or {}).get("shortDescription") or _description(cve),
        "cvss": _cvss(cve),
        "epss": _as_float((epss_entry or {}).get("epss")),
        "epss_percentile": _as_float((epss_entry or {}).get("percentile")),
        "cisa_kev": _kev(kev_entry),
        "exploitation_status": exploitation,
        "published_time": cve.get("published"),
        "updated_time": cve.get("lastModified"),
        "collected_time": collected_at.isoformat(),
        "source_url": NVD_DETAIL_URL.format(cve_id=cve_id) if nvd_wrapper else None,
        "source_type": source_type,
        "references": _references(cve),
        "cwes": _cwes(cve),
        "affected": affected,
        "change_flags": {
            "newly_published": _in_window(cve.get("published"), window_start, window_end),
            "recently_modified": _in_window(cve.get("lastModified"), window_start, window_end),
            "new_kev": _kev_in_window(kev_entry, window_start.date(), window_end.date()),
        },
        "provenance": {
            "nvd": NVD_DETAIL_URL.format(cve_id=cve_id) if nvd_wrapper else None,
            "cisa_kev": "https://www.cisa.gov/known-exploited-vulnerabilities-catalog" if kev_entry else None,
            "epss": f"https://api.first.org/data/v1/epss?cve={cve_id}" if epss_entry else None,
        },
    }


def _description(cve: dict[str, Any]) -> str | None:
    rows = cve.get("descriptions", [])
    if not isinstance(rows, list):
        return None
    for row in rows:
        if row.get("lang") == "en" and row.get("value"):
            return row["value"]
    return next((row.get("value") for row in rows if row.get("value")), None)


def _cvss(cve: dict[str, Any]) -> dict[str, Any] | None:
    metrics = cve.get("metrics", {})
    if not isinstance(metrics, dict):
        return None
    for key, fallback_version in (
        ("cvssMetricV40", "4.0"),
        ("cvssMetricV31", "3.1"),
        ("cvssMetricV30", "3.0"),
        ("cvssMetricV2", "2.0"),
    ):
        entries = metrics.get(key)
        if not isinstance(entries, list) or not entries:
            continue
        entry = next((x for x in entries if x.get("type") == "Primary"), entries[0])
        data = entry.get("cvssData", {})
        if not isinstance(data, dict):
            continue
        return {
            "version": data.get("version") or fallback_version,
            "score": _as_float(data.get("baseScore")),
            "severity": data.get("baseSeverity") or entry.get("baseSeverity"),
            "vector": data.get("vectorString"),
            "source": entry.get("source"),
            "type": entry.get("type"),
        }
    return None


def _affected(cve: dict[str, Any]) -> list[dict[str, Any]]:
    direct = cve.get("affected")
    if isinstance(direct, list):
        flattened = _flatten_affected(direct)
        if flattened:
            return flattened
    for obj in _walk_dicts(cve):
        value = obj.get("affectedData")
        if isinstance(value, list):
            flattened = _flatten_affected([{"source": obj.get("source"), "affectedData": value}])
            if flattened:
                return flattened
    return []


def _flatten_affected(rows: list[Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        nested = row.get("affectedData")
        if isinstance(nested, list):
            for item in nested:
                if not isinstance(item, dict):
                    continue
                normalized = dict(item)
                if row.get("source") and not normalized.get("source"):
                    normalized["source"] = row["source"]
                out.append(normalized)
        elif any(key in row for key in ("vendor", "product", "versions", "packageName")):
            out.append(dict(row))
    return out


def _ssvc(cve: dict[str, Any]) -> dict[str, Any] | None:
    candidates = []
    for obj in _walk_dicts(cve):
        options = obj.get("options")
        if isinstance(options, list) and any(
            isinstance(x, dict) and "exploitation" in x for x in options
        ):
            candidates.append(obj)
    if not candidates:
        return None
    obj = next(
        (x for x in candidates if "cisa" in str(x.get("role", "")).lower()),
        candidates[0],
    )
    options: dict[str, Any] = {}
    for item in obj.get("options", []):
        if isinstance(item, dict):
            options.update(item)
    return {
        "exploitation": options.get("exploitation"),
        "automatable": options.get("automatable"),
        "technical_impact": options.get("technicalImpact"),
        "timestamp": obj.get("timestamp"),
        "role": obj.get("role"),
        "version": obj.get("version"),
    }


def _vendor_product(
    affected: list[dict[str, Any]], kev_entry: dict[str, Any] | None
) -> tuple[str | None, str | None]:
    if kev_entry:
        return kev_entry.get("vendorProject"), kev_entry.get("product")
    for item in affected:
        if isinstance(item, dict) and (item.get("vendor") or item.get("product")):
            return _known_text(item.get("vendor")), _known_text(item.get("product"))
    return None, None


def _known_text(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    text = value.strip()
    if text.lower() in {"n/a", "na"}:
        return None
    return text


def _kev(entry: dict[str, Any] | None) -> dict[str, Any]:
    if not entry:
        return {"listed": False}
    return {
        "listed": True,
        "date_added": entry.get("dateAdded"),
        "due_date": entry.get("dueDate"),
        "required_action": entry.get("requiredAction"),
        "known_ransomware_campaign_use": entry.get("knownRansomwareCampaignUse"),
        "notes": entry.get("notes"),
        "cwes": entry.get("cwes", []),
    }


def _references(cve: dict[str, Any]) -> list[dict[str, Any]]:
    rows = cve.get("references", [])
    if not isinstance(rows, list):
        return []
    return [
        {"url": x.get("url"), "source": x.get("source"), "tags": x.get("tags", [])}
        for x in rows if isinstance(x, dict) and x.get("url")
    ]


def _cwes(cve: dict[str, Any]) -> list[str]:
    out: set[str] = set()
    rows = cve.get("weaknesses", [])
    if not isinstance(rows, list):
        return []
    for row in rows:
        for desc in row.get("description", []):
            value = desc.get("value")
            if isinstance(value, str) and value.startswith("CWE-"):
                out.add(value)
    return sorted(out)


def _walk_dicts(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_dicts(child)


def _parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def _in_window(value: str | None, start: datetime, end: datetime) -> bool:
    parsed = _parse_dt(value)
    return bool(parsed and start <= parsed <= end)


def _kev_in_window(entry: dict[str, Any] | None, start: date, end: date) -> bool:
    if not entry or not entry.get("dateAdded"):
        return False
    try:
        added = date.fromisoformat(entry["dateAdded"])
    except ValueError:
        return False
    return start <= added <= end


def _as_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
