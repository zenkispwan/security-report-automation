#!/usr/bin/env python3
"""
每日資安威脅情報報告生成器（使用 Google Gemini）
固定檔名版本：每次覆蓋 security_report_latest.md
注意：Gemini API 目前不支援即時搜尋，但會使用其訓練資料生成報告
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

**任務說明**
根據你的知識和推理能力，生成一份專業的資安威脅情報報告。

**重要資訊**
- 今天的日期是：{current_date} ({current_date_en})
- 目標時間範圍：{date_range}（最近7天）
- 報告語言：繁體中文

**報告要求**

請生成一份結構化的資安威脅情報報告，涵蓋以下領域：

### 威脅領域分類

🔴 **高風險威脅（3-5則）**
- 零日漏洞和未修補的重大漏洞
- 關鍵基礎設施攻擊
- 大規模資料外洩事件
- 勒索軟體新變種

🟡 **中風險威脅（5-8則）**
- 已知漏洞的新利用手法
- APT 組織活動
- 供應鏈安全事件
- 特定產業威脅

🟢 **低風險/資訊性（2-3則）**
- 安全趨勢和統計
- 法規更新
- 最佳實踐建議

### 重點關注領域

1. **台灣本地威脅**
   - 台灣企業和政府機關面臨的威脅
   - 繁體中文釣魚攻擊
   - 區域性 APT 活動

2. **國際重大事件**
   - Microsoft、Google、Apple 等主要廠商的安全更新
   - 主流軟體和作業系統的 CVE
   - 雲端平台（AWS、Azure、GCP）安全公告

3. **專項技術領域**
   - 🤖 AI/LLM 安全（ChatGPT、Claude、提示注入）
   - 🔐 身份管理（Okta、Azure AD、CyberArk）
   - ⚙️ DevOps（GitHub Actions、Jenkins、CI/CD）
   - 🐳 容器雲原生（Kubernetes、Docker）
   - 📦 供應鏈（npm、PyPI、開源軟體）

4. **攻擊手法趨勢**
   - 新型勒索軟體變種
   - 社交工程技術
   - 零信任架構繞過
   - API 安全漏洞

---

## 📝 輸出格式（完整 Markdown）

# 資安威脅情報日報
**報告時間：{current_date}**
**資料範圍：{date_range}**
**生成模型：Google Gemini**

> ⚠️ **免責聲明**：本報告基於 AI 模型的知識庫生成，建議搭配官方資安資源（CISA、NVD、iThome）進行驗證。

---

## 📊 執行摘要

（3-5句話概述本期最重要的威脅趨勢）

**本期重點：**
1. [最重大威脅 1]
2. [最重大威脅 2]
3. [最重大威脅 3]

---

## 🔴 高風險威脅事件

### 1. [威脅標題] 🔴 CRITICAL

**威脅類型：** [零日漏洞/勒索軟體/資料外洩/供應鏈攻擊]

**時間範圍：** {search_month}

**CVE 編號：** CVE-2025-XXXXX（如適用）

**威脅描述：**
詳細描述威脅的技術細節、攻擊手法、影響範圍...

**影響產品/服務：**
- 產品 A（版本 X.X）
- 產品 B（所有版本）

**風險評估：**
- **CVSS 分數：** 9.8 (Critical)
- **影響範圍：** 全球 / 特定區域 / 特定產業
- **攻擊複雜度：** 低 / 中 / 高
- **是否有修補：** 是 / 否 / 部分

**修補建議：**

🔥 **立即措施（24小時內）：**
1. [具體行動 1]
2. [具體行動 2]

⚡ **短期措施（本週內）：**
1. [具體行動 1]
2. [具體行動 2]

📋 **長期措施：**
1. [具體行動 1]
2. [具體行動 2]

**監控重點：**
- [監控項目 1]
- [監控項目 2]

**參考資源：**
- [官方公告連結]
- [技術分析文章]

---

### 2-5. [其他高風險威脅，格式同上]

---

## 🟡 中風險威脅事件

### 6. [威脅標題] 🟡 HIGH/MEDIUM

[格式類似高風險，但可以更精簡]

---

### 7-13. [其他中風險威脅]

---

## 🟢 低風險/資訊性威脅

### 14. [資訊標題] 🟢 INFO

**類型：** 趨勢分析 / 法規更新 / 統計數據 / 最佳實踐

**內容：**
[簡要說明]

**建議：**
[可選的建議行動]

---

### 15-16. [其他資訊性內容]

---

## 📈 威脅統計分析

### 威脅類型分布
| 威脅類型 | 數量 | 佔比 |
|---------|------|------|
| 漏洞利用 | X | XX% |
| 勒索軟體 | X | XX% |
| 釣魚攻擊 | X | XX% |
| 供應鏈 | X | XX% |
| 其他 | X | XX% |

### 風險等級分布
- 🔴 Critical/High: X則 (XX%)
- 🟡 Medium: X則 (XX%)
- 🟢 Low/Info: X則 (XX%)

### 受影響技術領域 Top 5
1. [領域 1] - X則
2. [領域 2] - X則
3. [領域 3] - X則
4. [領域 4] - X則
5. [領域 5] - X則

### 攻擊向量分析
- 網路攻擊：XX%
- 本地攻擊：XX%
- 社交工程：XX%
- 供應鏈：XX%

---

## 🎯 優先行動建議

### 🔥 立即執行（24小時內）

**高優先級修補：**
1. ✅ [行動 1] - 預計時間：X小時
2. ✅ [行動 2] - 預計時間：X小時
3. ✅ [行動 3] - 預計時間：X小時

**緊急監控：**
- 監控項目 1
- 監控項目 2

---

### ⚡ 本週內完成

**安全更新：**
1. [ ] [更新項目 1]
2. [ ] [更新項目 2]
3. [ ] [更新項目 3]

**配置審查：**
- [ ] 審查項目 1
- [ ] 審查項目 2

---

### 📋 本月內完成

**架構改善：**
1. [ ] [改善項目 1]
2. [ ] [改善項目 2]

**訓練與演練：**
- [ ] 社交工程演練
- [ ] 事件響應演練

---

### 🔍 持續監控重點

**技術監控：**
- 監控異常登入行為
- 檢查未授權的系統變更
- 審查網路流量異常

**威脅情報：**
- 關注 [特定威脅組織] 動態
- 追蹤 [特定漏洞] 利用情況
- 監控 [特定產品] 安全公告

---

## 🏢 特定產業建議

### 💰 金融業
- [特定建議 1]
- [特定建議 2]

### 🏥 醫療業
- [特定建議 1]
- [特定建議 2]

### 🏭 製造業
- [特定建議 1]
- [特定建議 2]

### 💻 科技業
- [特定建議 1]
- [特定建議 2]

---

## 📚 延伸閱讀

### 官方資源
- [CISA 已知利用漏洞目錄](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [NVD 漏洞資料庫](https://nvd.nist.gov/)
- [iThome 資安頻道](https://www.ithome.com.tw/security)

### 本週推薦文章
1. [推薦文章 1]
2. [推薦文章 2]
3. [推薦文章 3]

---

## 📞 聯絡資訊

如發現緊急威脅或需要協助：
- 資安團隊：[聯絡方式]
- CERT/CSIRT：[聯絡方式]

---

**報告結束**

*下次更新時間：{next_update}*

---

**重要提醒：**
- 請立即開始撰寫完整的報告內容
- 使用真實可信的威脅情報
- 確保所有 CVE 編號格式正確
- 提供可操作的具體建議
- 保持專業的語氣和格式"""


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
    next_update = now + timedelta(days=1)
    
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    current_date = now.strftime("%Y年%m月%d日")
    current_date_en = now.strftime("%B %d, %Y")
    current_month = now.strftime("%B %Y")
    
    # 搜尋日期範圍
    date_range = f"{week_ago.strftime('%Y-%m-%d')} 至 {now.strftime('%Y-%m-%d')}"
    search_month = now.strftime("%B %Y")
    next_update_str = next_update.strftime("%Y年%m月%d日")
    
    # 格式化 prompt
    prompt = PROMPT_TEMPLATE.format(
        current_time=current_time,
        current_date=current_date,
        current_date_en=current_date_en,
        current_month=current_month,
        date_range=date_range,
        search_month=search_month,
        next_update=next_update_str
    )
    
    print(f"📊 開始生成資安報告...")
    print(f"⏰ 執行時間：{current_time}")
    print(f"📅 資料範圍：{date_range}")
    print(f"🤖 使用模型：Gemini 1.5 Flash")
    print(f"📁 輸出檔案：{REPORT_FILENAME} (固定檔名，每次覆蓋)")
    print(f"⚠️  注意：使用 AI 推理生成報告（非即時搜尋）")
    
    try:
        # 建立模型（使用 Gemini 1.5 Flash - 快速且便宜）
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash-latest'
        )
        
        print(f"🔍 正在生成報告...")
        print(f"📝 預計需要 30-60 秒...")
        
        # 生成內容
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.7,  # 稍高的溫度以獲得更多創意
                max_output_tokens=8192,
            )
        )
        
        # 取得報告內容
        report_content = response.text
        
        # 儲存報告（固定檔名，每次覆蓋）
        report_path = REPORTS_DIR / REPORT_FILENAME
        
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_content)
        
        print(f"✅ 報告已生成（覆蓋舊檔案）：{report_path}")
        print(f"📏 報告長度：{len(report_content)} 字元")
        
        # 顯示 token 使用情況
        if hasattr(response, 'usage_metadata'):
            print(f"📊 Token 使用情況：")
            print(f"   - Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"   - Response tokens: {response.usage_metadata.candidates_token_count}")
            print(f"   - Total tokens: {response.usage_metadata.total_token_count}")
            
            # 估算成本（Gemini 1.5 Flash 是免費的）
            print(f"💰 成本：免費（Gemini 1.5 Flash）")
        
        return str(report_path)
        
    except Exception as e:
        print(f"❌ 錯誤：{e}")
        print(f"💡 請確認：")
        print(f"   1. GEMINI_API_KEY 是否正確")
        print(f"   2. API Key 是否有效且未過期")
        print(f"   3. 是否已安裝 google-generativeai 套件")
        print(f"   4. 網路連線是否正常")
        sys.exit(1)


if __name__ == "__main__":
    report_path = generate_report()
    print(f"\n🎉 報告生成完成！")
    print(f"📁 檔案位置：{report_path}")
    print(f"📝 說明：每次執行都會覆蓋此檔案，保持最新版本")
    print(f"\n⚠️  重要提醒：")
    print(f"   - 本報告基於 AI 模型推理生成")
    print(f"   - 建議搭配官方資安資源進行驗證")
    print(f"   - 如需即時威脅情報，請參考 CISA、NVD 等官方來源")
