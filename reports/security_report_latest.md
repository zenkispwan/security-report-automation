# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**93** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=93、NEW_KEV=1。
- Intelligence 候選：**30** 筆；P1 **1**、P2 **0**、P3 **0**、WATCH **29**。
- Baseline：state / generated_at=2026-11-06T07:30:24.056900+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-19868。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **93** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-19868｜SonicWall / SonicOS SSLVPN
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T19:17:48.437)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-06 / due_date=2026-11-20
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-06T19:17:48.437 / 2026-11-07T05:19:01.300
- **官方描述（原文）**：SonicWall SonicOS SSLVPN contains a use of single-factor authentication vulnerability that may allow a user with valid credentials for an alternate authentication method to bypass SAML authentication controls. Successful exploitation may also bypass SAML-enforced multi-factor authentication (MFA).

### 2. CVE-2026-123974｜PyTorch / TorchServe
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T20:17:20.633)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T20:17:20.633 / 2026-11-06T21:17:08.410
- **官方描述（原文）**：In all versions of PyTorch's TorchServe, a predictable extraction directory in /tmp lets a local user swap the model handler and run code as the TorchServe service account leading to local privilege escalation.

### 3. CVE-2026-123621｜webmin / usermin
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T15:17:19.730)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T15:17:19.730 / 2026-11-06T18:18:04.240
- **官方描述（原文）**：Usermin through 2.570 contains a path traversal vulnerability in mailbox/detachall.cgi that allows remote unauthenticated attackers to write files outside the temporary directory via unsanitized attachment filenames. Attackers can email attachments with ../ sequences in filenames, and when the recipient downloads all attachments, files like ~/.forward are overwritten, enabling command execution.

### 4. CVE-2026-123485｜sgoudelis / ground-station
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T15:17:17.597)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T15:17:17.597 / 2026-11-06T18:18:02.793
- **官方描述（原文）**：Ground Station from 0.6.0 before 0.8.20 does not restrict the get-orbital-sources Socket.IO handler (also exposed as get-tle-sources) to administrators, although the orbital-source write handlers are admin-only. An authenticated operator-role user can call either handler to retrieve the plaintext usernames, passwords, and tokens that administrators stored for basic and token orbital sources.

### 5. CVE-2026-119758｜Monogramm / erpnext_ocr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T18:17:58.240)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T18:17:58.240 / 2026-11-06T18:17:58.240
- **官方描述（原文）**：ERPNext OCR app for Frappe/ERPNext through 1.1.1 contains a missing authorization and path traversal vulnerability that allows any authenticated user to read arbitrary server files by passing a fully client-controlled path argument to the whitelisted read_document method. Attackers can supply local file paths to bypass Frappe's File doctype permission model and access other users' private uploads, or supply arbitrary URLs to trigger server-side requests reaching internal services and cloud metadata endpoints.

### 6. CVE-2026-112340｜wazuh / wazuh-dashboard-plugins
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T15:17:08.537)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T15:17:08.537 / 2026-11-06T20:15:23.650
- **官方描述（原文）**：Wazuh dashboard plugins from 4.9.0 before 4.14.9 contain an authorization bypass vulnerability that allows authenticated dashboard users to override the Manager API Authorization header via the /api/request proxy endpoint. Attackers can supply nested body.headers.Authorization values that replace the server-side session Bearer token, letting them act as another Manager API identity or send unauthenticated upstream requests.

### 7. CVE-2026-112338｜wazuh / wazuh
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T15:17:08.217)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T15:17:08.217 / 2026-11-06T20:15:23.650
- **官方描述（原文）**：Wazuh from 4.3.0 before 4.14.9 contains a server-side request forgery vulnerability in the GitHub module (wm_github.c) that trusts unvalidated Link rel="next" pagination URLs. Attackers controlling the next-page URL can make the manager send requests with the GitHub API token to attacker hosts, exposing organization repositories and settings.

### 8. CVE-2026-103985｜freescout-help-desk / freescout
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T17:17:10.887)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T17:17:10.887 / 2026-11-06T18:17:38.903
- **官方描述（原文）**：FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.231, the profile form exposes the only_assigned_tickets permission to its non-admin owner, and UsersController::profileSave() adds or removes User::PERM_ONLY_ASSIGNED_TICKETS without checking that the editor is an administrator. A restricted agent can uncheck the option, or submit an ordinary profile save that omits it, to remove the administrator-imposed restriction. The agent can then read and modify conversations assigned to other agents in every mailbox they already belong to. This issue is fixed in version 1.8.231.

### 9. CVE-2026-93754｜payever / payever Checkout – Composable Payment Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T03:17:08.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T03:17:08.410 / 2026-11-07T03:17:08.570
- **官方描述（原文）**：The payever – WooCommerce Gateway plugin for WordPress is vulnerable to arbitrary file upload leading to remote code execution in various versions up to, and including, 4.8.0. Three WooCommerce-API callbacks (payever_set_sandbox_api_keys, payever_toggle_subscription, payever_synchronization_incoming) are registered with no authentication, capability check, or nonce, and the upload_image() routine writes a remotely fetched file to the public uploads directory using an attacker-controlled basename() BEFORE validating the file type. This makes it possible for unauthenticated attackers to write an executable PHP file and achieve remote code execution. NOTE: the token-recovery leg of the full chain depends on the plugin's outbound validateToken() call to Payever's service; the unauthenticated hard-coded-credential identity overwrite (CWE-862/CWE-798) is independently exploitable.

### 10. CVE-2026-88800｜Unknown / MDJM Event Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T08:17:38.283)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00309 / percentile=0.23892
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T08:17:38.283 / 2026-11-06T20:09:13.780
- **官方描述（原文）**：The MDJM Event Management and Mobile Events Manager WordPress plugins through 1.7.8.7 act on a role deletion request on every page load with no capability check and no nonce, and the guard meant to protect roles that have users assigned reads a different part of the request from the one that selects what is deleted, allowing unauthenticated attackers to remove any WordPress role including administrator, which permanently strips every user of their capabilities.

### 11. CVE-2026-86044｜jupyterlab / jupyterlab-desktop
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T21:17:12.297)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T21:17:12.297 / 2026-11-06T21:17:12.297
- **官方描述（原文）**：JupyterLab Desktop is the cross-platform desktop application for JupyterLab. Prior to 4.6.2-1, JupyterLab Desktop exposed getServerInfo to the renderer without confirming that the current page still had the local Jupyter server origin. In a local managed session using JupyterLab before 4.4.8, an attacker can place a crafted MathJax link in an untrusted notebook. If a victim opens the notebook and clicks the link, the existing renderer navigates to an attacker-controlled site while retaining access to the preload bridge. The site can call getServerInfo to obtain the local server URL and authentication token, then use the Jupyter REST API to create and trust a notebook that executes arbitrary code as the victim. Users whose environment already uses JupyterLab 4.4.8 or later are unaffected because the corrected link handling breaks the first step of the chain. This vulnerability is fixed in 4.6.2-1.

### 12. CVE-2026-86005｜chartbrew / chartbrew
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T21:17:12.117)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T21:17:12.117 / 2026-11-06T21:17:12.253
- **官方描述（原文）**：Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create charts. Prior to 5.2.3, the administrative BullMQ dashboard was mounted without an authentication check. The vulnerable surface is the Bull Board/BullMQ administration dashboard at /apps/queues. A remote unauthenticated attacker reaches /apps/queues on a Chartbrew instance where Redis and BullMQ are enabled and a reverse proxy does not independently block the route. The dashboard trusted network reachability as authorization and exposed its queue-management interface directly. Redis and BullMQ must be enabled and the route must be reachable. Available actions depend on the installed Bull Board version and queue state, while confidentiality depends on job payload and log contents. An unauthenticated user can inspect exposed job payloads and logs and, when enabled by the installed version and queue state, retry or delete jobs or otherwise alter queue processing, affecting confidentiality, integrity, or availability. This issue is fixed in version 5.2.3.

### 13. CVE-2026-85295｜chartbrew / chartbrew
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T21:17:10.890)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T21:17:10.890 / 2026-11-06T21:17:11.140
- **官方描述（原文）**：Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create charts. Prior to 5.2.3, four authentication helpers accepted session tokens signed with CB_SECRET, including known, weak, or shipped-default values. The vulnerable surface is session JWT fallback in server/modules/verifyToken.js, verifyUser.js, getUserFromToken.js, and socketManager.js across the API and socket layer. A stock source or repository Docker Compose deployment retains a known, weak, or default CB_SECRET and an attacker submits a forged HS256 token decoding to a target user id. Knowing the symmetric secret lets the attacker create a token that the legacy verification fallback accepts as the target user without that user's password or two-factor authentication. The condition includes stock source and repository Docker Compose installs and any otherwise known or weak CB_SECRET; a bare container where CB_SECRET is undefined is not affected by this fallback path. A forged session impersonates the chosen user across the entire API and socket layer and exercises that user's Chartbrew privileges. This issue is fixed in version 5.2.3.

### 14. CVE-2026-71495｜open-wanderer / wanderer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T19:17:56.657)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T19:17:56.657 / 2026-11-06T19:17:56.657
- **官方描述（原文）**：Wanderer is a self-hosted trail database for saving and sharing adventures. Prior to 0.20.0, when PUBLIC_PRIVATE_INSTANCE is not set to true, the unauthenticated POST /api/v1/trail/download handler passes the attacker-controlled JSON url field directly to event.fetch() and returns the fetched response. This allows requests to internal services such as db:8090 and search:7700, cloud metadata addresses, and other network destinations, exposing returned data and permitting internal network reconnaissance or denial of service. This issue is fixed in version 0.20.0.

### 15. CVE-2026-68935｜chartbrew / chartbrew
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T22:17:59.390)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T22:17:59.390 / 2026-11-06T22:17:59.523
- **官方描述（原文）**：Chartbrew is an open-source web application for creating charts from databases and APIs. In versions 4.8.5 through 5.2.2, API connection creation and update operations accept the internal allowPrivateHost field from user input. An authenticated user with permission to manage API connections can enable this field to bypass private and reserved-network destination restrictions. An upgrade migration also enables the override on pre-existing API connections. The per-connection setting takes precedence over CB_ALLOW_PRIVATE_NETWORK_CALLS , so disabling that instance option does not protect connections with the override enabled. Successful exploitation allows requests to internal HTTP services reachable from the Chartbrew server, potentially disclosing information or triggering unauthorized actions depending on the target service. Recognized cloud metadata endpoints remain separately blocked. This issue is fixed in version 5.2.3.

### 16. CVE-2026-63439｜Bubka / 2FAuth
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T21:17:09.970)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T21:17:09.970 / 2026-11-06T21:17:09.970
- **官方描述（原文）**：2FAuth is a web app to manage Two-Factor Authentication (2FA) accounts and generate their security codes. Prior to 8.0.0, when AUTHENTICATION_GUARD=reverse-proxy-guard is enabled, ReverseProxyGuard::user() reads the default REMOTE_USER identity header, or a custom identity header selected by the AUTH_PROXY_HEADER_FOR_USER configuration setting, without confirming that the request originated from a configured trusted proxy. A remote client that can reach the application directly can forge the selected identity header and authenticate as an existing user, including an administrator, gaining access to stored 2FA secrets and account or application management functions. This issue is fixed in version 8.0.0.

### 17. CVE-2026-63438｜Bubka / 2FAuth
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T21:17:09.770)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T21:17:09.770 / 2026-11-06T21:17:09.770
- **官方描述（原文）**：2FAuth is a web app to manage Two-Factor Authentication (2FA) accounts and generate their security codes. Prior to 8.0.0, when AUTHENTICATION_GUARD=reverse-proxy-guard accepts authentication headers from a client that did not pass through a trusted proxy, RemoteUserProvider::retrieveById() creates an account for an unknown REMOTE_USER, promotes the first created account to administrator, and synchronizes the account email from the configured mail header. An unauthenticated remote client can therefore create an administrator on a fresh instance or impersonate and redirect email for a known account, exposing 2FA secrets and administrative functions. This issue is fixed in version 8.0.0.

### 18. CVE-2026-59105｜Jumis Pro SIA / Jumis
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T15:17:22.270)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T15:17:22.270 / 2026-11-06T16:18:57.353
- **官方描述（原文）**：Jumis (formerly Tildes Jumis) creates and uses a Microsoft SQL Server login named ##Tilde_JumisAdmin## whose password is derived deterministically from a single non-secret input - the SQL Server name (@@servername). The derivation algorithm is hard-coded in the client application and is identical across every installation; it contains a hard-coded secret key for entropy. Because the only input (the server name) is not secret - the instance suffix is hard-coded and the host name is discoverable via the SQL Server Browser service (UDP 1434), the TDS pre-login response, or DNS/NetBIOS - any party able to reach a Jumis SQL Server can compute the password offline and authenticate. The ##Tilde_JumisAdmin## login is a member of the sysadmin server role. Successful authentication therefore grants full administrative control of the SQL Server instance and read/write access to every customer's accounting database hosted on it. The on-premise server installation also programmatically enables xp_cmdshell during routine operation, so sysadmin access escalates to operating-system command execution on the database server.

### 19. CVE-2026-59104｜SPH Engineering / UgCS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T22:17:59.043)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T22:17:59.043 / 2026-11-06T22:17:59.043
- **官方描述（原文）**：UgCS server before 6.2 contains an authentication bypass in the HCI protocol login handler (LoginHandler) exposed on TCP port 3334. When the user database contains exactly one user (the default single-operator installation), a LoginRequest with empty userLogin and userPassword fields is interpreted as \"use the only user\" rather than as invalid credentials, and the server returns a fully authenticated session. Because the service listens on all interfaces (0.0.0.0) without TLS by default, an unauthenticated remote attacker with network access to port 3334 can obtain an authenticated session without knowing any credential and then issue privileged commands, including commanding connected drones and uploading flight routes.

### 20. CVE-2026-58490｜TracecatHQ / tracecat
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T20:17:23.253)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T20:17:23.253 / 2026-11-06T20:17:23.253
- **官方描述（原文）**：Tracecat is an open-source security automation platform for teams and AI agents. From version 0.37.0 until 1.0.0-beta.49, Docker Compose deployments with SAML enabled can render SAML_SIGNED_ASSERTIONS and SAML_SIGNED_RESPONSES as empty values, overriding secure application defaults and disabling both signature requirements. An unauthenticated attacker who can reach the SAML assertion consumer endpoint can submit a forged unsigned response for an existing Tracecat user email address and obtain that user’s session. Targeting an existing superadmin can result in superadmin account takeover. Exploitation does not create users when SAML user creation is disabled and does not affect default Fargate or Helm deployments. Version 1.0.0-beta.49 removes the insecure deployment pass-through and requires signed assertions and responses.

### 21. CVE-2026-54349｜chartbrew / chartbrew
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T21:17:08.947)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T21:17:08.947 / 2026-11-06T21:17:09.090
- **官方描述（原文）**：Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create charts. Prior to 5.2.1, SQL dashboard-variable substitution used attacker-controlled JavaScript replacement strings unsafely across SQL connectors and separately failed to escape backslashes for MySQL and MariaDB quoted contexts. The vulnerable surface is public and embedded dashboard/chart requests that call applyMysqlOrPostgresVariables. An unauthenticated user sends crafted URL filter values to a public or embedded chart backed by a stored SQL query. Replacement-string dollar sequences can alter SQL independently of the database engine, while MySQL and MariaDB backslash handling provides a second quoted-string escape path. The target must expose a public or embedded chart using URL-controlled variables in a SQL query; only the backslash branch is specific to MySQL and MariaDB. Injected SQL can read, modify, or delete data available to the configured database account. This issue is fixed in version 5.2.1.

### 22. CVE-2026-19803｜printcart / Printcart Store – Web to Print Product Designer for WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T04:17:29.233)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T04:17:29.233 / 2026-11-07T04:17:29.377
- **官方描述（原文）**：The Printcart Store – Web to Print Product Designer for WooCommerce plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 2.13.2. This is due to the `nbu_crop_image` AJAX handler accepting a user-supplied `url` parameter that `Nbdesigner_IO::convert_url_to_path()` concatenates onto the uploads base directory without normalizing or stripping `../` sequences, and then deriving both the output directory and output file extension via `pathinfo()` from the same attacker-controlled path — with no `stripImage()` call before `writeImage()` is invoked. This makes it possible for unauthenticated attackers to write attacker-controlled PHP content to arbitrary locations outside the uploads directory, resulting in remote code execution when the written file is subsequently requested. This vulnerability is only exploitable when the `nbdesigner_upload_popup_style` site option is set to `a` (Advanced Upload Popup), which causes the handler to be registered for unauthenticated requests; however, the required `save-design` nonce is printed on the fully public frontend `upload-design-file` page, making it trivially obtainable by any anonymous visitor once that configuration is active.

### 23. CVE-2026-18838｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:59.803)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:59.803 / 2026-11-07T05:18:59.920
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information and modify API configurations due to improper authentication. Identity information supplied in requests is not sufficiently verified, which could allow a caller to impersonate another user.

### 24. CVE-2026-18836｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:59.597)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:59.597 / 2026-11-07T05:18:59.760
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information due to server-side request forgery. The affected component can be made to send requests to unintended destinations and return the response to the attacker.

### 25. CVE-2026-18535｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:59.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:59.120 / 2026-11-07T05:18:59.300
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 are vulnerable to a Regular Expression Denial of Service (ReDoS) attack and to improper neutralisation of wildcard query operators.

### 26. CVE-2026-17410｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:58.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:58.410 / 2026-11-07T05:18:58.590
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to access and modify other tenants' portal data due to improper neutralization of argument delimiters.

### 27. CVE-2026-17409｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:58.157)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:58.157 / 2026-11-07T05:18:58.353
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to execute unauthorized administrative operations and obtain sensitive information due to improper handling of case sensitivity. Access controls are not applied consistently to all variations of a request, which could allow restricted operations to be reached.

### 28. CVE-2026-17408｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:57.917)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:57.917 / 2026-11-07T05:18:58.107
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to execute arbitrary code due to improper neutralization of special elements in an OS command.

### 29. CVE-2026-17403｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:56.690)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:56.690 / 2026-11-07T05:18:56.870
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to gain full administrative control due to the use of hard-coded credentials.

### 30. CVE-2026-17402｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:56.460)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:56.460 / 2026-11-07T05:18:56.630
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary commands due to OS command injection. User-supplied input is not properly neutralized before it is passed to the operating system, which could allow commands to run on the underlying host.

### 31. CVE-2026-17399｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:55.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:55.790 / 2026-11-07T05:18:55.963
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary code due to insufficient validation of uploaded content. Content uploaded to the product is not sufficiently checked before it is processed, which could allow code to run on the server.

### 32. CVE-2026-17396｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:55.103)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:55.103 / 2026-11-07T05:18:55.280
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information due to SQL injection.

### 33. CVE-2026-17394｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:54.617)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:54.617 / 2026-11-07T05:18:54.807
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information due to improperly controlled modification of object attributes. A user-supplied value could change an access-related setting that should be controlled by the system, which could expose sensitive information.

### 34. CVE-2026-17392｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:54.113)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:54.113 / 2026-11-07T05:18:54.270
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to gain unauthorized administrative access to other tenants due to LDAP injection. User-supplied input is not properly neutralized in directory queries, which could change the query and grant access beyond the user's own tenant.

### 35. CVE-2026-17362｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T04:17:29.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T04:17:29.070 / 2026-11-07T05:18:48.580
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to create, modify, or delete tenants due to missing authorization.

### 36. CVE-2026-17360｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:48.197)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:48.197 / 2026-11-07T05:18:48.347
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to gain full administrative control due to the use of hard-coded credentials.

### 37. CVE-2026-17359｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:48.017)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:48.017 / 2026-11-07T05:18:48.157
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary code due to improper control of generation of code. A user-supplied value can influence code that the product generates, which could lead to code execution.

### 38. CVE-2026-17354｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:47.057)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:47.057 / 2026-11-07T05:18:47.207
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to perform arbitrary file writes due to path traversal.

### 39. CVE-2026-17353｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:46.880)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:46.880 / 2026-11-07T05:18:47.017
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information and bypass security restrictions due to server-side request forgery.

### 40. CVE-2026-17344｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:46.317)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:46.317 / 2026-11-07T05:18:46.463
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information due to server-side request forgery. A service that can be reached without authentication could be made to send requests to unintended destinations.

### 41. CVE-2026-17342｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:45.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:45.943 / 2026-11-07T05:18:46.087
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary code due to improper control of generation of code.

### 42. CVE-2026-17340｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:45.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:45.510 / 2026-11-07T05:18:45.690
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to execute arbitrary code due to a path traversal vulnerability.

### 43. CVE-2026-17339｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:45.287)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:45.287 / 2026-11-07T05:18:45.447
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to access or delete resources belonging to other tenants due to path traversal.

### 44. CVE-2026-17338｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:45.083)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:45.083 / 2026-11-07T05:18:45.237
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information due to broken object-level authorization.

### 45. CVE-2026-17336｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:44.673)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:44.673 / 2026-11-07T05:18:44.837
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary SQL commands due to improper neutralization of special elements used in an SQL command.

### 46. CVE-2026-17329｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:43.273)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:43.273 / 2026-11-07T05:18:43.413
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information due to improper validation of endpoint URLs.

### 47. CVE-2026-17313｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:40.163)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:40.163 / 2026-11-07T05:18:40.313
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information and take control of gateway configuration due to authentication bypass via an alternate path.

### 48. CVE-2026-17301｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:37.913)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:37.913 / 2026-11-07T05:18:38.057
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow an unauthenticated attacker to bypass authentication due to improper verification of a cryptographic signature.

### 49. CVE-2026-17299｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:37.700)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:37.700 / 2026-11-07T05:18:37.863
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to perform arbitrary file reads and server-side request forgery due to unrestricted resolution of external references. Externally referenced content in submitted definitions is not sufficiently restricted when processed, and the retrieved content could be returned to the attacker.

### 50. CVE-2026-17298｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:37.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:37.510 / 2026-11-07T05:18:37.647
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information due to server-side request forgery.

### 51. CVE-2026-17297｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:37.333)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:37.333 / 2026-11-07T05:18:37.470
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to perform an account takeover due to an open redirect vulnerability. The redirect address used during sign-in is not sufficiently validated, which could allow authentication results to be sent to an attacker-controlled location.

### 52. CVE-2026-17296｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:37.140)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:37.140 / 2026-11-07T05:18:37.290
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information due to server-side request forgery.

### 53. CVE-2026-17292｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:36.330)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:36.330 / 2026-11-07T05:18:36.513
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to take over ownership of other organizations due to broken object-level authorization. Access checks on organization objects are incomplete, which could allow ownership of organizations the user does not control to be changed.

### 54. CVE-2026-17278｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:33.440)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:33.440 / 2026-11-07T05:18:33.587
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to gain unauthorized access to sensitive API catalog and runtime configuration data due to improper authentication. Information supplied by the client is not sufficiently verified, which could allow a caller to appear as a trusted party.

### 55. CVE-2026-17239｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:32.657)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:32.657 / 2026-11-07T05:18:32.803
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary code due to a path traversal vulnerability.

### 56. CVE-2026-17158｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:28.853)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:28.853 / 2026-11-07T05:18:29.003
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to gain elevated privileges due to improper authentication.

### 57. CVE-2026-17150｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:28.230)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:28.230 / 2026-11-07T05:18:28.390
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary code and access sensitive information from other tenants due to insufficient input validation. Uploaded custom module content is not sufficiently validated before it is processed, which could allow code to run with access beyond the user's own tenant.

### 58. CVE-2026-17147｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:28.037)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:28.037 / 2026-11-07T05:18:28.187
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary code and perform unauthorized administrative actions due to a path traversal vulnerability.

### 59. CVE-2026-17146｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:27.843)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:27.843 / 2026-11-07T05:18:27.993
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary JavaScript and obtain sensitive information due to improper input validation.

### 60. CVE-2026-17134｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:26.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:26.630 / 2026-11-07T05:18:26.787
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary SQL commands due to SQL injection.

### 61. CVE-2026-17132｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:26.430)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:26.430 / 2026-11-07T05:18:26.583
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary SQL commands due to improper neutralization of special elements used in an SQL command.

### 62. CVE-2026-17131｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:26.230)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:26.230 / 2026-11-07T05:18:26.387
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information due to server-side request forgery. Restrictions on outbound requests can be bypassed, so the server could be made to contact unintended destinations and return the response.

### 63. CVE-2026-17117｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:25.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:25.647 / 2026-11-07T05:18:25.787
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary code due to improperly controlled modification of object attributes. A user could set a field that should only be controlled by the system, which could lead to code execution.

### 64. CVE-2026-17066｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:23.787)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:23.787 / 2026-11-07T05:18:23.917
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information and modify or delete data belonging to other tenants due to missing authorization.

### 65. CVE-2026-17049｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:23.173)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:23.173 / 2026-11-07T05:18:23.310
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information and modify arbitrary documents due to authorization bypass through user-controlled keys.

### 66. CVE-2026-16920｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:22.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:22.990 / 2026-11-07T05:18:23.130
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to bypass security restrictions due to a confused deputy vulnerability.

### 67. CVE-2026-16918｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:22.803)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:22.803 / 2026-11-07T05:18:22.943
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to access internal network resources due to server-side request forgery.

### 68. CVE-2026-16884｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:22.440)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:22.440 / 2026-11-07T05:18:22.587
- **官方描述（原文）**：IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information due to an XML external entity (XXE) injection.

### 69. CVE-2026-16720｜IBM / API Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T05:18:21.883)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T05:18:21.883 / 2026-11-07T05:18:22.027
- **官方描述（原文）**：IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain valid access tokens for other users due to improper authentication. Authentication against a connected directory service is not sufficiently enforced, which could allow another user's identity to be assumed.

### 70. CVE-2026-124040｜civetweb / civetweb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T20:17:22.203)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T20:17:22.203 / 2026-11-06T20:17:22.347
- **官方描述（原文）**：CivetWeb through 1.16, when built with USE_HTTP2 and enable_http2 on, contains a use-after-free vulnerability in handle_http2() that retains freed :method and :path pointers. Unauthenticated remote attackers can send a later HEADERS frame omitting these pseudo-headers to influence request method or path seen by access rules, or crash the server.

### 71. CVE-2026-123832｜JetBrains / CLion
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T17:17:21.387)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T17:17:21.387 / 2026-11-07T05:18:16.857
- **官方描述（原文）**：In JetBrains CLion before 2026.2 code execution was possible in Safe Mode via JSON compilation database

### 72. CVE-2026-123831｜JetBrains / CLion
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T17:17:21.240)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T17:17:21.240 / 2026-11-07T05:18:15.857
- **官方描述（原文）**：In JetBrains CLion before 2026.2, 2026.1.4 code execution was possible in Safe Mode via Meson project settings

### 73. CVE-2026-123488｜craftcms / cms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T15:17:18.133)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T15:17:18.133 / 2026-11-06T20:15:23.650
- **官方描述（原文）**：Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains an unauthenticated SQL injection vulnerability in the element search endpoint because the attribute parameter is concatenated into the query unsanitized and emulated PDO prepares allow stacked statements. Remote attackers can read and write the database, setting the admin flag or overwriting password hashes in the users table to gain administrator access.

### 74. CVE-2026-123294｜JetBrains / Hub
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T11:17:08.140)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T11:17:08.140 / 2026-11-07T05:18:12.623
- **官方描述（原文）**：In JetBrains Hub before 2026.2.52556 privilege escalation was possible by changing email authentication details during the verification flow

### 75. CVE-2026-123279｜JetBrains / Datalore
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T11:17:06.140)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T11:17:06.140 / 2026-11-06T21:29:48.800
- **官方描述（原文）**：In JetBrains Datalore before 2026.4 code execution was possible in a notebook's computation by view-only collaborators

### 76. CVE-2026-123218｜IBM / Aspera Faspex
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T04:17:28.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T04:17:28.900 / 2026-11-07T04:17:29.027
- **官方描述（原文）**：IBM Aspera Faspex 5.0.0 through 5.0.19 could allow an authorized user to craft a specific message to bypass user authorization and gain full administrative privileges.

### 77. CVE-2026-122193｜AWS / trusted-remote-execution
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T17:17:20.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T17:17:20.313 / 2026-11-06T21:17:07.030
- **官方描述（原文）**：OS command injection in the example SSM document provisioning script in Trusted Remote Execution (REX) before 2026-07-28 might allow an authenticated remote user who is permitted to invoke the Rex-RO or Rex-RW SSM document to execute arbitrary commands as root on the managed instance, bypassing Cedar policy enforcement. To remediate this issue, users should delete any Rex-RO and Rex-RW SSM documents created from the example script, in each account and Region where it was run.

### 78. CVE-2026-120844｜miniOrange / OAuth Single Sign On – SSO (OAuth Client)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T08:17:19.657)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00331 / percentile=0.26367
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T08:17:19.657 / 2026-11-06T18:17:59.930
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in miniOrange OAuth Single Sign On – SSO (OAuth Client) miniorange-login-with-eve-online-google-facebook allows Privilege Escalation.This issue affects OAuth Single Sign On – SSO (OAuth Client): from n/a through 7.1.3.

### 79. CVE-2026-119923｜AWS / babelfish-for-postgresql
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T19:17:39.360)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T19:17:39.360 / 2026-11-06T21:17:06.347
- **官方描述（原文）**：A heap-based buffer overflow in the TDS prelogin parser in the Babelfish for PostgreSQL extension versions 1.0-1.5, 2.1-2.15, 3.1-3.12, 4.0-4.8, 5.1-5.4 and in Amazon Aurora PostgreSQL with Babelfish might allow remote attackers to execute arbitrary OS commands as the database process user via a specially crafted malformed TDS prelogin packet to the TDS port. This record consolidates a related NULL-pointer-dereference finding in the same prelogin parser. To remediate this issue, we recommend users upgrade to Babelfish for PostgreSQL extension versions 4.10, 5.6, 6.1 or later. As a workaround, restrict network access to the TDS port (default 1433). Customers using Amazon Aurora PostgreSQL with Babelfish should upgrade their cluster to Aurora PostgreSQL 13.9.16 (1.5.5), 13.23.3 (1.17.2), 14.6.16 (2.3.5), 14.17.8 (2.12.4), 14.18.6 (2.13.3), 14.19.5 (2.14.2), 14.20.5 (2.15.2), 14.22.3 (2.16.1), 14.23.1 (2.17.0), 15.10.8 (3.8.4), 15.12.8 (3.9.4), 15.13.6 (3.10.3), 15.14.5 (3.11.2), 15.15.5 (3.12.2), 15.17.3 (3.13.1), 15.18.1 (3.14.0), 16.8.8 (4.5.5), 16.9.6 (4.6.3), 16.10.5 (4.7.2), 16.11.5 (4.8.2), 16.13.3 (4.9.1), 16.14.1 (4.10.0), 17.4.8 (5.1.4), 17.5.6 (5.2.3), 17.6.5 (5.3.2), 17.7.5 (5.4.2), 17.9.3 (5.5.1), 17.10.1 (5.6.0), 18.3.4 (6.0.2), 18.4.1 (6.1.0) or later, and apply any pending maintenance to ensure they are on the latest patch.

### 80. CVE-2026-119516｜Mamunur Rashid / Radius Booking — Booking Calendar for Appointments &amp; Services
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T08:17:19.227)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00386 / percentile=0.32903
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T08:17:19.227 / 2026-11-06T08:17:19.353
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Mamunur Rashid Radius Booking — Booking Calendar for Appointments &amp; Services radius-booking allows Object Injection.This issue affects Radius Booking — Booking Calendar for Appointments &amp; Services: from n/a through 1.0.20.

### 81. CVE-2026-118423｜Unknown / WP Libre Form
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T08:17:18.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00569 / percentile=0.47318
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T08:17:18.550 / 2026-11-06T20:09:13.780
- **官方描述（原文）**：The WP Libre Form WordPress plugin 1.5.0.1 does not validate the type of files uploaded through its form submissions, allowing unauthenticated attackers to upload PHP files to a web-accessible location and execute them, leading to remote code execution.

### 82. CVE-2026-114630｜elextensions / ELEX WordPress HelpDesk & Customer Ticketing System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T12:17:16.503)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T12:17:16.503 / 2026-11-06T18:17:55.283
- **官方描述（原文）**：The ELEX WordPress HelpDesk & Customer Ticketing System plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient file path validation in the factory_reset function in all versions up to, and including, 3.3.8 This makes it possible for unauthenticated attackers to delete arbitrary files on the server, which can easily lead to remote code execution when the right file is deleted (such as wp-config.php). This vulnerability is exploitable via a two-step chain: an unauthenticated attacker first stores an arbitrary ticket_attachment_path value by submitting a ticket through the nopriv eh_crm_new_ticket_post AJAX endpoint (whose nonce is publicly exposed via the [wsdesk_support] shortcode), then triggers the factory_reset routine via a GET request to wp-admin/admin.php?page=wsdesk_factory_reset, which is guarded only by is_admin() — a request-type check — rather than a capability check, causing unlink() to be called on the attacker-supplied path.

### 83. CVE-2026-109469｜Microsoft / Entra Device Registration
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T23:17:20.557)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T23:17:20.557 / 2026-11-06T23:17:20.707
- **官方描述（原文）**：Authorization bypass through user-controlled key in Entra Device Registration allows an unauthorized attacker to elevate privileges over a network.

### 84. CVE-2026-107622｜themekraft / BuddyForms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T12:17:16.020)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T12:17:16.020 / 2026-11-06T16:17:36.057
- **官方描述（原文）**：The BuddyForms plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 2.10.5 via a form-type confusion attack through the `bf_post_type` parameter. This is due to the public frontend submission handler `buddyforms_form_response_no_ajax()` authorizing logged-out submissions based solely on the target form's `public_submit` flag while independently trusting the attacker-supplied `$_POST['bf_post_type']` to determine the post type of the newly created object — a cross-check introduced in 2.10.2 applies only to existing posts (`post_id != 0`) and is completely bypassed for new-object creation — combined with the `save_post` listener `buddyforms_edit_form_save_meta_box_data()` lacking both a `current_user_can()` capability check and a form-builder nonce, causing it to unconditionally persist attacker-supplied `$_POST['buddyforms_options']` for any newly inserted `buddyforms` CPT post. This makes it possible for unauthenticated attackers to insert a rogue BuddyForms form configuration with an attacker-controlled `new_user_role` value into the live global form registry, then submit a registration through that form to create a new WordPress account with administrator-level privileges and achieve full site takeover. Exploitation requires the WordPress site to have "Anyone can register" enabled and at least one public BuddyForms form attached to a page, both of which are standard BuddyForms deployment configurations.

### 85. CVE-2026-102530｜jupyterlab / jupyterlab-desktop
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T21:17:05.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T21:17:05.510 / 2026-11-06T21:17:05.510
- **官方描述（原文）**：JupyterLab Desktop is the cross-platform desktop application for JupyterLab. Prior to 4.6.2-1, remote-server URLs were inserted into the server-selection dialog and Welcome view without safe encoding. An attacker who convinces a user to submit a crafted URL can execute JavaScript in the Welcome renderer and abuse its privileged IPC bridge to execute arbitrary code with the user’s privileges. The Welcome view also unsafely renders RSS news-feed titles; exploitation through this separate input path requires control over content delivered through the application’s Jupyter Blog feed or its cached feed data, rather than submission of a remote-server URL. This issue affects all supported platforms and is fixed in version 4.6.2-1.

### 86. CVE-2026-62855｜freescout-help-desk / freescout
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T17:18:33.877)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T17:18:33.877 / 2026-11-06T18:18:17.450
- **官方描述（原文）**：FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.225, the administrator-only App Logs viewer accepts Laravel-encrypted folder and file parameters whose constructed path is checked only as a raw string. An administrator who also knows the APP_KEY can supply traversal segments that the filesystem normalizes outside storage/logs. The /app-logs/app route can then read local files accessible to the PHP worker, including environment files, source files, credentials, tokens, and operating-system files. This issue is fixed in version 1.8.225.

### 87. CVE-2026-123675｜OpenBMB / Internet of Agents
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T16:17:54.737)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T16:17:54.737 / 2026-11-06T18:18:04.420
- **官方描述（原文）**：A flaw has been found in OpenBMB Internet of Agents up to 9d78e88e47160eb42ee1ee8538c05e1c2c47877a. This affects the function execute_code of the file im_client/agents/tools/code_executor.py of the component Code Executor Tool. This manipulation of the argument filename/lang causes code injection. The attack can be initiated remotely. The exploit has been published and may be used. Continious delivery with rolling releases is used by this product. Therefore, no version details of affected nor updated releases are available. The project was informed of the problem early through an issue report but has not responded yet.

### 88. CVE-2026-123624｜zhimaAi / chatwiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T15:17:20.070)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T15:17:20.070 / 2026-11-06T17:17:20.780
- **官方描述（原文）**：ChatWiki before 2.10.0 contains an insecure direct object reference vulnerability that allows authenticated users to modify other tenants' fast commands by supplying arbitrary sequential ids to POST /manage/saveFastCommand. Attackers can overwrite another tenant's command title, type, content and robot binding, redirecting webpage-jump commands to attacker URLs and reassigning the record to their own tenant.

### 89. CVE-2026-123619｜lektor / lektor
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T15:17:19.363)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T15:17:19.363 / 2026-11-06T17:17:20.627
- **官方描述（原文）**：Lektor through 3.3.14 and 3.4.0b15 contains an absolute path traversal vulnerability in the admin API on Windows that allows attackers to escape the project directory by supplying drive-letter paths that cleanup_path does not normalise. Attackers can use a malicious web page with cross-site requests or DNS rebinding against the unauthenticated local server to recursively delete directories via deleterecord or write attacker-controlled files via newattachment.

### 90. CVE-2026-123617｜openwhyd / openwhyd
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T15:17:19.017)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T15:17:19.017 / 2026-11-06T18:18:04.030
- **官方描述（原文）**：Openwhyd before 1.65.1 contains a NoSQL injection vulnerability that allows unauthenticated attackers to manipulate user lookups by passing JSON objects in the id parameter. Attackers can send MongoDB query operators such as $ne or $gt to POST /api/user to select and enumerate other users' public profile records.

### 91. CVE-2026-112334｜wazuh / wazuh
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T15:17:07.553)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T15:17:07.553 / 2026-11-06T20:15:23.650
- **官方描述（原文）**：Wazuh from 1.0.0 before 4.14.9 contains an out-of-bounds write vulnerability in wazuh-execd that allows privileged manager-configuration attackers to corrupt root process memory via excess ar.conf entries. Attackers controlling ossec.conf active-response blocks can push over 64 commands to agents, overflowing ReadExecConfig() arrays and crashing Active Response fleet-wide.

### 92. CVE-2026-103984｜freescout-help-desk / freescout
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T17:17:10.710)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T17:17:10.710 / 2026-11-06T18:17:38.747
- **官方描述（原文）**：FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.231, when limit_user_customer_visibility is enabled, the load_customer_info AJAX action performs a global lookup using an attacker-controlled customer email and checks only whether the agent can access a separately supplied mailbox. A non-admin agent can name an accessible mailbox and retrieve an unrelated customer's rendered profile without invoking CustomerPolicy::view(). The response can expose names, email addresses, phone numbers, company and job information, postal addresses, social profiles, websites, and confidential internal agent notes. This issue is fixed in version 1.8.231.

### 93. CVE-2026-123677｜xxyopen / novel
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T16:17:55.247)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T16:17:55.247 / 2026-11-06T17:17:20.937
- **官方描述（原文）**：A vulnerability was found in xxyopen/201206030 novel up to 3.5.0. Affected is the function getBookChapter of the file src/main/java/io/github/xxyopen/novel/service/impl/BookServiceImpl.java of the component Book Chapter Read Handler. Performing a manipulation of the argument chapterId results in authorization bypass. The attack may be initiated remotely. The exploit has been made public and could be used. The patch is named b8134e774820e0971fa9d8074405b49a01c99bdc. It is suggested to install a patch to address this issue.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-19868｜SonicWall / SonicOS SSLVPN
- **Title**：SonicWall SonicOS SSLVPN Use of Single-factor Authentication Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-06 / due_date=2026-11-20
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：SonicWall SonicOS SSLVPN contains a use of single-factor authentication vulnerability that may allow a user with valid credentials for an alternate authentication method to bypass SAML authentication controls. Successful exploitation may also bypass SAML-enforced multi-factor authentication (MFA).
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-123974 | WATCH / 30 | PyTorch / TorchServe | v3.1 7.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-123621 | WATCH / 30 | webmin / usermin | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-123485 | WATCH / 30 | sgoudelis / ground-station | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-119758 | WATCH / 30 | Monogramm / erpnext_ocr | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112340 | WATCH / 30 | wazuh / wazuh-dashboard-plugins | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112338 | WATCH / 30 | wazuh / wazuh | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-103985 | WATCH / 30 | freescout-help-desk / freescout | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93754 | WATCH / 28 | payever / payever Checkout – Composable Payment Gateway | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-88800 | WATCH / 28 | Unknown / MDJM Event Management | v3.1 9.1 (CRITICAL) | 0.00309 / percentile=0.23892 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-86044 | WATCH / 28 | jupyterlab / jupyterlab-desktop | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-86005 | WATCH / 28 | chartbrew / chartbrew | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-85295 | WATCH / 28 | chartbrew / chartbrew | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-71495 | WATCH / 28 | open-wanderer / wanderer | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-68935 | WATCH / 28 | chartbrew / chartbrew | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-63439 | WATCH / 28 | Bubka / 2FAuth | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-63438 | WATCH / 28 | Bubka / 2FAuth | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-59105 | WATCH / 28 | Jumis Pro SIA / Jumis | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-59104 | WATCH / 28 | SPH Engineering / UgCS | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-58490 | WATCH / 28 | TracecatHQ / tracecat | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-54349 | WATCH / 28 | chartbrew / chartbrew | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-19803 | WATCH / 28 | printcart / Printcart Store – Web to Print Product Designer for WooCommerce | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-18838 | WATCH / 28 | IBM / API Connect | v3.1 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-18836 | WATCH / 28 | IBM / API Connect | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-18535 | WATCH / 28 | IBM / API Connect | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-17410 | WATCH / 28 | IBM / API Connect | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-17409 | WATCH / 28 | IBM / API Connect | v3.1 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-17408 | WATCH / 28 | IBM / API Connect | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-17403 | WATCH / 28 | IBM / API Connect | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-17402 | WATCH / 28 | IBM / API Connect | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：29。
- EPSS 未確認：29；Exploitation status 未確認：20。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-07T06:43:17.189212+00:00`；Delta generated at：`2026-11-07T06:43:17.189212+00:00`。

---

## 可驗證資料來源

- **CVE-2026-19868** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19868) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (psirt.global.sonicwall.com)](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-123974** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123974)
- **CVE-2026-123621** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123621)
- **CVE-2026-123485** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123485)
- **CVE-2026-119758** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119758)
- **CVE-2026-112340** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112340)
- **CVE-2026-112338** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112338)
- **CVE-2026-103985** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103985)
- **CVE-2026-93754** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93754)
- **CVE-2026-88800** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88800) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88800)
- **CVE-2026-86044** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86044)
- **CVE-2026-86005** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86005)
- **CVE-2026-85295** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85295)
- **CVE-2026-71495** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71495)
- **CVE-2026-68935** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-68935)
- **CVE-2026-63439** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63439)
- **CVE-2026-63438** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63438)
- **CVE-2026-59105** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59105)
- **CVE-2026-59104** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59104)
- **CVE-2026-58490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58490)
- **CVE-2026-54349** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54349)
- **CVE-2026-19803** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19803)
- **CVE-2026-18838** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18838)
- **CVE-2026-18836** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18836)
- **CVE-2026-18535** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18535)
- **CVE-2026-17410** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17410)
- **CVE-2026-17409** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17409)
- **CVE-2026-17408** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17408)
- **CVE-2026-17403** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17403)
- **CVE-2026-17402** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17402)
- **CVE-2026-17399** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17399)
- **CVE-2026-17396** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17396)
- **CVE-2026-17394** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17394)
- **CVE-2026-17392** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17392)
- **CVE-2026-17362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17362)
- **CVE-2026-17360** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17360)
- **CVE-2026-17359** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17359)
- **CVE-2026-17354** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17354)
- **CVE-2026-17353** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17353)
- **CVE-2026-17344** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17344)
- **CVE-2026-17342** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17342)
- **CVE-2026-17340** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17340)
- **CVE-2026-17339** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17339)
- **CVE-2026-17338** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17338)
- **CVE-2026-17336** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17336)
- **CVE-2026-17329** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17329)
- **CVE-2026-17313** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17313)
- **CVE-2026-17301** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17301)
- **CVE-2026-17299** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17299)
- **CVE-2026-17298** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17298)
- **CVE-2026-17297** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17297)
- **CVE-2026-17296** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17296)
- **CVE-2026-17292** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17292)
- **CVE-2026-17278** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17278)
- **CVE-2026-17239** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17239)
- **CVE-2026-17158** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17158)
- **CVE-2026-17150** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17150)
- **CVE-2026-17147** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17147)
- **CVE-2026-17146** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17146)
- **CVE-2026-17134** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17134)
- **CVE-2026-17132** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17132)
- **CVE-2026-17131** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17131)
- **CVE-2026-17117** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17117)
- **CVE-2026-17066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17066)
- **CVE-2026-17049** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17049)
- **CVE-2026-16920** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16920)
- **CVE-2026-16918** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16918)
- **CVE-2026-16884** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16884)
- **CVE-2026-16720** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16720)
- **CVE-2026-124040** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124040)
- **CVE-2026-123832** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123832)
- **CVE-2026-123831** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123831)
- **CVE-2026-123488** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123488)
- **CVE-2026-123294** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123294)
- **CVE-2026-123279** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123279)
- **CVE-2026-123218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123218)
- **CVE-2026-122193** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122193)
- **CVE-2026-120844** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120844) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-120844)
- **CVE-2026-119923** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119923)
- **CVE-2026-119516** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119516) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-119516)
- **CVE-2026-118423** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118423) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-118423)
- **CVE-2026-114630** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114630)
- **CVE-2026-109469** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109469)
- **CVE-2026-107622** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107622)
- **CVE-2026-102530** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102530)
- **CVE-2026-62855** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62855)
- **CVE-2026-123675** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123675)
- **CVE-2026-123624** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123624)
- **CVE-2026-123619** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123619)
- **CVE-2026-123617** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123617)
- **CVE-2026-112334** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112334)
- **CVE-2026-103984** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103984)
- **CVE-2026-123677** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123677)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
