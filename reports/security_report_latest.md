# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**20** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=20。
- Intelligence 候選：**30** 筆；P1 **10**、P2 **0**、P3 **0**、WATCH **20**。
- Baseline：state / generated_at=2026-11-08T06:49:44.174201+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-97229、CVE-2026-9586、CVE-2026-9198、CVE-2026-9082、CVE-2026-88772。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **20** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-6715｜IBM / Concert
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T19:17:39.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T19:17:39.980 / 2026-11-08T19:17:40.093
- **官方描述（原文）**：IBM Concert 1.0 through 3.0.1.1 allows an attacker can supply crafted input that is incorporated into an operating system command without adequate validation or sanitization. Successful exploitation allows remote attackers to execute arbitrary commands on the underlying operating system with the privileges of the affected service.

### 2. CVE-2026-17466｜IBM / Optim
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T18:17:03.303)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T18:17:03.303 / 2026-11-08T18:17:03.410
- **官方描述（原文）**：IBM Optim 1.0.0, 1.1.0, and 1.2.0 could allow a remote authenticated attacker to obtain sensitive information due to path traversal.

### 3. CVE-2026-15266｜IBM / Concert
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T18:17:02.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T18:17:02.450 / 2026-11-08T18:17:02.560
- **官方描述（原文）**：IBM Concert 1.0 through 3.0.1.1 contains components that allow potentially unsafe command execution, which could be exploited to run arbitrary system commands on the host.

### 4. CVE-2026-124494｜JiHong88 / suneditor
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T14:18:19.277)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T14:18:19.277 / 2026-11-08T14:18:19.277
- **官方描述（原文）**：SunEditor before 3.4.0 contains a stored cross-site scripting vulnerability because the html.clean() sanitizer's _normalizeURL() function decodes named entities like &colon; to an empty string. Attackers can inject href values such as javascript&colon; that pass the _isSafeURL() check but are decoded by browsers, executing JavaScript when victims click stored links.

### 5. CVE-2026-124493｜JiHong88 / suneditor
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T14:18:19.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T14:18:19.130 / 2026-11-08T14:18:19.130
- **官方描述（原文）**：SunEditor before 3.4.0 contains a stored cross-site scripting vulnerability in the DocumentType constructor that injects header textContent into innerHTML without HTML escaping. Attackers can store entity-encoded HTML in h1-h6 headers that executes JavaScript when editors using document:header mode initialize, enabling session cookie theft.

### 6. CVE-2026-124490｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T14:18:18.667)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T14:18:18.667 / 2026-11-08T14:18:18.667
- **官方描述（原文）**：OpenEMR before 8.3.0 contains a path traversal vulnerability in the RingCentral RCFaxClient disposeDocument() method of oe-module-faxsms that allows authenticated attackers to read and write arbitrary files via the file_path parameter. Attackers can use action=download to read credentials and source code, or action=setup with base64 content to write web-executable files for code execution.

### 7. CVE-2026-124469｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T14:18:15.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T14:18:15.130 / 2026-11-08T14:18:15.130
- **官方描述（原文）**：OpenEMR before 8.3.0 contains an SQL injection vulnerability in the Fee Sheet drug-inventory lookup (DrugSalesService::sellDrug) that interpolates the prod[N][warehouse] POST field into an ORDER BY clause. Low-privileged authenticated users can submit Fee Sheet product lines with constant subqueries to run a time-based blind oracle, extracting patient data and users_secure bcrypt hashes.

### 8. CVE-2026-124463｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T14:18:14.167)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T14:18:14.167 / 2026-11-08T14:18:14.167
- **官方描述（原文）**：OpenEMR before 8.3.0 contains a stored cross-site scripting vulnerability that allows authenticated users with CAMOS access to inject HTML by saving malicious CAMOS content through ajax_save.php. Attackers can store a script payload that executes unencoded when the entry is printed via the non-print_html branch of rx_print.php, performing actions and reading data as the victim user.

### 9. CVE-2026-124450｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T14:18:12.260)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T14:18:12.260 / 2026-11-08T14:18:12.260
- **官方描述（原文）**：OpenEMR before 8.3.0 contains a broken access control and path traversal vulnerability in the fax/sms module disposeDocument action via an unvalidated file_path parameter. Authenticated low-privilege users can read sqlconf.php to recover database credentials and write arbitrary files as the web user, enabling remote code execution.

### 10. CVE-2026-124445｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T14:18:11.487)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T14:18:11.487 / 2026-11-08T14:18:11.487
- **官方描述（原文）**：OpenEMR from 7.0.1 before 8.4.0 contains a flaw in src/Common/Auth/OneTimeAuth.php that ignores the enforce_onetime_use and max_access_count flags, never revokes consumed service_auth tokens, and checks login_pin without rate limiting or strict comparison. Attackers holding a captured token can replay it or brute-force the PIN to open patient-portal sessions exposing PHI.

### 11. CVE-2026-124440｜kyverno / kyverno
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T14:18:10.633)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T14:18:10.633 / 2026-11-08T14:18:10.633
- **官方描述（原文）**：Kyverno from 1.19.1 before 1.19.2 contains an authorization bypass vulnerability in the apiCall namespace clamp that allows namespace tenants to issue cross-namespace and cluster-scoped API requests by appending malformed percent-escapes to urlPath. Attackers can create namespaced Policies whose apiCall runs as the admission-controller ServiceAccount to read other namespaces' resources and create mutating webhooks, escalating to cluster admin.

### 12. CVE-2026-124438｜scriban / scriban
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T14:18:10.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T14:18:10.320 / 2026-11-08T14:18:10.320
- **官方描述（原文）**：Scriban before 7.5.2 contains an information disclosure and object manipulation vulnerability that allows template authors to access .NET internals of function values through reflection member accessors. Attackers can use array.map to read Target, Method, or ReturnType on imported delegates, exposing and overwriting service properties, captured closure secrets, and assembly paths.

### 13. CVE-2026-124427｜craftcms / cms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T14:18:08.517)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T14:18:08.517 / 2026-11-08T14:18:08.517
- **官方描述（原文）**：Craft CMS from 5.0.0 before 5.11.2 contains an authorization bypass vulnerability that allows anonymous GraphQL clients to read out-of-scope section entries via prev/next fields. Attackers can chain next hops from one visible in-scope entry to enumerate entries and read titles, slugs, and custom-field content from withheld sections.

### 14. CVE-2026-119506｜DynamiApps / Frontend Admin by DynamiApps
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T01:17:01.197)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T01:17:01.197 / 2026-11-09T01:17:02.270
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in DynamiApps Frontend Admin by DynamiApps acf-frontend-form-element allows Privilege Escalation.This issue affects Frontend Admin by DynamiApps: from n/a through 3.30.1.

### 15. CVE-2026-114464｜IBM / Process Mining
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T17:16:36.583)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T17:16:36.583 / 2026-11-08T17:16:36.690
- **官方描述（原文）**：IBM Process Mining 2.0.0 through 2.2.1 could allow a remote attacker to obtain sensitive information due to improper access control.

### 16. CVE-2026-113364｜NEC Corporation / WebSAM WinShare
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T05:18:26.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T05:18:26.810 / 2026-11-09T05:18:26.810
- **官方描述（原文）**：Buffer Overflow in the data receiving process in NEC Corporation WebSAM WinShare Ver 7.5.0 and earlier, Ver 7.6.0 and Ver 7.7.0 through 7.7.2 on Windows allows a remote unauthenticated attacker to execute arbitrary code with SYSTEM privileges via a crafted packet with a malformed data size value in the protocol header.

### 17. CVE-2026-113363｜NEC Corporation / WebSAM WinShare
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T05:18:26.107)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T05:18:26.107 / 2026-11-09T05:18:26.107
- **官方描述（原文）**：Improper Input Validation in the network communication processing in NEC Corporation WebSAM WinShare Ver 7.2.0 through 7.5.0, Ver 7.6.0 and Ver 7.7.0 through 7.7.2 on Windows allows a remote unauthenticated attacker to execute arbitrary commands with SYSTEM privileges via a crafted network packet sent to the computer on which WinShare is running.

### 18. CVE-2026-109900｜Melapress / Melapress Role Editor
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T16:16:36.773)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T16:16:36.773 / 2026-11-08T19:17:33.233
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in Melapress Melapress Role Editor melapress-role-editor allows Privilege Escalation.This issue affects Melapress Role Editor: from n/a through 1.3.0.

### 19. CVE-2026-107331｜IBM / DataStage on Cloud Pak for Data
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T17:16:35.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T17:16:35.550 / 2026-11-08T17:16:35.660
- **官方描述（原文）**：IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to obtain sensitive information due to an absolute-path traversal vulnerability.

### 20. CVE-2026-101117｜IBM / WebSphere Extreme Scale
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T16:16:36.103)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T16:16:36.103 / 2026-11-08T16:16:36.223
- **官方描述（原文）**：IBM WebSphere Extreme Scale 8.6.1.0 through 8.6.2.2 could allow a remote attacker to bypass security restrictions due to improper Content Security Policy configuration.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-97229｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.6522 / percentile=0.99259
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
- **EPSS**：0.18979 / percentile=0.9732
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
- **EPSS**：0.28658 / percentile=0.98151
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
- **EPSS**：0.89381 / percentile=0.99787
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
- **EPSS**：0.76566 / percentile=0.99545
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
- **EPSS**：0.81894 / percentile=0.99653
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
- **EPSS**：0.26166 / percentile=0.98006
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
- **EPSS**：0.34454 / percentile=0.98425
- **CISA KEV**：listed=true / date_added=2026-05-07 / due_date=2026-05-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ivanti Endpoint Manager Mobile (EPMM) contains an improper input validation vulnerability that allows a remotely authenticated user with administrative access to achieve remote code execution.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-48939｜iCagenda / iCagenda
- **Title**：iCagenda Unrestricted Upload of File with Dangerous Type Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.20069 / percentile=0.97464
- **CISA KEV**：listed=true / date_added=2026-07-10 / due_date=2026-07-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：iCagenda contains an unrestricted upload of file with dangerous type vulnerability that allows the upload of arbitrary files in the file attachment feature, ultimately resulting in PHP code upload and execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-48908｜JoomShaper / SP Page Builder
- **Title**：JoomShaper SP Page Builder Unrestricted Upload of File with Dangerous Type Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.89176 / percentile=0.99782
- **CISA KEV**：listed=true / date_added=2026-07-07 / due_date=2026-07-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JoomShaper SP Page Builder contains an unrestricted upload of file with dangerous type vulnerability that allows unauthenticated users to upload arbitrary files, ultimately resulting in the upload and execution of PHP code.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-6715 | WATCH / 28 | IBM / Concert | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-17466 | WATCH / 28 | IBM / Optim | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-15266 | WATCH / 28 | IBM / Concert | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124494 | WATCH / 28 | JiHong88 / suneditor | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124493 | WATCH / 28 | JiHong88 / suneditor | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124490 | WATCH / 28 | openemr / openemr | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124469 | WATCH / 28 | openemr / openemr | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124463 | WATCH / 28 | openemr / openemr | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124450 | WATCH / 28 | openemr / openemr | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124445 | WATCH / 28 | openemr / openemr | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124440 | WATCH / 28 | kyverno / kyverno | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124438 | WATCH / 28 | scriban / scriban | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124427 | WATCH / 28 | craftcms / cms | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-119506 | WATCH / 28 | DynamiApps / Frontend Admin by DynamiApps | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-114464 | WATCH / 28 | IBM / Process Mining | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-113364 | WATCH / 28 | NEC Corporation / WebSAM WinShare | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-113363 | WATCH / 28 | NEC Corporation / WebSAM WinShare | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-109900 | WATCH / 28 | Melapress / Melapress Role Editor | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-107331 | WATCH / 28 | IBM / DataStage on Cloud Pak for Data | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-101117 | WATCH / 28 | IBM / WebSphere Extreme Scale | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：20。
- EPSS 未確認：20；Exploitation status 未確認：19。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-09T07:27:59.747862+00:00`；Delta generated at：`2026-11-09T07:27:59.747862+00:00`。

---

## 可驗證資料來源

- **CVE-2026-97229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97229) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97229) · [Vendor / Advisory (ruby-lang.org)](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9586** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9586) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9586) · [Vendor / Advisory (sangomakb.atlassian.net)](https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9198) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9198) · [Vendor / Advisory (ibm.com)](https://www.ibm.com/support/pages/node/7278927) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9082) · [Vendor / Advisory (drupal.org)](https://www.drupal.org/sa-core-2026-004)
- **CVE-2026-88772** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88772) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-6715** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-6715)
- **CVE-2026-17466** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17466)
- **CVE-2026-15266** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15266)
- **CVE-2026-124494** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124494)
- **CVE-2026-124493** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124493)
- **CVE-2026-124490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124490)
- **CVE-2026-124469** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124469)
- **CVE-2026-124463** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124463)
- **CVE-2026-124450** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124450)
- **CVE-2026-124445** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124445)
- **CVE-2026-124440** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124440)
- **CVE-2026-124438** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124438)
- **CVE-2026-124427** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124427)
- **CVE-2026-119506** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119506)
- **CVE-2026-114464** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114464)
- **CVE-2026-113364** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113364)
- **CVE-2026-113363** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113363)
- **CVE-2026-109900** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109900)
- **CVE-2026-107331** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107331)
- **CVE-2026-101117** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101117)
- **CVE-2026-88771** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88771) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88771) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772)
- **CVE-2026-86950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86950) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86950) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149226) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149228) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149229) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-6973** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-6973) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-6973) · [Vendor / Advisory (hub.ivanti.com)](https://hub.ivanti.com/s/article/May-2026-Security-Advisory-Ivanti-Endpoint-Manager-Mobile-EPMM-Multiple-CVEs?language=en_US)
- **CVE-2026-48939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48939) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48939) · [Vendor / Advisory (icagenda.com)](https://www.icagenda.com/#download) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48908) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48908) · [Vendor / Advisory (extensions.joomla.org)](https://extensions.joomla.org/extension/sp-page-builder/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
