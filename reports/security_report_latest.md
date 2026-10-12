# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**17** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=17。
- Intelligence 候選：**30** 筆；P1 **13**、P2 **0**、P3 **0**、WATCH **17**。
- Baseline：state / generated_at=2026-10-11T06:38:54.512909+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-9082、CVE-2026-87902、CVE-2026-76460、CVE-2026-63030、CVE-2026-48908。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **17** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-86717｜Unknown / Insurify
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:26.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00146 / percentile=0.03384
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:26.337 / 2026-10-11T12:17:24.653
- **官方描述（原文）**：The Insurify WordPress plugin through 1.0 does not have authorisation and nonce checks on one of its AJAX actions, allowing unauthenticated users to delete arbitrary WordPress options, which can take the site offline and strip every user of their role.

### 2. CVE-2026-86706｜Unknown / Quick quotes
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:26.220)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00146 / percentile=0.03385
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:26.220 / 2026-10-11T12:17:24.510
- **官方描述（原文）**：The Quick quotes WordPress plugin through 1.0.0 does not perform any capability or nonce check on one of its AJAX actions and lets the caller choose which option is written, allowing unauthenticated users to alter arbitrary site settings and to make the site unavailable.

### 3. CVE-2026-85121｜Unknown / Insurify
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:26.007)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00146 / percentile=0.03386
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:26.007 / 2026-10-11T12:17:24.223
- **官方描述（原文）**：The Insurify WordPress plugin through 1.0 does not have authorisation and nonce checks on one of its AJAX actions, allowing unauthenticated users to create and overwrite arbitrary WordPress options with request data, which can take the site offline and deactivate all of its Insurify WordPress plugin through 1.0.

### 4. CVE-2026-85118｜Unknown / AI Content Generator Marketing
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:25.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00146 / percentile=0.03385
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:25.900 / 2026-10-11T12:17:24.063
- **官方描述（原文）**：The AI Content Generator Marketing WordPress plugin through 1.0.0 does not enforce a nonce or capability check on some of its AJAX actions, allowing unauthenticated users to update and delete arbitrary WordPress options, which can be used to gain administrator access to the site.

### 5. CVE-2026-84737｜Unknown / Freeton WP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:25.797)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00146 / percentile=0.03385
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:25.797 / 2026-10-11T12:17:23.923
- **官方描述（原文）**：The Freeton WP WordPress plugin through 1.0.0 does not correctly validate the activation code when authenticating a user, allowing unauthenticated attackers to log in as any user whose email address they know, including administrators.

### 6. CVE-2026-84734｜Unknown / Mindstien Quick Login
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:25.687)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00146 / percentile=0.03385
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:25.687 / 2026-10-11T12:17:23.780
- **官方描述（原文）**：The Mindstien Quick Login WordPress plugin through 1.0 does not correctly validate a value supplied in the request against the visitor's own session before authenticating them, allowing unauthenticated attackers to obtain a session as the administrator account the Mindstien Quick Login WordPress plugin through 1.0 is configured with.

### 7. CVE-2026-84254｜Unknown / click5 CRM add-on to Contact Form 7
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:25.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00106 / percentile=0.01036
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:25.180 / 2026-10-11T12:17:23.040
- **官方描述（原文）**：The click5 CRM add-on to Contact Form 7 WordPress plugin through 1.0.4 does not have authorisation and CSRF checks when updating options via a REST endpoint, and does not ensure that the option to be updated belongs to the click5 CRM add-on to Contact Form 7 WordPress plugin through 1.0.4. As a result, unauthenticated attackers could change arbitrary blog options, allowing them to create a new administrator account and take over the site.

### 8. CVE-2026-84253｜Unknown / click5 CRM add-on to Gravity Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:25.057)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00106 / percentile=0.01036
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:25.057 / 2026-10-11T12:17:22.900
- **官方描述（原文）**：The click5 CRM add-on to Gravity Forms WordPress plugin through 1.0.3 does not have authorisation and CSRF checks when updating options via a REST endpoint, and does not ensure that the option to be updated belongs to the click5 CRM add-on to Gravity Forms WordPress plugin through 1.0.3. As a result, unauthenticated attackers could change arbitrary blog options, allowing them to create a new administrator account and take over the site.

### 9. CVE-2026-84252｜Unknown / click5 CRM add-on to WPForms
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:24.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00106 / percentile=0.01036
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:24.943 / 2026-10-11T12:17:22.757
- **官方描述（原文）**：The click5 CRM add-on to WPForms WordPress plugin through 1.0.3 does not have authorisation and CSRF checks when updating options via a REST endpoint, and does not ensure that the option to be updated belongs to the click5 CRM add-on to WPForms WordPress plugin through 1.0.3. As a result, unauthenticated attackers could change arbitrary blog options, allowing them to create a new administrator account and take over the site.

### 10. CVE-2026-84251｜Unknown / click5 CRM add-on to Ninja Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:24.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00106 / percentile=0.01035
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:24.820 / 2026-10-11T12:17:22.613
- **官方描述（原文）**：The click5 CRM add-on to Ninja Forms WordPress plugin through 1.0.1 does not have authorisation and CSRF checks when updating options via a REST endpoint, and does not ensure that the option to be updated belongs to the click5 CRM add-on to Ninja Forms WordPress plugin through 1.0.1. As a result, unauthenticated attackers could change arbitrary blog options, allowing them to create a new administrator account and take over the site.

### 11. CVE-2026-81649｜Unknown / Fundiin cho WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:24.703)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00144 / percentile=0.03197
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:24.703 / 2026-10-11T12:17:22.347
- **官方描述（原文）**：The Fundiin cho WooCommerce WordPress plugin through 3.4.0 does not have proper authorisation on several of its REST API routes, relying instead on a credential that is identical on every installation, allowing unauthenticated attackers to disclose the store's payment credentials and customer order data, overwrite the payment gateway configuration so that payments are credited elsewhere, and mark unpaid orders as paid. The same missing authorisation also allows arbitrary script to be stored in a field which is output unescaped on the classic checkout, leading to unauthenticated stored XSS on stores that do not use the block-based checkout.

### 12. CVE-2026-66086｜Unisoc (Shanghai) Technologies Co., Ltd. / Modem
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T02:16:57.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T02:16:57.600 / 2026-10-12T02:16:57.600
- **官方描述（原文）**：In the modem OTA stack, there is a possible stack-based buffer overflow due to improper validation of scheduling information in SIB1 messages. This could lead to remote code execution or denial of service with no additional execution privileges needed.

### 13. CVE-2026-108860｜SciSharp / BotSharp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T14:17:05.933)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T14:17:05.933 / 2026-10-11T14:17:05.933
- **官方描述（原文）**：BotSharp through 5.2.0 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to forge bearer tokens using the hard-coded Jwt:Key in WebStarter appsettings.json. Attackers can sign tokens with the committed HMAC secret and fixed botsharp issuer and audience to impersonate any known user, including administrators, on Authorize-protected API routes.

### 14. CVE-2026-108804｜TRENDnet / TEW-751DR
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T06:16:59.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T06:16:59.457 / 2026-10-12T06:16:59.457
- **官方描述（原文）**：A vulnerability was detected in TRENDnet TEW-751DR, TEW-752DRU and TEW733GR 1.03B01/1.03B03. Affected is the function fwrite of the file pigwidgeon.cgi of the component Web Management Backend. The manipulation of the argument service results in os command injection. It is possible to launch the attack remotely. The exploit is now public and may be used. The vendor confirms: "As this router was EOL'd in 2011, we have no way of testing if such vulnerability exists. We will notify our customers of a potential vulnerability on this product." This vulnerability only affects products that are no longer supported by the maintainer.

### 15. CVE-2026-108753｜agnaistic / agnai
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T13:17:20.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T13:17:20.237 / 2026-10-11T13:17:20.237
- **官方描述（原文）**：Agnaistic agnai through 1.0.555 contains a hard-coded credentials vulnerability in self-host.docker-compose.yml, which sets a fixed admin password and public JWT secret. Unauthenticated attackers can log in as admin or sign their own JWT with admin: true to impersonate users, reset passwords, and change server configuration.

### 16. CVE-2026-108576｜TOZED / X300
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T13:17:13.067)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T13:17:13.067 / 2026-10-11T13:17:13.067
- **官方描述（原文）**：A vulnerability was found in TOZED X300 up to 6.01.3. This vulnerability affects the function process_ping of the component IPPingDiagnostics Handler. The manipulation of the argument Host results in os command injection. The attack can be launched remotely. The vendor was contacted early about this disclosure but did not respond in any way.

### 17. CVE-2026-104028｜Unknown / Anton Extensions
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T07:17:22.440)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T07:17:22.440 / 2026-10-11T12:16:51.367
- **官方描述（原文）**：The Anton Extensions WordPress plugin through 1.2.2 does not perform any capability check, nonce verification, or file-type validation before writing attacker-supplied content to an attacker-chosen path, allowing unauthenticated attackers to upload arbitrary PHP files and achieve remote code execution.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-9082｜Drupal / Core
- **Title**：Drupal Core SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.15701 / percentile=0.96787
- **CISA KEV**：listed=true / date_added=2026-05-22 / due_date=2026-05-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Drupal Core contains a SQL injection vulnerability that could allow for privilege escalation and remote code execution via specially crafted requests sent with the database abstraction API.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-87902｜WordPress / Core
- **Title**：WordPress Core Remote File Inclusion Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.39979 / percentile=0.986
- **CISA KEV**：listed=true / date_added=2026-09-25 / due_date=2026-09-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WordPress Core contains a remote file inclusion vulnerability which could allow an unauthenticated attacker to make page-template resolution include a chosen readable local `.php` file outside the active theme directories, leading to remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-76460｜Cisco / Identity Services Engine
- **Title**：Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.14026 / percentile=0.96482
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) contain an incorrect use of privileged APIs vulnerability that could allow an unauthenticated, remote attacker to gain unauthorized access to the affected device by bypassing the web-based management interface.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-63030｜WordPress / Core
- **Title**：WordPress Core Interpretation Conflict Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.10649 / percentile=0.95709
- **CISA KEV**：listed=true / date_added=2026-07-21 / due_date=2026-07-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WordPress Core contains an interpretation conflict vulnerability that could allow an attacker to perform SQL Injection and achieve Remote Code Execution. This vulnerability can be chained with CVE-2026-60137.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-48908｜JoomShaper / SP Page Builder
- **Title**：JoomShaper SP Page Builder Unrestricted Upload of File with Dangerous Type Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.88512 / percentile=0.99772
- **CISA KEV**：listed=true / date_added=2026-07-07 / due_date=2026-07-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JoomShaper SP Page Builder contains an unrestricted upload of file with dangerous type vulnerability that allows unauthenticated users to upload arbitrary files, ultimately resulting in the upload and execution of PHP code.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-48282｜Adobe / ColdFusion
- **Title**：Adobe ColdFusion Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.42388 / percentile=0.98676
- **CISA KEV**：listed=true / date_added=2026-07-07 / due_date=2026-07-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Adobe ColdFusion contains a path traversal vulnerability that could lead to arbitrary code execution in the context of the current user.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-24061｜GNU / InetUtils
- **Title**：GNU InetUtils Argument Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.98984 / percentile=0.99929
- **CISA KEV**：listed=true / date_added=2026-01-26 / due_date=2026-02-16
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GNU InetUtils contains an argument injection vulnerability in telnetd that could allow for remote authentication bypass via a "-f root" value for the USER environment variable.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2026-20230｜Cisco / Unified Communications Manager
- **Title**：Cisco Unified Communications Manager Server-Side Request Forgery (SSRF) Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：0.882 / percentile=0.99767
- **CISA KEV**：listed=true / date_added=2026-06-25 / due_date=2026-06-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Unified Communications Manager (Unified CM) and Cisco Unified Communications Manager Session Management Edition (Unified CM SME) contain a server-side request forgery (SSRF) Vulnerability that could allow an unauthenticated, remote attacker to write files to the underlying operating system that could be used later to elevate to root.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-19490｜Citrix / NetScaler
- **Title**：Citrix NetScaler Authentication Bypass Using an Alternate Path or Channel Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.23158 / percentile=0.97724
- **CISA KEV**：listed=true / date_added=2026-09-09 / due_date=2026-09-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an authentication-bypass vulnerability involving an alternate path or channel. When the NetScaler appliance is configured as an AAA virtual server or as a Gateway (SSL VPN, ICA Proxy, CVPN, or RDP Proxy), an unauthenticated remote threat actor may be able to bypass authentication.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2025-61884｜Oracle / E-Business Suite
- **Title**：Oracle E-Business Suite Server-Side Request Forgery (SSRF) Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.95891 / percentile=0.99874
- **CISA KEV**：listed=true / date_added=2025-10-20 / due_date=2025-11-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Oracle E-Business Suite contains a server-side request forgery (SSRF) vulnerability in the Runtime component of Oracle Configurator. This vulnerability is remotely exploitable without authentication.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2025-61882 | P1 / 100 | Oracle / E-Business Suite | v3.1 9.8 (CRITICAL) | 0.99732 / percentile=0.99953 | listed=true / date_added=2025-10-06 / due_date=2025-10-27 | status=known_exploited / source=cisa_kev | Known |
| CVE-2025-61757 | P1 / 100 | Oracle / Fusion Middleware | v3.1 9.8 (CRITICAL) | 0.88647 / percentile=0.99774 | listed=true / date_added=2025-11-21 / due_date=2025-12-12 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-5777 | P1 / 100 | Citrix / NetScaler ADC and Gateway | v4.0 9.3 (CRITICAL) | 0.99972 / percentile=0.99978 | listed=true / date_added=2025-07-10 / due_date=2025-07-11 | status=known_exploited / source=cisa_kev | Known |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-86717 | WATCH / 28 | Unknown / Insurify | v3.1 9.1 (CRITICAL) | 0.00146 / percentile=0.03384 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-86706 | WATCH / 28 | Unknown / Quick quotes | v3.1 9.1 (CRITICAL) | 0.00146 / percentile=0.03385 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-85121 | WATCH / 28 | Unknown / Insurify | v3.1 9.1 (CRITICAL) | 0.00146 / percentile=0.03386 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-85118 | WATCH / 28 | Unknown / AI Content Generator Marketing | v3.1 9.8 (CRITICAL) | 0.00146 / percentile=0.03385 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-84737 | WATCH / 28 | Unknown / Freeton WP | v3.1 9.8 (CRITICAL) | 0.00146 / percentile=0.03385 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-84734 | WATCH / 28 | Unknown / Mindstien Quick Login | v3.1 9.8 (CRITICAL) | 0.00146 / percentile=0.03385 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-84254 | WATCH / 28 | Unknown / click5 CRM add-on to Contact Form 7 | v3.1 9.8 (CRITICAL) | 0.00106 / percentile=0.01036 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-84253 | WATCH / 28 | Unknown / click5 CRM add-on to Gravity Forms | v3.1 9.8 (CRITICAL) | 0.00106 / percentile=0.01036 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-84252 | WATCH / 28 | Unknown / click5 CRM add-on to WPForms | v3.1 9.8 (CRITICAL) | 0.00106 / percentile=0.01036 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-84251 | WATCH / 28 | Unknown / click5 CRM add-on to Ninja Forms | v3.1 9.8 (CRITICAL) | 0.00106 / percentile=0.01035 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-81649 | WATCH / 28 | Unknown / Fundiin cho WooCommerce | v3.1 9.1 (CRITICAL) | 0.00144 / percentile=0.03197 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-66086 | WATCH / 28 | Unisoc (Shanghai) Technologies Co., Ltd. / Modem | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-108860 | WATCH / 28 | SciSharp / BotSharp | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-108804 | WATCH / 28 | TRENDnet / TEW-751DR | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-108753 | WATCH / 28 | agnaistic / agnai | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-108576 | WATCH / 28 | TOZED / X300 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-104028 | WATCH / 28 | Unknown / Anton Extensions | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

## 建議行動

### 24 小時內
- 以資產清冊、CMDB 或 SBOM 比對所有 P1 與 CISA KEV 項目是否存在於環境；本報告未取得組織資產清冊，因此實際曝險狀態為**未確認**。
- 對已列 CISA KEV 的項目，依本報告列出的 **CISA Required Action（原文）** 與官方來源核對後執行；不要由本報告自行推定適用版本。

### 本週內
- 檢視 P2 / P3 與 WATCH 項目的 NVD / vendor 來源，確認實際使用版本與官方處置；compact intelligence 未提供結構化受影響版本時，一律視為**未確認**。
- 對 exploitation status 為 `unconfirmed` 的項目持續等待官方或可信來源更新；EPSS 不作為『已遭利用』的證據。

### 持續監控
- 持續比較 KEV、EPSS、CVSS 與 exploitation status 的跨日變化；只有資料來源狀態變更才更新對應事實。
- Google Search grounding 恢復後，才允許 LLM 以有 citation 的方式補充 vendor advisory、修補與近期攻擊脈絡。

## 產業影響

本 Facts-only 模式**不進行未驗證的產業攻擊歸因**。是否影響台灣金融、製造、科技、政府或關鍵基礎設施，必須與組織自身的 CMDB、SBOM、軟體清冊及外網暴露面比對；目前輸入未提供該類組織資產資料，因此實際產業/組織受影響狀態為**未確認**。

## 資料品質與未確認事項

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：17。
- EPSS 未確認：6；Exploitation status 未確認：5。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-12T06:47:58.696313+00:00`；Delta generated at：`2026-10-12T06:47:58.696313+00:00`。

---

## 可驗證資料來源

- **CVE-2026-9082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9082) · [Vendor / Advisory (drupal.org)](https://www.drupal.org/sa-core-2026-004)
- **CVE-2026-87902** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87902) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87902) · [Vendor / Advisory (github.com)](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-76460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76460) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-63030** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63030) · [Vendor / Advisory (wordpress.org)](https://wordpress.org/news/2026/07/wordpress-7-0-2-release/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48908) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48908) · [Vendor / Advisory (extensions.joomla.org)](https://extensions.joomla.org/extension/sp-page-builder/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-86717** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86717) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86717)
- **CVE-2026-86706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86706) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86706)
- **CVE-2026-85121** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85121) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85121)
- **CVE-2026-85118** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85118) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85118)
- **CVE-2026-84737** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84737) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84737)
- **CVE-2026-84734** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84734) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84734)
- **CVE-2026-84254** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84254) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84254)
- **CVE-2026-84253** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84253) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84253)
- **CVE-2026-84252** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84252) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84252)
- **CVE-2026-84251** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84251) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84251)
- **CVE-2026-81649** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81649) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-81649)
- **CVE-2026-66086** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66086)
- **CVE-2026-108860** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108860)
- **CVE-2026-108804** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108804)
- **CVE-2026-108753** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108753)
- **CVE-2026-108576** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108576)
- **CVE-2026-104028** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104028)
- **CVE-2026-48282** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48282) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48282) · [Vendor / Advisory (helpx.adobe.com)](https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-24061** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-24061) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-24061) · [Vendor / Advisory (cgit.git.savannah.gnu.org)](https://cgit.git.savannah.gnu.org/cgit/inetutils.git) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/ccba9f748aa8d50a38d7748e2e60362edd6a32cc) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/fd702c02497b2f398e739e3119bed0b23dd7aa7b)
- **CVE-2026-20230** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20230) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20230) · [Vendor / Advisory (cisco.com)](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssrf-cXPnHcW.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-19490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19490) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-19490) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-61884** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-61884) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-61884) · [Vendor / Advisory (oracle.com)](https://www.oracle.com/security-alerts/alert-cve-2025-61884.html)
- **CVE-2025-61882** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-61882) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-61882) · [Vendor / Advisory (oracle.com)](https://www.oracle.com/security-alerts/alert-cve-2025-61882.html)
- **CVE-2025-61757** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-61757) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-61757) · [Vendor / Advisory (oracle.com)](https://www.oracle.com/security-alerts/cpuoct2025.html)
- **CVE-2025-5777** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-5777) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-5777) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX693420)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
