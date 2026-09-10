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


def render_verified_facts_report(
    intelligence: dict[str, Any],
    delta: dict[str, Any],
) -> str:
    """Render a report without an LLM, using only compact verified facts.

    This is the safe fallback when Google Search grounding is unavailable.
    The renderer does not infer affected versions, exploit status, campaign
    attribution, patch names, or vendor guidance from free text.
    """
    items = list(intelligence.get("items") or [])
    delta_items = list(delta.get("items") or [])
    intel_summary = intelligence.get("summary") or {}
    delta_summary = delta.get("summary") or {}
    baseline = delta.get("baseline") or {}

    p1 = [row for row in items if _priority(row) == "P1"]
    p2 = [row for row in items if _priority(row) == "P2"]
    p3 = [row for row in items if _priority(row) == "P3"]
    watch = [row for row in items if _priority(row) == "WATCH"]

    meaningful = _as_int(delta_summary.get("meaningful_change_count"), len(delta_items))
    event_counts = delta_summary.get("events") or {}
    p1_count = _as_int(intel_summary.get("p1"), len(p1))
    p2_count = _as_int(intel_summary.get("p2"), len(p2))
    p3_count = _as_int(intel_summary.get("p3"), len(p3))
    selected_count = _as_int(
        (intelligence.get("selection") or {}).get("selected_count"),
        len(items),
    )

    lines: list[str] = [
        "# 每日資安威脅情報簡報",
        "",
        "> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。",
        "",
        "## 執行摘要",
        "",
        f"- Daily Delta：**{meaningful}** 筆符合目前門檻的重要變化；事件統計：{_event_counts_text(event_counts)}。",
        f"- Intelligence 候選：**{selected_count}** 筆；P1 **{p1_count}**、P2 **{p2_count}**、P3 **{p3_count}**、WATCH **{len(watch)}**。",
        f"- Baseline：{_baseline_text(baseline)}。",
    ]

    if p1:
        top = "、".join(_cve(row) for row in p1[:5])
        lines.append(f"- 目前排序最前的 P1：{top}。此排序直接沿用 deterministic risk score，不由本報告重新評分。")
    else:
        lines.append("- 目前 compact intelligence 中沒有 P1 項目。")

    lines.extend(["", "## Daily Delta｜自上一份報告的重要變化", ""])
    if meaningful == 0 or not delta_items:
        lines.append("**本次未偵測到符合門檻的重大 Daily Delta。**")
    else:
        lines.append(f"本次共有 **{len(delta_items)}** 筆 delta item；以下欄位直接取自 `data/delta.json`。")
        lines.append("")
        for index, row in enumerate(delta_items, start=1):
            lines.extend(_render_delta_item(index, row))

    lines.extend(["", "## P1｜立即優先處理", ""])
    if not p1:
        lines.append("目前沒有 P1 項目。")
    else:
        lines.append("以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。")
        lines.append("")
        for index, row in enumerate(p1[:10], start=1):
            lines.extend(_render_p1_item(index, row))
        if len(p1) > 10:
            lines.extend(["", "### 其他 P1", ""])
            lines.extend(_compact_table(p1[10:]))

    lines.extend(["", "## P2 / P3｜排程處理與監控", ""])
    if p2 or p3:
        lines.extend(_compact_table([*p2, *p3]))
    else:
        lines.append("目前沒有 P2 / P3 項目。")

    lines.extend(["", "## WATCH｜新增或待觀察項目", ""])
    if watch:
        lines.extend(_compact_table(watch))
    else:
        lines.append("目前沒有 WATCH 項目。")

    lines.extend(
        [
            "",
            "## 建議行動",
            "",
            "### 24 小時內",
            "- 以資產清冊、CMDB 或 SBOM 比對所有 P1 與 CISA KEV 項目是否存在於環境；本報告未取得組織資產清冊，因此實際曝險狀態為**未確認**。",
            "- 對已列 CISA KEV 的項目，依本報告列出的 **CISA Required Action（原文）** 與官方來源核對後執行；不要由本報告自行推定適用版本。",
            "",
            "### 本週內",
            "- 檢視 P2 / P3 與 WATCH 項目的 NVD / vendor 來源，確認實際使用版本與官方處置；compact intelligence 未提供結構化受影響版本時，一律視為**未確認**。",
            "- 對 exploitation status 為 `unconfirmed` 的項目持續等待官方或可信來源更新；EPSS 不作為『已遭利用』的證據。",
            "",
            "### 持續監控",
            "- 持續比較 KEV、EPSS、CVSS 與 exploitation status 的跨日變化；只有資料來源狀態變更才更新對應事實。",
            "- Google Search grounding 恢復後，才允許 LLM 以有 citation 的方式補充 vendor advisory、修補與近期攻擊脈絡。",
            "",
            "## 產業影響",
            "",
            "本 Facts-only 模式**不進行未驗證的產業攻擊歸因**。是否影響台灣金融、製造、科技、政府或關鍵基礎設施，必須與組織自身的 CMDB、SBOM、軟體清冊及外網暴露面比對；目前輸入未提供該類組織資產資料，因此實際產業/組織受影響狀態為**未確認**。",
            "",
            "## 資料品質與未確認事項",
            "",
        ]
    )

    quality = _quality_summary(items)
    lines.extend(
        [
            f"- Intelligence items：{len(items)}；缺少 Vendor：{quality['missing_vendor']}；缺少 Product：{quality['missing_product']}；缺少 Title：{quality['missing_title']}。",
            f"- EPSS 未確認：{quality['missing_epss']}；Exploitation status 未確認：{quality['unconfirmed_exploitation']}。",
            f"- 結構化受影響版本未提供：{quality['missing_affected_versions']}。本 renderer **不會**從 description 自行解析或猜測版本。",
            "- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。",
            f"- Intelligence generated at：`{_known(intelligence.get('generated_at'))}`；Delta generated at：`{_known(delta.get('generated_at'))}`。",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


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


def _render_delta_item(index: int, row: dict[str, Any]) -> list[str]:
    facts = row.get("facts") or {}
    risk = row.get("risk") or {}
    lines = [
        f"### {index}. {_cve(row)}｜{_known(facts.get('vendor'))} / {_known(facts.get('product'))}",
        f"- **Delta event**：{_events_text(row.get('events') or [])}",
        f"- **Risk**：{_known(risk.get('priority'))} / score {_known(risk.get('score'))}；reasons：{_risk_reasons_text(risk.get('reasons') or [])}",
        f"- **CVSS**：{_cvss_text(facts.get('cvss'))}",
        f"- **EPSS**：{_epss_text(facts)}",
        f"- **CISA KEV**：{_kev_text(facts.get('cisa_kev'))}",
        f"- **Exploitation status**：{_exploit_text(facts.get('exploitation_status'))}",
        f"- **Known ransomware campaign use**：{_ransomware_text(facts.get('cisa_kev'))}",
        f"- **Published / Updated**：{_known(facts.get('published_time'))} / {_known(facts.get('updated_time'))}",
        f"- **官方描述（原文）**：{_official_text(facts.get('description'))}",
        "",
    ]
    return lines


def _render_p1_item(index: int, row: dict[str, Any]) -> list[str]:
    facts = row.get("facts") or {}
    risk = row.get("risk") or {}
    kev = facts.get("cisa_kev") or {}
    action = _official_text(kev.get("required_action"))
    affected = _affected_versions_text(facts)
    return [
        f"### {index}. {_cve(row)}｜{_known(facts.get('vendor'))} / {_known(facts.get('product'))}",
        f"- **Title**：{_known(facts.get('title'))}",
        f"- **Risk**：{_known(risk.get('priority'))} / score {_known(risk.get('score'))}；reasons：{_risk_reasons_text(risk.get('reasons') or [])}",
        f"- **CVSS**：{_cvss_text(facts.get('cvss'))}",
        f"- **EPSS**：{_epss_text(facts)}",
        f"- **CISA KEV**：{_kev_text(kev)}",
        f"- **Exploitation status**：{_exploit_text(facts.get('exploitation_status'))}",
        f"- **Known ransomware campaign use**：{_ransomware_text(kev)}",
        f"- **受影響版本**：{affected}",
        f"- **官方描述（原文）**：{_official_text(facts.get('description'))}",
        f"- **CISA Required Action（原文）**：{action}",
        "- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。",
        "",
    ]


def _compact_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        facts = row.get("facts") or {}
        risk = row.get("risk") or {}
        kev = facts.get("cisa_kev") or {}
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape_table(_cve(row)),
                    _escape_table(f"{_known(risk.get('priority'))} / {_known(risk.get('score'))}"),
                    _escape_table(f"{_known(facts.get('vendor'))} / {_known(facts.get('product'))}"),
                    _escape_table(_cvss_text(facts.get("cvss"))),
                    _escape_table(_epss_text(facts)),
                    _escape_table(_kev_text(kev)),
                    _escape_table(_exploit_text(facts.get("exploitation_status"))),
                    _escape_table(_ransomware_text(kev)),
                ]
            )
            + " |"
        )
    return lines


def _quality_summary(rows: list[dict[str, Any]]) -> dict[str, int]:
    result = {
        "missing_vendor": 0,
        "missing_product": 0,
        "missing_title": 0,
        "missing_epss": 0,
        "unconfirmed_exploitation": 0,
        "missing_affected_versions": 0,
    }
    for row in rows:
        facts = row.get("facts") or {}
        if not facts.get("vendor"):
            result["missing_vendor"] += 1
        if not facts.get("product"):
            result["missing_product"] += 1
        if not facts.get("title"):
            result["missing_title"] += 1
        if facts.get("epss") is None:
            result["missing_epss"] += 1
        if (facts.get("exploitation_status") or {}).get("status") in {None, "unconfirmed"}:
            result["unconfirmed_exploitation"] += 1
        if _affected_versions_text(facts).startswith("未確認"):
            result["missing_affected_versions"] += 1
    return result


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


def _cve(row: dict[str, Any]) -> str:
    facts = row.get("facts") or {}
    return str(row.get("cve") or facts.get("cve") or "未確認").upper()


def _priority(row: dict[str, Any]) -> str:
    return str((row.get("risk") or {}).get("priority") or "UNCONFIRMED").upper()


def _event_counts_text(events: Any) -> str:
    if not isinstance(events, dict) or not events:
        return "無"
    return "、".join(f"{_clean_inline(key)}={_known(value)}" for key, value in events.items())


def _baseline_text(baseline: dict[str, Any]) -> str:
    available = baseline.get("available")
    if available is False:
        return "不可用（首次執行或尚無前一份 state）"
    return f"{_known(baseline.get('type'))} / generated_at={_known(baseline.get('generated_at'))} / available={_known(available)}"


def _events_text(events: list[dict[str, Any]]) -> str:
    if not events:
        return "無"
    rendered: list[str] = []
    for event in events:
        event_type = _known(event.get("type"))
        before = _known(event.get("from"))
        after = _known(event.get("to"))
        rendered.append(f"{event_type} (from={before}; to={after})")
    return "；".join(rendered)


def _risk_reasons_text(reasons: list[dict[str, Any]]) -> str:
    if not reasons:
        return "未確認"
    return "、".join(
        f"{_known(row.get('code'))}(+{_known(row.get('points'))})" for row in reasons
    )


def _cvss_text(value: Any) -> str:
    if not isinstance(value, dict) or value.get("score") is None:
        return "未確認"
    version = _known(value.get("version"))
    score = _known(value.get("score"))
    severity = _known(value.get("severity"))
    return f"v{version} {score} ({severity})"


def _epss_text(facts: dict[str, Any]) -> str:
    epss = facts.get("epss")
    percentile = facts.get("epss_percentile")
    if epss is None:
        return "未確認"
    if percentile is None:
        return f"{epss} / percentile=未確認"
    return f"{epss} / percentile={percentile}"


def _kev_text(value: Any) -> str:
    if not isinstance(value, dict):
        return "未確認"
    listed = value.get("listed")
    if listed is True:
        return f"listed=true / date_added={_known(value.get('date_added'))} / due_date={_known(value.get('due_date'))}"
    if listed is False:
        return "listed=false"
    return "未確認"


def _exploit_text(value: Any) -> str:
    if not isinstance(value, dict):
        return "未確認"
    return f"status={_known(value.get('status'))} / source={_known(value.get('source'))}"


def _ransomware_text(kev: Any) -> str:
    if not isinstance(kev, dict):
        return "未確認"
    return _known(kev.get("known_ransomware_campaign_use"))


def _affected_versions_text(facts: dict[str, Any]) -> str:
    affected = facts.get("affected")
    if not isinstance(affected, list) or not affected:
        return "未確認（compact intelligence 未提供結構化受影響版本）"

    values: list[str] = []
    for row in affected:
        if not isinstance(row, dict):
            continue
        versions = row.get("versions")
        if not isinstance(versions, list):
            continue
        for version in versions:
            if isinstance(version, dict):
                text = version.get("version")
                if text:
                    values.append(str(text))
            elif version:
                values.append(str(version))
    values = list(dict.fromkeys(values))
    if not values:
        return "未確認（未找到結構化 version 值）"
    return "、".join(_clean_inline(x) for x in values[:20])


def _official_text(value: Any) -> str:
    if value is None or value == "":
        return "未確認"
    return _clean_inline(value)


def _known(value: Any) -> str:
    if value is None or value == "":
        return "未確認"
    if isinstance(value, bool):
        return "true" if value else "false"
    return _clean_inline(value)


def _clean_inline(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value)).strip()


def _escape_table(value: Any) -> str:
    return _clean_inline(value).replace("|", "\\|")


def _as_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return int(default)


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
