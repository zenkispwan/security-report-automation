#!/usr/bin/env python3
"""
郵件發送腳本
將生成的資安報告透過郵件發送
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
    """尋找最新的報告檔案"""
    reports_dir = Path("reports")
    if not reports_dir.exists():
        print("❌ 錯誤：reports 目錄不存在")
        sys.exit(1)
    
    # 找到今天的報告
    today = datetime.now().strftime('%Y%m%d')
    report_file = reports_dir / f"security_report_{today}.md"
    
    if not report_file.exists():
        # 如果找不到今天的，就找最新的
        reports = sorted(reports_dir.glob("security_report_*.md"), reverse=True)
        if not reports:
            print("❌ 錯誤：找不到任何報告檔案")
            sys.exit(1)
        report_file = reports[0]
    
    return report_file


def markdown_to_html(markdown_text):
    """將 Markdown 轉換為 HTML"""
    
    # 基本的 HTML 樣式
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
            .risk-critical {{
                background-color: #ffebee;
                border-left: 4px solid #f44336;
                padding: 15px;
                margin: 15px 0;
            }}
            .risk-high {{
                background-color: #fff3e0;
                border-left: 4px solid #ff9800;
                padding: 15px;
                margin: 15px 0;
            }}
            .risk-medium {{
                background-color: #e8f5e9;
                border-left: 4px solid #4caf50;
                padding: 15px;
                margin: 15px 0;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
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
                <p>此報告由 GitHub Actions 自動生成</p>
                <p>生成時間：{timestamp}</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # 轉換 Markdown 到 HTML
    html_content = markdown.markdown(
        markdown_text,
        extensions=['tables', 'fenced_code', 'nl2br']
    )
    
    # 插入樣式模板
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html = html_template.format(content=html_content, timestamp=timestamp)
    
    return html


def send_email(report_path):
    """發送郵件"""
    
    # 取得環境變數
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    recipient_email = os.getenv("EMAIL_RECIPIENT")
    
    if not all([sender_email, sender_password, recipient_email]):
        print("❌ 錯誤：郵件設定不完整")
        print(f"   EMAIL_SENDER: {'✓' if sender_email else '✗'}")
        print(f"   EMAIL_PASSWORD: {'✓' if sender_password else '✗'}")
        print(f"   EMAIL_RECIPIENT: {'✓' if recipient_email else '✗'}")
        sys.exit(1)
    
    # 讀取報告內容
    with open(report_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # 轉換為 HTML
    html_content = markdown_to_html(markdown_content)
    
    # 建立郵件
    today = datetime.now().strftime('%Y年%m月%d日')
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'📊 每日資安威脅情報報告 - {today}'
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    # 附加純文字版本（備用）
    text_part = MIMEText(markdown_content, 'plain', 'utf-8')
    msg.attach(text_part)
    
    # 附加 HTML 版本
    html_part = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(html_part)
    
    # 附加原始 Markdown 檔案
    with open(report_path, 'rb') as f:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(f.read())
        encoders.encode_base64(attachment)
        attachment.add_header(
            'Content-Disposition',
            f'attachment; filename={report_path.name}'
        )
        msg.attach(attachment)
    
    print(f"📧 準備發送郵件...")
    print(f"   寄件者：{sender_email}")
    print(f"   收件者：{recipient_email}")
    print(f"   主旨：{msg['Subject']}")
    
    try:
        # 連接 Gmail SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.set_debuglevel(0)  # 設為 1 可看詳細除錯訊息
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        print("✅ 郵件發送成功！")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("❌ 郵件認證失敗")
        print("   請確認：")
        print("   1. Gmail 帳號已啟用兩步驟驗證")
        print("   2. 使用的是「應用程式密碼」而非一般密碼")
        print("   3. 應用程式密碼格式正確（16字元，無空格）")
        sys.exit(1)
    except smtplib.SMTPException as e:
        print(f"❌ SMTP 錯誤：{e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 發送失敗：{e}")
        sys.exit(1)


if __name__ == "__main__":
    # 尋找最新報告
    report_path = find_latest_report()
    print(f"📄 找到報告：{report_path}")
    
    # 發送郵件
    send_email(report_path)
    print("\n🎉 郵件發送完成！")
