# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**55** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=1、NEW_CVE=53、NEW_KEV=1。
- Intelligence 候選：**30** 筆；P1 **1**、P2 **0**、P3 **2**、WATCH **27**。
- Baseline：state / generated_at=2026-09-21T05:41:16.010287+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-7273。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **55** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-7273｜Zyxel / GS1900 Series Switches
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00315 / percentile=0.24603
- **CISA KEV**：listed=true / date_added=2026-09-21 / due_date=2026-09-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-06-16T03:16:13.557 / 2026-09-22T04:17:59.273
- **官方描述（原文）**：Zyxel GS1900 series switches contain a stack-based buffer overflow vulnerability in the CGI program which could allow a LAN-based, unauthenticated attacker to exploit the flaw and potentially execute OS commands via a crafted HTTP request.

### 2. CVE-2026-61674｜fluent / fluent-bit
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T17:17:36.663)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T17:17:36.663 / 2026-09-21T19:17:07.067
- **官方描述（原文）**：Fluent Bit is a fast and lightweight logs, metrics, and traces processor for Linux, BSD, macOS, and Windows. From 0.11.0 until 5.0.8, plugins/out_forward/forward.c secure_forward_pong copies the server-controlled PONG[2] reason into the 32-byte stack buffer msg with memcpy without checking its MessagePack type or length. An attacker who controls or can impersonate an out_forward Secure Forward destination configured with Shared_Key or Empty_Shared_Key can send an oversized reason during the first handshake and overwrite stack control data. Protected builds reliably terminate, while builds without a stack canary or with a disclosure can allow remote code execution as the Fluent Bit process user. When the opt-in --supervisor mode is used, fork-only respawns preserve the canary and address layout, allowing repeated crash-or-survive probes to support code execution on a hardened build; ordinary exec-based or service-manager restarts do not preserve that state. This issue is fixed in version 5.0.8.

### 3. CVE-2025-12999｜Eclipse Foundation / Eclipse Open VSX
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T09:17:04.533)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00405 / percentile=0.34452
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T09:17:04.533 / 2026-09-21T18:11:49.423
- **官方描述（原文）**：UrlUtil.getBaseUrl builds the absolute URLs in a response — download links, icons, asset and API URLs — from the X-Forwarded-Host, X-Forwarded-Proto and X-Forwarded-Prefix request headers, with no check on whether the sender was a trusted proxy, falling back to the client-supplied Host header. Those responses are cached under keys that do not include the host (extension.json since 0.6.0, namespace.details.json since 0.9.0, sitemap since 0.14.5, latest.extension.version.vscode since 0.34.2). A single request carrying a forged header therefore places attacker-chosen URLs into an entry served to every other client for the lifetime of that entry — one hour by default, and cluster-wide where ovsx.redis.enabled is set. The VSIX download URL, its signature URL and the public key URL are all derived from the same base URL, so extension signing does not limit the impact: an attacker who poisons an entry supplies the package, the signature over it, and the key used to verify it. Exploitability depends on deployment topology. A server reachable directly by clients, or fronted by a proxy that relays the client's X-Forwarded-Host rather than overwriting it, is exploitable by an unauthenticated remote attacker. A proxy that overwrites the header is not. An unauthenticated attacker can poison Open VSX's per-extension metadata cache with attacker-controlled download, signature, and public-key URLs by supplying a crafted X-Forwarded-Host header, causing downstream VS Code-compatible editors to fetch and install a malicious VSIX. Workarounds (unpatched versions) 1. Configure the reverse proxy to set rather than relay X-Forwarded-Host, X-Forwarded-Proto and X-Forwarded-Prefix — note that nginx's $host is the client's Host header and is not a safe value. 2. Ensure the server is not reachable except through that proxy. 3. Flush the caches afterwards; poisoned entries survive the configuration change.

### 4. CVE-2026-94501｜jishenghua / jshERP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T19:17:21.910)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T19:17:21.910 / 2026-09-21T19:17:21.910
- **官方描述（原文）**：jshERP through 3.6 contains an authorization bypass vulnerability in the userBusiness CRUD endpoints that allows authenticated users to create, modify, or delete authorization-relation rows without privilege checks. Attackers can manipulate user-role mappings and access controls to escalate privileges, strip access from other accounts, or modify role-function relationships for any user in the tenant.

### 5. CVE-2026-94496｜jishenghua / jshERP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T19:17:21.590)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T19:17:21.590 / 2026-09-21T20:17:41.680
- **官方描述（原文）**：jshERP through 3.6 fails to validate caller permissions in role management endpoints, allowing authenticated users to modify any role's data scope or delete roles. Attackers can exploit the /role/update and /role/delete endpoints to escalate privileges, change data visibility to all data, and access all business records in the tenant.

### 6. CVE-2026-94488｜Telegram / Telegram Desktop
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T18:17:17.173)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T18:17:17.173 / 2026-09-21T18:17:17.173
- **官方描述（原文）**：Telegram Desktop before 6.9.4 allows XSS in the HTML exporter. (The first fixed stable version is 7.0.1.) This occurs in button.text.toUtf8 in export_output_html.cpp. Exploitation cannot occur unless HTML export was used by a victim. However, the exploit payload can be exported if a message were forwarded into a group by a member (it is not necessary for the message author to be a member of a group).

### 7. CVE-2026-94412｜jishenghua / jshERP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T19:17:20.217)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T19:17:20.217 / 2026-09-21T19:17:20.217
- **官方描述（原文）**：jshERP through 3.6 contains an authorization bypass vulnerability in the POST /user/resetPwd endpoint that allows authenticated users to reset any other user's password. Attackers can submit a request with an arbitrary target user ID to reset that account's password to a known default value, enabling unauthorized access to other user accounts including administrators.

### 8. CVE-2026-73546｜envoyproxy / envoy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T20:17:28.040)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T20:17:28.040 / 2026-09-21T21:17:09.360
- **官方描述（原文）**：Envoy is an open source edge and service proxy designed for cloud-native applications. Prior to 1.36.10, 1.37.6, 1.38.4, and 1.39.1, Envoy's /stats?format=html admin endpoint uses StatsHtmlRender, which sanitizes string statistic values but emits statistic names without HTML encoding. A data-plane component such as grpc_stats with stats_for_all_methods enabled can incorporate attacker-controlled path segments into cached dynamic statistic names. When an operator views the HTML stats page, the stored name can execute script with the admin interface's origin and issue privileged same-origin requests. The relevant scope boundary is that the admin interface must be browser-accessible and an enabled component must persist attacker-influenced text in statistic names. This issue is fixed in versions 1.36.10, 1.37.6, 1.38.4, and 1.39.1.

### 9. CVE-2026-63116｜deepstreamIO / deepstream.io
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T17:17:38.510)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T17:17:38.510 / 2026-09-21T18:17:09.873
- **官方描述（原文）**：deepstream is a server that allows clients and backend services to sync data, send messages and make rpcs at scale. From 10.1.0 until 10.1.1, src/services/permission/valve/rules-map.ts omits RECORD_ACTION.PATCH_MULTI from RULES_MAP. When an authenticated user sends a PATCH_MULTI record operation while permission.type is config, getRulesForMessage returns a null rule specification and ConfigPermission.canPerformAction treats the missing specification as an unconditional allow instead of applying RULE_TYPES.WRITE. Any authenticated user can therefore modify arbitrary protected records, corrupt application state, or cause service disruption; deployments using the default permission type none already allow all operations and are not additionally affected. This issue is fixed in version 10.1.1.

### 10. CVE-2026-61628｜lucasdillmann / nginx-ignition
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T15:17:30.290)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T15:17:30.290 / 2026-09-21T15:17:30.290
- **官方描述（原文）**：nginx ignition is a user interface for the nginx web server. Prior to version 2.41.1, `POST /api/users/onboarding/finish` is registered as anonymous (unauthenticated) and creates a user with full ReadWrite admin permissions. Because the handler uses a check-then-act (TOCTOU) pattern between the "onboarding already completed?" check and the user-creation write, with no atomic guard, a remote unauthenticated attacker who can reach an instance in its pre-onboarding state can create an administrator account for themselves — and concurrent requests can create multiple admin accounts in a single race. Version 2.41.1 patches the issue.

### 11. CVE-2026-55897｜openwrt / luci
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T20:17:26.670)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T20:17:26.670 / 2026-09-21T21:17:05.723
- **官方描述（原文）**：luci-app-advanced-reboot is a LuCI (web interface) application for OpenWrt that provides a way to reboot your router into an alternative firmware partition or perform reboot operations directly from the web UI. Prior to 1.1.2-6, the luci-app-advanced-reboot read ACL in applications/luci-app-advanced-reboot/root/usr/share/rpcd/acl.d/luci-app-advanced-reboot.json grants rpcd file.exec permission for the general shell interpreter /bin/sh. An authenticated delegated session with that read ACL can supply caller-controlled params; rpcd authorizes the executable path and passes those arguments to the shell, allowing arbitrary commands to execute as root. Builds without the /bin/sh exec grant, including the checked openwrt-24.10 and openwrt-23.05 branches, are not affected by this specific chain. This vulnerability is fixed in 1.1.2-6.

### 12. CVE-2026-55567｜bleachbit / bleachbit
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T15:17:29.793)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T15:17:29.793 / 2026-09-21T16:17:09.557
- **官方描述（原文）**：BleachBit cleans files to free disk space and to maintain privacy. Prior to 6.0.1, privileged Windows cleaning does not lock and validate a target's parent directory before deletion. A local unprivileged user can replace that directory with a Windows junction and use a native symlink to redirect the elevated deletion to an attacker-selected file. The arbitrary privileged file deletion can be combined with Windows Installer behavior to obtain local SYSTEM privileges. This issue is fixed in version 6.0.1.

### 13. CVE-2026-55563｜feast-dev / feast
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T16:17:09.390)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.9 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T16:17:09.390 / 2026-09-21T18:17:08.923
- **官方描述（原文）**：Feast is the open source feature store for AI and machine learning. Prior to 0.65.0, .github/workflows/pr_integration_tests.yml uses pull_request_target with the synchronize event and preserves ok-to-test, approved, or lgtm labels across newly pushed commits, allowing a fork contributor to obtain approval for a benign revision and then run changed code from refs/pull/${{ github.event.pull_request.number }}/merge through privileged make targets. The job exposes GCP, AWS, and Snowflake credentials to that code, enabling runner code execution, credential disclosure, and possible access to downstream cloud resources. An external label-removal integration could mitigate the condition, but no repository workflow provided that protection. This issue is fixed in version 0.65.0.

### 14. CVE-2026-55071｜SepineTam / mcp-for-stata
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T15:17:29.450)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T15:17:29.450 / 2026-09-21T15:17:29.450
- **官方描述（原文）**：MCP-for-Stata is a MCP server for integrating Stata into agent loops with a safety-first design. Prior to version 1.19.0, the ado_package_install MCP tool in stata-mcp concatenates user-controlled input directly into a Stata command string without any validation or sanitization. An attacker who can invoke the MCP tool or the equivalent Python API can embed newline characters in the package argument to inject arbitrary Stata commands. Because Stata supports a shell escape command, this leads to full OS-level arbitrary command execution (RCE) under the account running the Stata-MCP server. The tool is registered in the default all profile, so no non-default configuration is required. This issue has been patched in version 1.19.0.

### 15. CVE-2026-53940｜conda / conda
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T16:17:09.010)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T16:17:09.010 / 2026-09-21T19:17:06.670
- **官方描述（原文）**：Conda is a system-level binary package and environment manager that runs on major operating systems and platforms. Prior to 26.5.2, parse_entry_point_def in conda/common/path/python.py accepted an unvalidated entry-point command from a noarch:python package's info/link.json metadata. CreatePythonEntryPointAction in conda/core/path_actions.py interpolated that command into target_short_path, and PrefixPathAction.target_full_path joined it to the installation prefix without verifying that the result remained under the intended bin or Scripts directory. create_python_entry_point in conda/gateways/disk/create.py then wrote an executable wrapper to the resulting path. A malicious package could use path separators, traversal segments, or an absolute command path to write outside the prefix or overwrite another in-prefix entry point during default install and environment transactions. Out-of-prefix writes require the target parent directory to exist, while an overwritten entry point can execute attacker-controlled Python when later invoked with the installing user's privileges. This issue is fixed in version 26.5.2.

### 16. CVE-2026-52835｜Tautulli / Tautulli
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T20:17:26.140)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.0 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T20:17:26.140 / 2026-09-21T20:17:26.280
- **官方描述（原文）**：Tautulli is a Python based monitoring and tracking tool for Plex Media Server. Prior to 2.17.2, the import_config handler and the database_file branch of import_database in plexpy/webserve.py join the attacker-controlled config_file.filename or database_file.filename directly to CACHE_DIR without basename reduction or a containment check. An administrator or caller with the instance API key can submit a multipart filename containing parent-directory segments, causing the upload to be created or overwritten outside CACHE_DIR before file-content validation runs. The write is limited to paths permitted to the Tautulli process, but it can enable configuration tampering, service disruption, or code execution. This issue is fixed in version 2.17.2.

### 17. CVE-2026-94572｜OpenStack / Octavia
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T21:17:22.150)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T21:17:22.150 / 2026-09-21T21:17:22.150
- **官方描述（原文）**：In OpenStack Octavia before 18.0.1, the Amphora provider driver did not validate the listener and pool tls_ciphers field for control characters. The value is written verbatim into the HAProxy configuration generated on the amphora, and thus an authenticated project member who owns a TLS-enabled load balancer can embed a newline and inject arbitrary HAProxy configuration directives. Only deployments using the Amphora provider are affected.

### 18. CVE-2026-94571｜OpenStack / Octavia
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T21:17:21.970)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T21:17:21.970 / 2026-09-21T21:17:21.970
- **官方描述（原文）**：In OpenStack Octavia before 18.0.1, the Amphora provider driver did not reject control characters in the L7 policy redirect_url and redirect_prefix fields. The RFC 3986 URL validator percent-encodes control characters before validating, and thus newlines passed structural checks, but Octavia stored and wrote the raw unencoded value directly into the HAProxy configuration generated on the amphora. An authenticated project member who owns a load balancer can therefore inject arbitrary HAProxy directives through a REDIRECT_TO_URL L7 policy. Only deployments using the Amphora provider are affected.

### 19. CVE-2026-94493｜Gigatech / PDV5701
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T01:16:56.437)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T01:16:56.437 / 2026-09-22T01:16:56.437
- **官方描述（原文）**：A vulnerability was detected in Gigatech PDV5701 1.0.31_240305_112640. This issue affects some unknown processing of the file /index.html of the component WebSocket Service. The manipulation results in missing authentication. The attack can be launched remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 20. CVE-2026-94425｜Moore Threads / MTT S80 Driver Package
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T23:16:56.697)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T23:16:56.697 / 2026-09-21T23:16:56.697
- **官方描述（原文）**：A vulnerability was found in Moore Threads MTT S80 Driver Package 340.150. The affected element is the function sub_140006F0C in the library mtdispkm64.sys of the component IOCTL Handler. The manipulation results in improper privilege management. Attacking locally is a requirement. The vendor was contacted early about this disclosure but did not respond in any way.

### 21. CVE-2026-94424｜Moore Threads / MTT S80 Driver Package
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T21:17:21.793)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T21:17:21.793 / 2026-09-21T21:17:21.793
- **官方描述（原文）**：A vulnerability has been found in Moore Threads MTT S80 Driver Package up to 340.150. Impacted is the function sub_140001000 in the library mtdispkm64.sys of the component IOCTL Handler. The manipulation leads to heap-based buffer overflow. An attack has to be approached locally. The vendor was contacted early about this disclosure but did not respond in any way.

### 22. CVE-2026-94301｜Apache Software Foundation / Apache MINA
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T15:17:38.903)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T15:17:38.903 / 2026-09-22T04:18:02.810
- **官方描述（原文）**：The fix for CVE-2026-47065/ZDRES-232 ("resolveProxyClass Not Overridden - acceptMatchers Filter Bypass via java.lang.reflect.Proxy"), released on 2026-06-02 and announced as "Fully addressed" in MINA 2.2.8, 2.1.13 and 2.0.29, was committed to the 2.2.X branch only. The 2.0.X and 2.1.X maintenance branches never received the resolveProxyClass() override, so the 2.0.29 and 2.1.13 artifacts listed as fixed -- and every later release on those lines, up to and including the current 2.0.30 and 2.1.14 -- remain vulnerable to the exact allow-list bypass that CVE-2026-47065 was meant to close.

### 23. CVE-2026-86473｜Apache Software Foundation / Apache Airflow
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T15:17:32.997)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T15:17:32.997 / 2026-09-21T19:17:13.880
- **官方描述（原文）**：Apache Airflow: the Core API logout endpoint revokes only a session token presented as the _token cookie. When a client logs out presenting its credential as an Authorization bearer header instead, the endpoint returns its normal logout response but revokes nothing, so the token remains valid until it expires. An attacker who already holds a copy of that token keeps the victim's access after the victim has logged out and believes the session ended; the default token lifetime is 24 hours and is configurable. Affects API clients that authenticate with a bearer token rather than the browser session cookie. The attacker must already possess a copy of a valid token; obtaining one is outside the scope of this issue, and no privileges beyond the victim's own are gained. Users of apache-airflow are recommended to upgrade to apache-airflow version 3.3.2 or later, which fixes the issue.

### 24. CVE-2026-85751｜Mailu / Mailu
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T16:17:25.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T16:17:25.070 / 2026-09-21T18:17:11.697
- **官方描述（原文）**：Mailu is a mail server distributed as a set of Docker images. From Mailu 2.0 until 2024.06.55 and prior to Mailu helm-charts 2.7.3, deployments with PROXY_AUTH_WHITELIST configured but REAL_IP_HEADER unset trusted a client-controlled X-Forwarded-By header for header-based proxy authentication. The proxy_hide_header directive in the nginx template at core/nginx/conf/proxy.conf hid the header from upstream responses but did not overwrite the incoming request value in this configuration. An unauthenticated remote attacker could therefore spoof the trusted proxy identity and bypass authentication. This issue is fixed in Mailu 2024.06.55 and Mailu helm-charts 2.7.3.

### 25. CVE-2026-82187｜Unknown / Web to Print Online Designer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T07:16:53.317)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00145 / percentile=0.04187
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T07:16:53.317 / 2026-09-21T15:17:32.223
- **官方描述（原文）**：The Web to Print Online Designer WordPress plugin before 2.15.0 does not validate the type or extension of uploaded files, and hands the token protecting those uploads to any visitor who asks for it, allowing unauthenticated attackers to upload arbitrary files, including PHP ones, and run code on the server.

### 26. CVE-2026-79920｜ajenti / ajenti
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T17:18:59.567)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T17:18:59.567 / 2026-09-21T19:17:11.323
- **官方描述（原文）**：Ajenti is a Linux & BSD modular server admin panel. Prior to version 2.2.16, any authenticated user can call /api/core/tasks/start to enqueue InstallPlugin, UnInstallPlugin, or UpgradeAll from plugins/plugins/tasks.py without plugin-management authorization. InstallPlugin and UnInstallPlugin construct a pip package specification from unvalidated name and version fields, and the task worker invokes pip while running as root. A low-privileged user can therefore select or manipulate a package installed with root privileges and can install, remove, or upgrade plugins without administrative permission, resulting in root code execution and full host compromise. This issue is fixed in version 2.2.16.

### 27. CVE-2026-79916｜1Panel-dev / MaxKB
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T21:17:12.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T21:17:12.450 / 2026-09-21T21:17:12.580
- **官方描述（原文）**：MaxKB is an open-source AI assistant for enterprise. Prior to 2.10.5-lts, authenticated workspace members can inject control characters into AWS Bedrock access_key_id and secret_access_key fields that _update_aws_credentials writes to /root/.aws/credentials without safe parsing. An attacker can append a new AWS profile containing credential_process, then select that profile during a later model-validation request so botocore executes an attacker-controlled command as root. This vulnerability is fixed in 2.10.5-lts.

### 28. CVE-2026-77521｜1Panel-dev / MaxKB
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T21:17:10.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T21:17:10.943 / 2026-09-21T21:17:11.083
- **官方描述（原文）**：MaxKB is an open-source AI assistant for enterprise. Prior to version 2.10.5-lts, assistants with a tool, MCP tool, skill, or sub-application use SandboxShellBackend, which exposes an execute shell tool without excluding it and omits execute from interrupt_on, so human approval is not required. Untrusted chat or ingested content can therefore cause command execution; source deployments with MAXKB_SANDBOX disabled run commands directly as the application user, while the official root container's string-based gosu wrapper allowed shell metacharacters to execute outside the intended sandbox. This issue is fixed in version 2.10.5-lts.

### 29. CVE-2026-58491｜warp-tech / warpgate
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T19:17:06.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T19:17:06.910 / 2026-09-21T19:17:06.910
- **官方描述（原文）**：Warpgate is an open source SSH, HTTPS and MySQL bastion host for Linux. Prior to 0.25.5, the /@warpgate/api/sso/providers/:name/start endpoint stores an attacker-controlled next parameter that the POST /@warpgate/api/sso/return handler inserts without HTML escaping into the response generated by warpgate-protocol-http/src/api/sso_provider_list.rs. A victim who follows a crafted link and completes SSO can cause markup and JavaScript to execute in the authenticated Warpgate origin, allowing access to session data and actions through user APIs, and through administrator APIs only when the victim is an administrator. The GET /@warpgate/api/sso/return path also uses the same unvalidated value as a redirect destination, enabling an open redirect. This issue is fixed in version 0.25.5.

### 30. CVE-2026-46649｜laurent22 / joplin
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T21:17:03.323)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T21:17:03.323 / 2026-09-21T21:17:03.323
- **官方描述（原文）**：Joplin is an open source note-taking and to-do application that organises notes and lists into notebooks. Prior to 3.7.2, Joplin Server's GET /api/login_with_code/:id endpoint accepts a nine-digit SSO authentication code with a ten-minute lifetime without applying limiterLoginBruteForce. An unauthenticated attacker who targets a user during an active SSO login can make unlimited guesses, and a correct code returns a full session token that permits access to and modification of the user's notes, notebooks, and account settings. This issue is fixed in version 3.7.2.

### 31. CVE-2026-19658｜LiquidWeb / Give Tributes
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T05:16:55.167)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T05:16:55.167 / 2026-09-22T05:16:55.167
- **官方描述（原文）**：The Give Tributes plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 2.3.1 via deserialization of untrusted input . This makes it possible for unauthenticated attackers to inject a PHP Object. No known POP chain is present in the vulnerable software, which means this vulnerability has no impact unless another plugin or theme containing a POP chain is installed on the site. If a POP chain is present via an additional plugin or theme installed on the target system, it may allow the attacker to perform actions like delete arbitrary files, retrieve sensitive data, or execute code depending on the POP chain present. This vulnerability is only reachable when the "Allow Multiple Recipients" option is enabled for the donation form, as the single-recipient code path applies sanitize_textarea_field() which would neutralize the payload. Exploitation additionally requires the eCard "Custom Message" option to be disabled, which is the plugin default: when it is enabled the personalized message becomes a required field and GiveWP's give_clean() blanks serialized input during validation, causing the donation to be rejected before it is stored.

### 32. CVE-2026-13355｜Meta Box / Meta Box Frontend Submission
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T05:16:54.960)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T05:16:54.960 / 2026-09-22T05:16:54.960
- **官方描述（原文）**：The Meta Box AIO plugin for WordPress is vulnerable to Privilege Escalation to Administrator in versions up to, and including, 3.11.0. This is due to a chained flaw: the populate_via_query_string() function in the mb-frontend-submission component unconditionally overrides the form's target object_id from the GET parameter 'rwmb_frontend_field_object_id' without any authorization check, and Form::process() lacks the user_can_edit() check present in render(), allowing unauthenticated attackers to overwrite the post_content of any page with an arbitrary shortcode via wp_update_post(); the mb-user-profile component then directly trusts the 'role' and 'auto_login' shortcode attributes in the injected [mb_user_profile_register] shortcode with no role validation. This makes it possible for unauthenticated attackers to elevate their privileges to Administrator. The standalone plugins Meta Box Frontend Submission (in versions up to 4.5.6) and Meta Box User Profile (versions up to 3.11.0) are also affected.

### 33. CVE-2026-94494｜jishenghua / jshERP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T19:17:20.993)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T19:17:20.993 / 2026-09-21T20:17:41.550
- **官方描述（原文）**：jshERP through 3.6 contains a tenant isolation bypass vulnerability that allows authenticated users to read other tenants' records via the GET /tenant/info endpoint. Attackers can iterate the primary key to enumerate and access sensitive tenant data including login names, validity dates, user quotas, and enabled state across all platform tenants.

### 34. CVE-2026-94414｜jishenghua / jshERP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T19:17:20.800)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T19:17:20.800 / 2026-09-21T19:17:20.800
- **官方描述（原文）**：jshERP through 3.6 is missing an authorization check on the POST /userBusiness/updateBtnStr endpoint that allows authenticated users to modify role button-permission definitions. Attackers can supply arbitrary roleId and btnStr parameters to overwrite button-permission configurations for any role in the tenant without privilege validation.

### 35. CVE-2026-94151｜Omega Solution / HRM OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T09:17:06.567)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00394 / percentile=0.3339
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T09:17:06.567 / 2026-09-21T16:17:29.307
- **官方描述（原文）**：A weakness has been identified in Omega Solution HRM OS up to 20260717. This affects an unknown function of the file /role-permission/permission of the component Role Permission API. Executing a manipulation of the argument roleId can lead to missing authentication. The attack may be launched remotely. The exploit has been made available to the public and could be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 36. CVE-2026-94148｜未確認 / ScadaBR
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T08:16:38.987)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00314 / percentile=0.24488
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T08:16:38.987 / 2026-09-21T20:17:41.100
- **官方描述（原文）**：A vulnerability was determined in ScadaBR up to 1.1. Impacted is the function EmportDwr.createExportJSON of the file /ScadaBR/export_project.htm of the component Export Project Endpoint. This manipulation causes information disclosure. The attack can be initiated remotely. The exploit has been publicly disclosed and may be utilized. Upgrading to version 1.2.0 is recommended to address this issue. Patch name: c852b4988a15bce6011ef169299ad604538f70a9. The affected component should be upgraded. Import path was already gated with Permissions.ensureAdmin(); only export was left unprotected.

### 37. CVE-2026-94143｜drogonframework / drogon
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T06:17:02.003)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00254 / percentile=0.17198
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T06:17:02.003 / 2026-09-21T22:16:59.717
- **官方描述（原文）**：A vulnerability was detected in drogonframework drogon up to 1.9.13. Affected by this issue is the function Mapper::orderBy in the library Mapper.h of the component ORM Mapper. Performing a manipulation of the argument sort results in sql injection. The attack is possible to be carried out remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 38. CVE-2026-77165｜Nextcloud / Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T16:17:23.863)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T16:17:23.863 / 2026-09-21T19:17:10.713
- **官方描述（原文）**：File owners were unable to unlock TYPE_TOKEN locks placed by other users, leaving files permanently locked with no recovery path outside of the database.

### 39. CVE-2026-63373｜jgraph / drawio
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T17:17:39.367)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.2 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T17:17:39.367 / 2026-09-21T18:17:09.987
- **官方描述（原文）**：draw.io is a configurable diagramming and whiteboarding application. Prior to version 30.2.7, the OAuth callback handler in src/main/java/com/mxgraph/online/AbsAuth.java skips comparison of stateToken and cookieToken whenever IS_GAE is false, which affects self-hosted Docker and WAR deployments. An attacker can provide an authorization code for the attacker's cloud-storage identity and induce a victim to visit a callback URL, causing the victim's draw.io session to become authenticated as the attacker identity without a valid state binding. The shared handler affects Google Drive, OneDrive, GitHub, GitLab, and Dropbox integrations. The victim can then unknowingly perform cloud-storage actions under the attacker's identity, causing session integrity loss and misattribution, but the identity binding does not itself grant access to existing victim cloud files. This issue is fixed in version 30.2.7.

### 40. CVE-2026-63334｜jgraph / drawio
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T17:17:39.220)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T17:17:39.220 / 2026-09-21T19:17:08.587
- **官方描述（原文）**：draw.io is a configurable diagramming and whiteboarding application. Prior to version 30.2.7, deployments with ENABLE_DRAWIO_PROXY=1 are vulnerable to server-side request forgery because src/main/java/com/mxgraph/online/Utils.java performs the private-address check in Utils.sanitizeUrl() using one DNS resolution, while src/main/java/com/mxgraph/online/ProxyServlet.java later calls URL.openConnection() and performs a second resolution. An attacker-controlled hostname can resolve to a public address during validation and then to a private, link-local, or cloud metadata address when the connection is opened. Successful exploitation can return cloud instance metadata or responses from internal HTTP services through the proxy. This issue is fixed in version 30.2.7.

### 41. CVE-2026-62987｜fabiolb / fabio
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T17:17:38.340)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T17:17:38.340 / 2026-09-21T19:17:08.173
- **官方描述（原文）**：Fabio is an HTTP(S) and TCP router for deploying applications managed by consul. From 1.6.6 until 1.7.2, the CVE-2025-48865 fix in proxy/http_headers.go uses protectHeaders for a hardcoded set of forwarded headers but omits the operator-configured ClientIPHeader, TLSHeader, and RequestID names. In proxy/http_proxy.go, HTTPProxy.ServeHTTP calls addHeaders to set these trust headers before Go ReverseProxy processes the inbound Connection header, allowing an unauthenticated client to name and remove the configured headers before the request reaches the backend. Deployments that enable the corresponding proxy.header options can therefore lose client-IP, TLS-termination, or request-correlation signals used by backend authorization and auditing; the options are empty by default, and the hardcoded protected forwarded headers are unaffected. This issue is fixed in version 1.7.2.

### 42. CVE-2026-62866｜TomWright / dasel
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T17:17:38.053)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.2 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T17:17:38.053 / 2026-09-21T18:17:09.753
- **官方描述（原文）**：Dasel is a command-line tool and library for querying, modifying, and transforming data structures. From 3.0.0 until 3.11.2, selector/lexer/tokenize.go parseCurRune advances the input index across trailing whitespace and then reads the source at the exhausted index without an end-of-input check. A selector ending in whitespace, including input passed through lexer.NewTokenizer(...).Tokenize() or dasel.Query, can therefore cause an index-out-of-range panic and terminate the process. This issue is fixed in version 3.11.2.

### 43. CVE-2026-61746｜inventree / InvenTree
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T19:17:07.453)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T19:17:07.453 / 2026-09-21T20:17:27.343
- **官方描述（原文）**：InvenTree is an Open Source Inventory Management System. Prior to 1.4.0, PluginSettingList, PluginAllSettingList, and PluginSettingDetail set GlobalSettingsPermissions without the IsAuthenticated permission used by the project default and equivalent global-settings endpoints. GlobalSettingsPermissions returns true for safe methods, while AuthRequiredMiddleware exempts /api/ paths, so an unauthenticated caller can retrieve plugin names, setting keys, descriptions, types, choices, and non-protected configuration values through /api/plugin/settings/ and the per-plugin settings endpoints. Protected secret values remain masked as three asterisks, limiting the issue to metadata and non-secret configuration disclosure. This issue is fixed in version 1.4.0.

### 44. CVE-2026-61745｜inventree / InvenTree
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T18:17:09.253)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T18:17:09.253 / 2026-09-21T19:17:07.343
- **官方描述（原文）**：InvenTree is an Open Source Inventory Management System. Prior to 1.4.0, the POST /api/machine/{pk}/restart/ endpoint in src/backend/InvenTree/machine/api.py uses IsAuthenticatedOrReadScope without requiring the ADMIN role used by other machine management operations. Any authenticated user who lacks the ADMIN role, including a warehouse user with only the STOCK role, can cause MachineRestart to invoke registry.restart_machine() for any registered machine, resetting its status and interrupting active printing, scanning, or other machine operations. This issue is fixed in version 1.4.0.

### 45. CVE-2026-48521｜envoyproxy / envoy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T20:17:25.463)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T20:17:25.463 / 2026-09-21T20:17:25.463
- **官方描述（原文）**：Envoy is an open source edge and service proxy designed for cloud-native applications. Prior to 1.36.10, 1.37.6, 1.38.4, and 1.39.1, Envoy's ProdClusterManagerFactory::allocateConnPool dereferences transport_socket_options while selecting an HTTP/3 connection pool without first checking whether the pointer is null. LoadBalancerContext implementations used by synthetic, mirror, health-check, and async-client calls can return no transport-socket options. With auto_config and HTTP/3 enabled, routine traffic reaching one of those contexts can crash an Envoy worker. The relevant scope boundary is that the affected branch requires HTTP/3 in the protocol set and a context that supplies no transport-socket options. This issue is fixed in versions 1.36.10, 1.37.6, 1.38.4, and 1.39.1.

### 46. CVE-2025-71420｜uvdesk / core-framework
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T14:17:14.720)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T14:17:14.720 / 2026-09-21T15:17:27.707
- **官方描述（原文）**：UVdesk core-framework before 1.1.7 contains an authorization bypass vulnerability in the saved reply endpoint that allows authenticated agents to access replies restricted to other support groups. Attackers with ROLE_AGENT can enumerate saved reply identifiers and read content reserved for groups and teams they do not belong to.

### 47. CVE-2026-94382｜henrygd / beszel
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T14:17:30.170)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T14:17:30.170 / 2026-09-21T15:17:39.290
- **官方描述（原文）**：Beszel before 0.19.0 contains an insecure direct object reference vulnerability in the POST and DELETE /api/beszel/user-alerts handlers that allows any authenticated user to create or delete alerts on systems they cannot access. Attackers can supply arbitrary system IDs in the request body to register alert rules and receive notifications disclosing target system names and metrics.

### 48. CVE-2026-94216｜ST Engineering iDirect / Evolution
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T13:17:12.360)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T13:17:12.360 / 2026-09-21T16:17:29.547
- **官方描述（原文）**：A vulnerability was determined in ST Engineering iDirect Evolution and Velocity WebServer Evolution up to 20260717. This vulnerability affects the function authorize of the file /usr/sbin/webserver of the component HTTP Header Handler. Executing a manipulation of the argument Success can lead to open redirect. It is possible to launch the attack remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 49. CVE-2026-94211｜Hyve5 / Leantime
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T13:17:11.953)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T13:17:11.953 / 2026-09-21T15:17:38.767
- **官方描述（原文）**：A vulnerability has been found in Hyve5 Leantime up to 3.9.8. Affected by this issue is some unknown functionality of the file /app/Domain/Dashboard/Templates/show.blade.php of the component Project Dashboard. Such manipulation leads to cross site scripting. The attack may be performed from remote. The exploit has been disclosed to the public and may be used. "EDIT perm" needed to plant; fires cross-user for anyone viewing the project dashboard since the poisoned label name is echoed raw. The vendor was contacted early about this disclosure but did not respond in any way.

### 50. CVE-2026-94210｜Hyve5 / Leantime
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T12:17:27.177)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T12:17:27.177 / 2026-09-21T20:17:41.407
- **官方描述（原文）**：A flaw has been found in Hyve5 Leantime up to 3.9.8. Affected by this vulnerability is the function getAllGrouped of the file app/Domain/Tickets/Services/Tickets.php of the component Kanban Board. This manipulation causes cross site scripting. The attack is possible to be carried out remotely. The exploit has been published and may be used. Patch name: a30a6837b4071ac05a4f58d0e1baa2c62aa8695e. To fix this issue, it is recommended to deploy a patch.

### 51. CVE-2026-94149｜Omega Solution / HRM OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T08:16:39.190)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00221 / percentile=0.12937
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T08:16:39.190 / 2026-09-21T13:33:33.387
- **官方描述（原文）**：A vulnerability was identified in Omega Solution HRM OS up to 20260717. The affected element is an unknown function of the file /role-permission/permission of the component Role Permission Retrieval Endpoint. Such manipulation of the argument roleId leads to improper control of resource identifiers. The attack can be launched remotely. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 52. CVE-2026-94145｜xuxueli / xxl-job
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T07:16:53.810)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：0.00191 / percentile=0.09011
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T07:16:53.810 / 2026-09-21T16:17:29.170
- **官方描述（原文）**：A vulnerability has been found in xuxueli xxl-job up to 3.4.2/3.5.0. This vulnerability affects unknown code of the file xxl-job-admin/src/main/java/com/xxl/job/admin/business/controller/JobInfoController.java of the component Task Management Interface. The manipulation of the argument name/author leads to cross site scripting. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 53. CVE-2026-92612｜Eclipse Foundation / Eclipse iceoryx™
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T11:17:12.590)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T11:17:12.590 / 2026-09-21T18:11:49.423
- **官方描述（原文）**：In Eclipse iceoryx2 versions greater than v0.8.0, the StaticString exposes its contents as mutable bytes through safe APIs, while String::as_str() converts those bytes into a Rust string slice without validating UTF-8. An application can therefore create an invalid &str and trigger undefined behavior using entirely safe Rust.

### 54. CVE-2026-77166｜Nextcloud / Collectives
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T16:17:24.013)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 2.4 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T16:17:24.013 / 2026-09-21T19:17:10.840
- **官方描述（原文）**：The emoji field in the page emoji update endpoint does not properly validate user input. By injecting long text and line breaks, the sidebar layout becomes broken and can hide other items.

### 55. CVE-2026-81627｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：CVSS_CHANGED (from=6.7; to=8.2)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T11:17:18.490 / 2026-09-21T12:17:20.197
- **官方描述（原文）**：A flaw was found in QEMU. The VAPIC setup hypercall in hw/i386/vapic.c does not validate that the writable RAM alias remains within the option ROM window. A privileged guest user on a Q35/KVM machine can position this alias over locked SMRAM, bypassing chipset D_LCK protection and injecting code into System Management Mode memory.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-7273｜Zyxel / GS1900 Series Switches
- **Title**：Zyxel GS1900 Series Switches Stack-Based Buffer Overflow Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00315 / percentile=0.24603
- **CISA KEV**：listed=true / date_added=2026-09-21 / due_date=2026-09-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Zyxel GS1900 series switches contain a stack-based buffer overflow vulnerability in the CGI program which could allow a LAN-based, unauthenticated attacker to exploit the flaw and potentially execute OS commands via a crafted HTTP request.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-61674 | P3 / 38 | fluent / fluent-bit | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2025-12999 | P3 / 38 | Eclipse Foundation / Eclipse Open VSX | v4.0 9.1 (CRITICAL) | 0.00405 / percentile=0.34452 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-94501 | WATCH / 30 | jishenghua / jshERP | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-94496 | WATCH / 30 | jishenghua / jshERP | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-94488 | WATCH / 30 | Telegram / Telegram Desktop | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-94412 | WATCH / 30 | jishenghua / jshERP | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-73546 | WATCH / 30 | envoyproxy / envoy | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63116 | WATCH / 30 | deepstreamIO / deepstream.io | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-61628 | WATCH / 30 | lucasdillmann / nginx-ignition | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55897 | WATCH / 30 | openwrt / luci | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55567 | WATCH / 30 | bleachbit / bleachbit | v3.1 7.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55563 | WATCH / 30 | feast-dev / feast | v4.0 8.9 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55071 | WATCH / 30 | SepineTam / mcp-for-stata | v3.1 8.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-53940 | WATCH / 30 | conda / conda | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-52835 | WATCH / 30 | Tautulli / Tautulli | v4.0 7.0 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-94572 | WATCH / 28 | OpenStack / Octavia | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94571 | WATCH / 28 | OpenStack / Octavia | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94493 | WATCH / 28 | Gigatech / PDV5701 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94425 | WATCH / 28 | Moore Threads / MTT S80 Driver Package | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94424 | WATCH / 28 | Moore Threads / MTT S80 Driver Package | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94301 | WATCH / 28 | Apache Software Foundation / Apache MINA | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-86473 | WATCH / 28 | Apache Software Foundation / Apache Airflow | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-85751 | WATCH / 28 | Mailu / Mailu | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-82187 | WATCH / 28 | Unknown / Web to Print Online Designer | v3.1 9.8 (CRITICAL) | 0.00145 / percentile=0.04187 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-79920 | WATCH / 28 | ajenti / ajenti | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-79916 | WATCH / 28 | 1Panel-dev / MaxKB | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-77521 | WATCH / 28 | 1Panel-dev / MaxKB | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-58491 | WATCH / 28 | warp-tech / warpgate | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-46649 | WATCH / 28 | laurent22 / joplin | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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
- EPSS 未確認：27；Exploitation status 未確認：9。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-22T05:38:29.007634+00:00`；Delta generated at：`2026-09-22T05:38:29.007634+00:00`。

---

## 可驗證資料來源

- **CVE-2026-7273** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-7273) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-7273) · [Vendor / Advisory (zyxel.com)](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-61674** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61674)
- **CVE-2025-12999** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-12999) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-12999)
- **CVE-2026-94501** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94501)
- **CVE-2026-94496** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94496)
- **CVE-2026-94488** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94488)
- **CVE-2026-94412** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94412)
- **CVE-2026-73546** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73546)
- **CVE-2026-63116** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63116)
- **CVE-2026-61628** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61628)
- **CVE-2026-55897** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55897)
- **CVE-2026-55567** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55567)
- **CVE-2026-55563** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55563)
- **CVE-2026-55071** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55071)
- **CVE-2026-53940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53940)
- **CVE-2026-52835** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-52835)
- **CVE-2026-94572** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94572)
- **CVE-2026-94571** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94571)
- **CVE-2026-94493** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94493)
- **CVE-2026-94425** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94425)
- **CVE-2026-94424** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94424)
- **CVE-2026-94301** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94301)
- **CVE-2026-86473** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86473)
- **CVE-2026-85751** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85751)
- **CVE-2026-82187** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82187) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-82187)
- **CVE-2026-79920** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79920)
- **CVE-2026-79916** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79916)
- **CVE-2026-77521** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77521)
- **CVE-2026-58491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58491)
- **CVE-2026-46649** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46649)
- **CVE-2026-19658** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19658)
- **CVE-2026-13355** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13355)
- **CVE-2026-94494** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94494)
- **CVE-2026-94414** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94414)
- **CVE-2026-94151** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94151) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-94151)
- **CVE-2026-94148** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94148) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-94148)
- **CVE-2026-94143** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94143) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-94143)
- **CVE-2026-77165** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77165)
- **CVE-2026-63373** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63373)
- **CVE-2026-63334** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63334)
- **CVE-2026-62987** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62987)
- **CVE-2026-62866** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62866)
- **CVE-2026-61746** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61746)
- **CVE-2026-61745** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61745)
- **CVE-2026-48521** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48521)
- **CVE-2025-71420** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-71420)
- **CVE-2026-94382** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94382)
- **CVE-2026-94216** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94216)
- **CVE-2026-94211** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94211)
- **CVE-2026-94210** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94210)
- **CVE-2026-94149** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94149) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-94149)
- **CVE-2026-94145** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94145) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-94145)
- **CVE-2026-92612** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92612)
- **CVE-2026-77166** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77166)
- **CVE-2026-81627** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81627)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
