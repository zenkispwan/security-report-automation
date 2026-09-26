# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**68** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=1、EPSS_INCREASED=2、NEW_CVE=62、NEW_KEV=3。
- Intelligence 候選：**30** 筆；P1 **6**、P2 **0**、P3 **2**、WATCH **22**。
- Baseline：state / generated_at=2026-09-25T05:38:02.420690+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-87902、CVE-2026-65660、CVE-2026-67279、CVE-2026-93616、CVE-2026-85706。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **68** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-87902｜WordPress / Core
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.02877 / percentile=0.86275
- **CISA KEV**：listed=true / date_added=2026-09-25 / due_date=2026-09-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-22T17:17:28.310 / 2026-09-26T04:17:49.733
- **官方描述（原文）**：WordPress Core contains a remote file inclusion vulnerability which could allow an unauthenticated attacker to make page-template resolution include a chosen readable local `.php` file outside the active theme directories, leading to remote code execution.

### 2. CVE-2026-65660｜Microsoft / SharePoint
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.01221 / percentile=0.6743
- **CISA KEV**：listed=true / date_added=2026-09-25 / due_date=2026-09-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-08-11T17:18:54.080 / 2026-09-26T04:17:45.630
- **官方描述（原文）**：Microsoft SharePoint contains a code injection vulnerability which could allow an authorized attacker to execute code over a network.

### 3. CVE-2026-67279｜MikroTik / RouterOS
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.0071 / percentile=0.51535
- **CISA KEV**：listed=true / date_added=2026-09-25 / due_date=2026-09-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-05T20:17:18.390 / 2026-09-26T04:17:47.273
- **官方描述（原文）**：Mikrotik RouterOS contains an improper enforcement of behavioral workflow vulnerability that could allow an unauthenticated client to open a session channel and send an exec request. This vulnerability can be chained to achieve unauthenticated exploitation of CVE-2026-86060.

### 4. CVE-2026-93616｜Check Point / Multiple Products
- **Delta event**：EPSS_INCREASED (from=0.02421; to=0.19654)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.19654 / percentile=0.97303
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-22T13:17:11.963 / 2026-09-23T16:38:38.987
- **官方描述（原文）**：Check Point Security Management Server, Multi-Domain Security Management Server, Log Server, Multi-Domain Log Server, and SmartEvent contain a path traversal vulnerability that allows an unauthenticated attacker to upload and execute arbitrary scripts.

### 5. CVE-2026-85706｜GitLab / Community Edition and Enterprise Edition
- **Delta event**：EPSS_INCREASED (from=0.09287; to=0.91425)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.91425 / percentile=0.9981
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-12T03:16:30.473 / 2026-09-24T12:52:28.143
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contains a path traversal vulnerability that allows an unauthenticated user to read arbitrary files due to an improper path confinement and missing authentication enforcement in the repository commits API.

### 6. CVE-2026-85542｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T14:17:20.193)
- **Risk**：P1 / score 45；reasons：ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=active / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T14:17:20.193 / 2026-09-26T04:17:49.463
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is affected by a command injection vulnerability in the GIM bundle import functionality. An authenticated attacker can provide a crafted GIM bundle that causes attacker-controlled arguments to be passed to the tar command, resulting in arbitrary command execution with elevated privileges on the Central Manager.

### 7. CVE-2026-97063｜yzcheng90 / X-SpringBoot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T19:17:59.267)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T19:17:59.267 / 2026-09-25T19:17:59.267
- **官方描述（原文）**：X-SpringBoot through 6.0 returns login verification codes in HTTP responses from unauthenticated endpoints GET /sys/mobile/code and GET /sys/email/code without sending them to account owners. Attackers can request codes using known mobile numbers or email addresses, read them from responses, and authenticate as victims via POST /sys/emailOrMobileLogin/login to hijack accounts.

### 8. CVE-2026-39353｜InvoicePlane / InvoicePlane
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:25.053)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:25.053 / 2026-09-25T17:17:08.360
- **官方描述（原文）**：InvoicePlane is a self-hosted open source application for managing invoices, clients, and payments. Prior to 1.7.2-rc-1, InvoicePlane builds its permitted template list by scanning a PHP template directory that can be written through an administrator-controlled file-write capability. A malicious PHP file placed in the directory is automatically trusted by Mdl_templates and can be selected as public_invoice_template. When a public invoice is rendered, the guest View controller includes the trusted file and executes it with web-server privileges. This issue is fixed in version 1.7.2-rc-1.

### 9. CVE-2026-93834｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T14:17:24.063)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T14:17:24.063 / 2026-09-25T14:17:24.063
- **官方描述（原文）**：A use-after-free vulnerability was found in QEMU's 9pfs subsystem. A race condition between the main thread and a worker thread when processing concurrent Tlcreate and Twalk requests allows a malicious guest user to craft a fid path containing stale heap data, bypassing directory traversal restrictions and escaping the shared directory boundary. This can lead to arbitrary host file read/write and code execution (VM escape) as the QEMU process user.

### 10. CVE-2026-88421｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T13:17:16.903)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T13:17:16.903 / 2026-09-25T17:17:18.050
- **官方描述（原文）**：Incorrect access control in the BlogPage.get_entries() component of APSL puput v1.2.1 through v2.2.0 allows unauthenticated attackers to view restricted blog entries via the blog index, the tag, category, author and date archives, the sidebar widgets, or the RSS feed.

### 11. CVE-2026-85750｜Piwigo / Piwigo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T14:17:20.330)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T14:17:20.330 / 2026-09-25T15:17:56.560
- **官方描述（原文）**：Piwigo before v16.4.0 is vulnerable to arbitrary file read and remote code execution in image upload handling when using the Imagick library due to insufficient validation and unsafe processing of user-supplied image files. By abusing format confusion (e.g., disguising SVG content as PNG), an attacker can trigger unintended interpretation of embedded SVG elements that reference local files. In more advanced scenarios, the Imagick support for Magick Scripting Language (MSL) may be abused to process attacker-controlled instructions, potentially leading to unauthorized server-side file writes and remote code execution, depending on configuration. This has been patched in 16.4.0.

### 12. CVE-2026-67419｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:13.830)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:13.830 / 2026-09-25T18:17:30.443
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. Prior to 4.3.5, an authenticated user who can bind a queue to a topic exchange and publish to it can use consecutive # segments in a binding key to make both topic matchers revisit the same trie-node and routing-key-suffix states without memoization. The matcher materializes duplicate destinations before deduplication, causing combinatorial CPU work and memory pressure that can disrupt routing for all tenants. This vulnerability is fixed in 4.3.5.

### 13. CVE-2026-67410｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:13.093)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:13.093 / 2026-09-25T18:17:30.320
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. From 4.2.0 until 4.3.3 and 4.2.9, OAuth2 Client Secret Exposed via Unauthenticated JavaScript Endpoint (CWE-200). when OAuth2 authentication is enabled for the RabbitMQ Management UI and the configured flow, IDP use a client secret, the oauthclientsecret configuration value is included in the JavaScript served by the unauthenticated endpoint /js/oidc-oauth/bootstrap.js. Any user who can reach the management UI port can retrieve the OAuth2 client secret without Files: deps/rabbitmqmanagement/src/rabbitmgmtwmauth.erl, line 186 deps/rabbitmqmanagement/src/rabbitmgmtoauthbootstrap.erl, lines 35-50 deps/rabbitmqmanagement/src/rabbitmgmtdispatcher.erl, lines 45-49 (route registration) Code Path: 1. The route /js/oidc-oauth/bootstrap.js is registered as a plain Cowboy handler (rabbitmgmtdispatcher.erl:46): Credential exposure for the affected configuration: OAuth2 client secret is accessible without any authentication Token theft: Attacker can complete the authorization code flow using stolen authorization codes Client impersonation: Attacker can make requests. Any RabbitMQ deployment with: This issue is fixed in versions 4.3.3 and 4.2.9.

### 14. CVE-2026-67409｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:12.943)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:12.943 / 2026-09-25T18:17:30.190
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. From 3.13.0 until 4.3.3, 4.2.9, 4.1.14, 4.0.23, and 3.13.18, JWKS Fetch Ignores HTTP Response Status Code - Signing Key Destruction Causes Authentication DoS (CWE-252). the JWKS key fetching mechanism in uaajwt.erl does not validate the HTTP response status code when downloading signing keys from the OAuth2 provider's JWKS endpoint. Non-200 responses (including 4xx and 5xx errors) are processed identically to successful responses. When the JWKS endpoint returns an error response with a valid-JSON body that lacks a keys field, all previously cached signing keys are destroyed, causing a persistent authentication denial of Files: deps/rabbitmqauthbackendoauth2/src/uaajwt.erl, lines 50-63 deps/rabbitmqauthbackendoauth2/src/uaajwks.erl, lines 5-7 deps/rabbitmqauthbackendoauth2/src/rabbitoauth2provider.erl, lines 98-107 Bug 1: HTTP status code ignored (uaajwt.erl:50-63): The Erlang httpc module returns {ok, {{HttpVersion, StatusCode, ReasonPhrase}, Headers, Body}}. The pattern {ok, {, , JwksBody}} matches ANY successful HTTP transaction Persistent authentication DoS: Once keys are destroyed, ALL OAuth2/JWT authentication fails for all users until a new successful JWKS refresh occurs Amplification: A single attacker can deny access to all legitimate OAuth2 users across the entire RabbitMQ. This issue is fixed in versions 4.3.3, 4.2.9, 4.1.14, 4.0.23, and 3.13.18.

### 15. CVE-2026-67408｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:12.767)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:12.767 / 2026-09-25T20:17:39.313
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. From 4.1.0 until 4.3.3, 4.2.9, and 4.1.11, Stream Management Super-Stream Binding Keys Allocation Allows Low-Privilege Node Denial of Service. rabbitMQ 4.3.1 with rabbitmqstreammanagement enabled accepts PUT /api/stream/super-streams/{vhost}/{name} requests from an authenticated management user that can access the target vhost. When the request body contains the binding-keys field, the handler parses the attacker-controlled comma-separated string and builds the full stream-name list before checking whether the user has permission to configure the resulting streams. A low-privileged management user with vhost access but no configure, write, or read permission can therefore force large transient allocations before the resource permission check. In a 768 MB memory-limited container, one HTTP PUT with about 4.5 MB of JSON body killed the RabbitMQ container with Docker state exited true An authenticated low-privileged management user can kill a memory-limited RabbitMQ node with one HTTP This issue is fixed in versions 4.3.3, 4.2.9, and 4.1.11.

### 16. CVE-2026-51773｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T13:17:14.673)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T13:17:14.673 / 2026-09-25T17:17:08.900
- **官方描述（原文）**：An issue in the VMware datastore driver of OpenStack glance_store. When an authenticated attacker provides a maliciously crafted image location URI pointing to an external server, the _retry_request function fails to validate the destination host before attaching sensitive authentication headers.

### 17. CVE-2026-44642｜Piwigo / Piwigo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:25.970)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:25.970 / 2026-09-25T17:17:08.577
- **官方描述（原文）**：Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, check_upgrade_access_rights() in admin/include/functions_upgrade.php conditionally escapes the submitted username only when the removed get_magic_quotes_gpc function exists, so PHP 8 and later concatenate an unauthenticated username directly into the upgrade authentication SQL query. When database upgrades are pending, a crafted query result can satisfy the status and password checks, set PHPWG_IN_UPGRADE, and authorize upgrade execution without valid administrator credentials. This can cause unauthorized database integrity changes and service disruption. This vulnerability is fixed in 16.4.0.

### 18. CVE-2026-42324｜Piwigo / Piwigo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:25.793)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:25.793 / 2026-09-25T17:17:08.467
- **官方描述（原文）**：Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, admin/element_set_ranks.php stores administrator-controlled image_order[] values without enforcing the existing sort-field whitelist. The stored album image_order expression is later concatenated into ORDER BY clauses by admin/batch_manager_global.php, admin/batch_manager_unit.php, include/section_init.inc.php, and include/ws_functions/pwg.categories.php. When at least one album contains at least one photo, an authenticated administrator can store a crafted expression and trigger it in a later album or Batch Manager query to disclose, modify, or disrupt database data. This issue is fixed in version 16.4.0.

### 19. CVE-2025-51457｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T13:17:05.613)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T13:17:05.613 / 2026-09-25T16:17:23.823
- **官方描述（原文）**：D-Link DAP-2610 up to 2.06B08r099 contains an authenticated command injection vulnerability within the web interface at the /index.xgi endpoint. An attacker with authenticated access can exploit some parameters to execute arbitrary system commands.

### 20. CVE-2026-97064｜yzcheng90 / X-SpringBoot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T19:17:59.427)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T19:17:59.427 / 2026-09-25T19:17:59.427
- **官方描述（原文）**：X-SpringBoot through 6.0 ships with a hardcoded static master login verification code 172839 enabled by default in the database seed. Unauthenticated attackers can authenticate as any user by submitting the public master code to the emailOrMobileLogin endpoint with a known email or mobile number.

### 21. CVE-2026-95832｜Kovid Goyal / kitty
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T13:17:24.063)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T13:17:24.063 / 2026-09-25T16:17:30.250
- **官方描述（原文）**：Improper Neutralization of Special Elements in Output Used by a Downstream Component in the colour control escape code handler in kitty from 0.47.3 before 0.49.0 allows a program writing to the terminal to execute an arbitrary command in the user's shell, because color_control() in kitty/window.py answers a query for an unrecognised field name by placing that field name into the reply, and write_escape_code_to_child() in kitty/screen.c then writes the reply to the pseudoterminal master, where it is not distinguishable from input typed by the user, without neutralising it for the shell that reads it. The payload is reduced to printable ASCII before the field name is echoed, which is the restriction introduced in 0.47.3 as the fix for CVE-2026-54057, and the record and field separators ; and = are consumed as delimiters, but every other printable character survives, which is sufficient to compose a shell command. A newline is available from handle_remote_ssh() in kitty/window.py, which writes the bytes yielded by get_ssh_data() in kittens/ssh/utils.py, the first of which begin with a newline, to the pseudoterminal master before any credential carried in the request is checked. The reply is framed as an OSC sequence carrying the escape code number, the field name, and the literal value ?. This results in execution of an attacker-chosen command with the privileges of the user running the terminal.

### 22. CVE-2026-93647｜Zimbra / Zimbra Collaboration Suite (ZCS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T14:17:23.673)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T14:17:23.673 / 2026-09-26T04:17:52.143
- **官方描述（原文）**：An unauthenticated calendar sender can place active markup in a COUNTER message's RFC From address. Selecting the message in Zimbra Classic triggers stored XSS, allowing the attacker to access mailbox data and act as the victim.

### 23. CVE-2026-93643｜Zimbra / Zimbra Collaboration Suite (ZCS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T14:17:23.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T14:17:23.550 / 2026-09-26T04:17:51.710
- **官方描述（原文）**：When OnlyOffice/Document Editing is available, an unauthenticated remote attacker with access to an existing supported public Briefcase document can abuse unsigned save fields to perform path-traversal writes and execute commands as zimbra.

### 24. CVE-2026-93642｜Zimbra / Zimbra Collaboration Suite (ZCS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T14:17:23.423)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T14:17:23.423 / 2026-09-25T17:17:19.750
- **官方描述（原文）**：An unauthenticated sender can forge a share notification that triggers stored XSS when a signed-in Zimbra Modern recipient clicks Accept Share, allowing the attacker to access mailbox data and act as the victim.

### 25. CVE-2026-93641｜Zimbra / Zimbra Collaboration Suite (ZCS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T14:17:23.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T14:17:23.290 / 2026-09-25T17:17:19.650
- **官方描述（原文）**：An unauthenticated sender can forge a share notification that triggers stored XSS when a signed-in Zimbra Classic recipient clicks Accept Share, allowing the attacker to access mailbox data and act as the victim.

### 26. CVE-2026-93399｜ladela / Online Scheduling and Appointment Booking System – Bookly
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T07:16:56.027)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.0037 / percentile=0.28244
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T07:16:56.027 / 2026-09-25T13:08:26.930
- **官方描述（原文）**：The Bookly plugin for WordPress is vulnerable to Insecure Direct Object Reference in versions up to, and including, 28.2 via the 'bookly_get_form_id', 'bookly_render_complete', 'bookly_add_to_calendar' and 'bookly_rollback_order' AJAX actions. This is due to the 'bookly_get_form_id' handler blindly storing the attacker-controlled 'order_id' from the submitted form_data into a new booking session, which the 'bookly_render_complete' handler then trusts to look up and return the corresponding Order's secret token without verifying that the current session created that order. This makes it possible for unauthenticated attackers to enumerate sequential order IDs, disclose other customers' order tokens, retrieve calendar/appointment information via 'bookly_add_to_calendar' and permanently delete arbitrary non-completed bookings via 'bookly_rollback_order', which cascade-deletes the customer_appointment and (when no other customers are attached) the underlying appointment.

### 27. CVE-2026-92609｜Apache Software Foundation / Apache Qpid Broker-J
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T08:16:41.203)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00195 / percentile=0.08173
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T08:16:41.203 / 2026-09-25T14:17:22.317
- **官方描述（原文）**：Session fixation in HTTP management authentication allows remote attackers to gain unauthorized access to an authenticated management session via reuse of a session identifier retained across successful authentication. This issue affects Apache Qpid Broker-J: through 10.1.0. Users are recommended to upgrade to version 10.1.1, which fixes the issue.

### 28. CVE-2026-92161｜FriendsOfFlarum / oauth
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:29.387)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:29.387 / 2026-09-25T16:17:29.387
- **官方描述（原文）**：FriendsOfFlarum OAuth allows users to log in to Flarum with GitHub, Twitter, Facebook, and other providers. Prior to 1.7.4 and 2.0.0-beta.4, the Discord OAuth provider does not check the verified field returned for an OAuth email before passing the address to Flarum core as trusted through provideTrustedEmail(). When Discord sign-in is enabled, an unauthenticated attacker who knows the email address of a Flarum user can configure a Discord account with that unverified address and a verified phone number, then sign in to cause Flarum to match the trusted address, link the attacker-controlled Discord identity to the existing user, and authenticate as the victim without a password or victim interaction. Exploitation requires that the victim's email address is not already associated with a Discord account, and it can compromise administrator accounts. Other bundled providers were not confirmed to be practically exploitable by this method because their relevant authentication flows return only verified or confirmed email addresses. This issue is fixed in versions 1.7.4 and 2.0.0-beta.4.

### 29. CVE-2026-89055｜ivole / Customer Reviews for WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T07:16:55.140)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00385 / percentile=0.29793
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T07:16:55.140 / 2026-09-25T14:17:21.510
- **官方描述（原文）**：The Customer Reviews for WooCommerce plugin for WordPress is vulnerable to authorization bypass in all versions up to, and including, 5.120.0. This is due to the plugin not properly verifying that a user is authorized to perform an action. This makes it possible for unauthenticated attackers to permanently delete arbitrary attachments from the Media Library — including administrator-owned product images, logos, and documents — by injecting their IDs into a review that is later trashed and purged. Exploitation requires a public review-form link (a 13-hex formId distributed to customers via e-mail), which exposes the nonce needed to reach the handler without any WordPress account or session.

### 30. CVE-2026-84458｜zammad / zammad
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T19:17:57.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T19:17:57.130 / 2026-09-25T19:17:57.130
- **官方描述（原文）**：Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, when the "Automatic account link on initial logon" setting is enabled, Zammad binds an incoming third-party (SSO) identity to an existing local account by matching the email address the identity provider reports, without verifying that the provider actually confirmed ownership of that email. An attacker who controls any identity at a configured provider, including, by default, any Azure AD tenant via Zammad's multi-tenant Microsoft 365 /common app registration, can set that identity's email to a victim's address, authenticate, and be logged in as the victim. This bypasses the victim's local password entirely and affects any existing account, including agents and administrators. Zammad will honor the xms_edov ID token claim when email verification is required in the Microsoft 365 setting, treating a missing claim as unverified. This issue is fixed in version 7.1.2.

### 31. CVE-2026-62262｜Piwigo / Piwigo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:26.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:26.750 / 2026-09-25T16:17:26.877
- **官方描述（原文）**：Piwigo is a full featured open source photo gallery application for the web. In 17.0.0beta1 and earlier, when rating is enabled, an unauthenticated guest can call pwg.images.filteredSearch.create with a crafted ratings[] value and then open the returned search URL. include/ws_functions/pwg.images.php stores the unvalidated value in the search rules, and include/functions_search.inc.php integer-casts only the lower rating bound while concatenating the raw value as the SQL upper bound. This allows error-based or blind extraction of database information and database-dependent time delays through the public search flow. No fixed version is available as of this review.

### 32. CVE-2026-48482｜glpi-project / glpi
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T19:16:55.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T19:16:55.180 / 2026-09-25T19:16:55.320
- **官方描述（原文）**：GLPI is a free asset and IT management software package. From 11.0.0 until 11.0.8, a form administrator can use Form import with a crafted illustration or scene identifier that traverses outside the intended custom-asset directory. The imported file can be written to an executable server location, allowing a malicious script to be invoked remotely. This issue is fixed in version 11.0.8.

### 33. CVE-2026-42322｜Piwigo / Piwigo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:25.420)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:25.420 / 2026-09-25T16:17:25.563
- **官方描述（原文）**：Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, admin/themes_standard_pages.php validates uploaded logo content by MIME type but reuses the attacker-controlled extension from std_pgs_logo when constructing the stored filename. An authenticated administrator can upload image content with a server-executable final extension, causing the file to be placed in the web-accessible logo directory and executed when requested if the web server handles that extension. This can permit arbitrary command execution, data disclosure, modification, persistence, and service disruption. This vulnerability is fixed in 16.4.0.

### 34. CVE-2026-14281｜101gen / Automation Web Platform – Notifications and OTP for WooCommerce, Advanced Country Code
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T07:16:53.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00531 / percentile=0.4248
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T07:16:53.540 / 2026-09-25T13:08:26.930
- **官方描述（原文）**：The Automation Web Platform – Notifications and OTP for WooCommerce, Advanced Country Code plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 4.8.6. This is due to missing permission enforcement on the publicly accessible REST route `POST /wp-json/wawp/v1/signup/<op>` and the absence of a key allowlist in the `finish_registration_logic` function, which copies the attacker-controlled `wawp_custom_fields` parameter directly into `update_user_meta()` — allowing sensitive meta keys such as `wp_capabilities` and `wp_user_level` to be set by the caller. This makes it possible for unauthenticated attackers to register a new account with the administrator role and gain full administrative access to the site. When OTP verification is enabled at signup, the OTP session token (`otp_transient`) is returned in plaintext in the HTTP response body, and the `handle_magic_link_request()` handler marks that token as verified on any unauthenticated GET request containing it without ever checking the OTP code value — making the OTP step trivially bypassable with no inbox or SMS access required.

### 35. CVE-2026-100551｜OpenClaw / OpenClaw
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T03:17:01.487)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T03:17:01.487 / 2026-09-26T03:17:01.487
- **官方描述（原文）**：OpenClaw for iOS versions >= 2026.7.1 and < 2026.8.11 do not enforce saved Gateway TLS pins in the Control UI. While native connections enforced the saved Gateway fingerprint, the authenticated Terminal and session Dashboard WebViews omitted it. If a user had accepted a Gateway fingerprint, an attacker able to redirect the same host and port and present a different certificate that is accepted by iOS system trust can serve a replacement Control UI page; opening the Terminal or a session Dashboard then allows that page to read the injected Gateway token or password. The stolen credential can grant operator access, including reading sensitive Gateway state and invoking host-capable tools. This issue is fixed in 2026.8.11.

### 36. CVE-2026-100390｜tobychui / zoraxy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T21:17:22.637)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T21:17:22.637 / 2026-09-25T21:17:22.637
- **官方描述（原文）**：Zoraxy versions 3.2.3 through 3.3.4 fail to properly parse IPv6 addresses in the RemoteAddr field when setting forwarded headers. Unauthenticated attackers connecting over IPv6 can supply arbitrary X-Forwarded-For values to spoof their source IP and bypass authorization provider IP-based access controls.

### 37. CVE-2026-100389｜GestSup / GestSup
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T21:17:22.483)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T21:17:22.483 / 2026-09-25T21:17:22.483
- **官方描述（原文）**：GestSup versions before 3.2.61 contain a remote code execution vulnerability in the basic IMAP connector's attachment handling that fails to skip blocked file extensions. Unauthenticated attackers can send emails with PHP attachments to monitored mailboxes, which are written to the web-accessible upload/ticket directory and executed when accessed.

### 38. CVE-2026-100382｜Wikimedia Foundation / Mediawiki - ExternalData Extension
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T22:17:10.150)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T22:17:10.150 / 2026-09-25T22:17:10.150
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Wikimedia Foundation Mediawiki - ExternalData Extension allows OS Command Injection. This issue affects Mediawiki - ExternalData Extension: from * before 3.7.

### 39. CVE-2026-100075｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T14:17:14.163)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T14:17:14.163 / 2026-09-25T15:17:52.117
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: RDMA/srpt: Fix srpt_alloc_rw_ctxs() unwind counters When srpt_alloc_rw_ctxs() fails partway through a multi-buffer indirect descriptor, the unwind path destroys RDMA contexts but leaves stale n_rw_ctx and n_rdma values (and a dangling rw_ctxs pointer). Later sq_wr_avail accounting in srpt_queue_response() or srpt_write_pending() can then subtract the wrong number of send queue credits. Reset the counters and clear rw_ctxs after freeing the heap allocation before returning an error.

### 40. CVE-2026-97885｜mathurvishal / CloudClassroom-PHP-Project
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T18:17:35.613)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T18:17:35.613 / 2026-09-25T18:17:35.613
- **官方描述（原文）**：A flaw has been found in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db3fb95b66e7be. Affected is an unknown function of the file updatefaculty.php. This manipulation of the argument fid causes sql injection. The attack may be initiated remotely. The exploit has been published and may be used. This product uses a rolling release model to deliver continuous updates. As a result, specific version information for affected or updated releases is not available. The vendor was contacted early about this disclosure but did not respond in any way.

### 41. CVE-2026-97883｜mathurvishal / CloudClassroom-PHP-Project
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T18:17:35.247)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T18:17:35.247 / 2026-09-25T18:17:35.247
- **官方描述（原文）**：A security vulnerability has been detected in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db3fb95b66e7be. This affects an unknown function of the file updatequery.php. The manipulation of the argument gid leads to sql injection. The attack can be initiated remotely. The exploit has been disclosed publicly and may be used. Continious delivery with rolling releases is used by this product. Therefore, no version details of affected nor updated releases are available. The vendor was contacted early about this disclosure but did not respond in any way.

### 42. CVE-2026-97879｜zhistaredu / StarTraining
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:22.113)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:22.113 / 2026-09-25T18:17:34.930
- **官方描述（原文）**：A security flaw has been discovered in zhistaredu StarTraining up to 3.8.1. The affected element is an unknown function of the file SecurityConfig.java of the component api-docs Endpoint. Performing a manipulation results in missing authentication. It is possible to initiate the attack remotely. The exploit has been released to the public and may be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 43. CVE-2026-97878｜zhistaredu / StarTraining
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:21.940)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:21.940 / 2026-09-25T18:17:34.797
- **官方描述（原文）**：A vulnerability was identified in zhistaredu StarTraining up to 3.8.1. Impacted is the function anonymous of the file /druid/index.html of the component Druid Console. Such manipulation leads to missing authentication. The attack may be performed from remote. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 44. CVE-2026-97877｜zhistaredu / StarTraining
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:21.763)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:21.763 / 2026-09-25T18:17:34.660
- **官方描述（原文）**：A vulnerability was determined in zhistaredu StarTraining up to 3.8.1. This issue affects the function UserLoginService.createToken of the file application.yml of the component JWT Token Handler. This manipulation of the argument user_id/company_id causes use of hard-coded password. The attack is possible to be carried out remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 45. CVE-2026-97871｜Zhonglun / CloudPos
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:21.443)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:21.443 / 2026-09-25T17:17:21.443
- **官方描述（原文）**：A vulnerability has been found in Zhonglun CloudPos up to 3.0.1.76. This issue affects the function OpenLocalBrowser of the file ZlPos/ZlPos/Bizlogic/JSBridge.cs of the component JSBridge. Such manipulation of the argument url leads to code injection. The attack can be executed remotely. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 46. CVE-2026-97864｜GibbonEdu / Gibbon
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T14:17:27.217)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T14:17:27.217 / 2026-09-25T14:17:27.217
- **官方描述（原文）**：A vulnerability has been found in GibbonEdu Gibbon up to 30.0.01. The affected element is the function makeBlock of the file modules/Planner/units_add_blockAjax.php of the component Unit Planner. The manipulation of the argument gibbonUnitBlockID/mode leads to missing authentication. The attack is possible to be carried out remotely. The exploit has been disclosed to the public and may be used. Upgrading to version 31.0.00 is sufficient to fix this issue. The identifier of the patch is 07e719368eae8dfb4e22e19424ceab6074164ebc. It is recommended to upgrade the affected component.

### 47. CVE-2026-93682｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T20:17:47.597)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T20:17:47.597 / 2026-09-25T21:17:25.047
- **官方描述（原文）**：When the HTTP stream wrapper follows a redirect and the response carries a Location header with an empty value, the redirect code reads one byte past the end of the heap buffer holding the location. The value of that out-of-bounds byte decides which redirect target is built, so a malicious server controls whether the client is sent to the host root or to the current directory.

### 48. CVE-2026-85293｜InvoicePlane / InvoicePlane
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:28.743)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:28.743 / 2026-09-25T16:17:28.743
- **官方描述（原文）**：InvoicePlane is a self-hosted open source application for managing invoices, clients, and payments. In version 1.7.2-beta-1, InvoicePlane stores client_email values without enforcing email syntax and renders them unescaped inside double-quoted value attributes in the invoice mailer form and quote mailer form. An administrator who can edit a client can store attribute-breaking input, and, when the mailer is configured, JavaScript executes when another authenticated administrator opens the related mailer page. The script runs in the InvoicePlane origin and can perform same-origin actions with the victim's session. This issue is fixed in version 1.7.2.

### 49. CVE-2026-85289｜InvoicePlane / InvoicePlane
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:28.157)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:28.157 / 2026-09-25T16:17:28.157
- **官方描述（原文）**：InvoicePlane is a self-hosted open source application for managing invoices, clients, and payments. Prior to 1.7.2, InvoicePlane omits ensure_valid_post_request() from delete methods including Payments::delete(), Recurring::delete(), and User_clients::delete(). Although the routes require POST, they do not validate the request's CSRF token. An attacker can submit a cross-origin form through an authenticated administrator's browser to delete financial records and other application data. This issue is fixed in version 1.7.2.

### 50. CVE-2026-85274｜InvoicePlane / InvoicePlane
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:28.010)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:28.010 / 2026-09-25T17:17:16.013
- **官方描述（原文）**：InvoicePlane is a self-hosted open source application for managing invoices, clients, and payments. Prior to 1.7.2, InvoicePlane exposes Recurring::stop() as a state-changing GET route without CSRF token validation. When an authenticated administrator loads attacker-controlled content that requests /invoices/recurring/stop/{id}, the application stops the selected recurring invoice. An attacker can target multiple identifiers to interrupt recurring billing and cause financial loss. This issue is fixed in version 1.7.2.

### 51. CVE-2026-78902｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T13:17:16.170)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T13:17:16.170 / 2026-09-25T17:17:14.540
- **官方描述（原文）**：Cross Site Scripting vulnerability in Netgate pfSense 26.03.1-RELEASE allows an attacker to execute arbitrary code via the pfBlockerNG package

### 52. CVE-2026-67421｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:14.120)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 4.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:14.120 / 2026-09-25T20:17:39.547
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. From 3.13.0 until 3.13.19, 4.0.24, 4.1.15, 4.2.10, and 4.3.5, RabbitMQ Management rendered an AMQP authorization-error reason containing an attacker-controlled queue name as HTML when the OAuth management UI was enabled. Exploitation requires an attacker with queue configure permission, a management administrator who can see but cannot read that queue, and the administrator clicking Get Message(s). A queue name containing a base element can then retarget the automatic relative refresh because the Content Security Policy omits base-uri and connect-src, and an attacker endpoint that permits the management origin through CORS can receive the victim's Authorization header. This issue is fixed in versions 3.13.19, 4.0.24, 4.1.15, 4.2.10, and 4.3.5.

### 53. CVE-2026-67415｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:13.690)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:13.690 / 2026-09-25T20:17:39.433
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. From 4.2.0 until 4.2.9 and 4.3.3, the Shovel parameter parser converted attacker-controlled runtime parameter values into non-garbage-collected Erlang atoms before bounding them or checking a fixed allowlist. Exploitation requires network access to the Management HTTP API, valid credentials with both the management and policymaker tags, permission to set Shovel runtime parameters on a vhost, and the rabbitmq_shovel and rabbitmq_shovel_management plugins to be enabled. The attacker can exhaust the node-wide atom table and deny service, and malicious parameters are stored durably and reparsed when workers start, so atom pressure can recur after restart without a live attacker connection. This issue is fixed in versions 4.2.9 and 4.3.3.

### 54. CVE-2026-67412｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:13.393)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.0 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:13.393 / 2026-09-25T17:17:13.393
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. From 3.13.0 until 4.3.3, 4.2.9 , 4.1.14, 4.0.24, and 3.13.18, Federation upstream in RabbitMQ skips vhost authorization allowing cross-vhost message access. what the bug lets you do. A policymaker on one vhost reads and drains messages out of another vhost it has no permission on. With the default ack-mode the source messages are consumed (deleted), not copied. Why that should not 1. Federation validates the upstream URI without any vhost-access Cross-vhost message read/drain from a per-vhost policymaker, breaking vhost tenancy This issue is fixed in versions 4.3.3, 4.2.9 , 4.1.14, 4.0.24, and 3.13.18.

### 55. CVE-2026-67411｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:13.237)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.0 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:13.237 / 2026-09-25T17:17:13.237
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. From 3.13.0 until 3.13.18, 4.0.23, 4.1.14, 4.2.9, and 4.3.3, native MQTT and MQTT over WebSocket behind a trusted PROXY Protocol frontend could lose the proxy-derived client address before the MQTT authentication path checked loopback_users, causing the frontend-to-broker address to be treated as loopback. An attacker who can reach the trusted frontend and has valid credentials for a loopback-restricted account can therefore bypass the source-address restriction; the issue does not bypass password authentication. This issue is fixed in versions 3.13.18, 4.0.23, 4.1.14, 4.2.9, and 4.3.3.

### 56. CVE-2026-67242｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:12.337)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:12.337 / 2026-09-25T20:17:39.107
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. From 4.2.0 until 4.2.9 and 4.3.3, OAuth2 isinteger(Exp) guard skips token-expiry checks for float exp. validatetokenexpiry/1 (lines 208-214) and expirytimestamp/1 (138-144) both guard with 'when isinteger(Exp)' and fall through to ok/never for float values. josejwt:verify validates only the signature, not exp. With float exp, no expiry validation occurs anywhere in the If the IdP emits exp as a JSON float (RFC 7519 permits fractional NumericDate), both the login-time expiry check and the mid-connection disconnect timer are silently skipped , an already-expired token is accepted, and connections never time OAuth2 backend enabled IdP emits float exp (uncommon; mainstream IdPs emit integers) Attacker possesses a previously-valid signed. This issue is fixed in versions 4.2.9 and 4.3.3.

### 57. CVE-2026-67226｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T17:17:11.000)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T17:17:11.000 / 2026-09-25T20:17:38.860
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. From 4.0.0 until 4.0.22 and 4.1.14 and 4.2.7, Admin-only atom exhaustion: PUT /api/users tags list. settags/2 maps rabbitdatacoercion:toatom/1 over the user's tags list. The 20 MB management body limit fits ~3-4M short tag strings. An administrator can crash the node in a single request by creating a user (or importing definitions) with ~1M unique tag administrator. This issue is fixed in versions 4.0.22 and 4.1.14 and 4.2.7.

### 58. CVE-2026-6103｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T21:17:23.790)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T21:17:23.790 / 2026-09-25T21:17:23.790
- **官方描述（原文）**：phar_tar_number() parses the octal size field of a TAR header into a uint32_t with no overflow check. The field is 11 octal digits wide and holds values up to 0x1FFFFFFFF, so a size above 0xFFFFFFFF silently wraps. The parser then skips the wrong number of data blocks and interprets attacker-controlled file content as the next TAR header, which lets a crafted archive inject entries that PharData reports and extracts as if they were genuine.

### 59. CVE-2026-17545｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T21:17:23.253)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T21:17:23.253 / 2026-09-25T21:17:23.253
- **官方描述（原文）**：On Windows, PHP's filesystem and stream APIs do not reject reserved device names such as CON, PRN, AUX, NUL, COM1 to COM9, LPT1 to LPT9, CONIN$ and CONOUT$ when they appear as a component of a path. An attacker-controlled filename therefore reaches CreateFileW() and opens a device instead of the regular file the application expected, which can block or hang the request and exhaust worker processes.

### 60. CVE-2026-100373｜open-metadata / OpenMetadata
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T20:17:06.293)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T20:17:06.293 / 2026-09-25T21:17:21.393
- **官方描述（原文）**：OpenMetadata through 2.0.2 contains a server-side request forgery vulnerability in the URLValidator.validateURL function that fails to properly resolve DNS hostnames and validate internal addresses. Users permitted to create or update EventSubscription can set webhook destinations to internal hosts, allowing the server to send requests to private networks and cloud metadata endpoints while returning HTTP status codes that enable blind SSRF probing.

### 61. CVE-2026-100305｜TDuckCloud / tduck-survey-form
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T19:16:50.973)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T19:16:50.973 / 2026-09-25T19:16:50.973
- **官方描述（原文）**：TDuck survey form through 6.0 fails to enforce form fill-in restrictions on the authenticated submission endpoint POST /user/form/data/create. Authenticated attackers who know a form's key can submit unlimited entries to any form, bypassing publish status, time window, quota, and per-IP restrictions to falsify collected results.

### 62. CVE-2025-14181｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T21:17:19.840)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T21:17:19.840 / 2026-09-25T21:17:19.840
- **官方描述（原文）**：The SOAP HTTP client guards its response buffer growth with a check that relies on signed integer overflow, which is undefined behaviour and is not guaranteed to trigger. When the check is optimised away, a malicious SOAP server can make the client allocate a buffer far smaller than the data it then writes into it, producing a heap buffer overflow.

### 63. CVE-2026-97895｜krayin / laravel-crm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T19:17:59.727)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T19:17:59.727 / 2026-09-25T19:17:59.727
- **官方描述（原文）**：A vulnerability was determined in krayin laravel-crm up to 2.2.5. This affects an unknown part of the file packages/Webkul/Admin/src/Http/Controllers/Settings/UserController.php of the component User Management. Executing a manipulation of the argument role_id can lead to improper privilege management. The attack can be executed remotely. The exploit has been publicly disclosed and may be utilized. Upgrading to version 2.2.6 is able to mitigate this issue. This patch is called 5469d70336fbb25e8e513683e82b32982ce8aa82. Upgrading the affected component is advised.

### 64. CVE-2026-97884｜mathurvishal / CloudClassroom-PHP-Project
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T18:17:35.433)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T18:17:35.433 / 2026-09-25T19:17:59.590
- **官方描述（原文）**：A vulnerability was detected in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db3fb95b66e7be. This impacts an unknown function of the file updatestudent.php of the component Student Update Functionality. The manipulation of the argument eno results in sql injection. The attack can be launched remotely. The exploit is now public and may be used. This product does not use versioning. This is why information about affected and unaffected releases are unavailable. The vendor was contacted early about this disclosure but did not respond in any way.

### 65. CVE-2026-97869｜未確認 / langchain4j
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:31.740)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.2 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:31.740 / 2026-09-25T17:17:21.300
- **官方描述（原文）**：A flaw has been found in langchain4j up to 1.5.3-beta10/1.11.10-beta18/1.18.1-beta27. This vulnerability affects the function AgenticScopeSerializer.fromJson of the file AgenticScopeJsonSerializationIT.java of the component LangChain4j-agentic. This manipulation causes deserialization. Remote exploitation of the attack is possible. The attack's complexity is rated as high. It is stated that the exploitability is difficult. The exploit has been published and may be used. Upgrading to version 1.5.3-beta11, 1.11.10-beta19 and 1.18.1-beta28 is able to resolve this issue. Upgrading the affected component is advised. The project maintainer kindly explains: "The issue was reported to us privately on 23 July 2026 and fixed in releases published on 29 July 2026. It is tracked as GHSA-gmwr-7wmf-mrjm. Exploitation requires an application to have enabled AgenticScope persistence, which is opt-in, and an attacker who can already write to that store. All maintained release lines have been patched."

### 66. CVE-2026-97868｜sheshbabu / zen
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T16:17:31.537)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T16:17:31.537 / 2026-09-25T18:17:34.527
- **官方描述（原文）**：A security vulnerability has been detected in sheshbabu zen up to 1.5.0. Affected by this issue is the function dangerouslySetInnerHTML of the file features/notes/NotesEditor.jsx of the component Note Editor. The manipulation leads to cross site scripting. The attack may be initiated remotely. The exploit has been disclosed publicly and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 67. CVE-2026-97866｜Zhonglun / CloudPOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-25T15:18:01.780)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T15:18:01.780 / 2026-09-25T16:17:31.400
- **官方描述（原文）**：A weakness has been identified in Zhonglun CloudPOS 3.0. Affected by this vulnerability is an unknown functionality of the file Program.cs of the component Automatic Update. Executing a manipulation of the argument version/url/packagekey/package name can lead to channel accessible by non-endpoint. The attack can be launched remotely. Attacks of this nature are highly complex. The exploitation appears to be difficult. The exploit has been made available to the public and could be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 68. CVE-2026-81879｜radareorg / radare2
- **Delta event**：CVSS_CHANGED (from=5.5; to=6.1)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：0.00207 / percentile=0.09607
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:02.617 / 2026-09-25T16:53:48.707
- **官方描述（原文）**：radare2 is a UNIX-like reverse engineering framework and command-line toolset. Prior to 6.2.0, radare2's ELF PN_XNUM handling was vulnerable because the ELF parser allocated the program-header array using the resolved PN_XNUM count but several consumers still iterated with the original e_phnum value of 65535. The vulnerability is triggered by processing a crafted ELF file with e_phnum = 0xffff and a much smaller resolved count in shdr[0].sh_info. Consumers iterated beyond the allocated program-header array. This can cause a heap out-of-bounds read and process termination, resulting in denial of service; memory disclosure and code execution have not been demonstrated. This issue is fixed in version 6.2.0.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-87902｜WordPress / Core
- **Title**：WordPress Core Remote File Inclusion Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.02877 / percentile=0.86275
- **CISA KEV**：listed=true / date_added=2026-09-25 / due_date=2026-09-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WordPress Core contains a remote file inclusion vulnerability which could allow an unauthenticated attacker to make page-template resolution include a chosen readable local `.php` file outside the active theme directories, leading to remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-65660｜Microsoft / SharePoint
- **Title**：Microsoft SharePoint Code Injection Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.01221 / percentile=0.6743
- **CISA KEV**：listed=true / date_added=2026-09-25 / due_date=2026-09-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft SharePoint contains a code injection vulnerability which could allow an authorized attacker to execute code over a network.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-67279｜MikroTik / RouterOS
- **Title**：Mikrotik RouterOS Improper Enforcement of Behavioral Workflow Vulnerability
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.0071 / percentile=0.51535
- **CISA KEV**：listed=true / date_added=2026-09-25 / due_date=2026-09-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Mikrotik RouterOS contains an improper enforcement of behavioral workflow vulnerability that could allow an unauthenticated client to open a session channel and send an exec request. This vulnerability can be chained to achieve unauthenticated exploitation of CVE-2026-86060.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-93616｜Check Point / Multiple Products
- **Title**：Check Point Multiple Products Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.19654 / percentile=0.97303
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Check Point Security Management Server, Multi-Domain Security Management Server, Log Server, Multi-Domain Log Server, and SmartEvent contain a path traversal vulnerability that allows an unauthenticated attacker to upload and execute arbitrary scripts.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-85706｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.91425 / percentile=0.9981
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contains a path traversal vulnerability that allows an unauthenticated user to read arbitrary files due to an improper path confinement and missing authentication enforcement in the repository commits API.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-85542｜IBM / Guardium Data Protection
- **Title**：未確認
- **Risk**：P1 / score 45；reasons：ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=active / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is affected by a command injection vulnerability in the GIM bundle import functionality. An authenticated attacker can provide a crafted GIM bundle that causes attacker-controlled arguments to be passed to the tar command, resulting in arbitrary command execution with elevated privileges on the Central Manager.
- **CISA Required Action（原文）**：未確認
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-97063 | P3 / 38 | yzcheng90 / X-SpringBoot | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-39353 | P3 / 38 | InvoicePlane / InvoicePlane | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-93834 | WATCH / 30 | Red Hat / Red Hat Enterprise Linux 10 | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88421 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-85750 | WATCH / 30 | Piwigo / Piwigo | v3.1 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-67419 | WATCH / 30 | rabbitmq / rabbitmq-server | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-67410 | WATCH / 30 | rabbitmq / rabbitmq-server | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-67409 | WATCH / 30 | rabbitmq / rabbitmq-server | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-67408 | WATCH / 30 | rabbitmq / rabbitmq-server | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-51773 | WATCH / 30 | 未確認 / 未確認 | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-44642 | WATCH / 30 | Piwigo / Piwigo | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-42324 | WATCH / 30 | Piwigo / Piwigo | v3.1 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2025-51457 | WATCH / 30 | 未確認 / 未確認 | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97064 | WATCH / 28 | yzcheng90 / X-SpringBoot | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-95832 | WATCH / 28 | Kovid Goyal / kitty | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93647 | WATCH / 28 | Zimbra / Zimbra Collaboration Suite (ZCS) | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93643 | WATCH / 28 | Zimbra / Zimbra Collaboration Suite (ZCS) | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93642 | WATCH / 28 | Zimbra / Zimbra Collaboration Suite (ZCS) | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93641 | WATCH / 28 | Zimbra / Zimbra Collaboration Suite (ZCS) | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93399 | WATCH / 28 | ladela / Online Scheduling and Appointment Booking System – Bookly | v3.1 9.1 (CRITICAL) | 0.0037 / percentile=0.28244 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92609 | WATCH / 28 | Apache Software Foundation / Apache Qpid Broker-J | v3.1 9.8 (CRITICAL) | 0.00195 / percentile=0.08173 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-92161 | WATCH / 28 | FriendsOfFlarum / oauth | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89055 | WATCH / 28 | ivole / Customer Reviews for WooCommerce | v3.1 9.1 (CRITICAL) | 0.00385 / percentile=0.29793 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-84458 | WATCH / 28 | zammad / zammad | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：3；缺少 Product：3；缺少 Title：25。
- EPSS 未確認：22；Exploitation status 未確認：3。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-26T05:42:30.974498+00:00`；Delta generated at：`2026-09-26T05:42:30.974498+00:00`。

---

## 可驗證資料來源

- **CVE-2026-87902** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87902) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87902) · [Vendor / Advisory (github.com)](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-65660** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65660) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65660) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-67279** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67279) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-67279) · [Vendor / Advisory (mikrotik.com)](https://mikrotik.com/supportsec/september-2026-vulnerability/?utm_source=chatgpt.com) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-93616** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93616) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93616) · [Vendor / Advisory (support.checkpoint.com)](https://support.checkpoint.com/results/sk/sk1000171/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85706) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85706) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85542** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85542)
- **CVE-2026-97063** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97063)
- **CVE-2026-39353** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-39353)
- **CVE-2026-93834** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93834)
- **CVE-2026-88421** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88421)
- **CVE-2026-85750** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85750)
- **CVE-2026-67419** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67419)
- **CVE-2026-67410** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67410)
- **CVE-2026-67409** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67409)
- **CVE-2026-67408** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67408)
- **CVE-2026-51773** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-51773)
- **CVE-2026-44642** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-44642)
- **CVE-2026-42324** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42324)
- **CVE-2025-51457** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-51457)
- **CVE-2026-97064** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97064)
- **CVE-2026-95832** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95832)
- **CVE-2026-93647** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93647)
- **CVE-2026-93643** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93643)
- **CVE-2026-93642** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93642)
- **CVE-2026-93641** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93641)
- **CVE-2026-93399** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93399) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93399)
- **CVE-2026-92609** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92609) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-92609)
- **CVE-2026-92161** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92161)
- **CVE-2026-89055** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89055) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89055)
- **CVE-2026-84458** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84458)
- **CVE-2026-62262** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62262)
- **CVE-2026-48482** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48482)
- **CVE-2026-42322** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42322)
- **CVE-2026-14281** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14281) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-14281)
- **CVE-2026-100551** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100551)
- **CVE-2026-100390** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100390)
- **CVE-2026-100389** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100389)
- **CVE-2026-100382** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100382)
- **CVE-2026-100075** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100075)
- **CVE-2026-97885** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97885)
- **CVE-2026-97883** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97883)
- **CVE-2026-97879** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97879)
- **CVE-2026-97878** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97878)
- **CVE-2026-97877** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97877)
- **CVE-2026-97871** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97871)
- **CVE-2026-97864** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97864)
- **CVE-2026-93682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93682)
- **CVE-2026-85293** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85293)
- **CVE-2026-85289** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85289)
- **CVE-2026-85274** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85274)
- **CVE-2026-78902** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78902)
- **CVE-2026-67421** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67421)
- **CVE-2026-67415** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67415)
- **CVE-2026-67412** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67412)
- **CVE-2026-67411** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67411)
- **CVE-2026-67242** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67242)
- **CVE-2026-67226** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67226)
- **CVE-2026-6103** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-6103)
- **CVE-2026-17545** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17545)
- **CVE-2026-100373** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100373)
- **CVE-2026-100305** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100305)
- **CVE-2025-14181** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-14181)
- **CVE-2026-97895** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97895)
- **CVE-2026-97884** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97884)
- **CVE-2026-97869** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97869)
- **CVE-2026-97868** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97868)
- **CVE-2026-97866** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97866)
- **CVE-2026-81879** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81879) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-81879)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
