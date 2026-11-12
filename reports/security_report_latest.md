# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**39** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=39。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **0**、WATCH **30**。
- Baseline：state / generated_at=2026-11-11T07:22:39.370628+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **39** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-85632｜Sipay Electronic Money and Payment Services Inc. / WooCommerce Virtual POS Module
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T15:17:25.163)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T15:17:25.163 / 2026-11-11T15:17:25.163
- **官方描述（原文）**：Missing authentication for critical function and Improper validation of integrity check value vulnerability in Sipay Electronic Money and Payment Services Inc. WooCommerce Virtual POS Module allows Authentication Bypass and Application API Message Manipulation via Man-in-the-Middle. This issue affects WooCommerce Virtual POS Module: from 26.8.3 before 26.9.1.

### 2. CVE-2026-8333｜Microchip / TimePictra
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T07:16:49.413)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T07:16:49.413 / 2026-11-12T07:16:49.413
- **官方描述（原文）**：A stored cross-site scripting vulnerability in Microchip the TimePictra platform could allow an authenticated, low-privileged attacker to store malicious script content that executes when another user views the affected page

### 3. CVE-2026-78287｜Staggs / STAGGS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T11:17:21.293)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T11:17:21.293 / 2026-11-11T11:17:21.420
- **官方描述（原文）**：Improper Control of Generation of Code ('Code Injection') vulnerability in Staggs STAGGS staggs allows Remote Code Inclusion.This issue affects STAGGS: from n/a through 3.3.0.

### 4. CVE-2026-76954｜Synology / DiskStation Manager (DSM)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T04:17:20.407)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T04:17:20.407 / 2026-11-12T04:17:20.407
- **官方描述（原文）**：An improper neutralization of special elements used in an SQL command vulnerability in the Auth API in Synology DiskStation Manager (DSM) before 7.2.1-69057-13, 7.2.2-72806-10, 7.3.2-86009-5, and 7.4.1-90080-1 allows remote attackers to read or write arbitrary files and conduct denial-of-service attacks.

### 5. CVE-2026-67449｜Portabase / portabase
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:28.257)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:28.257 / 2026-11-11T22:17:28.257
- **官方描述（原文）**：Portabase is a database backup and restore tool for PostgreSQL, MySQL, MsSQL, MariaDB, Firebird SQL, SQLite, MongoDB, Redis, Files and Docker Volume. Prior to version 1.21.2, a path traversal in the TUS upload webhook handler (app/api/tus/hooks/route.ts) allowed an unauthenticated attacker to overwrite arbitrary files under the private data directory, including /data/private/keys/master_key.bin (the AES-256-GCM master key). This issue has been patched in version 1.21.2.

### 6. CVE-2026-65840｜getfider / fider
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T19:17:43.937)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T19:17:43.937 / 2026-11-11T19:17:43.937
- **官方描述（原文）**：Fider is a feedback portal for feature requests and suggestions. Prior to version 0.36.0, in multi-tenant mode (HOST_MODE=multi), an attacker can use an email verification key issued by Tenant A to authenticate as the same email address on Tenant B. This completely bypasses tenant isolation and allows unauthorized account takeover across tenants. Single-host deployments (HOST_MODE=single, the default) are NOT affected. This issue has been patched in version 0.36.0.

### 7. CVE-2026-126812｜blueprintue / blueprintue-self-hosted-edition
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T21:16:45.690)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T21:16:45.690 / 2026-11-11T21:16:45.690
- **官方描述（原文）**：blueprintUE Self-Hosted Edition before 4.3.7 contains an insecure default configuration in its Docker Compose examples that sets MYSQL_ALLOW_EMPTY_PASSWORD=yes in database.env and publishes MariaDB on port 3306. Unauthenticated attackers reaching the Docker host on port 3306 can log in as root without a password to read, modify, or delete user accounts, blueprints, and all databases.

### 8. CVE-2026-126806｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T21:16:44.583)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T21:16:44.583 / 2026-11-11T21:16:44.747
- **官方描述（原文）**：WWBN AVideo 14.3 through 29.7.1 contains a stored cross-site scripting vulnerability that allows uploaders to inject scripts via the videoDownloadedLink value stored unescaped through objects/aVideoEncoder.json.php. Attackers can embed event-handler payloads in the URL host rendered as a Source tag in view/managerVideos_body.php, executing in administrator sessions to install plugin archives containing PHP.

### 9. CVE-2026-126800｜hydro-dev / @hydrooj/ui-default
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T21:16:43.507)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T21:16:43.507 / 2026-11-11T21:16:43.507
- **官方描述（原文）**：Hydro @hydrooj/ui-default before 4.59.1 contains a stored cross-site scripting vulnerability that allows registered users to inject script by placing double quotes in language- class tokens within markdown-it-xss.ts. Attackers can store a payload in their profile bio that executes when administrators or other users view it, stealing the non-httpOnly sid session cookie for session hijacking.

### 10. CVE-2026-126797｜tongcheng-security-team / NextScan
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T21:16:43.027)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T21:16:43.027 / 2026-11-11T21:16:43.027
- **官方描述（原文）**：NextScan 1.1.0 through 1.2.0 contains an authentication bypass vulnerability in ns-admin that allows unauthenticated attackers to forge administrator tokens using a hardcoded JWT signing key. Attackers can sign an HS256 X-Access-Token carrying the public super administrator role ID to gain full access to user management, scan tasks and stored vulnerability results.

### 11. CVE-2026-126785｜rmalright / TR-VISION HOME
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T01:17:11.603)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T01:17:11.603 / 2026-11-12T01:17:11.760
- **官方描述（原文）**：A vulnerability has been found in rmalright TR-VISION HOME 2.0.5. Impacted is the function sub_11504 in the library WFanManager.sys of the component IOCTL Handler. Such manipulation leads to incorrect default permissions. The attack must be carried out locally. The vendor was contacted early about this disclosure but did not respond in any way.

### 12. CVE-2026-126777｜Traccar / Traccar
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T19:17:38.497)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T19:17:38.497 / 2026-11-11T19:17:38.627
- **官方描述（原文）**：Traccar 3.15 before 6.17.0 contains an authentication bypass vulnerability in LdapProvider.login() that fails to reject empty passwords, causing LDAP binds to be performed as unauthenticated binds when LDAP authentication is enabled. Unauthenticated attackers who know a valid username can log in via POST /api/session or HTTP Basic authentication with an empty password against directories that permit unauthenticated binds, obtaining sessions for any account including administrators.

### 13. CVE-2026-126768｜OpsTree Solutions / REMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T19:17:37.140)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T19:17:37.140 / 2026-11-11T19:17:37.140
- **官方描述（原文）**：OpsTree REMS through 1.0.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to obtain valid JWTs by setting the client-controlled is_local_auth field. Attackers can send a POST /api/v1/user/login/ request for the admin account with an invalid password and is_local_auth true to gain SuperUser administrative access.

### 14. CVE-2026-126537｜SaturdayDrive / Ninja Forms - File Uploads
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T13:17:23.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T13:17:23.810 / 2026-11-11T13:17:23.940
- **官方描述（原文）**：The Ninja Forms - File Uploads add-on for WordPress is vulnerable to Arbitrary File Deletion (and arbitrary file read via S3/Dropbox/Google Drive exfiltration) in versions up to, and including, 3.3.36. The flaw spans NF_FU_Fields_Upload::process() in includes/fields/upload.php — which returns early (leaving the client-supplied files[] intact) whenever a public submission carries a nonempty extra.saveProgress — and NF_FU_External_Abstracts_Service::process_upload() in includes/external/abstracts/service.php, whose authoritative-path reload only fires when the client sends upload_id. By omitting upload_id, an attacker's data[file_path] survives into the Background Upload queue and is used by both upload_file_to_s3() (as SourceFile) and the maybe_delete_server_file() unlink() call in includes/external/abstracts/backgroundupload.php, with no canonicalization or upload-directory containment check (the plugin's own is_path_within_upload_dir() helper is only applied on admin paths). This makes it possible for unauthenticated attackers to delete arbitrary files on the affected site's server which may make remote code execution possible — specifically, deleting wp-config.php forces WordPress into its setup screen, enabling full site takeover.

### 15. CVE-2026-126325｜PTC / Windchill
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T15:17:22.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T15:17:22.510 / 2026-11-11T15:17:22.510
- **官方描述（原文）**：A critical remote code execution (RCE) vulnerability has been reported in PTC Windchill and PTC FlexPLM. The vulnerability may be exploited through the deserialization of untrusted data.

### 16. CVE-2026-126263｜Fortinet / FortiMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:26.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:26.520 / 2026-11-11T22:17:26.520
- **官方描述（原文）**：A improper neutralization of special elements used in an sql command ('sql injection') vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.4, FortiMail 7.4.0 through 7.4.6 may allow an authenticated attacker to execute unauthorized code or commands via specifically crafted requests.

### 17. CVE-2026-126262｜Fortinet / FortiAnalyzer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:26.343)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:26.343 / 2026-11-11T22:17:26.343
- **官方描述（原文）**：A improper neutralization of special elements used in an sql command ('sql injection') vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 through 7.6.7, FortiAnalyzer 7.4.0 through 7.4.11, FortiAnalyzer 7.2.0 through 7.2.12, FortiManager 8.0.0, FortiManager 7.6.0 through 7.6.7, FortiManager 7.4.0 through 7.4.11, FortiManager 7.2.0 through 7.2.12 may allow an unauthenticated attacker who has access to the oftp port to execute code or command on the system via crafted OFTP packets.

### 18. CVE-2026-126259｜Fortinet / FortiOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:26.200)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:26.200 / 2026-11-11T22:17:26.200
- **官方描述（原文）**：A missing authentication for critical function vulnerability in Fortinet FortiOS 8.0.0, FortiOS 7.6.0 through 7.6.7, FortiOS 7.4.0 through 7.4.12, FortiOS 7.2.0 through 7.2.13 may allow an unauthenticated attacker with HA FGSP + standalone-config-sync, or autoscale to execute command as super admin via crafted HA packets.

### 19. CVE-2026-126257｜Fortinet / FortiAuthenticator
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:25.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:25.930 / 2026-11-11T22:17:25.930
- **官方描述（原文）**：A use of hard-coded password vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0 through 6.6.10 may allow an unauthenticated attacker to bypass credential validation in certain circumstances outside of the attacker's control and gain unauthorized access.

### 20. CVE-2026-126254｜Fortinet / FortiOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:25.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:25.490 / 2026-11-11T22:17:25.490
- **官方描述（原文）**：A numeric truncation error vulnerability in Fortinet FortiOS 8.0.0 through 8.0.1, FortiOS 7.6.0 through 7.6.7, FortiOS 7.4.0 through 7.4.12, FortiOS 7.2.0 through 7.2.13 may allow a configured ibgp neighbor to send malicious/malformed attributes to all connected routers via a specially crafted request

### 21. CVE-2026-126253｜Fortinet / FortiOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:25.347)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:25.347 / 2026-11-11T22:17:25.347
- **官方描述（原文）**：A authentication bypass by primary weakness vulnerability in Fortinet FortiOS 8.0.0 through 8.0.1, FortiOS 7.6.0 through 7.6.7, FortiOS 7.4.0 through 7.4.12, FortiOS 7.2.0 through 7.2.13 may allow an unauthenticated attacker to broadcast LSA via specially crafted request

### 22. CVE-2026-126251｜Fortinet / FortiAuthenticator
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:25.087)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:25.087 / 2026-11-11T22:17:25.087
- **官方描述（原文）**：A incorrect authorization vulnerability in Fortinet FortiAuthenticator 8.0.0 through 8.0.3, FortiAuthenticator 6.6.0 through 6.6.10 may allow an attacker to bypass authentication and gain unauthorized access.

### 23. CVE-2026-126229｜Fortinet / FortiManager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:21.447)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:21.447 / 2026-11-11T22:17:21.447
- **官方描述（原文）**：A authorization bypass through user-controlled key vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.1, FortiAnalyzer 7.6.0 through 7.6.7, FortiAnalyzer 7.4.0 through 7.4.11, FortiAnalyzer 7.2 all versions, FortiAnalyzer Cloud 8.0.1, FortiAnalyzer Cloud 7.6.0 through 7.6.7, FortiAnalyzer Cloud 7.4.1 through 7.4.11, FortiAnalyzer Cloud 7.2 all versions, FortiManager 8.0.0 through 8.0.1, FortiManager 7.6.0 through 7.6.7, FortiManager 7.4.0 through 7.4.11, FortiManager 7.2 all versions, FortiManager Cloud 8.0.1, FortiManager Cloud 7.6.0 through 7.6.7, FortiManager Cloud 7.4.1 through 7.4.11, FortiManager Cloud 7.2 all versions may allow an authenticated administrator to access to other VDOMs via specially crafted HTTP requests.

### 24. CVE-2026-126170｜Fortinet / FortiManager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:15.340)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:15.340 / 2026-11-11T22:17:15.340
- **官方描述（原文）**：A improper encoding or escaping of output vulnerability in Fortinet FortiAnalyzer 8.0.0 through 8.0.2, FortiAnalyzer 7.6.0 through 7.6.7, FortiAnalyzer Cloud 8.0.1 through 8.0.2, FortiAnalyzer Cloud 7.6.0 through 7.6.7, FortiAnalyzer-BigData 7.6.0 through 7.6.2, FortiManager 8.0.0 through 8.0.2, FortiManager 7.6.0 through 7.6.7, FortiManager Cloud 8.0.1 through 8.0.2, FortiManager Cloud 7.6.0 through 7.6.7 may allow an unauthenticated attacker to execute unauthorized code or commands via a specially crafted HTTP request

### 25. CVE-2026-126164｜Fortinet / FortiMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:14.537)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:14.537 / 2026-11-11T22:17:14.537
- **官方描述（原文）**：A improper neutralization of special elements used in an sql command ('sql injection') vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiMail 7.4.0 through 7.4.8, FortiMail 7.2 all versions may allow an unauthenticated attacker to execute unauthorized code or commands via crafted requests.

### 26. CVE-2026-126157｜Fortinet / FortiMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:13.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:13.587 / 2026-11-11T22:17:13.587
- **官方描述（原文）**：A improper authentication vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiMail 7.4.0 through 7.4.8, FortiMail 7.2 all versions may allow an unauthenticated attacker to gain access to other users' secure email accounts via crafted HTTP requests.

### 27. CVE-2026-126156｜Fortinet / FortiMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:13.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:13.450 / 2026-11-11T22:17:13.450
- **官方描述（原文）**：A authorization bypass through user-controlled key vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiMail 7.4.0 through 7.4.8, FortiMail 7.2 all versions may allow an unauthenticated remote attacker to take over an arbitrary IBE recipient account via crafted HTTP requests.

### 28. CVE-2026-126155｜Fortinet / FortiMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:13.323)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:13.323 / 2026-11-11T22:17:13.323
- **官方描述（原文）**：A incorrect authorization vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiMail 7.4.0 through 7.4.8, FortiMail 7.2 all versions may allow an unauthenticated remote attacker to obtain an authenticated IBE webmail session as any IBE recipient and read or send their encrypted mail via crafted HTTP requests.

### 29. CVE-2026-126150｜Fortinet / FortiMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:12.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:12.543 / 2026-11-11T22:17:12.543
- **官方描述（原文）**：A weak password recovery mechanism for forgotten password vulnerability in Fortinet FortiMail 8.0.0, FortiMail 7.6.0 through 7.6.5, FortiMail 7.4.0 through 7.4.7, FortiMail 7.2.0 through 7.2.9 may allow an unauthenticated attacker to reset the password of an arbitrary IBE webmail user and take over their account via specially crafted HTTP requests.

### 30. CVE-2026-126148｜Fortinet / FortiMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:12.010)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:12.010 / 2026-11-11T22:17:12.010
- **官方描述（原文）**：A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6 may allow an unauthenticated attacker to execute unauthorized code or commands via crafted HA join-request packets.

### 31. CVE-2026-126147｜Fortinet / FortiMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T22:17:11.880)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T22:17:11.880 / 2026-11-11T22:17:11.880
- **官方描述（原文）**：A improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiMail 7.4.0 through 7.4.8, FortiMail 7.2 all versions may allow an unauthenticated attacker to execute unauthorized code or commands via crafted requests.

### 32. CVE-2026-12591｜Zohocorp / M365 Manager Plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T07:16:47.260)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T07:16:47.260 / 2026-11-12T07:16:47.260
- **官方描述（原文）**：Zohocorp ManageEngine M365 Manager Plus versions below 4818 is affected by an authenticated technician may exploit insufficient permission validation in the delegated administration interface to escalate privileges beyond their intended scope, which could result in remote code execution during administrative processing.

### 33. CVE-2026-12507｜Zohocorp / AssetExplorer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-12T07:16:46.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-12T07:16:46.750 / 2026-11-12T07:16:46.750
- **官方描述（原文）**：Zohocorp ManageEngine AssetExplorer versions below 7860, ServiceDesk Plus versions below 15290, ServiceDesk Plus MSP versions below 15150, and SupportCenter Plus versions below 15150 are affected by a authenticated remote code execution vulnerability in the Reports module. An authenticated user with the Create Query Reports permission could exploit specially crafted database queries to execute arbitrary commands on the underlying server.

### 34. CVE-2026-123710｜Red Hat / Red Hat Quay 3
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T15:17:18.340)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T15:17:18.340 / 2026-11-11T15:17:18.480
- **官方描述（原文）**：A flaw was found in Red Hat Quay. An unauthenticated client can obtain an anonymous registry token with an audience it controls, present that token to the service key rotation endpoint, and install its own approved signing key with no expiry. Registry tokens signed with that key are accepted for any repository, allowing read and write access to private images and replacement of repository tags.

### 35. CVE-2026-121374｜Checkmk GmbH / Checkmk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T11:17:14.377)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T11:17:14.377 / 2026-11-11T11:17:14.487
- **官方描述（原文）**：Argument injection in the Kubernetes special agent in Checkmk <2.5.0p19, <2.4.0p40, and 2.3.0 (EOL) allows a user with permission to edit rules in at least one folder to write files to arbitrary locations writable by the site user via crafted node roles in the "Exclude nodes based on their role" rule option, leading to code execution as the site user.

### 36. CVE-2026-120495｜Checkmk GmbH / Checkmk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T11:17:13.433)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T11:17:13.433 / 2026-11-11T11:17:13.547
- **官方描述（原文）**：Path traversal in the Synthetic Monitoring "Robotmk" test service of Checkmk <2.5.0p19, <2.4.0p40, and 2.3.0 (EOL) allows an attacker who controls the agent output of a monitored host's check output for a host to inject a crafted robot output to define the contents and location for the generated HTML log, leading to code execution as the site user.

### 37. CVE-2026-118965｜Checkmk GmbH / Checkmk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T11:17:13.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T11:17:13.080 / 2026-11-11T11:17:13.223
- **官方描述（原文）**：Path traversal in the discovered host label synchronization in Checkmk <2.5.0p19, <2.4.0p40 and 2.3.0 (EOL) allows an attacker in control of a remote site in a distributed monitoring setup to write arbitrary files on the central site and thereby execute code as the central site user.

### 38. CVE-2026-112174｜Enter / Iperius Backup
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T10:16:42.960)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T10:16:42.960 / 2026-11-11T10:16:42.960
- **官方描述（原文）**：Local privilege escalation vulnerability in Iperius Backup 8.8.3, due to insufficient separation between the graphical user interface running with elevated privileges and local users with low privileges. When the backup service is configured to run persistently with Administrator privileges, a local attacker with low privileges can use the native Windows dialogues exposed by the application to run programmes that inherit its elevated context. This allows commands to be executed with SYSTEM or Administrator privileges, depending on the application’s context, and compromises the affected Windows system.

### 39. CVE-2026-110697｜Red Hat / Red Hat OpenShift Update Service
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T17:17:14.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T17:17:14.897 / 2026-11-11T17:17:15.587
- **官方描述（原文）**：A flaw was found in Quay where the robot account listing function constructs a SQL LIKE pattern from user-controlled namespace names without escaping wildcard metacharacters. An attacker who creates a namespace containing an underscore character can match and retrieve robot accounts and their decrypted authentication tokens from other tenants' namespaces, leading to cross-tenant credential theft and unauthorized image operations.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-85632 | WATCH / 28 | Sipay Electronic Money and Payment Services Inc. / WooCommerce Virtual POS Module | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-8333 | WATCH / 28 | Microchip / TimePictra | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-78287 | WATCH / 28 | Staggs / STAGGS | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76954 | WATCH / 28 | Synology / DiskStation Manager (DSM) | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-67449 | WATCH / 28 | Portabase / portabase | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-65840 | WATCH / 28 | getfider / fider | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126812 | WATCH / 28 | blueprintue / blueprintue-self-hosted-edition | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126806 | WATCH / 28 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126800 | WATCH / 28 | hydro-dev / @hydrooj/ui-default | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126797 | WATCH / 28 | tongcheng-security-team / NextScan | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126785 | WATCH / 28 | rmalright / TR-VISION HOME | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126777 | WATCH / 28 | Traccar / Traccar | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126768 | WATCH / 28 | OpsTree Solutions / REMS | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126537 | WATCH / 28 | SaturdayDrive / Ninja Forms - File Uploads | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126325 | WATCH / 28 | PTC / Windchill | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126263 | WATCH / 28 | Fortinet / FortiMail | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126262 | WATCH / 28 | Fortinet / FortiAnalyzer | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126259 | WATCH / 28 | Fortinet / FortiOS | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126257 | WATCH / 28 | Fortinet / FortiAuthenticator | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126254 | WATCH / 28 | Fortinet / FortiOS | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126253 | WATCH / 28 | Fortinet / FortiOS | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126251 | WATCH / 28 | Fortinet / FortiAuthenticator | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126229 | WATCH / 28 | Fortinet / FortiManager | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126170 | WATCH / 28 | Fortinet / FortiManager | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126164 | WATCH / 28 | Fortinet / FortiMail | v3.1 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126157 | WATCH / 28 | Fortinet / FortiMail | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126156 | WATCH / 28 | Fortinet / FortiMail | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126155 | WATCH / 28 | Fortinet / FortiMail | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126150 | WATCH / 28 | Fortinet / FortiMail | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-126148 | WATCH / 28 | Fortinet / FortiMail | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：30。
- EPSS 未確認：30；Exploitation status 未確認：30。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-12T07:52:01.651144+00:00`；Delta generated at：`2026-11-12T07:52:01.651144+00:00`。

---

## 可驗證資料來源

- **CVE-2026-85632** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85632)
- **CVE-2026-8333** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-8333)
- **CVE-2026-78287** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78287)
- **CVE-2026-76954** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76954)
- **CVE-2026-67449** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67449)
- **CVE-2026-65840** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65840)
- **CVE-2026-126812** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126812)
- **CVE-2026-126806** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126806)
- **CVE-2026-126800** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126800)
- **CVE-2026-126797** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126797)
- **CVE-2026-126785** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126785)
- **CVE-2026-126777** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126777)
- **CVE-2026-126768** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126768)
- **CVE-2026-126537** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126537)
- **CVE-2026-126325** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126325)
- **CVE-2026-126263** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126263)
- **CVE-2026-126262** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126262)
- **CVE-2026-126259** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126259)
- **CVE-2026-126257** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126257)
- **CVE-2026-126254** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126254)
- **CVE-2026-126253** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126253)
- **CVE-2026-126251** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126251)
- **CVE-2026-126229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126229)
- **CVE-2026-126170** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126170)
- **CVE-2026-126164** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126164)
- **CVE-2026-126157** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126157)
- **CVE-2026-126156** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126156)
- **CVE-2026-126155** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126155)
- **CVE-2026-126150** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126150)
- **CVE-2026-126148** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126148)
- **CVE-2026-126147** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126147)
- **CVE-2026-12591** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12591)
- **CVE-2026-12507** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12507)
- **CVE-2026-123710** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123710)
- **CVE-2026-121374** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121374)
- **CVE-2026-120495** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120495)
- **CVE-2026-118965** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118965)
- **CVE-2026-112174** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112174)
- **CVE-2026-110697** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110697)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
