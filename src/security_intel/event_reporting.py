from __future__ import annotations

import json
import re
from typing import Any

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,}\b", re.IGNORECASE)

EVENT_SYSTEM_INSTRUCTION = """你是資安威脅情報分析師。報告的主體是最近 24 小時已由來源驗證機制整理的 Security Events；CVE 是事件的關聯技術細節，不是報告主體。

強制規則：
1. VERIFIED_EVENTS 中的事件標題、來源、發布時間、verification、relevance、confirmed CVEs 是輸入 Facts；不得把 discovery-only 內容升格成已確認事實。
2. 只有 confirmed_cves 可用 CVE 編號寫入正文；不得輸出任何被遮罩或未驗證的 CVE。
3. organizational relevance 代表設定檔匹配程度，不代表組織確實使用該產品；未提供 CMDB/SBOM 時不得聲稱「我們受影響」。
4. Google Search 只用於驗證/補充近期事件脈絡與官方處置來源；不得覆寫 CISA/NVD/EPSS 核心漏洞 Facts。
5. EPSS 高不代表已遭利用。只有 KEV、明確 exploitation status 或事件來源的 active exploitation 證據才能這樣描述。
6. Event Delta 必須忠實反映輸入。bootstrap 模式要說明尚無前一份 event baseline，不可把目前 24h 事件稱為「相較昨日新增」。
7. Risk / event score / priority 直接引用輸入，不得自行重算另一套分數。
8. 全文使用繁體中文；事件標題、產品名、CVE 與技術名詞可保留原文。
"""


def build_event_report_prompt(
    events: dict[str, Any],
    event_delta: dict[str, Any],
    intelligence: dict[str, Any],
    vulnerability_delta: dict[str, Any],
) -> str:
    trusted_events = [
        _prompt_event(row)
        for row in events.get("items") or []
        if (row.get("verification") or {}).get("status") != "discovery_only"
    ]
    payload = {
        "event_window": events.get("window") or {},
        "event_baseline": events.get("baseline") or {},
        "event_summary": events.get("summary") or {},
        "event_delta": {
            "mode": event_delta.get("mode"),
            "baseline": event_delta.get("baseline") or {},
            "summary": event_delta.get("summary") or {},
            "items": [_prompt_event(x) for x in event_delta.get("items") or []],
        },
        "verified_events": trusted_events,
        "vulnerability_intelligence": {
            "generated_at": intelligence.get("generated_at"),
            "summary": intelligence.get("summary") or {},
            "selection": intelligence.get("selection") or {},
            "items": [_prompt_vulnerability(x) for x in intelligence.get("items") or []],
        },
        "vulnerability_delta_summary": vulnerability_delta.get("summary") or {},
    }
    facts_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return f"""請根據下方 VERIFIED_EVENT_FACTS 產生「最近 24 小時資安事件情報簡報」。

報告應先回答：
- 最近 24 小時真正發生/被報導了哪些值得注意的資安事件？
- 哪些是官方確認、多來源交叉確認、或只有單一可信來源？
- 哪些與 Taiwan/APAC、設定的技術/產業或一般企業資產類型較相關？
- 若有關聯 CVE，再列出其 KEV/CVSS/EPSS/exploitation Facts；不要讓 CVE 清單蓋過事件本身。

請用以下結構：
# 每日資安事件情報簡報
## 24 小時態勢摘要
## 今日重要資安事件
## 24 小時新事件｜相較前一份 Event State
## 關聯漏洞與處理優先級
## 建議行動
## 資料品質與未確認事項

對每個重要事件至少說明：發生什麼、來源驗證狀態、時間、相關性範圍、confirmed CVE（若有）、為何值得注意，以及可驗證來源。沒有 CMDB/SBOM 時，不要聲稱組織實際受影響。

<VERIFIED_EVENT_FACTS>
{facts_json}
</VERIFIED_EVENT_FACTS>
"""


def render_event_first_verified_report(
    events: dict[str, Any],
    event_delta: dict[str, Any],
    intelligence: dict[str, Any],
    vulnerability_delta: dict[str, Any],
) -> str:
    event_items = list(events.get("items") or [])
    event_summary = events.get("summary") or {}
    baseline = event_delta.get("baseline") or events.get("baseline") or {}
    delta_items = list(event_delta.get("items") or [])
    vulnerabilities = list(intelligence.get("items") or [])

    lines: list[str] = [
        "# 每日資安事件情報簡報",
        "",
        "> **資料來源模式：Verified facts only（deterministic）。** 本報告先呈現最近 24 小時 Security Events，再呈現關聯漏洞；正文完全由來源資料與 deterministic 規則產生，沒有使用 LLM model memory 補寫近期事件。",
        "",
        "## 24 小時態勢摘要",
        "",
        f"- Event window：{_known((events.get('window') or {}).get('start'))} → {_known((events.get('window') or {}).get('end'))}。",
        f"- 收斂後事件：**{len(event_items)}**；P1 **{_count_priority(event_items, 'P1')}**、P2 **{_count_priority(event_items, 'P2')}**、P3 **{_count_priority(event_items, 'P3')}**、WATCH **{_count_priority(event_items, 'WATCH')}**。",
        f"- 官方來源確認：**{_count_verification(event_items, 'official_confirmed')}**；多來源交叉確認：**{_count_verification(event_items, 'corroborated')}**；單一可信來源：**{_count_verification(event_items, 'single_trusted_source')}**；僅 discovery：**{_count_verification(event_items, 'discovery_only')}**。",
        f"- Event Delta：{_event_delta_summary(event_delta, baseline)}",
        f"- 漏洞處理層：**{len(vulnerabilities)}** 筆 compact intelligence；CVE Daily Delta **{len(vulnerability_delta.get('items') or [])}** 筆。",
        "- `Relevance` 是設定檔/一般企業資產類型的匹配程度，**不是組織實際曝險證明**；未接 CMDB/SBOM 前，是否真正受影響仍為未確認。",
        "",
        "## 今日重要資安事件",
        "",
    ]

    actionable = [x for x in event_items if x.get("priority") != "WATCH"]
    watch = [x for x in event_items if x.get("priority") == "WATCH"]
    if not actionable:
        lines.append("目前沒有經來源驗證後達 P1/P2/P3 的事件；搜尋 discovery-only 項目不會被升格為正式警報。")
    else:
        for index, event in enumerate(actionable, start=1):
            lines.extend(_render_event(index, event))

    if watch:
        lines.extend(["", "### WATCH｜待更多來源確認", ""])
        lines.append("下列事件可作為搜尋線索，但目前未達可執行警報門檻：")
        for event in watch[:8]:
            verification = event.get("verification") or {}
            lines.append(
                f"- **{_safe(event.get('title'))}** — {_event_label(event.get('event_type'))} / "
                f"{_known(verification.get('status'))} / score {_known(event.get('score'))}。"
            )

    lines.extend(["", "## 24 小時新事件｜相較前一份 Event State", ""])
    if event_delta.get("mode") == "bootstrap" or baseline.get("available") is False:
        lines.append("**目前為 Event State bootstrap。** 系統已建立最近 24 小時事件基線，因此本次不把整個視窗中的事件誤稱為『相較上一份新增』；下一次執行起才會產生真正的 Event Delta。")
    elif not delta_items:
        lines.append("**相較前一份 Event State，本次沒有新增達 P1/P2/P3 門檻的事件。**")
    else:
        for index, event in enumerate(delta_items, start=1):
            lines.extend(_render_event(index, event, compact=True))

    lines.extend(["", "## 關聯漏洞與處理優先級", ""])
    if not vulnerabilities:
        lines.append("目前沒有 vulnerability intelligence candidates。")
    else:
        lines.extend(_vulnerability_table(vulnerabilities))

    lines.extend([
        "",
        "## 建議行動",
        "",
        "### 24 小時內",
        "- 先閱讀 P1/P2 事件的官方或交叉驗證來源，判斷事件是否涉及組織使用的產品、供應商、SaaS、身分系統或網路邊界設備。",
        "- 若事件關聯到 CISA KEV / known exploitation CVE，再用 CMDB、SBOM、EDR、弱掃或外網暴露清冊確認是否存在；未比對前不要把『全球事件』等同『本組織受影響』。",
        "- 對 data breach、ransomware、supply-chain 等無 CVE 事件，依涉及的 vendor/service/account/套件名稱進行 IOC、帳號、套件版本或第三方依賴盤點。",
        "",
        "### 本週內",
        "- 依 P1/P2/P3 事件整理組織自己的 technology / industry profile，逐步把 `config/event_profile.json` 從 general enterprise 調成真正的環境相關性模型。",
        "- 對單一可信來源事件等待官方或第二個可信來源確認；discovery-only 只作為 hunting / research 線索。",
        "",
        "## 資料品質與未確認事項",
        "",
        f"- Discovery articles：{_known(event_summary.get('discovered_articles'))}；24h 可用文章：{_known(event_summary.get('eligible_articles'))}；clusters：{_known(event_summary.get('cluster_count'))}。",
        f"- 排除無法確認發布時間：{_known(event_summary.get('excluded_unknown_time'))}；排除超出 24h window：{_known(event_summary.get('excluded_outside_window'))}。",
        f"- 目前 technology profile 設定數：{_known((events.get('profile') or {}).get('technology_keywords_configured'))}；industry profile 設定數：{_known((events.get('profile') or {}).get('industry_keywords_configured'))}。兩者為 0 時，網站不會宣稱特定產品屬於組織資產。",
        "- 搜尋來源提到、但尚未由 NVD / vulnerability layer 驗證的 CVE 不會被當成 confirmed CVE；正文不列其編號。",
        "",
        "## 可驗證事件來源",
        "",
    ])
    lines.extend(_event_sources(event_items))
    return "\n".join(lines).rstrip() + "\n"


def confirmed_event_cves(events: dict[str, Any]) -> list[str]:
    return sorted({
        str(cve).upper()
        for event in events.get("items") or []
        for cve in event.get("confirmed_cves") or []
    })


def _prompt_event(event: dict[str, Any]) -> dict[str, Any]:
    unverified = {str(x).upper() for x in event.get("unverified_cve_mentions") or []}
    return {
        "event_id": event.get("event_id"),
        "title": _mask_unverified_cves(event.get("title"), unverified),
        "summary": _mask_unverified_cves(event.get("summary"), unverified),
        "event_type": event.get("event_type"),
        "signals": event.get("signals") or [],
        "priority": event.get("priority"),
        "score": event.get("score"),
        "is_new": event.get("is_new"),
        "first_seen": event.get("first_seen"),
        "last_seen": event.get("last_seen"),
        "confirmed_cves": event.get("confirmed_cves") or [],
        "unverified_cve_mention_count": len(unverified),
        "linked_vulnerabilities": event.get("linked_vulnerabilities") or [],
        "verification": event.get("verification") or {},
        "relevance": event.get("relevance") or {},
        "sources": [
            {
                "title": _mask_unverified_cves(source.get("title"), unverified),
                "url": source.get("url"),
                "publisher": source.get("publisher"),
                "authority": source.get("authority"),
                "published_time": source.get("published_time"),
            }
            for source in event.get("sources") or []
        ],
    }


def _prompt_vulnerability(row: dict[str, Any]) -> dict[str, Any]:
    facts = row.get("facts") or {}
    return {
        "cve": row.get("cve") or facts.get("cve"),
        "risk": row.get("risk") or {},
        "events": row.get("events") or [],
        "facts": {
            "vendor": facts.get("vendor"),
            "product": facts.get("product"),
            "title": facts.get("title"),
            "cvss": facts.get("cvss"),
            "epss": facts.get("epss"),
            "epss_percentile": facts.get("epss_percentile"),
            "cisa_kev": facts.get("cisa_kev") or {},
            "exploitation_status": facts.get("exploitation_status") or {},
            "published_time": facts.get("published_time"),
            "updated_time": facts.get("updated_time"),
            "source_url": facts.get("source_url"),
            "provenance": facts.get("provenance") or {},
        },
    }


def _render_event(index: int, event: dict[str, Any], compact: bool = False) -> list[str]:
    verification = event.get("verification") or {}
    relevance = event.get("relevance") or {}
    confirmed = event.get("confirmed_cves") or []
    lines = [
        f"### {index}. {_safe(event.get('title'))}",
        f"- **Event / Priority**：{_event_label(event.get('event_type'))} / {_known(event.get('priority'))} / score {_known(event.get('score'))}",
        f"- **Verification**：{_known(verification.get('status'))} / confidence={_known(verification.get('confidence'))} / sources={_known(verification.get('source_count'))}",
        f"- **Time**：first_seen={_known(event.get('first_seen'))} / last_seen={_known(event.get('last_seen'))}",
        f"- **Relevance**：level={_known(relevance.get('level'))} / scope={_known(relevance.get('scope'))}；這是設定檔匹配，不代表組織已確認受影響。",
        f"- **Confirmed CVE**：{', '.join(confirmed) if confirmed else '無 / 未確認'}",
    ]
    if event.get("unverified_cve_mentions"):
        lines.append(f"- **Unverified CVE mentions**：來源另提及 {len(event.get('unverified_cve_mentions') or [])} 個 CVE 編號，尚未驗證，因此正文不列編號。")
    if not compact and event.get("summary"):
        lines.append(f"- **來源摘要（原文/節錄）**：{_safe(event.get('summary'))}")
    if not compact:
        sources = event.get("sources") or []
        for source in sources[:5]:
            lines.append(
                f"- **Source**：[{_safe(source.get('publisher') or source.get('domain') or '來源')}]({_safe_url(source.get('url'))}) — "
                f"{_known(source.get('authority'))} / {_known(source.get('published_time'))}"
            )
    lines.append("")
    return lines


def _vulnerability_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        facts = row.get("facts") or {}
        risk = row.get("risk") or {}
        cvss = facts.get("cvss") or {}
        kev = facts.get("cisa_kev") or {}
        exploit = facts.get("exploitation_status") or {}
        lines.append(
            "| " + " | ".join([
                _table(row.get("cve") or facts.get("cve")),
                _table(f"{_known(risk.get('priority'))} / {_known(risk.get('score'))}"),
                _table(f"{_known(facts.get('vendor'))} / {_known(facts.get('product'))}"),
                _table(f"{_known(cvss.get('score'))} {_known(cvss.get('severity'))}"),
                _table(facts.get("epss")),
                _table("listed" if kev.get("listed") else "not listed"),
                _table(exploit.get("status")),
            ]) + " |"
        )
    return lines


def _event_sources(events: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    seen: set[str] = set()
    for event in events:
        for source in event.get("sources") or []:
            url = str(source.get("url") or "").strip()
            if not url.startswith("https://") or url in seen:
                continue
            seen.add(url)
            label = _safe(source.get("publisher") or source.get("domain") or "來源")
            lines.append(f"- [{label}]({url}) — {_safe(source.get('title'))}")
    return lines or ["- 本次沒有可列出的事件來源。"]


def _event_delta_summary(event_delta: dict[str, Any], baseline: dict[str, Any]) -> str:
    if event_delta.get("mode") == "bootstrap" or baseline.get("available") is False:
        return "bootstrap（本次只建立基線，不宣稱相較前次新增）"
    count = (event_delta.get("summary") or {}).get("new_notable_count")
    return f"**{_known(count)}** 個相較前次新增且達 P1/P2/P3 的事件"


def _count_priority(items: list[dict[str, Any]], priority: str) -> int:
    return sum(str(x.get("priority")) == priority for x in items)


def _count_verification(items: list[dict[str, Any]], status: str) -> int:
    return sum((x.get("verification") or {}).get("status") == status for x in items)


def _event_label(value: Any) -> str:
    labels = {
        "active_exploitation": "Active exploitation",
        "zero_day": "Zero-day",
        "ransomware": "Ransomware",
        "supply_chain": "Supply chain",
        "data_breach": "Data breach",
        "malware_campaign": "Malware campaign",
        "phishing": "Phishing",
        "ddos_disruption": "DDoS / disruption",
        "vulnerability": "Vulnerability",
        "general": "Security event",
    }
    return labels.get(str(value), _known(value))


def _mask_unverified_cves(value: Any, unverified: set[str]) -> str | None:
    if value is None:
        return None
    text = str(value)
    for cve in unverified:
        text = re.sub(re.escape(cve), "[未驗證CVE]", text, flags=re.IGNORECASE)
    return text


def _safe(value: Any) -> str:
    if value is None:
        return "未確認"
    return str(value).replace("\n", " ").replace("\r", " ").strip() or "未確認"


def _safe_url(value: Any) -> str:
    raw = str(value or "").strip()
    return raw if raw.startswith("https://") else "#"


def _known(value: Any) -> str:
    if value is None or value == "":
        return "未確認"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _table(value: Any) -> str:
    return _safe(value).replace("|", "\\|")
