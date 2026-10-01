# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**82** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=1、EXPLOITATION_CHANGED=1、NEW_CVE=80、NEW_KEV=1。
- Intelligence 候選：**30** 筆；P1 **1**、P2 **0**、P3 **6**、WATCH **23**。
- Baseline：state / generated_at=2026-09-30T06:11:13.755032+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-76504。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **82** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-76504｜Cisco / Catalyst SD-WAN Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:20.247)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-30 / due_date=2026-10-03
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-30T13:17:20.247 / 2026-10-01T04:18:19.193
- **官方描述（原文）**：Cisco Catalyst SD-WAN Manager contains a hex encoding vulnerability that could allow an unauthenticated, remote attacker to access an affected system with privileges of the admin user due to improper handling of URI encoding in an HTTP request.

### 2. CVE-2017-20051｜未確認 / 未確認
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=unconfirmed)
- **Risk**：WATCH / score 0；reasons：未確認
- **CVSS**：未確認
- **EPSS**：0.0075 / percentile=0.53121
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2022-06-16T07:15:07.053 / 2026-09-30T18:17:17.283
- **官方描述（原文）**：Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: The sole source documents PE-format conformance defects in innosetup-5.5.9.exe with no exploit, attack path, or untrusted search path condition (CWE-426/427), and the author states Windows loads these files normally; the record's remote/exploited claims are unsupported, as is the product maintainer's contention.

### 3. CVE-2026-62308｜Quenary / tugtainer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:49.423)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:49.423 / 2026-09-30T20:17:34.140
- **官方描述（原文）**：Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.6, Tugtainer allows an authenticated user to make the backend server send outbound HTTP requests to arbitrary user-supplied URLs through the notification test endpoint. The /settings/test_notification endpoint accepts a urls field and passes it directly to Apprise without restricting protocols, hostnames, localhost addresses, private IP ranges, or cloud metadata addresses. This can be abused as an authenticated blind server-side request forgery (SSRF). This issue has been patched in version 1.30.6.

### 4. CVE-2026-55494｜Quenary / tugtainer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:47.100)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:47.100 / 2026-09-30T19:57:08.043
- **官方描述（原文）**：Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.4, Tugtainer Agent allows unauthenticated access to Docker management APIs when AGENT_SECRET is not configured. The Agent uses request signatures to protect its API routes. However, in agent/auth.py, the signature verification function returns successfully if Config.AGENT_SECRET is empty. This causes protected Agent APIs to become accessible without authentication. This issue has been patched in version 1.30.4.

### 5. CVE-2026-55181｜Quenary / tugtainer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:46.937)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:46.937 / 2026-09-30T20:17:33.650
- **官方描述（原文）**：Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.3, Tugtainer's OIDC authentication can still be initiated even when OIDC_ENABLED=false. The /auth/oidc/enabled endpoint correctly reports that OIDC is disabled. However, a direct request to /auth/oidc/login still starts the OIDC login flow, returns HTTP 302, sets an oidc_state cookie, and redirects the user to the configured OIDC authorization endpoint. This bypasses the intended OIDC disable switch. This issue has been patched in version 1.30.3.

### 6. CVE-2026-55107｜elct9620 / kobako
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T18:18:37.550)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T18:18:37.550 / 2026-09-30T20:17:32.923
- **官方描述（原文）**：Kobako is a Ruby gem that embeds a Wasm-isolated mruby interpreter inside applications, allowing execution of untrusted Ruby scripts (LLM-generated code, user formulas, student submissions, third-party plugins) in-process without giving them access to host memory, files, network, or credentials. From version 0.1.0 to before version 0.9.1, a guest mruby script running inside the Kobako sandbox can execute arbitrary Ruby in the host process, fully escaping the sandbox. This issue has been patched in version 0.9.1.

### 7. CVE-2026-103395｜ModelTC / LightLLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T15:22:27.710)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T15:22:27.710 / 2026-09-30T20:17:30.840
- **官方描述（原文）**：LightLLM through 1.2.0 visual_only deployments expose an unauthenticated RPyC service with allow_pickle enabled that deserializes attacker-supplied arguments in the remote_infer_images method. Attackers can reach the visual RPyC port and pass objects with __reduce__ methods to execute arbitrary code with service account privileges.

### 8. CVE-2026-102992｜piscinajs / piscina
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T20:17:27.080)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T20:17:27.080 / 2026-09-30T21:17:06.450
- **官方描述（原文）**：piscina is a node.js worker pool implementation. Prior to 4.9.4, 5.3.2, and 6.0.0-rc.5, Piscina stores ThreadPool.options in src/index.ts as a plain object that inherits from Object.prototype. Applications with a separate prototype-pollution primitive can therefore supply inherited values for security-sensitive options that do not have own defaults. An inherited execArgv value is passed to the Node.js Worker constructor and can preload attacker-controlled code in worker threads, an inherited loadBalancer function can execute during task scheduling, and inherited env values can alter worker environments. This issue is fixed in versions 4.9.4, 5.3.2, and 6.0.0-rc.5.

### 9. CVE-2026-87004｜Quenary / tugtainer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T18:18:41.470)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T18:18:41.470 / 2026-09-30T19:57:08.043
- **官方描述（原文）**：Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.31.3, when the OIDC login flow completes, backend/modules/auth/providers/auth_oidc_provider.py decodes the id_token returned by the identity provider's token endpoint using jose.jwt.get_unverified_claims() instead of jwt.decode(). This skips signature verification, audience (aud) validation, issuer (iss) validation, and expiry (exp) checking entirely. The extracted claims (email/sub/preferred_username) are then used directly as the user_id for the resulting Tugtainer session. This issue has been patched in version 1.31.3.

### 10. CVE-2026-55177｜dfpc-coe / CloudTAK
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:46.787)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:46.787 / 2026-09-30T20:17:33.477
- **官方描述（原文）**：CloudTAK is a browser-based Common Operating Picture and situational awareness tool compatible with TAK. Prior to version 13.10.0, every route in the ESRI helper family (api/routes/esri.ts) takes a fully attacker-controlled URL from the request (POST /api/esri body url, and the portal / server / layer query parameters on the GET /api/esri/* routes) and passes it into EsriBase / EsriProxyPortal / EsriProxyServer / EsriProxyLayer in api/lib/esri.ts, which fetch it with the bare fetch from @tak-ps/etl. No IP / DNS / hostname classification is applied at any point, so the destination is never validated against private, loopback, or link-local ranges. Any authenticated user (the routes only require Auth.is_auth(config, req, { anyResources: true }), i.e. any token, not an admin) can therefore make the CloudTAK server issue arbitrary outbound GET/POST requests to internal addresses such as the cloud instance-metadata service (169.254.169.254), loopback admin ports (127.0.0.1:<port>), and other hosts reachable only from inside the deployment VPC. This is a full-read SSRF, not blind: on success the upstream JSON body is returned to the caller via res.json(...), and on failure the upstream error string is reflected verbatim as ESRI Server Error: <message>. An attacker can read cloud metadata (and the temporary IAM credentials the instance role exposes), enumerate internal services, and exfiltrate their response bodies. The sniff() URL classifier provides no protection: it only pattern-matches the pathname (/rest, /arcgis/rest, /sharing/rest), so a URL like http://169.254.169.254/arcgis/rest or http://127.0.0.1:8500/rest passes sniff() and is fetched. This issue has been patched in version 13.10.0.

### 11. CVE-2026-46711｜Soft-Machine-io / security
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:46.060)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:46.060 / 2026-09-30T19:57:08.043
- **官方描述（原文）**：Soft Machine is a Virtual Machine–based agentic development environment / Cloud OS. In versions 0.2.247 and prior, the workspace HTTP service that listens on 0.0.0.0:8080 inside each sm-ws-* Fly Machine exposes endpoints (/health, /file/<path>, /archive/<dir>) without any authentication or origin check. Any host that can reach TCP/8080 on a workspace can read arbitrary files under that workspace's /workspace root and download whole project trees as tar archives. Because every workspace shares the same Fly private 6PN and resolves all peer addresses via the unauthenticated _instances.internal TXT record, every other sm-ws-* machine on the same Fly app/org is a reachable, unauthenticated attacker — the trust boundary (workspace owner ↔ everyone-else) is missing. At time of publication, there are no publicly known patches.

### 12. CVE-2026-103471｜Corvusoft / restbed
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T18:18:17.163)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T18:18:17.163 / 2026-09-30T20:17:31.283
- **官方描述（原文）**：restbed through 5.0.0 buffers HTTP request headers without enforcing a maximum size limit, allowing remote unauthenticated attackers to exhaust server memory. Attackers can open TCP connections and stream bytes indefinitely without sending the header delimiter, forcing the server to allocate unbounded heap memory until the process is killed.

### 13. CVE-2026-103270｜ModelTC / LightLLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T15:22:26.903)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T15:22:26.903 / 2026-09-30T16:17:08.847
- **官方描述（原文）**：LightLLM through 1.2.0 mounts reinforcement learning control routes on the public HTTP API without authentication checks. Unauthenticated attackers can call endpoints like /pause_generation, /abort_request, /flush_cache, and /init_weights_update_group to disrupt inference operations and wedge workers on deployments started with --enable_rl.

### 14. CVE-2026-102990｜patrickjuchli / basic-ftp
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T20:17:26.140)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T20:17:26.140 / 2026-09-30T21:17:06.307
- **官方描述（原文）**：basic-ftp is an FTP client for Node.js. Prior to 6.2.1, Client.list() can be forced by a malicious or compromised FTP server to spend quadratic CPU time parsing a directory listing because the RE_LINE expression in src/parseListUnix.ts backtracks across adjacent variable-length owner and group fields when a long Unix-style line has a valid prefix but cannot satisfy the later size and date fields. parseList() selects a parser from the last nonblank line and then applies it to every line, so a normal final line can select the Unix parser while an earlier crafted line blocks the Node.js event loop and freezes the process. This issue is fixed in version 6.2.1.

### 15. CVE-2026-101885｜zeroclaw-labs / ZeroClaw
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T20:17:21.157)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T20:17:21.157 / 2026-10-01T02:20:29.877
- **官方描述（原文）**：ZeroClaw versions before 0.8.5 built with plugins-wasm feature contain a path traversal vulnerability in plugin installation that fails to validate the wasm_path manifest field. Attackers can convince users to install crafted plugins that write arbitrary files to paths outside the plugins directory, such as shell startup files, enabling code execution.

### 16. CVE-2026-101884｜OpenClaw / OpenClaw Windows Node
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T20:17:20.663)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T20:17:20.663 / 2026-10-01T02:20:29.877
- **官方描述（原文）**：OpenClaw Windows Node before 2026.7.1 contains an incomplete environment-variable sanitizer in system.run that fails to block GIT_CONFIG_*, DOTNET_STARTUP_HOOKS, and JAVA_TOOL_OPTIONS variables. Attackers with gateway or agent access can supply these variables to allowlisted tools like git, dotnet, or java to load attacker-controlled code and achieve arbitrary code execution.

### 17. CVE-2026-101881｜OpenClaw / OpenClaw Windows Node
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T20:17:19.330)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T20:17:19.330 / 2026-10-01T02:20:29.877
- **官方描述（原文）**：OpenClaw Windows Node before 2026.7.1 contains an allocation of resources without limits vulnerability in the gateway WebSocket transport that allows connected gateways to exhaust node memory. Attackers can send an unending sequence of WebSocket continuation frames without EndOfMessage to cause unbounded memory growth until the node process crashes.

### 18. CVE-2026-101880｜OpenClaw / OpenClaw Windows Node
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T20:17:18.857)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T20:17:18.857 / 2026-10-01T02:20:29.877
- **官方描述（原文）**：OpenClaw Windows Node before 2026.7.1 contains an incorrect authorization vulnerability in the system.run exec-approval policy where ExecShellWrapperParser fails to split commands on pipe operators or extract command substitutions. Connected gateways or agents can bypass approval rules by placing denied commands behind allowed prefixes using pipe operators or command substitution syntax, achieving arbitrary command execution on Windows hosts.

### 19. CVE-2026-97274｜miniOrange / OAuth Single Sign On – SSO (OAuth Client)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:38.293)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:38.293 / 2026-09-30T14:18:17.173
- **官方描述（原文）**：Unauthenticated Bypass Vulnerability in OAuth Single Sign On – SSO (OAuth Client) <= 7.1.2 versions.

### 20. CVE-2026-97248｜Booking Activities Team / Booking Activities
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:36.830)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:36.830 / 2026-09-30T14:18:15.890
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Booking Activities <= 1.18.7.1 versions.

### 21. CVE-2026-97196｜Liquid Web / StellarWP / GiveWP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T07:16:31.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T07:16:31.320 / 2026-09-30T14:18:14.160
- **官方描述（原文）**：Improper Validation of Unsafe Equivalence in Input vulnerability in Liquid Web / StellarWP GiveWP allows Authentication Bypass. This issue affects GiveWP: from n/a through 4.16.9.

### 22. CVE-2026-96822｜Hossni Mubarak / Books Gallery
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:31.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:31.750 / 2026-09-30T14:18:11.310
- **官方描述（原文）**：Unauthenticated SQL Injection in Books Gallery <= 4.8.3 versions.

### 23. CVE-2026-96350｜Estatik / Estatik
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:30.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:30.090 / 2026-09-30T14:18:09.523
- **官方描述（原文）**：Subscriber Privilege Escalation in Estatik <= 4.3.5 versions.

### 24. CVE-2026-96349｜SiteSkite / SiteSkite
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:29.967)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:29.967 / 2026-09-30T14:18:09.253
- **官方描述（原文）**：Unauthenticated Remote Code Execution (RCE) in SiteSkite <= 2.1.8 versions.

### 25. CVE-2026-94389｜AcyMailing Newsletter Team / AcyMailing SMTP Newsletter
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:26.840)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:26.840 / 2026-09-30T14:17:49.070
- **官方描述（原文）**：Unauthenticated Remote Code Execution (RCE) in AcyMailing SMTP Newsletter <= 11.0.5 versions.

### 26. CVE-2026-94053｜Apache Software Foundation / Apache MINA SSHD
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T10:17:18.283)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T10:17:18.283 / 2026-09-30T16:13:13.493
- **官方描述（原文）**：Authentication bypass via LDAP injection in component sshd-ldap in Apache MINA SSHD versions 1.2.0 to 2.19.0 and 3.0.0-M1 to 3.0.0-M5. Apache MINA SSHD is a Java library for client-side and server-side SSH. The optional sshd-ldap component provides support for integrating password and publickey authentication on the server side with an LDAP server. sshd-ldap is an optional component. SSH servers implemented with Apache MINA SSHD are affected only if they use sshd-ldap and do configure it to be used for password of public key authentication. Other Apache MINA SSHD servers are not affected. Lack of escaping LDAP filter metacharacters enabled successful authentication with username "*" and password "*". Users are recommended to upgrade affected applications to version 2.20.0 or 3.0.0-M6, which fix this issue by properly escaping filter parameters according to RFC 4515.

### 27. CVE-2026-94052｜Apache Software Foundation / Apache MINA SSHD
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T10:17:18.147)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T10:17:18.147 / 2026-09-30T16:13:13.493
- **官方描述（原文）**：A missing check in LdapPasswordAuthenticator in component sshd-ldap in Apache MINA SSHD versions 1.2.0 to 2.19.0 or 3.0.0-M1 to 3.0.0-M5 bypassed authentication checks. Apache MINA SSHD is a Java library for client-side and server-side SSH. The optional sshd-ldap component provides support for integrating password and publickey authentication on the server side with an LDAP server. sshd-ldap is an optional component. SSH servers implemented with Apache MINA SSHD are affected only if they use sshd-ldap and do configure an LdapPasswordAuthenticator to be used for password authentication. Normal password authentication via the built-in mechanisms in sshd-core is _not_ affected by this vulnerability, which concerns only LdapPasswordAuthenticator. Users are recommended to upgrade affected applications to version 2.20.0 or 3.0.0-M6, which fix this issue.

### 28. CVE-2026-93903｜litespeedtech / LiteSpeed Web Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T14:17:37.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T14:17:37.060 / 2026-09-30T17:23:08.953
- **官方描述（原文）**：LiteSpeed Web Server (LSWS) before 6.3.7 build 1 mishandles internal redirect URL validation in a certain "corner case."

### 29. CVE-2026-92966｜latepoint / Appointment Booking Plugin – LatePoint | Calendar & Scheduling for WordPress
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T05:17:11.967)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T05:17:11.967 / 2026-10-01T05:17:11.967
- **官方描述（原文）**：The The Appointment Booking Plugin – LatePoint | Calendar & Scheduling for WordPress plugin for WordPress is vulnerable to arbitrary shortcode execution in all versions up to, and including, 5.7.0. This is due to the software allowing users to execute an action that does not properly validate a value before running do_shortcode. This makes it possible for unauthenticated attackers to execute arbitrary shortcodes. The payload is planted during the unauthenticated booking flow and triggered when the Customer Cabinet block rendered by render_customer_dashboard() outputs the stored name into the content stream, where WordPress core's do_shortcode filter at priority 11 re-parses and executes it.

### 30. CVE-2026-89238｜Apache Software Foundation / Apache WSS4J
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:21.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:21.587 / 2026-09-30T20:17:35.917
- **官方描述（原文）**：WSS4J EncryptedHeader child confusion could promote an attacker-controlled plaintext element as the decrypted header, leading to incorrect confidentiality coverage and possible policy bypass. Users are recommended to upgrade to versions 4.0.2 or 3.0.6 or 2.4.4, which fix this issue.

### 31. CVE-2026-88920｜Apache Software Foundation / Apache WSS4J
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T12:17:14.203)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T12:17:14.203 / 2026-09-30T20:17:35.737
- **官方描述（原文）**：An authentication bypass in the DOM security processor in Apache WSS4J allows unauthenticated remote attackers to forge authenticated SOAP messages via a crafted unsigned SAML sender-vouches assertion containing an attacker-controlled key. Users are recommended to upgrade to versions 4.0.2 or 3.0.6 or 2.4.4, which fix this issue.

### 32. CVE-2026-87830｜Apache Software Foundation / Apache WSS4J
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T12:17:14.087)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T12:17:14.087 / 2026-09-30T20:17:35.183
- **官方描述（原文）**：In the StAX streaming WS-SecurityPolicy validator, certain relative or unsupported XPath expressions can be converted into paths that never match the actual XML element path. A remote SOAP peer may therefore send a required element without the expected signature or encryption. Users are recommended to upgrade to versions 4.0.2 or 3.0.6 or 2.4.4, which fix this issue.

### 33. CVE-2026-82829｜Hitachi Industrial Equipment Systems / Hitachi Coding Software Suite
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T05:17:11.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T05:17:11.090 / 2026-10-01T05:17:11.090
- **官方描述（原文）**：Hitachi Coding Software Suite contains a vulnerability related to Hidden Functionality vulnerability which allows an attacker to gain unauthorized access by exploiting hidden accounts or hard coded credentials. This issue affects Hitachi Coding Software Suite: through 3.3.0.

### 34. CVE-2026-82827｜Hitachi Industrial Equipment Systems / Hitachi Coding Software Suite
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T05:17:10.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T05:17:10.780 / 2026-10-01T05:17:10.780
- **官方描述（原文）**：Hitachi Coding Software Suite contains a vulnerability related to Use of Hard-coded Cryptographic Key. The Hardcoding of JWT signing secret key allows an attacker to generate unauthorized Bearer tokens and exploit administrative functions. This issue affects Hitachi Coding Software Suite: through 3.3.0.

### 35. CVE-2026-82825｜Hitachi Industrial Equipment Systems / Hitachi Coding Software Suite
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T05:17:10.443)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T05:17:10.443 / 2026-10-01T05:17:10.443
- **官方描述（原文）**：Hitachi Coding Software Suite contains a vulnerability related to Missing Authentication for Critical Function. This allows an unauthenticated attacker to invoke a critical API, potentially leading to unauthorized retrieval or alteration of sensitive information, or unauthorized manipulation. This issue affects Hitachi Coding Software Suite: through 3.3.0.

### 36. CVE-2026-82824｜Hitachi Industrial Equipment Systems / Hitachi Coding Software Suite
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T05:17:10.270)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T05:17:10.270 / 2026-10-01T05:17:10.270
- **官方描述（原文）**：Hitachi Coding Software Suite contains a vulnerability related to Path Traversal vulnerability that allows an attacker to access, create, modify, or delete files. This issue affects Hitachi Coding Software Suite: through 3.3.0.

### 37. CVE-2026-82307｜Dolusoft Software Technologies / SOPLOG
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T14:17:31.257)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T14:17:31.257 / 2026-09-30T16:18:57.403
- **官方描述（原文）**：Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Dolusoft Software Technologies SOPLOG allows SQL Injection. This issue affects SOPLOG: before Soplog 2026.9.4.1.

### 38. CVE-2026-77185｜Apache Software Foundation / Apache MINA SSHD
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T10:17:17.123)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T10:17:17.123 / 2026-09-30T17:16:49.877
- **官方描述（原文）**：Authentication bypass in sshd-core in Apache MINA SSHD versions 2.0.0 to 2.19.0 and 3.0.0-M1 to 3.0.0-M5 for a certain (presumed rare) way to implement an SSH server. Apache MINA SSHD is a Java library for client- and server-side SSH. In the server part of the library, a mechanism to perform "asynchronous authentication" exists. A server implemented with Apache MINA SSHD must contain explicit code to make use of this feature. The implementation of this feature was flawed and could potentially lead to skipping checking the signature in public-key or hostbased authentication, or returning a wrong result. Users are recommended to upgrade to Apache MINA SSHD 2.20.0 or 3.0.0-M6, which fix the logic error and which additionally forbid the use of this "asynchronous authentication" mechanism with the public-key or hostbased authentication schemes: if used, the SSH session will be closed and the server will log an entry indicating that asynchronous authentication may be used only with password or keyboard-interactive authentication.

### 39. CVE-2026-76570｜joomcode.com / JCTables extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T15:22:34.903)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T15:22:34.903 / 2026-09-30T16:44:39.840
- **官方描述（原文）**：Joomla Extension - joomcode.com - Unauthenticated SQL injection in read and write queries in JCTables 1.21.1 - The front-end CRUD API controller performs no Joomla token validation and no authentication check on any task. Table names, column names, and values are taken directly from request parameters and concatenated into SQL queries, allowing SQLi for reading and writing queries.

### 40. CVE-2026-76142｜Genians, Inc / Genian NAC 5.0.75 LTS Release
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T05:17:09.093)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T05:17:09.093 / 2026-10-01T05:17:09.093
- **官方描述（原文）**：Insufficient authentication and access control on the internal-only IPC SOAP endpoint of the Genian NAC/ZTNA policy server allows an unauthenticated attacker to invoke internal functions

### 41. CVE-2026-75969｜PTZOptics / Move 4K 12X
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:49.583)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:49.583 / 2026-09-30T21:17:13.377
- **官方描述（原文）**：Missing authentication for critical function vulnerability for all PTZOptics cameras and the Firmware Upgrade Tool - Firmware Update modules. A missing authentication vulnerability in the firmware update mechanism of affected PTZOptics cameras allows an unauthenticated user to install modified firmware on the device without administrator credentials. This vulnerability allows attackers to upload modified firmware to the device without admin credentials. This issue affects: * Move 4K 12X before: 0.0.98 * Move 4K 20X before: 0.1.33 * Move 4K 30X before: 2.1.17 * Link 4K 12X before: 0.0.99 * Link 4K 20X before: 0.1.37 * Link 4K 30X before: 2.1.18 * Move SE 12X before: 9.1.66 * Move SE 20X before: 9.1.44 * Move SE 30X before: 9.1.46 * Studio 4K 12X before: 8.3.32 * Studio 4K 20X before: 8.3.32 * Studio SE 12X before: 8.3.32 * Studio SE 20X before: 8.3.32 * All Generation 2 cameras, including: PT12X-SDI-GY-G2, PT12X-SDI-WH-G2, PT12X-NDI-GY-G2, PT12X-NDI-WH-G2; PT12X-USB-GY-G2, PT12X-USB-WH-G2; PT20X-SDI-GY-G2, PT20X-SDI-WH-G2, PT20X-NDI-GY-G2, PT20X-NDI-WH-G2; PT20X-USB-GY-G2, PT20X-USB-WH-G2; PT30X-SDI-GY-G2, PT30X-SDI-WH-G2, PT30X-NDI-GY-G2, PT30X-NDI-WH-G2; PTVL-ZCAM, PTVL-NDI-ZCAM; PTEPTZ-ZCAM-G2, PTEPTZ-NDI-ZCAM-G2; PT12X-ZCAM, PT12X-NDI-ZCAM; PT20X-ZCAM, PT20X-NDI-ZCAM; Studio Pro - All versions * Upgrade Tool - All versions

### 42. CVE-2026-75873｜Unknown / Zella Theme
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T06:17:04.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T06:17:04.670 / 2026-09-30T16:28:31.510
- **官方描述（原文）**：The Zella Theme WordPress theme before 2.6.3 does not perform any capability or nonce check on one of its font upload actions, which is available to unauthenticated users, allowing them to upload arbitrary files, including PHP ones, and achieve remote code execution.

### 43. CVE-2026-74865｜YunoHost-Apps / sogo_yhn
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:20.083)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:20.083 / 2026-09-30T19:57:08.043
- **官方描述（原文）**：sogo_yhn configures SOGo with a parameter "SOGoTrustProxyAuthentication=YES". This causes the password to be bypassed during HTTP Basic authentication. An unauthenticated attacker who provides the username of an existing user and any arbitrary password can successfully log in to that user's account. This issue was fixed in version 5.8.0~ynh9.

### 44. CVE-2026-74864｜YunoHost-Apps / sogo_yhn
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:19.913)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:19.913 / 2026-09-30T19:57:08.043
- **官方描述（原文）**：sogo_yhn configures SOGo with a parameter that forces the request with HTTP header "x-webobjects-remote-user" to be treated as sent by a verified user without performing password validation. Since Nginx does not strip this header, any client can supply it arbitrarily and gain access as any user, including a privileged user, without providing a password. This issue was fixed in version 5.8.0~ynh9.

### 45. CVE-2026-55176｜Soft-Machine-io / security
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:46.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:46.630 / 2026-09-30T19:57:08.043
- **官方描述（原文）**：Soft Machine is a Virtual Machine–based agentic development environment / Cloud OS. In versions 0.2.247 and prior, two authentication helpers in /app/server.js — verifyContainerAuth() and authenticateWorkspaceHttp() — accept the global CONTAINER_SHARED_SECRET as a bearer token without verifying which workspace the caller belongs to. Because that secret is set identically on every container in the Fly app and is reachable from the user-facing process environment inside each workspace, any tenant can use it to authenticate to any other tenant's workspace API. The result is cross-workspace read, write, and destructive-restore primitives reachable from any paying customer's shell. The existing per-workspace token check (workspaceTokenMatches) protects the user-facing per-workspace token path, but the shared-secret bearer path bypasses it entirely. At time of publication, there are no publicly known patches.

### 46. CVE-2026-19445｜Python Software Foundation / CPython
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:45.720)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:45.720 / 2026-10-01T01:16:36.590
- **官方描述（原文）**：A remote, unauthenticated TLS client can make a server crash or call through a freed pointer if its sni_callback assigns a different context to SSLSocket.context (the documented way to select a certificate per server name) and nothing else keeps the original ssl.SSLContext alive. Typical cases are servers that create an SSLContext per connection or replace it while connections are open; servers that wrap their listening socket with it are not affected. Mitigation: keep a reference to every SSLContext that sets sni_callback for the lifetime of the server. TLS clients are not affected.

### 47. CVE-2026-18782｜Trex Digital Smart Manufacturing Systems Inc. / Trex MES
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T15:22:30.177)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T15:22:30.177 / 2026-09-30T16:18:57.403
- **官方描述（原文）**：Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Trex Digital Smart Manufacturing Systems Inc. Trex MES allows Command Line Execution through SQL Injection. This issue affects Trex MES: through 2026-09-29.

### 48. CVE-2026-14157｜ASUS / Router
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T02:16:53.983)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T02:16:53.983 / 2026-10-01T02:16:53.983
- **官方描述（原文）**：Use of an Externally Controlled Format String in the ASUS Router modules allow a remote authenticated user to execute arbitrary commands via a crafted file uploaded through the web management interface.

### 49. CVE-2026-103547｜OpenBSD / OpenBSD
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T20:17:31.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T20:17:31.607 / 2026-09-30T20:17:31.607
- **官方描述（原文）**：In ldapd in OpenBSD 7.8 before errata 057 and 7.9 before errata 021, delegated BSD authentication results are correlated only by the LDAP child process client file descriptor and LDAP message ID. After a connection closes, a later connection that reuses the same file descriptor and message ID can receive the earlier authentication result. A remote attacker who can reach ldapd can complete a Bind as another identity. A missing connection can also cause a NULL pointer dereference. (ldapd is not enabled by default.)

### 50. CVE-2026-103475｜yii2-starter-kit / yii2-starter-kit
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T18:18:17.817)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T18:18:17.817 / 2026-09-30T20:17:31.447
- **官方描述（原文）**：yii2-starter-kit through 4.2.0 exposes the Yii debug and Gii modules to all IP addresses by setting allowedIPs to ['*'] in its default development configuration. Unauthenticated remote attackers can access the debug endpoint to read sensitive data including session cookies and database queries, or access the Gii endpoint to generate and write PHP files into the application directory.

### 51. CVE-2026-103473｜denoland / deno
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T18:18:17.483)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T18:18:17.483 / 2026-09-30T19:08:21.363
- **官方描述（原文）**：Deno versions 2.7.0 through 2.9.7 on Windows contain a command injection vulnerability in node:child_process where shell arguments are escaped for the wrong shell type. Attackers can inject OS commands by passing untrusted arguments with the shell option, allowing arbitrary command execution with Deno process privileges.

### 52. CVE-2026-103470｜Internet2 / Grouper
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T16:17:10.230)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T16:17:10.230 / 2026-09-30T19:16:40.507
- **官方描述（原文）**：In Internet2 Grouper before 7.5.1 (in some configurations), a user who is allowed to create or edit rules in the User Interface can escalate privileges.

### 53. CVE-2026-102508｜Apache Software Foundation / Apache PLC4X
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T08:16:31.903)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T08:16:31.903 / 2026-09-30T16:14:10.347
- **官方描述（原文）**：Improper Verification of Cryptographic Signature and Improper Certificate Validation in the OPC UA driver of Apache PLC4X (PLC4J) allows an attacker in a network position between client and server to impersonate the OPC UA server and to read, forge or modify secure-channel traffic, including user credential ssent by the client. The defect manifests differently depending on the version: - In 0.9.0 through 0.11.0 a failed message-signature check is only logged and never enforced, and there is no mechanism to verify the server certificate: it is taken from the unauthenticated GetEndpoints discovery response and used to encrypt the user's password. - In 0.12.0 through 0.13.1 the signature check is inverted (valid signatures are rejected, invalid ones accepted), and server certificates are accepted without a trust anchor by default. - In all affected versions the default security policy is None. Starting with 0.12.0 the driver additionally continues silently at a weaker security policy than the one configured, and starting with 0.13.0 endpoint selection prefers the weakest matching endpoint. Users checking only for one of these mechanisms may wrongly conclude they are unaffected. This issue affects Apache PLC4X: from 0.9.0 before 1.0.0. Users are recommended to upgrade to version 1.0.0, which fixes the issue. Version 1.0.0 verifies message signatures correctly, refuses to connect unless the server certificate can be verified against a configured trust store or pinned certificate, defaults to Basic256Sha256 with SignAndEncrypt, and fails the connection if the negotiated security policy is weaker than the configured one.

### 54. CVE-2026-102490｜Zammad GmbH / Zammad
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:40.707)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:40.707 / 2026-09-30T19:57:08.043
- **官方描述（原文）**：All versions of Zammad including the latest alpha enable the local zammad user to escalate privileges to root.

### 55. CVE-2026-102489｜Zammad GmbH / Zammad
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:40.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:40.550 / 2026-09-30T19:57:08.043
- **官方描述（原文）**：Zammad versions 6.3.0 to 6.5.4 are vulnerable a session hijack vulnerability that leads to remote code execution as the zammad user. The vulnerability is also present in version 7.0.0 to version 7.1.3, but not exploitable due to environment conditions.

### 56. CVE-2026-102458｜DigiWin / EasyFlow .NET
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T09:17:13.800)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T09:17:13.800 / 2026-09-30T16:30:42.327
- **官方描述（原文）**：EasyFlow .NET developed by Digiwin has a Missing Authentication vulnerability. Unauthenticated remote attackers can obtain other users' plaintext passwords through a specific API.

### 57. CVE-2026-102455｜DigiWin / EasyFlow .NET
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T09:17:13.343)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T09:17:13.343 / 2026-09-30T16:30:42.327
- **官方描述（原文）**：EasyFlow .NET developed by Digiwin has a Insecure Deserialization vulnerability. Unauthenticated remote attackers can execute arbitrary code on the server by sending maliciously crafted serialized content.

### 58. CVE-2026-102427｜ordasoft.com / OrdaSoft Joomla CCK
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T16:17:06.623)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T16:17:06.623 / 2026-09-30T16:44:39.840
- **官方描述（原文）**：Joomla Extension - ordasoft.com - Unauthenticated Remote Code Execution in OrdaSoft Joomla CCK < 8.3.16 - site/uploader.php is reached through the component’s normal frontend routing (task=getContent), a task with no authentication or ACL check anywhere in the dispatch chain. The handler validates the uploaded file’s content with a real magic-byte MIME check, but the extension allow-list that would otherwise restrict the saved file’s extension was present in the source and commented out. The saved file’s extension was taken directly from the attacker-supplied filename with no validation, and the file was written to a path directly under the Joomla web root that is executed by the PHP handler. An image/PHP polyglot, a file whose header bytes satisfy the MIME check with PHP source appended after, passed the content check while carrying a .php extension of the attacker’s choosing.

### 59. CVE-2026-102149｜Kiteworks / Email Protection Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T21:17:03.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T21:17:03.760 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：Kiteworks Email Protection Gateway did not sufficiently restrict which account a certificate could be assigned to. This could allow an attacker to associate a certificate with another user's account, affecting the confidentiality and integrity of that account's encrypted mail and, where certificate-based login is enabled, potentially permitting unauthorized access to the account.

### 60. CVE-2026-102147｜Kiteworks / Core
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T21:17:03.633)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T21:17:03.633 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：A stored cross-site scripting (XSS) weakness in Kiteworks Core could allow an unauthenticated attacker to store crafted content that later executes arbitrary JavaScript in the authenticated session of an administrator who views the affected page. This could have permitted the attacker to gain full administrative control, including the creation of a new administrative account.

### 61. CVE-2026-102115｜Kiteworks / Core
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T21:16:59.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T21:16:59.180 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：Kiteworks Core did not correctly validate a parameter submitted to the password reset workflow. An unauthenticated attacker who knew the email address of a user with a locally stored password could potentially reset that account's password without access to the emailed reset link and then authenticate as that user, including where the account holds administrative privileges.

### 62. CVE-2026-102106｜Kiteworks / Email Protection Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T21:16:57.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T21:16:57.490 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：Improper authentication in a Kiteworks Email Protection Gateway administrative service. An administrative service in Kiteworks Email Protection Gateway did not consistently enforce administrator authentication, so the required password check could be bypassed. An attacker who referenced a valid administrator account could potentially create, modify, or delete internal users and managed domains and change their security-feature configuration without authenticating; deleting a managed domain also removes its user accounts and could lock administrators out of the gateway.

### 63. CVE-2026-102105｜Kiteworks / Email Protection Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T21:16:57.370)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T21:16:57.370 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Server-Side Request Forgery (SSRF). A server-side request forgery (SSRF) weakness in Kiteworks Email Protection Gateway could allow a remote, unauthenticated attacker to induce the gateway to issue crafted requests to internal or otherwise unintended network destinations. The requests are triggered while the gateway renders message content that references external resources. Depending on the services reachable from the gateway, this could disclose sensitive internal information or trigger unintended actions on internal systems.

### 64. CVE-2026-102104｜Kiteworks / Email Protection Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T21:16:57.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T21:16:57.250 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Server-Side Request Forgery (SSRF). A server-side request forgery (SSRF) weakness in Kiteworks Email Protection Gateway could allow a remote, unauthenticated attacker to induce the gateway to issue crafted requests to internal or otherwise unintended network destinations. The requests are triggered while the gateway performs an online certificate status check for an inbound message. Depending on the services reachable from the gateway, this could disclose sensitive internal information or disrupt gateway operation.

### 65. CVE-2026-102103｜Kiteworks / Email Protection Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T21:16:57.127)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T21:16:57.127 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Server-Side Request Forgery (SSRF). A server-side request forgery (SSRF) weakness in Kiteworks Email Protection Gateway could allow a remote, unauthenticated attacker to induce the gateway to issue crafted requests to internal or otherwise unintended network destinations. The requests are triggered while the gateway retrieves a certificate revocation list in an inbound message. Depending on the services reachable from the gateway, this could disclose sensitive internal information or disrupt gateway operation.

### 66. CVE-2026-102102｜Kiteworks / Email Protection Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T21:16:57.000)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T21:16:57.000 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Server-Side Request Forgery (SSRF). A server-side request forgery (SSRF) weakness in Kiteworks Email Protection Gateway could allow a remote, unauthenticated attacker to induce the gateway to issue crafted requests to internal or otherwise unintended network destinations. The requests are triggered while the gateway retrieves an issuer certificate in an inbound message. Depending on the services reachable from the gateway, this could disclose sensitive internal information or disrupt gateway operation.

### 67. CVE-2026-102095｜Kiteworks / Email Protection Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T21:16:56.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T21:16:56.120 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：Kiteworks Email Protection Gateway before version 9.5.0 is vulnerable to Server-Side Request Forgery. Kiteworks Email Protection Gateway performed server-side fetches of URLs contained in the message content it processed, without adequately restricting the fetch destination. A remote, unauthenticated sender could craft a message that caused the gateway to issue requests to internal services and cloud instance metadata endpoints and return the responses, potentially disclosing sensitive internal data and, depending on the internal service reached, affecting its state.

### 68. CVE-2026-101283｜esnet / iperf3
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T22:16:33.317)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T22:16:33.317 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：iperf3 3.20–3.21 (esnet/iperf) has a pre-auth heap buffer overflow in decrypt_rsa_message(): a 256-byte RSA buffer is BIO_read with the attacker-controlled ciphertext length (guard warns only), so an unauthenticated client overflows the heap via an oversized authtoken; fixed in 3.22

### 69. CVE-2026-101276｜esnet / iperf3
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T21:16:54.913)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T21:16:54.913 / 2026-10-01T02:17:43.350
- **官方描述（原文）**：iperf3 3.21 (esnet/iperf) contains a remote, unauthenticated heap use-after-free: the server's per-test watchdog server_timer_proc() frees streams without cancelling/joining their worker threads, so a blocked worker dereferences a freed iperf_stream; fixed in 3.22.

### 70. CVE-2026-100512｜Hook & Filter / Nested Pages
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T18:17:59.300)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T18:17:59.300 / 2026-09-30T19:04:41.917
- **官方描述（原文）**：Contributor PHP Object Injection in Nested Pages <= 3.3.2 versions.

### 71. CVE-2026-55174｜shrec / UltrafastSecp256k1
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T16:17:31.457)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T16:17:31.457 / 2026-09-30T20:17:33.243
- **官方描述（原文）**：UltrafastSecp256k1 is a high-performance, multi-backend secp256k1 engine with reproducible audit evidence, compatibility shims, and profile-based review scopes. Prior to version 4.2.0, UltrafastSecp256k1's ECDSA adaptor pre-signature verification accepts forged adaptor pre-signatures whose "r" value is not cryptographically bound to the adaptor point "T". This issue has been patched in version 4.2.0.

### 72. CVE-2026-103232｜AdithyaYelloju / Restaurant-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:42.000)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:42.000 / 2026-09-30T18:18:15.767
- **官方描述（原文）**：A weakness has been identified in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff6b9c. This affects the function mysqli_query of the file admin/table_booking.php. This manipulation of the argument Name causes sql injection. Remote exploitation of the attack is possible. The exploit has been made available to the public and could be used for attacks. The project was informed of the problem early through an issue report but has not responded yet.

### 73. CVE-2026-103230｜AdithyaYelloju / Restaurant-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T16:17:08.463)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T16:17:08.463 / 2026-09-30T20:17:30.187
- **官方描述（原文）**：A vulnerability was determined in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff6b9c. Impacted is the function mysqli_query of the file User/ord.php of the component Order Placement. Executing a manipulation of the argument id/name can lead to sql injection. The attack can be launched remotely. The exploit has been publicly disclosed and may be utilized. The project was informed of the problem early through an issue report but has not responded yet.

### 74. CVE-2026-103229｜AdithyaYelloju / Restaurant-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T16:17:08.243)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T16:17:08.243 / 2026-09-30T16:38:36.297
- **官方描述（原文）**：A vulnerability was found in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff6b9c. This issue affects the function mysqli_query of the file admin/delete1.php of the component Unauthenticated Action Script. Performing a manipulation of the argument ID results in sql injection. The attack can be initiated remotely. The exploit has been made public and could be used. Continious delivery with rolling releases is used by this product. Therefore, no version details of affected nor updated releases are available. The project was informed of the problem early through an issue report but has not responded yet.

### 75. CVE-2026-102991｜sqlalchemy / mako
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T20:17:26.547)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T20:17:26.547 / 2026-09-30T20:17:26.973
- **官方描述（原文）**：Mako is a template library written in Python. Prior to 1.4.2, on Windows, TemplateLookup.get_template() in mako/lookup.py resolves template URIs with posixpath, while Template.__init__() in mako/template.py validates them with os.path, which uses ntpath. A URI beginning with a drive designator causes ntpath to absorb the traversal segments before the leading dot-dot check, while posixpath resolution can escape the configured template directory. An application that passes attacker-controlled template names or include paths can disclose process-readable files on the same volume, and a targeted file containing Mako template syntax may also be parsed and executed as a template. Raw URL paths are generally normalized before reaching this form, but query strings, form or JSON bodies, route parameters, and dynamic include expressions can preserve it. This issue is fixed in version 1.4.2.

### 76. CVE-2026-103387｜garycourt / uri-js
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T20:17:30.620)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T20:17:30.620 / 2026-10-01T02:12:10.020
- **官方描述（原文）**：A weakness has been identified in garycourt uri-js up to 4.4.1. This affects the function URI.parse of the file src/schemes/mailto.ts of the component Mailto Header Handler. This manipulation of the argument to causes uncaught exception. The attack may be initiated remotely. The exploit has been made available to the public and could be used for attacks. The project was informed of the problem early through an issue report but has not responded yet.

### 77. CVE-2026-103233｜AdithyaYelloju / Restaurant-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T17:16:42.177)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T17:16:42.177 / 2026-09-30T20:17:30.453
- **官方描述（原文）**：A security vulnerability has been detected in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff6b9c. This impacts an unknown function of the file /admin/ of the component Admin Area. Such manipulation of the argument ID leads to authorization bypass. The attack can be executed remotely. The exploit has been disclosed publicly and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 78. CVE-2026-103117｜OS4ED / openSIS-Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:18.280)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:18.280 / 2026-09-30T14:17:27.157
- **官方描述（原文）**：A security vulnerability has been detected in OS4ED openSIS-Classic up to 9.3. Affected is the function db_properties of the file functions/DatabaseInc.php of the component Save Data Handler. Such manipulation of the argument values leads to sql injection. The attack can be launched remotely. The exploit has been disclosed publicly and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 79. CVE-2026-103116｜OS4ED / openSIS-Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T13:17:18.090)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T13:17:18.090 / 2026-09-30T17:16:41.723
- **官方描述（原文）**：A weakness has been identified in OS4ED openSIS-Classic up to 9.3. This impacts the function DBQuery of the file functions/GetStuListFnc.php of the component Student List Search Endpoint. This manipulation of the argument LO_sort causes sql injection. The attack can be initiated remotely. The exploit has been made available to the public and could be used for attacks. The project was informed of the problem early through an issue report but has not responded yet.

### 80. CVE-2026-103114｜OS4ED / openSIS-Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T12:17:12.457)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T12:17:12.457 / 2026-09-30T14:17:27.010
- **官方描述（原文）**：A vulnerability was identified in OS4ED openSIS-Classic up to 9.3. The impacted element is the function DBQuery_assignment of the file modules/grades/Assignments.php of the component Assignment Management Endpoint. The manipulation of the argument Tables leads to sql injection. It is possible to initiate the attack remotely. The exploit is publicly available and might be used. The project was informed of the problem early through an issue report but has not responded yet.

### 81. CVE-2026-103113｜OS4ED / openSIS-Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T11:16:43.330)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T11:16:43.330 / 2026-09-30T17:16:41.583
- **官方描述（原文）**：A vulnerability was determined in OS4ED openSIS-Classic up to 9.3. The affected element is the function save action of the file modules/students/Student.php of the component General Information Tab. Executing a manipulation of the argument students can lead to sql injection. The attack may be performed from remote. The exploit has been publicly disclosed and may be utilized. The project was informed of the problem early through an issue report but has not responded yet.

### 82. CVE-2026-93353｜9001 / copyparty
- **Delta event**：CVSS_CHANGED (from=6.0; to=2.3)
- **Risk**：WATCH / score 10；reasons：POC_AVAILABLE(+10)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：0.00323 / percentile=0.22821
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T21:18:58.310 / 2026-09-30T21:17:17.490
- **官方描述（原文）**：copyparty contains a volume restriction bypass vulnerability in its SFTP front end that allows authenticated SFTP users to create, remove, and truncate arbitrary paths outside permitted volume boundaries by exploiting three handlers that bypass the xvol volflag enforcement. The _mkdir, _rmdir, and _chattr handlers construct destination paths using vfs.get(), vn.canonical(), and os.path.join() without invoking the chk_ap access check, enabling attackers to traverse symlinks leaving a volume's top directory and perform unauthorized file creation, deletion, or truncation via SSH_FXP_SETSTAT operations on paths outside any volume the account is authorized to access.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-76504｜Cisco / Catalyst SD-WAN Manager
- **Title**：Cisco Catalyst SD-WAN Manager Hex Encoding Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-30 / due_date=2026-10-03
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Catalyst SD-WAN Manager contains a hex encoding vulnerability that could allow an unauthenticated, remote attacker to access an affected system with privileges of the admin user due to improper handling of URI encoding in an HTTP request.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-62308 | P3 / 38 | Quenary / tugtainer | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55494 | P3 / 38 | Quenary / tugtainer | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55181 | P3 / 38 | Quenary / tugtainer | v3.1 9.4 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55107 | P3 / 38 | elct9620 / kobako | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-103395 | P3 / 38 | ModelTC / LightLLM | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102992 | P3 / 38 | piscinajs / piscina | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2017-20051 | WATCH / 0 | 未確認 / 未確認 | 未確認 | 0.0075 / percentile=0.53121 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-87004 | WATCH / 30 | Quenary / tugtainer | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55177 | WATCH / 30 | dfpc-coe / CloudTAK | v4.0 7.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-46711 | WATCH / 30 | Soft-Machine-io / security | v3.1 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-103471 | WATCH / 30 | Corvusoft / restbed | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-103270 | WATCH / 30 | ModelTC / LightLLM | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102990 | WATCH / 30 | patrickjuchli / basic-ftp | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101885 | WATCH / 30 | zeroclaw-labs / ZeroClaw | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101884 | WATCH / 30 | OpenClaw / OpenClaw Windows Node | v4.0 7.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101881 | WATCH / 30 | OpenClaw / OpenClaw Windows Node | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101880 | WATCH / 30 | OpenClaw / OpenClaw Windows Node | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97274 | WATCH / 28 | miniOrange / OAuth Single Sign On – SSO (OAuth Client) | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-97248 | WATCH / 28 | Booking Activities Team / Booking Activities | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-97196 | WATCH / 28 | Liquid Web / StellarWP / GiveWP | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96822 | WATCH / 28 | Hossni Mubarak / Books Gallery | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96350 | WATCH / 28 | Estatik / Estatik | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96349 | WATCH / 28 | SiteSkite / SiteSkite | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-94389 | WATCH / 28 | AcyMailing Newsletter Team / AcyMailing SMTP Newsletter | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-94053 | WATCH / 28 | Apache Software Foundation / Apache MINA SSHD | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-94052 | WATCH / 28 | Apache Software Foundation / Apache MINA SSHD | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93903 | WATCH / 28 | litespeedtech / LiteSpeed Web Server | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-92966 | WATCH / 28 | latepoint / Appointment Booking Plugin – LatePoint \| Calendar & Scheduling for WordPress | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89238 | WATCH / 28 | Apache Software Foundation / Apache WSS4J | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：1；缺少 Product：1；缺少 Title：29。
- EPSS 未確認：29；Exploitation status 未確認：2。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-01T06:42:01.194668+00:00`；Delta generated at：`2026-10-01T06:42:01.194668+00:00`。

---

## 可驗證資料來源

- **CVE-2026-76504** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76504) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2017-20051** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2017-20051) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2017-20051)
- **CVE-2026-62308** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62308)
- **CVE-2026-55494** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55494)
- **CVE-2026-55181** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55181)
- **CVE-2026-55107** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55107)
- **CVE-2026-103395** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103395)
- **CVE-2026-102992** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102992)
- **CVE-2026-87004** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87004)
- **CVE-2026-55177** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55177)
- **CVE-2026-46711** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46711)
- **CVE-2026-103471** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103471)
- **CVE-2026-103270** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103270)
- **CVE-2026-102990** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102990)
- **CVE-2026-101885** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101885)
- **CVE-2026-101884** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101884)
- **CVE-2026-101881** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101881)
- **CVE-2026-101880** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101880)
- **CVE-2026-97274** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97274)
- **CVE-2026-97248** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97248)
- **CVE-2026-97196** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97196)
- **CVE-2026-96822** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96822)
- **CVE-2026-96350** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96350)
- **CVE-2026-96349** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96349)
- **CVE-2026-94389** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94389)
- **CVE-2026-94053** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94053)
- **CVE-2026-94052** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94052)
- **CVE-2026-93903** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93903)
- **CVE-2026-92966** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92966)
- **CVE-2026-89238** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89238)
- **CVE-2026-88920** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88920)
- **CVE-2026-87830** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87830)
- **CVE-2026-82829** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82829)
- **CVE-2026-82827** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82827)
- **CVE-2026-82825** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82825)
- **CVE-2026-82824** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82824)
- **CVE-2026-82307** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82307)
- **CVE-2026-77185** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77185)
- **CVE-2026-76570** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76570)
- **CVE-2026-76142** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76142)
- **CVE-2026-75969** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75969)
- **CVE-2026-75873** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75873)
- **CVE-2026-74865** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-74865)
- **CVE-2026-74864** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-74864)
- **CVE-2026-55176** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55176)
- **CVE-2026-19445** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19445)
- **CVE-2026-18782** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18782)
- **CVE-2026-14157** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14157)
- **CVE-2026-103547** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103547)
- **CVE-2026-103475** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103475)
- **CVE-2026-103473** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103473)
- **CVE-2026-103470** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103470)
- **CVE-2026-102508** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102508)
- **CVE-2026-102490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102490)
- **CVE-2026-102489** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102489)
- **CVE-2026-102458** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102458)
- **CVE-2026-102455** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102455)
- **CVE-2026-102427** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102427)
- **CVE-2026-102149** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102149)
- **CVE-2026-102147** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102147)
- **CVE-2026-102115** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102115)
- **CVE-2026-102106** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102106)
- **CVE-2026-102105** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102105)
- **CVE-2026-102104** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102104)
- **CVE-2026-102103** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102103)
- **CVE-2026-102102** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102102)
- **CVE-2026-102095** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102095)
- **CVE-2026-101283** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101283)
- **CVE-2026-101276** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101276)
- **CVE-2026-100512** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100512)
- **CVE-2026-55174** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55174)
- **CVE-2026-103232** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103232)
- **CVE-2026-103230** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103230)
- **CVE-2026-103229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103229)
- **CVE-2026-102991** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102991)
- **CVE-2026-103387** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103387)
- **CVE-2026-103233** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103233)
- **CVE-2026-103117** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103117)
- **CVE-2026-103116** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103116)
- **CVE-2026-103114** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103114)
- **CVE-2026-103113** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103113)
- **CVE-2026-93353** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93353) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93353)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
