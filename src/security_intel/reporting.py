from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,}\b", re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s;<>\"]+")

SYSTEM_INSTRUCTION = """你是資安威脅情報分析師。你的工作是把已由官方 API 驗證的威脅 Facts 轉成可執行的繁體中文情報，不是自行尋找或創造漏洞事實。

強制規則：
1. 輸入 JSON 中的 CVE、CVSS、EPSS、EPSS percentile、CISA KEV、exploitation status、發布/更新時間是權威 Facts；不得改寫數值、不得補猜缺值。
2. Google Search 只可用於補充近期背景、vendor advisory、修補/緩解建議與已公開攻擊活動脈絡；不得用搜尋結果覆寫輸入中的核心 Facts。
3. 不得新增輸入清單之外的 CVE 編號。若搜尋發現相關 CVE，只能描述為「另有相關漏洞，未納入本報告 Facts」，且不要列出其 CVE 編號。
4. 受影響版本、修補版本、攻擊手法、勒索軟體歸因等若沒有輸入或可靠搜尋來源直接支持，必須標示「未確認」。
5. EPSS 高低不能推論成已遭利用；只有 CISA KEV 或明確 exploitation status 才可陳述已知利用情況。
6. Daily Delta 必須忠實反映輸入 delta。若 meaningful_change_count 為 0，要明確寫「本次未偵測到符合門檻的重大 Daily Delta」，不可硬湊新事件。
7. 風險優先順序以輸入 risk score / priority 為基礎，可做文字解釋，但不得自行重算成另一套分數。
8. 全文使用繁體中文；產品名、CVE、技術名詞可保留英文。
"""


def build_report_prompt(intelligence: dict[str, Any], delta: dict[str, Any]) -> str:
    payload = {
        "intelligence_generated_at": intelligence.get("generated_at"),
        "risk_version": intelligence.get("risk_version"),
        "intelligence_summary": intelligence.get("summary") or {},
        "selection": intelligence.get("selection") or {},
        "delta": {
            "generated_at": delta.get("generated_at"),
            "baseline": delta.get("baseline") or {},
            "summary": delta.get("summary") or {},
            "items": delta.get("items") or [],
        },
        "intelligence_items": [_prompt_item(x) for x in intelligence.get("items") or []],
    }

    facts_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return f"""請根據下方 VERIFIED_FACTS 產生每日資安威脅情報簡報。

報告目標：
- 第一優先回答「從上一份報告到現在，有什麼重要變化？」
- 若沒有重大 Delta，明確說明沒有新變化，再呈現目前最高優先的持續風險。
- 聚焦約 8–12 個最值得採取行動的項目，其餘可用簡短 watchlist 表格呈現。
- 對 P1 說明為何需要優先處理；對 P3 說明監控或排程修補理由。
- 搜尋近期 vendor advisory 或可信來源補充「修補 / 緩解 / 已公開攻擊背景」，必要時才搜尋，不要為每一筆都強制搜尋。
- 不要生成沒有資料支持的統計；所有數量應直接從輸入 summary 計算或引用。

請使用以下 Markdown 結構：
# 每日資安威脅情報簡報

## 執行摘要
用 3–5 點概括今日重點，包含 Delta 是否存在、P1/P2/P3 數量與最需優先處理的產品。

## Daily Delta｜自上一份報告的重要變化
逐項說明 delta events；若為 0，直接寫明本次沒有符合門檻的重大變化。

## P1｜立即優先處理
每項至少包含：CVE、Vendor / Product、已驗證風險 Facts、為何優先、建議處置。受影響版本若未確認就寫「未確認」。

## P2 / P3｜排程處理與監控
用精簡表格呈現高風險但優先度較低的項目。

## 建議行動
分成「24 小時內」、「本週內」、「持續監控」。建議要能對應上述威脅，不要寫泛泛而談的安全口號。

## 產業影響
只針對有合理關聯的台灣企業情境（例如金融、製造、科技、政府/關鍵基礎設施）做簡潔分析；沒有證據就不要聲稱特定產業正在遭攻擊。

## 資料品質與未確認事項
列出 Facts 中缺失或仍需 vendor confirmation 的重要欄位。

不要自行建立「資料來源」章節，系統會在生成後以程式附加可驗證來源。

<VERIFIED_FACTS>
{facts_json}
</VERIFIED_FACTS>
"""


def render_source_appendix(
    report_text: str,
    intelligence: dict[str, Any],
    grounding_citations: list[dict[str, Any]] | None = None,
) -> str:
    facts_by_cve = {
        str((row.get("facts") or {}).get("cve") or row.get("cve") or "").upper(): row.get("facts") or {}
        for row in intelligence.get("items") or []
    }
    mentioned = ordered_cves(report_text)
    mentioned = [cve for cve in mentioned if cve in facts_by_cve]
    if not mentioned:
        mentioned = list(facts_by_cve)[:10]

    lines = ["", "---", "", "## 可驗證資料來源", ""]
    for cve in mentioned:
        facts = facts_by_cve[cve]
        sources = fact_sources(facts)
        if not sources:
            continue
        rendered = " · ".join(f"[{label}]({url})" for label, url in sources)
        lines.append(f"- **{cve}** — {rendered}")

    citations = _dedupe_grounding(grounding_citations or [])
    if citations:
        lines.extend(["", "### Google Search Grounding", ""])
        for row in citations:
            title = _clean_title(row.get("title")) or _domain(row.get("url")) or "Grounding source"
            lines.append(f"- [{title}]({row['url']})")

    lines.extend(
        [
            "",
            "> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。",
            "",
        ]
    )
    return "\n".join(lines)


def fact_sources(facts: dict[str, Any]) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    provenance = facts.get("provenance") or {}
    labels = {"nvd": "NVD", "cisa_kev": "CISA KEV", "epss": "FIRST EPSS"}
    for key in ("nvd", "cisa_kev", "epss"):
        url = provenance.get(key)
        if url and url not in seen:
            out.append((labels[key], str(url)))
            seen.add(str(url))

    notes = (facts.get("cisa_kev") or {}).get("notes") or ""
    for url in URL_RE.findall(str(notes)):
        url = url.rstrip(".,)]}")
        if url in seen:
            continue
        out.append((_source_label(url), url))
        seen.add(url)
    return out


def ordered_cves(text: str) -> list[str]:
    return list(dict.fromkeys(x.upper() for x in CVE_RE.findall(text or "")))


def unknown_report_cves(report_text: str, intelligence: dict[str, Any]) -> list[str]:
    allowed = {
        str((x.get("facts") or {}).get("cve") or x.get("cve") or "").upper()
        for x in intelligence.get("items") or []
    }
    return [cve for cve in ordered_cves(report_text) if cve not in allowed]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _prompt_item(row: dict[str, Any]) -> dict[str, Any]:
    facts = row.get("facts") or {}
    kev = facts.get("cisa_kev") or {}
    exploit = facts.get("exploitation_status") or {}
    return {
        "cve": row.get("cve") or facts.get("cve"),
        "events": row.get("events") or [],
        "risk": row.get("risk") or {},
        "facts": {
            "vendor": facts.get("vendor"),
            "product": facts.get("product"),
            "title": facts.get("title"),
            "description": facts.get("description"),
            "cvss": facts.get("cvss"),
            "epss": facts.get("epss"),
            "epss_percentile": facts.get("epss_percentile"),
            "cisa_kev": {
                "listed": kev.get("listed", False),
                "date_added": kev.get("date_added"),
                "due_date": kev.get("due_date"),
                "required_action": kev.get("required_action"),
                "known_ransomware_campaign_use": kev.get("known_ransomware_campaign_use"),
                "notes": kev.get("notes"),
            },
            "exploitation_status": exploit,
            "published_time": facts.get("published_time"),
            "updated_time": facts.get("updated_time"),
            "source_url": facts.get("source_url"),
            "provenance": facts.get("provenance") or {},
        },
    }


def _source_label(url: str) -> str:
    domain = _domain(url)
    if "cisa.gov" in domain:
        return "CISA"
    if "nist.gov" in domain:
        return "NVD"
    if "first.org" in domain:
        return "FIRST EPSS"
    return f"Vendor / Advisory ({domain})" if domain else "Vendor / Advisory"


def _domain(url: str | None) -> str:
    if not url:
        return ""
    try:
        return urlparse(url).netloc.lower().removeprefix("www.")
    except Exception:
        return ""


def _dedupe_grounding(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for row in rows:
        url = row.get("url")
        if not url or url in seen:
            continue
        seen.add(str(url))
        out.append(row)
    return out


def _clean_title(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"[\[\]\n\r]+", " ", str(value)).strip()
