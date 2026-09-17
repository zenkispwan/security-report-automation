# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**10** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=10。
- Intelligence 候選：**30** 筆；P1 **12**、P2 **0**、P3 **9**、WATCH **9**。
- Baseline：state / generated_at=2026-09-17T05:36:46.527188+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-65400、CVE-2026-20316、CVE-2026-20079、CVE-2026-76460、CVE-2026-86218。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **10** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-92913｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T12:18:30.290)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T12:18:30.290 / 2026-09-17T12:18:30.290
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 uses a cryptographically weak pseudo-random number generator when creating account activation / login pairing codes. getRandomCode() in objects/functions.php derives the code entirely from uniqid() (sprintf('%08x%05x', seconds, microseconds)) with a single non-CSPRNG rand() character used only as padding, reducing the code space to roughly 36 x 10^6 (~2^25) values for a known generation second. Because plugin/API/set.json.php?APIName=login_code can be called without authentication, it also serves as an oracle for the server's exact microtime. An unauthenticated remote attacker who guesses a valid, unexpired code (codes expire after 10 minutes) can redeem it at plugin/API/get.json.php?APIName=login_code to obtain the target account's email address and a User::getUserHash(users_id, '+1 year') value, a credential accepted in place of the account password for one year, resulting in account takeover. No patched version is available.

### 2. CVE-2026-92918｜cjbi / admin3
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T13:17:01.013)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T13:17:01.013 / 2026-09-17T13:17:01.013
- **官方描述（原文）**：admin3 through 3.0.0 persists user session tokens in the audit log event body when publishing UserLoggedIn domain events. Attackers with log:view permission can read the JSON response from the GET /logs endpoint to harvest session tokens and replay them as bearer credentials for full user access.

### 3. CVE-2026-92860｜rcourtman / Pulse
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T12:18:29.927)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T12:18:29.927 / 2026-09-17T12:18:29.927
- **官方描述（原文）**：A security flaw has been discovered in rcourtman Pulse up to 6.0.4/6.1.0-rc.4. Affected by this issue is the function fmt.Sprintf of the file /api/security/quick-setup of the component Quick Security Setup Handler. The manipulation of the argument Username results in improper input validation. The attack may be performed from remote. Upgrading the affected component is advised.

### 4. CVE-2026-90823｜FatPipe Networks / MPVPN
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T12:18:28.843)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T12:18:28.843 / 2026-09-17T13:16:58.503
- **官方描述（原文）**：FatPipe MPVPN, WARP, and IPVPN appliances running the end-of-life firmware version 10.1.2r60p100 contain a stack-based buffer overflow in /usr/sbin/auth_user_pass. An unauthenticated remote attacker with access to the affected management interface can submit a crafted authentication request that reaches an unchecked copy into a fixed-size stack buffer, potentially allowing arbitrary code execution as root. The affected management interface is disabled by default and must be affirmatively enabled by the customer before the endpoint becomes reachable. FatPipe recommends restricting management access to trusted administrative networks and using WAN access control lists to limit access to trusted sources. Customers running the affected end-of-life firmware can contact FatPipe Support for help confirming their firmware version and upgrading to a current supported release at https://www.fatpipeinc.com/support/support, support@fatpipeinc.com, or +1 800-724-8521 (option 3).

### 5. CVE-2026-90822｜FatPipe Networks / MPVPN
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T12:18:28.713)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T12:18:28.713 / 2026-09-17T13:16:58.407
- **官方描述（原文）**：FatPipe MPVPN, WARP, and IPVPN appliances running the end-of-life firmware version 10.1.2r60p100 contain an OS command injection vulnerability in the xtremed daemon. An unauthenticated remote attacker with access to the affected management interface can submit crafted input to the AuthFormServlet endpoint, causing authentication data to be processed by a shell and allowing arbitrary commands to execute as root. The affected management interface is disabled by default and must be affirmatively enabled by the customer before the endpoint becomes reachable. FatPipe recommends restricting management access to trusted administrative networks and using WAN access control lists to limit access to trusted sources. Customers running the affected end-of-life firmware can contact FatPipe Support for help confirming their firmware version and upgrading to a current supported release at https://www.fatpipeinc.com/support/support, support@fatpipeinc.com, or +1 800-724-8521 (option 3).

### 6. CVE-2026-88795｜Unknown / wpShopGermany IT-RECHT KANZLEI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T06:16:52.097)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T06:16:52.097 / 2026-09-17T13:16:57.580
- **官方描述（原文）**：The wpShopGermany IT-RECHT KANZLEI WordPress plugin before 2.4 does not generate its API authentication token securely, deriving it from data the requester controls and creating it as a side effect of the check that is supposed to validate it, allowing unauthenticated attackers to predict the token and use the access it grants to write arbitrary files, leading to remote code execution.

### 7. CVE-2026-86710｜Unknown / Login with QR
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T06:16:51.437)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T06:16:51.437 / 2026-09-17T13:16:53.443
- **官方描述（原文）**：The Login with QR WordPress plugin through 1.0.0 does not verify that the code used to log a user in is one it issued, matching any stored user metadata value instead, which allows unauthenticated attackers to log in as any user, including administrators.

### 8. CVE-2026-86709｜Unknown / The Pressengine
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T06:16:51.327)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T06:16:51.327 / 2026-09-17T13:16:53.283
- **官方描述（原文）**：The Pressengine WordPress plugin through 1.0 does not stop its login handler from issuing a session when authentication fails, allowing unauthenticated attackers to log in as any user, including administrators.

### 9. CVE-2026-86707｜Unknown / Private Feed Key
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T06:16:51.213)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T06:16:51.213 / 2026-09-17T13:16:53.113
- **官方描述（原文）**：The Private Feed Key WordPress plugin through 0.1 does not verify that the key used to authenticate a feed request is one it issued, matching any stored user metadata value instead, which allows unauthenticated attackers to log in as any user, including administrators.

### 10. CVE-2026-15688｜Mitsubishi Electric Corporation / GX Works3
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T09:16:39.240)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T09:16:39.240 / 2026-09-17T13:16:42.530
- **官方描述（原文）**：Incorrect Implementation of Authentication Algorithm Vulnerability in Mitsubishi Electric GX Works3 and Motion Control Setting allows a local attacker to successfully authenticate even with an invalid block password by executing the affected product and modifying part of the executable module in memory, and thereby may be able to view, tamper with, destroy, or delete control programs.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-65400｜Apple / macOS
- **Title**：Apple macOS Improper Authentication Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.10461 / percentile=0.95505
- **CISA KEV**：listed=true / date_added=2026-08-18 / due_date=2026-08-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apple macOS contains an improper authentication vulnerability that could allow an attacker on the network to authenticate to Screen Sharing without valid credentials.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-20316｜Cisco / Secure Firewall Management Center (FMC)
- **Title**：Cisco Secure Firewall Management Center Use of Hard-coded Password Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_MEDIUM(+4)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.11153 / percentile=0.95714
- **CISA KEV**：listed=true / date_added=2026-07-29 / due_date=2026-08-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Secure Firewall Management Center (FMC) formerly known as Firepower Management Center contains a use of hard-coded password vulnerability that could allow an unauthenticated, remote attacker to log in to an affected device using a low-privileged account to access sensitive data within the impacted systems.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-20079｜Cisco / Secure Firewall Management Center (FMC) and Security Cloud Control (SCC) Firewall Management
- **Title**：Cisco Firewall Management Center Authentication Bypass Using an Alternate Path or Channel Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.75752 / percentile=0.99496
- **CISA KEV**：listed=true / date_added=2026-09-09 / due_date=2026-09-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Secure Firewall Management Center (FMC) Software and Cisco Security Cloud Control (SCC) Firewall Management contain an authentication Bypass using an alternate path or channel vulnerability that could allow an unauthenticated, remote attacker to bypass authentication and execute script files on an affected device to obtain root access to the underlying operating system.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-76460｜Cisco / Identity Services Engine
- **Title**：Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability
- **Risk**：P1 / score 98；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) contain an incorrect use of privileged APIs vulnerability that could allow an unauthenticated, remote attacker to gain unauthorized access to the affected device by bypassing the web-based management interface.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-86218｜N-able / N-central
- **Title**：N-able N-central Static Code Injection Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.00744 / percentile=0.53005
- **CISA KEV**：listed=true / date_added=2026-09-08 / due_date=2026-09-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：N-able N-central contains a static code injection vulnerability that could allow for pre-authentication remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-76461｜Cisco / Secure Email Gateway
- **Title**：Cisco Secure Email Gateway SQL Injection Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.02009 / percentile=0.79862
- **CISA KEV**：listed=true / date_added=2026-09-14 / due_date=2026-09-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco AsyncOS software for Cisco Secure Email Gateway (SEG) contains a SQL injection vulnerability that could allow an unauthenticated, remote attacker to execute arbitrary commands with root privileges on the underlying operating system.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-58704｜Google / Pixel
- **Title**：Google Pixel Improper Authorization Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00112 / percentile=0.01564
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Pixel devices contain an improper authorization vulnerability in the cellular modem. A logic error may allow an attacker to bypass permission checks and escalate privileges.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2026-87491｜Google / Chromium V8
- **Title**：Google Chromium V8 Out of Bounds Write Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00997 / percentile=0.60979
- **CISA KEV**：listed=true / date_added=2026-09-09 / due_date=2026-09-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium V8 contains an out of bounds write vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-67277｜MikroTik / RouterOS
- **Title**：MikroTik RouterOS Missing Authentication for Critical Function Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：0.00869 / percentile=0.56984
- **CISA KEV**：listed=true / date_added=2026-09-10 / due_date=2026-09-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：MikroTik RouterOS contains a missing authenticaion for critical function vulnerability which allows kernel memory disclosure and denial of service in the btest service.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-20349｜Cisco / Secure Firewall Adaptive Security Appliance (ASA) and Secure Firewall Threat Defense (FTD)
- **Title**：Cisco Secure Firewall Adaptive Security Appliance (ASA) and Secure Firewall Threat Defense (FTD) Heap Inspection Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：0.02213 / percentile=0.81741
- **CISA KEV**：listed=true / date_added=2026-08-11 / due_date=2026-08-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Secure Firewall Adaptive Security Appliance (ASA) and Secure Firewall Threat Defense (FTD) contain a heap inspection vulnerability that could allow an unauthenticated, remote attacker to cause the device to reload unexpectedly, resulting in a denial of service (DoS) condition.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-87886 | P1 / 70 | Acronis / Backup | 未確認 | 未確認 | listed=true / date_added=2026-09-16 / due_date=2026-09-19 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-20284 | P1 / 53 | Cisco / Cisco Identity Services Engine Software | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=active / source=nvd_ssvc | 未確認 |

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-92913 | P3 / 38 | WWBN / AVideo | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-66066 | P3 / 49 | rails / rails | v4.0 9.5 (CRITICAL) | 0.27861 / percentile=0.97995 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2025-56005 | P3 / 43 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 0.17506 / percentile=0.96976 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-71362 | P3 / 39 | Adobe / Adobe Commerce | v3.1 9.1 (CRITICAL) | 0.2452 / percentile=0.97763 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-91939 | P3 / 38 | Cotonti / Cotonti | v4.0 9.3 (CRITICAL) | 0.00594 / percentile=0.46806 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91932 | P3 / 38 | FlowiseAI / Flowise | v4.0 9.0 (CRITICAL) | 0.00822 / percentile=0.55502 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-61560 | P3 / 38 | zereight / gitlab-mcp | v3.1 9.8 (CRITICAL) | 0.00703 / percentile=0.51559 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-37152 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 0.00189 / percentile=0.08779 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2024-14029 | P3 / 38 | tornadoweb / tornado | v4.0 9.0 (CRITICAL) | 0.00351 / percentile=0.28603 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-92918 | WATCH / 30 | cjbi / admin3 | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92860 | WATCH / 28 | rcourtman / Pulse | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-90823 | WATCH / 28 | FatPipe Networks / MPVPN | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-90822 | WATCH / 28 | FatPipe Networks / MPVPN | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-88795 | WATCH / 28 | Unknown / wpShopGermany IT-RECHT KANZLEI | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-86710 | WATCH / 28 | Unknown / Login with QR | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-86709 | WATCH / 28 | Unknown / The Pressengine | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-86707 | WATCH / 28 | Unknown / Private Feed Key | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-15688 | WATCH / 28 | Mitsubishi Electric Corporation / GX Works3 | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：2；缺少 Product：2；缺少 Title：19。
- EPSS 未確認：13；Exploitation status 未確認：3。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-17T14:16:33.251179+00:00`；Delta generated at：`2026-09-17T14:16:33.251179+00:00`。

---

## 可驗證資料來源

- **CVE-2026-65400** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65400) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65400) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148170) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148171) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148172) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-20316** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20316) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20316) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-20079** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20079) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20079) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-76460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-86218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86218) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86218) · [Vendor / Advisory (status.n-able.com)](https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/) · [Vendor / Advisory (me.n-able.com)](https://me.n-able.com/s/security-advisory/aArVy0000002Ld3KAE/cve202686218-preauthentication-remote-code-execution) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-92913** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92913)
- **CVE-2026-92918** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92918)
- **CVE-2026-92860** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92860)
- **CVE-2026-90823** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90823)
- **CVE-2026-90822** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90822)
- **CVE-2026-88795** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88795)
- **CVE-2026-86710** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86710)
- **CVE-2026-86709** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86709)
- **CVE-2026-86707** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86707)
- **CVE-2026-15688** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15688)
- **CVE-2026-76461** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76461) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76461) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-58704** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58704) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-58704) · [Vendor / Advisory (source.android.com)](https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87491) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87491) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-67277** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67277) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-67277) · [Vendor / Advisory (mikrotik.com)](https://mikrotik.com/supportsec/september-2026-vulnerability/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-20349** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20349) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20349) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87886** — [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (security-advisory.acronis.com)](https://security-advisory.acronis.com/advisories/SEC-10986) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87886)
- **CVE-2026-20284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20284)
- **CVE-2026-66066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66066) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-66066)
- **CVE-2025-56005** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-56005) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-56005)
- **CVE-2026-71362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71362) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-71362)
- **CVE-2026-91939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91939) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91939)
- **CVE-2026-91932** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91932) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91932)
- **CVE-2026-61560** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61560) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-61560)
- **CVE-2026-37152** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-37152) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-37152)
- **CVE-2024-14029** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-14029) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2024-14029)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
