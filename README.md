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

目前偵測事件包含：`NEW_CVE`、`NEW_KEV`、`EPSS_INCREASED`、`EXPLOITATION_CHANGED`、`CVSS_CHANGED`、`RANSOMWARE_USE_CHANGED`。

CVE 沒出現在新的 48 小時 NVD window 不代表已修補或風險消失，因此不會產生 resolved 類型推論。Risk Score 為 deterministic 且可解釋，每筆保存 `risk.reasons`，不交給 LLM 黑箱打分。

## Grounded Report

報告輸入只有 `data/intelligence.json` 與 `data/delta.json`。Gemini 不允許新增輸入之外的 CVE，也不得覆寫 CVSS、EPSS、KEV、exploit status 等核心 Facts。

Google Search grounding 只用於補充 Vendor Security Advisory、修補/緩解建議、近期公開攻擊背景與其他需要即時驗證的脈絡。

```text
GEMINI_SEARCH_MODE=auto      # 預設：優先 Search；不可用時安全降級
GEMINI_SEARCH_MODE=required  # Search 必須成功，否則 report job 失敗
GEMINI_SEARCH_MODE=off       # 不呼叫 Search，只使用 verified facts
```

`auto` transport 順序：

```text
Interactions API + Google Search
            ↓ transient transport error
GenerateContent + Google Search
            ↓ Search quota / transient error
GenerateContent + VERIFIED_FACTS_ONLY
```

`verified_facts_only` 模式下，模型不得用既有知識新增近期漏洞事實、版本、修補細節或攻擊事件，只能重述/分析 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 已提供的資料；不知道的資訊維持「未確認」。正文與 metadata 都會明確記錄降級狀態。

### Model fallback

模型本身也可能因 high demand 暫時回 503。V2 因此把 model fallback 與 fact fallback 分開：只有 transient 429/5xx/timeout/connection error 才能切換模型，401/403/400 等認證、權限或參數錯誤會直接失敗。

預設 stable model chain：

```text
gemini-3.8-flash
  → gemini-3.7-flash
  → gemini-3.6-flash
```

fallback chain 由 `GEMINI_FALLBACK_MODELS` 控制，不綁死程式。Google Search 路徑若直接遇到 quota 429，不會輪替模型浪費 Search request；進入 facts-only 後若模型本身暫時不可用，才會依序嘗試 fallback model。metadata 會保存 requested model、actual model、attempted models 與 fallback reason。

為避免 SDK transient retry 讓單一報告卡住過久，Search request 預設 timeout 45 秒、facts-only 120 秒，SDK 僅做有限重試，再交由明確的 transport/model fallback 策略處理。

生成後寫入：

```text
reports/security_report_latest.md
reports/security_report_metadata.json
```

metadata 保存 Gemini requested/actual model、model fallback trace、API mode、interaction/response ID、grounding mode/fallback reason、Google Search citations/queries（若有）、request timeout、token usage，以及 `delta.json` / `intelligence.json` 的 SHA-256。

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

data/
  state.json
  delta.json
  intelligence.json
  raw/

reports/
  security_report_latest.md
  security_report_metadata.json
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
export GEMINI_FALLBACK_MODELS=gemini-3.7-flash,gemini-3.6-flash
export GEMINI_SEARCH_MODE=auto
python scripts/generate_report_v2.py
python scripts/validate_report.py
```

API Key 不得 commit 到 repository。GitHub Actions 使用 repository secrets / variables：

```text
NVD_API_KEY                 # optional
GEMINI_API_KEY              # required
GEMINI_MODEL                # optional; default gemini-3.8-flash
GEMINI_FALLBACK_MODELS      # optional; default 3.7 Flash, 3.6 Flash
GEMINI_SEARCH_MODE          # optional: auto / required / off; default auto
GEMINI_SEARCH_TIMEOUT_MS    # optional; default 45000
GEMINI_FACTS_TIMEOUT_MS     # optional; default 120000
```

## GitHub Actions

`V2 Security Intelligence Collector` 每天台北時間 09:00 執行，產生 full artifact、compact state、Daily Delta 與最多 30 筆 intelligence candidates。

`V2 Grounded Security Intelligence Report` 在 main Collector 成功後接續執行，也可手動執行。Validation 會拒絕 LLM 新增未在 verified intelligence 中的 CVE，並檢查 input hash、grounding mode 與 model fallback metadata 一致性。

## 後續階段

1. 驗證 V2 Report 每日穩定性與來源品質
2. Cloudflare R2 保存長期 raw / full snapshots
3. Vendor advisories direct collectors，降低對付費 Search grounding 的依賴
4. HTML Email
5. TWCERT/CC 與其他台灣資安來源
6. Dashboard / historical trends / D1 評估

舊版 Gemini / Email 程式目前保留為 manual-only，待 V2 report 穩定後再移除。
