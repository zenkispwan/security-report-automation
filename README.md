# Security Report Automation V2

可信、即時、可驗證的每日資安威脅情報自動化系統。

## 核心原則

**Search / API 負責 Facts，LLM 負責 Intelligence。**

V2 不再要求 LLM 依模型既有知識產生最近幾天的 CVE、CVSS、EPSS、KEV 或 exploit 狀態。所有時效性事實先由官方資料來源取得，再交給 LLM 做繁體中文摘要、風險排序與處置建議。

## Phase 1 資料流

```text
CISA KEV
   ↓
NVD CVE API 2.0
   ↓
FIRST EPSS
   ↓
Normalize / Deduplicate
   ↓
data/latest.json
```

目前 Collector：

- CISA KEV：canonical JSON feed，失敗時 fallback 到 CISA 官方 `cisagov/kev-data` mirror
- NVD：抓指定 lookback window 內 `lastModified` 的 CVE
- 新 KEV 若未出現在當期 NVD modified window，會依 CVE ID 補抓 NVD
- FIRST EPSS：依 CVE 批次 enrich `epss` 與 `percentile`
- Raw payload 存在 GitHub Actions artifact 7 天，不寫入 Git history
- Normalized facts 寫入 `data/latest.json`
- 未確認欄位使用 `null` 或 `unconfirmed`，不得自行猜測
- EPSS 不會被推論成 exploitation status

## 目錄

```text
.github/workflows/v2-collect.yml

src/security_intel/
  http.py
  normalize.py
  pipeline.py
  collectors/
    cisa_kev.py
    nvd.py
    epss.py

scripts/
  collect_v2.py
  validate_latest.py

data/
  latest.json
  raw/

tests/
  test_normalize.py
```

舊版 Gemini / Email 程式目前先保留，方便比對與回滾；V2 report generator 完成後再移除。

## Normalized record

每筆 CVE 盡可能保留：

- CVE
- Vendor / Product
- Title / Description
- CVSS
- EPSS / EPSS Percentile
- CISA KEV
- Exploitation status（KEV 或 NVD SSVC；否則 `unconfirmed`）
- Published / Updated / Collected time
- Source URL / Source type
- References / CWE / affected data
- `change_flags`: newly published / recently modified / new KEV
- provenance

## 本機執行

```bash
pip install -r requirements.txt
python scripts/collect_v2.py --lookback-hours 48
python scripts/validate_latest.py
```

NVD API Key 為選用，但建議新增 GitHub Actions Secret：

```text
NVD_API_KEY
```

沒有 API Key 仍可執行，Collector 會自動降低 NVD request rate。

## GitHub Actions

`V2 Security Intelligence Collector`：

- 每天台北時間 09:00（UTC 01:00）
- 支援手動執行
- PR 會跑 unit tests、真實 Collector 與 JSON validation
- raw snapshots 只保留為 artifact
- main 的 schedule/manual run 會更新 `data/latest.json`

## 下一階段

1. Previous snapshot + Daily Delta
2. Risk scoring
3. Gemini + Google Search enrichment
4. `reports/security_report_latest.md`
5. HTML Email
6. Vendor advisories / TWCERT/CC / dashboard / historical trends
