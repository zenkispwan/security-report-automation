# Security Report Automation V2

可信、即時、可驗證的每日資安威脅情報自動化系統。

## 核心原則

**Search / API 負責 Facts，LLM 負責 Intelligence。**

V2 不要求 LLM 依模型既有知識產生最近幾天的 CVE、CVSS、EPSS、KEV、exploit 狀態、受影響版本或修補資訊。所有時效性事實先由官方資料來源取得，再交給 deterministic scoring；只有 Google Search grounding 成功時，LLM 才負責有來源的即時 enrichment 與繁體中文情報整理。

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
        Google Search grounding
             ↙            ↘
          成功              不可用/停用
           ↓                  ↓
 Gemini Intelligence     Deterministic
      Report          Verified-Facts Report
             ↘            ↙
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
data/intelligence.json   # 最多 30 筆，提供給報告層的可信候選集
```

目前偵測事件包含：`NEW_CVE`、`NEW_KEV`、`EPSS_INCREASED`、`EXPLOITATION_CHANGED`、`CVSS_CHANGED`、`RANSOMWARE_USE_CHANGED`。

CVE 沒出現在新的 48 小時 NVD window 不代表已修補或風險消失，因此不會產生 resolved 類型推論。Risk Score 為 deterministic 且可解釋，每筆保存 `risk.reasons`，不交給 LLM 黑箱打分。

## Report Trust Boundary

報告輸入只有 `data/intelligence.json` 與 `data/delta.json`。CVE、CVSS、EPSS、KEV、exploitation status、發布/更新時間等核心 Facts 以 Collector 輸入為準。

Google Search grounding 只用於補充：

- Vendor Security Advisory
- 修補 / 緩解建議
- 近期公開攻擊背景
- 其他需要即時驗證的脈絡

```text
GEMINI_SEARCH_MODE=auto      # 預設：優先 Search；不可用時 deterministic 降級
GEMINI_SEARCH_MODE=required  # Search 必須成功，否則 report job 失敗
GEMINI_SEARCH_MODE=off       # 完全不呼叫 Search / LLM 正文，直接 deterministic report
```

`auto` transport 順序：

```text
Interactions API + Google Search
            ↓ transient transport error
GenerateContent + Google Search
            ↓ Search quota / exhausted transient error
Deterministic VERIFIED_FACTS_ONLY renderer
```

### 關鍵規則：Facts-only 不使用 LLM

Google Search grounding 不可用時，V2 **不再要求 Gemini 產生 facts-only 正文**。`reporting.py` 會直接從 `intelligence.json` / `delta.json` 產生 Markdown：

- Daily Delta 直接呈現 deterministic events
- Risk / priority 直接沿用 risk engine
- CVSS / EPSS / KEV / exploitation status 直接呈現來源值
- NVD description 標示為「官方描述（原文）」
- CISA Required Action 標示為「原文」
- 沒有結構化版本資料時固定顯示「未確認」
- 不從 description 自行解析版本
- 不自行補充 Patch Tuesday、Hotfix、攻擊鏈、產業歸因等模型知識

metadata 在此模式會記錄：

```text
renderer: deterministic
llm_body_used: false
model: null
usage: null
api_mode: deterministic_facts_only
```

validator 會用相同輸入重新 render，要求 deterministic report 與預期輸出完全一致；任何額外文字都會讓 validation 失敗。

### Grounded LLM mode

只有 Google Search grounding 成功並取得 citation 時，才允許 Gemini 產生正文。Gemini 不得新增輸入清單之外的 CVE，也不得覆寫 Collector 核心 Facts。受影響版本、修補版本、攻擊歸因等若沒有輸入或 grounding source 支持，必須標示「未確認」。

Interactions API 若遇到 transient transport error，會嘗試 GenerateContent + Google Search。Search 路徑的 transient 5xx/high-demand 狀況可依 `GEMINI_FALLBACK_MODELS` 切換模型；401/403/400 等認證、權限或參數錯誤直接失敗，不會被 fallback 隱藏。Search quota 429 不會輪替模型浪費 Search request。

為避免 SDK transient retry 讓單一報告卡住過久，Search request 預設 timeout 45 秒，並限制 SDK retry 次數。

## Report Metadata

生成後寫入：

```text
reports/security_report_latest.md
reports/security_report_metadata.json
```

metadata 保存：

- report renderer 與 `llm_body_used`
- Gemini requested / actual model（deterministic 模式 actual model 為 `null`）
- attempted models / model fallback reason
- API mode、interaction/response ID
- grounding mode / fallback reason
- Google Search citations / queries（若有）
- request timeout / token usage
- `delta.json` / `intelligence.json` SHA-256

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

Grounded report：

```bash
pip install -r requirements-report.txt
export GEMINI_API_KEY=...
export GEMINI_MODEL=gemini-3.8-flash
export GEMINI_FALLBACK_MODELS=gemini-3.7-flash,gemini-3.6-flash
export GEMINI_SEARCH_MODE=auto
python scripts/generate_report_v2.py
python scripts/validate_report.py
```

完全 deterministic smoke test 不需要 API key：

```bash
export GEMINI_SEARCH_MODE=off
python scripts/generate_report_v2.py
python scripts/validate_report.py
```

API Key 不得 commit 到 repository。GitHub Actions 使用 repository secrets / variables：

```text
NVD_API_KEY                 # optional
GEMINI_API_KEY              # auto / required 模式需要
GEMINI_MODEL                # optional; default gemini-3.8-flash
GEMINI_FALLBACK_MODELS      # optional; Search transient model fallback chain
GEMINI_SEARCH_MODE          # optional: auto / required / off; default auto
GEMINI_SEARCH_TIMEOUT_MS    # optional; default 45000
```

## GitHub Actions

`V2 Security Intelligence Collector` 每天台北時間 09:00 執行，產生 full artifact、compact state、Daily Delta 與最多 30 筆 intelligence candidates。

`V2 Grounded Security Intelligence Report` 在 main Collector 成功後接續執行，也可手動執行。PR CI 除完整 unit tests 外，還會以 `GEMINI_SEARCH_MODE=off` 執行 deterministic report smoke test，不需要 secret。

Validation 會檢查：

- input SHA-256 與 item count
- 未驗證 CVE
- grounding mode / citation
- requested / actual model metadata
- deterministic mode 不得出現 model response、token usage 或 Search citation
- deterministic report 必須與程式重新 render 的輸出完全一致

## 後續階段

1. 驗證 V2 Report 每日穩定性與來源品質
2. Cloudflare R2 保存長期 raw / full snapshots
3. Vendor advisories direct collectors，降低對付費 Search grounding 的依賴
4. HTML Email
5. TWCERT/CC 與其他台灣資安來源
6. Dashboard / historical trends / D1 評估

舊版 Gemini / Email 程式目前保留為 manual-only，待 V2 report 穩定後再移除。
