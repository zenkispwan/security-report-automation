# 📊 每日資安威脅情報自動化報告系統（Gemini 版本）

使用 GitHub Actions 和 Google Gemini API 自動生成每日資安威脅情報報告。

## ✨ 功能特色

- 🤖 **自動化收集**：使用 Google Search 搜尋最新資安威脅
- 🆓 **完全免費**：Gemini API 免費額度充足
- 📧 **郵件通知**：自動發送 HTML 格式報告
- 📁 **固定檔名**：報告固定為 `security_report_latest.md`，每次覆蓋
- 🔍 **多來源整合**：台灣本地與國際資安新聞
- 📅 **最近7天資料**：自動搜尋最近一週的威脅情報

## 🚀 快速開始

### 1. Fork 此專案

### 2. 取得 Gemini API Key

1. 前往 https://aistudio.google.com/apikey
2. 點擊「Create API key」
3. 複製 API Key

### 3. 設定 GitHub Secret

在 Repository Settings → Secrets and variables → Actions：

| Secret 名稱 | 說明 |
|------------|------|
| `GEMINI_API_KEY` | Google Gemini API Key |
| `EMAIL_SENDER` | Gmail 發送帳號（選用） |
| `EMAIL_PASSWORD` | Gmail 應用程式密碼（選用） |
| `EMAIL_RECIPIENT` | 接收報告郵箱（選用） |

### 4. 手動測試

1. 前往 Actions → 📊 每日資安威脅情報報告（Gemini）
2. 點擊「Run workflow」
3. 等待執行完成
4. 查看 `reports/security_report_latest.md`

## ⏰ 執行排程

預設每天台北時間早上 9:00 自動執行

## 💰 成本

**完全免費！**
- Gemini API: 免費額度充足
- GitHub Actions: 免費（Public Repo）或 2000分鐘/月（Private Repo）

## 📝 報告位置

固定位置：`reports/security_report_latest.md`

每次執行會覆蓋此檔案，保持最新版本。
