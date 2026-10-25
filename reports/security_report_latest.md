# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**12** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=12。
- Intelligence 候選：**30** 筆；P1 **18**、P2 **0**、P3 **0**、WATCH **12**。
- Baseline：state / generated_at=2026-10-24T05:13:58.138489+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-9586、CVE-2026-9198、CVE-2026-9082、CVE-2026-8037、CVE-2026-63077。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **12** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-94075｜Tribulant Software / Newsletters
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T08:16:52.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00564 / percentile=0.46162
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T08:16:52.790 / 2026-10-24T15:17:35.387
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Tribulant Software Newsletters newsletters-lite allows Object Injection.This issue affects Newsletters: from n/a through 4.18.1.

### 2. CVE-2026-116014｜open62541 / open62541
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T12:16:57.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T12:16:57.607 / 2026-10-24T12:16:57.607
- **官方描述（原文）**：open62541 1.5.0 before 1.5.7 contains an integer overflow in UA_DataType_fromStructureDescription() that wraps the 16-bit memSize field for large custom structure definitions. A malicious OPC UA server can supply DataType definitions via UA_Client_getRemoteDataTypes(), causing decodeBinaryStructure() to overflow the heap, crashing clients or enabling code execution.

### 3. CVE-2026-115995｜Unitree Robotics / Unitree Go2
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T23:16:58.323)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T23:16:58.323 / 2026-10-24T23:16:58.323
- **官方描述（原文）**：A security vulnerability has been detected in Unitree Robotics Unitree Go2 up to 1.1.11.4. The impacted element is the function set_volume of the file gpt_thread.py of the component chat_go. Such manipulation of the argument Value leads to os command injection. The attack can be launched remotely. Upgrading to version 1.1.11.5 is sufficient to resolve this issue. You should upgrade the affected component. The vendor confirmed early: "Submission 990502 corresponds to our internal ticket #474 (Go2 chat_go set_volume OS command injection, CWE-78)."

### 4. CVE-2026-115933｜GitroomHQ / postiz-app
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T15:17:33.957)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T15:17:33.957 / 2026-10-24T15:17:33.957
- **官方描述（原文）**：Postiz signs its session, invitation and password reset tokens with one shared secret and without any marker of what a token is for. A route that refreshes the credentials of a browser-extension channel signed data taken from the request itself and stored the result where the requesting user can read it back. A user could therefore obtain a validly signed token containing any claims they choose, which the application accepts as a session, as an organization invitation with a chosen role, as a password reset or as an enterprise provisioning token. A second, narrower route that creates team invitations signs extra fields from the request body in the same way.

### 5. CVE-2026-115932｜GitroomHQ / postiz-app
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T13:16:37.217)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T13:16:37.217 / 2026-10-24T13:16:37.217
- **官方描述（原文）**：When a post is published, Postiz treats a media path that is not a web address as a file on the server's disk, but it does not check that the file lies inside the upload directory. A registered user can store a crafted media path with a post, get it past the checks that normally restrict it, and have the publishing worker read an arbitrary file and send it as an attachment to a Discord server the user controls. The same unconfined reads can be reached through two further routes. One tells the caller whether a file exists and can exhaust the backend's memory, the other delivers the file the same way as the main route. Self-registration is open by default, so the attacker needs no existing account.

### 6. CVE-2026-115806｜codexonics / Prime Mover – Backup and Migration
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T05:17:04.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00819 / percentile=0.56855
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T05:17:04.900 / 2026-10-24T05:17:04.900
- **官方描述（原文）**：The Prime Mover – Backup and Migration plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 2.2.1 via deserialization of untrusted input in the migration search-and-replace routine (recursiveUnserializeReplace()). An unauthenticated attacker can store a crafted, base64-encoded serialized object in wp_comments.comment_content through the standard comment-submission endpoint (wp-comments-post.php). When an administrator subsequently performs a routine Prime Mover export or restore, the plugin base64-decodes that stored value and passes it to unserialize() with no allowed_classes restriction. A Property-Oriented Programming (POP) chain is present in the plugin's own bundled Freemius library (FS_Clone_Manager::__set → FS_Option_Manager::set_option → store() → update_option()), so no additional plugin or theme is required — the plugin ships the gadget itself.

### 7. CVE-2026-115557｜Python Software Foundation / CPython
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T15:17:33.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T15:17:33.600 / 2026-10-25T01:16:49.377
- **官方描述（原文）**：Python has added a denylist for known compromised certificates to the "ssl" module to ensure user safety even without certificate revocation configured. Known compromised certificates will automatically be rejected regardless of the SSLContext policy configuration.

### 8. CVE-2026-114820｜Oracle Corporation / Oracle Java SE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T19:17:04.413)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T19:17:04.413 / 2026-10-25T04:17:07.843
- **官方描述（原文）**：Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition product of Oracle Java SE (component: JSSE). Supported versions that are affected are Oracle Java SE: 8u511-b32, 8u511-perf-b32, 11.0.33.0.2, 17.0.21.0.2, 21.0.13.0.2, 25.0.5.0.2, 27.0.1.0.2; Oracle GraalVM for JDK: 17.0.21.0.2 and 21.0.13.0.2; Oracle GraalVM Enterprise Edition: 21.3.20.0.2. Easily exploitable vulnerability allows unauthenticated attacker with network access via multiple protocols to compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition accessible data as well as unauthorized access to critical data or complete access to all Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition accessible data. Note: This vulnerability can be exploited by using APIs in the specified Component, e.g., through a web service which supplies data to the APIs. This vulnerability also applies to Java deployments, typically in clients running sandboxed Java Web Start applications or sandboxed Java applets, that load and run untrusted code (e.g., code that comes from the internet) and rely on the Java sandbox for security. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 9. CVE-2026-114196｜paytiumsupport / Paytium
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T08:16:51.963)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00564 / percentile=0.46167
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T08:16:51.963 / 2026-10-24T15:17:25.897
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in paytiumsupport Paytium paytium allows Object Injection.This issue affects Paytium: from n/a through 5.0.5.

### 10. CVE-2026-112866｜WPFactory / Product Filter by WBW
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T08:16:51.303)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.004 / percentile=0.33157
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T08:16:51.303 / 2026-10-24T15:17:11.433
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WPFactory Product Filter by WBW woo-product-filter allows Blind SQL Injection.This issue affects Product Filter by WBW: from n/a through 3.4.6.

### 11. CVE-2026-111402｜Tribulant Software / Newsletters
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T08:16:50.877)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.004 / percentile=0.33154
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T08:16:50.877 / 2026-10-24T15:16:55.547
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Tribulant Software Newsletters newsletters-lite allows SQL Injection.This issue affects Newsletters: from n/a through 4.18.1.

### 12. CVE-2026-110956｜Unknown / asVereinbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-24T06:16:36.010)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00186 / percentile=0.07786
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-24T06:16:36.010 / 2026-10-24T15:16:54.590
- **官方描述（原文）**：The asVereinbase WordPress plugin before 1.1.8 does not require a valid password or a genuine second factor before authenticating a user, treating an empty stored value as a match, so an unauthenticated attacker can log in as any user, including an administrator.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-9586｜Sangoma / Switchvox
- **Title**：Sangoma Switchvox SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.18979 / percentile=0.97302
- **CISA KEV**：listed=true / date_added=2026-09-02 / due_date=2026-09-05
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Sangoma Switchvox contains a SQL injection vulnerability which allows an unauthenticated remote attacker to execute arbitrary SQL statements against the backend PostgreSQL database using a single crafted request, including database operations and remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-9198｜IBM / Langflow
- **Title**：IBM Langflow Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.28658 / percentile=0.98142
- **CISA KEV**：listed=true / date_added=2026-08-04 / due_date=2026-08-07
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Langflow contains a code injection vulnerability that allows unauthenticated attackers to achieve full remote code execution on default Langflow deployments.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-9082｜Drupal / Core
- **Title**：Drupal Core SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.15701 / percentile=0.96858
- **CISA KEV**：listed=true / date_added=2026-05-22 / due_date=2026-05-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Drupal Core contains a SQL injection vulnerability that could allow for privilege escalation and remote code execution via specially crafted requests sent with the database abstraction API.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-8037｜Progress / LoadMaster
- **Title**：Progress LoadMaster Command Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.77362 / percentile=0.9956
- **CISA KEV**：listed=true / date_added=2026-08-07 / due_date=2026-08-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Progress LoadMaster contains a command injection vulnerability that allows an un-authenticated attacker to execute arbitrary commands on the LoadMaster appliance by exploiting unsanitized input in multiple command endpoints.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-63077｜JetBrains / TeamCity
- **Title**：JetBrains TeamCity Deserialization of Untrusted Data Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.8957 / percentile=0.99789
- **CISA KEV**：listed=true / date_added=2026-08-05 / due_date=2026-08-08
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JetBrains TeamCity contains a deserialization of untrusted data vulnerability that could allow unauthenticated remote code execution via the agent polling protocol.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-63030｜WordPress / Core
- **Title**：WordPress Core Interpretation Conflict Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.10649 / percentile=0.95803
- **CISA KEV**：listed=true / date_added=2026-07-21 / due_date=2026-07-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WordPress Core contains an interpretation conflict vulnerability that could allow an attacker to perform SQL Injection and achieve Remote Code Execution. This vulnerability can be chained with CVE-2026-60137.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-24061｜GNU / InetUtils
- **Title**：GNU InetUtils Argument Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.98984 / percentile=0.99931
- **CISA KEV**：listed=true / date_added=2026-01-26 / due_date=2026-02-16
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GNU InetUtils contains an argument injection vulnerability in telnetd that could allow for remote authentication bypass via a "-f root" value for the USER environment variable.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2026-21589｜Atlassian / Multiple Products
- **Title**：Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.12711 / percentile=0.96267
- **CISA KEV**：listed=true / date_added=2026-10-15 / due_date=2026-10-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Multiple Atlassian products (Bitbucket Data Center ,Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye) contain a files or directories accessible to external parties vulnerability which could allow an unauthenticated attacker to access specific files within the web application root directory in affected versions.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-20316｜Cisco / Secure Firewall Management Center (FMC)
- **Title**：Cisco Secure Firewall Management Center Use of Hard-coded Password Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_MEDIUM(+4)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.35096 / percentile=0.98442
- **CISA KEV**：listed=true / date_added=2026-07-29 / due_date=2026-08-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Secure Firewall Management Center (FMC) formerly known as Firepower Management Center contains a use of hard-coded password vulnerability that could allow an unauthenticated, remote attacker to log in to an affected device using a low-privileged account to access sensitive data within the impacted systems.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-20230｜Cisco / Unified Communications Manager
- **Title**：Cisco Unified Communications Manager Server-Side Request Forgery (SSRF) Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：0.882 / percentile=0.99771
- **CISA KEV**：listed=true / date_added=2026-06-25 / due_date=2026-06-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Unified Communications Manager (Unified CM) and Cisco Unified Communications Manager Session Management Edition (Unified CM SME) contain a server-side request forgery (SSRF) Vulnerability that could allow an unauthenticated, remote attacker to write files to the underlying operating system that could be used later to elevate to root.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-16232 | P1 / 100 | Check Point / SmartConsole | v4.0 9.3 (CRITICAL) | 0.77972 / percentile=0.99576 | listed=true / date_added=2026-07-22 / due_date=2026-07-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-15410 | P1 / 100 | SonicWall / SMA1000 Appliances | v3.1 7.2 (HIGH) | 0.11791 / percentile=0.96086 | listed=true / date_added=2026-07-14 / due_date=2026-07-17 | status=known_exploited / source=cisa_kev | Known |
| CVE-2026-15409 | P1 / 100 | SonicWall / SMA1000 Appliances | v3.1 10.0 (CRITICAL) | 0.06795 / percentile=0.93996 | listed=true / date_added=2026-07-14 / due_date=2026-07-17 | status=known_exploited / source=cisa_kev | Known |
| CVE-2025-9377 | P1 / 100 | TP-Link / Multiple Routers | v4.0 8.6 (HIGH) | 0.37731 / percentile=0.98544 | listed=true / date_added=2025-09-03 / due_date=2025-09-24 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-68613 | P1 / 100 | n8n / n8n | v3.1 8.8 (HIGH) | 0.98994 / percentile=0.99931 | listed=true / date_added=2026-03-11 / due_date=2026-03-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-64446 | P1 / 100 | Fortinet / FortiWeb | v3.1 9.8 (CRITICAL) | 0.91965 / percentile=0.99822 | listed=true / date_added=2025-11-14 / due_date=2025-11-21 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-62593 | P1 / 100 | Ray-Project / Ray | v4.0 9.4 (CRITICAL) | 0.62459 / percentile=0.9919 | listed=true / date_added=2026-08-17 / due_date=2026-08-20 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-60710 | P1 / 100 | Microsoft / Windows | v3.1 7.8 (HIGH) | 0.04614 / percentile=0.91663 | listed=true / date_added=2026-04-13 / due_date=2026-04-27 | status=known_exploited / source=cisa_kev | Known |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-94075 | WATCH / 28 | Tribulant Software / Newsletters | v3.1 9.8 (CRITICAL) | 0.00564 / percentile=0.46162 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-116014 | WATCH / 28 | open62541 / open62541 | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115995 | WATCH / 28 | Unitree Robotics / Unitree Go2 | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115933 | WATCH / 28 | GitroomHQ / postiz-app | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115932 | WATCH / 28 | GitroomHQ / postiz-app | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115806 | WATCH / 28 | codexonics / Prime Mover – Backup and Migration | v3.1 9.8 (CRITICAL) | 0.00819 / percentile=0.56855 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115557 | WATCH / 28 | Python Software Foundation / CPython | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-114820 | WATCH / 28 | Oracle Corporation / Oracle Java SE | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-114196 | WATCH / 28 | paytiumsupport / Paytium | v3.1 9.8 (CRITICAL) | 0.00564 / percentile=0.46167 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-112866 | WATCH / 28 | WPFactory / Product Filter by WBW | v3.1 9.3 (CRITICAL) | 0.004 / percentile=0.33157 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-111402 | WATCH / 28 | Tribulant Software / Newsletters | v3.1 9.3 (CRITICAL) | 0.004 / percentile=0.33154 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-110956 | WATCH / 28 | Unknown / asVereinbase | v3.1 9.8 (CRITICAL) | 0.00186 / percentile=0.07786 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：12。
- EPSS 未確認：6；Exploitation status 未確認：6。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-25T05:31:38.364189+00:00`；Delta generated at：`2026-10-25T05:31:38.364189+00:00`。

---

## 可驗證資料來源

- **CVE-2026-9586** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9586) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9586) · [Vendor / Advisory (sangomakb.atlassian.net)](https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9198) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9198) · [Vendor / Advisory (ibm.com)](https://www.ibm.com/support/pages/node/7278927) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9082) · [Vendor / Advisory (drupal.org)](https://www.drupal.org/sa-core-2026-004)
- **CVE-2026-8037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-8037) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-8037) · [Vendor / Advisory (community.progress.com)](https://community.progress.com/s/article/LoadMaster-Critical-Security-Bulletin-June-2026-CVE-2026-8037-CVE-2026-33691) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-63077** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63077) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63077) · [Vendor / Advisory (blog.jetbrains.com)](https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/) · [Vendor / Advisory (jetbrains.com)](https://www.jetbrains.com/privacy-security/issues-fixed/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-94075** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94075) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-94075)
- **CVE-2026-116014** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116014)
- **CVE-2026-115995** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115995)
- **CVE-2026-115933** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115933)
- **CVE-2026-115932** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115932)
- **CVE-2026-115806** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115806) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115806)
- **CVE-2026-115557** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115557)
- **CVE-2026-114820** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114820)
- **CVE-2026-114196** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114196) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114196)
- **CVE-2026-112866** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112866) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112866)
- **CVE-2026-111402** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111402) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111402)
- **CVE-2026-110956** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110956) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-110956)
- **CVE-2026-63030** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63030) · [Vendor / Advisory (wordpress.org)](https://wordpress.org/news/2026/07/wordpress-7-0-2-release/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-24061** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-24061) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-24061) · [Vendor / Advisory (cgit.git.savannah.gnu.org)](https://cgit.git.savannah.gnu.org/cgit/inetutils.git) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/ccba9f748aa8d50a38d7748e2e60362edd6a32cc) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/fd702c02497b2f398e739e3119bed0b23dd7aa7b)
- **CVE-2026-21589** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21589) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (confluence.atlassian.com)](https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html?ref=labs.watchtowr.com) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-20316** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20316) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20316) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-20230** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20230) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20230) · [Vendor / Advisory (cisco.com)](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssrf-cXPnHcW.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-16232** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16232) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-16232) · [Vendor / Advisory (support.checkpoint.com)](https://support.checkpoint.com/results/sk/sk185169/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-15410** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15410) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-15410) · [Vendor / Advisory (psirt.global.sonicwall.com)](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0008) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-15409** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15409) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-15409) · [Vendor / Advisory (psirt.global.sonicwall.com)](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0008) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-9377** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-9377) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-9377) · [Vendor / Advisory (tp-link.com)](https://www.tp-link.com/us/support/faq/4308/)
- **CVE-2025-68613** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-68613) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (github.com)](https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp)
- **CVE-2025-64446** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-64446) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-64446) · [Vendor / Advisory (fortiguard.com)](https://www.fortiguard.com/psirt/FG-IR-25-910)
- **CVE-2025-62593** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-62593) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-62593) · [Vendor / Advisory (github.com)](https://github.com/ray-project/ray/security/advisories/GHSA-q279-jhrf-cc6v) · [Vendor / Advisory (github.com)](https://github.com/ray-project/ray/commit/70e7c72780bdec075dba6cad1afe0832772bfe09) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-60710** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-60710) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-60710)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
