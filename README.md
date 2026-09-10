# Security Report Automation V2

可信、即時、可驗證的每日資安威脅情報自動化系統。

## 核心原則

**Search / API 負責 Facts，LLM 負責 Intelligence。**

V2 不要求 LLM 依模型既有知識產生最近幾天的 CVE、CVSS、EPSS、KEV 或 exploit 狀態。所有時效性事實先由官方資料來源取得，再交給 deterministic scoring 與 LLM 做繁體中文摘要、風險分析與處置建議。

## 目前資料流

```text
CISA KEV + NVD CVE API 2.0 + FIRST EPSS
                    ↓
           Normalize / Deduplicate
                    ↓
        full latest.json + raw payloads
          （GitHub Actions artifact）
                    ↓
        Previous State / Daily Delta
                    ↓
       Deterministic Risk Scoring
                    ↓
        data/intelligence.json
           （最多 30 筆）
                    ↓
 Gemini + optional Google Search Grounding
                    ↓
 reports/security_report_latest.md
```

## Facts Collector

- CISA KEV：canonical JSON feed，失敗時 fallback 到 CISA 官方 `cisagov/kev-data` mirror
- NVD：抓指定 lookback window 內 `lastModified` 的 CVE
- 新 KEV 若未出現在當期 NVD modified window，依 CVE ID 補抓 NVD
- FIRST EPSS：依 CVE 批次 enrich `epss` 與 `percentile`
- Raw payload 與完整 `data/latest.json` 只存在 GitHub Actions artifact，不寫入 Git history
- 未確認欄位使用 `null` 或 `unconfirmed`，不得自行猜測
- EPSS 不會被推論成 exploitation status

## Daily Delta / Risk Scoring

Repository 只保留 compact state：

```text
data/state.json          # 高風險 CVE 狀態，用於跨日比較與 EPSS monitoring
data/delta.json          # 從上一份 state 到現在的重要變化
data/intelligence.json   # 最多 30 筆，提供給 LLM 的可信候選集
```

目前偵測事件包含：

- `NEW_CVE`：Critical-first；High 必須搭配 KEV / exploit / EPSS 等額外風險訊號
- `NEW_KEV`
- `EPSS_INCREASED`
- `EXPLOITATION_CHANGED`
- `CVSS_CHANGED`
- `RANSOMWARE_USE_CHANGED`

CVE 沒出現在新的 48 小時 NVD window 不代表已修補或風險消失，因此不會產生 resolved 類型推論。

Risk Score 為 deterministic 且可解釋，每筆會保存 `risk.reasons`。KEV、已知利用、勒索軟體使用、CVSS、EPSS 與重大狀態變化依固定權重加分，不交給 LLM 黑箱打分。

## Grounded Report

V2 報告使用獨立 workflow，不與 Collector 綁死。Collector 失敗與 Gemini / Search 失敗會分開處理。

報告輸入只有 `data/intelligence.json` 與 `data/delta.json`。Gemini 不允許新增輸入之外的 CVE，也不得覆寫 CVSS、EPSS、KEV、exploit status 等核心 Facts。

Google Search grounding 只用於補充：

- Vendor Security Advisory
- 修補 / 緩解建議
- 近期公開攻擊背景
- 其他需要即時驗證的脈絡

Gemini API 的 Google Search grounding 可能受方案與 quota 限制，因此 V2 支援三種模式：

```text
GEMINI_SEARCH_MODE=auto      # 預設：先嘗試 Search；quota 429 時安全降級
GEMINI_SEARCH_MODE=required  # Search 必須成功，否則 report job 失敗
GEMINI_SEARCH_MODE=off       # 不呼叫 Search，只使用 verified facts
```

`auto` 若因 Google Search quota 不可用而降級，會切換成 `verified_facts_only`：模型不得用既有知識新增近期漏洞事實、版本、修補細節或攻擊事件，只能重述/分析 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 已提供的資料。報告正文與 metadata 都會明確記錄降級狀態，不會靜默假裝已做即時搜尋。

受影響版本、修補版本、攻擊歸因等若沒有可靠來源，報告必須標示「未確認」。

生成後另寫：

```text
reports/security_report_latest.md
reports/security_report_metadata.json
```

metadata 會保存 Gemini model、interaction ID、grounding mode / fallback reason、Google Search citations / queries（若有）、token usage，以及輸入 `delta.json` / `intelligence.json` 的 SHA-256，方便驗證報告來源。

## 目錄

```text
.github/workflows/
  v2-collect.yml
  v2-report.yml
  aily-report-gemini.yml       # legacy manual-only

src/security_intel/
  http.py
  normalize.py
  pipeline.py
  intelligence.py
  reporting.py
  collectors/
    cisa_kev.py
    nvd.py
    epss.py
  llm/
    gemini.py

scripts/
  collect_v2.py
  validate_latest.py
  build_intelligence.py
  validate_intelligence.py
  generate_report_v2.py
  validate_report.py
  generate_report_gemini.py    # legacy
  send_email_gemini.py         # legacy

data/
  state.json
  delta.json
  intelligence.json
  raw/

reports/
  security_report_latest.md
  security_report_metadata.json

tests/
  test_normalize.py
  test_intelligence.py
  test_reporting.py
  test_gemini.py
```

## 本機執行

Collector：

```bash
pip install -r requirements.txt
python scripts/collect_v2.py --lookback-hours 48
python scripts/validate_latest.py
python scripts/build_intelligence.py
python scripts/validate_intelligence.py
```

Report：

```bash
pip install -r requirements-report.txt
export GEMINI_API_KEY=...
export GEMINI_MODEL=gemini-3.8-flash
export GEMINI_SEARCH_MODE=auto
python scripts/generate_report_v2.py
python scripts/validate_report.py
```

API Key 不得 commit 到 repository。GitHub Actions 使用 repository secrets / variables：

```text
NVD_API_KEY          # optional
GEMINI_API_KEY       # required for V2 report
GEMINI_MODEL         # optional repository variable; default gemini-3.8-flash
GEMINI_SEARCH_MODE   # optional: auto / required / off; default auto
```

## GitHub Actions

### V2 Security Intelligence Collector

- 每天台北時間 09:00（UTC 01:00）
- 支援手動執行
- 程式更新 merge 到 main 時自動重新跑一次
- Unit tests、Collector、JSON validation、Daily Delta、Risk Scoring
- full snapshot / raw payload 保存為 artifact
- main 只 commit `state.json`、`delta.json`、`intelligence.json`

### V2 Grounded Security Intelligence Report

- Collector 在 main 成功後自動接續
- 可手動執行
- 優先使用 Gemini + Google Search grounding；quota 不允許時可透明降級為 verified-facts-only
- 產生 Markdown report + report metadata
- Validation 會拒絕 LLM 新增未在 verified intelligence 中的 CVE
- facts-only mode 必須在正文與 metadata 明確標示，且不可留下假的 Search query/citation

## 後續階段

1. 驗證 V2 Report 每日穩定性與來源品質
2. Cloudflare R2 保存長期 raw / full snapshots
3. Vendor advisories direct collectors，降低對付費 Search grounding 的依賴
4. HTML Email
5. TWCERT/CC 與其他台灣資安來源
6. Dashboard / historical trends / D1 評估

舊版 Gemini / Email 程式目前保留為 manual-only，待 V2 report 穩定後再移除。
