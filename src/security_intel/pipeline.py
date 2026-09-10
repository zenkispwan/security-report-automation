from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from security_intel.collectors.cisa_kev import CisaKevCollector
from security_intel.collectors.epss import EpssCollector
from security_intel.collectors.nvd import NvdCollector
from security_intel.http import HttpClient
from security_intel.normalize import normalize_record


class CollectionPipeline:
    def __init__(
        self,
        lookback_hours: int = 48,
        output_path: str = "data/latest.json",
        raw_dir: str = "data/raw/latest",
    ) -> None:
        if lookback_hours <= 0:
            raise ValueError("lookback_hours must be > 0")
        self.lookback_hours = lookback_hours
        self.output_path = Path(output_path)
        self.raw_dir = Path(raw_dir)

    def run(self) -> dict[str, Any]:
        now = datetime.now(timezone.utc)
        start = now - timedelta(hours=self.lookback_hours)

        client = HttpClient()
        kev_payload, kev_source = CisaKevCollector(client).collect()
        nvd = NvdCollector(client)
        nvd_payload = nvd.collect_recent_changes(start, now)

        kev_index = {
            x["cveID"]: x
            for x in kev_payload.get("vulnerabilities", [])
            if x.get("cveID")
        }
        nvd_index = {
            x.get("cve", {}).get("id"): x
            for x in nvd_payload.get("vulnerabilities", [])
            if x.get("cve", {}).get("id")
        }

        recent_kev_ids = {
            cve_id
            for cve_id, entry in kev_index.items()
            if self._recent_kev(entry, start, now)
        }

        supplemental = []
        for cve_id in sorted(recent_kev_ids - set(nvd_index)):
            row = nvd.fetch_cve(cve_id)
            if row:
                nvd_index[cve_id] = row
                supplemental.append(row)

        target_ids = set(nvd_index) | recent_kev_ids
        epss_index, epss_raw = EpssCollector(client).collect(target_ids)

        items = [
            normalize_record(
                nvd_wrapper=nvd_index.get(cve_id),
                kev_entry=kev_index.get(cve_id),
                epss_entry=epss_index.get(cve_id),
                collected_at=now,
                window_start=start,
                window_end=now,
            )
            for cve_id in sorted(target_ids)
        ]

        result = {
            "schema_version": "2.0",
            "generated_at": now.isoformat(),
            "window": {
                "start": start.isoformat(),
                "end": now.isoformat(),
                "lookback_hours": self.lookback_hours,
            },
            "sources": {
                "cisa_kev": {
                    "source_url": kev_source,
                    "catalog_version": kev_payload.get("catalogVersion"),
                    "date_released": kev_payload.get("dateReleased"),
                    "catalog_count": kev_payload.get("count"),
                    "new_in_window": len(recent_kev_ids),
                },
                "nvd": {
                    "api": "https://services.nvd.nist.gov/rest/json/cves/2.0",
                    "recent_change_count": nvd_payload.get("totalResults", 0),
                    "supplemental_kev_fetch_count": len(supplemental),
                },
                "first_epss": {
                    "api": "https://api.first.org/data/v1/epss",
                    "matched_count": len(epss_index),
                },
            },
            "summary": self._summary(items),
            "items": items,
        }

        self._write(self.output_path, result)
        self._write_raw(now, kev_payload, nvd_payload, supplemental, epss_raw)
        return result

    def _write_raw(
        self,
        now: datetime,
        kev: dict[str, Any],
        nvd: dict[str, Any],
        supplemental: list[dict[str, Any]],
        epss: list[dict[str, Any]],
    ) -> None:
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self._write(self.raw_dir / "manifest.json", {
            "collected_at": now.isoformat(),
            "files": ["cisa_kev.json", "nvd_recent.json", "nvd_supplemental_kev.json", "epss_batches.json"],
        })
        self._write(self.raw_dir / "cisa_kev.json", kev)
        self._write(self.raw_dir / "nvd_recent.json", nvd)
        self._write(self.raw_dir / "nvd_supplemental_kev.json", {"vulnerabilities": supplemental})
        self._write(self.raw_dir / "epss_batches.json", {"batches": epss})

    @staticmethod
    def _recent_kev(entry: dict[str, Any], start: datetime, end: datetime) -> bool:
        value = entry.get("dateAdded")
        if not value:
            return False
        try:
            day = datetime.fromisoformat(value).date()
        except ValueError:
            return False
        return start.date() <= day <= end.date()

    @staticmethod
    def _summary(items: list[dict[str, Any]]) -> dict[str, int]:
        return {
            "total": len(items),
            "newly_published": sum(x["change_flags"]["newly_published"] for x in items),
            "recently_modified": sum(x["change_flags"]["recently_modified"] for x in items),
            "new_kev": sum(x["change_flags"]["new_kev"] for x in items),
            "kev_total": sum(x["cisa_kev"]["listed"] for x in items),
            "critical": sum((x.get("cvss") or {}).get("severity") == "CRITICAL" for x in items),
            "with_epss": sum(x.get("epss") is not None for x in items),
        }

    @staticmethod
    def _write(path: Path, payload: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
