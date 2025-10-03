# 📊 每日資安威脅情報自動化報告系統

這是一個使用 GitHub Actions 和 Claude API 自動生成每日資安威脅情報報告的系統。

## ✨ 功能特色

- 🤖 **自動化收集**：每天自動搜尋最新資安威脅資訊
- 📧 **郵件通知**：自動發送 HTML 格式報告到指定信箱
- 🔍 **多來源整合**：整合台灣本地與國際資安新聞
- 📑 **結構化報告**：包含風險等級、CVE 資訊、修補建議
- 💾 **歷史保存**：自動保存 30 天歷史報告
- 🎯 **可客製化**：可調整搜尋關鍵字和報告格式

## 📁 專案結構

```
security-report-automation/
├── .github/
│   └── workflows/
│       └── daily-report.yml          # GitHub Actions 工作流程
├── scripts/
│   ├── generate_report.py            # 報告生成腳本
│   └── send_email.py                 # 郵件發送腳本
├── reports/                          # 報告儲存目錄（自動建立）
├── requirements.txt                  # Python 依賴套件
└── README.md                         # 說明文件
```

## 🚀 快速開始

### 1. Fork 或 Clone 此專案

```bash
git clone https://github.com/YOUR_USERNAME/security-report-automation.git
cd security-report-automation
```

### 2. 設定 GitHub Secrets

在 GitHub Repository 中設定以下 Secrets：

| Secret 名稱 | 說明 | 如何取得 |
|------------|------|---------|
| `CLAUDE_API_KEY` | Claude API 金鑰 | [Anthropic Console](https://console.anthropic.com/) |
| `EMAIL_SENDER` | Gmail 發送帳號 | 您的 Gmail 地址 |
| `EMAIL_PASSWORD` | Gmail 應用程式密碼 | [Google 應用程式密碼](https://myaccount.google.com/apppasswords) |
| `EMAIL_RECIPIENT` | 接收報告的郵箱 | 任何有效的郵箱地址 |

**設定步驟：**
1. 進入 Repository → `Settings`
2. 左側選單 → `Secrets and variables` → `Actions`
3. 點選 `New repository secret`
4. 依序新增上述四個 secrets

### 3. 取得 Claude API 金鑰

1. 前往 [Anthropic Console](https://console.anthropic.com/)
2. 註冊或登入
3. 點選 `API Keys` → `Create Key`
4. 複製金鑰（格式：`sk-ant-...`）
5. 貼到 GitHub Secret `CLAUDE_API_KEY`

**費用說明：**
- 按使用量計費
- 每次報告約 $0.50-1.00 USD
- 建議充值 $10-20 USD 即可使用數週

### 4. 設定 Gmail 應用程式密碼

1. 前往 [Google 帳戶](https://myaccount.google.com/)
2. 左側 → `安全性`
3. 確認已啟用 `兩步驟驗證`
4. 搜尋 `應用程式密碼`
5. 選擇 `郵件` 和 `其他裝置`
6. 生成 16 字元密碼
7. 複製並貼到 GitHub Secret `EMAIL_PASSWORD`

**⚠️ 注意：**
- 必須使用「應用程式密碼」，不是 Gmail 一般密碼
- 密碼格式：`xxxx xxxx xxxx xxxx`（16 字元，有空格）
- 貼到 GitHub Secret 時可以保留或移除空格

## ⏰ 執行排程

預設每天**台北時間早上 8:00** 自動執行（UTC 0:00）

### 修改執行時間

編輯 `.github/workflows/daily-report.yml`：

```yaml
on:
  schedule:
    # 台北時間 8:00 = UTC 0:00
    - cron: '0 0 * * *'
    
    # 其他範例：
    # 台北時間 9:00 = UTC 1:00
    # - cron: '0 1 * * *'
    
    # 台北時間 20:00 = UTC 12:00
    # - cron: '0 12 * * *'
```

**Cron 格式說明：**
```
* * * * *
│ │ │ │ │
│ │ │ │ └─── 星期幾 (0-6, 0=週日)
│ │ │ └───── 月份 (1-12)
│ │ └─────── 日期 (1-31)
│ └───────── 小時 (0-23, UTC 時間)
└─────────── 分鐘 (0-59)
```

## 🧪 手動測試

### 在 GitHub 上手動觸發

1. 進入 Repository → `Actions`
2. 左側選擇 `每日資安威脅情報報告`
3. 點選右上角 `Run workflow`
4. 選擇 `Branch: main`
5. 點選 `Run workflow`

### 本地測試

```bash
# 1. 安裝依賴
pip install -r requirements.txt

# 2. 設定環境變數
export CLAUDE_API_KEY="sk-ant-..."
export EMAIL_SENDER="your-email@gmail.com"
export EMAIL_PASSWORD="your-app-password"
export EMAIL_RECIPIENT="recipient@example.com"

# 3. 生成報告
python scripts/generate_report.py

# 4. 發送郵件
python scripts/send_email.py
```

## 🎨 客製化設定

### 調整搜尋關鍵字

編輯 `scripts/generate_report.py` 中的 `PROMPT_TEMPLATE`：

```python
# 新增您關注的特定關鍵字
【客製化搜尋】
- "您公司名稱 + 資安事件"
- "您使用的特定產品 + vulnerability"
- "您關注的特定威脅組織"
```

### 調整報告格式

在 `PROMPT_TEMPLATE` 中修改輸出要求：

```python
【輸出要求】
請將最終報告以 markdown 格式輸出，包含：
1. 您想要的章節...
2. 您想要的格式...
```

### 調整郵件樣式

編輯 `scripts/send_email.py` 中的 CSS 樣式：

```python
html_template = """
    <style>
        /* 在這裡自訂您的 CSS 樣式 */
        body { ... }
    </style>
"""
```

### 多個收件者

修改 `scripts/send_email.py`：

```python
# 支援多個收件者
recipient_emails = os.getenv("EMAIL_RECIPIENT").split(",")
msg['To'] = ", ".join(recipient_emails)
```

然後在 GitHub Secret 中設定：
```
EMAIL_RECIPIENT = email1@example.com,email2@example.com,email3@example.com
```

## 📊 報告範例

報告將包含以下內容：

### 🔴 高風險威脅（緊急處理）
- 零日漏洞攻擊
- 關鍵基礎設施威脅
- 大規模資料外洩

### 🟡 中風險威脅（重要關注）
- 已修補的重要漏洞
- APT 組織活動
- 供應鏈攻擊

### 🟢 低風險/資訊性（持續關注）
- 產業趨勢
- 法規更新
- 統計數據

### 每個威脅包含：
- ✅ 發布時間與 CVE 編號
- ✅ 威脅摘要與攻擊手法
- ✅ 影響範圍與產品
- ✅ 風險等級評估
- ✅ 具體修補建議
- ✅ 監控重點
- ✅ 可驗證的來源連結

## 🔍 檢視執行狀態

### 查看工作流程執行記錄

1. 進入 Repository → `Actions`
2. 點選執行記錄查看詳細日誌
3. 綠色勾勾 ✅ = 成功
4. 紅色叉叉 ❌ = 失敗（點選查看錯誤）

### 下載歷史報告

1. 進入 `Actions` → 選擇執行記錄
2. 頁面底部 `Artifacts` 區塊
3. 下載 `security-report-X` 壓縮檔
4. 解壓縮即可看到 Markdown 報告

## ❌ 常見問題排解

### 1. 郵件發送失敗

**錯誤訊息：** `SMTPAuthenticationError`

**解決方法：**
- ✅ 確認已啟用 Gmail 兩步驟驗證
- ✅ 使用「應用程式密碼」而非一般密碼
- ✅ 應用程式密碼複製正確（16 字元）
- ✅ 檢查 `EMAIL_SENDER` 和 `EMAIL_PASSWORD` 是否設定正確

### 2. Claude API 錯誤

**錯誤訊息：** `APIError: authentication_error`

**解決方法：**
- ✅ 確認 API 金鑰格式正確（`sk-ant-...`）
- ✅ 檢查 API 金鑰是否有效（未過期）
- ✅ 確認 Anthropic 帳戶有足夠餘額
- ✅ 訪問 [Anthropic Console](https://console.anthropic.com/) 檢查狀態

### 3. 找不到報告檔案

**錯誤訊息：** `找不到任何報告檔案`

**解決方法：**
- ✅ 確認 `generate_report.py` 已成功執行
- ✅ 檢查 `reports/` 目錄是否存在
- ✅ 查看 GitHub Actions 日誌確認生成步驟

### 4. GitHub Actions 未執行

**可能原因：**
- ✅ Repository 設定為 Private 且未啟用 Actions
- ✅ Workflow 檔案路徑錯誤
- ✅ Cron 語法錯誤

**解決方法：**
1. 進入 `Settings` → `Actions` → `General`
2. 確認 `Allow all actions and reusable workflows` 已勾選
3. 檢查 `.github/workflows/daily-report.yml` 路徑正確

### 5. API 使用量過高

**解決方法：**
- 調整搜尋範圍（減少搜尋次數）
- 使用較小的 `max_tokens` 限制
- 減少報告生成頻率

## 💰 成本估算

### Claude API 費用

| 項目 | 估算 |
|-----|------|
| 每次報告 Input tokens | ~10,000 tokens |
| 每次報告 Output tokens | ~20,000 tokens |
| 單次報告成本 | $0.50-1.00 USD |
| 每月成本（每天一次） | $15-30 USD |

**節省成本建議：**
- 減少搜尋領域數量
- 縮短報告長度
- 使用 Claude Haiku（較便宜但品質略低）

### GitHub Actions 費用

- ✅ **完全免費**（Public Repository）
- ✅ **每月 2000 分鐘免費額度**（Private Repository）
- 本專案每次執行約 3-5 分鐘
- 每月 30 次執行 = 90-150 分鐘（遠低於免費額度）

### Gmail

- ✅ **完全免費**

### 總成本

**每月約 $15-30 USD**（主要是 Claude API）

## 🔐 安全建議

### ✅ 務必執行

- 🔒 使用 Private Repository 儲存此專案
- 🔒 絕不將 API 金鑰直接寫在程式碼中
- 🔒 定期輪換 Gmail 應用程式密碼
- 🔒 監控 Anthropic 帳戶使用量

### ⚠️ 注意事項

- 不要將 `.env` 檔案提交到 Git
- 不要在公開場合分享報告（可能含敏感資訊）
- 定期檢查 GitHub Actions 執行日誌
- 留意異常的 API 使用量

## 📈 進階功能

### 1. 整合 Slack 通知

新增 `scripts/send_slack.py`：

```python
import requests
import os

def send_to_slack(report_summary):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    
    payload = {
        "text": "📊 今日資安報告已生成",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": report_summary
                }
            }
        ]
    }
    
    requests.post(webhook_url, json=payload)
```

在 GitHub Secrets 新增 `SLACK_WEBHOOK_URL`

### 2. 儲存到 Notion

使用 Notion API 將報告儲存到 Notion 資料庫：

```python
import requests
import os

def save_to_notion(report_content):
    notion_token = os.getenv("NOTION_TOKEN")
    database_id = os.getenv("NOTION_DATABASE_ID")
    
    # Notion API 實作...
```

### 3. 產生 PDF 報告

安裝額外套件：

```bash
pip install markdown pdfkit
```

修改 `send_email.py` 加入 PDF 轉換功能

### 4. 多語言支援

修改 prompt 模板支援英文報告：

```python
LANGUAGE = os.getenv("REPORT_LANGUAGE", "zh-TW")  # zh-TW 或 en

if LANGUAGE == "en":
    prompt = ENGLISH_PROMPT_TEMPLATE
else:
    prompt = CHINESE_PROMPT_TEMPLATE
```

### 5. 整合內部威脅情報

連接您公司的 SIEM、EDR 系統：

```python
# 從內部系統取得威脅資料
internal_threats = fetch_from_siem()

# 合併到報告中
prompt += f"\n\n【內部威脅資料】\n{internal_threats}"
```

## 🤝 貢獻

歡迎提交 Issue 或 Pull Request！

### 開發流程

1. Fork 此專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 📄 授權

MIT License

## 🙏 致謝

- [Anthropic Claude API](https://www.anthropic.com/)
- [GitHub Actions](https://github.com/features/actions)
- [iThome 資安頻道](https://www.ithome.com.tw/security)

## 📞 支援

如有問題或建議，請：
- 開啟 [GitHub Issue](https://github.com/YOUR_USERNAME/security-report-automation/issues)
- 查看 [討論區](https://github.com/YOUR_USERNAME/security-report-automation/discussions)

## 🎯 路線圖

- [ ] 支援多種通知管道（Telegram、Discord）
- [ ] Web Dashboard 視覺化介面
- [ ] 自訂威脅優先級規則
- [ ] 整合更多威脅情報來源
- [ ] AI 威脅趨勢預測

---

**⭐ 如果這個專案對您有幫助，請給個 Star！**
