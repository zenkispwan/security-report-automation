# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**17** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=16、NEW_KEV=1。
- Intelligence 候選：**30** 筆；P1 **14**、P2 **0**、P3 **0**、WATCH **16**。
- Baseline：state / generated_at=2026-10-04T06:31:45.846349+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-88779、CVE-2026-87902、CVE-2026-8037、CVE-2026-64849、CVE-2026-41940。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **17** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-88779｜Citrix / NetScaler
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.00276 / percentile=0.18203
- **CISA KEV**：listed=true / date_added=2026-10-04 / due_date=2026-10-07
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-04T04:16:43.680 / 2026-10-05T04:17:08.547
- **官方描述（原文）**：Citrix NetScaler ADC (formerly Citrix ADC) and Citrix NetScaler Gateway (formerly Citrix Gateway) contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for a denial of service.

### 2. CVE-2026-105294｜Legcord / Legcord
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T01:16:28.923)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T01:16:28.923 / 2026-10-05T01:16:28.923
- **官方描述（原文）**：Legcord 1.1.0 through 1.3.0 contains a configuration injection vulnerability that allows script in the Discord page to write any config key via the window.legcord settings.setConfig bridge. Attackers exploiting a Discord XSS can set additionalArguments to persistently add --proxy-server and --ignore-certificate-errors switches, routing all client traffic through an interception proxy.

### 3. CVE-2026-105293｜Legcord / Legcord
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T01:16:28.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T01:16:28.780 / 2026-10-05T01:16:28.780
- **官方描述（原文）**：Legcord 1.1.0 through 1.3.0 contains a path traversal vulnerability in theme IPC handlers that allows script in the Discord page to escape the themes directory via unvalidated theme ids. Attackers running script in the Discord origin, such as through XSS, can abuse themes.folder, themes.uninstall, and themes.install to launch local executables, recursively delete directories, and write files outside the themes directory.

### 4. CVE-2026-105223｜maclof / kubernetes-client
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T01:16:28.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T01:16:28.480 / 2026-10-05T01:16:28.480
- **官方描述（原文）**：maclof kubernetes-client 0.17.0 before 0.32.0 disables TLS certificate verification in parseKubeconfig() and parseKubeconfigFile() when a kubeconfig lacks certificate-authority-data, ignoring insecure-skip-tls-verify. On-path attackers can impersonate the Kubernetes API server to capture Bearer tokens or Basic credentials and tamper with WebSocket or REST API traffic.

### 5. CVE-2026-105222｜alexpechkarev / google-maps
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T23:16:59.917)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T23:16:59.917 / 2026-10-04T23:16:59.917
- **官方描述（原文）**：The alexpechkarev/google-maps Laravel package through 12.16 disables TLS certificate verification by default because the bundled config sets ssl_verify_peer to FALSE, which is passed to CURLOPT_SSL_VERIFYPEER. On-path attackers can present any certificate to intercept Google Maps web-service requests, steal the API key from the query string, and tamper with responses.

### 6. CVE-2026-105221｜defunkt / gist
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T23:16:59.770)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T23:16:59.770 / 2026-10-04T23:16:59.770
- **官方描述（原文）**：The gist RubyGem before 6.1.0 contains an improper certificate validation vulnerability that allows on-path attackers to intercept HTTPS traffic because http_connection in lib/gist.rb sets VERIFY_NONE. Attackers can present any certificate to read or modify GitHub API traffic, stealing OAuth tokens and login credentials to read and modify the victim's gists.

### 7. CVE-2026-105218｜go-pay / gopay
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T18:16:34.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T18:16:34.630 / 2026-10-04T18:16:34.630
- **官方描述（原文）**：gopay before 1.5.119 disables TLS certificate verification in defaultClient() in pkg/xhttp/client.go, allowing man-in-the-middle attackers to impersonate payment provider APIs. Attackers can present any certificate to read merchant credentials, signatures and transaction data, and modify payment, refund and order query responses.

### 8. CVE-2026-105216｜micro / go-micro
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T18:16:34.287)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T18:16:34.287 / 2026-10-04T18:16:34.287
- **官方描述（原文）**：go-micro before 6.0.0 contains an improper certificate validation vulnerability that allows network attackers to impersonate services because the shared TLS helper sets InsecureSkipVerify to true by default. Man-in-the-middle attackers can present any certificate to intercept or modify gRPC transport, HTTP and RabbitMQ broker, and Consul or etcd registry traffic, including authentication tokens and credentials.

### 9. CVE-2026-105215｜zitadel / zitadel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T15:16:32.993)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T15:16:32.993 / 2026-10-04T15:16:33.107
- **官方描述（原文）**：ZITADEL before 3.4.14 and 4.x before 4.16.2 contains an authentication bypass in the hosted Login V1 UI because the 'external account not found' registration endpoint trusts client-supplied external identity fields without a completed IdP callback. Unauthenticated attackers can submit forged IDPConfigID and ExternalUserID values to pre-create an account bound to a victim's external IdP identity, which the victim's later genuine external login then signs into.

### 10. CVE-2026-105211｜zitadel / zitadel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T15:16:32.333)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T15:16:32.333 / 2026-10-04T15:16:32.467
- **官方描述（原文）**：ZITADEL before 4.17.1 contains an authentication bypass vulnerability in Login V2 that allows unauthenticated attackers to take over accounts by obtaining OTP codes via the returnCode delivery type. Attackers knowing a login name of a victim with OTP-Email and OTP-SMS enrolled can read both codes from server-action responses to gain MFA-authenticated sessions, including administrator takeover.

### 11. CVE-2026-105209｜zitadel / zitadel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T15:16:32.007)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T15:16:32.007 / 2026-10-04T15:16:32.127
- **官方描述（原文）**：ZITADEL 3.x before 3.4.15 and 4.x before 4.17.1 contains an improper authorization vulnerability: when issuing passkey or passwordless enrollment codes, it checks only the organization in the x-zitadel-orgid header, not the target user's organization. Attackers with user-write permission in one organization can obtain an enrollment code for a user in another organization on the same instance and register their own authenticator to take over that account.

### 12. CVE-2026-105207｜zitadel / zitadel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T15:16:31.677)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T15:16:31.677 / 2026-10-04T15:16:31.793
- **官方描述（原文）**：ZITADEL 3.0.0 through 3.4.15 and 4.0.0 before 4.17.3 creates links between user accounts and external identity providers without verifying a primary factor or the caller's permission, including on identify-only Login V2 sessions and via the User Service V2 AddIDPLink endpoint. An unauthenticated attacker knowing a victim's login name can bind their own external IdP identity to the victim's account and then sign in as the victim.

### 13. CVE-2026-105135｜InternLM / MindSearch
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T07:16:33.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.0077 / percentile=0.54065
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T07:16:33.693 / 2026-10-04T07:16:33.693
- **官方描述（原文）**：A vulnerability has been found in InternLM MindSearch 0.1.0. This issue affects the function ExecutionAction.run of the file mindsearch/agent/graph.py of the component Planner Agent. The manipulation of the argument inputs leads to code injection. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 14. CVE-2026-105134｜Ahsay / AhsayCBS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T07:16:33.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.01843 / percentile=0.78277
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T07:16:33.480 / 2026-10-04T07:16:33.480
- **官方描述（原文）**：A flaw has been found in Ahsay AhsayCBS up to 10.3.2. This vulnerability affects unknown code of the file /rps/api/json/UpdateReceivers.do of the component Replication Receiver. Executing a manipulation of the argument random can lead to os command injection. It is possible to launch the attack remotely. The exploit has been published and may be used. Upgrading to version 10.3.4 is able to resolve this issue. Upgrading the affected component is advised.

### 15. CVE-2026-105089｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T16:16:30.330)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T16:16:30.330 / 2026-10-04T16:16:30.330
- **官方描述（原文）**：WWBN AVideo through 29.2.0 contains a stored cross-site scripting vulnerability that allows users with upload permission to inject script by setting a malicious video trailer1 URL. The value is rendered unescaped in YouPHPFlix2 templates and channel playlists, letting attackers break out of onclick strings or iframe src attributes to execute JavaScript in victims' browsers.

### 16. CVE-2026-105086｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T16:16:30.183)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T16:16:30.183 / 2026-10-04T16:16:30.183
- **官方描述（原文）**：WWBN AVideo 12.4 through 29.2.0 contains a stored cross-site scripting vulnerability that allows authenticated uploaders to inject HTML by submitting doubly-encoded entities in video titles. Because safeString() strips tags before decoding entities and runs twice via setTitle() and save(), attackers can store markup that executes in trending, gallery, embed, and playlist pages.

### 17. CVE-2026-103355｜Unlimited Elements / Unlimited Elements For Elementor (Free Widgets, Addons, Templates)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-04T09:16:38.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.0025 / percentile=0.14812
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-04T09:16:38.820 / 2026-10-04T09:16:38.820
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Unlimited Elements Unlimited Elements For Elementor (Free Widgets, Addons, Templates) unlimited-elements-for-elementor allows Blind SQL Injection.This issue affects Unlimited Elements For Elementor (Free Widgets, Addons, Templates): from n/a through 2.0.20.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-88779｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.00276 / percentile=0.18203
- **CISA KEV**：listed=true / date_added=2026-10-04 / due_date=2026-10-07
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC (formerly Citrix ADC) and Citrix NetScaler Gateway (formerly Citrix Gateway) contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for a denial of service.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-87902｜WordPress / Core
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

### 3. CVE-2026-8037｜Progress / LoadMaster
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

### 4. CVE-2026-64849｜MLflow / MLflow
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

### 5. CVE-2026-41940｜WebPros / cPanel & WHM and WP2 (WordPress Squared)
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

### 6. CVE-2026-24061｜GNU / InetUtils
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

### 7. CVE-2025-62593｜Ray-Project / Ray
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
- **EPSS**：0.43782 / percentile=0.98709
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
| CVE-2026-42018 | P1 / 95 | JFrog / Artifactory | v3.1 7.5 (HIGH) | 0.09805 / percentile=0.95416 | listed=true / date_added=2026-09-11 / due_date=2026-09-25 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-105294 | WATCH / 28 | Legcord / Legcord | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105293 | WATCH / 28 | Legcord / Legcord | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105223 | WATCH / 28 | maclof / kubernetes-client | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105222 | WATCH / 28 | alexpechkarev / google-maps | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105221 | WATCH / 28 | defunkt / gist | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105218 | WATCH / 28 | go-pay / gopay | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105216 | WATCH / 28 | micro / go-micro | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105215 | WATCH / 28 | zitadel / zitadel | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105211 | WATCH / 28 | zitadel / zitadel | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105209 | WATCH / 28 | zitadel / zitadel | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105207 | WATCH / 28 | zitadel / zitadel | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105135 | WATCH / 28 | InternLM / MindSearch | v4.0 9.3 (CRITICAL) | 0.0077 / percentile=0.54065 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105134 | WATCH / 28 | Ahsay / AhsayCBS | v4.0 9.3 (CRITICAL) | 0.01843 / percentile=0.78277 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105089 | WATCH / 28 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105086 | WATCH / 28 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-103355 | WATCH / 28 | Unlimited Elements / Unlimited Elements For Elementor (Free Widgets, Addons, Templates) | v3.1 9.3 (CRITICAL) | 0.0025 / percentile=0.14812 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：16。
- EPSS 未確認：13；Exploitation status 未確認：16。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-05T06:26:23.594502+00:00`；Delta generated at：`2026-10-05T06:26:23.594502+00:00`。

---

## 可驗證資料來源

- **CVE-2026-88779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88779) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88779) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87902** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87902) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87902) · [Vendor / Advisory (github.com)](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-8037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-8037) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-8037) · [Vendor / Advisory (community.progress.com)](https://community.progress.com/s/article/LoadMaster-Critical-Security-Bulletin-June-2026-CVE-2026-8037-CVE-2026-33691) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-64849** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-64849) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-64849) · [Vendor / Advisory (github.com)](https://github.com/mlflow/mlflow/pull/24258) · [Vendor / Advisory (github.com)](https://github.com/mlflow/mlflow/issues/24179) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-41940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-41940) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-41940) · [Vendor / Advisory (support.cpanel.net)](https://support.cpanel.net/hc/en-us/articles/40073787579671-cPanel-WHM-Security-Update-04-28-2026) · [Vendor / Advisory (docs.cpanel.net)](https://docs.cpanel.net/release-notes/release-notes/) · [Vendor / Advisory (docs.wpsquared.com)](https://docs.wpsquared.com/changelogs/versions/changelog/#13617)
- **CVE-2026-105294** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105294)
- **CVE-2026-105293** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105293)
- **CVE-2026-105223** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105223)
- **CVE-2026-105222** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105222)
- **CVE-2026-105221** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105221)
- **CVE-2026-105218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105218)
- **CVE-2026-105216** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105216)
- **CVE-2026-105215** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105215)
- **CVE-2026-105211** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105211)
- **CVE-2026-105209** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105209)
- **CVE-2026-105207** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105207)
- **CVE-2026-105135** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105135) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105135)
- **CVE-2026-105134** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105134) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105134)
- **CVE-2026-105089** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105089)
- **CVE-2026-105086** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105086)
- **CVE-2026-103355** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103355) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-103355)
- **CVE-2026-24061** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-24061) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-24061) · [Vendor / Advisory (cgit.git.savannah.gnu.org)](https://cgit.git.savannah.gnu.org/cgit/inetutils.git) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/ccba9f748aa8d50a38d7748e2e60362edd6a32cc) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/fd702c02497b2f398e739e3119bed0b23dd7aa7b)
- **CVE-2025-62593** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-62593) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-62593) · [Vendor / Advisory (github.com)](https://github.com/ray-project/ray/security/advisories/GHSA-q279-jhrf-cc6v) · [Vendor / Advisory (github.com)](https://github.com/ray-project/ray/commit/70e7c72780bdec075dba6cad1afe0832772bfe09) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-14174** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-14174) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-14174) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2025/12/stable-channel-update-for-desktop_10.html) · [Vendor / Advisory (learn.microsoft.com)](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security)
- **CVE-2025-0282** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-0282) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-0282) · [CISA](https://www.cisa.gov/cisa-mitigation-instructions-CVE-2025-0282) · [Vendor / Advisory (forums.ivanti.com)](https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-Policy-Secure-ZTA-Gateways-CVE-2025-0282-CVE-2025-0283)
- **CVE-2024-9379** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-9379) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2024-9379) · [Vendor / Advisory (forums.ivanti.com)](https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-CSA-Cloud-Services-Appliance-CVE-2024-9379-CVE-2024-9380-CVE-2024-9381)
- **CVE-2024-7399** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-7399) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2024-7399) · [Vendor / Advisory (security.samsungtv.com)](https://security.samsungtv.com/securityUpdates)
- **CVE-2023-46805** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-46805) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-46805) · [Vendor / Advisory (forums.ivanti.com)](https://forums.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways?language=en_US)
- **CVE-2023-27351** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-27351) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-27351) · [Vendor / Advisory (papercut.com)](https://www.papercut.com/kb/Main/PO-1216-and-PO-1219)
- **CVE-2026-42018** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42018) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42018) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/jfrog-security-advisories) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
