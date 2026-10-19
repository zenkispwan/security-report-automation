# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**10** 筆符合目前門檻的重要變化；事件統計：EXPLOITATION_CHANGED=1、NEW_CVE=9。
- Intelligence 候選：**30** 筆；P1 **20**、P2 **0**、P3 **0**、WATCH **10**。
- Baseline：state / generated_at=2026-10-18T05:16:38.217828+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-9082、CVE-2026-8037、CVE-2026-63030、CVE-2026-24061、CVE-2026-20230。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **10** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-14765｜Epic Games / Unreal Engine
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 12；reasons：CVSS_HIGH(+12)
- **CVSS**：v3.1 7.7 (HIGH)
- **EPSS**：0.00387 / percentile=0.31179
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T03:17:21.927 / 2026-10-18T14:16:54.843
- **官方描述（原文）**：Epic Games Unreal Engine versions up to and including 5.8.0 ship with an insecure default configuration for the LaunchURL Blueprint node (UKismetSystemLibrary::LaunchURL). The URL scheme filter (FURLRequestFilter) is empty by default, which permits all URL schemes. On Windows, this results in a call to ShellExecuteW() with the open verb, so a supplied file:/// URI causes the referenced file to be executed. Any Unreal Engine game that loads user-generated content containing Blueprints is vulnerable to command execution via a malicious local file or a remote file on a WebDAV share. This is an instance of CWE-1188 (Initialization of a Resource with an Insecure Default).

### 2. CVE-2026-112005｜clidey / whodb
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-18T12:17:12.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-18T12:17:12.790 / 2026-10-18T12:17:12.790
- **官方描述（原文）**：WhoDB 0.104.0 before 0.135.0 contains a path traversal vulnerability that allows remote attackers to read and write arbitrary host files by running DuckDB filesystem functions through the query editor. Attackers can log in to a DuckDB file without credentials and use read_text, read_blob, COPY ... TO or ATTACH to steal session.key and stored database credentials or overwrite files.

### 3. CVE-2026-111998｜vanus-labs / vanus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-18T12:17:11.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-18T12:17:11.730 / 2026-10-18T12:17:11.730
- **官方描述（原文）**：Vanus 0.8.0 through 0.9.0 contains a default credentials vulnerability that allows unauthenticated remote attackers to gain cluster-admin access by using the hardcoded admin token. Attackers can send the fixed Bearer token to the gateway gRPC proxy port to manage namespaces, eventbuses, users, tokens, and role bindings, and read or publish events.

### 4. CVE-2026-110886｜QuantumCloud / Conversational Forms for ChatBot
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-18T11:16:37.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-18T11:16:37.450 / 2026-10-18T11:16:37.450
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in QuantumCloud Conversational Forms for ChatBot conversational-forms allows Object Injection.This issue affects Conversational Forms for ChatBot: from n/a through 1.5.1.

### 5. CVE-2026-110372｜Brainstorm Force / OttoKit
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-18T11:16:36.580)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-18T11:16:36.580 / 2026-10-18T11:16:36.580
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in Brainstorm Force OttoKit suretriggers allows Privilege Escalation.This issue affects OttoKit: from n/a through 1.1.40.

### 6. CVE-2026-109894｜Arraytics / Booktics
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-18T11:16:36.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-18T11:16:36.190 / 2026-10-18T11:16:36.190
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Arraytics Booktics booktics allows SQL Injection.This issue affects Booktics: from n/a through 1.0.29.

### 7. CVE-2026-108983｜GeoVision Inc. / GV-ASManager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T02:17:05.853)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T02:17:05.853 / 2026-10-19T02:17:05.853
- **官方描述（原文）**：A vulnerability is in Web Server default connection ports under the process name GeoWebServer.exe .

### 8. CVE-2026-103091｜Google / SAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T03:16:58.377)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T03:16:58.377 / 2026-10-19T03:16:58.377
- **官方描述（原文）**：Missing Authorization (CWE-862) and Initialization of a Resource with an Insecure Default (CWE-1188) in the MCP proxy (HandleStreamPassThrough in mcp_service.go) and OIDC registration flow (GET /info and POST /register in internal/controlplane/server.go) in Google OSS Agent Mesh (SAM) versions 0.1.0-alpha.1 through 0.1.0-alpha.8 allow a remote attacker to self-enroll into the mesh and invoke arbitrary tools across all connected MCP backend nodes. Because GET /info publicly discloses OIDC configuration, POST /register auto-enrolls any valid OIDC token holder without claim filtering or ban checks, and the default policy binds sam:system:authenticated to wildcard services and targets, an attacker can obtain a mesh credential with full read, write, and execution access on backend services. Users should upgrade to version 0.1.0-alpha.9 or later, which enforces a fail-closed default policy, explicit policy-binding requirements on enrollment, and ban checks.

### 9. CVE-2026-102503｜Google / SAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T03:16:58.193)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T03:16:58.193 / 2026-10-19T03:16:58.193
- **官方描述（原文）**：Missing Authentication for Critical Function (CWE-306) and Missing Authorization (CWE-862) in the /libp2p-http ingress server (StartIngressServer in cmd/sam-node/node.go) in Google OSS Agent Mesh (SAM) versions 0.1.0-alpha.1 through 0.1.0-alpha.2 allow an unauthenticated remote libp2p peer to bypass Biscuit capability policy enforcement and invoke arbitrary registered backend services (including command/stdio-backed MCP servers, A2A, and inference endpoints). While the MCP protocol stream handler enforces WithBiscuitAuth and Authorize checks, the parallel /libp2p-http ingress routes requests directly to backend service handlers without verifying a Biscuit token or mesh enrollment. Users should upgrade to version 0.1.0-alpha.3 or later.

### 10. CVE-2026-112009｜icculus / smpeg
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-18T12:17:13.383)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-18T12:17:13.383 / 2026-10-18T13:16:36.110
- **官方描述（原文）**：smpeg through 2.0.0 contains a heap out-of-bounds read vulnerability in MPEGsystem::FillBuffer() that allows attackers to read past the 16384-byte buffer by supplying a crafted system header stream table. Attackers can provide an MPEG file whose stream table bytes all set the high bit, which crashes applications opening it through SMPEG_new, SMPEG_new_rwops, or SMPEG_new_data.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-9082｜Drupal / Core
- **Title**：Drupal Core SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.15701 / percentile=0.96825
- **CISA KEV**：listed=true / date_added=2026-05-22 / due_date=2026-05-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Drupal Core contains a SQL injection vulnerability that could allow for privilege escalation and remote code execution via specially crafted requests sent with the database abstraction API.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-8037｜Progress / LoadMaster
- **Title**：Progress LoadMaster Command Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.77362 / percentile=0.99555
- **CISA KEV**：listed=true / date_added=2026-08-07 / due_date=2026-08-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Progress LoadMaster contains a command injection vulnerability that allows an un-authenticated attacker to execute arbitrary commands on the LoadMaster appliance by exploiting unsanitized input in multiple command endpoints.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-63030｜WordPress / Core
- **Title**：WordPress Core Interpretation Conflict Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.10649 / percentile=0.95758
- **CISA KEV**：listed=true / date_added=2026-07-21 / due_date=2026-07-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WordPress Core contains an interpretation conflict vulnerability that could allow an attacker to perform SQL Injection and achieve Remote Code Execution. This vulnerability can be chained with CVE-2026-60137.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-24061｜GNU / InetUtils
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

### 5. CVE-2026-20230｜Cisco / Unified Communications Manager
- **Title**：Cisco Unified Communications Manager Server-Side Request Forgery (SSRF) Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：0.882 / percentile=0.99769
- **CISA KEV**：listed=true / date_added=2026-06-25 / due_date=2026-06-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Unified Communications Manager (Unified CM) and Cisco Unified Communications Manager Session Management Edition (Unified CM SME) contain a server-side request forgery (SSRF) Vulnerability that could allow an unauthenticated, remote attacker to write files to the underlying operating system that could be used later to elevate to root.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2025-9377｜TP-Link / Multiple Routers
- **Title**：TP-Link Archer C7(EU) and TL-WR841N/ND(MS) OS Command Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：0.37731 / percentile=0.98531
- **CISA KEV**：listed=true / date_added=2025-09-03 / due_date=2025-09-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：TP-Link Archer C7(EU) and TL-WR841N/ND(MS) contain an OS command injection vulnerability that exists in the Parental Control page. The impacted products could be end-of-life (EoL) and/or end-of-service (EoS). Users should discontinue product utilization.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2025-68613｜n8n / n8n
- **Title**：n8n Improper Control of Dynamically-Managed Code Resources Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.98994 / percentile=0.99931
- **CISA KEV**：listed=true / date_added=2026-03-11 / due_date=2026-03-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：n8n contains an improper control of dynamically managed code resources vulnerability in its workflow expression evaluation system that allows for remote code execution.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2025-64446｜Fortinet / FortiWeb
- **Title**：Fortinet FortiWeb Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.91965 / percentile=0.9982
- **CISA KEV**：listed=true / date_added=2025-11-14 / due_date=2025-11-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Fortinet FortiWeb contains a relative path traversal vulnerability that may allow an unauthenticated attacker to execute administrative commands on the system via crafted HTTP or HTTPS requests.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2025-60710｜Microsoft / Windows
- **Title**：Microsoft Windows Link Following Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.04614 / percentile=0.91572
- **CISA KEV**：listed=true / date_added=2026-04-13 / due_date=2026-04-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft Windows contains a link following vulnerability that allows for privilege escalation
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2025-58360｜OSGeo / GeoServer
- **Title**：OSGeo GeoServer Improper Restriction of XML External Entity Reference Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.60522 / percentile=0.99137
- **CISA KEV**：listed=true / date_added=2025-12-11 / due_date=2026-01-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：OSGeo GeoServer contains an improper restriction of XML external entity reference vulnerability that occurs when the application accepts XML input through a specific endpoint /geoserver/wms operation GetMap and could allow an attacker to define external entities within the XML request.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2025-58034 | P1 / 100 | Fortinet / FortiWeb | v3.1 7.2 (HIGH) | 0.5558 / percentile=0.99031 | listed=true / date_added=2025-11-18 / due_date=2025-11-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-55182 | P1 / 100 | Meta / React Server Components | v3.1 10.0 (CRITICAL) | 0.99802 / percentile=0.99958 | listed=true / date_added=2025-12-05 / due_date=2025-12-12 | status=known_exploited / source=cisa_kev | Known |
| CVE-2025-53690 | P1 / 100 | Sitecore / Multiple Products | v3.1 9.0 (CRITICAL) | 0.60601 / percentile=0.99138 | listed=true / date_added=2025-09-04 / due_date=2025-09-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-34291 | P1 / 100 | Langflow / Langflow | v4.0 9.4 (CRITICAL) | 0.92808 / percentile=0.9983 | listed=true / date_added=2026-05-21 / due_date=2026-06-04 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-3248 | P1 / 100 | Langflow / Langflow | v3.1 9.8 (CRITICAL) | 0.99993 / percentile=0.99987 | listed=true / date_added=2025-05-05 / due_date=2025-05-26 | status=known_exploited / source=cisa_kev | Known |
| CVE-2025-26399 | P1 / 100 | SolarWinds / Web Help Desk | v3.1 9.8 (CRITICAL) | 0.9012 / percentile=0.99797 | listed=true / date_added=2026-03-09 / due_date=2026-03-12 | status=known_exploited / source=cisa_kev | Known |
| CVE-2025-21042 | P1 / 100 | Samsung / Mobile Devices | v3.1 9.8 (CRITICAL) | 0.3317 / percentile=0.98354 | listed=true / date_added=2025-11-10 / due_date=2025-12-01 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-20362 | P1 / 100 | Cisco / Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense | v3.1 8.6 (HIGH) | 0.87085 / percentile=0.9975 | listed=true / date_added=2025-09-25 / due_date=2025-09-26 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-20333 | P1 / 100 | Cisco / Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense | v3.1 9.9 (CRITICAL) | 0.71207 / percentile=0.99405 | listed=true / date_added=2025-09-25 / due_date=2025-09-26 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-14611 | P1 / 100 | Gladinet / CentreStack and Triofox | v4.0 7.1 (HIGH) | 0.53302 / percentile=0.98976 | listed=true / date_added=2025-12-15 / due_date=2026-01-05 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-14765 | WATCH / 12 | Epic Games / Unreal Engine | v3.1 7.7 (HIGH) | 0.00387 / percentile=0.31179 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-112005 | WATCH / 28 | clidey / whodb | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-111998 | WATCH / 28 | vanus-labs / vanus | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-110886 | WATCH / 28 | QuantumCloud / Conversational Forms for ChatBot | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-110372 | WATCH / 28 | Brainstorm Force / OttoKit | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-109894 | WATCH / 28 | Arraytics / Booktics | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-108983 | WATCH / 28 | GeoVision Inc. / GV-ASManager | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-103091 | WATCH / 28 | Google / SAM | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-102503 | WATCH / 28 | Google / SAM | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-112009 | WATCH / 22 | icculus / smpeg | v4.0 6.8 (MEDIUM) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：10。
- EPSS 未確認：9；Exploitation status 未確認：8。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-19T05:30:26.270237+00:00`；Delta generated at：`2026-10-19T05:30:26.270237+00:00`。

---

## 可驗證資料來源

- **CVE-2026-9082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9082) · [Vendor / Advisory (drupal.org)](https://www.drupal.org/sa-core-2026-004)
- **CVE-2026-8037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-8037) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-8037) · [Vendor / Advisory (community.progress.com)](https://community.progress.com/s/article/LoadMaster-Critical-Security-Bulletin-June-2026-CVE-2026-8037-CVE-2026-33691) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-63030** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63030) · [Vendor / Advisory (wordpress.org)](https://wordpress.org/news/2026/07/wordpress-7-0-2-release/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-24061** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-24061) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-24061) · [Vendor / Advisory (cgit.git.savannah.gnu.org)](https://cgit.git.savannah.gnu.org/cgit/inetutils.git) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/ccba9f748aa8d50a38d7748e2e60362edd6a32cc) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/fd702c02497b2f398e739e3119bed0b23dd7aa7b)
- **CVE-2026-20230** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20230) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20230) · [Vendor / Advisory (cisco.com)](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssrf-cXPnHcW.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-14765** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14765) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-14765)
- **CVE-2026-112005** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112005)
- **CVE-2026-111998** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111998)
- **CVE-2026-110886** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110886)
- **CVE-2026-110372** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110372)
- **CVE-2026-109894** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109894)
- **CVE-2026-108983** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108983)
- **CVE-2026-103091** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103091)
- **CVE-2026-102503** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102503)
- **CVE-2026-112009** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112009)
- **CVE-2025-9377** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-9377) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-9377) · [Vendor / Advisory (tp-link.com)](https://www.tp-link.com/us/support/faq/4308/)
- **CVE-2025-68613** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-68613) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (github.com)](https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp)
- **CVE-2025-64446** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-64446) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-64446) · [Vendor / Advisory (fortiguard.com)](https://www.fortiguard.com/psirt/FG-IR-25-910)
- **CVE-2025-60710** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-60710) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-60710) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-60710)
- **CVE-2025-58360** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-58360) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-58360) · [Vendor / Advisory (github.com)](https://github.com/geoserver/geoserver/security/advisories/GHSA-fjf5-xgmq-5525) · [Vendor / Advisory (osgeo-org.atlassian.net)](https://osgeo-org.atlassian.net/browse/GEOS-11922)
- **CVE-2025-58034** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-58034) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-58034) · [Vendor / Advisory (fortiguard.fortinet.com)](https://fortiguard.fortinet.com/psirt/FG-IR-25-513)
- **CVE-2025-55182** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-55182) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-55182) · [Vendor / Advisory (react.dev)](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components) · [Vendor / Advisory (github.com)](https://github.com/vercel-labs/fix-react2shell-next?tab=readme-ov-file)
- **CVE-2025-53690** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-53690) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-53690) · [Vendor / Advisory (support.sitecore.com)](https://support.sitecore.com/kb?id=kb_article_view&sysparm_article=KB1003865)
- **CVE-2025-34291** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-34291) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-34291) · [Vendor / Advisory (github.com)](https://github.com/langflow-ai/langflow) · [Vendor / Advisory (github.com)](https://github.com/langflow-ai/langflow/releases/tag/v1.9.3) · [Vendor / Advisory (github.com)](https://github.com/langflow-ai/langflow/issues/11465#event-25774545848)
- **CVE-2025-3248** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-3248) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (github.com)](https://github.com/advisories/GHSA-c995-4fw3-j39m)
- **CVE-2025-26399** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-26399) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-26399) · [Vendor / Advisory (solarwinds.com)](https://www.solarwinds.com/trust-center/security-advisories/cve-2025-26399) · [Vendor / Advisory (documentation.solarwinds.com)](https://documentation.solarwinds.com/en/success_center/whd/content/release_notes/whd_12-8-7-hotfix-1_release_notes.htm)
- **CVE-2025-21042** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-21042) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-21042) · [Vendor / Advisory (security.samsungmobile.com)](https://security.samsungmobile.com/securityUpdate.smsb?year=2025&month=04)
- **CVE-2025-20362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-20362) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-20362) · [CISA](https://www.cisa.gov/news-events/directives/ed-25-03-identify-and-mitigate-potential-compromise-cisco-devices) · [CISA](https://www.cisa.gov/news-events/directives/supplemental-direction-ed-25-03-core-dump-and-hunt-instructions) · [CISA](https://www.cisa.gov/eviction-strategies-tool/create-from-template) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/resources/asa_ftd_continued_attacks) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/private/resources/asa_ftd_continued_attacks#Details) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-webvpn-YROOTUW)
- **CVE-2025-20333** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-20333) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-20333) · [CISA](https://www.cisa.gov/news-events/directives/ed-25-03-identify-and-mitigate-potential-compromise-cisco-devices) · [CISA](https://www.cisa.gov/news-events/directives/supplemental-direction-ed-25-03-core-dump-and-hunt-instructions) · [CISA](https://www.cisa.gov/eviction-strategies-tool/create-from-template) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/resources/asa_ftd_continued_attacks) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/private/resources/asa_ftd_continued_attacks#Details) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-webvpn-z5xP8EUB)
- **CVE-2025-14611** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-14611) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-14611) · [Vendor / Advisory (centrestack.com)](https://www.centrestack.com/p/gce_latest_release.html) · [Vendor / Advisory (access.triofox.com)](https://access.triofox.com/releases_history/) · [Vendor / Advisory (support.centrestack.com)](https://support.centrestack.com/hc/en-us/articles/360007159054-Hardening-the-CentreStack-Cluster#h_01JQRV57T37HJFQZKBZH9NBXQP)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
