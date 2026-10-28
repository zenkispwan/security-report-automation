# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**61** 筆符合目前門檻的重要變化；事件統計：EPSS_INCREASED=1、EXPLOITATION_CHANGED=1、NEW_CVE=59、NEW_KEV=2、RANSOMWARE_USE_CHANGED=1。
- Intelligence 候選：**30** 筆；P1 **2**、P2 **0**、P3 **0**、WATCH **28**。
- Baseline：state / generated_at=2026-10-27T05:49:02.764065+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-48356、CVE-2026-111497。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **61** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-48356｜Adobe / Commerce and Magento
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.30582 / percentile=0.98231
- **CISA KEV**：listed=true / date_added=2026-10-27 / due_date=2026-11-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-07-14T20:17:08.437 / 2026-10-28T04:18:02.533
- **官方描述（原文）**：Adobe Commerce and Magento contain an unrestricted upload of file with dangerous type vulnerability that could result in arbitrary code execution in the context of the current user, potentially gaining elevated access or control over the victim's account or session.

### 2. CVE-2026-111497｜Google / Brotli
- **Delta event**：NEW_KEV (from=false; to=true)；EPSS_INCREASED (from=0.36027; to=0.55483)；EXPLOITATION_CHANGED (from=none; to=known_exploited)；RANSOMWARE_USE_CHANGED (from=未確認; to=Unknown)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)、DELTA_EPSS_JUMP(+15)、DELTA_EXPLOIT_ESCALATION(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.55483 / percentile=0.9903
- **CISA KEV**：listed=true / date_added=2026-10-27 / due_date=2026-11-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-22T14:17:37.190 / 2026-10-28T04:17:56.950
- **官方描述（原文）**：Google Brotli contains an unchecked return value vulnerability that allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.

### 3. CVE-2026-93866｜WatchGuard / Fireware OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T16:17:33.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T16:17:33.013 / 2026-10-27T16:17:33.013
- **官方描述（原文）**：An integer overflow vulnerability in the WebSocket connection handling used by WatchGuard Fireware OS's Access Portal allows a remote, unauthenticated attacker to write beyond the bounds of a heap buffer by sending a specially crafted request while the Access Portal feature is enabled.

### 4. CVE-2026-93865｜WatchGuard / Fireware OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T16:17:32.843)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T16:17:32.843 / 2026-10-27T16:17:32.843
- **官方描述（原文）**：A missing authentication vulnerability in the Fireware OS FireCluster synchronization daemon allows a remote, unauthenticated attacker to invoke privileged system-level administrative actions by sending a specially crafted request to the FireCluster management IP when the clustering feature is enabled.

### 5. CVE-2026-93857｜WatchGuard / Fireware OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T16:17:32.463)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T16:17:32.463 / 2026-10-27T16:17:32.463
- **官方描述（原文）**：A stack-based buffer overflow vulnerability in Fireware OS's SIP proxy allows a remote, unauthenticated attacker to execute arbitrary code by sending a specially crafted request through a policy that uses the SIP proxy.

### 6. CVE-2026-92885｜Qode Themes / Qode Membership
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T09:16:34.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00368 / percentile=0.30461
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T09:16:34.630 / 2026-10-27T14:52:13.410
- **官方描述（原文）**：The Qode Membership plugin for WordPress is vulnerable to Authentication Bypass leading to Account Takeover in all versions up to, and including, 2.0.6.2 via the qode_membership_check_facebook_user AJAX action. This is due to a typographic error in the Facebook OAuth token verification guard within the qode_membership_login_user_from_social_network function — the guard condition tests an undefined variable ($check_social_useqoder instead of $check_social_user), causing empty() to always return true and rendering the Graph API token verification branch dead code, leaving wp_set_auth_cookie() reachable with no credential or token validation whatsoever. This makes it possible for unauthenticated attackers to log in as any existing WordPress account — including Administrator-level accounts — by supplying a known or enumerated administrator login name (rather than an email address) in the response[email] parameter, which the fallback path in get_user_by('login', $email) resolves to the matching account. Exploitation does require harvesting a valid qode_validate_facebook_login nonce, but this nonce is rendered on any public front-end page containing the [qode_user_login] or [qode_user_register] shortcode and is therefore obtainable without any prior authentication.

### 7. CVE-2026-90465｜WatchGuard / Fireware OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T16:17:31.640)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T16:17:31.640 / 2026-10-27T16:17:31.640
- **官方描述（原文）**：A missing authentication vulnerability in the FireCluster Sync processing allows an attacker positioned on the cluster interconnect, such as a compromised cluster peer or an on-path network attacker, to invoke privileged firewall management actions as root by sending a specially crafted request.

### 8. CVE-2026-86577｜Hitachi / JP1/Integrated Management 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:56.993)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00456 / percentile=0.39417
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:56.993 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Out-of-bounds Write Vulnerability in JP1 Products. This issue affects JP1/Integrated Management 3 - Manager: from 13-00 before 13-50-31; JP1/Automatic Job Management System 3 - Manager: from 13-00 before 13-50-31; JP1/Automatic Job Management System 3 - Agent: from 13-00 before 13-50-31; JP1/Automatic Job Management System 3 - Agent Minimal Edition: from 13-00 before 13-50-31; JP1/Base: from 11-00 before 12-50-54.

### 9. CVE-2026-86576｜Hitachi / JP1/Integrated Management 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:56.880)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00454 / percentile=0.39212
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:56.880 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Heap-based Buffer Overflow Vulnerability in JP1 Products. This issue affects JP1/Integrated Management 3 - Manager: from 13-00 before 13-50-31; JP1/Automatic Job Management System 3 - Manager: from 13-00 before 13-50-31; JP1/Automatic Job Management System 3 - Agent: from 13-00 before 13-50-31; JP1/Automatic Job Management System 3 - Agent Minimal Edition: from 13-00 before 13-50-31; JP1/Base: from 11-00 before 12-50-54.

### 10. CVE-2026-86575｜Hitachi / JP1/Integrated Management 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:56.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00454 / percentile=0.39212
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:56.760 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Stack-based Buffer Overflow Vulnerability in JP1 Products. This issue affects JP1/Integrated Management 3 - Manager: from 13-00 before 13-50-31; JP1/Automatic Job Management System 3 - Manager: from 13-00 before 13-50-31; JP1/Automatic Job Management System 3 - Agent: from 13-00 before 13-50-31; JP1/Automatic Job Management System 3 - Agent Minimal Edition: from 13-00 before 13-50-31; JP1/Base: from 11-00 before 12-50-54.

### 11. CVE-2026-86574｜Hitachi / JP1/Base
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:56.643)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00519 / percentile=0.43926
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:56.643 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Heap-based Buffer Overflow Vulnerability in JP1/Base. This issue affects JP1/Base: from 11-00 before 12-50-54.

### 12. CVE-2026-84999｜Pie Register / Pie Register Premium
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T03:17:16.157)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T03:17:16.157 / 2026-10-28T03:17:16.157
- **官方描述（原文）**：The Pie Register Premium plugin for WordPress is vulnerable to Unrestricted File Type Upload in all versions up to, and including, 3.8.4.0 via the piereg_file_upload function. This is due to the plugin performing file type validation via wp_check_filetype and wp_check_filetype_and_ext but never checking whether those validation calls produced errors before move_uploaded_file() is called, combined with no nonce or capability check on the AJAX handler. This makes it possible for unauthenticated attackers to upload files of dangerous types (e.g. PHP scripts) that may be executable, which makes remote code execution possible. The server returns the generated destination filename in the response, giving the attacker the exact path needed to trigger the uploaded file.

### 13. CVE-2026-82122｜Hitachi / HiRDB Server Version 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:56.380)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00454 / percentile=0.39212
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:56.380 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Stack-based Buffer Overflow Vulnerability in HiRDB. This issue affects HiRDB Server Version 10: from 10-00 before 10-12-01; HiRDB Server Version 9: from 09-00 through 09-66-22; HiRDB Server with Additional Function Version 9: from 09-00 through 09-66/V; HiRDB Server Version 9(32): from 09-02 through 09-66-22; HiRDB Server with Additional Function Version 9(32): from 09-00 through 09-66-/V.

### 14. CVE-2026-82120｜Hitachi / HiRDB Server Version 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:56.147)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:56.147 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Heap-based Buffer Overflow Vulnerability in HiRDB. This issue affects HiRDB Server Version 10: from 10-00 before 10-12-01; HiRDB Server Version 9: from 09-00 through 09-66-22; HiRDB Server with Additional Function Version 9: from 09-00 through 09-66/V; HiRDB Server Version 9(32): from 09-02 through 09-66-22; HiRDB Server with Additional Function Version 9(32): from 09-00 through 09-66-/V.

### 15. CVE-2026-82119｜Hitachi / HiRDB Server Version 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:56.033)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:56.033 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：OS Command Injection Vulnerability in HiRDB. This issue affects HiRDB Server Version 10: from 10-00 before 10-12-01; HiRDB Server Version 9: from 09-00 through 09-66-22; HiRDB Server with Additional Function Version 9: from 09-00 through 09-66/V; HiRDB Server Version 9(32): from 09-02 through 09-66-22; HiRDB Server with Additional Function Version 9(32): from 09-00 through 09-66-/V.

### 16. CVE-2026-82118｜Hitachi / HiRDB Server Version 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:55.917)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:55.917 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Stack-based Buffer Overflow Vulnerability in HiRDB. This issue affects HiRDB Server Version 10: from 10-00 before 10-12-01; HiRDB Server Version 9: from 09-00 through 09-66-22; HiRDB Server with Additional Function Version 9: from 09-00 through 09-66/V; HiRDB Server Version 9(32): from 09-02 through 09-66-22; HiRDB Server with Additional Function Version 9(32): from 09-00 through 09-66-/V.

### 17. CVE-2026-82117｜Hitachi / HiRDB Server Version 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:55.797)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:55.797 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Authentication Bypass by Spoofing Vulnerability in HiRDB. This issue affects HiRDB Server Version 10: from 10-00 before 10-12-01; HiRDB Server Version 9: from 09-00 through 09-66-22; HiRDB Server with Additional Function Version 9: from 09-00 through 09-66/V; HiRDB Server Version 9(32): from 09-02 through 09-66-22; HiRDB Server with Additional Function Version 9(32): from 09-00 through 09-66-/V.

### 18. CVE-2026-82116｜Hitachi / HiRDB Server Version 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:55.680)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:55.680 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Missing Authentication for Critical Function Vulnerability in HiRDB. This issue affects HiRDB Server Version 10: from 10-00 before 10-12-01; HiRDB Server Version 9: from 09-00 through 09-66-22; HiRDB Server with Additional Function Version 9: from 09-00 through 09-66/V; HiRDB Server Version 9(32): from 09-02 through 09-66-22; HiRDB Server with Additional Function Version 9(32): from 09-00 through 09-66-/V.

### 19. CVE-2026-76939｜Hitachi / JP1/Automatic Job Management System 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:55.563)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00519 / percentile=0.43925
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:55.563 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Heap-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3. This issue affects JP1/Automatic Job Management System 3 - Manager: from 11-00 before 13-50-31; JP1/Automatic Job Management System 3 - Agent: from 11-00 before 13-50-31.

### 20. CVE-2026-76938｜Hitachi / JP1/Automatic Job Management System 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:55.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00643 / percentile=0.50612
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:55.450 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Authentication Bypass Vulnerability in JP1/Automatic Job Management System 3. This issue affects JP1/Automatic Job Management System 3 - Manager: from 10-00 before 13-50-31.

### 21. CVE-2026-76937｜Hitachi / JP1/Automatic Job Management System 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:55.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00454 / percentile=0.39213
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:55.337 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Heap-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3. This issue affects JP1/Automatic Job Management System 3 - Manager: from 10-00 before 13-50-31.

### 22. CVE-2026-76936｜Hitachi / JP1/Automatic Job Management System 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:55.223)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00454 / percentile=0.39213
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:55.223 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Stack-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3. This issue affects JP1/Automatic Job Management System 3 - Manager: from 10-00 before 13-50-31.

### 23. CVE-2026-76935｜Hitachi / JP1/Automatic Job Management System 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:55.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00454 / percentile=0.39213
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:55.110 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Stack-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3. This issue affects JP1/Automatic Job Management System 3 - Manager: from 10-00 before 13-50-31.

### 24. CVE-2026-76934｜Hitachi / JP1/Automatic Job Management System 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:54.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00519 / percentile=0.43926
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:54.990 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Stack-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3. This issue affects JP1/Automatic Job Management System 3 - Manager: from 11-00 before 13-50-31; JP1/Automatic Job Management System 3 - Agent: from 11-00 before 13-50-31.

### 25. CVE-2026-76933｜Hitachi / JP1/Automatic Job Management System 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:54.870)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00454 / percentile=0.39213
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:54.870 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Heap-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3. This issue affects JP1/Automatic Job Management System 3 - Manager: from 11-00 before 13-50-31; JP1/Automatic Job Management System 3 - Agent: from 11-00 before 13-50-31.

### 26. CVE-2026-76932｜Hitachi / JP1/Automatic Job Management System 3 - Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:54.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00454 / percentile=0.39212
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:54.730 / 2026-10-27T15:00:49.240
- **官方描述（原文）**：Stack-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3. This issue affects JP1/Automatic Job Management System 3 - Manager: from 11-00 before 13-50-31; JP1/Automatic Job Management System 3 - Agent: from 11-00 before 13-50-31.

### 27. CVE-2026-65145｜NVIDIA / NeMo Agent Toolkit
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T13:16:59.860)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T13:16:59.860 / 2026-10-27T15:03:41.023
- **官方描述（原文）**：NVIDIA NeMo Agent Toolkit contains a vulnerability where a attacker could cause a missing authentication issue. This vulnerability might lead to code execution, escalation of privileges, data tampering, denial of service, and information disclosure.

### 28. CVE-2026-58256｜JeromeDevome / GRR
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T23:17:06.140)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T23:17:06.140 / 2026-10-27T23:17:06.140
- **官方描述（原文）**：GRR is a resource management and reservation application. Prior to the advisory-reported fixed version 4.5.0, an administrator can inject malicious PHP through LDAP connector configuration parameters such as `ldap_filter`, poisoning `/personnalisation/config_ldap.inc.php` and permitting remote code execution. The administrator must first successfully connect to an LDAP server, which can be attacker-controlled, and then submit malicious input on the subsequent connector settings page. The advisory reports this issue as fixed in version 4.5.0.

### 29. CVE-2026-48360｜Adobe / Adobe Connect Desktop App
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:17:00.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:17:00.740 / 2026-10-27T17:17:00.740
- **官方描述（原文）**：Adobe Connect is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue requires user interaction in that a victim must visit a maliciously crafted URL or interact with a compromised web page. Scope is changed.

### 30. CVE-2026-18450｜SMCI / X12SPI
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T08:16:53.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.004 / percentile=0.34114
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T08:16:53.710 / 2026-10-27T15:54:05.340
- **官方描述（原文）**：The BMC does not correctly enforce integrity and encryption requirements for IPMI commands. An attacker may be able to craft packets that execute arbitrary commands on an active session.

### 31. CVE-2026-118375｜ggml-org / llama.cpp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T03:17:14.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T03:17:14.077 / 2026-10-28T03:17:14.077
- **官方描述（原文）**：llama.cpp b8841 before b11865 contains an out-of-bounds write vulnerability in the ggml-rpc RDMA transport rdma_recv() function that allows unauthenticated peers to overflow the rpc-server stack. Attackers advertising RDMA capabilities in the HELLO message can send up to 256 KiB into a 1-byte stack variable in rpc_serve_client(), crashing the server or potentially executing code.

### 32. CVE-2026-117603｜spesmilo / electrum
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T14:16:40.233)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T14:16:40.233 / 2026-10-27T16:03:45.247
- **官方描述（原文）**：Electrum before 4.7.2 contains a spending limit bypass vulnerability in the Nostr Wallet Connect plugin that allows malicious NWC clients to exceed daily_limit_sat by exploiting non-atomic budget checks and millisatoshi truncation. Attackers can send concurrent pay_invoice requests that pass budget_allows_spend() before add_to_budget() runs, or repeatedly pay msat amounts that are floored to whole satoshis, to drain funds beyond the limit.

### 33. CVE-2026-117601｜spesmilo / electrum
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T14:16:39.947)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T14:16:39.947 / 2026-10-27T16:03:45.247
- **官方描述（原文）**：Electrum before 4.8.3 fails to verify signatures of wallet-owned inputs in unconfirmed mempool transactions, allowing malicious servers to replace a just-broadcast transaction with a conflicting one. Attackers can swallow the user's transaction and display an invalid zero-fee copy paying an attacker address, tricking users into RBF fee-bumping and signing it.

### 34. CVE-2026-117564｜buqiyuan / nest-admin
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T14:16:38.720)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T14:16:38.720 / 2026-10-27T16:04:22.707
- **官方描述（原文）**：nest-admin before 1.0.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge administrator tokens by using a hardcoded JWT_SECRET committed in .env.production. Attackers can sign tokens with the known secret that JwtStrategy and RbacGuard trust, impersonating any user ID or claiming the admin role for full administrative access.

### 35. CVE-2026-117532｜redaxo / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T11:17:33.597)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T11:17:33.597 / 2026-10-27T15:02:47.683
- **官方描述（原文）**：REDAXO core from 5.3.0 before 5.21.4 contains an authentication bypass vulnerability in the structure/history plugin that allows unauthenticated attackers to forge temporary login tokens. Attackers can force the session-tied secret into a predictable state and forge tokens for accounts like admin, gaining backend access and code execution outside live mode.

### 36. CVE-2026-116863｜Tribulant Software / Newsletters
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T16:17:30.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T16:17:30.543 / 2026-10-27T16:17:30.543
- **官方描述（原文）**：Cross-Site Request Forgery (CSRF) vulnerability in Tribulant Software Newsletters newsletters-lite allows Cross Site Request Forgery.This issue affects Newsletters: from n/a through 4.18.2.

### 37. CVE-2026-116692｜mlflow / mlflow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T21:18:05.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T21:18:05.013 / 2026-10-27T21:18:05.013
- **官方描述（原文）**：MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. From 3.12.0rc0 until 3.17.0, third-party scorer deserialization in mlflow/genai/scorers/base.py accepts request-selected descendants of THIRD_PARTY_SCORER_ALLOWED_MODULES rather than requiring an exact allowed module. A caller can use MLflow artifact endpoints to place a Python module beneath a writable allowed package and submit its module and class through /ajax-api/3.0/mlflow/scorer/invoke. Scorer.model_validate_json() imports the module and constructs the class before trace processing. Authentication-disabled deployments permit this code execution without credentials, while basic-auth deployments require a principal capable of creating an experiment and run and uploading artifacts. In either configuration, the allowed scorer package must be writable by the server process. This issue is fixed in version 3.17.0.

### 38. CVE-2026-115216｜Eclipse Foundation / Eclipse ioFog
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T12:17:07.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T12:17:07.090 / 2026-10-27T16:04:22.707
- **官方描述（原文）**：In Eclipse ioFog Operator versions 3.8.0 before 3.9.2, TLS certificate verification is disabled when the operator contacts the Controller API and when it logs in to an external OIDC issuer. An on-path attacker can present any certificate, capture the OAuth client secret (external mode) or the Controller bootstrap admin password (embedded mode with Controller HTTPS enabled), and supply the access token the operator stores for later Controller API calls. v3.8 removed Keycloak. The exposed credential is not a Keycloak realm-admin secret.

### 39. CVE-2026-114595｜The EPICS Community / EPICS Base
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:58.530)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:58.530 / 2026-10-27T17:16:58.530
- **官方描述（原文）**：In EPICS Base release 7.0.10 and prior, an integer overflow in network request processing can cause memory to be allocated with an incorrect size. Subsequent handling of attacker supplied data may result in memory corruption, denial of service, or potential remote code execution.

### 40. CVE-2026-112710｜WatchGuard / Fireware OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T16:17:30.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T16:17:30.120 / 2026-10-27T16:17:30.120
- **官方描述（原文）**：A heap-based buffer overflow vulnerability exists in the Fireware OS authentication service allows an attacker who controls or intercepts traffic to the configured Active Directory server to create a denial of service condition and potentially execute arbitrary code by returning a specially crafted response.

### 41. CVE-2026-112709｜WatchGuard / Fireware OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T16:17:29.997)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T16:17:29.997 / 2026-10-27T16:17:29.997
- **官方描述（原文）**：A heap-based buffer overflow vulnerability in the Fireware OS authentication service allows an attacker who controls or intercepts traffic to the configured Active Directory server to create a denial of service condition and potentially execute arbitrary code by returning a specially crafted response.

### 42. CVE-2026-112362｜@fastify/express / @fastify/express
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T12:17:04.970)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T12:17:04.970 / 2026-10-27T15:03:41.023
- **官方描述（原文）**：@fastify/express is a Fastify plugin that runs Express middleware inside Fastify. In versions 4.0.5 through 4.0.8, when Fastify runs with the non-default ignoreDuplicateSlashes option enabled, the plugin matches path-scoped Express middleware against a URL whose duplicate-slash normalization has also collapsed the separator after an absolute-form request target's scheme, so Fastify's router resolves the request to the scoped path and runs the handler while the Express layer no longer sees that path. As a result, a request using an absolute-form target can reach a handler on a scoped route such as an admin path while the middleware for authentication, authorization, or rate limiting is skipped. An unauthenticated attacker needs only the non-default ignoreDuplicateSlashes option to be enabled. The issue is fixed in @fastify/express 4.0.9, and users should upgrade to 4.0.9 or later. As a workaround, enforce authentication in a Fastify hook such as preHandler that runs after the router resolves the request, or leave ignoreDuplicateSlashes at its default.

### 43. CVE-2026-112352｜Sunhillo Corporation / SureLine
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T20:17:12.997)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T20:17:12.997 / 2026-10-27T20:17:12.997
- **官方描述（原文）**：Sunhillo SureLine before 9.1.5 contains an authentication bypass vulnerability that allows an unauthenticated remote attacker to impersonate any user with an active web session by forging a session cookie containing only a cleartext username with no random identifier or integrity protection. Attackers can guess default account names such as Admin or sftp_user and submit a forged username cookie to satisfy the login check in checkLogin (libwebcmn.so) and networkDiag.cgi, chaining into root command execution.

### 44. CVE-2026-110879｜FasterXML / jackson-databind
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T01:16:55.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T01:16:55.180 / 2026-10-28T01:16:55.180
- **官方描述（原文）**：jackson-databind validates the outer class of a class-name type ID but accepts attacker-selected classes inside its generic arguments, even when those classes violate the declared type or would be rejected as direct type IDs. This bypasses the generic-argument validation added for CVE-2026-54512 (GHSA-j3rv-43j4-c7qm), of which this is an incomplete fix. DatabindContext._resolveAndValidateGeneric() checks the outer class against the declared base type and then passes each argument from the type ID to _validateTypeParameter(), which validates the argument against the outer base type rather than enforcing its corresponding declared generic binding. It also invokes validators with arguments that have not passed the subtype check those validators expect. Under the default DefaultBaseTypeLimitingValidator this accepts an unrelated class inside a generic subtype even when the same class is rejected as a direct type ID. Where an allowIfBaseType(...) rule approves the outer type, Jackson substitutes LaissezFaireSubTypeValidator, so the configured validator no longer restricts the embedded arguments. The element type of a plain array type ID such as [Lpkg.Gadget; is likewise left unvalidated once the array's base type is approved. Affected paths include annotation-based class-name polymorphism with a default Jackson 3.x JsonMapper, configured default typing in both Jackson 2.x and 3.x, and integrations that expose that default typing. The default-validator case requires no application-authored validator: with @JsonTypeInfo(use = Id.CLASS), a direct gadget type ID is rejected as "Not a subtype", while a type ID naming a generic wrapper around the same gadget is accepted and deserialized, including attacker-supplied bean properties. Where class-name default typing permits Map, a property declared as Map<String,String> accepts HashMap<FileSystemXmlApplicationContext,String>; map-key discovery then passes the attacker-controlled JSON property name to the selected class's one-string constructor. With Spring on the classpath and attacker-controlled XML the application can load, that constructor loads the XML and invokes ProcessBuilder.start() under the application account, giving arbitrary command execution. This issue affects com.fasterxml.jackson.core:jackson-databind from 2.10.0 and tools.jackson.core:jackson-databind from 3.0.0. Releases before 2.10.0 are not affected, because PolymorphicTypeValidator was introduced in jackson-databind 2.10.0.

### 45. CVE-2026-108142｜Veeam / Backup and Replication
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:57.553)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:57.553 / 2026-10-27T17:16:57.553
- **官方描述（原文）**：A vulnerability allowing an unauthenticated attacker to bypass authorization on the CDP Coordinator Service.

### 46. CVE-2026-108015｜HCLSoftware / Notes Client
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:57.187)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:57.187 / 2026-10-27T21:18:00.127
- **官方描述（原文）**：Private keys for eight eMudhra intermediate CA certificates have been compromised https://emudhra.we-have-a-problem.com/ , which impacts certificate trust for outbound network request features of HCL Notes Client. An unauthenticated network attacker could spoof server certificates to execute a man in the middle (MITM) attack, enabling them to intercept and/or modify the content of outbound TLS connections.

### 47. CVE-2026-108014｜HCLSoftware / Domino Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:57.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:57.040 / 2026-10-27T21:17:59.450
- **官方描述（原文）**：Private keys for eight eMudhra intermediate CA certificates have been compromised https://emudhra.we-have-a-problem.com/ , which impacts certificate trust for outbound network request features of HCL Domino Server. An unauthenticated network attacker could spoof server certificates to execute a man in the middle (MITM) attack, enabling them to intercept and/or modify the content of outbound TLS connections.

### 48. CVE-2026-106076｜Veeam / Backup for Microsoft 365
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:56.553)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:56.553 / 2026-10-27T17:16:56.553
- **官方描述（原文）**：A vulnerability allowing an authenticated organization-transfer peer to inject SQL into the configuration database of the source Veeam Backup for Microsoft 365 server, leading to cross-tenant read and write of configuration data and remote code execution as the PostgreSQL service account.

### 49. CVE-2026-106013｜artbees / Jupiter X Core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T02:17:01.303)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T02:17:01.303 / 2026-10-28T02:17:01.303
- **官方描述（原文）**：The Jupiter X Core plugin for WordPress is vulnerable to Authentication Bypass via the Twitter/X Social Login handler in all versions up to and including 4.61.0. The vulnerability exists within the verify_twitter_callback function because after exchanging the visitor's oauth_verifier for their access token, the handler never calls setOauthToken() to reassign the returned credentials to the TwitterOAuth client, causing the subsequent account/verify_credentials API call to remain signed with the site operator's stored Access Token and Access Token Secret rather than the authenticating visitor's token. This causes the X API to return the profile of the X application owner instead of the signing-in visitor, and the plugin then resolves and authenticates a WordPress account solely by matching that owner's email address via wp_set_auth_cookie(), allowing unauthenticated attackers to gain authenticated access as the WordPress user whose email corresponds to the X app owner, who is typically the site administrator.

### 50. CVE-2026-105781｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:56.430)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:56.430 / 2026-10-27T17:16:56.430
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary SQL commands, potentially gaining elevated access or control over the victim's account or session. Exploitation of this issue does not require user interaction. Scope is changed.

### 51. CVE-2026-105780｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:56.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:56.313 / 2026-10-27T17:16:56.313
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 52. CVE-2026-105779｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:56.193)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:56.193 / 2026-10-27T17:16:56.193
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in a Security feature bypass. A low-privileged attacker could leverage this vulnerability to bypass security measures and gain unauthorized read and limited write access. Exploitation of this issue does not require user interaction. Scope is changed.

### 53. CVE-2026-105489｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:56.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:56.080 / 2026-10-27T17:16:56.080
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 54. CVE-2026-104383｜EagleCloud / Aquila
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T05:16:59.533)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T05:16:59.533 / 2026-10-28T05:16:59.533
- **官方描述（原文）**：Improper Control of Generation of Code in Pigeon MFA service in EagleCloud Aquila versions through 2.6.7.2 on on-premises platforms allows authenticated remote attackers to execute arbitrary code via code injection

### 55. CVE-2026-104354｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:55.837)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:55.837 / 2026-10-27T17:16:55.837
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution in the context of the current user. An attacker with high privileges could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 56. CVE-2026-104353｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:55.717)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:55.717 / 2026-10-27T17:16:55.717
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 57. CVE-2026-104351｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:55.593)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:55.593 / 2026-10-27T17:16:55.593
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 58. CVE-2026-104350｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T17:16:55.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T17:16:55.457 / 2026-10-27T17:16:55.457
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by a reflected Cross-Site Scripting (XSS) vulnerability. An attacker could exploit this vulnerability to inject malicious scripts into a web page, potentially gaining elevated access or control over the victim's account or session. Exploitation of this issue requires user interaction in that a victim must visit a maliciously crafted URL or interact with a compromised web page. Scope is changed.

### 59. CVE-2026-103594｜WatchGuard / Fireware OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T16:17:28.517)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T16:17:28.517 / 2026-10-27T16:17:28.517
- **官方描述（原文）**：A stack-based buffer overflow vulnerability in Fireware OS's WireGuard configuration processing allows a remote attacker that has man-in-the-middle TLS-decrypted access between the Firebox and WatchGuard Cloud to create a Denial of Service condition and potentially execute arbitrary code by tampering with a FireCloud Gateway configuration payload.

### 60. CVE-2026-102789｜balbooa.com / Gridbox extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:53.907)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00315 / percentile=0.24273
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:53.907 / 2026-10-27T15:08:50.630
- **官方描述（原文）**：Joomla Extension - balbooa.com - Missing Authorization Check on Editor Controller Task in Gridbox < 2.20.4.2 - EditorController::getBlogPosts() reads the order parameter and invokes getBlogPosts() . Unlike other tasks in this controller, it omits the GridboxHelper::checkUserEditLevel() check.

### 61. CVE-2026-102788｜balbooa.com / Gridbox extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-27T10:16:53.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00386 / percentile=0.32452
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-27T10:16:53.780 / 2026-10-27T15:08:50.630
- **官方描述（原文）**：Joomla Extension - balbooa.com - Unauthenticated SQL injection in Gridbox < 2.20.4.2 - On store product list pages, the value of the sort-by URL parameter is retrieved using a string filter and passed directly to GridboxHelper::getBlogPosts(). When the parameter does not match known sorting keys, it is prefixed with a table alias and inserted into the ORDER BY clause without checking against an allowlist


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-48356｜Adobe / Commerce and Magento
- **Title**：Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.30582 / percentile=0.98231
- **CISA KEV**：listed=true / date_added=2026-10-27 / due_date=2026-11-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Adobe Commerce and Magento contain an unrestricted upload of file with dangerous type vulnerability that could result in arbitrary code execution in the context of the current user, potentially gaining elevated access or control over the victim's account or session.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-111497｜Google / Brotli
- **Title**：Google Brotli Unchecked Return Value Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)、DELTA_EPSS_JUMP(+15)、DELTA_EXPLOIT_ESCALATION(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.55483 / percentile=0.9903
- **CISA KEV**：listed=true / date_added=2026-10-27 / due_date=2026-11-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Brotli contains an unchecked return value vulnerability that allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-93866 | WATCH / 28 | WatchGuard / Fireware OS | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93865 | WATCH / 28 | WatchGuard / Fireware OS | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93857 | WATCH / 28 | WatchGuard / Fireware OS | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92885 | WATCH / 28 | Qode Themes / Qode Membership | v3.1 9.8 (CRITICAL) | 0.00368 / percentile=0.30461 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-90465 | WATCH / 28 | WatchGuard / Fireware OS | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-86577 | WATCH / 28 | Hitachi / JP1/Integrated Management 3 - Manager | v3.1 9.4 (CRITICAL) | 0.00456 / percentile=0.39417 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-86576 | WATCH / 28 | Hitachi / JP1/Integrated Management 3 - Manager | v3.1 9.4 (CRITICAL) | 0.00454 / percentile=0.39212 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-86575 | WATCH / 28 | Hitachi / JP1/Integrated Management 3 - Manager | v3.1 9.4 (CRITICAL) | 0.00454 / percentile=0.39212 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-86574 | WATCH / 28 | Hitachi / JP1/Base | v3.1 9.8 (CRITICAL) | 0.00519 / percentile=0.43926 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-84999 | WATCH / 28 | Pie Register / Pie Register Premium | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-82122 | WATCH / 28 | Hitachi / HiRDB Server Version 10 | v3.1 9.4 (CRITICAL) | 0.00454 / percentile=0.39212 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-82120 | WATCH / 28 | Hitachi / HiRDB Server Version 10 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-82119 | WATCH / 28 | Hitachi / HiRDB Server Version 10 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-82118 | WATCH / 28 | Hitachi / HiRDB Server Version 10 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-82117 | WATCH / 28 | Hitachi / HiRDB Server Version 10 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-82116 | WATCH / 28 | Hitachi / HiRDB Server Version 10 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76939 | WATCH / 28 | Hitachi / JP1/Automatic Job Management System 3 - Manager | v3.1 9.8 (CRITICAL) | 0.00519 / percentile=0.43925 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76938 | WATCH / 28 | Hitachi / JP1/Automatic Job Management System 3 - Manager | v3.1 9.8 (CRITICAL) | 0.00643 / percentile=0.50612 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76937 | WATCH / 28 | Hitachi / JP1/Automatic Job Management System 3 - Manager | v3.1 9.4 (CRITICAL) | 0.00454 / percentile=0.39213 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76936 | WATCH / 28 | Hitachi / JP1/Automatic Job Management System 3 - Manager | v3.1 9.4 (CRITICAL) | 0.00454 / percentile=0.39213 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76935 | WATCH / 28 | Hitachi / JP1/Automatic Job Management System 3 - Manager | v3.1 9.4 (CRITICAL) | 0.00454 / percentile=0.39213 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76934 | WATCH / 28 | Hitachi / JP1/Automatic Job Management System 3 - Manager | v3.1 9.8 (CRITICAL) | 0.00519 / percentile=0.43926 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76933 | WATCH / 28 | Hitachi / JP1/Automatic Job Management System 3 - Manager | v3.1 9.4 (CRITICAL) | 0.00454 / percentile=0.39213 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76932 | WATCH / 28 | Hitachi / JP1/Automatic Job Management System 3 - Manager | v3.1 9.4 (CRITICAL) | 0.00454 / percentile=0.39212 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-65145 | WATCH / 28 | NVIDIA / NeMo Agent Toolkit | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-58256 | WATCH / 28 | JeromeDevome / GRR | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-48360 | WATCH / 28 | Adobe / Adobe Connect Desktop App | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-18450 | WATCH / 28 | SMCI / X12SPI | v3.1 9.8 (CRITICAL) | 0.004 / percentile=0.34114 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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
- EPSS 未確認：13；Exploitation status 未確認：27。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-28T06:27:38.037172+00:00`；Delta generated at：`2026-10-28T06:27:38.037172+00:00`。

---

## 可驗證資料來源

- **CVE-2026-48356** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48356) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48356) · [Vendor / Advisory (adobe.com)](https://www.adobe.com/trust/security/products/commerce/apsb26-73.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-111497** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111497) · [Vendor / Advisory (github.com)](https://github.com/google/brotli/releases/tag/v1.2.1) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-93866** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93866)
- **CVE-2026-93865** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93865)
- **CVE-2026-93857** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93857)
- **CVE-2026-92885** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92885) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-92885)
- **CVE-2026-90465** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90465)
- **CVE-2026-86577** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86577) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86577)
- **CVE-2026-86576** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86576) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86576)
- **CVE-2026-86575** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86575) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86575)
- **CVE-2026-86574** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86574) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86574)
- **CVE-2026-84999** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84999)
- **CVE-2026-82122** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82122) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-82122)
- **CVE-2026-82120** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82120)
- **CVE-2026-82119** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82119)
- **CVE-2026-82118** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82118)
- **CVE-2026-82117** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82117)
- **CVE-2026-82116** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82116)
- **CVE-2026-76939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76939) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76939)
- **CVE-2026-76938** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76938) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76938)
- **CVE-2026-76937** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76937) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76937)
- **CVE-2026-76936** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76936) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76936)
- **CVE-2026-76935** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76935) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76935)
- **CVE-2026-76934** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76934) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76934)
- **CVE-2026-76933** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76933) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76933)
- **CVE-2026-76932** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76932) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76932)
- **CVE-2026-65145** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65145)
- **CVE-2026-58256** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58256)
- **CVE-2026-48360** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48360)
- **CVE-2026-18450** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18450) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-18450)
- **CVE-2026-118375** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118375)
- **CVE-2026-117603** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-117603)
- **CVE-2026-117601** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-117601)
- **CVE-2026-117564** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-117564)
- **CVE-2026-117532** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-117532)
- **CVE-2026-116863** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116863)
- **CVE-2026-116692** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116692)
- **CVE-2026-115216** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115216)
- **CVE-2026-114595** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114595)
- **CVE-2026-112710** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112710)
- **CVE-2026-112709** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112709)
- **CVE-2026-112362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112362)
- **CVE-2026-112352** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112352)
- **CVE-2026-110879** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110879)
- **CVE-2026-108142** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108142)
- **CVE-2026-108015** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108015)
- **CVE-2026-108014** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108014)
- **CVE-2026-106076** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-106076)
- **CVE-2026-106013** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-106013)
- **CVE-2026-105781** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105781)
- **CVE-2026-105780** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105780)
- **CVE-2026-105779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105779)
- **CVE-2026-105489** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105489)
- **CVE-2026-104383** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104383)
- **CVE-2026-104354** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104354)
- **CVE-2026-104353** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104353)
- **CVE-2026-104351** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104351)
- **CVE-2026-104350** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104350)
- **CVE-2026-103594** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103594)
- **CVE-2026-102789** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102789) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-102789)
- **CVE-2026-102788** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102788) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-102788)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
