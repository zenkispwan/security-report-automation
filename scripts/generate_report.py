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

# 讀取 prompt 模板
PROMPT_TEMPLATE = """請幫我收集今日最新的綜合安全威脅情報，執行以下搜尋策略：

【今日搜尋策略】
執行時間：{current_time}
搜尋範圍：過去24小時內發布的安全事件
語言：繁體中文優先，英文補充

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
    current_date_en = now.strftime("%B %d, 2025")
    current_month = now.strftime("%B")
    
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
            max_tokens=16000,
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
