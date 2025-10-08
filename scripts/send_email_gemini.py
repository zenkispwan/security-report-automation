#!/usr/bin/env python3
"""
郵件發送腳本（Gemini 版本）
發送固定檔名的資安報告
"""

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from pathlib import Path
import markdown


def find_latest_report():
    """尋找最新的報告檔案（固定檔名版本）"""
    reports_dir = Path("reports")
    if not reports_dir.exists():
        print("❌ 錯誤：reports 目錄不存在")
        sys.exit(1)
    
    # 固定檔名
    report_file = reports_dir / "security_report_latest.md"
    
    if not report_file.exists():
        print("❌ 錯誤：找不到報告檔案 security_report_latest.md")
        sys.exit(1)
    
    return report_file


def markdown_to_html(markdown_text):
    """將 Markdown 轉換為 HTML"""
    
    html_template = """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 900px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }}
            h2 {{
                color: #34495e;
                margin-top: 30px;
                border-left: 4px solid #3498db;
                padding-left: 10px;
            }}
            h3 {{
                color: #555;
                margin-top: 20px;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }}
            a {{
                color: #3498db;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            .footer {{
                margin-top: 40px;
                padding-top: 20px;
                border-top: 1px solid #ddd;
                color: #777;
                font-size: 0.9em;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {content}
            <div class="footer">
                <p>此報告由 GitHub Actions + Google Gemini 自動生成</p>
                <p>發送時間：{timestamp}</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    html_content = markdown.markdown(
        markdown_text,
        extensions=['tables', 'fenced_code', 'nl2br']
    )
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html = html_template.format(content=html_content, timestamp=timestamp)
    
    return html


def send_email(report_path):
    """發送郵件"""
    
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    recipient_email = os.getenv("EMAIL_RECIPIENT")
    
    if not all([sender_email, sender_password, recipient_email]):
        print("❌ 錯誤：郵件設定不完整")
        print(f"   EMAIL_SENDER: {'✓' if sender_email else '✗'}")
        print(f"   EMAIL_PASSWORD: {'✓' if sender_password else '✗'}")
        print(f"   EMAIL_RECIPIENT: {'✓' if recipient_email else '✗'}")
        sys.exit(1)
    
    with open(report_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    html_content = markdown_to_html(markdown_content)
    
    today = datetime.now().strftime('%Y年%m月%d日')
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'📊 資安威脅情報報告 - {today}'
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    text_part = MIMEText(markdown_content, 'plain', 'utf-8')
    msg.attach(text_part)
    
    html_part = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(html_part)
    
    print(f"📧 準備發送郵件...")
    print(f"   寄件者：{sender_email}")
    print(f"   收件者：{recipient_email}")
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        print("✅ 郵件發送成功！")
        return True
        
    except Exception as e:
        print(f"❌ 發送失敗：{e}")
        sys.exit(1)


if __name__ == "__main__":
    report_path = find_latest_report()
    print(f"📄 找到報告：{report_path}")
    send_email(report_path)
    print("\n🎉 郵件發送完成！")
