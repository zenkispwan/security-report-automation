# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**68** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=63、NEW_KEV=5。
- Intelligence 候選：**30** 筆；P1 **5**、P2 **0**、P3 **5**、WATCH **20**。
- Baseline：state / generated_at=2026-10-08T06:51:07.715417+00:00 / available=true。
- 目前排序最前的 P1：CVE-2021-3199、CVE-2016-3081、CVE-2015-3306、CVE-2015-5477、CVE-2023-22894。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **68** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2021-3199｜ONLYOFFICE / Docs
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.08215 / percentile=0.9475
- **CISA KEV**：listed=true / date_added=2026-10-08 / due_date=2026-10-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2021-01-26T18:16:28.507 / 2026-10-09T04:18:02.710
- **官方描述（原文）**：ONLYOFFICE Docs contains a path traversal vulnerability that can occur when JWT is used, via a /.. sequence in an image upload parameter and could allow for remote code execution.

### 2. CVE-2016-3081｜Apache / Struts
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.93352 / percentile=0.99838
- **CISA KEV**：listed=true / date_added=2026-10-08 / due_date=2026-10-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2016-04-26T14:59:02.207 / 2026-10-09T04:18:01.843
- **官方描述（原文）**：Apache Struts contains a command injection vulnerability that could allow remote attackers to execute arbitrary code via method:prefix when Dynamic Method Invocation is enabled.

### 3. CVE-2015-3306｜ProFTPD / ProFTPD
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-08 / due_date=2026-10-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2015-05-18T15:59:10.743 / 2026-10-09T04:17:53.027
- **官方描述（原文）**：ProFTPD contains an improper access control vulnerability that could allow remote attackers to read and write to arbitrary files via the site cpfr and site cpto commands.

### 4. CVE-2015-5477｜ISC / BIND
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-08 / due_date=2026-10-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2015-07-29T14:59:05.397 / 2026-10-09T04:18:00.970
- **官方描述（原文）**：ISC BIND contains a data processing errors vulnerability that could allow remote attackers to cause a denial of service via TKEY queries.

### 5. CVE-2023-22894｜Strapi / Strapi
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 4.9 (MEDIUM)
- **EPSS**：0.01658 / percentile=0.7591
- **CISA KEV**：listed=true / date_added=2026-10-08 / due_date=2026-10-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2023-04-19T16:15:07.303 / 2026-10-09T04:18:02.983
- **官方描述（原文）**：Strapi contains a cleartext storage of sensitive information vulnerability that could allow attackers with access to the admin panel to discover sensitive user details via the query filter. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version. This vulnerability can be chained with CVE-2023-22621 to achieve remote code execution.

### 6. CVE-2026-95210｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T18:18:33.370)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:18:33.370 / 2026-10-08T21:33:42.423
- **官方描述（原文）**：Improper certificate validation in gnutls v3.8.13 causes the application to accept certificates containing invalid extensions.

### 7. CVE-2026-9209｜mJob / mJobTime
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T15:17:57.677)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T15:17:57.677 / 2026-10-08T21:35:53.890
- **官方描述（原文）**：mJobTime through build 15.7.3.32 contains an unauthenticated SQL execution vulnerability in the Login.aspx admin panel handlers, where the runQueryButton postback and exportSqlQuery_Server PageMethod execute caller-supplied SQL against the backing Sybase SQL Anywhere database using DBA/sysadmin privileges with no server-side authentication enforced beyond a client-side sessionStorage flag. Attackers can submit arbitrary SQL through these exposed endpoints to invoke xp_cmdshell and xp_read_file, achieving pre-authentication remote code execution as LocalSystem via a single HTTP request.

### 8. CVE-2026-107703｜enmaso / @enmaso/node-convert
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T19:17:02.720)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T19:17:02.720 / 2026-10-08T21:35:53.890
- **官方描述（原文）**：@enmaso/node-convert through 1.0.0 contains an OS command injection vulnerability in convert.js that allows attackers to execute shell commands via unsanitized filepath and convertTo arguments. Attackers can inject shell metacharacters or a single quote into the ImageMagick command run by child_process.exec() to execute operating system commands with Node.js process privileges.

### 9. CVE-2026-107640｜Integrics / Enswitch
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T15:17:47.343)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T15:17:47.343 / 2026-10-08T21:35:53.890
- **官方描述（原文）**：Integrics Enswitch 3.13 through 4.4 contains an authentication bypass vulnerability in /api/json/user/password/update/ that allows unauthenticated attackers to change account passwords by omitting the reset parameter. Attackers can target accounts with no pending reset, whose empty reset_key matches the defaulted empty value, to take over administrator accounts after enumerating valid usernames.

### 10. CVE-2026-105110｜Iskratel / Innbox
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T09:16:40.930)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.02788 / percentile=0.85991
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T09:16:40.930 / 2026-10-08T21:35:53.890
- **官方描述（原文）**：OS Command Injection in the login.xgi CGI endpoint in Iskratel Innbox GPON ONT devices allows an unauthenticated remote attacker to execute arbitrary commands as root via the CLI parameter.

### 11. CVE-2026-93858｜OpenStack / Mistral
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T18:18:30.817)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:18:30.817 / 2026-10-08T21:10:41.427
- **官方描述（原文）**：In OpenStack Mistral through 23.0.0, the std.ssh_proxied action passes a caller-supplied proxy_command value directly to paramiko.ProxyCommand() before any SSH connection to a gateway or target host is attempted. An authenticated project member can use the standard action-execution API to submit an arbitrary local command as proxy_command; paramiko starts that command as a subprocess on the executor host under the executor's own service account, independent of whether the SSH connection itself ever succeeds. Only Mistral deployments that permit the std.ssh_proxied action, the default configuration, are affected.

### 12. CVE-2026-107378｜Kozea / CairoSVG
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T18:17:23.417)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:17:23.417 / 2026-10-08T21:33:42.423
- **官方描述（原文）**：CairoSVG is an SVG converter based on Cairo, a 2D graphics library. Prior to 2.9.1, rendering an attacker-controlled SVG with a path containing many segments can cause quadratic CPU consumption in cairosvg/path.py. The path tokenizer repeatedly slices and rescans the remaining path data, while draw_markers drains node.vertices with node.vertices.pop(0), causing repeated linear-time work. The svg2png, svg2pdf, and svg2ps APIs reach these operations during ordinary rendering, allowing a sub-megabyte SVG to consume substantial CPU and deny service to a rendering application. This issue is fixed in version 2.9.1.

### 13. CVE-2026-107376｜webonyx / graphql-php
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T18:17:22.373)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:17:22.373 / 2026-10-08T21:34:48.800
- **官方描述（原文）**：webonyx graphql-php is a PHP implementation of the GraphQL specification. Prior to 15.32.3, GraphQL\Language\Parser performs recursive descent without a recursion limit in parseSelectionSet, parseValueLiteral, and parseTypeReference. A remote attacker can submit deeply nested selection sets, object or list values, or list types that exhaust the PHP process stack during pre-validation parsing, before query validation and complexity controls run. The resulting SIGSEGV can terminate PHP-FPM workers or long-running Swoole, RoadRunner, ReactPHP, or CLI processes and cannot be caught by application-level exception handling. This issue is fixed in version 15.32.3.

### 14. CVE-2026-107362｜CISA / Malcolm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T18:17:21.587)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:17:21.587 / 2026-10-08T21:03:43.847
- **官方描述（原文）**：Malcolm file-upload component ships the upstream FilePond PHP server (pqina/filepond-server-php) largely unmodified: Dockerfile copies all upstream *.php files and Malcolm only overwrites config.php and submit.php. Upstream index.php exposes a fetch API route that instructs the server to download an arbitrary URL with curl (including FOLLOWLOCATION) and, for HEAD requests, stores the fetched response body in the upload container's transfer directory and returns the transfer ID to the caller, enabling full readback of the fetched content.

### 15. CVE-2026-107337｜CISA / Malcolm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T18:17:20.687)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:17:20.687 / 2026-10-08T21:03:43.847
- **官方描述（原文）**：The Malcolm kiosk Flask application exposes a POST /script_call/<script> endpoint with zero authentication and wildcard CORS (CORS(app)). An attacker can force the operator's browser to execute arbitrary management commands via CSRF, including control.py --wipe which permanently deletes all captured network traffic and forensic logs, or control.py --stop which blinds the security monitoring.

### 16. CVE-2026-105830｜thephpleague / commonmark
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T15:17:35.340)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T15:17:35.340 / 2026-10-08T21:33:42.423
- **官方描述（原文）**：league/commonmark from 2.0.0 before 2.10.2 contains a quadratic-time denial of service vulnerability in the GitHub Flavored Markdown Table extension's TableStartParser::tryStart() block-start scan. Unauthenticated attackers can submit a large paragraph of pipe-free lines not starting with letters, forcing repeated full-buffer strpos scans that exhaust PHP worker CPU.

### 17. CVE-2026-96207｜Microsoft / Microsoft Partner Center
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T23:17:05.583)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T23:17:05.583 / 2026-10-08T23:17:05.583
- **官方描述（原文）**：Improper certificate validation in Microsoft Partner Center allows an unauthorized attacker to elevate privileges over a network.

### 18. CVE-2026-94510｜Microsoft / Microsoft Bookings
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T23:17:05.427)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T23:17:05.427 / 2026-10-08T23:17:05.427
- **官方描述（原文）**：Authorization bypass through user-controlled key in Microsoft Bookings allows an unauthorized attacker to elevate privileges over a network.

### 19. CVE-2026-93034｜SGLang / SGLang
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T15:17:57.117)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T15:17:57.117 / 2026-10-08T21:18:03.583
- **官方描述（原文）**：SGLang contains an arbitrary code execution vulnerability caused by the ZMQ message decoder unconditionally deserializing PickleWrapper payloads via pickle.loads() in _maybe_unwrap_pickle without type allowlisting or authentication; this vulnerability persists via the msgpack path even when SGLANG_USE_PICKLE_IPC is disabled, and becomes remotely exploitable if data-parallel attention is enabled with a non-loopback --dist-init-addr setting.

### 20. CVE-2026-92555｜AKIN Software Computer Import-Export Industry and Trade Co. Ltd. / AKINSOFT WOLVOX Control Panel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T12:17:18.787)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T12:17:18.787 / 2026-10-08T20:09:14.010
- **官方描述（原文）**：Insertion of sensitive information into sent data vulnerability in AKIN Software Computer Import-Export Industry and Trade Co. Ltd. AKINSOFT WOLVOX Control Panel allows Pull Data from System Resources. This issue affects AKINSOFT WOLVOX Control Panel: from 26.02.25 before 26.02.26.

### 21. CVE-2026-88131｜Microsoft / Microsoft Dataverse
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T23:17:04.590)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T23:17:04.590 / 2026-10-08T23:17:04.590
- **官方描述（原文）**：Deserialization of untrusted data in Microsoft Dataverse allows an unauthorized attacker to execute code over a network.

### 22. CVE-2026-85097｜Bricksforge / Bricksforge
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T07:16:31.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00312 / percentile=0.22075
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T07:16:31.710 / 2026-10-08T17:24:11.230
- **官方描述（原文）**：The Bricksforge plugin for WordPress is vulnerable to unauthenticated arbitrary file upload in versions up to, and including, 3.1.8.9. This is due to insufficient validation of the attacker-controlled URL field in the 'temporaryFileUploads' parameter during form submission. An unauthenticated attacker can first obtain a valid nonce via the bricksforge_regenerate_nonce AJAX endpoint, then upload a GIF/PHP polyglot file to the temporary upload directory where MIME type validation is correctly performed. Subsequently, the attacker can submit a form with a crafted 'temporaryFileUploads' parameter where the server-side file path points to the validated GIF file, but the attacker-controlled url field ends with a .php extension. This makes it possible for unauthenticated attackers to upload and execute arbitrary PHP code on the server.

### 23. CVE-2026-84272｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T20:17:37.753)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T20:17:37.753 / 2026-10-08T20:49:50.083
- **官方描述（原文）**：IBM Guardium Data Protection 12.1 and 12.2.2 are vulnerable to missing authentication in the edge-controller component. An unauthenticated remote attacker could exploit this vulnerability to execute arbitrary container images and gain control of managed edge clusters.

### 24. CVE-2026-84249｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T22:17:34.213)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T22:17:34.213 / 2026-10-08T22:17:34.213
- **官方描述（原文）**：IBM Guardium Data Protection 12.2, and 12.2.2 could allow a remote attacker to execute arbitrary management operations due to missing authentication for critical function.

### 25. CVE-2026-84244｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T20:17:37.160)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T20:17:37.160 / 2026-10-08T20:49:50.083
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 IBM Security Guardium Data Protection is vulnerable to stored cross-site scripting (XSS) in the Quick Search results grid. An unauthenticated attacker who can influence monitored database traffic could execute malicious script in the browser of an authenticated Guardium user.

### 26. CVE-2026-80381｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T22:17:32.353)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T22:17:32.353 / 2026-10-08T22:17:32.353
- **官方描述（原文）**：IBM Guardium Data Protection 12.0, 12.1, and 12.2 could allow a remote attacker to execute unauthorized SQL statements due to SQL injection.

### 27. CVE-2026-79842｜Hewlett Packard Enterprise / HPE Intelligent Management Center (iMC)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T21:18:03.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T21:18:03.457 / 2026-10-08T21:26:32.080
- **官方描述（原文）**：An authentication bypass vulnerability exists in HPE Intelligent Management Center (iMC) prior to v7.3 E0713

### 28. CVE-2026-78406｜IBM / Security Verify Access
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T21:18:03.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T21:18:03.190 / 2026-10-08T21:26:32.080
- **官方描述（原文）**：IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote unauthenticated attacker to execute arbitrary code on the system due to the deserialization of untrusted data.

### 29. CVE-2026-78401｜IBM / Security Verify Access
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T21:18:03.043)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T21:18:03.043 / 2026-10-08T21:26:32.080
- **官方描述（原文）**：IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote unauthenticated attacker to execute arbitrary code on the system due to the deserialization of untrusted data.

### 30. CVE-2026-7827｜FalkorDB / FalkorDB
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-09T05:16:45.327)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-09T05:16:45.327 / 2026-10-09T05:16:45.447
- **官方描述（原文）**：A stack-based buffer overflow in the _RdbLoadEntity function of the RDB graph decoders (src/serializers/decoders/*/decode_graph_entities.c) in FalkorDB before 4.18.4 allows a remote attacker who can issue Redis replication commands (for example, against an instance with no password configured) to cause a denial of service and possibly execute arbitrary code by supplying a crafted RDB stream with an attacker-controlled entity property count. The count sizes two variable-length arrays on the thread stack with no upper bound, and the decoder then fills them with attacker-supplied values.

### 31. CVE-2026-77900｜Microsoft / Azure App Service for Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T23:17:03.107)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T23:17:03.107 / 2026-10-08T23:17:03.107
- **官方描述（原文）**：Missing authentication for critical function in Azure App Service allows an unauthorized attacker to execute code over a network.

### 32. CVE-2026-75875｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T22:17:32.223)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T22:17:32.223 / 2026-10-08T22:17:32.223
- **官方描述（原文）**：IBM Guardium Data Protection 12.0, 12.1, and 12.2 could allow a remote attacker to execute arbitrary code due to path traversal.

### 33. CVE-2026-69435｜Microsoft / Azure SRE Agent
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T23:17:02.783)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T23:17:02.783 / 2026-10-08T23:17:02.783
- **官方描述（原文）**：Missing authorization in Azure SRE Agent allows an authorized attacker to elevate privileges over a network.

### 34. CVE-2026-5759｜FalkorDB / FalkorDB
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-09T05:16:44.920)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-09T05:16:44.920 / 2026-10-09T05:16:45.043
- **官方描述（原文）**：A double free and use-after-free vulnerability in the RdbLoadDeletedNodes function of the RDB graph decoders (src/serializers/decoders/*/decode_graph_entities.c) in FalkorDB before 4.18.1 allows a remote attacker who can issue Redis replication commands (for example, against an instance with no password configured) to cause a denial of service or execute arbitrary code in the redis-server process by supplying a crafted RDB stream whose deleted-nodes buffer length is not a multiple of sizeof(NodeID). The length check relies on ASSERT(), which is compiled out in release builds, so the function continues after freeing the buffer, reading it and freeing it a second time.

### 35. CVE-2026-19491｜IBM / Security Verify Access
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T21:17:57.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T21:17:57.070 / 2026-10-08T21:26:32.080
- **官方描述（原文）**：IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote attacker to bypass authentication due to improper authentication.

### 36. CVE-2026-19218｜AKIN Software Computer Import-Export Industry and Trade Co. Ltd. / MyRezzta
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T13:17:16.753)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T13:17:16.753 / 2026-10-08T20:09:14.010
- **官方描述（原文）**：Weak Password Recovery Mechanism for Forgotten Password vulnerability in AKIN Software Computer Import-Export Industry and Trade Co. Ltd. MyRezzta allows Password Recovery Exploitation. This issue affects MyRezzta: from 2.06.03 before 2.07.01.

### 37. CVE-2026-16916｜IBM / Security Verify Access
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T21:17:56.500)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T21:17:56.500 / 2026-10-08T21:26:32.080
- **官方描述（原文）**：IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote authenticated attacker to execute arbitrary code due to a protection mechanism failure.

### 38. CVE-2026-16823｜IBM / Security Verify Access
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T21:17:56.233)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T21:17:56.233 / 2026-10-08T21:26:32.080
- **官方描述（原文）**：IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 could allow a remote attacker to bypass security restrictions due to improper authentication.

### 39. CVE-2026-16340｜IBM / DataPower Gateway 10.6CD
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T13:17:16.610)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T13:17:16.610 / 2026-10-09T04:18:10.727
- **官方描述（原文）**：IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 through 11.0.0.2 could allow a remote attacker to execute arbitrary code due to an out-of-bounds write in the RFC2047 encoded-word parser.

### 40. CVE-2026-15762｜IBM / DataPower Gateway 10.6CD
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T14:16:51.880)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T14:16:51.880 / 2026-10-09T04:18:09.937
- **官方描述（原文）**：IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 through 11.0.0.2 could allow a remote attacker to execute arbitrary code due to an out-of-bounds write.

### 41. CVE-2026-14992｜IBM / DataPower Gateway 10.6CD
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T15:17:50.210)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T15:17:50.210 / 2026-10-09T04:18:07.413
- **官方描述（原文）**：IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 through 11.0.0.2 vulnerable to buffer overflow.

### 42. CVE-2026-14991｜IBM / DataPower Gateway 10.6CD
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T14:16:51.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T14:16:51.740 / 2026-10-09T04:18:06.670
- **官方描述（原文）**：IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 through 11.0.0.2 is vulnerable to a buffer overflow, caused by improper bounds checking. A local user could overflow the buffer and execute arbitrary code on the system.

### 43. CVE-2026-14990｜IBM / DataPower Gateway 10.6.0
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T14:16:51.603)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T14:16:51.603 / 2026-10-08T20:49:50.083
- **官方描述（原文）**：IBM DataPower Gateway 10.6.0.0 through 10.6.0.10 is vulnerable to cross-site scripting. This vulnerability allows an unauthenticated user to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclosure within a trusted session.

### 44. CVE-2026-14502｜IBM / DataPower Gateway 10.6CD
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T15:17:49.150)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T15:17:49.150 / 2026-10-09T04:18:06.343
- **官方描述（原文）**：IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 through 11.0.0.2 could allow a remote attacker to obtain administrative access due to failure to reject empty passwords during LDAP authentication.

### 45. CVE-2026-14269｜IBM / DataPower Gateway 10.6CD
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T15:17:48.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T15:17:48.600 / 2026-10-09T04:18:05.330
- **官方描述（原文）**：IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 through 11.0.0.2 is vulnerable to a heap-based buffer overflow, caused by improper bounds checking. An unauthenticated remote attacker could overflow the buffer and execute arbitrary code on the system.

### 46. CVE-2026-12260｜NetBoard CRM / NetBoard CRM Demo Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T09:16:41.087)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.00228 / percentile=0.12441
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T09:16:41.087 / 2026-10-08T21:04:18.423
- **官方描述（原文）**：SQL injection in the NetBoard CRM demo platform; specifically, the vulnerable component is the ‘user-name’ POST parameter in the ‘/module/auth/recovery.php’ endpoint. The parameter is vulnerable to blind attacks based on Boolean, error, time-based and UNION techniques. Exploitation allows attackers to extract confidential information (such as the version and type of backend used), alter data or further compromise the CRM environment.

### 47. CVE-2026-107910｜FalkorDB / FalkorDB
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-09T06:17:12.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-09T06:17:12.457 / 2026-10-09T06:17:12.577
- **官方描述（原文）**：An improper authentication vulnerability in the is_authenticated function (src/bolt/bolt_api.c) in FalkorDB before 4.20.0 allows a remote unauthenticated attacker to execute graph queries without credentials through the Bolt endpoint. The function decides whether a password is required by issuing an empty AUTH command to Redis and treats only a WRONGPASS error as meaning that a password is required; any other error, such as LOADING while a dataset is being loaded, MASTERDOWN during replication failover, or OOM under memory pressure, causes the client to be treated as authenticated. Only deployments that enable the Bolt endpoint (BOLT_PORT, disabled by default) are affected.

### 48. CVE-2026-107908｜FalkorDB / FalkorDB
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-09T06:17:10.777)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-09T06:17:10.777 / 2026-10-09T06:17:12.243
- **官方描述（原文）**：A heap-based out-of-bounds write in the BoltReadHandler function (src/bolt/bolt_api.c) in FalkorDB before 4.20.0 allows a remote unauthenticated attacker to cause a denial of service and possibly execute arbitrary code by sending a Bolt RESET message with an attacker-chosen chunk size to the Bolt port. The handler checks the size only with ASSERT(), which is compiled out in release builds, then computes a destination pointer from the wire-supplied 16-bit size and moves buffered data up to about 64 KiB backwards past the start of the read buffer. Only deployments that enable the Bolt endpoint (BOLT_PORT, disabled by default) are affected.

### 49. CVE-2026-107781｜dromara / skyeye
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T21:17:53.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T21:17:53.080 / 2026-10-08T21:27:15.010
- **官方描述（原文）**：Dromara Skyeye through commit 003549ae5615bd114ba5bb8ddf6a8e8ead97c321 contains a server-side request forgery and missing authorization vulnerability in the OnlyOffice save callback editUploadOfficeFileById. Unauthenticated attackers can supply arbitrary url and key parameters to make the server fetch internal URLs and overwrite any user's stored file, then read results via queryFileToShowById.

### 50. CVE-2026-107780｜dromara / skyeye
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T21:17:52.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T21:17:52.940 / 2026-10-08T21:27:15.010
- **官方描述（原文）**：Dromara Skyeye through commit 003549ae5615bd114ba5bb8ddf6a8e8ead97c321 contains an OS command injection vulnerability in the unauthenticated /post/TtsController/textToSpeech endpoint via the format parameter. Attackers can inject a single quote into format to break out of the PowerShell string and execute commands as the Skyeye service account on Windows.

### 51. CVE-2026-107779｜dromara / skyeye
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T21:17:52.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T21:17:52.790 / 2026-10-08T21:27:15.010
- **官方描述（原文）**：Dromara Skyeye through commit 003549ae5615bd114ba5bb8ddf6a8e8ead97c321 contains a missing authentication vulnerability in bundled xxl-job-admin JobInfoController endpoints annotated with @PermissionLimit(limit = false). Unauthenticated attackers can POST GLUE_SHELL, GLUE_PYTHON, or GLUE_POWERSHELL jobs with attacker-supplied glueSource to /jobinfo/addAndStart, executing commands on the executor host or stopping and deleting jobs.

### 52. CVE-2026-107726｜hazelcast / hazelcast
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T22:17:29.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T22:17:29.120 / 2026-10-08T22:17:29.120
- **官方描述（原文）**：Hazelcast is a unified real-time data platform combining stream processing with a fast data store. Prior to 5.4.5, 5.5.10, and 5.6.1, improper validation of data supplied by a malicious client able to connect to a cluster allows arbitrary reads from a cluster member's Java heap, off-heap data, and JVM process address space. The same flaw can crash cluster members and, in some Hazelcast Enterprise Edition configurations, corrupt memory with possible arbitrary code execution. Both slim and full distributions are affected. This issue is fixed in versions 5.4.5, 5.5.10, 5.6.1, and 5.7.0.

### 53. CVE-2026-107722｜nearform / fast-jwt
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T22:17:28.447)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T22:17:28.447 / 2026-10-08T22:17:28.583
- **官方描述（原文）**：fast-jwt provides fast JSON Web Token (JWT) implementation. From 6.2.0 until 6.3.0, fast-jwt can misclassify RSA public-key text as an HMAC secret when the key has non-whitespace content before its PEM header. In src/crypto.js, performDetectPublicKeyAlgorithms trims whitespace but publicKeyPemMatcher remains start-anchored, so comments, control characters, zero-width characters, or wrapper text can prevent PEM detection and reach the HMAC fallback. An attacker who knows the public key bytes can sign arbitrary HS256 claims with that public material when HS256 is inferred or allowed, resulting in authentication or authorization bypass. An asymmetric-only algorithm allowlist prevents the attack. This issue is fixed in version 6.3.0.

### 54. CVE-2026-107704｜jtescher / image_optimizer
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T19:17:02.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T19:17:02.897 / 2026-10-08T21:35:53.890
- **官方描述（原文）**：The image_optimizer Ruby gem 1.3.0 through 1.9.0 contains an OS command injection vulnerability in ImageOptimizer#identify_format that allows attackers to execute commands by supplying a crafted image path when the identify option is enabled. Attackers controlling the path, such as an uploaded file name, can append shell metacharacters like ';' that are executed via Ruby backticks with the Ruby process privileges.

### 55. CVE-2026-107700｜ntharim / dot-access
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T19:17:02.213)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T19:17:02.213 / 2026-10-08T21:35:53.890
- **官方描述（原文）**：dot-access 0.0.3 through 1.0.0 contains a code injection vulnerability that allows remote attackers to execute JavaScript by supplying crafted paths to get(). The path is concatenated into a new Function body in index.js, so attackers can reach constructor.constructor to load child_process and run operating system commands in the Node.js process.

### 56. CVE-2026-107699｜tzwm / ppt2png
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T19:17:01.853)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T19:17:01.853 / 2026-10-08T21:35:53.890
- **官方描述（原文）**：ppt2png through 0.0.6 contains an OS command injection vulnerability that allows attackers to execute operating system commands by supplying unsanitized input or output path arguments. Attackers can append shell metacharacters such as ';' to file names passed to child_process.exec() in ppt2png.js, running commands with Node.js process privileges.

### 57. CVE-2026-107510｜Infoblox / NIOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T10:17:09.553)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T10:17:09.553 / 2026-10-08T21:35:53.890
- **官方描述（原文）**：An authenticated high privilege user can inject arguments in troubleshooting commands resulting in privilege escalation.

### 58. CVE-2026-107406｜NetScaler / ADC
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T22:17:26.847)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T22:17:26.847 / 2026-10-08T22:17:26.847
- **官方描述（原文）**：Memory overflow vulnerability leading to Remote Code Execution or Denial of Service Vulnerability in NetScaler ADC. NetScaler ADC or NetScaler Gateway must be configured as a SAML SP or SAML IdP, subject to the following version-specific requirements: * For the following versions: Applicable only when configured as a SAML IdP: * NetScaler ADC and NetScaler Gateway between 14.1-73.37 and 14.1-73.41, inclusive * NetScaler ADC 14.1-FIPS between 14.1-73.37 FIPS and 14.1-73.41 FIPS, inclusive * NetScaler ADC and NetScaler Gateway between 13.1-64.23 and 13.1-64.28, inclusive * NetScaler ADC 13.1-FIPS between 13.1-NDcPP 13.1-37.279 and 13.1- 37.282, inclusive For the following versions: Applicable only when configured as a SAML SP or SAML IdP: * NetScaler ADC and NetScaler Gateway before 14.1-73.37 * NetScaler ADC 14.1-FIPS before 14.1-73.37 FIPS * NetScaler ADC and NetScaler Gateway before 13.1-64.23 * NetScaler ADC 13.1-FIPS before13.1-NDcPP 13.1-37.279

### 59. CVE-2026-106126｜Tenable, Inc. / Tenable Identity Exposure (SaaS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T20:17:29.950)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T20:17:29.950 / 2026-10-08T21:17:51.547
- **官方描述（原文）**：A command injection vulnerability in the Active Directory Events Listener of Tenable Identity Exposure (SaaS) allows an authenticated, low-privileged attacker to execute arbitrary commands as SYSTEM on the PDCe.

### 60. CVE-2026-104076｜TVU Networks / TVU Receiver / Transceiver
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T20:17:29.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T20:17:29.543 / 2026-10-08T21:35:53.890
- **官方描述（原文）**：TVU Networks Receiver/Transceiver devices running firmware before version 7.9 contain a missing authentication vulnerability that allows remote unauthenticated attackers to read sensitive device information and modify device configuration via unprotected REST API endpoints on port 8288. Attackers can send unauthenticated GET requests to disclose network configuration, firmware details, and cloud service information, or issue POST requests to endpoints such as /Setting3/API/API/v1/LocalNetwork/DNS to alter DNS settings and enable man-in-the-middle attacks on outbound connections to TVU cloud infrastructure.

### 61. CVE-2026-104075｜TVU Networks / TVU Receiver / Transceiver
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T20:17:29.377)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T20:17:29.377 / 2026-10-08T21:35:53.890
- **官方描述（原文）**：TVU Networks Receiver/Transceiver devices running firmware before version 7.9 contain an authentication bypass vulnerability in the web management login endpoint POST /tvu/Login that allows remote unauthenticated attackers to obtain an administrative session by submitting an empty or absent UserName parameter. Attackers can send a crafted HTTP request directly, bypassing client-side JavaScript validation, to receive a valid session cookie regardless of the password value and gain full administrative control of the device's web management interface.

### 62. CVE-2026-103663｜Ollama / Ollama
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T14:16:46.187)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T14:16:46.187 / 2026-10-08T20:08:45.857
- **官方描述（原文）**：Ollama is vulnerable to path traversal in the `/api/pull` endpoint due to insufficient validation of layer digests by the `digestToPath` function. An unauthenticated remote attacker can specify a path traversal sequence as a layer digest, causing a malicious binary to be written outside the model store. Critically if the server process has write access to `/usr/lib/ollama` (the default in most Ollama Docker images), an attacker can write the malicious file to that directory. On the next server restart, the file is loaded and executed, resulting in remote code execution as root. This issue was fixed in version 0.35.0.

### 63. CVE-2026-107702｜Webkul / QloApps
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T18:17:26.637)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:17:26.637 / 2026-10-08T19:17:02.570
- **官方描述（原文）**：QloApps through 1.7.0 contains an authorization bypass vulnerability in AdminHotelRoomsBookingController::postProcess() that allows restricted back-office employees to access other hotels' data by supplying an id_hotel parameter. Attackers can modify the id_hotel URL parameter on the Book Now page to view room availability and booking status of hotels outside their assigned profile access.

### 64. CVE-2026-107392｜Borewit / music-metadata
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T20:17:33.707)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.2 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T20:17:33.707 / 2026-10-08T20:46:35.260
- **官方描述（原文）**：music-metadata is a metadata parser for audio and video media files. Prior to 11.15.0, the DSF parser handles an unrecognized chunk by calling tokenizer.ignore without awaiting the returned promise and without first rejecting a chunk size smaller than the 12-byte chunk header. A crafted DSF input can produce a negative ignore length; with strtok3 10.3.5 or later, the resulting RangeError is detached from the parseBuffer promise and becomes an unhandled rejection under Node.js default behavior. The parse call can appear to resolve before the process crashes, bypassing per-parse try/catch handling. The demonstrated impact is availability loss only and requires the DSF parsing path. This issue is fixed in version 11.15.0.

### 65. CVE-2026-107387｜Borewit / music-metadata
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T19:17:01.517)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.2 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T19:17:01.517 / 2026-10-08T20:46:35.260
- **官方描述（原文）**：music-metadata is a metadata parser for audio and video media files. Prior to 11.16.0, the APEv2 parser reads an attacker-controlled tag-item size and allocates a Uint8Array for a binary item before proving that the declared item fits in the remaining tag or file data. A small crafted APE file can therefore trigger a disproportionate allocation, including through cover-art items, and repeated or concurrent parsing can exhaust process memory. The demonstrated impact is availability loss only. This issue is fixed in version 11.16.0.

### 66. CVE-2026-107361｜CISA / Malcolm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T18:17:21.170)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.2 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:17:21.170 / 2026-10-08T21:03:43.847
- **官方描述（原文）**：The Arkime live capture service (arkime-live) in Malcolm runs with network_mode: host, exposing port 8005 on all network interfaces (viewHost=0.0.0.0). Arkime trusts the X-Forwarded-User header from any IP address (userAuthIps=::,0.0.0.0/0) and auto-creates users with full access. The passwordSecret is hardcoded to the public value "Malcolm". A network-adjacent attacker bypasses nginx entirely by connecting directly to port 8005 with a forged identity header.

### 67. CVE-2026-107335｜CISA / Malcolm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T18:17:19.970)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:17:19.970 / 2026-10-08T21:03:43.847
- **官方描述（原文）**：Malcolm's upload-processing pipeline (scripts/safe-extract.py) enforces entry-count, nesting-depth, and total-uncompressed-byte limits when extracting container archives (zip/tar/rar/7z via libarchive), but those limits are not applied when the uploaded file is a single-stream compressed format (.gz, .bz2, .xz, .lzma, .lz) that isn't a .tar.*-style archive. Any authenticated user permitted to upload PCAP/log files can upload a small, highly compressible file (e.g. a gzip bomb) that decompresses to an effectively unbounded size on disk, exhausting the shared Docker volume used by OpenSearch, Logstash, Arkime, and Zeek, and disrupting the platform for all users.

### 68. CVE-2026-107334｜CISA / Malcolm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T18:17:19.763)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:17:19.763 / 2026-10-08T21:03:43.847
- **官方描述（原文）**：Malcolm's nginx Lua role-based access control (RBAC) layer decides whether an authenticated user may reach a role-restricted path (e.g. /htadmin, /auth, /admin_login, /arkime/api/esadmin, NetBox, upload endpoints) by pattern-matching the raw, percent-encoded request URI. Nginx itself, however, selects which location block actually serves the request using the percent-decoded, normalized URI. Because the RBAC check never percent-decodes its input, an authenticated low-privilege user can request an admin-only path using percent-encoding (e.g. /%68tadmin.php) and have nginx route it to the restricted location while the Lua RBAC gate evaluating the un-decoded raw string finds no matching restriction and grants access.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2021-3199｜ONLYOFFICE / Docs
- **Title**：ONLYOFFICE Docs Server Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.08215 / percentile=0.9475
- **CISA KEV**：listed=true / date_added=2026-10-08 / due_date=2026-10-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：ONLYOFFICE Docs contains a path traversal vulnerability that can occur when JWT is used, via a /.. sequence in an image upload parameter and could allow for remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2016-3081｜Apache / Struts
- **Title**：Apache Struts Command Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.93352 / percentile=0.99838
- **CISA KEV**：listed=true / date_added=2026-10-08 / due_date=2026-10-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apache Struts contains a command injection vulnerability that could allow remote attackers to execute arbitrary code via method:prefix when Dynamic Method Invocation is enabled.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2015-3306｜ProFTPD / ProFTPD
- **Title**：ProFTPD Improper Access Control Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-08 / due_date=2026-10-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：ProFTPD contains an improper access control vulnerability that could allow remote attackers to read and write to arbitrary files via the site cpfr and site cpto commands.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2015-5477｜ISC / BIND
- **Title**：ISC BIND Data Processing Errors Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-08 / due_date=2026-10-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：ISC BIND contains a data processing errors vulnerability that could allow remote attackers to cause a denial of service via TKEY queries.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2023-22894｜Strapi / Strapi
- **Title**：Strapi Cleartext Storage of Sensitive Information Vulnerability
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 4.9 (MEDIUM)
- **EPSS**：0.01658 / percentile=0.7591
- **CISA KEV**：listed=true / date_added=2026-10-08 / due_date=2026-10-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Strapi contains a cleartext storage of sensitive information vulnerability that could allow attackers with access to the admin panel to discover sensitive user details via the query filter. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version. This vulnerability can be chained with CVE-2023-22621 to achieve remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-95210 | P3 / 38 | 未確認 / 未確認 | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-9209 | P3 / 38 | mJob / mJobTime | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107703 | P3 / 38 | enmaso / @enmaso/node-convert | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107640 | P3 / 38 | Integrics / Enswitch | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105110 | P3 / 38 | Iskratel / Innbox | v4.0 9.3 (CRITICAL) | 0.02788 / percentile=0.85991 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-93858 | WATCH / 30 | OpenStack / Mistral | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107378 | WATCH / 30 | Kozea / CairoSVG | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107376 | WATCH / 30 | webonyx / graphql-php | v3.1 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107362 | WATCH / 30 | CISA / Malcolm | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107337 | WATCH / 30 | CISA / Malcolm | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105830 | WATCH / 30 | thephpleague / commonmark | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-96207 | WATCH / 28 | Microsoft / Microsoft Partner Center | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94510 | WATCH / 28 | Microsoft / Microsoft Bookings | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93034 | WATCH / 28 | SGLang / SGLang | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-92555 | WATCH / 28 | AKIN Software Computer Import-Export Industry and Trade Co. Ltd. / AKINSOFT WOLVOX Control Panel | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-88131 | WATCH / 28 | Microsoft / Microsoft Dataverse | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-85097 | WATCH / 28 | Bricksforge / Bricksforge | v3.1 9.8 (CRITICAL) | 0.00312 / percentile=0.22075 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-84272 | WATCH / 28 | IBM / Guardium Data Protection | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-84249 | WATCH / 28 | IBM / Guardium Data Protection | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-84244 | WATCH / 28 | IBM / Guardium Data Protection | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-80381 | WATCH / 28 | IBM / Guardium Data Protection | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79842 | WATCH / 28 | Hewlett Packard Enterprise / HPE Intelligent Management Center (iMC) | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-78406 | WATCH / 28 | IBM / Security Verify Access | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-78401 | WATCH / 28 | IBM / Security Verify Access | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-7827 | WATCH / 28 | FalkorDB / FalkorDB | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：1；缺少 Product：1；缺少 Title：25。
- EPSS 未確認：25；Exploitation status 未確認：10。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-09T06:59:49.355525+00:00`；Delta generated at：`2026-10-09T06:59:49.355525+00:00`。

---

## 可驗證資料來源

- **CVE-2021-3199** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-3199) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2021-3199) · [Vendor / Advisory (github.com)](https://github.com/ONLYOFFICE/DocumentServer/blob/903fe5ab7a275bd69c3c3346af2d21cf87ebeabf/CHANGELOG.md#563) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2016-3081** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-3081) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2016-3081) · [Vendor / Advisory (cwiki.apache.org)](https://cwiki.apache.org/confluence/display/WW/S2-032) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2015-3306** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2015-3306) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (proftpd.org)](http://www.proftpd.org/) · [Vendor / Advisory (lists.debian.org)](https://lists.debian.org/debian-security-announce/2015/msg00154.html) · [Vendor / Advisory (lists.opensuse.org)](https://lists.opensuse.org/archives/list/updates@lists.opensuse.org/message/WE6YZRG5UVXMGQ7IVDRYBPIWV4M6UUGM/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2015-5477** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2015-5477) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (web.archive.org)](https://web.archive.org/web/20150729014733/https://kb.isc.org/article/AA-01272) · [Vendor / Advisory (access.redhat.com)](https://access.redhat.com/errata/RHSA-2015:1513.html) · [Vendor / Advisory (supportportal.juniper.net)](https://supportportal.juniper.net/s/article/2016-01-Security-Bulletin-Junos-Vulnerability-in-ISC-BIND-named-CVE-2015-5477) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2023-22894** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-22894) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-22894) · [Vendor / Advisory (strapi.io)](https://strapi.io/blog/security-disclosure-of-vulnerabilities-cve) · [Vendor / Advisory (github.com)](https://github.com/strapi/strapi/releases) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-95210** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95210)
- **CVE-2026-9209** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9209)
- **CVE-2026-107703** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107703)
- **CVE-2026-107640** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107640)
- **CVE-2026-105110** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105110) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105110)
- **CVE-2026-93858** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93858)
- **CVE-2026-107378** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107378)
- **CVE-2026-107376** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107376)
- **CVE-2026-107362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107362)
- **CVE-2026-107337** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107337)
- **CVE-2026-105830** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105830)
- **CVE-2026-96207** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96207)
- **CVE-2026-94510** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94510)
- **CVE-2026-93034** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93034)
- **CVE-2026-92555** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92555)
- **CVE-2026-88131** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88131)
- **CVE-2026-85097** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85097) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85097)
- **CVE-2026-84272** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84272)
- **CVE-2026-84249** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84249)
- **CVE-2026-84244** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84244)
- **CVE-2026-80381** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80381)
- **CVE-2026-79842** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79842)
- **CVE-2026-78406** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78406)
- **CVE-2026-78401** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78401)
- **CVE-2026-7827** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-7827)
- **CVE-2026-77900** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77900)
- **CVE-2026-75875** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75875)
- **CVE-2026-69435** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69435)
- **CVE-2026-5759** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-5759)
- **CVE-2026-19491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19491)
- **CVE-2026-19218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19218)
- **CVE-2026-16916** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16916)
- **CVE-2026-16823** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16823)
- **CVE-2026-16340** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16340)
- **CVE-2026-15762** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15762)
- **CVE-2026-14992** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14992)
- **CVE-2026-14991** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14991)
- **CVE-2026-14990** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14990)
- **CVE-2026-14502** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14502)
- **CVE-2026-14269** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14269)
- **CVE-2026-12260** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12260) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-12260)
- **CVE-2026-107910** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107910)
- **CVE-2026-107908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107908)
- **CVE-2026-107781** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107781)
- **CVE-2026-107780** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107780)
- **CVE-2026-107779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107779)
- **CVE-2026-107726** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107726)
- **CVE-2026-107722** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107722)
- **CVE-2026-107704** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107704)
- **CVE-2026-107700** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107700)
- **CVE-2026-107699** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107699)
- **CVE-2026-107510** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107510)
- **CVE-2026-107406** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107406)
- **CVE-2026-106126** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-106126)
- **CVE-2026-104076** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104076)
- **CVE-2026-104075** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104075)
- **CVE-2026-103663** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103663)
- **CVE-2026-107702** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107702)
- **CVE-2026-107392** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107392)
- **CVE-2026-107387** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107387)
- **CVE-2026-107361** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107361)
- **CVE-2026-107335** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107335)
- **CVE-2026-107334** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107334)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
