# Cloudflare Workers Static Assets 部署

本專案的 Web Report 採用 **Cloudflare Workers Static Assets**。第一版只有靜態資產，不需要 Worker script、R2、D1 或 AI binding。

## 架構

```text
GitHub Actions
  Collector -> Delta / Risk / Intelligence -> Report
                                      |
                                      v
                           main report commit
                                      |
                                      v
                     Cloudflare Workers Builds
                                      |
                 npm run build:web -> _site/
                                      |
                        npx wrangler deploy
                                      |
                                      v
                         Workers Static Assets
```

`wrangler.jsonc` 是 Cloudflare 部署設定的 source of truth：

```json
{
  "name": "security-report-automation",
  "compatibility_date": "2026-09-10",
  "assets": {
    "directory": "./_site"
  }
}
```

沒有 `main`，因此目前不部署任何 Worker JavaScript/Python runtime code。

## 第一次在 Cloudflare 建立專案

1. Cloudflare Dashboard -> **Workers & Pages** -> **Create application**。
2. 選 **Import a repository**，連接 GitHub。
3. 選擇 `zenkispwan/security-report-automation`。
4. Worker / Project name 使用 `security-report-automation`。
5. Production branch 設為 `main`。
6. Root directory 使用 repository root。
7. Build command：

   ```bash
   npm run build:web
   ```

8. Deploy command：

   ```bash
   npx wrangler deploy
   ```

9. 第一版網站不需要設定任何 Cloudflare secret 或 binding。
10. Deploy 完成後先用 `workers.dev` 網址驗證，再視需要綁定自訂網域。

Cloudflare Workers Builds 的 build image 同時提供 Node.js 與 Python；`package.json` 只負責固定 Wrangler 依賴，網站 build 本身由 Python standard library 完成。

## Build watch paths

為避免 Collector 的 `data/**` commit 在 Report 還沒完成前先部署一版「新 data + 舊 metadata」，建議在 Cloudflare Worker：

`Settings -> Build -> Build watch paths`

Production include paths設定為：

```text
reports/security_report_metadata.json
reports/security_report_latest.md
web/*
scripts/build_web_report.py
scripts/validate_web_report.py
wrangler.jsonc
package.json
```

這樣 Collector 更新 compact data 時不直接部署；Collector 成功後 Report workflow 產生 report commit，Cloudflare 才會重新 build，而 build 時會把同一個最新 `main` 的 `data/intelligence.json`、`data/delta.json` 與 report metadata 一起複製到 `_site`。

## Build output

```text
_site/
  index.html
  styles.css
  app.js
  _headers
  data/
    intelligence.json
    delta.json
    report_metadata.json
  security_report_latest.md
```

`_headers` 提供 CSP、Permissions Policy、Referrer Policy 與 cache policy。資料 JSON 與 report HTML shell 不依賴第三方 JavaScript/CDN。

## 本機 / CI 驗證

```bash
npm install
npm run build:web
```

或只用 Python：

```bash
python3 scripts/build_web_report.py
python3 scripts/validate_web_report.py
```

PR CI 會執行相同的 Web Report smoke test，確認 build output 中的 JSON 與 repository verified inputs SHA-256 一致，並檢查沒有外部 executable/style dependency。

## 後續擴充

等靜態網站穩定後，可在同一個 Cloudflare 專案逐步加入：

- R2：保存 raw / full snapshot / 歷史報告
- Workers AI：作為可替換的 Intelligence provider
- AI Gateway：統一 provider observability / quota / fallback
- D1：歷史趨勢與查詢索引
- Worker API：歷史日期、搜尋或 authenticated endpoints
- Cloudflare Access：若未來需要限制報告讀取權限

這些都不是第一版網站上線的必要條件。
