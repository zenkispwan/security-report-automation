#!/usr/bin/env python3
"""
每日資安威脅情報報告生成器（使用 Google Gemini）
簡化版本 - 確保可用
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


def generate_report():
    """使用 Google Gemini API 生成資安報告"""
    
    # 取得 API 金鑰
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ 錯誤：未找到 GEMINI_API_KEY 環境變數")
        sys.exit(1)
    
    # 設定 Gemini API
    genai.configure(api_key=api_key)
    
    # 準備時間變數
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    current_date = now.strftime("%Y年%m月%d日")
    date_range = f"{week_ago.strftime('%Y-%m-%d')} 至 {now.strftime('%Y-%m-%d')}"
    month_year = now.strftime("%B %Y")
    
    # 建立 Prompt
    prompt = f"""你是專業的資安威脅情報分析師。請生成一份詳細的資安威脅情報報告。

**報告資訊**
- 日期：{current_date}
- 時間範圍：{date_range}
- 語言：繁體中文

請生成包含以下章節的完整報告：

# 資安威脅情報日報
**報告時間：{current_date}**
**資料範圍：{date_range}**

> ⚠️ 本報告基於 AI 模型知識生成，建議搭配官方資安資源驗證

## 📊 執行摘要
（概述本期3大重要威脅趨勢）

## 🔴 高風險威脅事件（3-5則）

針對每個威脅，請包含：
- 威脅標題和等級
- CVE 編號（如果適用）
- 威脅描述
- 影響產品/服務
- 風險評估（CVSS 分數、影響範圍）
- 修補建議（立即措施、短期措施、長期措施）

重點關注：
- Windows、Linux、macOS 作業系統漏洞
- 主流瀏覽器（Chrome、Firefox、Edge）安全更新
- Microsoft 365、Google Workspace 安全問題
- AWS、Azure、GCP 雲端平台安全公告
- 勒索軟體新變種

## 🟡 中風險威脅事件（5-8則）

關注領域：
- 🤖 AI/LLM 安全（ChatGPT、Claude、提示注入）
- 🔐 身份管理（Okta、Azure AD、CyberArk）
- ⚙️ DevOps（GitHub Actions、Jenkins、CI/CD）
- 🐳 容器（Kubernetes、Docker）
- 📦 供應鏈（npm、PyPI、開源軟體）
- 🇹🇼 台灣本地威脅

## 🟢 低風險/資訊性威脅（2-3則）

包含：
- 安全趨勢和統計
- 法規更新
- 最佳實踐建議

## 📈 威脅統計分析

提供以下統計：
- 威脅類型分布（表格）
- 風險等級分布
- 受影響技術領域 Top 5
- 攻擊向量分析

## 🎯 優先行動建議

### 🔥 立即執行（24小時內）
列出 3-5 項高優先級行動

### ⚡ 本週內完成
列出 3-5 項安全更新和審查

### 📋 持續監控重點
列出需要持續關注的項目

## 🏢 特定產業建議

針對以下產業提供建議：
- 💰 金融業
- 🏥 醫療業  
- 🏭 製造業
- 💻 科技業

請立即開始生成完整、詳細、專業的報告內容。"""
    
    print(f"📊 開始生成資安報告...")
    print(f"⏰ 執行時間：{current_time}")
    print(f"📅 資料範圍：{date_range}")
    print(f"🤖 使用模型：Gemini 1.5 Flash")
    print(f"📁 輸出檔案：{REPORT_FILENAME}")
    
    try:
        # 列出可用模型（用於除錯）
        print(f"🔍 檢查可用模型...")
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
        
        print(f"✅ 找到 {len(available_models)} 個可用模型")
        
        # 嘗試不同的模型名稱
        model_names_to_try = [
            'gemini-1.5-flash',
            'gemini-1.5-pro',
            'gemini-pro',
            'models/gemini-1.5-flash',
            'models/gemini-pro'
        ]
        
        model = None
        used_model_name = None
        
        for model_name in model_names_to_try:
            try:
                print(f"🔄 嘗試模型：{model_name}")
                model = genai.GenerativeModel(model_name=model_name)
                # 測試模型是否可用
                test_response = model.generate_content("Hello")
                used_model_name = model_name
                print(f"✅ 成功使用模型：{model_name}")
                break
            except Exception as e:
                print(f"⚠️  模型 {model_name} 不可用：{str(e)[:50]}")
                continue
        
        if model is None:
            print(f"❌ 所有模型都不可用")
            print(f"可用的模型列表：")
            for m in available_models[:5]:
                print(f"  - {m}")
            sys.exit(1)
        
        print(f"📝 正在生成報告...")
        
        # 生成內容
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.7,
                max_output_tokens=8192,
            )
        )
        
        # 取得報告內容
        report_content = response.text
        
        # 儲存報告
        report_path = REPORTS_DIR / REPORT_FILENAME
        
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_content)
        
        print(f"✅ 報告已生成：{report_path}")
        print(f"📏 報告長度：{len(report_content)} 字元")
        
        # 顯示 token 使用情況
        if hasattr(response, 'usage_metadata'):
            print(f"📊 Token 使用：")
            print(f"   - Prompt: {response.usage_metadata.prompt_token_count}")
            print(f"   - Response: {response.usage_metadata.candidates_token_count}")
            print(f"   - Total: {response.usage_metadata.total_token_count}")
        
        return str(report_path)
        
    except Exception as e:
        print(f"❌ 錯誤：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    report_path = generate_report()
    print(f"\n🎉 報告生成完成！")
    print(f"📁 檔案位置：{report_path}")
