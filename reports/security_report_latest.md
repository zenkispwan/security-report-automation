# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**4** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=4。
- Intelligence 候選：**30** 筆；P1 **26**、P2 **0**、P3 **0**、WATCH **4**。
- Baseline：state / generated_at=2026-10-03T05:54:47.637906+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-87902、CVE-2026-8037、CVE-2026-64849、CVE-2026-41940、CVE-2026-24061。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **4** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-92084｜beaverbuilder / Beaver Builder Page Builder – Drag and Drop Website Builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-03T08:16:26.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00531 / percentile=0.42877
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-03T08:16:26.990 / 2026-10-03T16:16:41.610
- **官方描述（原文）**：The The Beaver Builder Page Builder – Drag and Drop Website Builder plugin for WordPress is vulnerable to arbitrary shortcode execution in all versions up to, and including, 2.11.0.5. This is due to the software allowing users to execute an action that does not properly validate a value before running do_shortcode. This makes it possible for unauthenticated attackers to execute arbitrary shortcodes. Exploitation requires the target site to have a Beaver Builder page containing the Sidebar module populated with a widget that displays attacker-controllable text, such as the core Recent Comments widget, with comment moderation disabled or the attacker's comment approved.

### 2. CVE-2026-87115｜e4jvikwp / VikAppointments Services Booking Calendar
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-03T07:16:48.347)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00881 / percentile=0.57736
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-03T07:16:48.347 / 2026-10-03T16:16:40.057
- **官方描述（原文）**：The VikAppointments Services Booking Calendar plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient file path validation in the extract function in all versions up to, and including, 1.2.21. This makes it possible for unauthenticated attackers to delete arbitrary files on the server, which can easily lead to remote code execution when the right file is deleted (such as wp-config.php). Exploitation requires at least one File-type custom field to be published on the confirmation page shortcode, as this field is not created by default during plugin installation.

### 3. CVE-2026-71885｜Legion of the Bouncy Castle Inc. / BC-JAVA
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-03T09:17:04.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00188 / percentile=0.07555
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-03T09:17:04.730 / 2026-10-03T09:17:04.730
- **官方描述（原文）**：In Bouncy Castle for Java before 1.86, the Messaging Layer Security (MLS, RFC 9420) implementation did not bind an X.509 credential to a LeafNode's signature_key. LeafNode.verify() checked a leaf's signature against the signature_key carried in the leaf itself, while the credential's X.509 certificate chain was stored but never parsed or validated, so the end-entity certificate's public key was never required to match signature_key as RFC 9420 sec. 5.3 requires. A party could therefore present another party's certificate as its credential while signing the leaf, and the enclosing KeyPackage, with an unrelated key, and be accepted under that other party's identity through KeyPackage.verify() and the Group leaf-validation path. In a deployment that admits external commits without an independent credential-admission check, an unauthenticated attacker could be admitted under a victim's X.509 identity, evict the victim (resynchronization compares whole credentials rather than signing keys), derive the current epoch, decrypt subsequent group messages, and send messages accepted as the victim. TreeKEM.LeafNode now requires the end-entity certificate's subject public key, in the cipher suite's signature encoding, to equal signature_key for an X.509 credential and rejects the leaf otherwise, including an empty chain or a certificate whose key type does not match the cipher suite; certificate-chain and identity validation to a trust anchor remain the application's responsibility per RFC 9420 sec. 5.3.1. Deployments using only basic credentials are unaffected.

### 4. CVE-2026-105105｜NASA-AMMOS / AIT-Core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-03T12:16:57.183)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-03T12:16:57.183 / 2026-10-03T16:16:35.200
- **官方描述（原文）**：CWE-306: Missing Authentication for Critical Function in the ait.core.server telemetry and command broker (ait-server) in NASA-AMMOS AIT-Core through 3.1.1 allows an unauthenticated remote attacker with network access to the ZeroMQ message bus to inject spacecraft command data, exfiltrate command and telemetry traffic, inject forged telemetry, or disrupt the command and telemetry bus. The ait-server ZeroMQ broker binds its XSUB and XPUB sockets to all network interfaces by default without authentication or transport security. An attacker able to reach TCP port 5559 can publish messages onto internal topics, including the __commands__ command topic. With the shipped default configuration, command messages are forwarded through command_stream and emitted on the command-uplink UDP path. An attacker able to reach TCP port 5560 can subscribe to command and telemetry traffic on the ground bus. AIT-Core 3.1.2 changes the default ZeroMQ bind addresses to loopback.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-87902｜WordPress / Core
- **Title**：WordPress Core Remote File Inclusion Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.45501 / percentile=0.98757
- **CISA KEV**：listed=true / date_added=2026-09-25 / due_date=2026-09-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WordPress Core contains a remote file inclusion vulnerability which could allow an unauthenticated attacker to make page-template resolution include a chosen readable local `.php` file outside the active theme directories, leading to remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-8037｜Progress / LoadMaster
- **Title**：Progress LoadMaster Command Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.77362 / percentile=0.99546
- **CISA KEV**：listed=true / date_added=2026-08-07 / due_date=2026-08-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Progress LoadMaster contains a command injection vulnerability that allows an un-authenticated attacker to execute arbitrary commands on the LoadMaster appliance by exploiting unsanitized input in multiple command endpoints.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-64849｜MLflow / MLflow
- **Title**：MLflow Server-Side Request Forgery Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.09839 / percentile=0.95427
- **CISA KEV**：listed=true / date_added=2026-08-19 / due_date=2026-09-02
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：MLflow contains a server-side request forgery vulnerability that can allow attackers to reach internal or cloud metadata services and receive response_status and response_body.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-41940｜WebPros / cPanel & WHM and WP2 (WordPress Squared)
- **Title**：WebPros cPanel & WHM and WP2 (WordPress Squared) Missing Authentication for Critical Function Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.98527 / percentile=0.9992
- **CISA KEV**：listed=true / date_added=2026-04-30 / due_date=2026-05-03
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WebPros cPanel & WHM (WebHost Manager) and WP2 (WordPress Squared) contain an authentication bypass vulnerability in the login flow that allows unauthenticated remote attackers to gain unauthorized access to the control panel.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-24061｜GNU / InetUtils
- **Title**：GNU InetUtils Argument Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.98984 / percentile=0.9993
- **CISA KEV**：listed=true / date_added=2026-01-26 / due_date=2026-02-16
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GNU InetUtils contains an argument injection vulnerability in telnetd that could allow for remote authentication bypass via a "-f root" value for the USER environment variable.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2025-62593｜Ray-Project / Ray
- **Title**：Ray-Project Ray Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.62459 / percentile=0.99167
- **CISA KEV**：listed=true / date_added=2026-08-17 / due_date=2026-08-20
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ray-Project Ray contains a code injection vulnerability that could allow remote code execution. Developers using Ray as a development tool may be exposed to this vulnerability exploitable through Firefox and Safari.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2025-21042｜Samsung / Mobile Devices
- **Title**：Samsung Mobile Devices Out-of-Bounds Write Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.3317 / percentile=0.98323
- **CISA KEV**：listed=true / date_added=2025-11-10 / due_date=2025-12-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Samsung mobile devices contain an out-of-bounds write vulnerability in libimagecodec.quram.so. This vulnerability could allow remote attackers to execute arbitrary code.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2025-14174｜Google / Chromium
- **Title**：Google Chromium Out of Bounds Memory Access Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.22327 / percentile=0.97626
- **CISA KEV**：listed=true / date_added=2025-12-12 / due_date=2026-01-02
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium contains an out of bounds memory access vulnerability in ANGLE that could allow a remote attacker to perform out of bounds memory access via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2025-0282｜Ivanti / Connect Secure, Policy Secure, and ZTA Gateways
- **Title**：Ivanti Connect Secure, Policy Secure, and ZTA Gateways Stack-Based Buffer Overflow Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：0.99979 / percentile=0.9998
- **CISA KEV**：listed=true / date_added=2025-01-08 / due_date=2025-01-15
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ivanti Connect Secure, Policy Secure, and ZTA Gateways contain a stack-based buffer overflow which can lead to unauthenticated remote code execution.
- **CISA Required Action（原文）**：Apply mitigations as set forth in the CISA instructions linked below to include conducting hunt activities, taking remediation actions if applicable, and applying updates prior to returning a device to service.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2024-9379｜Ivanti / Cloud Services Appliance (CSA)
- **Title**：Ivanti Cloud Services Appliance (CSA) SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 7.2 (HIGH)
- **EPSS**：0.43782 / percentile=0.9871
- **CISA KEV**：listed=true / date_added=2024-10-09 / due_date=2024-10-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ivanti Cloud Services Appliance (CSA) contains a SQL injection vulnerability in the admin web console in versions prior to 5.0.2, which can allow a remote attacker authenticated as administrator to run arbitrary SQL statements.
- **CISA Required Action（原文）**：As Ivanti CSA 4.6.x has reached End-of-Life status, users are urged to remove CSA 4.6.x from service or upgrade to the 5.0.x line, or later, of supported solution.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2024-7399 | P1 / 100 | Samsung / MagicINFO 9 Server | v3.1 9.8 (CRITICAL) | 0.91941 / percentile=0.99818 | listed=true / date_added=2026-04-24 / due_date=2026-05-08 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2023-46805 | P1 / 100 | Ivanti / Connect Secure and Policy Secure | v3.1 8.2 (HIGH) | 0.99986 / percentile=0.99983 | listed=true / date_added=2024-01-10 / due_date=2024-01-22 | status=known_exploited / source=cisa_kev | Known |
| CVE-2023-27351 | P1 / 100 | PaperCut / NG/MF | v3.1 7.5 (HIGH) | 0.78052 / percentile=0.99566 | listed=true / date_added=2026-04-20 / due_date=2026-05-04 | status=known_exploited / source=cisa_kev | Known |
| CVE-2022-30333 | P1 / 100 | RARLAB / UnRAR | v3.1 7.5 (HIGH) | 未確認 | listed=true / date_added=2022-08-09 / due_date=2022-08-30 | status=known_exploited / source=cisa_kev | Known |
| CVE-2022-27925 | P1 / 100 | Synacor / Zimbra Collaboration Suite (ZCS) | v3.1 7.2 (HIGH) | 0.98676 / percentile=0.99923 | listed=true / date_added=2022-08-11 / due_date=2022-09-01 | status=known_exploited / source=cisa_kev | Known |
| CVE-2022-27924 | P1 / 100 | Synacor / Zimbra Collaboration Suite (ZCS) | v3.1 7.5 (HIGH) | 未確認 | listed=true / date_added=2022-08-04 / due_date=2022-08-25 | status=known_exploited / source=cisa_kev | Known |
| CVE-2021-27065 | P1 / 100 | Microsoft / Exchange Server | v3.1 7.8 (HIGH) | 0.99876 / percentile=0.99963 | listed=true / date_added=2021-11-03 / due_date=2022-05-03 | status=known_exploited / source=cisa_kev | Known |
| CVE-2021-26858 | P1 / 100 | Microsoft / Exchange Server | v3.1 7.8 (HIGH) | 0.93651 / percentile=0.99841 | listed=true / date_added=2021-11-03 / due_date=2022-05-03 | status=known_exploited / source=cisa_kev | Known |
| CVE-2021-26411 | P1 / 100 | Microsoft / Internet Explorer | v3.1 8.8 (HIGH) | 0.80765 / percentile=0.9962 | listed=true / date_added=2021-11-03 / due_date=2021-11-17 | status=known_exploited / source=cisa_kev | Known |
| CVE-2021-22175 | P1 / 100 | GitLab / GitLab | v3.1 9.8 (CRITICAL) | 0.53372 / percentile=0.98959 | listed=true / date_added=2026-02-18 / due_date=2026-03-11 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2021-22054 | P1 / 100 | Omnissa / Workspace One UEM | v3.1 7.5 (HIGH) | 0.99677 / percentile=0.9995 | listed=true / date_added=2026-03-09 / due_date=2026-03-23 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2021-21975 | P1 / 100 | VMware / vRealize Operations Manager API | v3.1 7.5 (HIGH) | 未確認 | listed=true / date_added=2022-01-18 / due_date=2022-02-01 | status=known_exploited / source=cisa_kev | Known |
| CVE-2021-20023 | P1 / 100 | SonicWall / SonicWall Email Security | v3.1 4.9 (MEDIUM) | 0.51407 / percentile=0.98912 | listed=true / date_added=2021-11-03 / due_date=2021-11-17 | status=known_exploited / source=cisa_kev | Known |
| CVE-2021-20022 | P1 / 100 | SonicWall / SonicWall Email Security | v3.1 7.2 (HIGH) | 0.16509 / percentile=0.9691 | listed=true / date_added=2021-11-03 / due_date=2021-11-17 | status=known_exploited / source=cisa_kev | Known |
| CVE-2020-12812 | P1 / 100 | Fortinet / FortiOS | v3.1 9.8 (CRITICAL) | 未確認 | listed=true / date_added=2021-11-03 / due_date=2022-05-03 | status=known_exploited / source=cisa_kev | Known |
| CVE-2020-0796 | P1 / 100 | Microsoft / SMBv3 | v3.1 10.0 (CRITICAL) | 0.9981 / percentile=0.99958 | listed=true / date_added=2022-02-10 / due_date=2022-08-10 | status=known_exploited / source=cisa_kev | Known |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-92084 | WATCH / 28 | beaverbuilder / Beaver Builder Page Builder – Drag and Drop Website Builder | v3.1 9.1 (CRITICAL) | 0.00531 / percentile=0.42877 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-87115 | WATCH / 28 | e4jvikwp / VikAppointments Services Booking Calendar | v3.1 9.1 (CRITICAL) | 0.00881 / percentile=0.57736 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-71885 | WATCH / 28 | Legion of the Bouncy Castle Inc. / BC-JAVA | v4.0 9.2 (CRITICAL) | 0.00188 / percentile=0.07555 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105105 | WATCH / 28 | NASA-AMMOS / AIT-Core | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：4。
- EPSS 未確認：5；Exploitation status 未確認：1。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-04T06:31:45.846349+00:00`；Delta generated at：`2026-10-04T06:31:45.846349+00:00`。

---

## 可驗證資料來源

- **CVE-2026-87902** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87902) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87902) · [Vendor / Advisory (github.com)](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-8037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-8037) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-8037) · [Vendor / Advisory (community.progress.com)](https://community.progress.com/s/article/LoadMaster-Critical-Security-Bulletin-June-2026-CVE-2026-8037-CVE-2026-33691) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-64849** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-64849) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-64849) · [Vendor / Advisory (github.com)](https://github.com/mlflow/mlflow/pull/24258) · [Vendor / Advisory (github.com)](https://github.com/mlflow/mlflow/issues/24179) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-41940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-41940) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-41940) · [Vendor / Advisory (support.cpanel.net)](https://support.cpanel.net/hc/en-us/articles/40073787579671-cPanel-WHM-Security-Update-04-28-2026) · [Vendor / Advisory (docs.cpanel.net)](https://docs.cpanel.net/release-notes/release-notes/) · [Vendor / Advisory (docs.wpsquared.com)](https://docs.wpsquared.com/changelogs/versions/changelog/#13617)
- **CVE-2026-24061** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-24061) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-24061) · [Vendor / Advisory (cgit.git.savannah.gnu.org)](https://cgit.git.savannah.gnu.org/cgit/inetutils.git) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/ccba9f748aa8d50a38d7748e2e60362edd6a32cc) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/fd702c02497b2f398e739e3119bed0b23dd7aa7b)
- **CVE-2026-92084** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92084) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-92084)
- **CVE-2026-87115** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87115) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87115)
- **CVE-2026-71885** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71885) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-71885)
- **CVE-2026-105105** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105105)
- **CVE-2025-62593** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-62593) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-62593) · [Vendor / Advisory (github.com)](https://github.com/ray-project/ray/security/advisories/GHSA-q279-jhrf-cc6v) · [Vendor / Advisory (github.com)](https://github.com/ray-project/ray/commit/70e7c72780bdec075dba6cad1afe0832772bfe09) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-21042** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-21042) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-21042) · [Vendor / Advisory (security.samsungmobile.com)](https://security.samsungmobile.com/securityUpdate.smsb?year=2025&month=04)
- **CVE-2025-14174** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-14174) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-14174) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2025/12/stable-channel-update-for-desktop_10.html) · [Vendor / Advisory (learn.microsoft.com)](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security)
- **CVE-2025-0282** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-0282) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-0282) · [CISA](https://www.cisa.gov/cisa-mitigation-instructions-CVE-2025-0282) · [Vendor / Advisory (forums.ivanti.com)](https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-Policy-Secure-ZTA-Gateways-CVE-2025-0282-CVE-2025-0283)
- **CVE-2024-9379** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-9379) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2024-9379) · [Vendor / Advisory (forums.ivanti.com)](https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-CSA-Cloud-Services-Appliance-CVE-2024-9379-CVE-2024-9380-CVE-2024-9381)
- **CVE-2024-7399** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-7399) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2024-7399) · [Vendor / Advisory (security.samsungtv.com)](https://security.samsungtv.com/securityUpdates)
- **CVE-2023-46805** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-46805) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-46805) · [Vendor / Advisory (forums.ivanti.com)](https://forums.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways?language=en_US)
- **CVE-2023-27351** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-27351) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-27351) · [Vendor / Advisory (papercut.com)](https://www.papercut.com/kb/Main/PO-1216-and-PO-1219)
- **CVE-2022-30333** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-30333) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (rarlab.com)](https://www.rarlab.com/rar/rarlinux-x32-612.tar.gz)
- **CVE-2022-27925** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-27925) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2022-27925) · [Vendor / Advisory (blog.zimbra.com)](https://blog.zimbra.com/2022/08/authentication-bypass-in-mailboximportservlet-vulnerability/)
- **CVE-2022-27924** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-27924) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (wiki.zimbra.com)](https://wiki.zimbra.com/wiki/Zimbra_Releases/9.0.0/P24.1#Security_Fixes)
- **CVE-2021-27065** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-27065) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2021-27065) · [CISA](https://www.cisa.gov/news-events/directives/ed-21-02-mitigate-microsoft-exchange-premises-product-vulnerabilities)
- **CVE-2021-26858** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-26858) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2021-26858) · [CISA](https://www.cisa.gov/news-events/directives/ed-21-02-mitigate-microsoft-exchange-premises-product-vulnerabilities)
- **CVE-2021-26411** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-26411) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2021-26411)
- **CVE-2021-22175** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-22175) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2021-22175) · [Vendor / Advisory (gitlab.com)](https://gitlab.com/gitlab-org/cves/-/blob/master/2021/CVE-2021-22175.json)
- **CVE-2021-22054** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-22054) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2021-22054) · [Vendor / Advisory (web.archive.org)](https://web.archive.org/web/20211222154335/https://www.vmware.com/security/advisories/VMSA-2021-0029.html)
- **CVE-2021-21975** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-21975) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- **CVE-2021-20023** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-20023) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2021-20023)
- **CVE-2021-20022** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-20022) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2021-20022)
- **CVE-2020-12812** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-12812) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- **CVE-2020-0796** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-0796) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2020-0796)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
