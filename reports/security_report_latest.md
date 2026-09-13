# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**11** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=11。
- Intelligence 候選：**30** 筆；P1 **11**、P2 **0**、P3 **8**、WATCH **11**。
- Baseline：state / generated_at=2026-09-12T05:16:44.587798+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-85706、CVE-2026-86218、CVE-2026-86060、CVE-2026-84869、CVE-2026-87491。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **11** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-90647｜Kalkitech / ASE2000 V2 Communication Test Set
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T23:17:01.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T23:17:01.490 / 2026-09-12T23:17:01.490
- **官方描述（原文）**：ASE/Kalkitech ASE2000 V2 Communication Test Set 2.35 through 2.37 on Windows contains an improper certificate validation vulnerability in the IEC 60870-5-104 TLS client (Task Mode). This allows a network-positioned attacker to bypass certificate validation via a certificate with multiple simultaneous faults, enabling a Man-in-the-Middle attack on protected communications.

### 2. CVE-2026-90558｜irontec / sngrep
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T18:16:44.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T18:16:44.587 / 2026-09-12T18:16:44.587
- **官方描述（原文）**：sngrep through 1.8.4 contains stack buffer overflow vulnerabilities in SIP attribute formatting routines when header values exceed the 255-byte buffer limit. Attackers can craft malicious SIP packets with oversized Call-ID, X-Call-ID, or other header fields to overflow stack buffers and cause crashes or execute arbitrary code during packet parsing and rendering.

### 3. CVE-2026-85681｜Unknown / WP Component
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T06:16:27.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T06:16:27.250 / 2026-09-12T16:16:42.170
- **官方描述（原文）**：The WP Component WordPress plugin through 2.2.4 does not have any capability or nonce checks on one of the actions it makes available to unauthenticated users, and it takes both the option name and the option value from the request, allowing unauthenticated attackers to overwrite any of the site's options. On a single site installation this leads to a full takeover, as registration can be enabled with a default role of administrator.

### 4. CVE-2026-84171｜Unknown / WP images upload on piclect
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T06:16:27.137)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00162 / percentile=0.05674
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T06:16:27.137 / 2026-09-12T16:16:41.897
- **官方描述（原文）**：The WP images upload on piclect WordPress plugin through 1.0 does not validate the name or type of uploaded files before writing them to a publicly accessible directory, allowing unauthenticated attackers to upload arbitrary files and execute arbitrary code on the server.

### 5. CVE-2026-82845｜Unknown / Masteriyo LMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T06:16:26.043)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00167 / percentile=0.06224
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T06:16:26.043 / 2026-09-12T16:16:40.557
- **官方描述（原文）**：The Masteriyo LMS WordPress plugin before 3.4.1 does not prevent user-supplied values held as metadata from being deserialized when they are read back, allowing users with a minimal account to inject arbitrary PHP objects and, by way of a class shipped in a library bundled with the Masteriyo LMS WordPress plugin before 3.4.1, write and execute arbitrary code on the server. A weaker form of the same issue is reachable without an account and yields an arbitrary file write rather than code execution.

### 6. CVE-2026-81402｜Unknown / DS Ad Rotator
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T06:16:25.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00197 / percentile=0.09584
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T06:16:25.730 / 2026-09-12T16:16:40.140
- **官方描述（原文）**：The DS Ad Rotator WordPress plugin through 0.8 does not perform any capability check, nonce verification, or file-type validation on its image upload handler, allowing unauthenticated attackers to upload arbitrary files, including PHP, to a web-accessible directory, which can lead to remote code execution.

### 7. CVE-2026-78159｜stellarwp / The Events Calendar
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T08:16:24.377)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00762 / percentile=0.53333
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T08:16:24.377 / 2026-09-12T08:16:24.377
- **官方描述（原文）**：The The Events Calendar plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, 6.17.3 via the parse_array function. This is due to insufficient validation of the widget 'classes' map, allowing a plain-array payload to bypass the is_safe_widget_instance() object check and reach the callable-invocation sink in Element_Classes::parse_array(). This makes it possible for unauthenticated attackers to execute code on the server. Exploitation requires that the targeted site has comments enabled on tribe_events posts and that at least one comment containing a crafted wp:legacy-widget block has been submitted, as the attack chain is triggered when do_blocks() processes the single-event HTML including the comment area.

### 8. CVE-2026-78006｜stellarwp / The Events Calendar
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T08:16:24.240)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00778 / percentile=0.53841
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T08:16:24.240 / 2026-09-12T08:16:24.240
- **官方描述（原文）**：The The Events Calendar plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, 6.17.4 via the is_safe_widget_instance function. This is due to insufficient protection in is_safe_widget_instance, which can be bypassed because PHP fires magic methods during its pre-parse, combined with enable_rendering_widget_copied() forging a valid wp_hash integrity attribute before unserialize() is reached. This makes it possible for unauthenticated attackers to execute code on the server. This is exploitable without authentication or approval because the plugin's V2 single-event template runs do_blocks() over buffered comment HTML, and WordPress returns a moderation-hash URL that allows an unauthenticated commenter to immediately view their own pending comment, delivering the injected block markup to the vulnerable code path before any moderation occurs. This does require comments to be enabled and visible on events.

### 9. CVE-2026-77006｜Unknown / WebTotem Backups
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T06:16:24.733)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T06:16:24.733 / 2026-09-12T16:16:38.670
- **官方描述（原文）**：The WebTotem Backups WordPress plugin through 1.0.1 does not validate a user-supplied file path, does not check the capability of the user making the request, and discards the result of its own CSRF check, allowing any authenticated user, such as a subscriber, to delete arbitrary files on the server, which can lead to a site takeover.

### 10. CVE-2026-77005｜Unknown / CODE MONKEYS PROPOSALS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T06:16:24.623)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T06:16:24.623 / 2026-09-12T16:16:38.523
- **官方描述（原文）**：The CODE MONKEYS PROPOSALS WordPress plugin through 1.0.1 does not validate a user-supplied file path before deleting a file, and does not check the capability of the user making the request, allowing any authenticated user, such as a subscriber, to delete arbitrary files on the server, which can lead to a site takeover.

### 11. CVE-2026-75800｜Unknown / Frontegg SAML SSO
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T06:16:23.340)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00187 / percentile=0.08433
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T06:16:23.340 / 2026-09-12T16:16:38.363
- **官方描述（原文）**：The Frontegg SAML SSO WordPress plugin through 1.0.1 does not verify the signature or issuer of SAML authentication responses before establishing a session, allowing unauthenticated attackers to log in as any user, including administrators, as well as to create arbitrary accounts.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-85706｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability
- **Risk**：P1 / score 98；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contains a path traversal vulnerability that allows an unauthenticated user to read arbitrary files due to an improper path confinement and missing authentication enforcement in the repository commits API.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-86218｜N-able / N-central
- **Title**：N-able N-central Static Code Injection Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.00744 / percentile=0.52735
- **CISA KEV**：listed=true / date_added=2026-09-08 / due_date=2026-09-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：N-able N-central contains a static code injection vulnerability that could allow for pre-authentication remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-86060｜MikroTik / RouterOS
- **Title**：MikroTik RouterOS Improper Neutralization of Argument Delimiters in a Command Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-10 / due_date=2026-09-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：MikroTik RouterOS contains an improper neutralization of argument delimiters in a command vulnerability which allows an attacked to change the trusted RouterOS policy mask, leading to privilege escalation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-84869｜ConnectWise / ScreenConnect
- **Title**：ConnectWise ScreenConnect Improper Privilege Management and Missing Authorization Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00691 / percentile=0.50847
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：ConnectWise ScreenConnect contains both an improper privilege management and missing authorization vulnerability that may allow an attacker to file transfer and execution through an active remote sessions without authorization or host confirmation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-87491｜Google / Chromium V8
- **Title**：Google Chromium V8 Out of Bounds Write Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00859 / percentile=0.56441
- **CISA KEV**：listed=true / date_added=2026-09-09 / due_date=2026-09-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium V8 contains an out of bounds write vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-85880｜Microsoft / Windows
- **Title**：Microsoft Windows Heap-Based Buffer Overflow Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.00572 / percentile=0.45535
- **CISA KEV**：listed=true / date_added=2026-09-08 / due_date=2026-09-22
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft Windows Advanced Local Procedure Call contains a heap-based buffer overflow vulnerability that allows an attacker to elevate privileges locally.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-85046｜Google / Chromium V8
- **Title**：Google Chromium V8 Type Confusion Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.0126 / percentile=0.6793
- **CISA KEV**：listed=true / date_added=2026-09-04 / due_date=2026-09-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium V8 contains a type confusion vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2026-81963｜Microsoft / Windows
- **Title**：Microsoft Windows Link Following Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.00631 / percentile=0.48297
- **CISA KEV**：listed=true / date_added=2026-09-08 / due_date=2026-09-22
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft Windows Update Stack contains a link following vulnerability that allows a local attacker to escalate privileges locally up to SYSTEM.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-67277｜MikroTik / RouterOS
- **Title**：MikroTik RouterOS Missing Authentication for Critical Function Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：0.00856 / percentile=0.56333
- **CISA KEV**：listed=true / date_added=2026-09-10 / due_date=2026-09-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：MikroTik RouterOS contains a missing authenticaion for critical function vulnerability which allows kernel memory disclosure and denial of service in the btest service.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-42018｜JFrog / Artifactory
- **Title**：JFrog Artifactory Improper Authentication Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.0092 / percentile=0.58304
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JFrog Artifactory contains an improper authentication vulnerability that could return an internal anonymous-user token to an unauthenticated caller when anonymous access is disabled, potentially exposing sensitive resources.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-42016 | P1 / 82 | JFrog / Artifactory | v3.1 8.8 (HIGH) | 0.00886 / percentile=0.57253 | listed=true / date_added=2026-09-11 / due_date=2026-09-25 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-66066 | P3 / 49 | rails / rails | v4.0 9.5 (CRITICAL) | 0.27861 / percentile=0.9798 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-43284 | P3 / 47 | Linux / Linux | v3.1 8.8 (HIGH) | 0.93235 / percentile=0.9983 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-42945 | P3 / 45 | F5 / NGINX Plus | v4.0 9.2 (CRITICAL) | 0.68047 / percentile=0.99281 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-89256 | P3 / 38 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 0.00323 / percentile=0.25181 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89255 | P3 / 38 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 0.00347 / percentile=0.27904 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89253 | P3 / 38 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 0.00347 / percentile=0.27903 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89243 | P3 / 38 | WWBN / AVideo | v4.0 9.2 (CRITICAL) | 0.00361 / percentile=0.29509 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89010 | P3 / 38 | WAVLINK Technology / WN535M1 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-90647 | WATCH / 28 | Kalkitech / ASE2000 V2 Communication Test Set | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-90558 | WATCH / 28 | irontec / sngrep | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-85681 | WATCH / 28 | Unknown / WP Component | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-84171 | WATCH / 28 | Unknown / WP images upload on piclect | v3.1 9.8 (CRITICAL) | 0.00162 / percentile=0.05674 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-82845 | WATCH / 28 | Unknown / Masteriyo LMS | v3.1 9.9 (CRITICAL) | 0.00167 / percentile=0.06224 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-81402 | WATCH / 28 | Unknown / DS Ad Rotator | v3.1 9.8 (CRITICAL) | 0.00197 / percentile=0.09584 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-78159 | WATCH / 28 | stellarwp / The Events Calendar | v3.1 9.8 (CRITICAL) | 0.00762 / percentile=0.53333 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-78006 | WATCH / 28 | stellarwp / The Events Calendar | v3.1 9.8 (CRITICAL) | 0.00778 / percentile=0.53841 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-77006 | WATCH / 28 | Unknown / WebTotem Backups | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-77005 | WATCH / 28 | Unknown / CODE MONKEYS PROPOSALS | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-75800 | WATCH / 28 | Unknown / Frontegg SAML SSO | v3.1 9.8 (CRITICAL) | 0.00187 / percentile=0.08433 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：19。
- EPSS 未確認：8；Exploitation status 未確認：4。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-13T05:30:44.355904+00:00`；Delta generated at：`2026-09-13T05:30:44.355904+00:00`。

---

## 可驗證資料來源

- **CVE-2026-85706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85706) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-86218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86218) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86218) · [Vendor / Advisory (status.n-able.com)](https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/) · [Vendor / Advisory (me.n-able.com)](https://me.n-able.com/s/security-advisory/aArVy0000002Ld3KAE/cve202686218-preauthentication-remote-code-execution) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-86060** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86060) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-84869** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84869) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84869) · [Vendor / Advisory (connectwise.com)](https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87491) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87491) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-90647** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90647)
- **CVE-2026-90558** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90558)
- **CVE-2026-85681** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85681)
- **CVE-2026-84171** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84171) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84171)
- **CVE-2026-82845** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82845) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-82845)
- **CVE-2026-81402** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81402) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-81402)
- **CVE-2026-78159** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78159) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-78159)
- **CVE-2026-78006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78006) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-78006)
- **CVE-2026-77006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77006)
- **CVE-2026-77005** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77005)
- **CVE-2026-75800** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75800) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-75800)
- **CVE-2026-85880** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85880) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85880) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85046) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-81963** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81963) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-81963) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-67277** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67277) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-67277) · [Vendor / Advisory (mikrotik.com)](https://mikrotik.com/supportsec/september-2026-vulnerability/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-42018** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42018) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42018) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/jfrog-security-advisories) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-42016** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42016) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42016) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/jfrog-security-advisories) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-66066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66066) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-66066)
- **CVE-2026-43284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-43284) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-43284)
- **CVE-2026-42945** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42945) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42945)
- **CVE-2026-89256** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89256) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89256)
- **CVE-2026-89255** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89255) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89255)
- **CVE-2026-89253** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89253) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89253)
- **CVE-2026-89243** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89243) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89243)
- **CVE-2026-89010** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89010)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
