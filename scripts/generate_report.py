#!/usr/bin/env python3
"""
每日資安威脅情報報告生成器
使用 Claude API 自動收集和分析最新資安威脅
"""

import os
import sys
from datetime import datetime
from pathlib import Path
import anthropic

# 確保 reports 目錄存在
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Prompt 模板
PROMPT_TEMPLATE = """你是專業的資安威脅情報分析師。

請執行以下任務：收集並分析**今天與最近24-48小時**發布的最新資安威脅情報。

【任務要求】
- 使用 web_search 工具搜尋最新資訊
- 直接開始搜尋，不要詢問或確認
- 報告語言：繁體中文為主

【搜尋策略】

**第一階段：台灣本地資安新聞**
搜尋關鍵字：
- "iThome 資安 today" "iThome Security 最新"
- "台灣 資安事件" "台灣 cybersecurity"
- "台灣 資料外洩" "台灣 漏洞"

**第二階段：國際重大事件**
搜尋關鍵字：
- "security vulnerability today" "CVE today"
- "data breach latest" "security advisory latest"
- "cybersecurity news today" "zero-day exploit"

**第三階段：專項領域搜尋**

🤖 AI安全：
- "ChatGPT security issue" "Claude vulnerability"
- "LLM security" "AI model attack"
- "prompt injection" "jailbreak attack"

🔐 身份與存取管理：
- "Okta breach" "CyberArk vulnerability"
- "Azure AD security" "identity management attack"

⚙️ DevOps安全：
- "GitHub Actions attack" "Jenkins vulnerability"
- "Docker security" "CI/CD breach"

🐳 容器與雲原生：
- "Kubernetes CVE" "container security"
- "AWS security advisory" "Azure vulnerability"

**第四階段：供應鏈威脅**
- "supply chain attack" "APT campaign"
- "zero-day in the wild" "ransomware"

【輸出格式要求】

請直接輸出 markdown 格式的完整報告，包含：

## 📊 執行摘要
（3大最緊急威脅）

## 🔴 高風險威脅事件
（3-5則，含CVE、影響範圍、修補建議）

## 🟡 中風險威脅事件  
（5-8則）

## 🟢 低風險/資訊性威脅
（2-3則）

## 📈 威脅統計分析

## 🎯 優先行動建議

每個威脅事件必須包含：
- 威脅標題與風險等級（🔴/🟡/🟢）
- 發布時間與CVE編號
- 威脅摘要
- 影響產品/服務
- 來源鏈結（可驗證）
- 風險評估
- 具體修補建議

**立即開始搜尋並生成報告，不需要任何說明或確認。**"""

【第一階段：台灣本地安全新聞】
請先搜尋 "iThome 資安 今日" 和 "台灣 資安事件 {current_date}"
重點關注：
- iThome Security頻道最新報導
- 台灣企業遭受的安全攻擊
- 政府資安政策更新
- 本地廠商安全產品動態

【第二階段：國際重大安全事件】
搜尋關鍵字組合：
- "security vulnerability {current_date_en}"
- "CVE 2025 today security advisory"
- "cybersecurity incident latest news"
- "data breach {current_month} 2025"

【第三階段：各領域專項搜尋】
🤖 **AI安全威脅**：
- "OpenAI ChatGPT security issue today"
- "Claude API vulnerability 2025"
- "AI model attack {current_month} 2025"
- "LLM jailbreak prompt injection"

🔐 **身份與存取管理(IAM)**：
- "CyberArk security advisory {current_month} 2025"
- "Okta vulnerability latest"
- "Azure AD Entra ID security issue"
- "privileged access management breach"

⚙️ **DevOps安全**：
- "Jenkins security vulnerability today"
- "GitHub Actions supply chain attack"
- "Docker security advisory 2025"
- "CI/CD pipeline security breach"

🐳 **容器與雲原生安全**：
- "Kubernetes CVE {current_month} 2025"
- "container security vulnerability"
- "AWS EKS Azure AKS GKE security"
- "Istio service mesh security issue"

【第四階段：供應鏈與跨域威脅】
- "supply chain attack {current_month} 2025"
- "zero-day exploit in the wild"
- "APT group new campaign 2025"
- "critical infrastructure cyberattack"

【輸出要求】
請將最終報告以 markdown 格式輸出，包含：

1. 執行摘要（本日最緊急的 3 大威脅）
2. 🔴 高風險威脅事件（緊急處理）- 3-5則
3. 🟡 中風險威脅事件（重要關注）- 5-8則
4. 🟢 低風險/資訊性威脅（持續關注）- 2-3則
5. 威脅統計分析
6. 優先行動建議
7. 特定產業建議

每個威脅事件請包含：
- 發布時間
- 威脅摘要（含攻擊手法）
- CVE編號（如有）
- 影響產品/服務
- 來源鏈結（主要來源、官方回應、技術詳情）
- 風險評估（影響範圍、風險等級、是否有修補程式）
- 建議行動（立即措施、修補建議、監控重點）

請開始執行搜尋，並按風險等級排序輸出結果。
"""


def generate_report():
    """使用 Claude API 生成資安報告"""
    
    # 取得 API 金鑰
    api_key = os.getenv("CLAUDE_API_KEY")
    if not api_key:
        print("❌ 錯誤：未找到 CLAUDE_API_KEY 環境變數")
        sys.exit(1)
    
    # 初始化 Claude 客戶端
    client = anthropic.Anthropic(api_key=api_key)
    
    # 準備時間變數
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    current_date = now.strftime("%Y年%m月%d日")
    current_date_en = now.strftime("%B %d, %Y")  # 修正：使用 %Y 而非寫死 2025
    current_month = now.strftime("%B %Y")  # 加入年份避免混淆
    
    # 格式化 prompt
    prompt = PROMPT_TEMPLATE.format(
        current_time=current_time,
        current_date=current_date,
        current_date_en=current_date_en,
        current_month=current_month
    )
    
    print(f"📊 開始生成報告...")
    print(f"⏰ 執行時間：{current_time}")
    
    try:
        # 呼叫 Claude API
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=64000,
            temperature=0.3,  # 較低的溫度以獲得更一致的輸出
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # 取得報告內容
        report_content = message.content[0].text
        
        # 儲存報告
        report_filename = f"security_report_{now.strftime('%Y%m%d')}.md"
        report_path = REPORTS_DIR / report_filename
        
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"# 每日資安威脅情報報告\n")
            f.write(f"**生成時間：{current_time}**\n\n")
            f.write(report_content)
        
        print(f"✅ 報告已生成：{report_path}")
        print(f"📏 報告長度：{len(report_content)} 字元")
        
        # 顯示 API 使用情況
        if hasattr(message, 'usage'):
            print(f"📊 API 使用：")
            print(f"   - Input tokens: {message.usage.input_tokens}")
            print(f"   - Output tokens: {message.usage.output_tokens}")
        
        return str(report_path)
        
    except anthropic.APIError as e:
        print(f"❌ API 錯誤：{e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 未預期的錯誤：{e}")
        sys.exit(1)


if __name__ == "__main__":
    report_path = generate_report()
    print(f"\n🎉 報告生成完成！")
    print(f"📁 檔案位置：{report_path}")
