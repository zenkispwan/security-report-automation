# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**39** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=1、NEW_CVE=38。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **0**、WATCH **30**。
- Baseline：state / generated_at=2026-11-16T07:28:39.700149+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **39** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-129879｜lintsinghua / DeepAudit
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:26.900)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:26.900 / 2026-11-16T20:19:02.293
- **官方描述（原文）**：DeepAudit 2.0.0-beta.1 through 3.8.0 contains a path traversal vulnerability that allows authenticated users to write arbitrary files by importing projects with crafted IDs. Attackers can set absolute or ../ project IDs via /api/v1/database/import, then upload ZIPs through /api/v1/scan/upload-zip following cloned symlinks to overwrite app/main.py for remote code execution.

### 2. CVE-2026-129875｜getrebuild / rebuild
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:26.233)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:26.233 / 2026-11-16T20:19:02.160
- **官方描述（原文）**：REBUILD 4.5.0 through 4.5.4 contains an information disclosure vulnerability that allows low-privileged authenticated users to recover the administrator password hash by filtering User.password through the MCP QueryRecords tool. Attackers can send LK2 prefix-match filters to the /gw/mcp/sse gateway and use the returned total count as an oracle to extract the SHA-256 hash one character at a time, then log in as administrator.

### 3. CVE-2026-129863｜GitBucket / GitBucket
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:24.083)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:24.083 / 2026-11-16T17:17:32.590
- **官方描述（原文）**：GitBucket through 4.48.0 contains an incorrect authorization vulnerability that allows authenticated users to edit and merge other users' pull requests because the PATCH pulls and PUT pulls merge REST API endpoints only check read access. Attackers can close, reopen, retitle, retarget, or merge pull requests into the base branch without write permission on public repositories or as private-repository guest collaborators.

### 4. CVE-2026-129855｜samugit83 / RedAmon
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:22.723)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:22.723 / 2026-11-16T17:17:32.327
- **官方描述（原文）**：RedAmon before 7.8.0 contains a missing authentication vulnerability in the kali-sandbox terminal server that allows unauthenticated attackers to obtain a root shell by connecting to its WebSocket listener on port 8016. Attackers who can reach the port from co-resident containers or the host loopback can send keystrokes to an interactive /bin/bash session, executing commands as root inside the kali-sandbox container.

### 5. CVE-2026-129854｜samugit83 / RedAmon
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:22.553)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:22.553 / 2026-11-16T19:17:44.057
- **官方描述（原文）**：RedAmon 4.0.0 before 7.8.0 contains a missing object-level authorization vulnerability that allows authenticated users to control other tenants' agent sessions by supplying arbitrary session ids. Attackers can call /api/agent/sessions, interact and kill routes to list, kill, or send commands into other users' meterpreter and shell sessions on their compromised targets.

### 6. CVE-2026-120698｜requarks / wiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T22:18:14.720)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T22:18:14.720 / 2026-11-16T22:18:14.720
- **官方描述（原文）**：Wiki.js is an open source wiki app built on Node.js. Prior to 2.5.315, an authenticated account with only manage:users can use users.update to change the password of any local account, including the Root administrator and other accounts with manage:system, by omitting the optional groups argument, which is automatically allowed and bypasses destination-group authorization without checking the target's current privileges. The attacker can use users.disableTFA to clear the same target's tfaIsActive state and TFA secret without a target-privilege check, then authenticate with the replacement password. Supplying groups: [] to users.update can remove every group relationship from a selected administrator and leave the installation without a legitimate account holding manage:system. Additional administrators with IDs greater than 2 can also be deactivated or deleted. This issue is fixed in version 2.5.315.

### 7. CVE-2026-93664｜Dassault Systèmes / Station Launcher App in 3DEXPERIENCE platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T13:17:23.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T13:17:23.313 / 2026-11-16T15:17:34.640
- **官方描述（原文）**：A Deserialization of Untrusted Data vulnerability affecting Station Launcher App in 3DEXPERIENCE platform from Release 3DEXPERIENCE R2023x through Release 3DEXPERIENCE R2026x could lead to an unauthenticated remote code execution.

### 8. CVE-2026-79614｜Zyxel / DX3301-T0 firmware
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T02:17:22.743)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T02:17:22.743 / 2026-11-17T02:17:22.743
- **官方描述（原文）**：An out-of-bounds write vulnerability in “libclinkc.so” in Zyxel DX3301-T0/EX3301-T0 firmware versions through 5.50(ABVY.8.3)C0 could allow an unauthenticated attacker to elevate privileges and potentially execute arbitrary commands by sending a crafted HTTP request. WAN access is disabled by default on these devices.

### 9. CVE-2026-77033｜Dassault Systèmes / Station Launcher App in 3DEXPERIENCE platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T13:17:23.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T13:17:23.003 / 2026-11-17T00:17:27.257
- **官方描述（原文）**：An OS Command Injection vulnerability affecting Station Launcher App in 3DEXPERIENCE platform from Release 3DEXPERIENCE R2023x through Release 3DEXPERIENCE R2026x could allow an attacker to execute arbitrary commands on the server.

### 10. CVE-2026-53998｜Arize-ai / phoenix
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T20:19:06.807)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T20:19:06.807 / 2026-11-16T20:19:06.807
- **官方描述（原文）**：Phoenix is an AI observability and evaluation platform. From 13.0.0 until 15.7.0, the applyChatTemplate GraphQL query passed attacker-controlled F-string templates to FStringTemplateFormatter._format, while DotDict.__getattr__ did not prevent traversal through Python private attributes. A crafted field could traverse object internals such as __class__, __init__, and __globals__ to read process environment variables and internal module state. The endpoint is unauthenticated on default installations, and any account can reach it when authentication is enabled. Exposure of PHOENIX_SECRET can allow administrative session-token forgery and decryption of credentials protected by keys derived from that secret. This issue is fixed in version 15.7.0.

### 11. CVE-2026-19732｜Dassault Systèmes / Station Launcher App in 3DEXPERIENCE platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T13:17:22.843)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T13:17:22.843 / 2026-11-17T00:17:26.930
- **官方描述（原文）**：An OS Command Injection vulnerability affecting Station Launcher App in 3DEXPERIENCE platform from Release 3DEXPERIENCE R2023x through Release 3DEXPERIENCE R2026x could allow an attacker to execute arbitrary commands on the server.

### 12. CVE-2026-130380｜adminneo-org / AdminNeo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T02:17:22.037)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T02:17:22.037 / 2026-11-17T02:17:22.163
- **官方描述（原文）**：AdminNeo before 5.9.1 contains an authentication bypass vulnerability in the sqlsrv-based MS SQL driver that allows unauthenticated attackers to log in by submitting an empty username. Attackers can supply any non-empty password, triggering Windows integrated authentication that grants a full session with the web server identity's SQL Server privileges.

### 13. CVE-2026-130371｜thorsten / phpMyFAQ
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T02:17:20.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T02:17:20.490 / 2026-11-17T02:17:20.617
- **官方描述（原文）**：phpMyFAQ before 4.1.12 and 4.2.0-alpha before 4.2.0-RC.2 contains an authentication bypass vulnerability because the web installer ignores the legacy config/database.php during 3.x upgrades. Unauthenticated attackers can reinstall the site against an attacker-controlled database and create their own administrator account to take over the application.

### 14. CVE-2026-130369｜thorsten / phpMyFAQ
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T02:17:20.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T02:17:20.130 / 2026-11-17T02:17:20.257
- **官方描述（原文）**：phpMyFAQ 4.1.9 before 4.1.12 and 4.2.0-alpha before 4.2.0-RC.2 contains an authorization bypass vulnerability in multisite deployments that allows attackers to overwrite passkeys of accounts on other tenants via a shared PHP session store. Attackers can run WebAuthn prepare() for a login on one tenant, then replay the session against /api/webauthn/register on another tenant or the master to replace that user's passkeys and log in as admin.

### 15. CVE-2026-130366｜adminneo-org / AdminNeo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T02:17:19.593)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T02:17:19.593 / 2026-11-17T02:17:19.727
- **官方描述（原文）**：AdminNeo before 5.9.1 contains an authentication bypass vulnerability in the ClickHouse driver that allows remote attackers to log in to passwordless accounts without the configured defaultPasswordHash password. Attackers who know the name of a ClickHouse no_password account can submit any non-empty password, because connect() skips openPasswordless(), and obtain a session with that account's rights.

### 16. CVE-2026-130327｜Open Object Rexx / ooRexx
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T23:17:15.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T23:17:15.313 / 2026-11-16T23:17:15.313
- **官方描述（原文）**：In Open Object Rexx (ooRexx) before 5.2.0, RXAPI relies on a world-writable /tmp file unless XDG_RUNTIME_DIR is set, or localhost TCP port 10010, allowing RXAPI communication by any local user, e.g., for injection of a macro that will be executed by a REXX script.

### 17. CVE-2026-130320｜Open Object Rexx / ooRexx
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T23:17:15.177)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T23:17:15.177 / 2026-11-16T23:17:15.177
- **官方描述（原文）**：In Open Object Rexx (ooRexx) before 5.2.0, RXAPI mishandles nameArg and userid bounds checking, possibly leading to arbitrary code execution via crafted messages.

### 18. CVE-2026-130071｜TridotsTech / go1cms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T22:18:22.373)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T22:18:22.373 / 2026-11-16T22:18:22.373
- **官方描述（原文）**：TridotsTech go1cms master branch through commit 7f68d05 and version-3 branch before commit ead8da3 contains a missing authentication vulnerability in the guest-whitelisted update_doc method that allows unauthenticated attackers to modify any document. Attackers can supply a doctype, name and arbitrary fields that are saved with ignore_permissions=True, altering User records to escalate privileges, take over accounts or tamper with business data.

### 19. CVE-2026-130070｜muneeb141 / ghost
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T22:18:22.220)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T22:18:22.220 / 2026-11-16T22:18:22.220
- **官方描述（原文）**：Ghost by muneeb141 on the main branch from commit c731cdf through commit 672dfec contains an authentication bypass vulnerability in the whitelisted ghost.api.ghost.convert_to_real_user method that allows unauthenticated attackers to skip OTP verification by setting the client-supplied bypass_otp parameter. Attackers can obtain a ghost session from the guest-accessible create_ghost_session endpoint, then call convert_to_real_user with an arbitrary real_email and bypass_otp=1 to receive OAuth tokens for existing accounts and take them over.

### 20. CVE-2026-129955｜surmon-china / NodePress
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:31.030)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:31.030 / 2026-11-16T20:28:06.217
- **官方描述（原文）**：NodePress through 8.5.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to gain administrator access by using the hardcoded default password 'root'. Attackers can send base64-encoded 'root' to POST /admin/login when NP_ADMIN_DEFAULT_PASSWORD is unset to obtain admin tokens and fully control the site.

### 21. CVE-2026-129952｜surmon-china / NodePress
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:30.573)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:30.573 / 2026-11-16T20:28:06.217
- **官方描述（原文）**：NodePress through 8.5.1 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to gain administrator access by forging JWTs with the hardcoded 'nodepress-secret' fallback key. Attackers can sign HS256 bearer tokens with the default issuer, audience, and role 'admin' to access administrator-only APIs for article, comment, options, and file management.

### 22. CVE-2026-129941｜birkir / prime
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:28.800)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:28.800 / 2026-11-16T18:17:31.507
- **官方描述（原文）**：Prime CMS (@primecms/core) through 0.4.0-beta.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to register accounts via the createUser mutation on /prime/graphql. Because the isAuthenticated() guard has its check commented out and createAbility() hard-codes every role to admin, attackers can log in with full administrative control over content, users, webhooks and settings.

### 23. CVE-2026-129552｜tenseijs / @tensei/auth
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T12:17:53.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T12:17:53.337 / 2026-11-16T17:17:32.070
- **官方描述（原文）**：Tensei through 0.11.5 contains an authentication bypass vulnerability in @tensei/auth that falls back to the hard-coded JWT signing key 'auth-secret-key' when JWT_SECRET is unset. Unauthenticated attackers can sign tokens with arbitrary user ids accepted by populateContextFromToken to impersonate any user, including administrators.

### 24. CVE-2026-129550｜tenseijs / @tensei/auth
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T12:17:53.033)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T12:17:53.033 / 2026-11-16T16:17:52.537
- **官方描述（原文）**：Tensei through 0.11.5 contains a privilege escalation vulnerability in @tensei/auth that allows unauthenticated or authenticated users to assign themselves arbitrary roles via the exposed User Roles field. Attackers can supply a roles array during registration, a POST to the users route, or a PATCH to their own record to gain administrator permissions.

### 25. CVE-2026-120699｜TencentCloud / CubeSandbox
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T21:17:20.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T21:17:20.980 / 2026-11-16T22:18:14.877
- **官方描述（原文）**：CubeSandbox is an instant, concurrent, secure, and lightweight sandbox for AI agents. Prior to 0.5.1, any authenticated tenant permitted to call POST /sandboxes can supply metadata["host-mount"] with an arbitrary existing host path because the control plane performs no authorization check or allowed-prefix validation for the path. injectHostDirMounts forwards the path to prepareHostDirVolume, where Cubelet uses mount --rbind through the function to perform a recursive bind mount as root and exposes the host subtree to the tenant's MicroVM through virtio-fs, read-write by default. This allows host-root file access and modification, host code execution, access to the container runtime, and compromise of co-resident tenants without a kernel or virtual-machine-monitor flaw. This issue is fixed in version 0.5.1.

### 26. CVE-2026-120387｜Circutor / PowerStudio SCADA Wave
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T05:18:33.067)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T05:18:33.067 / 2026-11-17T05:18:33.067
- **官方描述（原文）**：An improper JWT signature verification vulnerability in CIRCUTOR PowerStudio SCADA WAVE desktop version allows an unauthenticated remote attacker to bypass authentication by submitting an unsigned JWT with the algorithm set to “none”. The shared JWT validation component accepts the token without verifying a cryptographic signature, allowing the attacker to impersonate another user and access protected functionality with that user's privileges.

### 27. CVE-2026-111559｜sruupl / Batflat
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T13:17:18.683)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T13:17:18.683 / 2026-11-16T16:17:48.797
- **官方描述（原文）**：Batflat CMS does not sanitize data passed to the /contact endpoint. A remote unauthenticated attacker can send a POST request with a crafted message, causing arbitrary PHP code execution with www-data user privileges. The project is no longer maintained and the issue has not been fixed.

### 28. CVE-2026-104840｜OpenCTI-Platform / opencti
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T21:17:17.393)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T21:17:17.393 / 2026-11-16T21:17:17.393
- **官方描述（原文）**：OpenCTI is an open source platform for managing cyber threat intelligence knowledge and observables. Prior to 7.260428.0, the token GraphQL mutation used for primary login has no endpoint-specific rate limit, while the global Express limiter defaults to permitting 10,000 requests in a one-second window. An unauthenticated remote attacker can make password guesses at network speed against a chosen user account and, if a credential is recovered, access the account's threat-intelligence data and permitted operations. This issue is fixed in version 7.260428.0.

### 29. CVE-2026-69221｜wpengine / faustjs
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T20:19:10.037)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T20:19:10.037 / 2026-11-16T22:18:25.387
- **官方描述（原文）**：Faust.js is a headless WordPress toolkit. Prior to 1.8.12, the FaustWP generateAuthorizationCode GraphQL mutation called wp_authenticate_username_password and wp_authenticate_email_password directly instead of using wp_authenticate. This bypassed callbacks registered on WordPress's outer authenticate filter, including policies for multifactor authentication, single sign-on, IP allowlists, or disabled accounts. On a site using FaustWP local login and one of those policies, an attacker with a valid username or email and password could obtain an authorization code and exchange it through /api/faust/auth/token for access and refresh tokens even when the normal WordPress login path would deny access. This issue is fixed in version 1.8.12.

### 30. CVE-2026-129950｜Rowy / Rowy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:30.243)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:30.243 / 2026-11-16T17:17:33.117
- **官方描述（原文）**：Rowy through 3.0.0 contains an incorrect permission assignment vulnerability in default Firebase Storage rules that grants any user holding a role read and write access to the entire bucket. Authenticated users restricted to a single table or read-only access can use the Firebase SDK directly to list, download, overwrite, and delete any stored files.

### 31. CVE-2026-129887｜thirdweb / thirdweb Dashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:28.123)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:28.123 / 2026-11-16T20:19:02.567
- **官方描述（原文）**：thirdweb Dashboard through commit 940b3745 contains an information disclosure vulnerability that allows authenticated users to read non-public team metadata by requesting the team join page with any invite ID. Attackers who know a team slug can obtain the serialized Team object, exposing billing email, billing status, Stripe customer ID, verified domain and support identifiers.

### 32. CVE-2026-129886｜thirdweb / thirdweb Dashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:27.973)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:27.973 / 2026-11-16T19:17:45.987
- **官方描述（原文）**：thirdweb Dashboard through commit 940b3745 contains a missing authorization vulnerability in revalidatePathAction and revalidateCacheTagAction server actions in revalidate.ts. Unauthenticated attackers can use action identifiers exposed in the client bundle to send POST requests that purge cached pages and data, forcing repeated regeneration and degrading performance.

### 33. CVE-2026-129883｜thirdweb / thirdweb Dashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:27.517)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:27.517 / 2026-11-16T20:19:02.430
- **官方描述（原文）**：thirdweb Dashboard through commit 940b3745 contains an open redirect vulnerability that allows remote attackers to send users to arbitrary sites by supplying an unvalidated redirectUri parameter on the /pay/[id] payment link page. Attackers can distribute payment links with a malicious redirectUri that PayPageWidget opens via window.open after payment without noopener, enabling phishing and reverse tabnabbing of the payment page.

### 34. CVE-2026-129871｜rocboss / paopao-ce
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:25.480)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:25.480 / 2026-11-16T17:17:32.863
- **官方描述（原文）**：Rocboss paopao-ce through 0.6.0-alpha.3 contains a payment bypass vulnerability that allows unauthenticated attackers to obtain paid attachments by reading storage URLs from the GET /v1/post endpoint. Attackers can download the paid file directly from the unauthenticated LocalOSS /oss static route, whose signed URL expired parameter is never checked.

### 35. CVE-2026-129867｜rocboss / paopao-ce
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:24.763)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:24.763 / 2026-11-16T17:17:32.733
- **官方描述（原文）**：Rocboss paopao-ce through 0.6.0-alpha.3 contains a stored cross-site scripting vulnerability that allows registered users to inject script by abusing #topic link wrapping in preparePost and parsePostTag. Attackers can publish posts or comments with a crafted topic containing a lone '<' and event handler to steal the PAOPAO_TOKEN JWT from localStorage and take over viewer accounts.

### 36. CVE-2026-129866｜DataLinkDC / Dinky
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:24.587)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:24.587 / 2026-11-16T19:17:44.950
- **官方描述（原文）**：Dinky through 1.2.5 contains a missing authorization vulnerability in ClusterConfigurationController that allows authenticated users without cluster configuration permissions to list Flink cluster configurations. Attackers can query the /api/clusterConfiguration/list and listAll endpoints to retrieve full configJson deployment settings for every cluster in their tenant.

### 37. CVE-2026-129851｜seaweedfs / seaweedfs
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T15:17:22.077)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T15:17:22.077 / 2026-11-16T17:17:32.197
- **官方描述（原文）**：SeaweedFS before 4.42 contains a server-side request forgery vulnerability in the VolumeServer.FetchAndWriteNeedle gRPC method that allows unauthenticated attackers to bypass the incomplete CVE-2026-73080 fix. Attackers can supply crafted replicas[].url entries or an azure_endpoint to make the volume server send requests with controlled tokens and bodies to internal services and metadata addresses.

### 38. CVE-2026-129303｜rennf93 / guard-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-16T20:19:01.200)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.7 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-16T20:19:01.200 / 2026-11-16T22:18:20.080
- **官方描述（原文）**：Guard Core is an API security core engine for the FastAPI-Guard, FlaskAPI Guard, and DjAPI Guard adapters. From 1.0.0 until 3.13.0, ContentPreprocessor.preprocess() in guard_core/detection_engine/preprocessor.py collapses all whitespace before built-in pattern matching in the default enhanced mode. This removes carriage returns and newlines required by the http_split and newline-anchored cmd_injection detectors in guard_core/handlers/suspatterns_handler.py, making those detectors unable to match. Framework-decoded CRLF can therefore pass through Guard Core unflagged while the downstream application still receives the raw newline-bearing value. Direct security impact requires a downstream stack or application that persists or re-emits the value into a CRLF-tolerant response or command context. This issue is fixed in version 3.13.0.

### 39. CVE-2026-114713｜UnrealIRCd / UnrealIRCd
- **Delta event**：CVSS_CHANGED (from=8.6; to=7.7)
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.7 (HIGH)
- **EPSS**：0.00508 / percentile=0.43872
- **CISA KEV**：listed=true / date_added=2026-11-13 / due_date=2026-11-16
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-08T03:16:33.410 / 2026-11-16T12:51:36.280
- **官方描述（原文）**：UnrealIRCd UnrealIRCd contains an improper neutralization of delimiters vulnerability that allows any user on a network with two or more linked servers to inject server-to-server commands that are executed with server authority.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-129879 | WATCH / 30 | lintsinghua / DeepAudit | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-129875 | WATCH / 30 | getrebuild / rebuild | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-129863 | WATCH / 30 | GitBucket / GitBucket | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-129855 | WATCH / 30 | samugit83 / RedAmon | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-129854 | WATCH / 30 | samugit83 / RedAmon | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-120698 | WATCH / 30 | requarks / wiki | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93664 | WATCH / 28 | Dassault Systèmes / Station Launcher App in 3DEXPERIENCE platform | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-79614 | WATCH / 28 | Zyxel / DX3301-T0 firmware | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-77033 | WATCH / 28 | Dassault Systèmes / Station Launcher App in 3DEXPERIENCE platform | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-53998 | WATCH / 28 | Arize-ai / phoenix | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-19732 | WATCH / 28 | Dassault Systèmes / Station Launcher App in 3DEXPERIENCE platform | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-130380 | WATCH / 28 | adminneo-org / AdminNeo | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-130371 | WATCH / 28 | thorsten / phpMyFAQ | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-130369 | WATCH / 28 | thorsten / phpMyFAQ | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-130366 | WATCH / 28 | adminneo-org / AdminNeo | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-130327 | WATCH / 28 | Open Object Rexx / ooRexx | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-130320 | WATCH / 28 | Open Object Rexx / ooRexx | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-130071 | WATCH / 28 | TridotsTech / go1cms | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-130070 | WATCH / 28 | muneeb141 / ghost | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-129955 | WATCH / 28 | surmon-china / NodePress | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-129952 | WATCH / 28 | surmon-china / NodePress | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-129941 | WATCH / 28 | birkir / prime | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-129552 | WATCH / 28 | tenseijs / @tensei/auth | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-129550 | WATCH / 28 | tenseijs / @tensei/auth | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-120699 | WATCH / 28 | TencentCloud / CubeSandbox | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-120387 | WATCH / 28 | Circutor / PowerStudio SCADA Wave | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-111559 | WATCH / 28 | sruupl / Batflat | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-104840 | WATCH / 28 | OpenCTI-Platform / opencti | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-69221 | WATCH / 22 | wpengine / faustjs | v3.1 5.9 (MEDIUM) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-129950 | WATCH / 22 | Rowy / Rowy | v4.0 5.3 (MEDIUM) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

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
- EPSS 未確認：30；Exploitation status 未確認：14。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-17T08:41:13.667495+00:00`；Delta generated at：`2026-11-17T08:41:13.667495+00:00`。

---

## 可驗證資料來源

- **CVE-2026-129879** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129879)
- **CVE-2026-129875** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129875)
- **CVE-2026-129863** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129863)
- **CVE-2026-129855** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129855)
- **CVE-2026-129854** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129854)
- **CVE-2026-120698** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120698)
- **CVE-2026-93664** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93664)
- **CVE-2026-79614** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79614)
- **CVE-2026-77033** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77033)
- **CVE-2026-53998** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53998)
- **CVE-2026-19732** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19732)
- **CVE-2026-130380** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130380)
- **CVE-2026-130371** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130371)
- **CVE-2026-130369** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130369)
- **CVE-2026-130366** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130366)
- **CVE-2026-130327** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130327)
- **CVE-2026-130320** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130320)
- **CVE-2026-130071** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130071)
- **CVE-2026-130070** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130070)
- **CVE-2026-129955** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129955)
- **CVE-2026-129952** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129952)
- **CVE-2026-129941** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129941)
- **CVE-2026-129552** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129552)
- **CVE-2026-129550** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129550)
- **CVE-2026-120699** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120699)
- **CVE-2026-120387** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120387)
- **CVE-2026-111559** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111559)
- **CVE-2026-104840** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104840)
- **CVE-2026-69221** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69221)
- **CVE-2026-129950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129950)
- **CVE-2026-129887** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129887)
- **CVE-2026-129886** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129886)
- **CVE-2026-129883** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129883)
- **CVE-2026-129871** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129871)
- **CVE-2026-129867** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129867)
- **CVE-2026-129866** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129866)
- **CVE-2026-129851** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129851)
- **CVE-2026-129303** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129303)
- **CVE-2026-114713** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114713) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114713) · [Vendor / Advisory (forums.unrealircd.org)](https://forums.unrealircd.org/viewtopic.php?t=9487) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
