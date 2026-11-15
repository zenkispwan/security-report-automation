# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**8** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=8。
- Intelligence 候選：**30** 筆；P1 **22**、P2 **0**、P3 **0**、WATCH **8**。
- Baseline：state / generated_at=2026-11-14T07:13:03.825629+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-97229、CVE-2026-9586、CVE-2026-9198、CVE-2026-9082、CVE-2026-86950。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **8** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-19907｜shipo / Shipo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-14T13:17:23.137)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-14T13:17:23.137 / 2026-11-14T13:17:23.250
- **官方描述（原文）**：The Shipo plugin for WordPress is vulnerable to Authentication Bypass in versions 1.6 through 1.8.0. This is due to the `authenticate_rest_user()` function parsing the `LOGGED_IN_COOKIE` value and authenticating the named user without verifying the cookie's cryptographic signature. The function's intended `/wp-json/shipo/` route restriction can also be bypassed by placing that substring in the query string of an unrelated REST endpoint. This makes it possible for unauthenticated attackers who know an existing username to impersonate that user, including an administrator, and perform authorized actions through the REST API, including creating another administrator account.

### 2. CVE-2026-129433｜Dokploy / dokploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-14T13:17:22.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-14T13:17:22.820 / 2026-11-14T13:17:22.940
- **官方描述（原文）**：Dokploy before 0.31.1 contains an OS command injection vulnerability in getComposeContainerCommand() that allows authenticated organization members to execute shell commands via the serviceName parameter. Attackers can store serviceName values with shell metacharacters through backup.create or backup.update tRPC procedures, executing commands as root when scheduled backups run and taking over the host via the mounted Docker socket.

### 3. CVE-2026-129354｜D-Link / DIR-600L
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-15T01:18:03.043)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-15T01:18:03.043 / 2026-11-15T01:18:03.190
- **官方描述（原文）**：A flaw has been found in D-Link DIR-600L 2.17b02. Affected by this issue is the function hnap_main of the file htdocs/cgibin of the component HNAP Handler. Executing a manipulation can lead to stack-based buffer overflow. The attack can be executed remotely. The exploit has been published and may be used.

### 4. CVE-2026-129353｜D-Link / DIR-600L
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-15T00:16:51.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-15T00:16:51.120 / 2026-11-15T00:16:51.267
- **官方描述（原文）**：A vulnerability was detected in D-Link DIR-600L 2.17/2.17b02. Affected by this vulnerability is the function authenticationcgi_main of the file authentication.cgi. Performing a manipulation of the argument id/password results in stack-based buffer overflow. Remote exploitation of the attack is possible. The exploit is now public and may be used.

### 5. CVE-2026-129351｜TRENDnet / TEW-657BRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-14T23:16:47.753)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-14T23:16:47.753 / 2026-11-14T23:16:47.983
- **官方描述（原文）**：A security vulnerability has been detected in TRENDnet TEW-657BRM 1.00.1. This vulnerability affects the function sprintf of the file /setup.cgi of the component mini_httpd. Such manipulation leads to out-of-bounds write. The attack can be executed remotely. The exploit has been disclosed publicly and may be used. The vendor explains: ""I am not able to confirm if such vulnerability exists as the product has been EOL for more than 15 years. We will send out an announcement letting customers know." This vulnerability only affects products that are no longer supported by the maintainer.

### 6. CVE-2026-129261｜Kingston / FURY CTRL RGB Control Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-14T16:17:04.517)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-14T16:17:04.517 / 2026-11-14T16:17:04.677
- **官方描述（原文）**：A vulnerability was found in Kingston FURY CTRL RGB Control Software up to 2.0.66.0. The impacted element is an unknown function in the library NTIOLib_X64.sys of the component IOCTL Handler. Performing a manipulation results in exposed ioctl with insufficient access control. The attack is only possible with local access.

### 7. CVE-2026-129255｜CoolerMaster / MASTERPLUS+
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-14T13:17:21.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-14T13:17:21.910 / 2026-11-14T13:17:22.050
- **官方描述（原文）**：A vulnerability was identified in CoolerMaster MASTERPLUS+ 1.9.6. This affects the function sub_11504 in the library WinRing0x64.sys of the component Device Driver. The manipulation of the argument PhysicalAddress leads to incorrect default permissions. The attack can only be performed from a local environment. The vendor was contacted early about this disclosure but did not respond in any way.

### 8. CVE-2026-120522｜fluentwiz / Cloud Storage Manager for Fluent Forms – Google Drive, Dropbox, OneDrive, S3 Uploads
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-14T13:17:20.403)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-14T13:17:20.403 / 2026-11-14T13:17:20.520
- **官方描述（原文）**：The Cloud Storage Manager for Fluent Forms – Google Drive, Dropbox, OneDrive, S3 Uploads plugin for WordPress is vulnerable to Arbitrary File Write in all versions up to, and including, 1.2.0. This is due to missing authorization checks on the `connection/{driver}/save` and `/download/single-file` REST endpoints, combined with insufficient path validation in the Google Drive `downloadFile()` function, where the Google Drive metadata `name` value is concatenated into a local path without `basename()`, `sanitize_file_name()`, or canonical path validation. This makes it possible for unauthenticated attackers to store attacker-controlled Google Drive credentials, trigger a download of an attacker-owned file whose provider-returned filename contains path traversal, and write attacker-controlled content outside the intended `downloads` directory. When the written file has a PHP extension and lands in a web-accessible location, this can lead to remote code execution.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-97229｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.69289 / percentile=0.99369
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
- **EPSS**：0.18979 / percentile=0.97348
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
- **EPSS**：0.28658 / percentile=0.98169
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
- **EPSS**：0.89381 / percentile=0.99789
- **CISA KEV**：listed=true / date_added=2026-05-22 / due_date=2026-05-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Drupal Core contains a SQL injection vulnerability that could allow for privilege escalation and remote code execution via specially crafted requests sent with the database abstraction API.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-86950｜Apple / Multiple Products
- **Title**：Apple Multiple Products Out-of-Bounds Write Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.26166 / percentile=0.98023
- **CISA KEV**：listed=true / date_added=2026-09-29 / due_date=2026-10-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apple iOS, macOS, and iPadOS contain an out-of-bounds write vulnerability in CoreGraphics that may lead to arbitrary code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-48939｜iCagenda / iCagenda
- **Title**：iCagenda Unrestricted Upload of File with Dangerous Type Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.20069 / percentile=0.97489
- **CISA KEV**：listed=true / date_added=2026-07-10 / due_date=2026-07-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：iCagenda contains an unrestricted upload of file with dangerous type vulnerability that allows the upload of arbitrary files in the file attachment feature, ultimately resulting in PHP code upload and execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-48908｜JoomShaper / SP Page Builder
- **Title**：JoomShaper SP Page Builder Unrestricted Upload of File with Dangerous Type Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.89176 / percentile=0.99785
- **CISA KEV**：listed=true / date_added=2026-07-07 / due_date=2026-07-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JoomShaper SP Page Builder contains an unrestricted upload of file with dangerous type vulnerability that allows unauthenticated users to upload arbitrary files, ultimately resulting in the upload and execution of PHP code.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2026-42208｜BerriAI / LiteLLM
- **Title**：BerriAI LiteLLM SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.8942 / percentile=0.9979
- **CISA KEV**：listed=true / date_added=2026-05-08 / due_date=2026-05-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：BerriAI LiteLLM contains a SQL injection vulnerability that allows an attacker to read data from the proxy's database and potentially modify it, leading to unauthorized access to the proxy and the credentials it manages.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-31431｜Linux / Kernel
- **Title**：Linux Kernel Incorrect Resource Transfer Between Spheres Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.98114 / percentile=0.99912
- **CISA KEV**：listed=true / date_added=2026-05-01 / due_date=2026-05-15
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Linux Kernel contains an incorrect resource transfer between spheres vulnerability that could allow for privilege escalation.
- **CISA Required Action（原文）**："Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-116606｜Barracuda Networks / Barracuda Email Security Gateway (ESG)
- **Title**：Barracuda Networks Email Security Gateway (ESG) Authentication Bypass Using an Alternate Path or Channel Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.10947 / percentile=0.95956
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Barracuda Networks Email Security Gateway (ESG) contains an authentication bypass using an alternate path or channel that could allow an unauthenticated remote attacker to invoke a configuration-import function and restore a crafted, compatible backup archive, resulting in unauthorized modification of the appliance’s global configuration. This vulnerability can be chained with CVE-2026-111560.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-111497 | P1 / 100 | Google / Brotli | v4.0 9.2 (CRITICAL) | 0.82641 / percentile=0.99673 | listed=true / date_added=2026-10-27 / due_date=2026-11-10 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-110447 | P1 / 100 | Collabora / Collabora Online – Built-in CODE Server | v4.0 9.2 (CRITICAL) | 0.73307 / percentile=0.99469 | listed=true / date_added=2026-10-23 / due_date=2026-10-26 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-109619 | P1 / 100 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.99999 / percentile=0.99999 | listed=true / date_added=2026-10-26 / due_date=2026-10-29 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-109618 | P1 / 100 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.99999 / percentile=0.99999 | listed=true / date_added=2026-10-26 / due_date=2026-10-29 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-105134 | P1 / 100 | Ahsay / AhsayCBS | v4.0 10.0 (CRITICAL) | 0.81763 / percentile=0.99652 | listed=true / date_added=2026-10-14 / due_date=2026-10-17 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-68645 | P1 / 100 | Synacor / Zimbra Collaboration Suite (ZCS) | v3.1 8.8 (HIGH) | 0.50572 / percentile=0.98936 | listed=true / date_added=2026-01-22 / due_date=2026-02-12 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-68613 | P1 / 100 | n8n / n8n | v3.1 8.8 (HIGH) | 0.98994 / percentile=0.99931 | listed=true / date_added=2026-03-11 / due_date=2026-03-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-105133 | P1 / 99 | Ahsay / AhsayCBS | v4.0 6.9 (MEDIUM) | 0.84478 / percentile=0.99707 | listed=true / date_added=2026-10-14 / due_date=2026-10-17 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-96951 | P1 / 95 | Microsoft / Windows | v3.1 8.8 (HIGH) | 0.09813 / percentile=0.95623 | listed=true / date_added=2026-10-13 / due_date=2026-10-16 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-46300 | P1 / 95 | Linux / Kernel | v3.1 7.8 (HIGH) | 0.1613 / percentile=0.96979 | listed=true / date_added=2026-10-28 / due_date=2026-10-31 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-42018 | P1 / 95 | JFrog / Artifactory | v3.1 7.5 (HIGH) | 0.09983 / percentile=0.95675 | listed=true / date_added=2026-09-11 / due_date=2026-09-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-111560 | P1 / 95 | Barracuda Networks / Multiple Products | v4.0 8.6 (HIGH) | 0.09082 / percentile=0.95375 | listed=true / date_added=2026-11-10 / due_date=2026-11-13 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-19907 | WATCH / 28 | shipo / Shipo | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-129433 | WATCH / 28 | Dokploy / dokploy | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-129354 | WATCH / 28 | D-Link / DIR-600L | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-129353 | WATCH / 28 | D-Link / DIR-600L | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-129351 | WATCH / 28 | TRENDnet / TEW-657BRM | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-129261 | WATCH / 28 | Kingston / FURY CTRL RGB Control Software | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-129255 | WATCH / 28 | CoolerMaster / MASTERPLUS+ | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120522 | WATCH / 28 | fluentwiz / Cloud Storage Manager for Fluent Forms – Google Drive, Dropbox, OneDrive, S3 Uploads | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：8。
- EPSS 未確認：8；Exploitation status 未確認：8。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-15T07:22:24.192484+00:00`；Delta generated at：`2026-11-15T07:22:24.192484+00:00`。

---

## 可驗證資料來源

- **CVE-2026-97229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97229) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97229) · [Vendor / Advisory (ruby-lang.org)](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9586** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9586) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9586) · [Vendor / Advisory (sangomakb.atlassian.net)](https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9198) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9198) · [Vendor / Advisory (ibm.com)](https://www.ibm.com/support/pages/node/7278927) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9082) · [Vendor / Advisory (drupal.org)](https://www.drupal.org/sa-core-2026-004)
- **CVE-2026-86950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86950) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86950) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149226) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149228) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149229) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-19907** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19907)
- **CVE-2026-129433** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129433)
- **CVE-2026-129354** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129354)
- **CVE-2026-129353** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129353)
- **CVE-2026-129351** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129351)
- **CVE-2026-129261** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129261)
- **CVE-2026-129255** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129255)
- **CVE-2026-120522** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120522)
- **CVE-2026-48939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48939) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48939) · [Vendor / Advisory (icagenda.com)](https://www.icagenda.com/#download) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48908) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48908) · [Vendor / Advisory (extensions.joomla.org)](https://extensions.joomla.org/extension/sp-page-builder/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-42208** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42208) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42208) · [Vendor / Advisory (github.com)](https://github.com/BerriAI/litellm/security/advisories/GHSA-r75f-5x8p-qvmc)
- **CVE-2026-31431** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-31431) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (lore.kernel.org)](https://lore.kernel.org/linux-cve-announce/2026042214-CVE-2026-31431-3d65@gregkh/) · [Vendor / Advisory (xint.io)](https://xint.io/blog/copy-fail-linux-distributions#the-fix-6) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/about/)
- **CVE-2026-116606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116606) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116606) · [Vendor / Advisory (trust.barracuda.com)](https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection) · [Vendor / Advisory (github.com)](https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0042.md) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-111560** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111560) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111560) · [Vendor / Advisory (trust.barracuda.com)](https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection) · [Vendor / Advisory (github.com)](https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0041.md) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-111497** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111497) · [Vendor / Advisory (github.com)](https://github.com/google/brotli/releases/tag/v1.2.1) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-110447** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110447) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-110447) · [Vendor / Advisory (help.nextcloud.com)](https://help.nextcloud.com/t/to-collabora-built-in-user-update-asap/250516) · [Vendor / Advisory (github.com)](https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-109619** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109619) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109619) · [Vendor / Advisory (php.net)](https://www.php.net/) · [CISA](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-109618** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109618) · [Vendor / Advisory (php.net)](https://www.php.net/) · [CISA](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-105134** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105134) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105134) · [Vendor / Advisory (ahsay.com)](https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-68645** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-68645) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-68645) · [Vendor / Advisory (wiki.zimbra.com)](https://wiki.zimbra.com/wiki/Security_Center)
- **CVE-2025-68613** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-68613) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (github.com)](https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp)
- **CVE-2026-105133** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105133) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105133) · [Vendor / Advisory (ahsay.com)](https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-96951** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96951) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96951) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-96951)
- **CVE-2026-46300** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46300) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-46300) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/3599e6b3cc1ada96883d496a50a210d3afbb6987) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/2f2b16022a2e10ca7bccfb98db5ed2ec0f72641c) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/9d3e5fd19fe1063bf607219e8562fbd567b8e8d5) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/78bf6b6bb19541d19fbda6242e7cfe2c682763c0) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/760e1addc27ba1a7beb4a0a7e8b3e9ec49e7a34e) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/3bd9e113d50034db99d7ef69fd8e5242d15e414a) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/3884358a9286b17f389a72b1426fc4547c23c111) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/f84eca5817390257cef78013d0112481c503b4a3) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-42018** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42018) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42018) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/jfrog-security-advisories) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
