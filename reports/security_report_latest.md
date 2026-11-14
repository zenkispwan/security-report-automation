# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**163** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=162、NEW_KEV=2。
- Intelligence 候選：**30** 筆；P1 **2**、P2 **0**、P3 **11**、WATCH **17**。
- Baseline：state / generated_at=2026-11-12T07:52:01.651144+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-123039、CVE-2026-114713。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **163** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-123039｜Check Point / Multiple Products
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T14:17:24.233)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-13 / due_date=2026-11-16
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-12T14:17:24.233 / 2026-11-14T05:18:31.413
- **官方描述（原文）**：Check Point Firewall, Multi-Domain Security Management Server, Scalable Platforms, Security Gateway, and Security Management Server contain an incorrect permissions assignment for critical resources vulnerability when the Gaia OS DynamicCLI daemon runs as root and listens on a world-writable local socket without authenticating connecting processes. An authenticated local user can send a command to the socket and have it executed as root.

### 2. CVE-2026-114713｜UnrealIRCd / UnrealIRCd
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-13 / due_date=2026-11-16
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-08T03:16:33.410 / 2026-11-14T05:18:24.417
- **官方描述（原文）**：UnrealIRCd UnrealIRCd contains an improper neutralization of delimiters vulnerability that allows any user on a network with two or more linked servers to inject server-to-server commands that are executed with server authority.

### 3. CVE-2026-75869｜Zohocorp / DDI Central
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T13:17:16.900)
- **Risk**：P3 / score 39；reasons：CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.20352 / percentile=0.97523
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T13:17:16.900 / 2026-11-12T19:02:35.830
- **官方描述（原文）**：Zohocorp ManageEngine DDI Central versions below 6301 is affected by an authorization bypass and PowerShell command injection vulnerability that allowed authenticated non-administrative users to target unauthorized Windows DHCP subnets and potentially execute arbitrary commands on managed Windows DHCP servers through crafted DNS suffix values.

### 4. CVE-2026-68548｜xyproto / algernon
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:51.307)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00754 / percentile=0.55646
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:51.307 / 2026-11-13T02:18:58.730
- **官方描述（原文）**：Algernon is a small self-contained pure-Go web server. Prior to version 1.17.10, Algernon's URL-prefix authorization gate matches its protected prefixes (/admin, /repo, /data) with case-sensitive strings.HasPrefix, while the exact same raw req.URL.Path is later resolved against the filesystem. On case-insensitive filesystems (Windows NTFS — always; macOS APFS/HFS+ — default), a request for /Admin/secret.lua evades every protected-prefix check, falls through to the public-prefix accept branch, and then resolves on disk to admin/secret.lua. The result is an unauthenticated bypass of the /admin, /repo, and /data authorization boundary, enabling read (and, for Lua files, execution) of protected content. The permission system is active in the default configuration. This issue has been patched in version 1.17.10.

### 5. CVE-2026-127275｜Linksys / EA8100
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T00:20:14.083)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00754 / percentile=0.55656
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T00:20:14.083 / 2026-11-13T23:17:17.477
- **官方描述（原文）**：A vulnerability was determined in Linksys EA8100 1.0.3.216940. This issue affects the function SetRemoteSetting/SetUnsecuredWiFiWarning of the file ui_server.lua of the component JNAP API. This manipulation of the argument isEnabled/enabled causes missing authentication. It is possible to initiate the attack remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 6. CVE-2026-127080｜OpsTree Solutions / BuildPiper
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:04.260)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00506 / percentile=0.43781
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:04.260 / 2026-11-13T23:17:17.230
- **官方描述（原文）**：OpsTree BuildPiper before 2.7.0 contains an improper authorization vulnerability that allows authenticated deploy users to define arbitrary Kubernetes hostPath volumes without allow-list or policy checks. Attackers can set the host path to / in the Define HostPath Volume configuration to mount the worker node root filesystem read-write, breaking container isolation and enabling node and cluster compromise.

### 7. CVE-2026-126952｜diced / zipline
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:02.590)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00339 / percentile=0.27755
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:02.590 / 2026-11-13T19:19:27.113
- **官方描述（原文）**：Zipline through 4.4.0 contains an authentication bypass vulnerability in the WebAuthn login endpoint that creates sessions for a supplied registered credential ID without verifying the assertion. Attackers who obtain a target's passkey credential ID can impersonate that account without its authenticator, potentially gaining administrative control over SUPERADMIN accounts.

### 8. CVE-2026-126473｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:56.590)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00461 / percentile=0.40455
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:56.590 / 2026-11-13T19:19:24.003
- **官方描述（原文）**：OpenEMR before 8.4.0 contains OAuth scope canonicalization and containment flaws that allow unauthenticated attackers to obtain unapproved system-level FHIR access. Attackers can register a colon-form system:Patient.read client that bypasses approval, then request unregistered system/Patient.write scope to read, modify, and create Patient records.

### 9. CVE-2026-126380｜givanz / Vvveb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:40.773)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00643 / percentile=0.51394
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:40.773 / 2026-11-13T21:17:42.083
- **官方描述（原文）**：Vvveb before 1.0.9.0 contains a denylist bypass in system/traits/media.php where '.phar' is misconfigured with a leading dot, allowing authenticated administrators to upload .phar PHP files. Attackers can upload a GIF magic-byte polyglot webshell bypassing binary inspection and execute arbitrary OS commands as the web-server user.

### 10. CVE-2026-124010｜Copeland / XWEB EVO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:24.263)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.03095 / percentile=0.87937
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:24.263 / 2026-11-13T23:17:14.170
- **官方描述（原文）**：XWEB EVO before 5.6.2 contains a command injection vulnerability that allows unauthenticated remote attackers to execute arbitrary commands as root by exploiting the setuid-root CGI xwconsole.cgi. Attackers can supply malicious input through the sh parameter, which is passed unsanitized to popen(), to achieve full system compromise. This product line reached it's end of service date in March 2026.

### 11. CVE-2026-124006｜Copeland / XWEB EVO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:23.033)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00553 / percentile=0.46764
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:23.033 / 2026-11-13T23:17:14.053
- **官方描述（原文）**：XWEB EVO through 5.8.8 contains a predictable credential generation vulnerability that allows attackers to derive the Linux root password by computing a fixed prefix combined with a daily password value. Attackers can calculate the deterministic root credential, which before 5.7.0 was identical across all units and from 5.7.0 onward remains derivable from the MAC-based daily password, to gain unauthorized root access to the underlying operating system. This product line reached it's end of service date in March 2026.

### 12. CVE-2026-124005｜Copeland / XWEB EVO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:22.673)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00547 / percentile=0.46394
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:22.673 / 2026-11-13T19:19:20.483
- **官方描述（原文）**：XWEB EVO 4.3.0 through 5.8.8 contains a weak password generation vulnerability that allows remote attackers to derive the Administrator code-of-the-day password using only the device MAC address and date, with no server secret involved. Attackers can analyze the firmware binary xwpasswd, which itself functions as the password generator, to compute valid Administrator credentials offline and authenticate to the device without authorization. This product line reached it's end of service date in March 2026.

### 13. CVE-2026-124002｜Copeland / XWEB EVO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:21.597)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.049 / percentile=0.92228
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:21.597 / 2026-11-13T23:17:13.910
- **官方描述（原文）**：XWEB EVO versions 5.2.3 through before 5.7.0 contains a pre-authentication OS command injection vulnerability that allows unauthenticated remote attackers to execute arbitrary OS commands by injecting shell metacharacters into the username field of login.lua, cleanout.lua, or api.lua before the password check occurs. Attackers can exploit this flaw combined with the setuid-root wlua interpreter to execute commands with root privileges, achieving full system compromise. This product line reached it's end of service date in March 2026.

### 14. CVE-2026-82414｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T19:19:36.740)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T19:19:36.740 / 2026-11-13T22:17:26.140
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. From versions 1.4.0 to before 1.4.6, 1.5.0 to before 1.5.1, and 1.6.0 to before 1.6.1, the BACnet MS/TP receive path decodes COBS frames into an output pointer inside the same fixed input buffer, but passes the full input-buffer size as the decode capacity. A long valid COBS payload can therefore write past the end of the actual remaining buffer. This issue has been patched in versions 1.4.6, 1.5.1, 1.6.1, and 1.7.0.

### 15. CVE-2026-68551｜teelur / budget-board
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T20:19:00.750)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T20:19:00.750 / 2026-11-13T22:17:25.687
- **官方描述（原文）**：Budget Board is an app for tracking monthly spending and working towards financial goals. Prior to version 3.6.2, Budget Board's OIDC login flow finds and signs into an existing local account purely by matching the email address asserted in the identity provider's token - it never checks the standard email_verified claim. If the configured OIDC provider ever allows a user to register or display an email address without proving they own it , an attacker can register there using a victim's email and get signed into the victim's existing Budget Board account - including all their linked bank data. This issue has been patched in version 3.6.2.

### 16. CVE-2026-62973｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T16:19:28.960)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T16:19:28.960 / 2026-11-13T22:11:32.147
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.5, 1.5.1, and 1.6.0, a remote out-of-bounds read exists in the official BACnet client application apps/readpropm in bacnet-stack commit e2bdbf6. When readpropm sends a legitimate ReadPropertyMultiple request to a malicious BACnet/IP peer, the peer can reply with a malformed but structurally valid ReadPropertyMultiple-ACK that drives the client into a global-buffer-overflow read on the global receive buffer Rx_Buf. This issue has been patched in versions 1.4.5, 1.5.1, and 1.6.0.

### 17. CVE-2026-52790｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T16:19:02.587)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T16:19:02.587 / 2026-11-13T22:11:32.147
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.5, 1.5.1, and 1.6.0, there is a library-level memory safety issue that is reachable from an unmodified official sample server (apps/server-basic/main.c) over BACnet/IP resulting in a stack-use-after-return in writable Device string properties. This issue has been patched in versions 1.4.5, 1.5.1, and 1.6.0.

### 18. CVE-2026-49990｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T16:19:01.983)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T16:19:01.983 / 2026-11-13T22:11:32.147
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. From versions 1.4.2 to before 1.4.5, and 1.5.0 to before 1.5.1, a signed fileStartPosition taken from AtomicReadFile and AtomicWriteFile stream-access requests is not validated tightly enough before it reaches the RAM file backends. Practical impact includes: reliable denial of service via process crash, out-of-bounds read that may expose adjacent memory contents, or out-of-bounds write that may corrupt heap memory and destabilize the process. This issue has been patched in versions 1.4.5 and 1.5.1.

### 19. CVE-2026-47710｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:40.747)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：0.00254 / percentile=0.17032
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:40.747 / 2026-11-13T20:18:58.537
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4, 1.5.1, and 1.6.0, a stack-buffer-overflow can be triggered in the current master branch when a Loop object reads a referenced property through its default timer path and the referenced property is OBJECT_STRUCTURED_VIEW / PROP_DESCRIPTION containing a long attacker-controlled string. This issue has been patched in versions 1.4.4, 1.5.1, and 1.6.0.

### 20. CVE-2026-47257｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:40.020)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.00393 / percentile=0.33926
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:40.020 / 2026-11-13T02:18:57.897
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. In versions 1.5.0 and 1.6.0-rc1, there is a restore logic flaw in bacnet-stack that is reachable through the official, unmodified apps/server management path when BACNET_BACKUP_RESTORE is enabled. This issue has been patched in versions 1.5.1 and 1.6.0.

### 21. CVE-2026-47217｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:39.770)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00383 / percentile=0.32862
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:39.770 / 2026-11-13T19:19:32.780
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4 and 1.5.1, a remote attacker can trigger an uncontrolled recursion and stack overflow in the default server application of bacnet-stack by abusing the Channel object. This issue has been patched in versions 1.4.4 and 1.5.1.

### 22. CVE-2026-46674｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:39.080)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00428 / percentile=0.37599
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:39.080 / 2026-11-13T02:18:57.780
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4 and 1.5.1, an out-of-bounds read vulnerability exists in bacnet-stack's AtomicWriteFile record-access path. The bug is caused by a mismatch between an externally controlled returnedRecordCount field and the fixed-size internal fileData[] array used by BACNET_ATOMIC_WRITE_FILE_DATA. This issue has been patched in versions 1.4.4 and 1.5.1.

### 23. CVE-2026-45341｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:38.667)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00274 / percentile=0.20066
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:38.667 / 2026-11-13T19:19:32.673
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. From versions 1.4.0 to before 1.4.4, and 1.5.0 to before 1.5.1, a NULL pointer dereference can be triggered in bacnet_device_object_reference_decode() when a WriteProperty request updates OBJECT_STRUCTURED_VIEW / PROP_SUBORDINATE_LIST. This issue has been patched in versions 1.4.4 and 1.5.1.

### 24. CVE-2026-129123｜OpenKermit / C-Kermit
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T17:17:29.517)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T17:17:29.517 / 2026-11-13T22:17:23.927
- **官方描述（原文）**：C-Kermit 8.0.200 before 11.1.515 contains a buffer overflow vulnerability in getreply() in ckcftp.c that allows malicious FTP servers to overwrite client memory by sending overlong security replies. Attackers controlling or intercepting an FTP server can send long PBSZ replies after AUTH TLS, or long ADAT replies in GSSAPI, Kerberos 4, and SRP builds, overflowing the static reply_buf with attacker-controlled bytes.

### 25. CVE-2026-129119｜OpenKermit / C-Kermit
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T17:17:28.753)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T17:17:28.753 / 2026-11-13T22:17:23.803
- **官方描述（原文）**：C-Kermit from 6.0.192 before 11.1.515 contains a file collision protection bypass that allows malicious senders to append data to existing files by marking transfers as RESEND. The gattr() function in ckcfn3.c clears the REJECT discard flag and switches to APPEND without a RECEIVE CONFIRM prompt, letting attackers modify files such as shell startup files.

### 26. CVE-2026-128344｜exceljs / exceljs
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:14.977)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.0063 / percentile=0.50744
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:14.977 / 2026-11-13T18:17:38.063
- **官方描述（原文）**：ExcelJS through 4.4.0 contains a memory exhaustion vulnerability that allows attackers to crash applications by supplying a workbook with an unbounded image anchor column in the drawing part. Attackers can set an anchor column such as 300000000 in xl/drawings/drawing1.xml so reading getImages() anchor positions makes Worksheet.getColumn allocate millions of Column objects and abort with a heap out-of-memory error.

### 27. CVE-2026-128340｜exceljs / exceljs
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:14.373)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.0063 / percentile=0.50745
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:14.373 / 2026-11-13T18:17:37.937
- **官方描述（原文）**：ExcelJS through 4.4.0 contains a memory exhaustion vulnerability that allows attackers to crash applications by supplying a workbook with an oversized defined-name range. DefinedNames.addEx expands ranges such as S!$A$1:$XFD$1048576 from xl/workbook.xml cell by cell, causing an uncatchable fatal heap out-of-memory error during xlsx.load().

### 28. CVE-2026-128082｜LuckyPennySoftware / AutoMapper
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T19:19:30.743)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T19:19:30.743 / 2026-11-13T22:17:22.843
- **官方描述（原文）**：AutoMapper is a convention-based object-object mapper in .NET. Prior to 15.1.4 and from 16.0.0 until 16.3.0, AutoMapper increments type depth only after creating the destination, so recursive mapping performed through constructor parameters occurs before MaxDepth is counted. Destinations built through positional records or other constructors, and recursive ConstructUsing mappings that call context.Mapper, can therefore bypass explicit MaxDepth values and the default limit of 64. Deep attacker-influenced input can throw an uncatchable StackOverflowException and terminate the process. This issue is fixed in versions 15.1.4 and 16.3.0.

### 29. CVE-2026-127076｜OpsTree Solutions / BuildPiper
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:03.680)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00402 / percentile=0.34929
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:03.680 / 2026-11-13T23:17:17.103
- **官方描述（原文）**：OpsTree BuildPiper before 2.7.0 contains a broken access control vulnerability that allows authenticated users to list and build from Git repositories restricted to other projects. Attackers can enumerate repositories via GET /api/v1/git_repo/?all=true and submit any git_repo_id to the ci endpoint, cloning other projects' source code, manifests, and committed secrets.

### 30. CVE-2026-126948｜diced / zipline
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:02.047)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.00442 / percentile=0.38956
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:02.047 / 2026-11-13T19:19:26.960
- **官方描述（原文）**：Zipline before 4.5.0 contains an insecure direct object reference vulnerability caused by missing ownership verification in the PATCH and DELETE handlers for /api/user/folders/:id. Authenticated attackers can supply another user's folder ID to rename it, make it public, enable uploads, or delete it.

### 31. CVE-2026-126938｜diced / zipline
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:00.573)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00415 / percentile=0.36335
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:00.573 / 2026-11-13T19:19:26.563
- **官方描述（原文）**：Zipline before 4.6.4 contains a resource allocation vulnerability that allows authenticated users to bypass chunked-upload size and quota checks by forging Content-Range offsets and totals. Attackers can send tiny chunks to the partial upload endpoint with large declared offsets, causing the server to create oversized files and exhaust disk space.

### 32. CVE-2026-126489｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:59.250)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：0.00475 / percentile=0.41584
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:59.250 / 2026-11-13T19:41:57.590
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a second-order SQL injection vulnerability in the IPPF contraceptive issue feature because issue_ippf_con_save concatenates layout_options field_id values into a REPLACE INTO query as column names. Authenticated administrators can add a malicious field_id via edit_layout.php, then trigger issue_ippf_con_save through add_edit_issue.php to execute arbitrary SQL.

### 33. CVE-2026-126481｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:57.893)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：0.00526 / percentile=0.45102
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:57.893 / 2026-11-13T19:19:24.300
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a path traversal vulnerability in era_payments.php and sl_eob_search.php that allows authenticated billing users to write files outside the ERA directory. Attackers can embed traversal sequences in the GS04 element of an uploaded X12 835 file to overwrite .edi or .835 files with attacker-controlled content anywhere writable by the web server.

### 34. CVE-2026-126469｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:55.920)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.00555 / percentile=0.46854
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:55.920 / 2026-11-13T20:18:47.900
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a missing authorization vulnerability in several custom/ scripts that rely only on session authentication and never call AclMain::aclCheckCore(). Any authenticated low-privilege user can request export_labworks.php, chart_tracker.php, or export_registry_xml.php to disclose patient SSN, DOB, and insurance data or provider NPI/tax IDs, and forge chart-tracker records.

### 35. CVE-2026-126465｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:55.247)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00438 / percentile=0.38635
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:55.247 / 2026-11-13T20:18:46.833
- **官方描述（原文）**：OpenEMR before 8.5.0 contains an SQL injection vulnerability in the patient portal api/onsiteactivityviews endpoint that allows any authenticated staff user to inject SQL through unquoted Id_BitwiseAnd Criteria values. Attackers can close the bitwise parenthesis and append OR or UNION SELECT clauses to read patient PHI, staff password hashes, MySQL authentication strings, and API tokens.

### 36. CVE-2026-126461｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:54.520)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:54.520 / 2026-11-13T20:18:45.500
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a missing authorization vulnerability in library/ajax/user_settings.php that lets any authenticated user persist arbitrary global configuration overrides. Attackers can POST global:-prefixed keys to re-point external service hosts like CouchDB, eRx, phiMail, or SMTP to attacker-controlled servers, exfiltrating system credentials and patient PHI.

### 37. CVE-2026-126452｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:53.190)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:53.190 / 2026-11-13T20:18:43.337
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a missing authorization vulnerability in diagnosis_full.php that allows authenticated users to delete or clear any billing record by ID. Attackers can supply a target billing ID in the id parameter with delete or clear mode to deactivate other patients' charges and corrupt financial records.

### 38. CVE-2026-126428｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:49.193)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.7 (HIGH)
- **EPSS**：0.00603 / percentile=0.49432
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:49.193 / 2026-11-13T20:18:36.087
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a remote code execution vulnerability that allows authenticated billing users to store attacker-controlled PHP by uploading a malformed ERA file to era_payments.php. Attackers with a database-write primitive such as SQL injection can register a background_services row whose require_once loads the stored .edi file, executing PHP as the web-server user.

### 39. CVE-2026-126416｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:47.163)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00352 / percentile=0.2927
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:47.163 / 2026-11-13T20:18:33.960
- **官方描述（原文）**：OpenEMR before 8.5.0 contains an improper authorization vulnerability in patient_tracker_status.php that allows low-privilege authenticated users to modify other patients' tracker entries by supplying arbitrary tracker_id values. Attackers can post statustype and roomnum parameters with a valid CSRF token to alter patient-flow status, room assignments, and linked calendar appointment state.

### 40. CVE-2026-126303｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:35.457)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.00488 / percentile=0.42562
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:35.457 / 2026-11-13T21:17:41.050
- **官方描述（原文）**：NLTK before 3.10.4 contains an uncontrolled resource consumption vulnerability in SteppingRecursiveDescentParser.parse() that lacks any max_time deadline or step limit. Attackers influencing the grammar can supply an ambiguous self-embedding grammar and short token input to force unbounded top-down search, pinning CPU cores and exhausting worker pools.

### 41. CVE-2026-126299｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:34.747)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.00582 / percentile=0.48336
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:34.747 / 2026-11-13T21:17:40.927
- **官方描述（原文）**：NLTK before 3.10.4 contains a denial of service vulnerability in the CCG lexicon parser fromstring that allows remote attackers to exhaust CPU by supplying wide inputs. Attackers can submit lexicon text with long flat bracket bodies or operator chains, triggering quadratic string re-slicing in matchBrackets and augParseCategory that blocks worker threads.

### 42. CVE-2026-126295｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:34.060)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.0 (HIGH)
- **EPSS**：0.00197 / percentile=0.09557
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:34.060 / 2026-11-13T21:17:40.803
- **官方描述（原文）**：NLTK from 3.10.0 before 3.10.4 contains an arbitrary file read vulnerability in BllipParser that allows attackers to open files outside NLTK data roots by supplying unvalidated model paths. Attackers controlling parser_model, reranker_features, reranker_weights, or from_unified_model_dir() input can make the bllipparser C extension read sensitive files or block on FIFOs and devices.

### 43. CVE-2026-126191｜facelessuser / soupsieve
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T17:17:32.627)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00434 / percentile=0.38224
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T17:17:32.627 / 2026-11-13T19:19:23.660
- **官方描述（原文）**：Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4. Prior to 3.0, the CSS_ESCAPES and IDENTIFIER regular-expression subpatterns can backtrack exponentially on runs of ambiguous digit escapes in an attribute-name or tag position of an otherwise valid selector. The failure occurs during selector compilation through soupsieve.compile() or Beautiful Soup select() before SELECTOR_LIMIT is applied, so an application that accepts untrusted selector strings can have a worker stalled by a short input. This issue is fixed in version 3.0.

### 44. CVE-2026-124014｜Copeland / XWEB EVO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:25.590)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：0.00726 / percentile=0.54666
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:25.590 / 2026-11-13T23:17:14.293
- **官方描述（原文）**：XWEB EVO 4.3.0 through 5.8.8 contains an unauthenticated arbitrary file write vulnerability that allows remote attackers to modify the system configuration file /etc/xwebconfig.json by sending a crafted POST request to config.lua with action=set, which performs no session validation and writes the raw, unvalidated request body. Attackers can tamper with configuration values such as model and plugin fields or trigger a SYSTEM_NOT_CONFIGURED state via the unauthenticated action=get and action=set operations, resulting in configuration tampering and denial of service. This product line reached it's end of service date in March 2026.

### 45. CVE-2026-124013｜Copeland / XWEB EVO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:25.237)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.02785 / percentile=0.86622
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:25.237 / 2026-11-13T20:18:16.630
- **官方描述（原文）**：XWEB EVO 5.6.2 through 5.8.8 contains an authenticated OS command injection vulnerability in the api.lua import_preconfiguration and restore actions, where server_url and related server credential fields are concatenated unescaped into a root curl command executed via io.popen. Attackers can inject malicious shell commands through these unfiltered parameters to achieve arbitrary command execution with root privileges on the underlying system. This product line reached it's end of service date in March 2026.

### 46. CVE-2026-124009｜Copeland / XWEB EVO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:23.960)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：0.02335 / percentile=0.83842
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:23.960 / 2026-11-13T19:19:20.623
- **官方描述（原文）**：XWEB EVO 5.2.3 through 5.8.8 contains an authenticated OS command injection vulnerability that allows authenticated attackers to execute arbitrary commands as root by injecting shell metacharacters into the output device path parameter processed by backup.lua. Attackers can exploit the unescaped concatenation into mount, unzip, and related shell commands run via the wlua interpreter, including through the setuid xwbackup.cgi and xwrestore.cgi interfaces, to achieve full system compromise. This product line reached it's end of service date in March 2026.

### 47. CVE-2026-104204｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T19:17:37.973)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T19:17:37.973 / 2026-11-13T22:17:19.217
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to version 1.6.1, there is a server-side denial-of-service issue affecting the Structured View object implementation. This issue has been patched in versions 1.6.1 and 1.7.0.

### 48. CVE-2024-58406｜Dalian Huatian Software Co., Ltd. / Huatian Dynamic OA8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T16:17:18.497)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T16:17:18.497 / 2026-11-13T23:10:00.153
- **官方描述（原文）**：Huatian Dynamic OA8000 collaborative office system contains an unauthenticated path traversal vulnerability in /OAapp/jsp/trace/ntkodownload.jsp, where the filename request parameter is used to locate a file without restricting access to an intended directory or rejecting traversal sequences. Attackers can supply ../ sequences to read arbitrary files from the server, such as the Tomcat configuration at ROOT/WEB-INF/web.xml, exposing sensitive configuration, source, and credential material that can enable further compromise. Exploitation evidence was first observed by the Shadowserver Foundation on 2024-11-20.

### 49. CVE-2026-95614｜Zenitel / Zenitel Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T16:19:38.853)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T16:19:38.853 / 2026-11-13T20:19:05.260
- **官方描述（原文）**：The host configuration watcher in Zenitel Connect before 1.11.0 applies a rsyslog configuration file written to a data volume that is shared with the hiatus application container, which allows local attackers with write access to the hiatus container filesystem to execute arbitrary OS commands as root on the host operating system via a crafted rsyslog configuration file.

### 50. CVE-2026-95377｜Zenitel / VSFF6
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T16:19:37.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T16:19:37.337 / 2026-11-13T20:19:02.090
- **官方描述（原文）**：OS command injection in the TFTP provisioning module of Zenitel EdgeAudioClient before 9.6.3.0, and 10.x before 10.1.3.0, on VSFF6, VSFF8, VSFF8MP, VSFF8MN, and VSFT devices allows unauthenticated adjacent attackers to execute arbitrary commands as root via a crafted DHCP option 66 (TFTP Server Name) value supplied by a rogue DHCP server on the same network segment. The DHCP-supplied value is passed to a shell without sanitization. Devices using DHCP, the default configuration, are affected on every boot and lease renewal. The same injection is also reachable via the config_update_tftp_server and sw_update_tftp_server configuration fields by an attacker able to modify the device configuration.

### 51. CVE-2026-90908｜Azul Payara / Payara Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T09:16:40.297)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00539 / percentile=0.45903
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T09:16:40.297 / 2026-11-12T22:09:39.233
- **官方描述（原文）**：A vulnerability in the GenericAdminAuthenticator component of Azul Payara Server and Azul Payara Micro allows a remote, unauthenticated attacker to bypass JMX/RMI administrative access restrictions by spoofing the client host address. Successful exploitation can grant administrative access to the MBean server and lead to remote code execution. Azul Payara Micro is affected only when its JMX connector is enabled.

### 52. CVE-2026-82504｜VITEC / EZ TV Platform Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T21:17:48.030)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T21:17:48.030 / 2026-11-13T21:17:48.030
- **官方描述（原文）**：VITEC EZ TV Platform Server before 8.5.0 contains an unrestricted file upload vulnerability in the upload handler that allows unauthenticated remote attackers to upload arbitrary files by supplying a target filename in the X-FILENAME request header with no authentication or file type validation required. Attackers can upload a malicious ASPX file directly to the web-accessible uploads directory, where it is immediately executable by the web server, achieving remote code execution in the context of the web server process. Patches are available for versions 8.3.0, 8.3.1, 8.4.0, and 8.4.1. Users running releases prior to 8.3.0 should upgrade to 8.5.0+.

### 53. CVE-2026-75495｜Shenzhen Cudy Technology Co., Ltd. / TR3000 1.0
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:17.170)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.02568 / percentile=0.8539
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:17.170 / 2026-11-13T10:18:17.170
- **官方描述（原文）**：Cudy TR3000 before 2.5.42 contains an OS command injection vulnerability that allows a malicious or compromised ACS to execute commands as root by supplying a crafted InternetGatewayDevice.User.{i}.Password value. Attackers can send a SetParameterValues request with shell metacharacters that obuspa_system.lua concatenates into a luci.util.exec() command string, gaining root command execution.

### 54. CVE-2026-75491｜Shenzhen Cudy Technology Co., Ltd. / TR3000 1.0
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:16.597)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:16.597 / 2026-11-13T10:18:16.597
- **官方描述（原文）**：Cudy TR3000 before 2.5.42 contains an authentication bypass vulnerability in the Mosquitto plugin auth_plugin_jwt.so that accepts unsigned JWTs using alg none. Attackers holding any Cudy-trusted client certificate can authenticate as admincudydevice on port 8883 and publish batchcmd requests to execute commands as root.

### 55. CVE-2026-63079｜RBH Access Technologies / Integra32 Security Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T16:19:30.253)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T16:19:30.253 / 2026-11-13T16:19:30.253
- **官方描述（原文）**：RBH Access Technologies Integra32 Security Management System 5.1.11 R5.0 contains an unauthenticated deserialization vulnerability in its deprecated .NET Remoting service, exposed on TCP port 2001 via the AxcvcLt.dll library using BinaryServerFormatterSinkProvider at TypeFilterLevel.Full without requiring authentication. A remote unauthenticated attacker can send a malicious serialized gadget payload (such as a ysoserial.net TypeConfuseDelegate chain) to the IntegraURI object endpoint, or exploit MarshalByRefObject/MarshalByValue unmarshalling for arbitrary file read/write and SMB/NTLMv2 credential coercion, to achieve remote code execution as NT AUTHORITY\SYSTEM and fully compromise the host.

### 56. CVE-2026-19422｜Zohocorp / DDI Central
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T13:17:16.347)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.02193 / percentile=0.82744
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T13:17:16.347 / 2026-11-12T19:02:35.830
- **官方描述（原文）**：Zohocorp ManageEngine DDI Central versions below 6301 is affected by an authentication bypass vulnerability in Windows DNS and DHCP agent synchronization APIs, allowing unauthenticated user to impersonate onboarded Windows servers and perform unauthorized DNS and DHCP modifications.

### 57. CVE-2026-129171｜likaia / NginxPulse
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T18:17:42.530)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T18:17:42.530 / 2026-11-13T18:17:42.530
- **官方描述（原文）**：NginxPulse 1.5.0 before 1.6.26 contains an unauthenticated sql injection vulnerability that allows remote attackers to append SQL via the id and locationType parameters of /api/stats/:type. Attackers can close the quoted table-name identifier and use error-based output to read database contents, and read or write server files via PostgreSQL superuser functions.

### 58. CVE-2026-129167｜Seafile / SeaDoc
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T18:17:41.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T18:17:41.910 / 2026-11-13T18:17:41.910
- **官方描述（原文）**：Seafile SeaDoc converter 2.0.4 before 2.0.11 and 3.0.0 before 3.0.8 contains an absolute path traversal vulnerability that allows unauthenticated attackers holding a public share token to execute code. Attackers supply an absolute filename to /api/v1/confluence-to-wiki/ to extract a ZIP from download_url into the Python library path, then trigger the module's import via a file-convert request.

### 59. CVE-2026-129165｜AmidaWare / Tactical RMM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T18:17:41.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T18:17:41.600 / 2026-11-13T22:17:24.647
- **官方描述（原文）**：Tactical RMM 0.17.0 through 1.6.1 contains an arbitrary file read in the /reporting/templates/preview/ endpoint because WeasyPrint resolves file:// links in user-supplied template_md and embeds the files in the returned PDF. Users with report management permission can read the Django SECRET_KEY, reused as the NATS password, and publish runscript commands to every managed agent.

### 60. CVE-2026-129161｜dromara / free-fs
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T18:17:41.007)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T18:17:41.007 / 2026-11-13T22:17:24.523
- **官方描述（原文）**：Dromara free-fs 2.0.1 through 2.3.1 contains an improper restriction of authentication attempts vulnerability that allows unauthenticated attackers to brute-force six-digit password reset codes via PUT /apis/user/forget-password. Attackers can request a code for a known email and submit unlimited guesses during its 300-second lifetime to set a chosen password and take over the account.

### 61. CVE-2026-129126｜OpenKermit / C-Kermit
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T17:17:29.977)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T17:17:29.977 / 2026-11-13T22:14:15.437
- **官方描述（原文）**：C-Kermit before 11.1.515 contains a heap buffer overflow vulnerability in putsrv() in ckcfns.c that allows malicious peers to write past the srvcmd buffer by sending crafted packets. Attackers can use Kermit repeat-count compression in server command, GET, or file-header packets to write attacker-chosen bytes beyond the heap buffer on servers or receiving instances.

### 62. CVE-2026-129125｜OpenKermit / C-Kermit
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T17:17:29.827)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T17:17:29.827 / 2026-11-13T22:14:15.437
- **官方描述（原文）**：C-Kermit 6.0.192 before 11.1.515 contains a remote code execution vulnerability that allows Kermit clients to run shell commands on servers with host commands disabled by abusing REMOTE QUERY evaluation. Attackers can send a REMOTE QUERY invoking the command function, or define a macro via REMOTE ASSIGN and call execute to reach RUN, bypassing the nopush restriction and DISABLE HOST.

### 63. CVE-2026-129124｜OpenKermit / C-Kermit
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T17:17:29.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T17:17:29.670 / 2026-11-13T22:14:15.437
- **官方描述（原文）**：C-Kermit before 11.1.515 contains an OS command injection vulnerability that allows remote clients to execute shell commands by supplying unquoted arguments to REMOTE WHO or REMOTE SPACE. Attackers can append shell metacharacters to arguments passed through WHOCMD or SPACM2 to syscmd(), executing commands on the server host even when DISABLE HOST is set.

### 64. CVE-2026-129110｜nuxsmin / sysPass
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T16:19:00.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T16:19:00.543 / 2026-11-13T16:19:00.700
- **官方描述（原文）**：sysPass 3.0.1 through 3.2.11 contains an authentication bypass vulnerability that allows unauthenticated attackers to reinstall an already-installed instance by POSTing to the install/install handler, which never checks isInstalled(). Attackers can overwrite config.xml, point the application at an attacker-controlled database, create an administrator account, and plant serialized PublicLink gadget chains triggered via account/viewLink to execute commands.

### 65. CVE-2026-128333｜knadh / listmonk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:13.210)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00544 / percentile=0.46221
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:13.210 / 2026-11-13T10:18:13.330
- **官方描述（原文）**：listmonk 6.0.0 before 7.0.0-beta.2 contains an authentication bypass vulnerability in doResetPassword that skips TOTP verification after a password reset. Attackers who can complete a reset, such as by reading the victim's reset email, obtain fully authenticated sessions including Super Admin without the TOTP code.

### 66. CVE-2026-128332｜knadh / listmonk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:13.030)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00455 / percentile=0.39964
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:13.030 / 2026-11-13T18:17:37.663
- **官方描述（原文）**：Listmonk 6.0.0 before 7.0.0-beta.2 contains a 2FA bypass vulnerability that allows attackers with a valid password to brute-force TOTP codes because the attempt counter resets on every new password login. Attackers can repeatedly submit credentials to POST /admin/login to obtain fresh tokens, each allowing 15 more guesses, gaining sessions for 2FA-protected accounts including Super Admin.

### 67. CVE-2026-128049｜OpenMage / magento-lts
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:10.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00226 / percentile=0.13419
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:10.820 / 2026-11-13T15:45:24.843
- **官方描述（原文）**：OpenMage Magento LTS before 20.18.2 and 21.0.0-beta1 before 21.0.0-beta3 contains a cross-site request forgery vulnerability in the admin and storefront OAuth confirm and confirmSimple actions, which accept GET requests without form-key validation. Attackers holding OAuth consumer credentials can lure a logged-in administrator or customer to a crafted confirm URL that authorizes the attacker's request token, then exchange it at /oauth/token for a persistent REST API access token bound to the victim.

### 68. CVE-2026-128047｜OpenMage / magento-lts
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:10.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00591 / percentile=0.48799
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:10.543 / 2026-11-13T19:19:30.223
- **官方描述（原文）**：OpenMage magento-lts before 20.18.2 and 21.0.0-beta pre-releases before 21.0.0-beta3 generate customer email-confirmation keys with md5(uniqid()) and customer and administrator password-reset tokens with the non-cryptographic uniqHash(). Unauthenticated attackers can brute-force the roughly 20-bit confirmation key via the unrate-limited confirmAction endpoint to log in as pending customers, or predict administrator reset tokens after recovering generator state.

### 69. CVE-2026-128046｜OpenMage / magento-lts
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:10.400)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00708 / percentile=0.54009
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:10.400 / 2026-11-13T17:17:27.287
- **官方描述（原文）**：OpenMage magento-lts 20.17.0 before 20.18.2 and 21.0.0-beta1 before 21.0.0-beta3 contains an unrestricted file upload vulnerability because the general/file/protected_extensions blocklist omits phar, php8, and phps. Unauthenticated attackers can upload a .phar file through a product File custom option to a predictable media/custom_options path and request it directly to execute code on servers that map .phar to PHP and serve that directory.

### 70. CVE-2026-128027｜php / frankenphp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:08.563)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00857 / percentile=0.58949
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:08.563 / 2026-11-13T10:18:08.663
- **官方描述（原文）**：FrankenPHP Docker images before 1.1.11 were rebuilt only when new base image tags were created, so security fixes that Alpine, PHP, and Go applied under existing tags were not propagated. Remote attackers could exploit known flaws in the stale system libraries, such as CVE-2025-15467 in libcrypto3, to execute code.

### 71. CVE-2026-128023｜php / frankenphp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:07.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00511 / percentile=0.44171
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:07.930 / 2026-11-13T10:18:08.043
- **官方描述（原文）**：FrankenPHP before 1.13.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to spoof trusted headers by sending dot-form header names that PHP rewrites to underscores. Attackers can send headers like X.Authenticated.User or X.Forwarded.For that map to $_SERVER keys, spoofing user identity, client IP, or scheme.

### 72. CVE-2026-128014｜php / frankenphp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:06.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00746 / percentile=0.55383
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:06.457 / 2026-11-13T10:18:06.583
- **官方描述（原文）**：FrankenPHP standalone static binaries 1.8.0 before 1.13.2 bundle the PHP brotli extension statically linked with Brotli 1.2.0, whose decoder contains an out-of-bounds write (CVE-2026-111497). Unauthenticated remote attackers can send crafted data to applications that pass it to brotli_uncompress_add() to crash the entire FrankenPHP process, and possibly cause memory disclosure or code execution.

### 73. CVE-2026-127277｜Linksys / EA8100
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T02:18:54.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00561 / percentile=0.47207
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T02:18:54.520 / 2026-11-13T02:18:54.667
- **官方描述（原文）**：A security flaw has been discovered in Linksys EA8100 1.0.3.216940. The affected element is an unknown function of the file etc/init.d/service_smbd.sh of the component SMB Service. Performing a manipulation of the argument ANON_ACCESS results in improper initialization. The attack can be initiated remotely. The exploit has been released to the public and may be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 74. CVE-2026-127131｜Alinto / sogo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T16:19:07.807)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00342 / percentile=0.28188
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T16:19:07.807 / 2026-11-12T16:19:07.980
- **官方描述（原文）**：SOGo before 5.12.13 contains a missing rate limiting vulnerability in its web login TOTP verification that allows attackers who already possess a victim's password to brute-force the second-factor code without triggering any lockout. Attackers can send repeated POST requests to /SOGo/connect with wrong verification codes at high speed since failed TOTP attempts never increment the failed-login counter and SOGoMaximumFailedLoginCount does not apply, enabling indefinite guessing across 30-second code windows to bypass two-factor authentication.

### 75. CVE-2026-127111｜Alinto / sogo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T16:19:07.260)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.0033 / percentile=0.26483
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T16:19:07.260 / 2026-11-13T19:19:29.070
- **官方描述（原文）**：SOGo before 5.12.13 contains an improper restriction of excessive authentication attempts vulnerability that allows unauthenticated attackers to reset account passwords by repeatedly guessing secret-question answers via the passwordRecoveryCheck endpoint without lockout or rate limiting. Attackers can submit unlimited candidate answers to obtain a valid recovery JWT, then use it to change the account password without the old credential and log in via the connect endpoint, achieving full account takeover on accounts without TOTP enabled.

### 76. CVE-2026-127079｜OpsTree Solutions / BuildPiper
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:04.113)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.0043 / percentile=0.37761
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:04.113 / 2026-11-13T15:45:24.843
- **官方描述（原文）**：OpsTree BuildPiper before 2.7.0 lacks rate limiting on password-reset OTP verification, allowing unauthenticated attackers to brute force 6-digit OTPs. Attackers can initiate a reset and submit unthrottled guesses to the check_otp endpoint, resetting the target's password and taking over the account.

### 77. CVE-2026-127073｜OpsTree Solutions / BuildPiper
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:03.200)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00506 / percentile=0.43782
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:03.200 / 2026-11-13T19:19:27.837
- **官方描述（原文）**：OpsTree BuildPiper before 2.7.0 contains a privilege escalation vulnerability that allows project users to gain Kubernetes cluster-admin rights by submitting unrestricted manifests through the Additional Manifest feature. Attackers can deploy a ClusterRoleBinding binding a service account to cluster-admin, which the pipeline applies with cluster-wide credentials, granting control over all workloads and secrets.

### 78. CVE-2026-127063｜DataComm / RMM+
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T18:17:39.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00376 / percentile=0.32097
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T18:17:39.760 / 2026-11-13T05:18:39.287
- **官方描述（原文）**：The third-party RMM+ extension for ConnectWise ScreenConnect uses a static API secret by default. The value can be changed by an administrator; however, environments retaining the default value may allow unauthorized access to extension API functionality, including the ability to send commands to managed agents. This issue is specific to the third-party extension and does not affect the ScreenConnect server or client. Scope: This issue affects the third-party RMM+ extension for ConnectWise ScreenConnect. Deployments without the extension are not affected. ScreenConnect server or client software are not impacted.

### 79. CVE-2026-127046｜misp / misp-modules
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T12:18:23.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00474 / percentile=0.41512
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T12:18:23.130 / 2026-11-12T12:18:23.267
- **官方描述（原文）**：The MISP Modules website component contains an information disclosure vulnerability in the external tools management interface. The /external_tools/list endpoint returned stored API keys (the api_key field) in its JSON response via the ExternalTools model serializer. Additionally, the browser-based edit form pre-populated the API key input field with the stored credential value, exposing it in the DOM. The /external_tools/list endpoint is accessible without authentication (the regression tests verify the response for both authenticated and unauthenticated clients), meaning any network-reachable client could retrieve the API keys for all configured external tools. These keys are used by the server to authenticate submissions to external analysis or enrichment services, so their disclosure allows an attacker to impersonate the MISP instance or directly access those external services. The vulnerability also affected the edit workflow: the change_config endpoint previously required the API key to be present and non-empty on every save, forcing the key to round-trip through the client. The browser JavaScript stored the key in a reactive state object and updated the in-memory tool list with the credential value, further increasing the window of exposure in client-side memory and network traffic. Affected component: the website sub-application of MISP Modules, specifically the external_tools module (serializer in models.py, list endpoint, and the external_tools_index.html template). The impact is limited to confidentiality of the stored API keys; no integrity or availability impact on the MISP Modules website itself is indicated by the patch.

### 80. CVE-2026-127016｜misp / misp-modules
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T10:17:28.960)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00661 / percentile=0.5219
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T10:17:28.960 / 2026-11-12T10:17:29.123
- **官方描述（原文）**：The MISP Modules website component exposes external tool management endpoints (add, delete, change status, and change configuration) that did not enforce the optional administrator authentication policy. When ADMIN_PASSWORD was configured in the application environment, the module configuration endpoints correctly required an authenticated administrator session, but the external tools management handlers processed requests from anonymous users without any authorization check. An unauthenticated attacker with network access to the website could add arbitrary external tools, delete existing tools, toggle their active status, and modify their configurations including API keys and ingestion URLs. This inconsistency allowed bypass of the intended access control for the external tools management functionality. The vulnerability is conditional on ADMIN_PASSWORD being set; installations without an admin password intentionally permit open management access by design. The affected component is the external_tools Flask blueprint within the MISP Modules website application.

### 81. CVE-2026-126953｜Shenzhen Cudy Technology Co., Ltd. / TR3000 1.0
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:02.737)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.02568 / percentile=0.8539
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:02.737 / 2026-11-13T10:18:02.737
- **官方描述（原文）**：Cudy TR3000 before 2.5.42 contains an OS command injection vulnerability that allows a malicious or compromised ACS to execute commands as root by supplying an unvalidated InternetGatewayDevice.User.{i}.Username value. Attackers can send a SetParameterValues request with shell metacharacters that set_UserUsername() in obuspa_system.lua passes to os.execute(), gaining root command execution.

### 82. CVE-2026-126945｜diced / zipline
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:01.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00367 / percentile=0.30948
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:01.600 / 2026-11-13T16:18:49.687
- **官方描述（原文）**：Zipline before 4.5.1 contains a stored cross-site scripting vulnerability in the HighlightCode component that renders unescaped file content before highlight.js finishes loading. Authenticated attackers can upload text files containing HTML/JavaScript payloads that execute in viewers' browsers, enabling API calls such as account changes on the victim's behalf.

### 83. CVE-2026-126937｜diced / zipline
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:00.417)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00364 / percentile=0.30706
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:00.417 / 2026-11-13T16:18:47.620
- **官方描述（原文）**：Zipline before 4.6.5 contains a TOCTOU race condition in the POST /api/setup endpoint that allows unauthenticated attackers to create multiple SUPERADMIN accounts by racing concurrent requests before the firstSetup flag is reset. Attackers can send simultaneous requests with spoofed X-Forwarded-For headers during the argon2 hashing window to gain full administrative control of the instance.

### 84. CVE-2026-126837｜MongoDB / Node.js Driver
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T17:17:33.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00205 / percentile=0.10604
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T17:17:33.320 / 2026-11-13T19:19:25.070
- **官方描述（原文）**：A validation flaw in the DNS SRV host discovery of the MongoDB Node.js driver may cause the driver to connect to a host outside the expected domain. For a mongodb+srv:// connection string, the driver checks each host name in the DNS SRV response against the domain of the connection string. The driver then builds the connection address from the original name, in which certain characters end the host name early. An unauthenticated party who can forge or change the DNS SRV response may redirect the connection to a host of their choice. TLS does not prevent this, because the driver verifies the server certificate against the redirected host name. This may result in unintended disclosure of application data and authentication credentials, and in altered query results. Applications that use mongodb:// connection strings are not affected.

### 85. CVE-2026-126378｜givanz / Vvveb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:40.430)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.0082 / percentile=0.57781
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:40.430 / 2026-11-13T10:17:40.557
- **官方描述（原文）**：Vvveb through 1.0.8.6 contains a file upload vulnerability in the theme installer validFile() function that uses strpos() instead of strict path matching. Attackers with admin credentials can upload a ZIP containing a PHP file whose path includes /theme.php to achieve remote code execution on nginx deployments.

### 86. CVE-2026-126377｜givanz / Vvveb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:40.257)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00558 / percentile=0.47071
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:40.257 / 2026-11-13T10:17:40.380
- **官方描述（原文）**：Vvveb before 1.0.9.0 contains an authentication bypass vulnerability in generateCookie() in system/user/user.php that uses loose comparison to validate MD5 cookie hashes. Unauthenticated attackers can brute-force cookie values until the server's MD5 computation yields a 0e magic hash, then forge persistent cookies for account takeover.

### 87. CVE-2026-126315｜frappe / hrms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:37.443)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00553 / percentile=0.46754
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:37.443 / 2026-11-13T21:17:41.427
- **官方描述（原文）**：Frappe HRMS 16.14.0 before 16.20.1 sends product usage events on certain HR transactions without checking the site's telemetry setting, and some events include more detail than needed. During normal use, with no user action, values such as leave type names, claimed amounts and appraisal scores are transmitted even when telemetry is disabled.

### 88. CVE-2026-126280｜nocodb / nocodb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:31.360)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.0029 / percentile=0.21861
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:31.360 / 2026-11-13T10:17:31.360
- **官方描述（原文）**：NocoDB before 2026.08.0 contains a race condition in refresh-token rotation that allows attackers to reuse tokens because UserRefreshToken.ts never checks the affected-row count. Attackers holding a captured refresh token can present it concurrently with the legitimate user to obtain a valid authenticated session, and no reuse event is recorded.

### 89. CVE-2026-126274｜nocodb / nocodb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:30.440)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00367 / percentile=0.30947
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:30.440 / 2026-11-13T16:18:04.687
- **官方描述（原文）**：NocoDB before 2026.08.0 contains a stored cross-site scripting vulnerability that allows authenticated Creator users to inject script by embedding markup in column or table titles. The Delete.vue confirmation dialog renders these titles through an unescaped innerHTML binding, executing script when a victim deletes an external-source table to steal session tokens from localStorage.

### 90. CVE-2026-126273｜nocodb / nocodb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:30.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00476 / percentile=0.4169
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:30.290 / 2026-11-13T10:17:30.290
- **官方描述（原文）**：NocoDB before 2026.09.0 contains a privilege escalation vulnerability in initAdminFromEnv.ts that silently skips super-admin bootstrap when the admin password environment variable is empty. Unauthenticated attackers can call the public signup endpoint first on a fresh instance to receive Creator and Super Admin roles, gaining full administrative control.

### 91. CVE-2026-126269｜nocodb / nocodb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:29.667)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00367 / percentile=0.30948
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:29.667 / 2026-11-13T10:17:29.667
- **官方描述（原文）**：NocoDB before 2026.09.0 contains a stored cross-site scripting vulnerability that allows authenticated Editor users to execute scripts by storing crafted attachment MIME types like text/html;image/png. Attackers can write the value through the records API so the /dltemp signed URL serves HTML inline, stealing session tokens from localStorage to impersonate victims.

### 92. CVE-2026-126265｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:29.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00356 / percentile=0.29806
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:29.003 / 2026-11-13T10:17:29.133
- **官方描述（原文）**：SiYuan 2.1.0 before 3.8.9 contains a flaw where the loginAuth CAPTCHA challenge lives in a signed client-side cookie, allowing reuse of a solved challenge. Attackers can replay the original signed siyuan cookie with distinct wrong access codes to brute-force the code and gain an administrator session.

### 93. CVE-2026-126173｜AutomatorWP / AutomatorWP Webhooks
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-14T05:18:37.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-14T05:18:37.750 / 2026-11-14T05:18:37.887
- **官方描述（原文）**：The AutomatorWP Pro plugin for WordPress' webhook addon is vulnerable to authorization bypass in all versions up to, and including, 1.4.4. This is due to the plugin not properly verifying that a user is authorized to perform an action. This makes it possible for unauthenticated attackers to reset the password of any WordPress account, including administrators, resulting in full account takeover. This is only exploitable when an administrator has configured an automation pairing a Receive Webhook trigger — with an 'Is the user ID' field — to an Update-User action whose User ID field is left blank and whose Password field is mapped to the webhook password tag, which is a documented, supported plugin configuration.

### 94. CVE-2026-126119｜Unknown / Streamit
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T06:16:54.350)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00225 / percentile=0.13251
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T06:16:54.350 / 2026-11-13T19:19:23.517
- **官方描述（原文）**：The Streamit WordPress plugin before 1.3.10 does not perform any authorization or nonce verification on one of its unauthenticated AJAX routes, which invokes an attacker-supplied PHP function with an attacker-supplied argument array, allowing unauthenticated attackers to call arbitrary functions (for example to create an administrator account), leading to privilege escalation and remote code execution.

### 95. CVE-2026-125855｜Elextensions / ELEX WordPress HelpDesk & Customer Ticketing System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T15:17:43.257)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T15:17:43.257 / 2026-11-13T17:17:24.207
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Elextensions ELEX WordPress HelpDesk & Customer Ticketing System elex-helpdesk-customer-support-ticket-system allows Object Injection.This issue affects ELEX WordPress HelpDesk & Customer Ticketing System: from n/a through 3.3.9.

### 96. CVE-2026-125851｜themagnifico52 / Hotel Booking Lite
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T15:17:42.697)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T15:17:42.697 / 2026-11-13T17:17:23.883
- **官方描述（原文）**：Unrestricted Upload of File with Dangerous Type vulnerability in themagnifico52 Hotel Booking Lite hotel-booking-lite allows Upload a Web Shell to a Web Server.This issue affects Hotel Booking Lite: from n/a through 2.5.1.

### 97. CVE-2026-125055｜sameh101 / Chatterbug Forms – Fast, Flexible WordPress Form Builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:28.153)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01141 / percentile=0.67143
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:28.153 / 2026-11-13T23:17:15.190
- **官方描述（原文）**：The Chatterbug Forms – Fast, Flexible WordPress Form Builder plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 1.0.2 via the cbforms_check_form_submissions function. This is due to missing server-side file extension validation in cbforms_check_form_submissions(), where the allowed-type check defaults to the uploaded file's own extension when no field restriction is configured, trivially allowing any extension including .php. This makes it possible for unauthenticated attackers to upload files that may be executable, which makes remote code execution possible. The submission nonce printed inline on every public page containing a Chatterbug form is freely obtainable by unauthenticated visitors and therefore does not constitute an effective access control barrier.

### 98. CVE-2026-124970｜WP BASE / WP BASE Booking
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T15:17:37.683)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T15:17:37.683 / 2026-11-13T17:17:21.103
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WP BASE WP BASE Booking wp-base-booking-of-appointments-services-and-events allows Blind SQL Injection.This issue affects WP BASE Booking: from n/a through 6.5.2.

### 99. CVE-2026-124833｜Unknown / Ahime Image Printer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T06:16:54.057)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00162 / percentile=0.05488
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T06:16:54.057 / 2026-11-13T19:19:22.500
- **官方描述（原文）**：The Ahime Image Printer WordPress plugin through 1.0.0 does not validate the name, extension or type of uploaded files before writing them to disk, allowing unauthenticated attackers to upload arbitrary files, including PHP, and execute code on the server.

### 100. CVE-2026-124822｜Unknown / Easy DragDrop File Uploader
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T06:16:53.960)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00146 / percentile=0.03889
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T06:16:53.960 / 2026-11-13T19:19:22.350
- **官方描述（原文）**：The Easy DragDrop File Uploader WordPress plugin before 1.1.10 does not validate a user-supplied path before deleting it, allowing unauthenticated users to delete arbitrary files and directories on the server, such as wp-config.php.

### 101. CVE-2026-124763｜Unknown / Woocommerce Wishlist
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T06:16:53.870)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.001 / percentile=0.00867
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T06:16:53.870 / 2026-11-13T19:19:22.197
- **官方描述（原文）**：The Woocommerce Wishlist WordPress plugin through 1.1.0 does not have authorisation and CSRF checks in one of its unauthenticated AJAX actions, allowing unauthenticated users to overwrite any site option with the URL of an uploaded image or an empty value, breaking the site (for example by changing its URL or active , or deactivating every Woocommerce Wishlist WordPress plugin through 1.1.0).

### 102. CVE-2026-124415｜Alejandro / Alex Reservations
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T15:17:37.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T15:17:37.130 / 2026-11-13T17:17:20.997
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Alejandro Alex Reservations alex-reservations allows SQL Injection.This issue affects Alex Reservations: from n/a through 2.4.8.

### 103. CVE-2026-124021｜Control Web Panel / Control Web Panel
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T22:17:22.217)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T22:17:22.217 / 2026-11-13T22:17:22.217
- **官方描述（原文）**：Control Web Panel (CWP) before webpanel_version 1.30.6 contains an authorization bypass vulnerability in the validate() function of api/v1/index.php that allows attackers holding a password-recovery token and a predictable legacy signature to obtain valid remote-API authorization without a proper API key. Attackers can exploit this flaw via the POST /cronjobsusers/ endpoint to add arbitrary cron commands and achieve command execution as the affected hosting account, and can also abuse the same token to access global account-list and account-detail routes exposing usernames, contact emails, and password hashes.

### 104. CVE-2026-124020｜Control Web Panel / Control Web Panel
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T22:17:22.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T22:17:22.070 / 2026-11-13T22:17:22.070
- **官方描述（原文）**：Control Web Panel (CWP) before webpanel_version 1.30.6 contains a host header injection vulnerability that allows unauthenticated attackers to manipulate the password-recovery reset URL by injecting the HTTP Host header into the /v1/lostpass/ route's token generation process. Attackers can lure an automated mail-security scanner into visiting the poisoned reset link to exfiltrate the live recovery token, replay it at /login/index.php?acc=newpass to set a new password, and subsequently abuse the File Manager and Crontab modules to achieve command execution as the targeted hosting account.

### 105. CVE-2026-124012｜Copeland / XWEB EVO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:24.970)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00571 / percentile=0.47782
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:24.970 / 2026-11-13T15:17:35.520
- **官方描述（原文）**：XWEB EVO 5.6.2 through 5.8.8 contains a hardcoded credential vulnerability where the Administrator web account is configured to use password_mode daily_password with no stored password, as the Users.authenticate function in lualib_users.lua synthesizes the Administrator configuration without validating any stored secret. Attackers who can derive the MAC-based daily password can authenticate as Administrator to obtain a full admin session on the device. This product line reached it's end of service date in March 2026.

### 106. CVE-2026-124007｜Copeland / XWEB EVO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:23.387)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.02096 / percentile=0.81962
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:23.387 / 2026-11-13T15:17:34.910
- **官方描述（原文）**：XWEB EVO before 5.6.2 contains a pre-authentication OS command injection vulnerability that allows unauthenticated remote attackers to execute arbitrary commands by injecting shell metacharacters into the password field. Attackers can exploit the unescaped interpolation of the password value into the hashpass invocation within login.lua, cleanout.lua, and api.lua to achieve root-level command execution via the setuid wlua interpreter. This product line reached it's end of service date in March 2026.

### 107. CVE-2026-124004｜Copeland / XWEB EVO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:22.367)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00756 / percentile=0.55694
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:22.367 / 2026-11-13T15:17:34.543
- **官方描述（原文）**：XWEB EVO before 5.6.2 contains a hardcoded backdoor password vulnerability that allows unauthenticated remote attackers to gain full administrative access to the built-in Administrator account. Attackers can authenticate using the hardcoded credential xwebevonewgeneration in a single request to obtain a complete admin session and full control over the application. This product line reached it's end of service date in March 2026.

### 108. CVE-2026-123965｜Jet Admin / Jet Admin Cloud Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T18:17:30.933)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T18:17:30.933 / 2026-11-13T22:08:23.607
- **官方描述（原文）**：A prompt injection vulnerability in all versions of Jet Admin Cloud Platform allows a remote attacker with a free account to expose sensitive .env configuration files and exfiltrate critical credentials. Mitigated via sandbox component around October 29, 2026.

### 109. CVE-2026-120869｜Citrix NetScaler / Console
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T14:17:23.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00513 / percentile=0.44324
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T14:17:23.990 / 2026-11-12T22:09:39.233
- **官方描述（原文）**：An unauthenticated attacker can bypass authentication controls to access restricted resources on the Citrix NetScaler Console appliance

### 110. CVE-2026-120868｜Citrix NetScaler / ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T00:20:09.977)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00289 / percentile=0.21682
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T00:20:09.977 / 2026-11-13T00:20:09.977
- **官方描述（原文）**：Memory overflow in Packet Processing can lead to unpredictable or erroneous behavior or Denial of Service in NetScaler ADC and NetScaler Gateway.

### 111. CVE-2026-120864｜Citrix / NetScaler ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T09:17:34.057)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.0031 / percentile=0.24135
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T09:17:34.057 / 2026-11-13T09:17:34.057
- **官方描述（原文）**：Memory overflow in ICA proxy can lead to unpredictable or erroneous behavior or Denial of Service in Citrix NetScaler ADC and Citrix NetScaler Gateway.

### 112. CVE-2026-119077｜elextensions / ELEX WordPress HelpDesk & Customer Ticketing System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:26.483)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:26.483 / 2026-11-13T23:17:13.633
- **官方描述（原文）**：The ELEX WordPress HelpDesk & Customer Ticketing System plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 3.3.9 via the 'form (specifically the attacker-controlled ticket_label field inside the url-encoded form string)' parameter parameter. This is due to missing server-side authentication and the absence of a class allowlist on deserialization, with the only guard being a nonce publicly emitted on any page carrying the [wsdesk_support] shortcode. This makes it possible for unauthenticated attackers to execute code on the server. A successful exploit requires a single anonymous GET to any public page carrying the [wsdesk_support] shortcode to harvest the publicly emitted wsdesk_nonce value, after which a single unauthenticated POST completes the attack.

### 113. CVE-2026-118064｜Unknown / Advance Guest Post
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T06:16:52.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00162 / percentile=0.05489
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T06:16:52.897 / 2026-11-13T19:18:36.110
- **官方描述（原文）**：The Advance Guest Post WordPress plugin through 1.9 does not properly restrict or validate file uploads, authorizing an upload action with a nonce exposed to every front-end visitor and checking only a file's leading bytes, allowing unauthenticated users to upload arbitrary PHP files and execute code remotely. Successful exploitation additionally requires the target to run PHP 7.x; on PHP 8.0 and later the vulnerable code path raises a fatal error before the file is written.

### 114. CVE-2026-118063｜Unknown / Advance Guest Post
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T06:16:52.807)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00213 / percentile=0.11747
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T06:16:52.807 / 2026-11-13T19:18:35.953
- **官方描述（原文）**：The Advance Guest Post WordPress plugin through 1.9 does not properly validate uploaded files, relying on a case-sensitive and incomplete extension check that unauthenticated users can trivially bypass, allowing them to upload arbitrary files, including executable PHP variants, into a web-reachable directory, which can lead to remote code execution depending on the server configuration.

### 115. CVE-2026-117551｜jdownloads.com / jDownloads extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T18:17:15.813)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T18:17:15.813 / 2026-11-12T22:18:33.260
- **官方描述（原文）**：Joomla Extension - jdownloads.com - RCE through file upload in jDownloads < 4.1.8 - Insufficient validation of frontend thumbnail uploads allowed users with upload permission to place executable files on the server. This results in PHP code execution.

### 116. CVE-2026-111334｜Citrix / NetScaler ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T08:17:15.557)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00265 / percentile=0.18617
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T08:17:15.557 / 2026-11-13T08:17:15.557
- **官方描述（原文）**：Memory overflow in Endpoint Analysis (EPA/EPAS) can lead to unpredictable or erroneous behavior or a Denial of Service in Citrix NetScaler ADC and Citrix NetScaler Gateway.

### 117. CVE-2026-110003｜Azul Payara / Payara Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T09:16:39.813)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00654 / percentile=0.519
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T09:16:39.813 / 2026-11-12T22:09:39.233
- **官方描述（原文）**：A vulnerability in the administration REST interface of Azul Payara allows a remote, unauthenticated attacker to bypass secure-admin remote-access restrictions by supplying an arbitrary value in the X-GlassFish-authToken HTTP header. The header's presence waives the remote-rejection check before the token is validated, and an invalid token falls through to password-based authentication, which succeeds without credentials on default domains configured with an empty administrative password. Successful exploitation grants execution of arbitrary administrative commands, equivalent to complete compromise of the server.

### 118. CVE-2026-109445｜PLANET Technology Corp. / PLANET GS-5220-8P2T2S
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T15:17:30.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T15:17:30.290 / 2026-11-13T15:17:30.290
- **官方描述（原文）**：PLANET GS-5220-8P2T2S (hardware version 3.0) firmware versions before 3.2412b261008 contains a stack-based buffer overflow vulnerability that allows unauthenticated attackers to corrupt stack memory by submitting an oversized webstax_auth HTTP Cookie value that is copied into a fixed-size stack buffer without length validation. Attackers can send a crafted unauthenticated HTTP request with an oversized cookie to overwrite the saved return address and corrupt stack memory, leading to memory corruption and potential denial of service on the device.

### 119. CVE-2026-107415｜Citrix / NetScaler ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T04:17:36.417)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00334 / percentile=0.27121
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T04:17:36.417 / 2026-11-13T04:17:36.417
- **官方描述（原文）**：Memory overflow in Email OTP authentication can lead to unpredictable or erroneous behavior or Denial of Service in Citrix NetScaler ADC and Citrix NetScaler Gateway.

### 120. CVE-2026-107412｜Citrix NetScaler / ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T03:17:28.877)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.00305 / percentile=0.23608
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T03:17:28.877 / 2026-11-13T03:17:28.877
- **官方描述（原文）**：Multiple Memory overflow vulnerabilities can lead to unpredictable or erroneous behavior and Denial of Service in Citrix NetScaler ADC and Citrix NetScaler Gateway.

### 121. CVE-2026-107410｜Citrix NetScaler / ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T02:18:49.997)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00359 / percentile=0.30138
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T02:18:49.997 / 2026-11-13T03:17:28.653
- **官方描述（原文）**：Memory overflow in NetScaler Push can lead to unpredictable or erroneous behavior or Denial of Service in Citrix NetScaler

### 122. CVE-2026-107409｜Citrix NetScaler / ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T02:18:49.863)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00359 / percentile=0.30137
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T02:18:49.863 / 2026-11-13T03:17:28.553
- **官方描述（原文）**：Memory corruption in DNS-over-HTTPS (DoH) can lead to unpredictable or erroneous behavior or a Denial of Service in Citrix NetScaler

### 123. CVE-2026-107408｜Citrix NetScaler / ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T02:18:49.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00329 / percentile=0.26392
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T02:18:49.740 / 2026-11-13T03:17:28.447
- **官方描述（原文）**：Memory corruption in DNS / DNS-over-HTTPS (DoH) can lead to unpredictable or erroneous behavior or Denial of Service in Citrix NetScaler

### 124. CVE-2026-107407｜Citrix NetScaler / ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T02:18:49.613)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00329 / percentile=0.26392
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T02:18:49.613 / 2026-11-13T03:17:27.423
- **官方描述（原文）**：Memory overflow in SMPP traffic can lead to unpredictable or erroneous behavior or Denial of Service in Citrix NetScaler

### 125. CVE-2026-107360｜Red Hat / Red Hat Satellite 6.16 for RHEL 8
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T20:18:14.907)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00474 / percentile=0.41556
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T20:18:14.907 / 2026-11-13T17:17:16.507
- **官方描述（原文）**：A flaw was found in rubygem-safemode. Compound assignment expressions in sandboxed code are evaluated without mediating method calls through the Jail allow-list. An authenticated attacker who can supply template content can invoke arbitrary no-argument methods on objects exposed to the template renderer without Jail mediation, including destructive operations such as host deletion and disclosure of non-allow-listed object state.

### 126. CVE-2026-103813｜Dell / PowerStore 500T
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T16:17:21.793)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T16:17:21.793 / 2026-11-14T05:18:14.840
- **官方描述（原文）**：Dell PowerStore contains an OS Command Injection vulnerability. An authenticated user with limited privileges could potentially exploit this vulnerability, potentially leading to privilege escalation to root on the appliance.

### 127. CVE-2026-64675｜bacnet-stack / bacnet-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T19:19:33.463)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T19:19:33.463 / 2026-11-13T22:17:25.573
- **官方描述（原文）**：BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.5 and 1.5.1, a single unauthenticated BACnet/IP UDP datagram (port 47808) triggers an out-of-bounds read in xy_color_decode() (src/bacnet/lighting.c), reachable pre-authentication through two default-registered service handlers: the UnconfirmedRequest WriteGroup service (0x0A) and Confirmed WriteProperty on a BACnetXYColor-typed property. This issue has been patched in versions 1.4.5, 1.5.1, and 1.6.0.

### 128. CVE-2026-128885｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T21:17:45.827)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T21:17:45.827 / 2026-11-13T22:17:23.543
- **官方描述（原文）**：A flaw was found in D-Bus. In configurations where the daemon falls back to using the Unix select() mechanism for event monitoring, it does not verify whether file descriptor numbers exceed allocated limits. A local attacker can exploit this flaw by opening a large number of concurrent connections to trigger an out-of-bounds write on the stack. This can cause the daemon to crash, resulting in a Denial of Service (DoS).

### 129. CVE-2026-128328｜Dokploy / dokploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:12.340)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：0.00438 / percentile=0.38596
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:12.340 / 2026-11-13T19:19:31.910
- **官方描述（原文）**：Dokploy 0.28.0 before 0.31.1 contains a path traversal vulnerability that allows authenticated organization members to list tracked files of any git repository by supplying an arbitrary repoPath to patch.readRepoDirectories. Attackers with read access to one service can enumerate file and directory names of other tenants' application and compose source trees on the host or managed servers.

### 130. CVE-2026-128239｜gpac / gpac
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:11.657)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：0.00172 / percentile=0.06685
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:11.657 / 2026-11-13T23:17:18.230
- **官方描述（原文）**：GPAC through 26.07.0 contains a NULL pointer dereference vulnerability in the MPEG-4 Form spatial-constraint handlers in src/compositor/mpeg4_form.c that lets attackers crash the process via unchecked group lookups. Attackers can supply a crafted XMT scene whose Form constraints reference a non-existent group, crashing tools like MP4Box during chapter import for denial of service.

### 131. CVE-2026-128065｜grpc / grpc-node
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T00:20:14.313)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.00448 / percentile=0.39436
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T00:20:14.313 / 2026-11-13T02:18:56.263
- **官方描述（原文）**：@grpc/grpc-js implements the core functionality of gRPC purely in JavaScript, without a C++ addon. From 1.14.0 through 1.14.1, XdsServer in @grpc/grpc-js-xds can acknowledge Route and VirtualHost resources while failing to apply their RBACPerRoute override configurations. The override parser is not registered under the override message type, override maps are stored under a type URL instead of the configured HTTP filter name, and VirtualHost override maps are not read. When experimental RBAC is enabled and a trusted xDS control plane supplies a broad top-level ALLOW policy with a stricter matching override, affected servers evaluate RPCs under the broad policy and can accept requests that should be denied. This issue is fixed in version 1.14.2.

### 132. CVE-2026-128025｜php / frankenphp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:08.237)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.00305 / percentile=0.236
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:08.237 / 2026-11-13T19:19:29.737
- **官方描述（原文）**：FrankenPHP before 1.13.0 contains a path-split interpretation conflict in splitPos in cgi.go that allows unauthenticated attackers to execute protected PHP scripts by embedding .php inside a filename component. Attackers can request paths like /uploads/a.php.txt/b.php to execute uploads/a.php despite route-level or WAF deny rules and forge PATH_INFO, SCRIPT_NAME, and PHP_SELF values.

### 133. CVE-2026-128021｜php / frankenphp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:07.623)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：0.00297 / percentile=0.22587
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:07.623 / 2026-11-13T19:19:29.610
- **官方描述（原文）**：FrankenPHP before 1.13.2 contains an information disclosure vulnerability that allows later clients to read earlier clients' libxml errors because worker mode never resets LIBXML(error_list) between requests. Attackers sending requests to the same worker thread can call libxml_get_errors() or libxml_get_last_error() to obtain other clients' parsed-document fragments and server filesystem paths.

### 134. CVE-2026-128017｜php / frankenphp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:06.970)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：0.00446 / percentile=0.39276
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:06.970 / 2026-11-13T19:19:29.480
- **官方描述（原文）**：FrankenPHP before 1.13.4 contains a double free vulnerability in worker mode that frees SG(request_info).content_type_dup twice when a worker script ends its loop after a non-form POST request. Unauthenticated attackers can send repeated JSON POST requests until the worker loop ends, aborting the whole process when USE_ZEND_ALLOC=0 is set.

### 135. CVE-2026-127284｜SourceCodester / Food Ordering System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T02:18:55.677)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00263 / percentile=0.18296
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T02:18:55.677 / 2026-11-13T23:17:17.763
- **官方描述（原文）**：A security flaw has been discovered in SourceCodester Food Ordering System 1.0. This affects an unknown part of the file admin/add_category.php of the component Admin Write Handler. Performing a manipulation of the argument title/description/price/current_image/featured/active/id results in sql injection. It is possible to initiate the attack remotely. The exploit has been released to the public and may be used for attacks.

### 136. CVE-2026-127281｜lanyulei / ferry
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T02:18:55.103)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00405 / percentile=0.35323
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T02:18:55.103 / 2026-11-13T18:17:34.283
- **官方描述（原文）**：A vulnerability was found in lanyulei ferry 1.0.0-beta.1/1.0.0. Affected is an unknown function of the file middleware/auth.go of the component JWT Validation. The manipulation results in improper authentication. The attack can be executed remotely. The exploit has been made public and could be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 137. CVE-2026-127279｜AIP-PUB / ACPs-community
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T02:18:54.907)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00397 / percentile=0.34449
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T02:18:54.907 / 2026-11-13T23:17:17.623
- **官方描述（原文）**：A vulnerability was detected in AIP-PUB ACPs-community up to 2.2.0. This impacts an unknown function of the file discovery-server/app/main.py of the component Discovery Server. The manipulation results in missing authentication. The attack may be launched remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure.

### 138. CVE-2026-127209｜Xiaomi / Mi Browser (com.mi.globalbrowser)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T22:19:21.247)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：0.00237 / percentile=0.14838
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T22:19:21.247 / 2026-11-13T02:18:54.190
- **官方描述（原文）**：Xiaomi Mi Browser Android Application (com.mi.globalbrowser) before 14.66.0-gn contains a path traversal vulnerability in the exported ThirdDocViewerActivity component, where CopyExternalFile.copyFromUri() copies content provider streams using an unsanitized filename from the _display_name column without basename reduction or canonical-path checks. A zero-permission co-resident malicious application can supply a crafted content provider with a _display_name containing .. sequences to make the browser write attacker-controlled bytes to an arbitrary path within its external storage directory, escaping the intended cache_docs staging location without requiring user interaction.

### 139. CVE-2026-127207｜Sendcloud / Sendcloud for WooCommerce: Automated Shipping, Branded Tracking & Returns
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T21:17:22.740)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：0.00171 / percentile=0.06623
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T21:17:22.740 / 2026-11-13T20:18:54.357
- **官方描述（原文）**：Sendcloud for WooCommerce through 1.0.41 contains a missing authorization vulnerability that allows authenticated low-privileged users, including Subscribers, to access the sc_support_get and sc_support_save AJAX actions due to the absence of capability and nonce checks in SCCSP_Support_Controller. Attackers can call these wp_ajax_ handlers directly or via cross-site request forgery to disclose integration configuration data such as INTEGRATION_ID, SERVICE_POINT, CARRIERS, and MIN_LOG_LEVEL, and to modify the plugin's logging verbosity. This is an incomplete fix of CVE-2026-57760.

### 140. CVE-2026-127085｜IgnisDa / ryot
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:05.010)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：0.00366 / percentile=0.30863
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:05.010 / 2026-11-13T19:19:28.647
- **官方描述（原文）**：Ryot before 10.5.6 contains an authorization bypass vulnerability that allows authenticated users to remove entries from other users' collections by supplying arbitrary collectionName and creatorUserId values. Attackers can obtain user ids from the usersList query and target fixed collection names like Watchlist to delete collection_to_entity rows belonging to other users.

### 141. CVE-2026-126998｜未確認 / JeecgBoot
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T15:17:49.497)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00463 / percentile=0.40696
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T15:17:49.497 / 2026-11-12T18:17:38.993
- **官方描述（原文）**：A security flaw has been discovered in JeecgBoot up to 3.9.5. This vulnerability affects the function OpenApiController.call of the file /openapi/call of the component Authentication Filter. The manipulation results in server-side request forgery. The attack can be executed remotely. The exploit has been released to the public and may be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 142. CVE-2026-126997｜未確認 / JeecgBoot
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T15:17:49.220)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00452 / percentile=0.39773
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T15:17:49.220 / 2026-11-13T19:19:27.437
- **官方描述（原文）**：A vulnerability was identified in JeecgBoot up to 3.9.6. This affects the function RestTemplate.exchange of the file org/jeecg/modules/airag/flow/c/a.class of the component flow-run Endpoint. The manipulation leads to server-side request forgery. Remote exploitation of the attack is possible. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 143. CVE-2026-126946｜diced / zipline
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:01.747)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：0.00235 / percentile=0.1452
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:01.747 / 2026-11-13T19:19:26.820
- **官方描述（原文）**：Zipline from 4.3.0 before 4.5.0 contains a stored cross-site scripting vulnerability that allows authenticated low-privilege users to inject HTML through unescaped embed settings in SSR meta tags. Attackers can set malicious embedTitle, embedDescription, embedSiteName, or embedColor values via PATCH /api/user to execute JavaScript in browsers of visitors opening their file view pages.

### 144. CVE-2026-126942｜diced / zipline
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:01.170)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：0.00239 / percentile=0.15139
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:01.170 / 2026-11-13T19:19:26.683
- **官方描述（原文）**：Zipline before 4.6.2 contains a missing authorization vulnerability in POST /api/user/folders that allows authenticated users to reparent other users' files by supplying their file IDs. Attackers can harvest file IDs from public folders and create a folder seeded with them, disclosing victims' file URLs and removing those files from their folder views.

### 145. CVE-2026-126493｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:59.930)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 4.8 (MEDIUM)
- **EPSS**：0.00235 / percentile=0.14529
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:59.930 / 2026-11-13T20:18:49.007
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a stored cross-site scripting vulnerability that allows low-privileged patient portal users to inject JavaScript via the tableArgs field of the onsiteportalactivity API. Attackers can store a payload with spaces that breaks out of an unquoted data-delete-id attribute, executing script when providers click the delete button on the audit review page.

### 146. CVE-2026-126485｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:58.587)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：0.00147 / percentile=0.04007
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:58.587 / 2026-11-13T19:19:24.450
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a cross-site request forgery vulnerability in ObservationController::deleteAction that allows attackers to delete observation form records without a CSRF token. Attackers can lure a logged-in clinician to a page issuing a GET to delete.php with guessed id values, soft-deleting observations in the victim's open encounter.

### 147. CVE-2026-126456｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:53.833)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:53.833 / 2026-11-13T20:18:44.403
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a stored cross-site scripting vulnerability in the Fee Sheet notecodes field, which is escaped with the wrong context. Attackers with clinician access can inject a payload that breaks out of the single-quoted value attribute and executes in higher-privileged users' browsers.

### 148. CVE-2026-126448｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:52.500)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：0.00264 / percentile=0.18482
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:52.500 / 2026-11-13T20:18:41.963
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a missing authorization vulnerability that allows authenticated users lacking nationnotes/nn_configure to modify shared Nation Notes templates by calling mutation endpoints directly. Attackers can send requests to ajax_code.php or add_context.php, which lack ACL and CSRF checks, to tamper with clinical-note templates and assignments.

### 149. CVE-2026-126444｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:51.830)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.0 (MEDIUM)
- **EPSS**：0.00273 / percentile=0.19898
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:51.830 / 2026-11-13T20:18:40.637
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a missing authorization vulnerability in the Ensora eRx integration that allows authenticated staff without patients/rx permission to access prescription data by directly requesting eRx.php. Attackers can expose selected patients' demographic, medication, and allergy data in the vendor XML and trigger eRx synchronization state changes.

### 150. CVE-2026-126440｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:51.150)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.0 (MEDIUM)
- **EPSS**：0.00273 / percentile=0.19898
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:51.150 / 2026-11-13T20:18:39.257
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a missing authorization flaw in the Care Coordination CCDA and CCR import controllers, which move a document named by the document_id parameter into the import category without checking access to the source document. Authenticated non-administrators with Care Coordination access can recategorize protected patient documents and then download them through normal ACL-checked retrieval.

### 151. CVE-2026-126432｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:49.867)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.0 (MEDIUM)
- **EPSS**：0.00297 / percentile=0.22649
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:49.867 / 2026-11-13T20:18:37.100
- **官方描述（原文）**：OpenEMR before 8.5.0 contains an improper authorization vulnerability in interface/orders/list_reports.php that allows read-only users to transmit lab orders because the patients/med check ignores write permission. Authenticated attackers can submit form_xmit with arbitrary procedure order IDs to send HL7 orders containing SSNs, insurance, and diagnoses to laboratories and mark them transmitted.

### 152. CVE-2026-126424｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:48.523)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 4.6 (MEDIUM)
- **EPSS**：0.00251 / percentile=0.16744
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:48.523 / 2026-11-13T21:17:43.340
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a stored cross-site scripting vulnerability that allows users with admin/superbill write permission to inject HTML into SNOMED code descriptions via superbill_custom_full.php. When a clinician selects the malicious code, the Functional and Cognitive Status form or fee-sheet forms assign it to innerHTML, executing JavaScript in the clinician's session to read patient data and perform actions.

### 153. CVE-2026-126420｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:47.843)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.0 (MEDIUM)
- **EPSS**：0.00328 / percentile=0.2632
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:47.843 / 2026-11-13T20:18:35.003
- **官方描述（原文）**：OpenEMR before 8.5.0 contains a missing authorization vulnerability in the FaxSMS module's utility.php that allows read-only demographics users to create patient charts. Attackers can submit the form_create request with chosen identity fields to create fictitious or duplicate patients with employer, history, and insurance records.

### 154. CVE-2026-126376｜givanz / Vvveb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:40.093)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：0.0026 / percentile=0.17823
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:40.093 / 2026-11-13T21:17:41.950
- **官方描述（原文）**：Vvveb 1.0.8.4 through 1.0.8.6 contains an incomplete authorization fix that allows low-privilege authors and vendors to access other users' records by bypassing admin_id owner scoping. Attackers can supply filter[admin_id] to list drafts, invoke duplicate() on posts or products, or enumerate every vendor's digital-asset metadata.

### 155. CVE-2026-126323｜givanz / Vvveb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:38.710)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:38.710 / 2026-11-13T21:17:41.693
- **官方描述（原文）**：Vvveb through 1.0.8.6 contains a cross-site request forgery vulnerability that allows attackers to perform admin state-changing actions because checkCsrf() in admin/controller/base.php only validates tokens for POST requests. Attackers can lure a logged-in admin into loading a forged cross-site GET request to delete admin/user accounts, sites, orders, and menus or change comment status.

### 156. CVE-2026-126192｜facelessuser / soupsieve
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T17:17:32.793)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：0.00477 / percentile=0.4175
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T17:17:32.793 / 2026-11-13T02:18:51.393
- **官方描述（原文）**：Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4. Prior to 2.10, matching a developer-authored selector that places the general sibling combinator inside :has() repeatedly scans each candidate element's following siblings when the right-hand side is absent, producing quadratic work on attacker-controlled HTML. Applications that evaluate a fixed selector such as div:has(a ~ b) over untrusted markup can have a worker occupied for minutes by a small document, while the adjacent sibling form and trusted-only document processing are not affected in the same way. This issue is fixed in version 2.10.

### 157. CVE-2026-120490｜checkpoint / Scalable Platforms (ElasticXL, Maestro, Chassis)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T14:17:23.770)
- **Risk**：WATCH / score 21；reasons：EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.8 (LOW)
- **EPSS**：0.08377 / percentile=0.95055
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T14:17:23.770 / 2026-11-12T20:04:52.377
- **官方描述（原文）**：On Scalable Platforms, an administrator with permissions to edit and install the Access Control Policy and NAT rules can create a NAT rule that redirects traffic to the Gateway's Sync interface, bypassing the built-in Sync protection. This could allow the administrator to execute operating system commands and write files on the Gateway with superuser privileges.

### 158. CVE-2026-128348｜exceljs / exceljs
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:18:15.580)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：0.00296 / percentile=0.22473
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:18:15.580 / 2026-11-13T18:17:38.197
- **官方描述（原文）**：ExcelJS through 4.4.0 contains a formula injection vulnerability in the totals row formula getter in lib/doc/table.js that fails to escape [, ], # and ' characters in structured reference column names. Attackers can supply column names containing ] via untrusted input like imported CSV headers to inject formulas such as HYPERLINK that exfiltrate cell values when users open and click the generated workbook.

### 159. CVE-2026-128087｜Eugeny / russh
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T19:19:31.477)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.7 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T19:19:31.477 / 2026-11-13T22:17:22.950
- **官方描述（原文）**：russh is a Rust SSH client and server library that includes an SSH agent protocol implementation. From version 0.55.0 until version 0.65.1, the initial key exchange invokes client::Handler::kex_done() with the raw shared secret before check_server_key() accepts the server host key or certificate. A malicious SSH server can therefore trigger application-defined secondary-channel initialization or early data handling even when the server identity is subsequently rejected. Ordinary clients that keep the callback's no-op default or independently defer callback-derived actions until trust is confirmed are not affected. This issue is fixed in version 0.65.1.

### 160. CVE-2026-127276｜Linksys / EA8100
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T02:18:54.317)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.9 (LOW)
- **EPSS**：0.00518 / percentile=0.44579
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T02:18:54.317 / 2026-11-13T02:18:54.477
- **官方描述（原文）**：A vulnerability was identified in Linksys EA8100 1.0.3.216940. Impacted is an unknown function of the component Web UI. Such manipulation leads to cookie without 'httponly' flag. It is possible to launch the attack remotely. This attack is characterized by high complexity. The exploitability is considered difficult. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 161. CVE-2026-126995｜tjake / Jlama
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T14:17:28.943)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00486 / percentile=0.4237
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T14:17:28.943 / 2026-11-13T02:18:53.277
- **官方描述（原文）**：A vulnerability was found in tjake Jlama up to 0.8.4/0.9.0-beta. Affected by this vulnerability is the function SafeTensorIndex.loadWeights of the file jlama-core/src/main/java/com/github/tjake/jlama/safetensors/SafeTensorIndex.java. Performing a manipulation of the argument weight_map results in path traversal. The attack may be initiated remotely. The exploit has been made public and could be used. The project was informed of the problem early through an issue report but has not responded yet.

### 162. CVE-2026-126994｜未確認 / braindecode
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T13:17:15.690)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00534 / percentile=0.4561
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T13:17:15.690 / 2026-11-12T18:17:38.663
- **官方描述（原文）**：A vulnerability has been found in braindecode up to 1.8.1. Affected is the function resolve_type_kwargs of the file braindecode/models/util.py of the component Model Config Deserialization. Such manipulation of the argument Activation leads to use of externally-controlled input to select classes or code. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. Upgrading to version 2.0.0 is able to address this issue. The name of the patch is 05b764d93b9a50400f523206fbe03d73d0cf5edb. The affected component should be upgraded.

### 163. CVE-2026-126408｜bytecodealliance / wasmtime
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-13T10:17:45.823)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.0 (LOW)
- **EPSS**：0.00178 / percentile=0.07438
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-13T10:17:45.823 / 2026-11-13T21:17:43.083
- **官方描述（原文）**：Wasmtime 47.0.0 before 48.0.8, 49.0.0 before 49.0.5, and 50.0.0 before 50.0.1 contains an insufficient type-check in the TypedFunc embedder API for I31, Option<I31>, and Option<NoneRef> parameter or result types, reaching an unreachable!() path. A malicious guest module exporting a function that uses another anyref-hierarchy type can panic the host embedding, causing denial of service.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-123039｜Check Point / Multiple Products
- **Title**：Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-13 / due_date=2026-11-16
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Check Point Firewall, Multi-Domain Security Management Server, Scalable Platforms, Security Gateway, and Security Management Server contain an incorrect permissions assignment for critical resources vulnerability when the Gaia OS DynamicCLI daemon runs as root and listens on a world-writable local socket without authenticating connecting processes. An authenticated local user can send a command to the socket and have it executed as root.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-114713｜UnrealIRCd / UnrealIRCd
- **Title**：UnrealIRCd Improper Neutralization of Delimiters Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-13 / due_date=2026-11-16
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：UnrealIRCd UnrealIRCd contains an improper neutralization of delimiters vulnerability that allows any user on a network with two or more linked servers to inject server-to-server commands that are executed with server authority.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-75869 | P3 / 39 | Zohocorp / DDI Central | v3.1 8.8 (HIGH) | 0.20352 / percentile=0.97523 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-68548 | P3 / 38 | xyproto / algernon | v3.1 9.4 (CRITICAL) | 0.00754 / percentile=0.55646 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-127275 | P3 / 38 | Linksys / EA8100 | v4.0 9.3 (CRITICAL) | 0.00754 / percentile=0.55656 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-127080 | P3 / 38 | OpsTree Solutions / BuildPiper | v4.0 9.4 (CRITICAL) | 0.00506 / percentile=0.43781 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-126952 | P3 / 38 | diced / zipline | v4.0 9.2 (CRITICAL) | 0.00339 / percentile=0.27755 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-126473 | P3 / 38 | openemr / openemr | v4.0 9.3 (CRITICAL) | 0.00461 / percentile=0.40455 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-126380 | P3 / 38 | givanz / Vvveb | v4.0 9.4 (CRITICAL) | 0.00643 / percentile=0.51394 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-124010 | P3 / 38 | Copeland / XWEB EVO | v4.0 9.3 (CRITICAL) | 0.03095 / percentile=0.87937 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-124006 | P3 / 38 | Copeland / XWEB EVO | v4.0 9.2 (CRITICAL) | 0.00553 / percentile=0.46764 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-124005 | P3 / 38 | Copeland / XWEB EVO | v4.0 9.2 (CRITICAL) | 0.00547 / percentile=0.46394 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-124002 | P3 / 38 | Copeland / XWEB EVO | v4.0 9.3 (CRITICAL) | 0.049 / percentile=0.92228 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-82414 | WATCH / 30 | bacnet-stack / bacnet-stack | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-68551 | WATCH / 30 | teelur / budget-board | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-62973 | WATCH / 30 | bacnet-stack / bacnet-stack | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-52790 | WATCH / 30 | bacnet-stack / bacnet-stack | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-49990 | WATCH / 30 | bacnet-stack / bacnet-stack | v3.1 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-47710 | WATCH / 30 | bacnet-stack / bacnet-stack | v3.1 8.2 (HIGH) | 0.00254 / percentile=0.17032 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-47257 | WATCH / 30 | bacnet-stack / bacnet-stack | v3.1 8.1 (HIGH) | 0.00393 / percentile=0.33926 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-47217 | WATCH / 30 | bacnet-stack / bacnet-stack | v3.1 7.5 (HIGH) | 0.00383 / percentile=0.32862 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-46674 | WATCH / 30 | bacnet-stack / bacnet-stack | v3.1 7.5 (HIGH) | 0.00428 / percentile=0.37599 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-45341 | WATCH / 30 | bacnet-stack / bacnet-stack | v3.1 7.5 (HIGH) | 0.00274 / percentile=0.20066 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-129123 | WATCH / 30 | OpenKermit / C-Kermit | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-129119 | WATCH / 30 | OpenKermit / C-Kermit | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-128344 | WATCH / 30 | exceljs / exceljs | v4.0 8.7 (HIGH) | 0.0063 / percentile=0.50744 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-128340 | WATCH / 30 | exceljs / exceljs | v4.0 8.7 (HIGH) | 0.0063 / percentile=0.50745 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-128082 | WATCH / 30 | LuckyPennySoftware / AutoMapper | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-127076 | WATCH / 30 | OpsTree Solutions / BuildPiper | v4.0 7.1 (HIGH) | 0.00402 / percentile=0.34929 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-126948 | WATCH / 30 | diced / zipline | v4.0 8.7 (HIGH) | 0.00442 / percentile=0.38956 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：28。
- EPSS 未確認：10；Exploitation status 未確認：1。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-14T07:13:03.825629+00:00`；Delta generated at：`2026-11-14T07:13:03.825629+00:00`。

---

## 可驗證資料來源

- **CVE-2026-123039** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123039) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (support.checkpoint.com)](https://support.checkpoint.com/results/sk/sk1000362) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-114713** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114713) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (forums.unrealircd.org)](https://forums.unrealircd.org/viewtopic.php?t=9487) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-75869** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75869) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-75869)
- **CVE-2026-68548** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-68548) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-68548)
- **CVE-2026-127275** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127275) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127275)
- **CVE-2026-127080** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127080) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127080)
- **CVE-2026-126952** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126952) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126952)
- **CVE-2026-126473** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126473) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126473)
- **CVE-2026-126380** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126380) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126380)
- **CVE-2026-124010** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124010) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124010)
- **CVE-2026-124006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124006) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124006)
- **CVE-2026-124005** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124005) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124005)
- **CVE-2026-124002** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124002) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124002)
- **CVE-2026-82414** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82414)
- **CVE-2026-68551** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-68551)
- **CVE-2026-62973** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62973)
- **CVE-2026-52790** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-52790)
- **CVE-2026-49990** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-49990)
- **CVE-2026-47710** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47710) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-47710)
- **CVE-2026-47257** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47257) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-47257)
- **CVE-2026-47217** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47217) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-47217)
- **CVE-2026-46674** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46674) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-46674)
- **CVE-2026-45341** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45341) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-45341)
- **CVE-2026-129123** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129123)
- **CVE-2026-129119** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129119)
- **CVE-2026-128344** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128344) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128344)
- **CVE-2026-128340** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128340) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128340)
- **CVE-2026-128082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128082)
- **CVE-2026-127076** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127076) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127076)
- **CVE-2026-126948** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126948) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126948)
- **CVE-2026-126938** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126938) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126938)
- **CVE-2026-126489** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126489) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126489)
- **CVE-2026-126481** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126481) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126481)
- **CVE-2026-126469** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126469) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126469)
- **CVE-2026-126465** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126465) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126465)
- **CVE-2026-126461** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126461)
- **CVE-2026-126452** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126452)
- **CVE-2026-126428** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126428) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126428)
- **CVE-2026-126416** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126416) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126416)
- **CVE-2026-126303** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126303) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126303)
- **CVE-2026-126299** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126299) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126299)
- **CVE-2026-126295** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126295) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126295)
- **CVE-2026-126191** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126191) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126191)
- **CVE-2026-124014** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124014) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124014)
- **CVE-2026-124013** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124013) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124013)
- **CVE-2026-124009** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124009) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124009)
- **CVE-2026-104204** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104204)
- **CVE-2024-58406** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-58406)
- **CVE-2026-95614** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95614)
- **CVE-2026-95377** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95377)
- **CVE-2026-90908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90908) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90908)
- **CVE-2026-82504** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82504)
- **CVE-2026-75495** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75495) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-75495)
- **CVE-2026-75491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75491)
- **CVE-2026-63079** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63079)
- **CVE-2026-19422** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19422) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-19422)
- **CVE-2026-129171** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129171)
- **CVE-2026-129167** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129167)
- **CVE-2026-129165** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129165)
- **CVE-2026-129161** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129161)
- **CVE-2026-129126** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129126)
- **CVE-2026-129125** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129125)
- **CVE-2026-129124** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129124)
- **CVE-2026-129110** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129110)
- **CVE-2026-128333** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128333) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128333)
- **CVE-2026-128332** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128332) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128332)
- **CVE-2026-128049** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128049) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128049)
- **CVE-2026-128047** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128047) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128047)
- **CVE-2026-128046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128046) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128046)
- **CVE-2026-128027** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128027) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128027)
- **CVE-2026-128023** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128023) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128023)
- **CVE-2026-128014** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128014) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128014)
- **CVE-2026-127277** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127277) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127277)
- **CVE-2026-127131** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127131) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127131)
- **CVE-2026-127111** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127111) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127111)
- **CVE-2026-127079** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127079) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127079)
- **CVE-2026-127073** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127073) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127073)
- **CVE-2026-127063** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127063) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127063)
- **CVE-2026-127046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127046) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127046)
- **CVE-2026-127016** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127016) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127016)
- **CVE-2026-126953** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126953) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126953)
- **CVE-2026-126945** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126945) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126945)
- **CVE-2026-126937** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126937) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126937)
- **CVE-2026-126837** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126837) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126837)
- **CVE-2026-126378** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126378) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126378)
- **CVE-2026-126377** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126377) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126377)
- **CVE-2026-126315** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126315) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126315)
- **CVE-2026-126280** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126280) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126280)
- **CVE-2026-126274** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126274) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126274)
- **CVE-2026-126273** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126273) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126273)
- **CVE-2026-126269** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126269) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126269)
- **CVE-2026-126265** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126265) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126265)
- **CVE-2026-126173** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126173)
- **CVE-2026-126119** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126119) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126119)
- **CVE-2026-125855** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125855)
- **CVE-2026-125851** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125851)
- **CVE-2026-125055** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125055) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-125055)
- **CVE-2026-124970** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124970)
- **CVE-2026-124833** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124833) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124833)
- **CVE-2026-124822** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124822) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124822)
- **CVE-2026-124763** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124763) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124763)
- **CVE-2026-124415** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124415)
- **CVE-2026-124021** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124021)
- **CVE-2026-124020** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124020)
- **CVE-2026-124012** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124012) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124012)
- **CVE-2026-124007** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124007) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124007)
- **CVE-2026-124004** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124004) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124004)
- **CVE-2026-123965** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123965)
- **CVE-2026-120869** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120869) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-120869)
- **CVE-2026-120868** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120868) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-120868)
- **CVE-2026-120864** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120864) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-120864)
- **CVE-2026-119077** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119077)
- **CVE-2026-118064** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118064) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-118064)
- **CVE-2026-118063** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118063) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-118063)
- **CVE-2026-117551** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-117551)
- **CVE-2026-111334** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111334) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111334)
- **CVE-2026-110003** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110003) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-110003)
- **CVE-2026-109445** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109445)
- **CVE-2026-107415** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107415) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107415)
- **CVE-2026-107412** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107412) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107412)
- **CVE-2026-107410** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107410) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107410)
- **CVE-2026-107409** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107409) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107409)
- **CVE-2026-107408** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107408) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107408)
- **CVE-2026-107407** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107407) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107407)
- **CVE-2026-107360** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107360) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107360)
- **CVE-2026-103813** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103813)
- **CVE-2026-64675** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-64675)
- **CVE-2026-128885** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128885)
- **CVE-2026-128328** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128328) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128328)
- **CVE-2026-128239** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128239) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128239)
- **CVE-2026-128065** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128065) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128065)
- **CVE-2026-128025** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128025) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128025)
- **CVE-2026-128021** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128021) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128021)
- **CVE-2026-128017** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128017) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128017)
- **CVE-2026-127284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127284) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127284)
- **CVE-2026-127281** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127281) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127281)
- **CVE-2026-127279** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127279) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127279)
- **CVE-2026-127209** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127209) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127209)
- **CVE-2026-127207** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127207) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127207)
- **CVE-2026-127085** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127085) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127085)
- **CVE-2026-126998** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126998) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126998)
- **CVE-2026-126997** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126997) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126997)
- **CVE-2026-126946** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126946) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126946)
- **CVE-2026-126942** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126942) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126942)
- **CVE-2026-126493** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126493) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126493)
- **CVE-2026-126485** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126485) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126485)
- **CVE-2026-126456** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126456)
- **CVE-2026-126448** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126448) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126448)
- **CVE-2026-126444** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126444) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126444)
- **CVE-2026-126440** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126440) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126440)
- **CVE-2026-126432** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126432) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126432)
- **CVE-2026-126424** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126424) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126424)
- **CVE-2026-126420** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126420) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126420)
- **CVE-2026-126376** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126376) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126376)
- **CVE-2026-126323** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126323)
- **CVE-2026-126192** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126192) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126192)
- **CVE-2026-120490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120490) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-120490)
- **CVE-2026-128348** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128348) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128348)
- **CVE-2026-128087** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128087)
- **CVE-2026-127276** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127276) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-127276)
- **CVE-2026-126995** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126995) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126995)
- **CVE-2026-126994** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126994) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126994)
- **CVE-2026-126408** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126408) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126408)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
