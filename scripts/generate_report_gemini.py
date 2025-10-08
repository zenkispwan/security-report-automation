#!/usr/bin/env python3
"""
每日資安威脅情報報告生成器（使用 Google Gemini）
固定檔名版本：每次覆蓋 security_report_latest.md
"""

import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
import google.generativeai as genai

# 確保 reports 目錄存在
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

# 固定的報告檔名
REPORT_FILENAME = "security_report_latest.md"

# Prompt 模板
PROMPT_TEMPLATE = """你是專業的資安威脅情報分析師。

**❗ 重要資訊 ❗**
- 今天的日期是：{current_date} ({current_date_en})
- 你有 Google Search 功能，**必須使用搜尋**獲取最新資訊
- **搜尋範圍：{date_range}**（最近7天內的資料）
- 不要使用舊知識，必須透過 Google 搜尋取得當前威脅情報
- 每個搜尋關鍵字都要包含時間限制
- 報告語言：繁體中文

## 🔍 搜尋策略（執行 12-15 次搜尋）

### 第一階段：台灣本地資安新聞（2次）
1. "iThome 資安 {search_month}"
2. "台灣 資安事件 {search_month}"

### 第二階段：國際重大事件（4次）
3. "CVE {search_month}"
4. "security vulnerability {search_month}"
5. "data breach {search_month}"
6. "zero-day exploit {search_month}"

### 第三階段：專項領域搜尋（8次）

🤖 **AI安全（2次）：**
7. "ChatGPT Claude security {search_month}"
8. "LLM vulnerability {search_month}"

🔐 **身份管理（1次）：**
9. "Okta Azure AD security {search_month}"

⚙️ **DevOps安全（2次）：**
10. "GitHub Actions Jenkins vulnerability {search_month}"
11. "CI/CD security breach {search_month}"

🐳 **容器雲原生（2次）：**
12. "Kubernetes CVE {search_month}"
13. "Docker AWS security {search_month}"

📦 **供應鏈（1次）：**
14. "supply chain attack ransomware {search_month}"

---

## 📝 輸出格式

# 資安威脅情報日報
**報告時間：{current_date}**
**資料來源：Google Search（{date_range}）**

## 📊 執行摘要
（基於搜尋結果的3大最緊急威脅，如果沒有找到近期資料請說明）

## 🔴 高風險威脅事件（3-5則）
每則必須包含：
- **威脅標題** 🔴 CRITICAL/HIGH
- **發布時間**（必須是 {search_month} 的日期）
- **CVE編號**（如有）
- **威脅摘要**（含攻擊手法）
- **影響產品/服務**
- **來源連結**（必須是實際可驗證的 URL）
- **風險評估**（影響範圍、CVSS分數）
- **修補建議**（立即措施、長期建議）

## 🟡 中風險威脅事件（5-8則）
（格式同上）

## 🟢 低風險/資訊性威脅（2-3則）

## 📈 威脅統計分析
- 威脅類型分布
- 風險等級分布
- 受影響技術領域

## 🎯 優先行動建議
### 🔥 立即執行（24小時內）
### ⚡ 本週內完成
### 📋 持續監控

---

**重要規則：**
1. ✅ 所有資訊必須來自 Google Search 結果
2. ✅ 每個威脅必須附上實際來源 URL
3. ✅ 發布時間必須是 {date_range}
4. ✅ 如果搜尋沒找到足夠資料，請明確說明
5. ✅ 優先使用官方來源

**現在請開始使用 Google Search 搜尋並生成報告。**"""


def generate_report():
    """使用 Google Gemini API 生成資安報告"""
    
    # 取得 API 金鑰
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ 錯誤：未找到 GEMINI_API_KEY 環境變數")
        print("💡 請到 https://aistudio.google.com/apikey 取得免費 API Key")
        sys.exit(1)
    
    # 設定 Gemini API
    genai.configure(api_key=api_key)
    
    # 準備時間變數
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    current_date = now.strftime("%Y年%m月%d日")
    current_date_en = now.strftime("%B %d, %Y")
    current_month = now.strftime("%B %Y")
    
    # 搜尋日期範圍
    date_range = f"{week_ago.strftime('%Y-%m-%d')} 至 {now.strftime('%Y-%m-%d')}"
    search_month = now.strftime("%B %Y")
    
    # 格式化 prompt
    prompt = PROMPT_TEMPLATE.format(
        current_time=current_time,
        current_date=current_date,
        current_date_en=current_date_en,
        current_month=current_month,
        date_range=date_range,
        search_month=search_month
    )
    
    print(f"📊 開始生成資安報告...")
    print(f"⏰ 執行時間：{current_time}")
    print(f"📅 資料範圍：{date_range}")
    print(f"🤖 使用模型：Gemini 2.0 Flash (含 Google Search)")
    print(f"📁 輸出檔案：{REPORT_FILENAME} (固定檔名，每次覆蓋)")
    
    try:
        # 建立模型（啟用 Google Search grounding）
        # 修正：使用新的 API 語法
        model = genai.GenerativeModel(
            model_name='gemini-2.0-flash-exp',
            tools=[{'google_search': {}}]  # 正確的語法
        )
        
        print(f"🔍 正在使用 Google Search 搜尋最新資訊...")
        print(f"📝 正在分析並生成報告（預計 1-2 分鐘）...")
        
        # 生成內容
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.3,
                max_output_tokens=8192,  # 限制輸出長度以節省 token
            )
        )
        
        # 取得報告內容
        report_content = response.text
        
        # 儲存報告（固定檔名，每次覆蓋）
        report_path = REPORTS_DIR / REPORT_FILENAME
        
        # 如果檔案已存在，會直接覆蓋
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"# 每日資安威脅情報報告\n")
            f.write(f"**生成時間：{current_time}**\n")
            f.write(f"**資料範圍：{date_range}**\n")
            f.write(f"**生成模型：Google Gemini 2.0 Flash (with Google Search)**\n\n")
            f.write(report_content)
        
        print(f"✅ 報告已生成（覆蓋舊檔案）：{report_path}")
        print(f"📏 報告長度：{len(report_content)} 字元")
        
        # 顯示 token 使用情況
        if hasattr(response, 'usage_metadata'):
            print(f"📊 Token 使用情況：")
            print(f"   - Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"   - Response tokens: {response.usage_metadata.candidates_token_count}")
            print(f"   - Total tokens: {response.usage_metadata.total_token_count}")
        
        # 顯示搜尋來源數量
        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'grounding_metadata') and candidate.grounding_metadata:
                if hasattr(candidate.grounding_metadata, 'grounding_chunks'):
                    search_count = len(candidate.grounding_metadata.grounding_chunks)
                    print(f"🔍 搜尋引用來源數量：{search_count}")
        
        return str(report_path)
        
    except Exception as e:
        print(f"❌ 錯誤：{e}")
        print(f"💡 請確認：")
        print(f"   1. GEMINI_API_KEY 是否正確")
        print(f"   2. API Key 是否有效且未過期")
        print(f"   3. 是否已安裝 google-generativeai 套件")
        print(f"   4. 網路連線是否正常")
        print(f"   5. 使用的是最新版本的 google-generativeai")
        sys.exit(1)


if __name__ == "__main__":
    report_path = generate_report()
    print(f"\n🎉 報告生成完成！")
    print(f"📁 檔案位置：{report_path}")
    print(f"📝 說明：每次執行都會覆蓋此檔案，保持最新版本")
    print(f"\n💡 優點：")
    print(f"   ✅ 固定檔案路徑，方便自動化讀取")
    print(f"   ✅ 不會累積大量歷史檔案")
    print(f"   ✅ 永遠是最新的報告")
