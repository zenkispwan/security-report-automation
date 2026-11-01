# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**13** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=13。
- Intelligence 候選：**30** 筆；P1 **17**、P2 **0**、P3 **0**、WATCH **13**。
- Baseline：state / generated_at=2026-10-31T06:28:50.900524+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-97229、CVE-2026-9586、CVE-2026-9198、CVE-2026-9082、CVE-2026-88772。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **13** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-89270｜popupbuilder / Popup Builder – Create highly converting, mobile friendly marketing popups.
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-31T07:16:37.707)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-31T07:16:37.707 / 2026-10-31T07:16:37.707
- **官方描述（原文）**：The Popup Builder – Create highly converting, mobile friendly marketing popups. plugin for WordPress is vulnerable to authorization bypass in all versions up to, and including, 4.4.5 This is due to the plugin not properly verifying that a user is authorized to perform an action. This makes it possible for unauthenticated attackers to trash all published popups on the site with a single unauthenticated GET request. The attack is amplified by a second flaw in SGPopup::find(), which returns false for every normally published popup when the sg_popup_preview_id parameter is present, causing the trash branch to fire against every popup on the site simultaneously.

### 2. CVE-2026-120209｜anji-plus / AJ-Report
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-31T18:17:09.263)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-31T18:17:09.263 / 2026-10-31T18:17:09.263
- **官方描述（原文）**：AJ-Report through 1.7.1 signs share tokens with a hard-coded JWT secret, allowing attackers to forge valid Share-Tokens offline. Attackers can mint a token with reportCode 'dataSet' to access the testTransform endpoint, which passes scripts to GroovyClassLoader for unauthenticated remote code execution.

### 3. CVE-2026-120201｜dromara / Jpom
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-31T18:17:07.890)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-31T18:17:07.890 / 2026-10-31T18:17:08.023
- **官方描述（原文）**：Jpom 2.10.0 through 2.11.12 contains an authentication bypass vulnerability that allows unauthenticated attackers to gain super-administrator access by injecting query conditions into the JPOM-USER-TOKEN header. Attackers can send a value like 'is not null', which Hutool's Condition parser treats as an operator, then execute commands through Jpom's script features.

### 4. CVE-2026-120198｜WAVLINK / WL-WN530BE1-A
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-01T05:18:57.620)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-01T05:18:57.620 / 2026-11-01T05:18:57.620
- **官方描述（原文）**：A vulnerability has been found in WAVLINK WL-WN530BE1-A V251117. Affected is the function con_check_read_finish of the file /protocol.csp. Such manipulation of the argument group_name/IP-FROM leads to command injection. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure.

### 5. CVE-2026-120195｜WAVLINK / WL-WN579A3-A
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-01T04:18:46.687)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-01T04:18:46.687 / 2026-11-01T04:18:46.687
- **官方描述（原文）**：A security vulnerability has been detected in WAVLINK WL-WN579A3-A 2026-03-10-94f93d4. The impacted element is the function set_wzdgwMesh of the file /cgi-bin/adm.cgi of the component Initial Setup Wizard. The manipulation of the argument wlan_ssid leads to os command injection. The attack is possible to be carried out remotely. The exploit has been disclosed publicly and may be used. The vendor was contacted early about this disclosure.

### 6. CVE-2026-120189｜D-Link / DIR-505
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-01T01:17:16.877)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-01T01:17:16.877 / 2026-11-01T01:17:16.877
- **官方描述（原文）**：A vulnerability was identified in D-Link DIR-505 1.10B02. Affected is the function save_upload_file/mp_upload_file of the file /usr/bin/tftpd of the component TFTP Upload Filename Handler. The manipulation leads to stack-based buffer overflow. The attack is possible to be carried out remotely. The exploit is publicly available and might be used.

### 7. CVE-2026-119096｜uncannyowl / Uncanny Toolkit for LearnDash
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-31T08:16:49.043)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00463 / percentile=0.40109
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-31T08:16:49.043 / 2026-10-31T08:16:49.043
- **官方描述（原文）**：The Uncanny Toolkit for LearnDash plugin for WordPress is vulnerable to Authentication Bypass in versions up to, and including, 3.8.2 via the `email` parameter of the `uo_login_action()` function. This is due to a parser-differential flaw in which the plugin's account-verification gate resolves the submitted `email` value using the raw, unsanitized string passed to `get_user_by()`, while the subsequent `wp_signon()` call relies on WordPress core's internal `sanitize_user()` to strip appended junk characters — causing the gate lookup to fail and be skipped entirely while the real account is still resolved and authenticated. This makes it possible for unauthenticated attackers to log in to unverified or administrator-suspended accounts whose credentials they already possess, obtaining a valid `wordpress_logged_in` session cookie and defeating the plugin's account-approval and account-suspension controls. The nonce required to reach the handler is freely obtainable in the same request from the unauthenticated `ult-refresh-nonce` endpoint, making exploitation trivial for any attacker with network access to the site and knowledge of a target account's credentials.

### 8. CVE-2026-118636｜Apache Software Foundation / Apache MINA
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-31T21:16:53.203)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-31T21:16:53.203 / 2026-10-31T21:16:53.203
- **官方描述（原文）**：**UNSUPPORTED WHEN ASSIGNED** JavaNativeMessageDecoder in the MINA 3.0 codec module calls ObjectInputStream.readObject() on frame bytes with no class filter, so an application that puts it in front of an untrusted peer is open to gadget-chain RCE. As the 3.0.0 branch is inactive, we do not plan to release a version that fixes this issue. Users are recommended to use the latest Apache MINA 2.2.X branch.

### 9. CVE-2026-118235｜wpazleen / SimpleForm – Form Maker to Chat Apps with Quiz, Poll and Multi Lead Notifications
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-31T09:16:33.620)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.0074 / percentile=0.54613
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-31T09:16:33.620 / 2026-10-31T09:16:33.620
- **官方描述（原文）**：The SimpleForm – Form Maker to Chat Apps with Quiz, Poll and Multi Lead Notifications plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 3.10.2 via the handle_upload function. This is due to missing server-side file key allowlist and pre-sanitization extension derivation that allows a trailing-dot filename to bypass all extension and MIME validation in handle_upload. This makes it possible for unauthenticated attackers to upload files that may be executable, which makes remote code execution possible. The only access control is a nonce that is printed into every public form's data-nonce attribute, making it trivially obtainable by any unauthenticated visitor on a page embedding the form shortcode.

### 10. CVE-2026-116557｜murgroland / WP Booking System – Booking Calendar
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-31T07:16:35.857)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00348 / percentile=0.28404
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-31T07:16:35.857 / 2026-10-31T07:16:35.857
- **官方描述（原文）**：The WP Booking System - Booking Calendar plugin for WordPress is vulnerable to unauthorized modification of data due to a missing capability check on the wpbs_action_ajax_calendar_remove_note() function in versions up to, and including, 2.1.0.5 This makes it possible for authenticated attackers, with Subscriber-level access and above, to delete arbitrary calendar notes belonging to any calendar.

### 11. CVE-2026-116512｜wedevs / Project Manager – AI Powered Project Management, Task Management, Kanban Board & Time Tracker
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-31T08:16:48.603)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00584 / percentile=0.47952
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-31T08:16:48.603 / 2026-10-31T08:16:48.603
- **官方描述（原文）**：The Project Manager – AI Powered Project Management, Task Management, Kanban Board & Time Tracker plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, 4.1.1 via the 'id' parameter parameter. This is due to unsanitized 'id' parameter value concatenated directly into the pipe-delimited validation rule string, which is then split and each token invoked as a dynamic PHP function with no allowlist check. This makes it possible for unauthenticated attackers to execute code on the server. This is exploitable by unauthenticated attackers because WordPress core executes the route argument's validate_callback inside WP_REST_Server::dispatch() before the route's permission_callback is invoked, meaning the Project_Manage_Capability authorization gate is never reached on the vulnerable code path.

### 12. CVE-2026-109220｜addonsorg / PDF Invoice for WooCommerce + Drag and Drop Template Builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-31T07:16:34.367)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.0052 / percentile=0.44208
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-31T07:16:34.367 / 2026-10-31T07:16:34.367
- **官方描述（原文）**：The PDF Invoice for WooCommerce + Drag and Drop Template Builder plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 7.1.1 via the 'customer_note' parameter parameter. This is due to insufficient sanitization of the customer_note checkout field, which is inlined verbatim into invoice HTML, entity-decoded back into a live tag by simplehtmldom, reassembled into raw bytes by mPDF, and passed to unserialize() in _getObjAttr without validation. This makes it possible for unauthenticated attackers to execute code on the server. An unauthenticated attacker can trigger the vulnerable code path on a default install by placing an anonymous WooCommerce checkout via the public Store API (POST /wc/store/v1/checkout) using a Direct Bank Transfer or cheque payment method, which automatically transitions the order to 'on-hold' status and fires the plugin's invoice-generation hook.

### 13. CVE-2026-103882｜acadlix / Acadlix LMS – AI Quiz Maker, Online Exam & Course Plugin for WordPress
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-31T09:16:32.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-31T09:16:32.510 / 2026-10-31T09:16:32.510
- **官方描述（原文）**：The Acadlix LMS – AI Quiz Maker, Online Exam & Course Plugin for WordPress plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient file path validation in the post_delete_assessment_file_by_id function in all versions up to, and including, 1.1.9. This makes it possible for authenticated attackers, with subscriber-level access and above, to delete arbitrary files on the server, which can easily lead to remote code execution when the right file is deleted (such as wp-config.php). The route's permission callback only verifies a generic wp_rest nonce that the plugin itself emits inside the public acadlixOptions JavaScript object on every frontend page, effectively reducing the authentication requirement to unauthenticated.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-97229｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.273 / percentile=0.9806
- **CISA KEV**：listed=true / date_added=2026-10-29 / due_date=2026-11-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-9586｜Sangoma / Switchvox
- **Title**：Sangoma Switchvox SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.18979 / percentile=0.97303
- **CISA KEV**：listed=true / date_added=2026-09-02 / due_date=2026-09-05
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Sangoma Switchvox contains a SQL injection vulnerability which allows an unauthenticated remote attacker to execute arbitrary SQL statements against the backend PostgreSQL database using a single crafted request, including database operations and remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-9198｜IBM / Langflow
- **Title**：IBM Langflow Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.28658 / percentile=0.98137
- **CISA KEV**：listed=true / date_added=2026-08-04 / due_date=2026-08-07
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Langflow contains a code injection vulnerability that allows unauthenticated attackers to achieve full remote code execution on default Langflow deployments.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-9082｜Drupal / Core
- **Title**：Drupal Core SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.89381 / percentile=0.99784
- **CISA KEV**：listed=true / date_added=2026-05-22 / due_date=2026-05-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Drupal Core contains a SQL injection vulnerability that could allow for privilege escalation and remote code execution via specially crafted requests sent with the database abstraction API.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-88772｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.78162 / percentile=0.99578
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-88771｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Input Validation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.8216 / percentile=0.99655
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-86950｜Apple / Multiple Products
- **Title**：Apple Multiple Products Out-of-Bounds Write Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.26166 / percentile=0.97995
- **CISA KEV**：listed=true / date_added=2026-09-29 / due_date=2026-10-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apple iOS, macOS, and iPadOS contain an out-of-bounds write vulnerability in CoreGraphics that may lead to arbitrary code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2026-6973｜Ivanti / Endpoint Manager Mobile (EPMM)
- **Title**：Ivanti Endpoint Manager Mobile (EPMM) Improper Input Validation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 7.2 (HIGH)
- **EPSS**：0.34454 / percentile=0.98414
- **CISA KEV**：listed=true / date_added=2026-05-07 / due_date=2026-05-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ivanti Endpoint Manager Mobile (EPMM) contains an improper input validation vulnerability that allows a remotely authenticated user with administrative access to achieve remote code execution.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-64849｜MLflow / MLflow
- **Title**：MLflow Server-Side Request Forgery Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.10017 / percentile=0.95614
- **CISA KEV**：listed=true / date_added=2026-08-19 / due_date=2026-09-02
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：MLflow contains a server-side request forgery vulnerability that can allow attackers to reach internal or cloud metadata services and receive response_status and response_body.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-63077｜JetBrains / TeamCity
- **Title**：JetBrains TeamCity Deserialization of Untrusted Data Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.93558 / percentile=0.99841
- **CISA KEV**：listed=true / date_added=2026-08-05 / due_date=2026-08-08
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JetBrains TeamCity contains a deserialization of untrusted data vulnerability that could allow unauthenticated remote code execution via the agent polling protocol.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-63030 | P1 / 100 | WordPress / Core | v3.1 9.8 (CRITICAL) | 0.10649 / percentile=0.95798 | listed=true / date_added=2026-07-21 / due_date=2026-07-24 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-56291 | P1 / 100 | Balbooa / Forms | v4.0 10.0 (CRITICAL) | 0.14854 / percentile=0.96695 | listed=true / date_added=2026-07-10 / due_date=2026-07-13 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-56290 | P1 / 100 | Joomlack / Page Builder | v4.0 10.0 (CRITICAL) | 0.30866 / percentile=0.98252 | listed=true / date_added=2026-07-07 / due_date=2026-07-10 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-48939 | P1 / 100 | iCagenda / iCagenda | v4.0 10.0 (CRITICAL) | 0.20069 / percentile=0.97447 | listed=true / date_added=2026-07-10 / due_date=2026-07-13 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-48908 | P1 / 100 | JoomShaper / SP Page Builder | v4.0 10.0 (CRITICAL) | 0.88512 / percentile=0.99772 | listed=true / date_added=2026-07-07 / due_date=2026-07-10 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-45321 | P1 / 100 | TanStack / TanStack | v3.1 9.6 (CRITICAL) | 0.03278 / percentile=0.88427 | listed=true / date_added=2026-05-27 / due_date=2026-06-10 | status=known_exploited / source=cisa_kev | Known |
| CVE-2026-42271 | P1 / 100 | BerriAI / LiteLLM | v4.0 8.7 (HIGH) | 0.91445 / percentile=0.99812 | listed=true / date_added=2026-06-08 / due_date=2026-06-22 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-89270 | WATCH / 28 | popupbuilder / Popup Builder – Create highly converting, mobile friendly marketing popups. | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120209 | WATCH / 28 | anji-plus / AJ-Report | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120201 | WATCH / 28 | dromara / Jpom | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120198 | WATCH / 28 | WAVLINK / WL-WN530BE1-A | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120195 | WATCH / 28 | WAVLINK / WL-WN579A3-A | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120189 | WATCH / 28 | D-Link / DIR-505 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-119096 | WATCH / 28 | uncannyowl / Uncanny Toolkit for LearnDash | v3.1 9.8 (CRITICAL) | 0.00463 / percentile=0.40109 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-118636 | WATCH / 28 | Apache Software Foundation / Apache MINA | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-118235 | WATCH / 28 | wpazleen / SimpleForm – Form Maker to Chat Apps with Quiz, Poll and Multi Lead Notifications | v3.1 9.8 (CRITICAL) | 0.0074 / percentile=0.54613 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-116557 | WATCH / 28 | murgroland / WP Booking System – Booking Calendar | v3.1 9.1 (CRITICAL) | 0.00348 / percentile=0.28404 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-116512 | WATCH / 28 | wedevs / Project Manager – AI Powered Project Management, Task Management, Kanban Board & Time Tracker | v3.1 9.8 (CRITICAL) | 0.00584 / percentile=0.47952 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-109220 | WATCH / 28 | addonsorg / PDF Invoice for WooCommerce + Drag and Drop Template Builder | v3.1 9.8 (CRITICAL) | 0.0052 / percentile=0.44208 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-103882 | WATCH / 28 | acadlix / Acadlix LMS – AI Quiz Maker, Online Exam & Course Plugin for WordPress | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：13。
- EPSS 未確認：8；Exploitation status 未確認：13。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-01T07:00:11.176869+00:00`；Delta generated at：`2026-11-01T07:00:11.176869+00:00`。

---

## 可驗證資料來源

- **CVE-2026-97229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97229) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97229) · [Vendor / Advisory (ruby-lang.org)](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9586** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9586) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9586) · [Vendor / Advisory (sangomakb.atlassian.net)](https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9198) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9198) · [Vendor / Advisory (ibm.com)](https://www.ibm.com/support/pages/node/7278927) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9082) · [Vendor / Advisory (drupal.org)](https://www.drupal.org/sa-core-2026-004)
- **CVE-2026-88772** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88772) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-89270** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89270)
- **CVE-2026-120209** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120209)
- **CVE-2026-120201** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120201)
- **CVE-2026-120198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120198)
- **CVE-2026-120195** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120195)
- **CVE-2026-120189** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120189)
- **CVE-2026-119096** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119096) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-119096)
- **CVE-2026-118636** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118636)
- **CVE-2026-118235** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118235) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-118235)
- **CVE-2026-116557** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116557) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116557)
- **CVE-2026-116512** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116512) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116512)
- **CVE-2026-109220** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109220) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109220)
- **CVE-2026-103882** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103882)
- **CVE-2026-88771** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88771) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88771) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772)
- **CVE-2026-86950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86950) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86950) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149226) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149228) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149229) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-6973** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-6973) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-6973) · [Vendor / Advisory (hub.ivanti.com)](https://hub.ivanti.com/s/article/May-2026-Security-Advisory-Ivanti-Endpoint-Manager-Mobile-EPMM-Multiple-CVEs?language=en_US)
- **CVE-2026-64849** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-64849) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-64849) · [Vendor / Advisory (github.com)](https://github.com/mlflow/mlflow/pull/24258) · [Vendor / Advisory (github.com)](https://github.com/mlflow/mlflow/issues/24179) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-63077** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63077) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (blog.jetbrains.com)](https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/) · [Vendor / Advisory (jetbrains.com)](https://www.jetbrains.com/privacy-security/issues-fixed/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-63030** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63030) · [Vendor / Advisory (wordpress.org)](https://wordpress.org/news/2026/07/wordpress-7-0-2-release/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-56291** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56291) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-56291) · [Vendor / Advisory (balbooa.com)](https://www.balbooa.com/joomla-forms) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-56290** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56290) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-56290) · [Vendor / Advisory (joomlack.fr)](https://www.joomlack.fr/en/joomla-extensions/page-builder-ck) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48939) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48939) · [Vendor / Advisory (icagenda.com)](https://www.icagenda.com/#download) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48908) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48908) · [Vendor / Advisory (extensions.joomla.org)](https://extensions.joomla.org/extension/sp-page-builder/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-45321** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45321) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-45321) · [Vendor / Advisory (github.com)](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)
- **CVE-2026-42271** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42271) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42271) · [Vendor / Advisory (github.com)](https://github.com/BerriAI/litellm/security/advisories/GHSA-v4p8-mg3p-g94g) · [Vendor / Advisory (github.com)](https://github.com/BerriAI/litellm/releases/tag/v1.83.7-stable)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
