# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**72** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=1、NEW_CVE=69、NEW_KEV=2。
- Intelligence 候選：**30** 筆；P1 **2**、P2 **0**、P3 **3**、WATCH **25**。
- Baseline：state / generated_at=2026-10-29T06:38:47.695264+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-97229、CVE-2026-76418。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **72** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-97229｜GitLab / Community Edition and Enterprise Edition
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.18427 / percentile=0.97229
- **CISA KEV**：listed=true / date_added=2026-10-29 / due_date=2026-11-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-13T02:17:00.840 / 2026-10-30T04:18:31.240
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.

### 2. CVE-2026-76418｜Cisco / Secure Firewall ASA Software and Cisco Secure FTD Software
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-29 / due_date=2026-11-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-28T20:18:47.063 / 2026-10-30T04:18:24.797
- **官方描述（原文）**：Cisco Secure Firewall ASA Software and Cisco Secure FTD Software contains an unchecked return value to NULL pointer dereference vulnerability that could allow an unauthenticated, remote attacker to cause the device to reload unexpectedly, resulting in a denial of service (DoS) condition.

### 3. CVE-2026-107058｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T17:17:58.620)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T17:17:58.620 / 2026-10-29T20:17:25.220
- **官方描述（原文）**：An issue in Shelter versionCode 445 allows attackers to register their own auth_key and execute a takeover of another user's binder service API and preference state.

### 4. CVE-2026-107032｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:48.943)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:48.943 / 2026-10-29T21:17:10.497
- **官方描述（原文）**：Insecure permissions in Bulk Share : Location Sender v2.1.0 (versionCode 5) allows unauthorized attackers to invoke an exported component, leading to arbitrary data access and control of data flow.

### 5. CVE-2026-107015｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T15:17:15.200)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T15:17:15.200 / 2026-10-29T20:17:24.567
- **官方描述（原文）**：Insecure permissions in Simple Contacts Pro versionCode 107 allow unauthorized attackers to write and read notes in another user's' note database.

### 6. CVE-2026-119195｜pyasn1 / pyasn1
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T20:17:30.633)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T20:17:30.633 / 2026-10-29T21:17:18.553
- **官方描述（原文）**：pyasn1 is a generic ASN.1 library for Python. Prior to 0.6.5, constructed string and indefinite-length ANY decoding repeatedly concatenates each fragment onto a growing bytes value. Attacker-controlled BER or CER data can use many constructed OCTET STRING or character-string fragments. DER rejects constructed OCTET STRING without a schema, but accepts its definite-length form when asn1Spec selects univ.OctetString; it also accepts constructed character strings such as UTF8String without a schema, even though those encodings are not valid DER. The separate indefinite-length ANY path is reachable in BER and CER when asn1Spec selects univ.Any; DER rejects indefinite lengths. OctetStringPayloadDecoder uses growing header concatenation and AnyPayloadDecoder.indefLenValueDecoder uses growing chunk concatenation, repeatedly copying an increasing prefix and causing quadratic work. A sufficiently fragmented value can occupy decoding workers and cause CPU exhaustion without confidentiality or integrity impact. This issue is fixed in version 0.6.5.

### 7. CVE-2026-119190｜digitalbazaar / forge
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T20:17:30.067)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T20:17:30.067 / 2026-10-29T21:17:18.450
- **官方描述（原文）**：Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, node-forge parsed deprecated extension OIDs 2.5.29.10 and 2.5.29.13 as basicConstraints, and pki.verifyCertificateChain() used the first extension with that name. Exploitation requires a CA trusted by the application to issue a certificate carrying an attacker-supplied deprecated-OID extension, commonly because the CA copies extensions from a certificate signing request. By placing a permissive deprecated extension before the genuine 2.5.29.19 basicConstraints extension, the certificate holder could have the certificate accepted as a CA and issue certificates for arbitrary names, enabling server or client impersonation. If the issuing CA adds a keyUsage extension without keyCertSign, node-forge rejects the chain. This issue is fixed in version 1.4.1.

### 8. CVE-2026-119118｜unclecode / crawl4ai
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:04.027)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:04.027 / 2026-10-29T21:17:17.480
- **官方描述（原文）**：Crawl4AI before 0.9.5 contains an improper certificate validation vulnerability that allows network attackers to intercept crawls because Chromium always launches with --ignore-certificate-errors. Man-in-the-middle or DNS-controlling attackers can serve forged content to the crawler and read cookies and headers sent, while hard-coded --no-sandbox also overrides CRAWL4AI_CHROMIUM_SANDBOX.

### 9. CVE-2026-118779｜digitalbazaar / forge
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T19:17:20.560)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T19:17:20.560 / 2026-10-29T21:17:17.287
- **官方描述（原文）**：Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, the affected implementation used pem.decode(), lib/pem.js, missing END line to process the relevant input or security decision. node-forge used polynomial-time regular expressions in pem.decode(), including when searching for a matching END line and parsing encapsulated headers. An unauthenticated attacker able to supply PEM input to any high-level parser could consume excessive CPU with a long malformed message and cause denial of service. This issue is fixed in version 1.4.1.

### 10. CVE-2026-107052｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T17:17:57.920)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T17:17:57.920 / 2026-10-29T20:17:25.060
- **官方描述（原文）**：Insecure permissions in the AIDL interface of ProjectMAXS MAXS Module FileRead versionCode 27 allows unauthorized attackers to arbitrarily reead files outside of the sandbox via providing an absolute path.

### 11. CVE-2026-107047｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T17:17:57.223)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T17:17:57.223 / 2026-10-29T20:17:24.890
- **官方描述（原文）**：Insecure permissions in mendhak GPSLogger versionCode 137 allows unauthorized attackers to arbitrarily manipulate the app's logging mechanism and log data.

### 12. CVE-2026-107042｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:50.050)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:50.050 / 2026-10-29T20:17:24.737
- **官方描述（原文）**：Insecure permissions in USP Ultimate Screenshot Painter versionCode 240213.009 allows unauthorized attackers to move or overwrite files in another user's private storage via supplying a crafted content URI.

### 13. CVE-2026-107037｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:49.490)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:49.490 / 2026-10-29T21:17:10.660
- **官方描述（原文）**：Insecure permissions in the NotificationHelper component of NoNonsense Notes versionCode 72600 allows unauthorized attackers to write in another user's notes via supplying a note id.

### 14. CVE-2026-107026｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:48.383)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:48.383 / 2026-10-29T21:17:10.340
- **官方描述（原文）**：Insecure permissions in Share to Clipboard v1.14.1 (versionCode 32) allows unauthorized attackers to arbitrarily overwrite another user's clipboard content.

### 15. CVE-2026-107020｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T15:17:15.780)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T15:17:15.780 / 2026-10-29T21:17:10.180
- **官方描述（原文）**：An issue in the activity.LoadLinkLaterActivity component of FeedEx / Handy News Reader versionCode 116 allows attackers to force victim users into fetching a crafted URL.

### 16. CVE-2026-97854｜Yamaha Corporation / NWR100
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T12:17:14.443)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T12:17:14.443 / 2026-10-29T15:45:15.310
- **官方描述（原文）**：Yamaha wireless LAN router NWR100 provided by Yamaha Corporation contains an OS command injection vulnerability. Arbitrary OS commands may be executed by sending a specially crafted request to the affected product.

### 17. CVE-2026-93680｜IBM / Langflow OSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:20:06.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:20:06.040 / 2026-10-30T04:18:29.947
- **官方描述（原文）**：IBM Langflow OSS 1.0.0 through 1.12.8 could allow a remote attacker to bypass security restrictions due to improper authentication.

### 18. CVE-2026-90868｜Progress Software / WS_FTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:20:04.963)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:20:04.963 / 2026-10-30T04:18:29.410
- **官方描述（原文）**：An OS command injection vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Windows could allow arbitrary command execution under certain configurations.

### 19. CVE-2026-90866｜Progress Software / WS_FTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:20:04.690)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:20:04.690 / 2026-10-30T04:18:29.170
- **官方描述（原文）**：A path traversal vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Windows could allow a delegated Host Administrator to access locations outside their authorized scope, potentially enabling remote code execution.

### 20. CVE-2026-90865｜Progress Software / WS_FTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:20:04.570)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:20:04.570 / 2026-10-30T04:18:29.047
- **官方描述（原文）**：An OS command injection vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Windows could allow arbitrary command execution with elevated privileges under certain configurations.

### 21. CVE-2026-90864｜Progress Software / WS_FTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:20:04.453)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:20:04.453 / 2026-10-30T04:18:28.927
- **官方描述（原文）**：A path traversal vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Windows could allow a delegated Host Administrator to access or modify files outside their authorized scope.

### 22. CVE-2026-90863｜Progress Software / WS_FTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:20:04.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:20:04.337 / 2026-10-30T04:18:28.807
- **官方描述（原文）**：Missing authorization in the administrative interface of Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Windows could allow a delegated Host Administrator to exceed their authorized scope, potentially enabling arbitrary command execution with elevated privileges and complete compromise of the underlying server.

### 23. CVE-2026-84295｜Progress Software / WS_FTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:19:29.860)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:19:29.860 / 2026-10-30T04:18:25.237
- **官方描述（原文）**：Improper authentication in Progress Software WS_FTP Server versions prior to 2024.0.6 and 2025.0.3 on Windows could allow an unauthenticated remote attacker to access sensitive information, including administrative credentials.

### 24. CVE-2026-62131｜Zoho Flow / Zoho Flow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:14.800)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:14.800 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Zoho Flow <= 2.14.5 versions.

### 25. CVE-2026-62018｜ThemeREX / Gunslinger
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:14.643)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:14.643 / 2026-10-29T20:17:32.290
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Gunslinger <= 1.11 versions.

### 26. CVE-2026-62017｜ThemeREX / Good Homes
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:14.513)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:14.513 / 2026-10-29T18:17:34.470
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Good Homes <= 1.3.13 versions.

### 27. CVE-2026-62016｜ThemeREX / Gamic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:14.387)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:14.387 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Gamic <= 1.19 versions.

### 28. CVE-2026-62015｜ThemeREX / Gamezone
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:14.263)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:14.263 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Gamezone <= 1.1.11 versions.

### 29. CVE-2026-62014｜ThemeREX / EmojiNation
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:14.143)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:14.143 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in EmojiNation <= 1.0.12 versions.

### 30. CVE-2026-62013｜ThemeREX / Edge Decor
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:14.027)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:14.027 / 2026-10-29T20:17:32.170
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Edge Decor <= 2.9 versions.

### 31. CVE-2026-62012｜ThemeREX / Coinpress
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:13.907)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:13.907 / 2026-10-29T18:17:34.370
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Coinpress <= 1.0.15 versions.

### 32. CVE-2026-62011｜ThemeREX / Bonbon
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:13.787)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:13.787 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Bonbon <= 1.11 versions.

### 33. CVE-2026-62010｜ThemeREX / Avventure
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:13.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:13.670 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Avventure <= 1.1.12 versions.

### 34. CVE-2026-62009｜ThemeREX / Filmax
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:13.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:13.543 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Filmax <= 1.1.11 versions.

### 35. CVE-2026-62008｜ThemeREX / Orpheus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:13.427)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:13.427 / 2026-10-29T20:17:32.073
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Orpheus <= 1.8 versions.

### 36. CVE-2026-62006｜ThemeREX / Nuts
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:13.310)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:13.310 / 2026-10-29T18:17:34.273
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Nuts <= 1.12 versions.

### 37. CVE-2026-62005｜ThemeREX / Muzicon
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:13.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:13.190 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Muzicon <= 1.15 versions.

### 38. CVE-2026-62004｜ThemeREX / Motorix
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:13.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:13.070 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Motorix <= 1.11 versions.

### 39. CVE-2026-62003｜ThemeREX / Mission
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:12.950)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:12.950 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Mission <= 1.22 versions.

### 40. CVE-2026-62002｜ThemeREX / Meals & Wheels
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:12.823)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:12.823 / 2026-10-29T20:17:31.980
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Meals & Wheels <= 1.1.13 versions.

### 41. CVE-2026-62001｜ThemeREX / Marcell
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:12.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:12.693 / 2026-10-29T18:17:34.173
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Marcell <= 1.2.14 versions.

### 42. CVE-2026-61998｜ThemeREX / Le Truffe
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:12.580)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:12.580 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Le Truffe <= 1.1.7 versions.

### 43. CVE-2026-61997｜ThemeREX / Legal Stone
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:12.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:12.457 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Legal Stone <= 1.2.11 versions.

### 44. CVE-2026-61992｜Von Eyal Fitoussi / GEO my WordPress
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:11.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:11.820 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in GEO my WordPress <= 4.5.5.3 versions.

### 45. CVE-2026-61991｜Ajax Load More / AjaxLoadMore Cache
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:11.463)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:11.463 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated Remote Code Execution (RCE) in AjaxLoadMore Cache <= 3.1.1 versions.

### 46. CVE-2026-61707｜socfortress / CoPilot
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T22:17:05.603)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T22:17:05.603 / 2026-10-29T22:17:05.603
- **官方描述（原文）**：SOCFortress CoPilot focuses on providing a single pane of glass for all your security operations needs. Prior to 0.1.76, in the reported deployment, case-report templates uploaded by `customer_user`, the lowest-privilege portal role, are later executed by non-sandboxed Jinja2 engines when an admin or analyst generates a report. The `/case-report-template/upload` route in `backend/app/incidents/routes/db_operations.py` validates only the filename-derived MIME type, not the template content. Templates share a global store without customer_code scoping, and `customer_user` can also list, download and delete them, allowing an attacker to replace a legitimate default template under the same name. In `backend/app/incidents/services/reports.py`, `render_document_with_context` uses `DocxTemplate` without a sandbox; in `backend/app/incidents/services/reports_pdf.py`, `render_html_template` uses a non-sandboxed `Environment` without autoescaping. Normal privileged requests to `POST /api/incidents/report/generate-report-docx` or `/generate-report-pdf` therefore evaluate attacker-controlled Jinja expressions as Python on the backend. The reported deployment executes commands as root, exposing all tenants' incident and SIEM data and stored connector credentials. The HTML/PDF wkhtmltopdf renderer additionally permits local-file reads and requests to internal services. This issue is fixed in version 0.1.76.

### 47. CVE-2026-61645｜docat-org / docat
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T22:17:04.963)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T22:17:04.963 / 2026-10-29T22:17:04.963
- **官方描述（原文）**：Docat is a tool for hosting versioned static documentation. In the affected implementation, an arbitrary file upload vulnerability in the `Upload API` arises because the API does not validate the `uploaded file path or type`. An attacker can overwrite sensitive configuration files or place malicious files on the Docat web server. Depending on deployment context, uploaded content can enable remote code execution or cross-site scripting intended to steal cookies or redirect users to malicious websites. Version 1.6.0 mitigates filename-based path traversal; remediation of unrestricted file types or deployment-dependent malicious-content effects is not established by the verified patch.

### 48. CVE-2026-54860｜ThemeREX / Ozisti
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:10.220)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:10.220 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Ozisti <= 1.1.10 versions.

### 49. CVE-2026-54859｜ThemeREX / Preservation
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:10.097)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:10.097 / 2026-10-29T20:17:31.677
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Preservation <= 1.15 versions.

### 50. CVE-2026-54858｜ThemeREX / Printy
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:09.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:09.980 / 2026-10-29T18:17:33.120
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Printy <= 1.13.0 versions.

### 51. CVE-2026-54857｜ThemeREX / Quirky
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:09.860)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:09.860 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Quirky <= 1.23 versions.

### 52. CVE-2026-54856｜ThemeREX / RexCoin
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:09.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:09.740 / 2026-10-29T16:20:19.663
- **官方描述（原文）**：Unauthenticated PHP Object Injection in RexCoin <= 1.2.6 versions.

### 53. CVE-2026-119145｜frappe / frappe
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:08.277)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:08.277 / 2026-10-29T17:18:08.053
- **官方描述（原文）**：Frappe before 15.121.0 and 16.x before 16.34.0 contains a path traversal vulnerability because certain file-upload handling does not validate the destination path before writing to disk. Authenticated attackers can upload crafted files to locations outside the intended storage directory to achieve remote code execution on the server.

### 54. CVE-2026-119128｜zitadel / zitadel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:05.643)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:05.643 / 2026-10-29T16:18:05.760
- **官方描述（原文）**：ZITADEL 4.0.0 before 4.19.5 contains an authentication bypass vulnerability in the Login V2 UI that allows unauthenticated attackers to set the first credential of users lacking any authentication method. Attackers can compute a valid verificationCheck cookie from the user ID and browser fingerprint to set a password, register a passkey, or link an identity provider, taking over the account.

### 55. CVE-2026-119050｜agno-agi / agno
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T14:17:51.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T14:17:51.990 / 2026-10-29T14:17:52.113
- **官方描述（原文）**：Agno through 3.1.11 contains an unsafe reflection vulnerability in PandasTools that allows attackers to invoke arbitrary pandas functions by supplying model-controlled function names to getattr(). Attackers can use prompt injection to make the agent call pandas.read_pickle on attacker-controlled paths for code execution, or call other readers to read local files.

### 56. CVE-2026-118769｜randombit / botan
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T18:17:29.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T18:17:29.180 / 2026-10-29T21:17:17.080
- **官方描述（原文）**：Botan is a C++ cryptography library. From 2.1.0 until 3.13.0, the Botan C API function botan_block_cipher_block_size converted a size_t block size to int without a bounds check. In an application that accepts external algorithm parameter strings and uses the FFI raw ECB mode, an attacker can select the variable-block-size Lion cipher so that the reported size is truncated, the caller allocates insufficient memory, and later block processing causes memory corruption. The C++ API and normally used C API modes such as CBC and CTR are unaffected. This issue is fixed in version 3.13.0.

### 57. CVE-2026-118762｜monkeytypegame / monkeytype
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T17:18:07.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T17:18:07.070 / 2026-10-29T17:18:07.200
- **官方描述（原文）**：Monkeytype is a minimalistic and customizable typing test. Prior to 26.43.0, the .github/workflows/fix-formatting.yml workflow runs on pull_request_target with repository write permissions, checks out a fork pull request, installs dependencies from the fork's package.json, and invokes the fork-controlled oxfmt binary. Because actions/checkout persists the elevated GITHUB_TOKEN in Git configuration until after untrusted code executes, an external contributor whose pull request receives the format label can run arbitrary code, read or exfiltrate the token, and push repository content or modify pull requests and issues. The issue affects the repository CI workflow, not the Monkeytype application or user data. This issue is fixed in version 26.43.0.

### 58. CVE-2026-115964｜StylemixThemes / Motors
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T11:17:31.220)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T11:17:31.220 / 2026-10-29T14:56:26.107
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in StylemixThemes Motors motors-car-dealership-classified-listings allows Blind SQL Injection.This issue affects Motors: from n/a through 1.4.126.

### 59. CVE-2026-114358｜Radius Synergies / Radius Xenia M2M Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T09:17:07.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00502 / percentile=0.42884
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T09:17:07.910 / 2026-10-29T15:45:15.310
- **官方描述（原文）**：This vulnerability exists in the Radius Xenia M2M Platform due to insufficient validation of user supplied input in the password recovery functionality in the web management interface. An unauthenticated remote attacker could exploit this vulnerability by supplying crafted SQL query through input fields to the targeted system. Successful exploitation of this vulnerability could allow the attacker to gain unauthorized access to sensitive information, enumerate database structure or modify database records on the targeted system.

### 60. CVE-2026-112256｜OpenText / Advanced Authentication Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:58.390)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:58.390 / 2026-10-29T16:29:56.553
- **官方描述（原文）**：Acceptance of extraneous untrusted data with trusted data vulnerability in OpenText Advanced Authentication Server allows Accessing Functionality Not Properly Constrained by ACLs. This issue affects Advanced Authentication Server: from 6.4.0.0 through 6.4.3.8, from 6.5.0.0 through 6.5.0.10, and from 6.6.0.0 through 6.6.1.0.

### 61. CVE-2026-111732｜RT-Labs / P-Net
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:57.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:57.480 / 2026-10-29T16:26:37.430
- **官方描述（原文）**：P-Net before 1.0.3, when built with PNET_OPTION_AR_VENDOR_BLOCKS enabled, parses a data length from a field of the ARVendorBlock request that is not part of the block definition and uses it as the number of bytes to copy into a fixed-size buffer, without comparing it with the buffer size or the block length. A crafted Connect request causes an out-of-bounds write. This can lead to a crash (denial of service) or potentially arbitrary code execution. This option is disabled by default.

### 62. CVE-2026-110186｜IBM / Langflow OSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:55.837)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:55.837 / 2026-10-30T04:18:07.693
- **官方描述（原文）**：IBM Langflow OSS 1.0.0 through 1.12.8 could allow a remote attacker to execute arbitrary code due to improper control of code generation.

### 63. CVE-2026-107329｜IBM / Langflow OSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:50.633)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:50.633 / 2026-10-30T04:18:03.613
- **官方描述（原文）**：IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to improper control of code generation.

### 64. CVE-2026-107328｜IBM / Langflow OSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:50.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:50.480 / 2026-10-30T04:18:02.890
- **官方描述（原文）**：IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to improper neutralization of code in eval/exec.

### 65. CVE-2026-107327｜IBM / Langflow OSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:50.330)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:50.330 / 2026-10-30T04:18:01.257
- **官方描述（原文）**：IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to missing authorization.

### 66. CVE-2026-104339｜IBM / Langflow OSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:17:44.403)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:17:44.403 / 2026-10-30T04:17:40.963
- **官方描述（原文）**：IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote attacker to execute arbitrary code due to improper neutralization of special elements used in an OS command.

### 67. CVE-2026-103093｜ServiceNow / ServiceNow AI Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T19:17:15.113)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T19:17:15.113 / 2026-10-29T21:17:08.327
- **官方描述（原文）**：ServiceNow has remediated a sandbox escape security issue that was identified in the ServiceNow AI Platform. This vulnerability could enable an authenticated user with the admin role to bypass Rhino sandbox restrictions and execute arbitrary code on the underlying host operating system, potentially enabling further unintended access. ServiceNow deployed an update to hosted instances, and ServiceNow provided the update to our partners and self-hosted customers. We are not currently aware of malicious exploitation against ServiceNow instances. We recommend customers promptly apply appropriate updates or upgrade to a patched release if they have not already done so.

### 68. CVE-2023-22793｜Veeam / Management Pack for Microsoft System Center
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T23:16:54.270)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T23:16:54.270 / 2026-10-29T23:16:54.270
- **官方描述（原文）**：A vulnerability allowing an unauthenticated attacker to perform remote code execution (RCE) on servers running the Veeam Virtualization Extensions service of Veeam Management Pack for Microsoft System Center.

### 69. CVE-2026-119186｜digitalbazaar / forge
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T20:17:29.500)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T20:17:29.500 / 2026-10-29T21:17:18.350
- **官方描述（原文）**：Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, node-forge did not validate the AES-GCM tagLength option passed to start() during decryption through forge.cipher.createDecipher(). When an application derived tagLength from received data or used an unset or zero-like configuration value, a value that converted to zero together with an empty or missing authentication tag caused the calculated and supplied tags to compare as empty, so decipher.finish() accepted unauthenticated ciphertext. Applications that omit tagLength to use the 128-bit default or pass a fixed valid tag length are unaffected. This issue is fixed in version 1.4.1.

### 70. CVE-2026-119122｜unclecode / crawl4ai
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T16:18:04.683)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T16:18:04.683 / 2026-10-29T21:17:17.590
- **官方描述（原文）**：Crawl4AI before 0.9.5 contains a blind server-side request forgery vulnerability in the Docker server that allows API clients to bypass the egress proxy by enabling check_cache_freshness. Attackers can cache a controlled URL, then trigger CacheValidator to follow 302 redirects or DNS rebinding to internal and cloud-metadata addresses for port and service discovery.

### 71. CVE-2026-118775｜digitalbazaar / forge
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T19:17:20.007)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.7 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T19:17:20.007 / 2026-10-29T21:17:17.180
- **官方描述（原文）**：Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, asn1.oidToDer() in lib/asn1.js did not range-check the first two arcs of an OID. An application that accepted an untrusted OID string, checked or authorized that string, and then encoded it with asn1.oidToDer() could emit DER representing a different, trusted OID from the one that was checked. DER parsing is not affected. This issue is fixed in version 1.4.1.

### 72. CVE-2026-114615｜authlib / authlib
- **Delta event**：CVSS_CHANGED (from=7.4; to=9.1)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00194 / percentile=0.09073
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T22:18:04.257 / 2026-10-29T14:50:19.033
- **官方描述（原文）**：Authlib is a Python library which builds OAuth and OpenID Connect servers. From 1.3.1 until 1.9.0, OctKey.import_key() checks asymmetric-key markers only at byte zero while Authlib's PEM loaders accept leading whitespace, comments, or a byte-order mark. In deployments that use the documented mixed algorithm registry and already configure verification with PEM or certificate bytes containing such a prefix, an unauthenticated attacker who knows those same public-key bytes can use them as an HMAC secret and forge HS256 tokens with arbitrary identity or authorization claims. This is a bypass of the remediation for CVE-2024-37568. The module-level jwt object reaches OctKey.import_key() in authlib/jose/rfc7518/oct_key.py, where POSSIBLE_UNSAFE_KEYS fails to identify prefixed asymmetric key material. This issue is fixed in version 1.9.0.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-97229｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.18427 / percentile=0.97229
- **CISA KEV**：listed=true / date_added=2026-10-29 / due_date=2026-11-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-76418｜Cisco / Secure Firewall ASA Software and Cisco Secure FTD Software
- **Title**：Cisco Secure Firewall ASA Software and Cisco Secure FTD Software Unchecked Return Value to NULL Pointer Dereference Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-29 / due_date=2026-11-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Secure Firewall ASA Software and Cisco Secure FTD Software contains an unchecked return value to NULL pointer dereference vulnerability that could allow an unauthenticated, remote attacker to cause the device to reload unexpectedly, resulting in a denial of service (DoS) condition.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-107058 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107032 | P3 / 38 | 未確認 / 未確認 | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107015 | P3 / 38 | 未確認 / 未確認 | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-119195 | WATCH / 30 | pyasn1 / pyasn1 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-119190 | WATCH / 30 | digitalbazaar / forge | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-119118 | WATCH / 30 | unclecode / crawl4ai | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-118779 | WATCH / 30 | digitalbazaar / forge | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107052 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107047 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107042 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107037 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107026 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107020 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97854 | WATCH / 28 | Yamaha Corporation / NWR100 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93680 | WATCH / 28 | IBM / Langflow OSS | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-90868 | WATCH / 28 | Progress Software / WS_FTP Server | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-90866 | WATCH / 28 | Progress Software / WS_FTP Server | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-90865 | WATCH / 28 | Progress Software / WS_FTP Server | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-90864 | WATCH / 28 | Progress Software / WS_FTP Server | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-90863 | WATCH / 28 | Progress Software / WS_FTP Server | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-84295 | WATCH / 28 | Progress Software / WS_FTP Server | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-62131 | WATCH / 28 | Zoho Flow / Zoho Flow | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-62018 | WATCH / 28 | ThemeREX / Gunslinger | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-62017 | WATCH / 28 | ThemeREX / Good Homes | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-62016 | WATCH / 28 | ThemeREX / Gamic | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-62015 | WATCH / 28 | ThemeREX / Gamezone | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-62014 | WATCH / 28 | ThemeREX / EmojiNation | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-62013 | WATCH / 28 | ThemeREX / Edge Decor | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：9；缺少 Product：9；缺少 Title：28。
- EPSS 未確認：29；Exploitation status 未確認：4。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-30T06:39:06.211109+00:00`；Delta generated at：`2026-10-30T06:39:06.211109+00:00`。

---

## 可驗證資料來源

- **CVE-2026-97229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97229) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97229) · [Vendor / Advisory (ruby-lang.org)](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-76418** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76418) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tunnel-dos-s6mgkb75) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-107058** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107058)
- **CVE-2026-107032** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107032)
- **CVE-2026-107015** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107015)
- **CVE-2026-119195** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119195)
- **CVE-2026-119190** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119190)
- **CVE-2026-119118** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119118)
- **CVE-2026-118779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118779)
- **CVE-2026-107052** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107052)
- **CVE-2026-107047** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107047)
- **CVE-2026-107042** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107042)
- **CVE-2026-107037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107037)
- **CVE-2026-107026** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107026)
- **CVE-2026-107020** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107020)
- **CVE-2026-97854** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97854)
- **CVE-2026-93680** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93680)
- **CVE-2026-90868** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90868)
- **CVE-2026-90866** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90866)
- **CVE-2026-90865** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90865)
- **CVE-2026-90864** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90864)
- **CVE-2026-90863** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90863)
- **CVE-2026-84295** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84295)
- **CVE-2026-62131** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62131)
- **CVE-2026-62018** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62018)
- **CVE-2026-62017** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62017)
- **CVE-2026-62016** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62016)
- **CVE-2026-62015** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62015)
- **CVE-2026-62014** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62014)
- **CVE-2026-62013** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62013)
- **CVE-2026-62012** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62012)
- **CVE-2026-62011** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62011)
- **CVE-2026-62010** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62010)
- **CVE-2026-62009** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62009)
- **CVE-2026-62008** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62008)
- **CVE-2026-62006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62006)
- **CVE-2026-62005** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62005)
- **CVE-2026-62004** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62004)
- **CVE-2026-62003** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62003)
- **CVE-2026-62002** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62002)
- **CVE-2026-62001** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62001)
- **CVE-2026-61998** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61998)
- **CVE-2026-61997** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61997)
- **CVE-2026-61992** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61992)
- **CVE-2026-61991** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61991)
- **CVE-2026-61707** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61707)
- **CVE-2026-61645** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61645)
- **CVE-2026-54860** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54860)
- **CVE-2026-54859** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54859)
- **CVE-2026-54858** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54858)
- **CVE-2026-54857** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54857)
- **CVE-2026-54856** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54856)
- **CVE-2026-119145** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119145)
- **CVE-2026-119128** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119128)
- **CVE-2026-119050** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119050)
- **CVE-2026-118769** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118769)
- **CVE-2026-118762** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118762)
- **CVE-2026-115964** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115964)
- **CVE-2026-114358** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114358) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114358)
- **CVE-2026-112256** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112256)
- **CVE-2026-111732** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111732)
- **CVE-2026-110186** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110186)
- **CVE-2026-107329** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107329)
- **CVE-2026-107328** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107328)
- **CVE-2026-107327** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107327)
- **CVE-2026-104339** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104339)
- **CVE-2026-103093** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103093)
- **CVE-2023-22793** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-22793)
- **CVE-2026-119186** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119186)
- **CVE-2026-119122** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119122)
- **CVE-2026-118775** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118775)
- **CVE-2026-114615** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114615) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114615)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
