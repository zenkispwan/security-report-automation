# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**95** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=94、NEW_KEV=1。
- Intelligence 候選：**30** 筆；P1 **2**、P2 **0**、P3 **3**、WATCH **25**。
- Baseline：state / generated_at=2026-11-03T07:24:28.430596+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-119977、CVE-2026-118527。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **95** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-119977｜WordPress / WordPress Core
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-03 / due_date=2026-11-06
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-31T06:16:34.550 / 2026-11-04T05:18:29.227
- **官方描述（原文）**：WordPress WordPress Core contains a time-of-check time-of-use (TOCTOU) race condition vulnerability that could allow unauthenticated attackers to execute code on the server during the upgrade window. This is due to predictable, web-accessible staging paths used during full-package core upgrades.

### 2. CVE-2026-118527｜Ivanti / Connect Secure
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:24.920)
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-30 / due_date=2026-11-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-03T15:17:24.920 / 2026-11-03T17:48:12.873
- **官方描述（原文）**：Ivanti Connect Secure contains a generation of predictable numbers or identifiers vulnerability that allows a remote authenticated attacker to upload files with attacker-controlled content to a known location on disk. This vulnerability can be chained with CVE-2026-104935 and CVE-2026-111357.

### 3. CVE-2026-63470｜koxudaxi / fastapi-code-generator
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T20:18:15.590)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T20:18:15.590 / 2026-11-03T20:31:38.783
- **官方描述（原文）**：fastapi-code-generator creates FastAPI applications from OpenAPI files. Prior to 0.8.1, the generator inserts Operation.summary into a generated route-handler docstring as a triple-double-quoted string without escaping embedded triple quotes. An attacker-controlled or attacker-influenced operation summary can close the docstring and inject a valid Python expression statement into the handler body. Syntax-breaking input only causes generation to fail, but syntactically valid generated code executes with the server process's privileges when the affected route handler is called. This call-time route-handler docstring sink is distinct from the project's separate import-time route-path and additional-response-key sinks. This issue is fixed in version 0.8.1.

### 4. CVE-2026-44266｜enspirit / elo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T18:18:02.957)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T18:18:02.957 / 2026-11-03T20:18:13.823
- **官方描述（原文）**：Elo is a purely functional expression language for no-code tools. Prior to 1.0.1, the Ruby backend in src/compilers/ruby.ts embeds attacker-controlled text in Ruby double-quoted strings without escaping #, so Ruby interpolation forms in the string-literal emitter or the labelled subtype-constraint branch become executable Ruby. The affected entry points include the /try playground with the Ruby target, bin/eloc -t ruby -x, and defaultFormats.elo.parse() followed by Ruby emission. A failing labelled subtype constraint evaluates its message, while an ordinary string literal is evaluated when the compiled Ruby runs, allowing Ruby code and shell command execution through backticks. JavaScript, Python, and SQL emission are not affected by this Ruby-specific path. This issue is fixed in version 1.0.1.

### 5. CVE-2026-38600｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T17:18:13.070)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T17:18:13.070 / 2026-11-03T22:19:47.327
- **官方描述（原文）**：A Zip Slip vulnerability in the /upload endpoint of codeskyblue gohttpserver through v1.3.0 allows attackers to write arbitrary files via uploading a crafted Zip archive.

### 6. CVE-2026-63501｜Agamnentzar / ag-psd
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T20:18:17.100)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T20:18:17.100 / 2026-11-03T22:19:47.923
- **官方描述（原文）**：ag-psd is a JavaScript library for reading and writing Photoshop Document files. Prior to 31.0.3, readPsd() accepts a totalMemoryLimit for parsing untrusted PSD files, but decodeLayerImageData expects a differently named memoryLimit property and therefore passes an undefined limit to createImageDataBitDepth. An attacker who can supply a PSD to an application with layer decoding enabled can use attacker-controlled layer dimensions to trigger an allocation larger than the configured limit, causing process memory exhaustion and denial of service. The advisory also identifies inflateSync(compressed) decompressing ZIP-encoded channel data without an output-size cap, which can cause a similar denial of service through unbounded decompression. This vulnerability is fixed in 31.0.1.

### 7. CVE-2026-63395｜isomorphic-git / isomorphic-git
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T20:18:14.917)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T20:18:14.917 / 2026-11-03T22:19:47.677
- **官方描述（原文）**：isomorphic-git is a pure JavaScript implementation of Git for Node.js and browsers. Prior to 1.38.6, isomorphic-git's git.checkout writes new child paths through symlinked leading directory components without checking them. A malicious repository can first place a directory symlink and later replace the tree state with a child file beneath that path; the usual trigger is a clone followed by a later pull, while a single clone can trigger the issue when a symlink already exists or the consuming application accesses the tree. With Node fs on Linux or macOS, the operating system can resolve the write outside the working tree, permitting arbitrary host file writes and possible code execution. Node fs on Windows usually blocks the symlink plant without additional privilege, and browser or in-memory providers limit impact to their virtual filesystem and are affected only when they implement symlink creation and following. This issue is fixed in version 1.38.6.

### 8. CVE-2026-121548｜jarun / nnn
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T16:17:26.557)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T16:17:26.557 / 2026-11-03T17:18:10.497
- **官方描述（原文）**：Jarun nnn through 5.3 contains an OS command injection vulnerability in plugins/togglex that allows attackers to execute commands via crafted filenames. Attackers can place files whose names contain a double quote and shell syntax, which xargs -I splices into an sh -c script, running commands as the user invoking togglex.

### 9. CVE-2026-121449｜Finsys / dockhand
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:37.397)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:37.397 / 2026-11-03T17:18:10.057
- **官方描述（原文）**：Dockhand from 1.0.47 before 1.0.54 exposes plaintext stack secrets because deployStack() attaches resolved secret values to its result as resolvedSecrets, which Git-stack routes return unfiltered. Holders of a stack's webhook secret or users with stacks:start permission can trigger the Git stack webhook, manual deploy, or create-and-deploy endpoints to receive stored and external-provider secrets such as 1Password or Vault values.

### 10. CVE-2026-121445｜darylldoyle / svg-sanitizer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:36.623)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:36.623 / 2026-11-03T17:18:09.917
- **官方描述（原文）**：darylldoyle svg-sanitizer from 1.0.0 before 1.1.0 contains a regular expression denial of service vulnerability in the image-set pattern of stripRemoteCssTokens() when removeRemoteReferences is enabled. Attackers can submit SVGs with many unclosed image-set tokens to exhaust CPU, or trigger PCRE limits causing sanitize() to throw a TypeError and leave unsanitized content.

### 11. CVE-2026-121437｜lepture / mistune
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:35.147)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:35.147 / 2026-11-03T17:18:09.653
- **官方描述（原文）**：Mistune from 3.3.0 before 3.3.4 contains a denial of service vulnerability that allows remote attackers to exhaust CPU through quadratic-time emphasis delimiter processing. Attackers can submit small markdown documents with repeated patterns like "*a_b" to trigger an O(n²) index-fixup loop, stalling workers for seconds.

### 12. CVE-2026-121429｜AzuraCast / AzuraCast
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:33.747)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:33.747 / 2026-11-03T17:18:09.393
- **官方描述（原文）**：AzuraCast through 0.23.8 contains a command injection vulnerability that allows station users with Profile permission to execute OS commands via StereoTool settings. Attackers can inject shell metacharacters into stereo_tool_configuration_path or stereo_tool_license_key, which are executed via /bin/sh on station restart, compromising the container.

### 13. CVE-2026-121425｜nodemailer / nodemailer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:33.057)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:33.057 / 2026-11-03T17:18:09.250
- **官方描述（原文）**：Nodemailer from 3.0.0 before 10.1.4 contains a parsing flaw in addressparser that ends an RFC 5322 group at a semicolon inside quoted display names or comments. Attackers can submit crafted group addresses that conformant validators approve, redirecting mail to attacker-chosen recipients and bypassing recipient allow lists.

### 14. CVE-2026-121417｜surrealdb / surrealdb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:31.553)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:31.553 / 2026-11-03T17:18:08.963
- **官方描述（原文）**：SurrealDB before 3.3.0 contains a use-after-free vulnerability in surrealdb-core KV backends that pass borrowed transaction state into affinitypool::spawn_local closures relying on future Drop for safety. Rust embedders that leak a dispatched future (e.g. via mem::forget) and drop the transaction cause pool workers to read and write freed memory, risking crashes or memory corruption.

### 15. CVE-2026-121409｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:29.790)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:29.790 / 2026-11-03T18:17:57.493
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a denial of service vulnerability that allows malicious servers or unauthenticated peers to abort clients or proxies via oversized X.224 routing tokens. Attackers can send an oversized LoadBalanceInfo in a Server Redirection PDU, or a 240–247 byte token to a FixedTarget freerdp-proxy, triggering a tpdu_write_header assertion that crashes the process.

### 16. CVE-2026-121393｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:26.917)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:26.917 / 2026-11-03T21:12:22.357
- **官方描述（原文）**：FreeRDP from 3.0.0 before 3.32.2 contains a denial of service vulnerability that allows malicious RDP servers to abort clients built with verbose WinPR assertions by sending crafted RemoteFX region rectangles. Attackers can supply a rectangle with x set to 65535 alongside a SurfaceBits destination left of 1, triggering a 16-bit coordinate assertion in rfx_process_message that terminates the client process.

### 17. CVE-2026-121260｜Ziroom / ZHOME A0101
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T16:17:23.393)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T16:17:23.393 / 2026-11-03T17:18:07.907
- **官方描述（原文）**：A flaw has been found in Ziroom ZHOME A0101 1.0.1.0 Build 202004151405. This issue affects the function loadstring of the file usr/lib/lua/luci/controller/api/zrUsb.lua of the component Lua Handler. This manipulation causes code injection. Remote exploitation of the attack is possible. The exploit has been published and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 18. CVE-2026-118487｜Eclipse Foundation / Eclipse Vert.x
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T16:17:19.890)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T16:17:19.890 / 2026-11-03T16:30:17.150
- **官方描述（原文）**：In Eclipse Vert.x versions [4.0.0, 4.5.35] or [5.0.0, 5.2.2], the `FrameParser` in vertx-stomp creates a `RecordParser` without setting `maxRecordSize`, so any peer that streams bytes continuously without a newline character causes the parser to accumulate data indefinitely. Both the STOMP server and the STOMP client are affected: a malicious server can exploit this against a connecting client, and a malicious client can exploit this against a server before or after authentication. Sustained byte streaming exhausts JVM heap memory, crashing the affected process and causing a complete denial of service.

### 19. CVE-2026-95860｜node-opcua / node-opcua
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:45.907)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:45.907 / 2026-11-03T21:17:46.053
- **官方描述（原文）**：node-opcua is an OPC UA implementation for TypeScript and Node.js. From 2.42.0 until 2.180.0, namespace-level access control configured through setDefaultRolePermissions is not honored by the runtime enforcement path for nodes without explicit per-node RolePermissions. SessionContext.getApplicableRolePermissions reads a missing or null DefaultRolePermissions metadata value instead of the configured namespace field, and the null result is treated permissively. An anonymous network client can consequently write variables with CurrentWrite access or call bound methods when an operator configured a restrictive namespace default and relied on inheritance. Servers with no declared policy, nodes with explicit per-node permissions, and correctly bound programmatic namespace metadata are outside the authorization-bypass case. This issue is fixed in version 2.180.0.

### 20. CVE-2026-95733｜Hewlett Packard Enterprise (HPE) / Fabric Composer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T20:18:21.433)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T20:18:21.433 / 2026-11-03T20:30:24.880
- **官方描述（原文）**：A vulnerability exists in a component of HPE Networking Fabric Composer. Successful exploitation could allow an unauthenticated adjacent attacker to execute arbitrary code on the affected system.

### 21. CVE-2026-95732｜Hewlett Packard Enterprise (HPE) / Fabric Composer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T20:18:21.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T20:18:21.320 / 2026-11-03T20:30:24.880
- **官方描述（原文）**：An authentication bypass vulnerability exists in the underlying operating system of HPE Networking Fabric Composer. Successful exploitation could allow an unauthenticated adjacent attacker to execute arbitrary code on the affected system.

### 22. CVE-2026-95731｜Hewlett Packard Enterprise (HPE) / Fabric Composer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T20:18:21.197)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T20:18:21.197 / 2026-11-03T20:30:24.880
- **官方描述（原文）**：Hardcoded password vulnerabilities in the command-line interface of HPE Networking Fabric Composer could allow an unauthenticated remote attacker to access the affected system using hardcoded credentials. Successful exploitation could allow an attacker to gain unauthorized administrative access to the affected system with elevated privileges.

### 23. CVE-2026-92190｜Quest / Foglight for Databases
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T00:17:29.390)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T00:17:29.390 / 2026-11-04T00:17:29.390
- **官方描述（原文）**：Quest Foglight for Databases baseRmiServiceExporter Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Quest Foglight for Databases. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the baseRmiServiceExporter bean. The issue results from the lack of proper validation of user-supplied data prior to deserializing it. An attacker can leverage this vulnerability to execute code in the context of SYSTEM. Was ZDI-CAN-29170.

### 24. CVE-2026-92189｜Quest / Foglight for Databases
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T00:17:29.260)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T00:17:29.260 / 2026-11-04T00:17:29.260
- **官方描述（原文）**：Quest Foglight for Databases writeTopologySectionToFile External Control of File Path Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Quest Foglight for Databases. Authentication is not required to exploit this vulnerability. The specific flaw exists within the writeTopologySectionToFile method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM. Was ZDI-CAN-29169.

### 25. CVE-2026-92188｜Quest / Foglight for Databases
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T00:17:29.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T00:17:29.130 / 2026-11-04T00:17:29.130
- **官方描述（原文）**：Quest Foglight for Databases ForgeMBeanServerSupport Missing Authentication Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Quest Foglight for Databases. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ForgeMBeanServerSupport module. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to execute code in the context of SYSTEM. Was ZDI-CAN-29168.

### 26. CVE-2026-89292｜Eclipse Foundation / Eclipse Mnestix
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T10:17:20.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00453 / percentile=0.39387
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T10:17:20.077 / 2026-11-03T21:17:45.263
- **官方描述（原文）**：In Eclipse Mnestix Browser versions 1.6.0 up until but excluding 2.3.0 it was possible for an unauthenticated attacker to exfiltrate the MNESTIX_BACKEND_API_KEY for all configured Infrastructures.

### 27. CVE-2026-82158｜Dell / Wyse Management Suite
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:43.823)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:43.823 / 2026-11-03T22:19:49.740
- **官方描述（原文）**：Dell Wyse Management Suite, versions prior to 2609.0.0.155, contain an Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability. A low privileged attacker with remote access could potentially exploit this vulnerability, leading to Script injection.

### 28. CVE-2026-63471｜koxudaxi / fastapi-code-generator
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T20:18:15.753)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T20:18:15.753 / 2026-11-03T20:31:38.783
- **官方描述（原文）**：fastapi-code-generator creates FastAPI applications from OpenAPI files. Prior to 0.8.1, the generator inserts an OpenAPI path into a generated @app.get(...) route decorator as a single-quoted generated route string without escaping embedded quotes. An attacker-controlled or attacker-influenced OpenAPI path can close the string and inject a valid Python expression into the decorator argument. Syntax-breaking input only causes generation to fail, but syntactically valid generated code executes with the application's or CI process's privileges when the generated module is imported and the decorator is evaluated. This OpenAPI path sink is distinct from the project's separate operation-summary docstring and additional-response-key sinks. This issue is fixed in version 0.8.1.

### 29. CVE-2026-63469｜koxudaxi / fastapi-code-generator
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T20:18:15.420)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T20:18:15.420 / 2026-11-03T20:31:38.783
- **官方描述（原文）**：fastapi-code-generator creates FastAPI applications from OpenAPI files. Prior to 0.8.1, the generator inserts an additional response status-code key into the generated responses={...} route-decorator dictionary as a single-quoted Python string without escaping embedded quotes. A multi-response OpenAPI operation with an attacker-controlled or attacker-influenced second non-primary response key can close the dictionary-key literal and inject a valid Python expression. Syntax-breaking input only causes generation to fail, but syntactically valid generated code executes with the application's or CI process's privileges when the generated module is imported and its decorator arguments are evaluated. This additional-response-key sink is distinct from the project's separate route-path and operation-summary sinks. This issue is fixed in version 0.8.1.

### 30. CVE-2026-44267｜enspirit / elo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T18:18:03.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T18:18:03.130 / 2026-11-03T18:18:03.130
- **官方描述（原文）**：Elo is a purely functional expression language for no-code tools. Prior to 1.0.1, plain Elo strings supplied to defaultFormats.elo.parse(), bin/elo, or elo-lang.org/try can use .constructor.constructor to reach JavaScript Function because the member_access handler in src/transform.ts does not reject meta-properties, src/compilers/javascript.ts emits the surviving property directly, and src/parser.ts accepts constructor as an ordinary identifier. The resulting generated JavaScript executes attacker-selected code in the host runtime. This permits browser script execution and session compromise on the auto-running playground and arbitrary Node.js code execution on library, CI, or DevOps hosts. This plain-string path is distinct from the programmatic AST-object injection issue. This issue is fixed in version 1.0.1.

### 31. CVE-2026-4052｜WSO2 / WSO2 API Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T08:17:15.530)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.0036 / percentile=0.29885
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T08:17:15.530 / 2026-11-03T20:18:14.127
- **官方描述（原文）**：This issue only impacts deployments where WSO2 Identity Server is configured as a Resident Key Manager with database sharing. In such environments, a self-registered user may gain access to the System REST APIs of WSO2 API Manager by obtaining a token from the WSO2 Identity Server token endpoint.

### 32. CVE-2026-28336｜SolarWinds / Dameware
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T17:18:12.570)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T17:18:12.570 / 2026-11-04T05:18:54.760
- **官方描述（原文）**：SolarWinds Dameware was found to be affected by a command injection vulnerability that could lead to the compromise of the remotely controlled host. Authentication is required.

### 33. CVE-2026-22058｜NETAPP / StorageGRID (formerly StorageGRID Webscale)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T22:19:47.030)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T22:19:47.030 / 2026-11-03T22:19:47.030
- **官方描述（原文）**：StorageGRID (formerly StorageGRID Webscale) versions 11.3 and higher allow an attacker with product-specific knowledge and the ability to communicate with the Grid Network on certain ports to make unauthorized requests.

### 34. CVE-2026-13594｜Zohocorp / Log360
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T08:17:15.203)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.01142 / percentile=0.66717
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T08:17:15.203 / 2026-11-04T05:18:42.640
- **官方描述（原文）**：Zoho Corporation's ManageEngine Log360 and EventLog Analyzer versions 13062 and below are vulnerable to an issue that could allow an adversary to gain unauthorized access to the product.

### 35. CVE-2026-121802｜better-auth / Better Auth
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T03:17:15.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T03:17:15.730 / 2026-11-04T03:17:15.877
- **官方描述（原文）**：@better-auth/expo before 1.7.16 allows certain account-takeover outcomes (e.g., unauthenticated changes of any account's email address), because it signs a caller-supplied state value without checking whether that value had been issued by the server. NOTE: the application secret must be rotated after updating to a fixed version.

### 36. CVE-2026-121615｜Linksys / E5600
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T03:17:14.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T03:17:14.810 / 2026-11-04T03:17:14.997
- **官方描述（原文）**：A vulnerability was determined in Linksys E5600 1.1.0.26. Affected is an unknown function of the file /cgi-bin/mesh_login.cgi of the component Login Handler. Executing a manipulation can lead to improper authentication. The attack can be launched remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way. This vulnerability only affects products that are no longer supported by the maintainer.

### 37. CVE-2026-121609｜Qihoo 360 / Whole Home Router M5
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T02:17:20.243)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T02:17:20.243 / 2026-11-04T02:17:20.413
- **官方描述（原文）**：A vulnerability was identified in Qihoo 360 Whole Home Router M5 4.0.17.1566. This issue affects the function Home of the file /etc/init.d/mpt of the component Boot Script. The manipulation leads to hard-coded credentials. Remote exploitation of the attack is possible. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 38. CVE-2026-121607｜Qihoo 360 / D603-2
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T02:17:19.753)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T02:17:19.753 / 2026-11-04T02:17:19.933
- **官方描述（原文）**：A vulnerability was found in Qihoo 360 D603-2, D600-2, D606-6 and D706 up to 6.4.9. This affects the function testspeed_command of the file /fs2/bin/iscm. Performing a manipulation of the argument host results in os command injection. The attack may be initiated remotely. The exploit has been made public and could be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 39. CVE-2026-121606｜Qihoo 360 / D621-2
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T01:17:23.880)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T01:17:23.880 / 2026-11-04T01:17:24.050
- **官方描述（原文）**：A vulnerability has been found in Qihoo 360 D621-2, D603-2, D600-2, D619, D606-6 and D706 up to 6.4.9. Affected by this issue is the function verify_sign of the file fs2/bin/iscm of the component Firmware Signature Verification. Such manipulation of the argument sign leads to improper verification of cryptographic signature. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 40. CVE-2026-121392｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:26.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:26.710 / 2026-11-03T21:12:38.530
- **官方描述（原文）**：FreeRDP before 3.32.2 contains an improper certificate validation vulnerability in tls_verify_certificate() that accepts Common Name fallback despite non-matching SAN entries and matches IP literals against DNS strings. Man-in-the-middle attackers holding a certificate from a client-trusted CA can bypass server identity checks to intercept RDP sessions, including keystrokes, clipboard, and screen content.

### 41. CVE-2026-121249｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:35.493)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:35.493 / 2026-11-03T22:19:45.487
- **官方描述（原文）**：Buffer overflow in ANGLE in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 42. CVE-2026-121247｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:35.220)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:35.220 / 2026-11-04T05:18:37.560
- **官方描述（原文）**：Buffer overflow in Dawn in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 43. CVE-2026-121246｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:35.093)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:35.093 / 2026-11-04T05:18:37.383
- **官方描述（原文）**：Use after free in WebGL in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 44. CVE-2026-121241｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:34.420)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:34.420 / 2026-11-03T22:19:44.963
- **官方描述（原文）**：Use after free in Navigation in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 45. CVE-2026-121234｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:33.503)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:33.503 / 2026-11-03T22:19:44.597
- **官方描述（原文）**：Privilege elevation in Contacts in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 46. CVE-2026-121229｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:32.837)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:32.837 / 2026-11-04T05:18:36.970
- **官方描述（原文）**：Memory corruption in ANGLE in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 47. CVE-2026-121214｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:30.847)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:30.847 / 2026-11-03T22:19:43.080
- **官方描述（原文）**：Use after free in Passwords in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 48. CVE-2026-121202｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:29.203)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:29.203 / 2026-11-03T22:19:42.423
- **官方描述（原文）**：Use after free in Autofill in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 49. CVE-2026-121200｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:28.887)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:28.887 / 2026-11-03T22:19:42.110
- **官方描述（原文）**：Incorrect reference resolution in DevTools in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 50. CVE-2026-121189｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:27.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:27.693 / 2026-11-03T22:19:41.947
- **官方描述（原文）**：Use after free in Browser in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Low)

### 51. CVE-2026-121185｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:27.177)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:27.177 / 2026-11-04T05:18:36.270
- **官方描述（原文）**：Use after free in PictureInPicture in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 52. CVE-2026-121156｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:23.283)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:23.283 / 2026-11-04T05:18:35.067
- **官方描述（原文）**：Buffer overflow in Dawn in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 53. CVE-2026-121148｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:23.150)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:23.150 / 2026-11-04T05:18:34.813
- **官方描述（原文）**：Use after free in ANGLE in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 54. CVE-2026-121126｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:20.860)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:20.860 / 2026-11-04T05:18:34.150
- **官方描述（原文）**：Use after free in Core in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 55. CVE-2026-121114｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:19.087)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:19.087 / 2026-11-03T22:19:37.963
- **官方描述（原文）**：Use after free in TabStrip in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 56. CVE-2026-121104｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:16.653)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:16.653 / 2026-11-03T22:19:37.630
- **官方描述（原文）**：Incorrect authorization in FileSystem in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 57. CVE-2026-121089｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:14.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:14.543 / 2026-11-04T05:18:32.807
- **官方描述（原文）**：Use after free in WebGPU in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 58. CVE-2026-121086｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:14.123)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:14.123 / 2026-11-03T22:19:36.290
- **官方描述（原文）**：Buffer overflow in Skia in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 59. CVE-2026-121077｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:12.893)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:12.893 / 2026-11-03T22:19:35.277
- **官方描述（原文）**：Use after free in Mobile in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 60. CVE-2026-121076｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:12.757)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:12.757 / 2026-11-03T22:19:35.120
- **官方描述（原文）**：Use after free in WebXR in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 61. CVE-2026-121074｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:12.463)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:12.463 / 2026-11-04T05:18:32.027
- **官方描述（原文）**：Memory corruption in GPU in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 62. CVE-2026-121071｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:12.057)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:12.057 / 2026-11-04T05:18:31.810
- **官方描述（原文）**：Incorrect authorization in FileSystem in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 63. CVE-2026-121060｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:10.570)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:10.570 / 2026-11-03T22:19:33.787
- **官方描述（原文）**：Incorrect authorization in FileSystem in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 64. CVE-2026-121037｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:07.000)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:07.000 / 2026-11-04T05:18:30.940
- **官方描述（原文）**：Out of bounds write in ANGLE in Google Chrome on on Windows prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 65. CVE-2026-121035｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:06.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:06.730 / 2026-11-04T05:18:30.717
- **官方描述（原文）**：Use after free in Prerender in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 66. CVE-2026-121034｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:06.593)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:06.593 / 2026-11-03T22:19:32.270
- **官方描述（原文）**：Use after free in Views in Google Chrome on on Windows prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 67. CVE-2026-121030｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:06.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:06.013 / 2026-11-03T22:19:32.107
- **官方描述（原文）**：Incorrect authorization in DevTools in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 68. CVE-2026-121022｜AxxonSoft / Axxon One
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T09:17:11.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00378 / percentile=0.31869
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T09:17:11.980 / 2026-11-03T21:17:05.430
- **官方描述（原文）**：Use of Default Password (CWE-1393) in the web client in AxxonSoft Axxon One before 3.0.0 on Windows and Linux allows a remote unauthenticated attacker to log in as the built-in administrator with the default credentials on a newly installed system, because the web client did not enforce the mandatory change of the default password on first login.

### 69. CVE-2026-120931｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T22:19:31.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T22:19:31.900 / 2026-11-03T22:19:32.063
- **官方描述（原文）**：Out of bounds write in WebGL in Google Chrome on on Android prior to 156.0.8078.47 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 70. CVE-2026-119084｜AWS / amazon-redshift-jdbc-driver
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T22:19:29.220)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T22:19:29.220 / 2026-11-03T22:19:29.220
- **官方描述（原文）**：Unsafe reflection in the connection parameter and credentials profile handling of Amazon Redshift JDBC Driver before 2.3.0 might allow an actor who can influence the JDBC connection URL or the AWS credentials profile to execute arbitrary code in the application context, provided a suitable class is available on the application classpath. To remediate this issue, users should upgrade to version 2.3.0 or later.

### 71. CVE-2026-115732｜Perforce / Puppet Enterprise
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:02.033)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:02.033 / 2026-11-03T21:17:02.033
- **官方描述（原文）**：Incorrect authorization in the certificate-name matching of trapperkeeper-authorization, as used by Puppet Server, in the affected products, allows a client that holds a CA-signed certificate whose name extends or shortens an authorized hostname to be authorized as that host. This enables impersonation of other nodes and, in Puppet Enterprise, access to certificate-authority administration and remote command execution on managed nodes. Exploitation requires a certificate with a colliding name, which the certificate authority issues by approval or autosign.

### 72. CVE-2026-115731｜Perforce / Puppet Enterprise
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:01.867)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:01.867 / 2026-11-03T21:17:01.867
- **官方描述（原文）**：Deserialization of untrusted data in the report-processing code of Puppet, as used by Puppet Server, in the affected releases, allows a client that holds any CA-signed agent certificate to execute arbitrary code on the Puppet Server as its service user by submitting a report containing a crafted rich-data type via PUT request. Where the certificate authority autosigns requests without strong verification, an unauthenticated network attacker can obtain such a certificate.

### 73. CVE-2026-114549｜NoMachine / NoMachine
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T00:17:22.627)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T00:17:22.627 / 2026-11-04T00:17:22.627
- **官方描述（原文）**：NoMachine nxwebrunner Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of NoMachine. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 4443 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account. Was ZDI-CAN-30685.

### 74. CVE-2026-112917｜Docker / Docker Desktop
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T19:17:53.727)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T19:17:53.727 / 2026-11-04T05:18:29.063
- **官方描述（原文）**：In Docker Desktop for Windows with the WSL2 backend, an unprivileged Linux container can use 32-bit socketcall to bypass the default seccomp restriction on AF_VSOCK. This can expose host-facing services and Windows files accessible to the logged-in user. The issue affects x86-64 WSL2; LinuxKit-based backends are unaffected. The issue is fully fixed only with Docker Desktop 4.98.0 or later and WSL 3.0.3 or later. Docker Desktop 4.98.0 or later running on an older WSL remains affected.

### 75. CVE-2026-112354｜Etrel d.o.o. / Etrel INCH
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T22:17:44.660)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T22:17:44.660 / 2026-11-03T22:17:44.660
- **官方描述（原文）**：Etrel INCH AC charging station management web interface prior to firmware versions 7.1.2 and 8.0.1 contains a hard-coded default credentials vulnerability that allows remote attackers to gain full Administrator access by authenticating with the factory-default account. Attackers can log in over cleartext HTTP to obtain complete charger configuration, OCPP ChargePoint Identity, and CSMS WebSocket connection details, enabling unauthorized administrative control of the charging station.

### 76. CVE-2026-109593｜SonicWall / Global Management System (GMS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T17:17:53.690)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T17:17:53.690 / 2026-11-03T20:32:50.687
- **官方描述（原文）**：An unauthenticated attacker with network access to the SonicWall GMS 9.5.2 and earlier versions may be able to read internal GMS files, potentially exposing sensitive information.

### 77. CVE-2022-29966｜Emerson / Ovation
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T23:17:20.353)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T23:17:20.353 / 2026-11-03T23:17:20.353
- **官方描述（原文）**：Emerson Ovation has several protocols that have no authentication, which could allow an attacker to change controller configuration or cause a denial-of-service condition.

### 78. CVE-2026-63499｜zeroturnaround / zt-zip
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T18:18:04.083)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T18:18:04.083 / 2026-11-03T20:18:16.777
- **官方描述（原文）**：zt-zip is a Java library that provides convenience methods for ZIP archive manipulation. Prior to 1.18.1, ZipUtil.unpack(...) can apply stored ZIP-entry permissions to the extraction output directory when an entry name such as / or ./ resolves to that directory itself. Because the path traversal checks permit self-referencing entries that do not escape the destination, the unpacker's permission-handling path can replace restrictive output-directory permissions with attacker-supplied permissions. This affects applications that unpack untrusted ZIP files, and POSIX systems demonstrate the issue directly, while ZTFilePermissionsUtil.fetchDefaultStrategy provides fallback permission handling on other supported systems. This issue is fixed in version 1.18.1.

### 79. CVE-2026-63475｜isomorphic-git / isomorphic-git
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T20:18:15.903)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T20:18:15.903 / 2026-11-03T22:19:47.803
- **官方描述（原文）**：isomorphic-git is a pure JavaScript implementation of Git for Node.js and browsers. Prior to 1.38.6, isomorphic-git persists server-supplied circular symref= capabilities through updateRemoteRefs, and GitRefManager.resolve() follows the resulting loose symbolic references without a default depth limit or cycle detection. After a clone from a malicious or man-in-the-middle-controlled remote, operations such as log, status, checkout, and branch that resolve refs/remotes/origin/a or refs/remotes/origin/b do not terminate. The circular references remain on disk, leaving the repository unusable for the application and causing a persistent denial of service. This issue is fixed in version 1.38.6.

### 80. CVE-2026-121628｜bagisto / bagisto
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T18:17:58.990)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T18:17:58.990 / 2026-11-03T23:17:35.873
- **官方描述（原文）**：Bagisto before 2.3.16 and 2.4.x before 2.4.1 contains a race condition vulnerability in manageCartRule() that allows attackers to redeem single-use coupons multiple times. Attackers can submit concurrent order requests to the onepage orders checkout endpoint, bypassing unlocked times_used checks to apply discounts repeatedly.

### 81. CVE-2026-121578｜Amidaware / Tactical RMM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T16:17:29.480)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T16:17:29.480 / 2026-11-03T18:17:57.950
- **官方描述（原文）**：Tactical RMM contains a stored XSS vulnerability caused by improperly validated input or encode output for various fields, enabling HTML/JavaScript to be stored in the tools database, which is then executed in the browsers of users when they view content containing the infected objects, leading to account takeover or code execution.

### 82. CVE-2026-121552｜dromara / domain-admin
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T16:17:27.263)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T16:17:27.263 / 2026-11-03T17:18:10.627
- **官方描述（原文）**：Dromara domain-admin before 1.6.79 contains a missing authorization vulnerability in the POST /api/getGroupUserList handler that allows authenticated users to read other groups' members. Attackers can enumerate sequential group_id values to disclose member usernames, leader and edit-permission flags, and owner usernames of groups they do not belong to.

### 83. CVE-2026-121544｜koodo-reader / koodo-reader
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T16:17:25.857)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T16:17:25.857 / 2026-11-03T17:18:10.353
- **官方描述（原文）**：Koodo Reader through 2.4.6 contains a path traversal vulnerability in the self-hosted HTTP server's OPDS handlers that allows authenticated attackers to read files outside the upload directory. Attackers can upload a crafted books.db with a cover value containing ../ sequences, then request /opds/cover/{key} to read files accessible to the server process.

### 84. CVE-2026-121509｜未確認 / Headless CMS Plugin
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T21:17:37.023)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T21:17:37.023 / 2026-11-03T23:17:34.013
- **官方描述（原文）**：A security flaw has been discovered in Headless CMS Plugin up to 2.0.4 on WordPress. This affects the function get_required_post_data of the file /wp-json/rae/v1/post of the component REST API. The manipulation of the argument post_id/post_slug results in information disclosure. The attack may be launched remotely. The exploit has been released to the public and may be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 85. CVE-2026-121433｜AzuraCast / AzuraCast
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:34.437)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:34.437 / 2026-11-03T17:18:09.527
- **官方描述（原文）**：AzuraCast before 0.24.0 contains a stored CSV formula injection vulnerability that allows station users with Media permission to persist formula-prefixed metadata via bulk media import. Attackers can import crafted titles, artists, or custom fields through /api/station/{station_id}/files/bulk so formulas evaluate when other users open exported CSVs in spreadsheets.

### 86. CVE-2026-121421｜surrealdb / surrealdb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:32.340)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:32.340 / 2026-11-03T17:18:09.110
- **官方描述（原文）**：SurrealDB 3.1.0 before 3.3.0 contains a server-side request forgery vulnerability in network-capability matching because port-specific --deny-net rules (HOST:PORT or IP:PORT) match only a literal host string, while the resolved-IP check discards the port. Authenticated users can call http::* functions with a hostname resolving to a denied IP, or the IP of a denied hostname, to reach blocked internal services.

### 87. CVE-2026-121405｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:29.057)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:29.057 / 2026-11-03T18:17:57.333
- **官方描述（原文）**：FreeRDP before 3.32.2 fails to cap the OutputBufferLength in serial device-control IRP requests, allowing malicious servers to trigger excessive memory allocation. Attackers running a server with serial redirection can send an IRP_MJ_DEVICE_CONTROL request with IOCTL_USBPRINT_GET_1284_ID and a near-maximum length to exhaust client memory.

### 88. CVE-2026-121401｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:28.360)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:28.360 / 2026-11-03T17:18:08.817
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a denial of service vulnerability where rdg_process_packet dispatches a PKT_TYPE_EXTENDED_AUTH_MSG without verifying negotiated mode or auth context. A malicious or compromised RD Gateway can send the extended-auth packet before tunnel authentication, triggering a null-pointer dereference that crashes the client.

### 89. CVE-2026-121397｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:27.630)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:27.630 / 2026-11-03T17:18:08.667
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a heap buffer over-read vulnerability in save_png_to_buffer() that allows malicious RDP servers to leak client memory by sending 16 bpp DIB clipboard data. Attackers can offer a CF_DIB BI_BITFIELDS image that, when converted to PNG for a local application, embeds client heap bytes into the clipboard image.

### 90. CVE-2026-120988｜NAVER / billboard.js
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T08:17:15.070)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：0.00159 / percentile=0.05029
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T08:17:15.070 / 2026-11-03T20:18:12.953
- **官方描述（原文）**：billboard.js before 4.1.3 allows an attacker to execute malicious JavaScript due to improper sanitization of series ids during legend template rendering.

### 91. CVE-2026-118488｜Eclipse Foundation / Eclipse Vert.x
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:24.647)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:24.647 / 2026-11-03T18:17:54.760
- **官方描述（原文）**：In Eclipse Vert.x versions [4.0.0, 4.5.35] or [5.0.0, 5.2.2], when a malicious server keeps sending bytes on an EOL-terminated line (not length-prefixed, for example a simple string [1]), we'll keep growing the buffer without bounds, eventually leading to an OOM. We need to have a configurable limit for EOL-terminated lines. If a malicious server sends a specially crafted RESP response (for example a bulk string [2] with missing CRLF trailer), the parser enters an infinite loop where it keeps parsing the same buffer and pushing the same response to the caller, which may lead e.g. to an OOM if the consumer just buffers the responses. We must fix the parser to avoid this infinite looping.

### 92. CVE-2026-116845｜netbox-community / netbox
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T18:17:54.530)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T18:17:54.530 / 2026-11-03T20:18:11.670
- **官方描述（原文）**：NetBox from 2.9.0 before 4.7.4 contains a broken access control vulnerability in BulkComponentCreateView that allows authenticated users to bypass view permissions on parent devices and virtual machines. Attackers with add-component permission can submit arbitrary device or VM IDs, or _all with filters, to view out-of-scope device details and create components on them.

### 93. CVE-2026-121531｜未確認 / Umami
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T22:19:46.370)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T22:19:46.370 / 2026-11-03T23:17:34.340
- **官方描述（原文）**：A vulnerability has been found in Umami 3.3.x/3.4.0/3.4.1. This affects an unknown part of the file src/app/api/auth/login/route.ts of the component 2FA Policy Handler. The manipulation leads to use of single-factor authentication. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 94. CVE-2026-121389｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T15:17:26.167)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T15:17:26.167 / 2026-11-03T21:13:36.777
- **官方描述（原文）**：FreeRDP from 3.27.0 before 3.32.2 contains a denial of service vulnerability in rdpdr_dump_packet that allows malicious RDP servers to abort clients by sending malformed RDPDR device-list announcements. Attackers can declare a DeviceDataLength exceeding the received packet, triggering a fatal Stream_Seek assertion when device redirection, TRACE logging, and WinPR assertions are enabled.

### 95. CVE-2026-121263｜phpMyAdmin / MoTranslator
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T18:17:57.087)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T18:17:57.087 / 2026-11-03T23:17:33.677
- **官方描述（原文）**：A vulnerability was determined in phpMyAdmin MoTranslator up to 6.0.1. The impacted element is the function Loader::getTranslator of the file motranslator-master/src/Loader.php. Executing a manipulation of the argument locale can lead to path traversal. The attack may be performed from remote. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-119977｜WordPress / WordPress Core
- **Title**：WordPress WordPress Core Time-of-check Time-of-use (TOCTOU) Race Condition Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-03 / due_date=2026-11-06
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WordPress WordPress Core contains a time-of-check time-of-use (TOCTOU) race condition vulnerability that could allow unauthenticated attackers to execute code on the server during the upgrade window. This is due to predictable, web-accessible staging paths used during full-package core upgrades.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-118527｜Ivanti / Connect Secure
- **Title**：Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-30 / due_date=2026-11-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ivanti Connect Secure contains a generation of predictable numbers or identifiers vulnerability that allows a remote authenticated attacker to upload files with attacker-controlled content to a known location on disk. This vulnerability can be chained with CVE-2026-104935 and CVE-2026-111357.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-63470 | P3 / 38 | koxudaxi / fastapi-code-generator | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-44266 | P3 / 38 | enspirit / elo | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-38600 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-63501 | WATCH / 30 | Agamnentzar / ag-psd | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63395 | WATCH / 30 | isomorphic-git / isomorphic-git | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121548 | WATCH / 30 | jarun / nnn | v4.0 8.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121449 | WATCH / 30 | Finsys / dockhand | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121445 | WATCH / 30 | darylldoyle / svg-sanitizer | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121437 | WATCH / 30 | lepture / mistune | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121429 | WATCH / 30 | AzuraCast / AzuraCast | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121425 | WATCH / 30 | nodemailer / nodemailer | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121417 | WATCH / 30 | surrealdb / surrealdb | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121409 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121393 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121260 | WATCH / 30 | Ziroom / ZHOME A0101 | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-118487 | WATCH / 30 | Eclipse Foundation / Eclipse Vert.x | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-95860 | WATCH / 28 | node-opcua / node-opcua | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-95733 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / Fabric Composer | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-95732 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / Fabric Composer | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-95731 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / Fabric Composer | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92190 | WATCH / 28 | Quest / Foglight for Databases | v3.0 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92189 | WATCH / 28 | Quest / Foglight for Databases | v3.0 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92188 | WATCH / 28 | Quest / Foglight for Databases | v3.0 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89292 | WATCH / 28 | Eclipse Foundation / Eclipse Mnestix | v4.0 9.2 (CRITICAL) | 0.00453 / percentile=0.39387 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-82158 | WATCH / 28 | Dell / Wyse Management Suite | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-63471 | WATCH / 28 | koxudaxi / fastapi-code-generator | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-63469 | WATCH / 28 | koxudaxi / fastapi-code-generator | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-44267 | WATCH / 28 | enspirit / elo | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：1；缺少 Product：1；缺少 Title：28。
- EPSS 未確認：29；Exploitation status 未確認：10。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-04T07:06:27.852213+00:00`；Delta generated at：`2026-11-04T07:06:27.852213+00:00`。

---

## 可驗證資料來源

- **CVE-2026-119977** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119977) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (wordpress.org)](https://wordpress.org/news/2026/10/wordpress-7-1-4) · [Vendor / Advisory (wordfence.com)](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-core/wordpress-core-470-713-unauthenticated-upgrade-window-staged-installer-remote-code-execution) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-118527** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118527) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (hub.ivanti.com)](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935?language=en_US) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-63470** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63470)
- **CVE-2026-44266** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-44266)
- **CVE-2026-38600** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-38600)
- **CVE-2026-63501** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63501)
- **CVE-2026-63395** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63395)
- **CVE-2026-121548** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121548)
- **CVE-2026-121449** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121449)
- **CVE-2026-121445** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121445)
- **CVE-2026-121437** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121437)
- **CVE-2026-121429** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121429)
- **CVE-2026-121425** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121425)
- **CVE-2026-121417** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121417)
- **CVE-2026-121409** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121409)
- **CVE-2026-121393** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121393)
- **CVE-2026-121260** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121260)
- **CVE-2026-118487** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118487)
- **CVE-2026-95860** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95860)
- **CVE-2026-95733** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95733)
- **CVE-2026-95732** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95732)
- **CVE-2026-95731** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95731)
- **CVE-2026-92190** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92190)
- **CVE-2026-92189** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92189)
- **CVE-2026-92188** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92188)
- **CVE-2026-89292** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89292) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89292)
- **CVE-2026-82158** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82158)
- **CVE-2026-63471** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63471)
- **CVE-2026-63469** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63469)
- **CVE-2026-44267** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-44267)
- **CVE-2026-4052** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-4052) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-4052)
- **CVE-2026-28336** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-28336)
- **CVE-2026-22058** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-22058)
- **CVE-2026-13594** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13594) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-13594)
- **CVE-2026-121802** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121802)
- **CVE-2026-121615** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121615)
- **CVE-2026-121609** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121609)
- **CVE-2026-121607** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121607)
- **CVE-2026-121606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121606)
- **CVE-2026-121392** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121392)
- **CVE-2026-121249** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121249)
- **CVE-2026-121247** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121247)
- **CVE-2026-121246** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121246)
- **CVE-2026-121241** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121241)
- **CVE-2026-121234** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121234)
- **CVE-2026-121229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121229)
- **CVE-2026-121214** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121214)
- **CVE-2026-121202** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121202)
- **CVE-2026-121200** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121200)
- **CVE-2026-121189** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121189)
- **CVE-2026-121185** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121185)
- **CVE-2026-121156** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121156)
- **CVE-2026-121148** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121148)
- **CVE-2026-121126** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121126)
- **CVE-2026-121114** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121114)
- **CVE-2026-121104** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121104)
- **CVE-2026-121089** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121089)
- **CVE-2026-121086** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121086)
- **CVE-2026-121077** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121077)
- **CVE-2026-121076** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121076)
- **CVE-2026-121074** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121074)
- **CVE-2026-121071** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121071)
- **CVE-2026-121060** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121060)
- **CVE-2026-121037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121037)
- **CVE-2026-121035** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121035)
- **CVE-2026-121034** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121034)
- **CVE-2026-121030** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121030)
- **CVE-2026-121022** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121022) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-121022)
- **CVE-2026-120931** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120931)
- **CVE-2026-119084** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119084)
- **CVE-2026-115732** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115732)
- **CVE-2026-115731** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115731)
- **CVE-2026-114549** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114549)
- **CVE-2026-112917** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112917)
- **CVE-2026-112354** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112354)
- **CVE-2026-109593** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109593)
- **CVE-2022-29966** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-29966)
- **CVE-2026-63499** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63499)
- **CVE-2026-63475** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63475)
- **CVE-2026-121628** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121628)
- **CVE-2026-121578** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121578)
- **CVE-2026-121552** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121552)
- **CVE-2026-121544** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121544)
- **CVE-2026-121509** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121509)
- **CVE-2026-121433** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121433)
- **CVE-2026-121421** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121421)
- **CVE-2026-121405** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121405)
- **CVE-2026-121401** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121401)
- **CVE-2026-121397** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121397)
- **CVE-2026-120988** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120988) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-120988)
- **CVE-2026-118488** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118488)
- **CVE-2026-116845** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116845)
- **CVE-2026-121531** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121531)
- **CVE-2026-121389** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121389)
- **CVE-2026-121263** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121263)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
