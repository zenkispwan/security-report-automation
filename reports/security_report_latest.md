# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**10** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=10、NEW_KEV=2。
- Intelligence 候選：**30** 筆；P1 **22**、P2 **0**、P3 **0**、WATCH **8**。
- Baseline：state / generated_at=2026-09-27T06:01:19.516470+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-88772、CVE-2026-88771、CVE-2026-93616、CVE-2026-85706、CVE-2026-76460。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **10** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-88772｜Citrix / NetScaler
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-27T17:16:56.390)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-27T17:16:56.390 / 2026-09-28T04:17:12.053
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service

### 2. CVE-2026-88771｜Citrix / NetScaler
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-27T17:16:56.260)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-27T17:16:56.260 / 2026-09-28T04:17:10.687
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands.

### 3. CVE-2026-88773｜Citrix NetScaler / ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-27T17:16:56.507)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-27T17:16:56.507 / 2026-09-27T17:16:56.507
- **官方描述（原文）**：Inconsistent interpretation of HTTP requests ('HTTP Request/Response smuggling') vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway. This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1-37.279 and NDcPP; Gateway: before 14.1-73.37 FIPS and before 13.1-64.23.

### 4. CVE-2026-101090｜nezhahq / nezha
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-27T21:17:03.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-27T21:17:03.003 / 2026-09-27T21:17:03.003
- **官方描述（原文）**：Nezha 2.2.3 contains a Host header injection regression in the OAuth2 redirect endpoint. When the new optional dashboard_host setting is empty, /api/v1/oauth2/{provider} (cmd/dashboard/controller/oauth2.go) reflects the attacker-supplied HTTP Host header into the redirect_uri sent to the identity provider instead of falling back to the configured install_host. An attacker who induces a victim to begin OAuth2 login via a request that reaches Nezha with a forged Host header can cause an attacker-controlled callback URL to be used as the redirect_uri; if the OAuth2 provider accepts it, the victim's authorization code is delivered to the attacker origin, allowing the attacker to complete the OAuth2 login/binding flow and take over the account. This regresses the fix for GHSA-9rc6-8cjv-rcvx and is configuration-dependent (dashboard_host empty). At the time of the advisory no patched version was available.

### 5. CVE-2026-101084｜obot-platform / obot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-27T21:17:02.163)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-27T21:17:02.163 / 2026-09-27T21:17:02.163
- **官方描述（原文）**：obot versions before v0.21.1 fail to enforce Access Control Rules on the /mcp-connect endpoint, allowing any authenticated user to connect to restricted MCP servers if they possess the server ID. Attackers can bypass authorization checks to access and manipulate sensitive backend systems through MCP tool calls using stored OAuth credentials.

### 6. CVE-2026-101065｜obot-platform / obot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-27T21:17:02.027)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-27T21:17:02.027 / 2026-09-27T21:17:02.027
- **官方描述（原文）**：Obot is an open-source AI agent/MCP platform. In all versions up to and including commit d7e6970, the Docker quickstart command documented in the README starts the container listening on 0.0.0.0:8080 with authentication disabled by default. When authentication is disabled, every request is mapped to a synthetic "nobody" user that holds the Owner and Admin roles, so any unauthenticated party who can reach the exposed port obtains full administrative access to the Obot API and UI, including the ability to register and launch attacker-controlled MCP servers. Because the quickstart also mounts /var/run/docker.sock into the container, the MCP runtime backend reachable this way has access to the host's Docker control surface. The fix is documentation-only: the quickstart now enables authentication, and operators who followed the previous instructions should set OBOT_SERVER_ENABLE_AUTHENTICATION=true before exposing the host to any untrusted network.

### 7. CVE-2026-101001｜Netcore / NBR200V2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T05:16:30.570)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T05:16:30.570 / 2026-09-28T05:16:30.570
- **官方描述（原文）**：A vulnerability was identified in Netcore NBR200V2 1.3.241127.071246. This impacts the function eval of the file /www/cgi-bin/network_tools of the component Web Management Interface. Such manipulation of the argument QUERY_STRING leads to os command injection. It is possible to launch the attack remotely. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 8. CVE-2026-101000｜Netcore / NBR100V2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T05:16:30.270)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T05:16:30.270 / 2026-09-28T05:16:30.270
- **官方描述（原文）**：A vulnerability was determined in Netcore NBR100V2 1.3.240614.030928. This affects the function uci.apply of the file /usr/share/rpcd/acl.d/unauthenticated.json of the component ACL Handler. This manipulation of the argument section causes missing authorization. It is possible to initiate the attack remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 9. CVE-2026-100886｜Seetong / T8108
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-27T23:16:59.020)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-27T23:16:59.020 / 2026-09-27T23:16:59.020
- **官方描述（原文）**：A vulnerability was identified in Seetong T8108, T8108P, T8116 and T8232 4.6.1.4-build202604241011. The affected element is an unknown function of the component Debug Service. Such manipulation leads to improper authentication. The attack may be launched remotely. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 10. CVE-2026-100741｜Progressive Robot Ltd / hMailServer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-27T08:16:26.813)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01729 / percentile=0.76662
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-27T08:16:26.813 / 2026-09-27T08:16:26.813
- **官方描述（原文）**：Eval injection in the JScript event-script dispatcher in Progressive Robot Ltd's hMailServer, versions 6.0.0 through 6.3.3 on Windows, allows a remote, unauthenticated attacker to run arbitrary JScript inside the hMailServer service process, with the privileges of the service account, via a password containing a backslash followed by an apostrophe, sent in any logon (SMTP AUTH, POP3, IMAP) that names an existing, active account. Exploitation requires a non-default configuration: event scripting enabled (off by default), the script language set to JScript (the default is VBScript), and an OnClientValidatePassword handler defined in the event script. The server wrote event values into the handler call as JScript string literals, escaping the apostrophe but not the backslash, so such a value closes the literal and the rest of it is parsed as script. The same flaw is reachable by a remote POP3 server through the message UID it returns, where an OnExternalAccountDownload handler is defined, and by a remote SMTP server through the error reply it rejects a delivery with, where an OnDeliveryFailed handler is defined. Before 6.2.25 the injected script can create any COM object, and from 6.2.25 it can with the default ScriptAllowedObjects value of '*'; WScript.Shell among them gives command execution as the service account. VBScript event scripts and the Linux builds of Progressive Robot Ltd's hMailServer are not affected.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-88772｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-88771｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Input Validation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-93616｜Check Point / Multiple Products
- **Title**：Check Point Multiple Products Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.19654 / percentile=0.97309
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Check Point Security Management Server, Multi-Domain Security Management Server, Log Server, Multi-Domain Log Server, and SmartEvent contain a path traversal vulnerability that allows an unauthenticated attacker to upload and execute arbitrary scripts.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-85706｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.91425 / percentile=0.99811
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contains a path traversal vulnerability that allows an unauthenticated user to read arbitrary files due to an improper path confinement and missing authentication enforcement in the repository commits API.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-76460｜Cisco / Identity Services Engine
- **Title**：Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.14026 / percentile=0.96436
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) contain an incorrect use of privileged APIs vulnerability that could allow an unauthenticated, remote attacker to gain unauthorized access to the affected device by bypassing the web-based management interface.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-71362｜Adobe / Commerce and Magento
- **Title**：Adobe Commerce and Magento Incorrect Authorization Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.87507 / percentile=0.99754
- **CISA KEV**：listed=true / date_added=2026-09-24 / due_date=2026-09-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Adobe Commerce and Magento contains an incorrect authorization vulnerability that could allow an attacker to leverage this vulnerability to gain elevated access to sensitive resources without any user interaction.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2025-57819｜Sangoma / FreePBX
- **Title**：Sangoma FreePBX Authentication Bypass Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.85463 / percentile=0.99716
- **CISA KEV**：listed=true / date_added=2025-08-29 / due_date=2025-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Sangoma FreePBX contains an authentication bypass vulnerability due to insufficiently sanitized user-supplied data allows unauthenticated access to FreePBX Administrator leading to arbitrary database manipulation and remote code execution.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2025-32432｜Craft CMS / Craft CMS
- **Title**：Craft CMS Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.99785 / percentile=0.99955
- **CISA KEV**：listed=true / date_added=2026-03-20 / due_date=2026-04-03
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Craft CMS contains a code injection vulnerability that allows a remote attacker to execute arbitrary code.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2025-30066｜tj-actions / changed-files GitHub Action
- **Title**：tj-actions/changed-files GitHub Action Embedded Malicious Code Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：0.72092 / percentile=0.99415
- **CISA KEV**：listed=true / date_added=2025-03-18 / due_date=2025-04-08
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：tj-actions/changed-files GitHub Action contains an embedded malicious code vulnerability that allows a remote attacker to discover secrets by reading Github Actions Workflow Logs. These secrets may include, but are not limited to, valid AWS access keys, GitHub personal access tokens (PATs), npm tokens, and private RSA keys.
- **CISA Required Action（原文）**：Apply mitigations as set forth in the CISA instructions linked below. Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2025-26633｜Microsoft / Windows
- **Title**：Microsoft Windows Management Console (MMC) Improper Neutralization Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 7.0 (HIGH)
- **EPSS**：0.30391 / percentile=0.98177
- **CISA KEV**：listed=true / date_added=2025-03-11 / due_date=2025-04-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft Windows Management Console (MMC) contains an improper neutralization vulnerability that allows an unauthorized attacker to bypass a security feature locally.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2025-23006 | P1 / 100 | SonicWall / SMA1000 Appliances | v3.1 9.8 (CRITICAL) | 0.23432 / percentile=0.97721 | listed=true / date_added=2025-01-24 / due_date=2025-02-14 | status=known_exploited / source=cisa_kev | Known |
| CVE-2025-20352 | P1 / 100 | Cisco / IOS and IOS XE | v3.1 7.7 (HIGH) | 0.39447 / percentile=0.98564 | listed=true / date_added=2025-09-29 / due_date=2025-10-20 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-87902 | P1 / 95 | WordPress / Core | v3.1 8.1 (HIGH) | 0.18166 / percentile=0.97112 | listed=true / date_added=2026-09-25 / due_date=2026-09-28 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-6558 | P1 / 95 | Google / Chromium | v3.1 8.8 (HIGH) | 0.09585 / percentile=0.95314 | listed=true / date_added=2025-07-22 / due_date=2025-08-12 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-65400 | P1 / 90 | Apple / macOS | v3.1 9.8 (CRITICAL) | 0.01219 / percentile=0.67448 | listed=true / date_added=2026-08-18 / due_date=2026-08-21 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-5430 | P1 / 90 | WSO2 / Multiple Products | v3.1 10.0 (CRITICAL) | 0.00588 / percentile=0.45981 | listed=true / date_added=2026-09-24 / due_date=2026-09-27 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-33824 | P1 / 90 | Microsoft / Internet Key Exchange (IKE) Service Extensions | v3.1 9.8 (CRITICAL) | 0.01619 / percentile=0.75102 | listed=true / date_added=2026-08-18 / due_date=2026-08-21 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-59374 | P1 / 90 | ASUS / Live Update | v4.0 9.3 (CRITICAL) | 0.01197 / percentile=0.66879 | listed=true / date_added=2025-12-17 / due_date=2026-01-07 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-42599 | P1 / 90 | Qualitia / Active! Mail | v3.1 9.8 (CRITICAL) | 0.03298 / percentile=0.88062 | listed=true / date_added=2025-04-28 / due_date=2025-05-19 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-87491 | P1 / 82 | Google / Chromium V8 | v3.1 8.8 (HIGH) | 0.03142 / percentile=0.87416 | listed=true / date_added=2026-09-09 / due_date=2026-09-23 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-85880 | P1 / 82 | Microsoft / Windows | v3.1 7.8 (HIGH) | 0.03616 / percentile=0.89097 | listed=true / date_added=2026-09-08 / due_date=2026-09-22 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-7273 | P1 / 82 | Zyxel / GS1900 Series Switches | v3.1 8.8 (HIGH) | 0.02501 / percentile=0.84081 | listed=true / date_added=2026-09-21 / due_date=2026-09-24 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-88773 | WATCH / 28 | Citrix NetScaler / ADC | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-101090 | WATCH / 28 | nezhahq / nezha | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-101084 | WATCH / 28 | obot-platform / obot | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-101065 | WATCH / 28 | obot-platform / obot | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-101001 | WATCH / 28 | Netcore / NBR200V2 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-101000 | WATCH / 28 | Netcore / NBR100V2 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-100886 | WATCH / 28 | Seetong / T8108 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-100741 | WATCH / 28 | Progressive Robot Ltd / hMailServer | v3.1 9.8 (CRITICAL) | 0.01729 / percentile=0.76662 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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
- EPSS 未確認：9；Exploitation status 未確認：8。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-28T06:07:26.258680+00:00`；Delta generated at：`2026-09-28T06:07:26.258680+00:00`。

---

## 可驗證資料來源

- **CVE-2026-88772** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-88771** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88771) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772)
- **CVE-2026-93616** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93616) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93616) · [Vendor / Advisory (support.checkpoint.com)](https://support.checkpoint.com/results/sk/sk1000171/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85706) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85706) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-76460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76460) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-88773** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88773)
- **CVE-2026-101090** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101090)
- **CVE-2026-101084** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101084)
- **CVE-2026-101065** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101065)
- **CVE-2026-101001** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101001)
- **CVE-2026-101000** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101000)
- **CVE-2026-100886** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100886)
- **CVE-2026-100741** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100741) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-100741)
- **CVE-2026-71362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71362) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-71362) · [Vendor / Advisory (helpx.adobe.com)](https://helpx.adobe.com/security/products/magento/apsb26-92.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-57819** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-57819) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-57819) · [Vendor / Advisory (github.com)](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-m42g-xg4c-5f3h)
- **CVE-2025-32432** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-32432) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-32432) · [Vendor / Advisory (craftcms.com)](https://craftcms.com/knowledge-base/craft-cms-cve-2025-32432) · [Vendor / Advisory (github.com)](https://github.com/craftcms/cms/security/advisories/GHSA-f3gw-9ww9-jmc3)
- **CVE-2025-30066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-30066) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [CISA](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction) · [Vendor / Advisory (github.com)](https://github.com/tj-actions/changed-files/blob/45fb12d7a8bedb4da42342e52fe054c6c2c3fd73/README.md?plain=1#L20-L28)
- **CVE-2025-26633** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-26633) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-26633) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-26633)
- **CVE-2025-23006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-23006) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-23006) · [Vendor / Advisory (psirt.global.sonicwall.com)](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0002)
- **CVE-2025-20352** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-20352) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-20352) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snmp-x4LPhte)
- **CVE-2026-87902** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87902) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (github.com)](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-6558** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-6558) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-6558) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2025/07/stable-channel-update-for-desktop_15.html)
- **CVE-2026-65400** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65400) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65400) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148170) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148171) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148172) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-5430** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-5430) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-5430) · [Vendor / Advisory (security.docs.wso2.com)](https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-33824** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-33824) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-33824) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33824) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-59374** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-59374) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-59374) · [Vendor / Advisory (asus.com)](https://www.asus.com/support/faq/1018727/)
- **CVE-2025-42599** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-42599) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-42599) · [Vendor / Advisory (qualitia.com)](https://www.qualitia.com/jp/news/2025/04/18_1030.html)
- **CVE-2026-87491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87491) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87491) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85880** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85880) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85880) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-7273** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-7273) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-7273) · [Vendor / Advisory (zyxel.com)](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
