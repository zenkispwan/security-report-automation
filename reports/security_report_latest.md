# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**87** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=1、EXPLOITATION_CHANGED=1、NEW_CVE=85。
- Intelligence 候選：**30** 筆；P1 **1**、P2 **0**、P3 **11**、WATCH **18**。
- Baseline：state / generated_at=2026-09-17T14:16:33.251179+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-87886。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **87** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-20284｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：EXPLOITATION_CHANGED (from=active; to=none)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T21:17:09.090 / 2026-09-18T04:17:36.943
- **官方描述（原文）**：A vulnerability in the SXP REST API of Cisco ISE could allow an authenticated, remote attacker to conduct SQL injection attacks. This vulnerability is due to insufficient validation of user-supplied input in REST API calls. An attacker could exploit this vulnerability by sending crafted input to an affected device. A successful exploit could allow the attacker to view or modify data on the underlying database for the affected device. In single-node deployments, successful exploitation of this vulnerability could cause the affected ISE node to become unavailable, resulting in a DoS condition. In that condition, endpoints that have not already authenticated would be unable to access the network until the node is restored. To exploit this vulnerability, the attacker must have valid administrative credentials, have the SXP service enabled, and have at least one SXP connection configured.

### 2. CVE-2026-87886｜Acronis / Backup
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T23:18:53.763)
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-17T23:18:53.763 / 2026-09-18T00:17:48.480
- **官方描述（原文）**：Acronis Backup plugin for cPanel & WHM and extension for Plesk contains an incorrect default permissions vulnerability that could allow for privilege escalation.

### 3. CVE-2026-92960｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:02.290)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:02.290 / 2026-09-17T15:17:01.170
- **官方描述（原文）**：vm2 before 3.11.6 fails to restrict access to os and dns builtins under the builtin: ['*'] configuration, allowing sandbox code to read host process identity and network topology. Attackers can invoke dns.setServers() to hijack the host process DNS resolver globally, redirecting all subsequent host DNS queries through an attacker-controlled resolver.

### 4. CVE-2026-92957｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:01.813)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:01.813 / 2026-09-17T18:17:15.430
- **官方描述（原文）**：vm2 through 3.11.6 does not normalize `node:`-prefixed builtin specifiers when evaluating user-supplied negative (deny) entries in a NodeVM wildcard require policy. Although NodeVM strips the `node:` prefix during require() resolution, negative wildcard entries are matched by exact string comparison against the canonical builtin names, so a policy such as `new NodeVM({ require: { builtin: ['*', '-node:child_process'] } })` fails to deny the canonical `child_process` module. Sandboxed code can therefore obtain the host `child_process` builtin via `require('child_process')` or `require('node:child_process')`, gaining references to process-spawning APIs such as execSync and spawn, which is equivalent to host command-execution capability for untrusted sandbox code. Fixed in vm2 3.11.7. (Suggested title: "vm2 before 3.11.7: NodeVM builtin deny-list bypass via node:-prefixed specifiers exposes child_process")

### 5. CVE-2026-92955｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:01.480)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:01.480 / 2026-09-17T15:17:01.040
- **官方描述（原文）**：vm2 before 3.11.8 contains a sandbox escape vulnerability in NodeVM that allows attackers to access the host __proto__ getter/setter through console._stdout and console._stderr. Attackers can overwrite EventEmitter.prototype.emit and trigger process events to execute code with process context, bypassing code generation restrictions.

### 6. CVE-2026-92950｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:00.637)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:00.637 / 2026-09-17T15:17:00.910
- **官方描述（原文）**：vm2 before 3.11.7 contains a sandbox escape vulnerability in the CLI tool that allows attackers to execute arbitrary code in the host Node.js process. Attackers can supply a malicious script file to the vm2 CLI that uses require(__filename) to re-execute itself in the host realm, bypassing sandbox isolation and accessing host modules like fs and child_process.

### 7. CVE-2026-92947｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:00.140)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:00.140 / 2026-09-17T16:18:34.667
- **官方描述（原文）**：vm2 before 3.11.7 exposes Node's shared Buffer pool to sandboxed code, allowing disclosure of host memory used by Buffer.from, Buffer.concat, and related allocations. Sandboxed code can read and write to host-realm buffers by acquiring ArrayBuffers from small allocations, leading to sensitive data exposure and potential denial-of-service.

### 8. CVE-2026-92941｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:59.310)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:59.310 / 2026-09-17T16:18:34.520
- **官方描述（原文）**：vm2 versions from 3.11.3 before 3.11.7 expose the host tls module to NodeVM sandbox code, allowing attackers to call tls.setDefaultCACertificates() and replace process-wide certificate authorities. Attackers with access to allowed tls and url builtins can use URLSearchParams to create host-realm arrays and manipulate the TLS trust store, enabling subsequent host HTTPS clients to accept attacker-controlled certificates.

### 9. CVE-2026-92939｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:58.970)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:58.970 / 2026-09-17T15:17:00.650
- **官方描述（原文）**：vm2 3.11.3 through 3.11.6 exposes the host Node.js crypto module to a NodeVM sandbox when the crypto builtin is allowed. The module is presented via a recursive read-only proxy, but its callable exports still execute with host-process authority. Sandboxed JavaScript can therefore call crypto.setEngine() with a filesystem path to an attacker-supplied native library (for example, one bundled in an untrusted plugin package already written to disk); OpenSSL asks the operating-system dynamic loader to load the file, and the library's constructor executes native code in the host process before engine-symbol validation rejects it. Exploitation requires only the crypto builtin and does not require fs, process, module, child_process, worker_threads, vm, or inspector access, resulting in a sandbox escape and arbitrary native code execution. Fixed in 3.11.7.

### 10. CVE-2026-92934｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:57.513)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:57.513 / 2026-09-17T15:17:00.520
- **官方描述（原文）**：vm2 before 3.11.8 contains an incomplete fix for Error.cause sanitization that allows sandbox escape when revisited host-wrapped AggregateError objects are caught within a single exception handler traversal. Attackers can exploit cycle detection bypass in handleException to access unsanitized host proxies embedded in the errors array, enabling full remote code execution and process information disclosure from the sandbox.

### 11. CVE-2026-63472｜vendurehq / vendure
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T15:16:49.743)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T15:16:49.743 / 2026-09-17T21:16:02.560
- **官方描述（原文）**：Vendure is an open-source headless commerce platform. Prior to 3.7.0, ExternalAuthenticationService.createCustomerAndUser in packages/core/src/service/helpers/external-authentication/external-authentication.service.ts selects an existing customer user by emailAddress and attaches a newly presented ExternalAuthenticationMethod without requiring verified to be true. In deployments with a custom external AuthenticationStrategy that forwards an email whose ownership the provider has not verified, an attacker can authenticate with a victim's email and bind the attacker's external identity to the victim's existing account. This can expose orders, addresses, and personal information and permit account changes or orders as the victim. Native-only email and password deployments and external strategies that always require provider-verified email ownership are unaffected, and new-account creation for an unused email remains permitted. This issue is fixed in version 3.7.0.

### 12. CVE-2026-54626｜HappySeaFox / sail
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T20:16:51.970)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T20:16:51.970 / 2026-09-17T21:17:17.163
- **官方描述（原文）**：SAIL is a cross-platform library for loading and saving images with support for animation, metadata, and ICC profiles. In 0.9.10 and earlier, the TGA_INDEXED_RLE path selected by image_type == 9 allocates an image buffer using the one-byte-per-pixel SAIL_PIXEL_FORMAT_BPP8_INDEXED format returned by tga_private_sail_pixel_format() in src/sail-codecs/tga/helpers.c, while sail_codec_load_frame_v8_tga() in src/sail-codecs/tga/tga.c derives a two-to-four-byte pixel_size from an attacker-controlled header bpp value from 9 through 32. Loading a crafted color-mapped run-length-encoded TGA through sail_load_from_file() or sail_load_from_memory() therefore writes attacker-controlled bytes beyond the heap pixel buffer. The pixel-count clamp added for CVE-2026-40494 does not constrain the per-pixel write width, so this issue is an incomplete fix of that vulnerability and can cause heap corruption, a reliable crash, or potential code execution. This issue is fixed in version 1.0.0.

### 13. CVE-2026-47252｜julien040 / anyquery
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T19:16:48.083)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T19:16:48.083 / 2026-09-17T20:16:49.803
- **官方描述（原文）**：Anyquery is an SQL query engine built on top of SQLite. Prior to 0.4.5, authenticated users with INSERT or UPDATE access to affected macOS virtual tables can execute operating-system commands because the Chrome plugin and equivalent Brave, Edge, and Safari variants interpolate a SQL-controlled URL into AppleScript or JXA source passed to osascript. In plugins/chrome/tabs.go, tabsTable.Insert() passes the URL through fmt.Sprintf(newTabScript, url), and tabsTable.Update() uses fmt.Sprintf(setURLScript, pk, url). A URL containing quote and newline characters can break out of the intended string or property record and append script statements, resulting in arbitrary command execution with the privileges of the anyquery process on the macOS host. This issue is fixed in version 0.4.5.

### 14. CVE-2026-93014｜RosarioSIS / RosarioSIS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T16:18:35.670)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T16:18:35.670 / 2026-09-17T16:18:35.670
- **官方描述（原文）**：RosarioSIS versions before 12.9 fail to validate the filename request parameter in Users and Students modules, allowing authenticated users to unlink allow-listed files via path traversal. Attackers can use parent-directory sequences to escape upload directories and delete CSS, XML, JSON resources and other users' documents throughout the installation.

### 15. CVE-2026-92985｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T15:17:01.840)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T15:17:01.840 / 2026-09-17T16:18:35.200
- **官方描述（原文）**：SiYuan versions before 3.8.4 fail to escape bookmark labels imported from notebook files when rendering them in the dock tree. Attackers can craft malicious .sy notebook files with unescaped HTML in bookmark attributes that execute scripts in the Electron renderer with access to child_process for command execution.

### 16. CVE-2026-92971｜InternLM / lmdeploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:03.190)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:03.190 / 2026-09-17T15:17:01.330
- **官方描述（原文）**：InternLM LMDeploy through 0.17.0 contains a reachable assertion vulnerability in the DistServe decode migration loop that allows unauthenticated attackers to terminate the inference engine. Attackers can submit a migration_request with an empty remote_block_ids list to trigger an AssertionError that crashes the engine loop and causes subsequent inference requests to fail.

### 17. CVE-2026-92952｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:00.987)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.9 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:00.987 / 2026-09-17T16:18:34.807
- **官方描述（原文）**：vm2 versions 3.11.4 through 3.11.6 incompletely filter Node.js registered internal symbols across the sandbox boundary. The extraction filters in lib/setup-sandbox.js and the cross-realm symbol checks and write traps in lib/bridge.js use a fixed list of known dangerous registered symbols that omits nodejs.stream.disturbed and nodejs.stream.errored, which are exposed on host WebStream prototypes on newer Node.js releases (validated on Node.js v25.8.0). When the embedder exposes a host WebStream object and the host stream/web module to the sandbox, sandbox code can obtain the real host symbols via Object.getOwnPropertySymbols(streamWeb.ReadableStream.prototype) and use them as write keys on host stream objects, corrupting host-visible stream state — for example making stream.Readable.isDisturbed() return false for an already-consumed stream. This can bypass host logic that relies on Node's public stream-state helpers to enforce one-shot body consumption, reject errored streams, or decide whether a stream is safe to hand to another component. It is not a host code-execution primitive in the reported proof of vulnerability. This is an incomplete fix for the earlier nodejs.* symbol filtering issue. Fixed in vm2 3.11.7.

### 18. CVE-2026-89418｜Google / protobuf-javascript (aka google-protobuf npm package)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:52.157)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:52.157 / 2026-09-17T20:18:52.523
- **官方描述（原文）**：google-protobuf contains an unbounded recursion when parsing unknown protobuf group fields. An attacker can send a small crafted payload of deeply nested START_GROUP wire bytes to any Node.js service that calls the generated deserializeBinary() API, causing a RangeError: Maximum call stack size exceeded and crashing the process. No authentication or prior knowledge of the schema is required.

### 19. CVE-2026-86038｜libp2p / js-libp2p
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T16:18:16.927)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T16:18:16.927 / 2026-09-17T18:17:12.203
- **官方描述（原文）**：libp2p is a JavaScript implementation of the libp2p networking stack. From 15.0.0 until 16.0.5, @libp2p/gossipsub uses the default StrictSign policy in packages/gossipsub/src/utils/buildRawMessage.ts, where validateToRawMessage verifies a signature with attacker-controlled msg.key but skips binding that key to msg.from when the claimed author is an RSA peer ID that does not inline a public key. An unauthenticated attacker can place a victim RSA peer ID in msg.from, sign the message with the attacker's private key, and supply the attacker's public key in msg.key, causing the message to be accepted and propagated as authored by the victim. Applications that trust message.from for validators, authorization, accounting, moderation, reputation, or audit logging can process attacker-controlled data under false origin attribution. The issue is fixed in version 16.0.5.

### 20. CVE-2026-85715｜mattiasw / ExifReader
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T16:18:15.790)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T16:18:15.790 / 2026-09-17T16:18:15.790
- **官方描述（原文）**：ExifReader is a JavaScript Exif information parser. Prior to 4.41.1, ExifReader parses attacker-controlled HEIC or AVIF ISO-BMFF files in getItems() within src/image-header-iso-bmff-iloc.js and trusts iloc itemCount and extentCount values while allocating an extent object for every nested-loop iteration. When offsetSize, lengthSize, baseOffsetSize, and indexSize are zero, the extent fields consume no input bytes and the buffer offset does not advance, but the parser can still allocate up to itemCount multiplied by extentCount objects without an allocation budget. A small malicious iloc box can therefore cause hundreds of megabytes of heap growth or exhaust system memory, terminating a Node.js process and denying service to web, desktop, or mobile applications that parse untrusted images. The zero field widths are valid ISO-BMFF values indicating absent fields, so the vulnerable parser must bound work rather than relying on offset advancement. The issue is fixed in version 4.41.1.

### 21. CVE-2026-77614｜opencast / opencast
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T15:16:51.503)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T15:16:51.503 / 2026-09-17T16:17:42.480
- **官方描述（原文）**：Opencast is a free, open-source platform to support the management of educational audio and video content. Prior to versions 19.7 and 20.2, the default security configuration in etc/security/mh_default_org.xml accepts a client-selected JSESSIONID from the ;jsessionid= URL path parameter and does not replace it when the victim logs in. An unauthenticated attacker can send a crafted link to a victim whose browser has no active Opencast session cookie, wait for the victim to authenticate, and then reuse the known identifier as the victim's authenticated session. This can expose the victim's data and actions and can produce full administrative account takeover when the victim is an administrator. This issue is fixed in versions 19.7 and 20.2.

### 22. CVE-2026-63460｜vendurehq / vendure
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T15:16:49.447)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T15:16:49.447 / 2026-09-17T21:16:02.560
- **官方描述（原文）**：Vendure is an open-source headless commerce platform. Prior to 3.6.5, the public Shop GraphQL API allows an unauthenticated caller to supply a catastrophically backtracking pattern through StringOperators.regex. packages/core/src/service/helpers/list-query-builder/parse-filter-params.ts passes the raw pattern to the REGEXP implementation registered by packages/core/src/service/helpers/list-query-builder/list-query-builder.ts, and better-sqlite3 and sqljs evaluate it synchronously in the Node.js event loop. ShopProductsResolver.products is publicly reachable, so one nested-quantifier pattern can block request processing and make the storefront and admin API unavailable, while repeated requests can sustain denial of service. PostgreSQL and MySQL or MariaDB deployments do not execute this regular expression in the Node.js event loop. This issue is fixed in version 3.6.5.

### 23. CVE-2026-54504｜andrea9293 / mcp-documentation-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T19:16:50.517)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T19:16:50.517 / 2026-09-17T20:16:51.120
- **官方描述（原文）**：MCP Documentation Server is a local-first document management and semantic search server for AI coding agents. From 1.13.0 until 1.13.1, the automatically started Web UI in src/server.ts calls startWebServer in src/web-server.ts with START_WEB_UI enabled by default and WEB_PORT set to 3080. startWebServer uses app.listen(PORT) without a host, which binds the unauthenticated document-management API to all interfaces rather than localhost. A network-reachable client can invoke GET /api/documents, GET /api/documents/:id, POST /api/documents, POST /api/search-all, DELETE /api/documents/:id, and GET /api/config without credentials to enumerate and read documents, search the corpus, insert or delete documents, and tamper with the MCP assistant's knowledge base. The service must be reachable from the attacker's LAN, VM network, container bridge, VPN, or another routed network, and the issue does not provide remote code execution. This issue is fixed in 1.13.1.

### 24. CVE-2026-54446｜Labs64 / NetLicensing-MCP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T18:16:46.040)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T18:16:46.040 / 2026-09-17T20:16:50.843
- **官方描述（原文）**：NetLicensing MCP Server is a natural-language interface that enables agentic applications to manage the software-licensing lifecycle in Labs64 NetLicensing. Prior to 0.1.6, network-reachable HTTP transport requests to /mcp that omit x-netlicensing-api-key, Authorization: Bearer, and the apikey query parameter pass through ApiKeyMiddleware in src/netlicensing_mcp/server.py without authentication. The downstream api_key_ctx in src/netlicensing_mcp/client.py then falls back to the operator's NETLICENSING_API_KEY and authenticates upstream NetLicensing REST API calls under the operator account. An unauthenticated attacker can invoke MCP tools to enumerate products, licenses, licensees, and transactions, create or modify licensing objects, perform validations, and execute destructive delete operations. The issue affects HTTP deployments configured with a server-side key and does not require user interaction. This issue is fixed in version 0.1.6.

### 25. CVE-2026-52851｜traccar / traccar
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T19:16:49.680)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T19:16:49.680 / 2026-09-17T20:16:50.710
- **官方描述（原文）**：Traccar is an open source GPS tracking system. Prior to 6.14.0, an authenticated, non-readonly user with access to an object usable in a permission pair can submit DELETE /api/permissions with an extra attacker-controlled JSON key. Permission(LinkedHashMap<String, Long>) in src/main/java/org/traccar/model/Permission.java validates only the first two keys, but DatabaseStorage.removePermission() in src/main/java/org/traccar/storage/DatabaseStorage.java concatenates every map key into the SQL WHERE clause as a column identifier. The extra key therefore becomes attacker-controlled SQL and provides a blind boolean or error oracle that can extract arbitrary database values, including administrator email, password hashes, and salts, or conditionally delete permission rows. Unauthenticated requests are rejected. This issue is fixed in 6.14.0.

### 26. CVE-2026-50285｜pomerium / pomerium
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T20:16:50.290)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T20:16:50.290 / 2026-09-17T21:17:14.383
- **官方描述（原文）**：Pomerium is an identity and context-aware access proxy. Prior to 0.32.8, decodeQueryStringV2 in pkg/hpke/url.go performs zstd decompression of attacker-controlled data without an output-memory limit when DecryptURLValues processes HPKE V2 values for Stateless.Callback in internal/authenticateflow/stateless.go. In hosted or stateless authentication deployments, an unauthenticated attacker can obtain the receiver key from /.well-known/pomerium/hpke-public-key, provide a matching attacker-controlled sender key, and send a compressed payload to /.pomerium/callback that expands before validateSenderPublicKey rejects the sender. This can allocate hundreds of megabytes per request, exhaust proxy memory, crash or degrade the process, and block access to applications protected by the deployment. Stateful deployments are not affected because the stateful callback verifies its HMAC signature before decryption and decompression. This issue is fixed in version 0.32.8.

### 27. CVE-2026-93467｜HGiga / OAKlouds-custom_page-2.0
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T03:16:33.753)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T03:16:33.753 / 2026-09-18T03:16:33.753
- **官方描述（原文）**：The OAKlouds developed by HGiga has a Insecure Deserialization vulnerability. Unauthenticated remote attackers can execute arbitrary code on the server by sending maliciously crafted serialized content.

### 28. CVE-2026-93393｜MongoDB Inc. / C Driver
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T21:17:56.163)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T21:17:56.163 / 2026-09-17T21:17:56.163
- **官方描述（原文）**：A heap-based buffer overflow exists in the TLS transport layer of the MongoDB C Driver when built with the Windows platform TLS backend. A remote endpoint that the client connects to, or an attacker able to impersonate or redirect the client's connection, can cause the driver to write attacker-supplied data outside the bounds of a heap allocation while processing incoming encrypted traffic. No authentication or user interaction is required, because the affected processing occurs before any application-level authentication completes. Successful exploitation may lead to memory corruption in the client process, disclosure of adjacent heap memory, or termination of the process.

### 29. CVE-2026-92956｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:01.640)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:01.640 / 2026-09-17T20:18:59.730
- **官方描述（原文）**：vm2 versions 3.10.1 through 3.11.6 contain a sandbox escape reachable from a default `new VM()` sandbox when running on Node.js 26. WebAssembly.compileStreaming and WebAssembly.instantiateStreaming can produce a raw host-realm Promise that rejects with a host-realm error object; by controlling Symbol.species via Promise.prototype.finally, sandbox code receives that raw host error, walks from the host error constructor to the host Function constructor, and recovers the real host `process` object, gaining host Node.js capabilities (e.g. access to host modules such as fs) in the context of the process running the sandbox. No NodeVM, require permission, host object injection, or otherwise unsafe configuration is required. This is a bypass of the fix for GHSA-6j2x-vhqr-qr7q, which removed the JSPI entry points WebAssembly.promising and WebAssembly.Suspending. The issue is fixed in 3.11.7.

### 30. CVE-2026-92954｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:01.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:01.320 / 2026-09-17T14:18:01.430
- **官方描述（原文）**：vm2 is a sandbox library for running untrusted JavaScript in Node.js. In versions >= 3.10.0 and <= 3.11.7, Promises returned from the host realm into the sandbox are not marked as handled at the bridge boundary; only Promises created inside the sandbox are wrapped with a rejection-swallowing handler (lib/setup-sandbox.js), and the bridge only installs host-side rejection sanitizers when sandbox code calls .then/.catch/.finally. As a result, code running in the sandbox can invoke a host function that returns a rejected Promise (for example events.once() exposed via the NodeVM events builtin, or any embedder-provided Promise-returning API) and simply ignore the return value, leaving the host Promise unhandled so that Node.js's default unhandled-rejection behavior terminates the host process. This is an incomplete fix of GHSA-hw58-p9xv-2mjh. The issue is fixed in version 3.11.8.

### 31. CVE-2026-92953｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:01.160)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:01.160 / 2026-09-17T14:18:01.273
- **官方描述（原文）**：vm2 versions from 3.11.0 before 3.11.8 fail to protect host TypedArray and ArrayBuffer prototypes from sandbox mutation. Attackers can use prototype-walking primitives to reach and modify host Uint8Array.prototype, %TypedArray%.prototype, and ArrayBuffer.prototype, causing host-created typed arrays to observe attacker-controlled properties after VM.run() returns.

### 32. CVE-2026-92951｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:00.827)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:00.827 / 2026-09-17T20:18:59.610
- **官方描述（原文）**：vm2 before 3.11.7 contains an incorrect authorization vulnerability in the external package allowlist check that uses non-exact substring matching instead of full package-name boundary validation. Attackers can bypass the allowlist by requiring a colliding package name that contains an allowlisted package substring, causing vm2 to load and execute unauthorized host packages in the host context.

### 33. CVE-2026-92948｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:00.310)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:00.310 / 2026-09-17T14:18:00.420
- **官方描述（原文）**：vm2 versions >= 3.9.6 and <= 3.11.6 are affected by a NodeVM builtin allowlist bypass that permits a sandbox escape on Node.js 24 and newer when the embedder explicitly allows the node:test builtin (e.g. require: { builtin: ['node:test'] }). On Node.js 24+, module.builtinModules exposes the scheme-only key node:test, which is not covered by vm2's family-based DANGEROUS_BUILTINS protection, so it is stored in the generic host-passthrough loader. Because requireImpl() in lib/setup-node-sandbox.js strips a single 'node:' prefix before the builtin lookup, sandbox code calling require('node:node:test') resolves to the stored node:test key and receives a readonly proxy to the host module. Calls to node:test.run() are forwarded to the host implementation, which spawns a separate Node process for process-isolated test execution and passes through attacker-controlled execArgv values; supplying --eval=<JavaScript> therefore executes arbitrary JavaScript in an unrestricted host Node process outside the NodeVM sandbox. Fixed in vm2 3.11.7.

### 34. CVE-2026-92946｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:59.963)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:59.963 / 2026-09-17T20:18:59.483
- **官方描述（原文）**：vm2 before 3.11.7 contains a remote code execution vulnerability when require.external is enabled without an explicit require.root that excludes node_modules. Sandboxed code can require vm2's own package, instantiate an unrestricted NodeVM instance, and execute arbitrary host OS commands via child_process.

### 35. CVE-2026-92944｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:59.623)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:59.623 / 2026-09-17T14:17:59.753
- **官方描述（原文）**：vm2 versions 3.10.2 through 3.11.6 contain a sandbox escape vulnerability on Node.js 26 where Promise.prototype.finally() bypasses vm2's wrapper protections due to a stale PromiseThenLookupChain protector in V8 14.6. Attackers can exploit this by creating an async function that returns a Promise with an attacker-controlled constructor Symbol.species, allowing them to reach the host Function constructor and process object for arbitrary code execution.

### 36. CVE-2026-92943｜AWS / AWSIoTPythonSDK
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T20:18:59.333)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T20:18:59.333 / 2026-09-17T20:18:59.333
- **官方描述（原文）**：Improper validation of certificate with host mismatch in the MQTT client TLS connection layer in AWS IoT Device SDK for Python 1.5.3 through 1.6.0 on Python 3.7 and later might allow an adversary-in-the-middle actor to impersonate the AWS IoT Core endpoint, read device telemetry, and inject arbitrary MQTT messages that the device processes as authentic, via a certificate issued for an unrelated hostname by a certificate authority present in the device trust store. To remediate this issue, users should upgrade to version 1.6.1.

### 37. CVE-2026-92940｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:59.143)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:59.143 / 2026-09-17T20:18:59.213
- **官方描述（原文）**：vm2 versions 3.11.3 through 3.11.6 expose the host process's real https.globalAgent to sandboxed code when a NodeVM is explicitly configured to allow require('https'). The builtin loader wraps host modules in a read-only proxy, but method calls such as Agent.prototype.on() are forwarded to the underlying host object, so sandbox code can register a listener for the agent's 'free' event. When an unrelated host HTTPS request releases a pooled connection, the listener receives the live host request options and the host TLSSocket, allowing sandboxed code to read the host's Authorization header and private destination host/port, attach a data listener to the released socket and read subsequent host response bodies in plaintext, and issue attacker-chosen authenticated requests using the stolen credentials. The issue is fixed in 3.11.7.

### 38. CVE-2026-92938｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:58.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:58.750 / 2026-09-17T14:17:58.920
- **官方描述（原文）**：vm2 versions 3.11.3 through 3.11.6 expose Node.js's host node:sqlite module to code running in NodeVM when that builtin is permitted, either explicitly or through builtin: ['*']. The module is wrapped with vm.readonly(), which prevents property assignment but leaves host-authority callables reachable; in addition, the resolver treats any request starting with 'node:' as a core-module request and the runtime strips only one 'node:' prefix, so a sandbox request for 'node:node:sqlite' resolves to the configured node:sqlite entry. Sandboxed code can therefore create an in-memory DatabaseSync with extension loading enabled and call DatabaseSync.loadExtension() on a native library bundled in the untrusted plugin package (path derived from __dirname). SQLite loads the library into the Node.js host process and invokes its native entry point, giving the sandboxed plugin arbitrary native code execution outside the sandbox with the host process's privileges. The issue is fixed in vm2 3.11.7.

### 39. CVE-2026-92937｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:58.517)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:58.517 / 2026-09-17T14:17:58.690
- **官方描述（原文）**：vm2 3.11.6 is vulnerable to a sandbox escape leading to remote code execution in the host Node.js process. The fix for GHSA-m283-3h24-438v is incomplete: the bridge gate at lib/bridge.js:1624 identity-checks only the direct call target when deciding whether to rebuild/sanitise a rejected host Promise value. Registering the rejection handler through Function.prototype.call or .apply indirection (e.g., p.then.call(p, undefined, cb)) makes the intercepted target host Function.prototype.call, so the sanitiser never runs and the raw host error reaches sandbox code with its own properties intact. If an embedder exposes a host-realm Promise to the sandbox (an async host function bridged via the sandbox option, or a NodeVM external module's async method) and that Promise rejects with an Error carrying a non-primitive own property referencing a host object (for example err.detail = process), untrusted code in the sandbox obtains a fully functional proxy to that host object and can execute arbitrary commands with the privileges of the host process (e.g., e.detail.mainModule.require('child_process').execSync(...)). The direct p.then(undefined, cb), bind, and Reflect.apply forms are correctly sanitised. Fixed in vm2 3.11.7.

### 40. CVE-2026-92935｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:57.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:57.810 / 2026-09-17T20:18:59.093
- **官方描述（原文）**：vm2 is a sandbox for running untrusted Node.js code. In versions >= 3.11.4 and <= 3.11.6, the NodeVM constructor computes `hasRealRequireConfig` with `typeof requireOpts === 'object' && requireOpts !== null`, so an array-shaped `require` value (for example `require: []`) satisfies the guard that is meant to reject nesting without an explicit require configuration. `makeResolverFromLegacyOptions()` then destructures the array into undefined option fields and returns a resolver containing only `NESTING_OVERRIDE.vm2`. As a result, an attacker who can supply JavaScript executed by a NodeVM configured with truthy `nesting` and an array-shaped `require` (e.g. `new NodeVM({nesting: true, require: []})`) can require the host `vm2` module, create an inner NodeVM with an attacker-chosen builtin allowlist (such as `child_process`), and execute arbitrary commands with the privileges of the host Node.js process, escaping the sandbox. Outer builtin restrictions do not constrain the attacker-created inner NodeVM. This issue is fixed in vm2 3.11.7.

### 41. CVE-2026-91039｜team-alembic / ash_authentication
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T16:18:28.700)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T16:18:28.700 / 2026-09-17T20:18:52.740
- **官方描述（原文）**：Authentication Bypass by Spoofing vulnerability in team-alembic ash_authentication allows an attacker who operates one identity-provider connection of a dynamic_oidc strategy to be signed in as a local user established through a different connection. The strategy is meant to keep each connection in its own identity namespace by writing every UserIdentity row's strategy field as "<name>/<connection_id>", but that namespacing never takes effect. __connection_id__ is populated only on the ephemeral runtime struct built per request in dynamic_oidc/plug.ex, and DynamicOidc.IdentityChange.change/3 re-fetches the strategy from the compile-time DSL through Info.strategy_for_action, yielding the persisted struct whose __connection_id__ is its defstruct default of nil. OAuth2.identity_strategy_name/1 therefore falls back to the bare strategy name for both the identity write and the reads in oauth2/user_resolver.ex and oauth2/sign_in_preparation.ex. Since the identity resource's unique key is (uid, strategy), one row exists per sub across every connection, and the identity-match branch runs before any email check. Neither strategy handles iss, so nothing else distinguishes the issuers: OpenID Connect Core section 5.7 makes sub unique only within an issuer, so two connections numbering subjects independently share one subject space. This issue affects ash_authentication: from 5.0.0-rc.10 before 5.0.0-rc.14.

### 42. CVE-2026-88952｜team-alembic / ash_authentication
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T15:16:56.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T15:16:56.290 / 2026-09-17T20:18:51.800
- **官方描述（原文）**：Improper Authentication vulnerability in team-alembic AshAuthentication allows an attacker to be signed in as another user by linking an OAuth2 identity to an account that is not theirs. AshAuthentication.Strategy.OAuth2.UserResolver.resolve/3 matches an existing account using the register action's upsert_identity keys, then gates linking the incoming provider identity to it on email_trusted?/2, which reads only the provider's email_verified boolean and never compares the provider's email value with the matched account's email. That gate assumes the account was matched by its email field, so under any other upsert_identity it is vacuous and an attacker presenting their own verified email is attached to, and issued a session for, an account matched on some other attribute. The same unguarded gate applies in OAuth2.SignInPreparation on the registration_enabled? false path, where the account is matched by the sign-in action's read filter instead. The upsert also rewrites the matched account's email to the attacker's address, so later account recovery reaches the attacker rather than the owner. This issue affects ash_authentication: from 4.14.0 before 4.15.0 and from 5.0.0-rc.10 before 5.0.0-rc.14.

### 43. CVE-2026-87701｜Microsoft / Azure Cosmos DB
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T23:18:53.623)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T23:18:53.623 / 2026-09-17T23:18:53.623
- **官方描述（原文）**：Improper neutralization of special elements in output used by a downstream component ('injection') in Azure Cosmos DB allows an authorized attacker to elevate privileges over a network.

### 44. CVE-2026-86863｜pgadmin.org / pgAdmin 4
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T16:18:17.863)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T16:18:17.863 / 2026-09-17T17:16:51.633
- **官方描述（原文）**：pgAdmin 4's Webserver authentication source is intended to accept an identity asserted by the web server or reverse proxy in front of pgAdmin, delivered through the WSGI/CGI environment. WebserverAuthentication.get_user() read config.WEBSERVER_REMOTE_USER from request.environ and, when that returned nothing, fell back to reading the same name directly from the inbound HTTP request headers via request.headers.get(). An inbound HTTP header is written by whoever sends the request, so any client able to reach pgAdmin could supply that header itself and be authenticated as any username it named, including an existing Administrator, without presenting a password or any other credential. The environment lookup could also be satisfied by a client-supplied header whenever WEBSERVER_REMOTE_USER was configured to an HTTP_-prefixed or hyphenated name such as HTTP_X_FORWARDED_USER or X-Forwarded-User, since WSGI servers place inbound headers into the environment under exactly those names. Deployments are affected only when 'webserver' is enabled in AUTHENTICATION_SOURCES. The fix distinguishes a genuine CGI/WSGI variable from a header-derived one and implicitly trusts only the former. A header-asserted identity is now accepted only when the operator explicitly opts in via WEBSERVER_REMOTE_USER_FROM_HEADER, the request arrives from a peer listed in WEBSERVER_TRUSTED_PROXIES, and, when configured, a shared secret supplied in WEBSERVER_SHARED_SECRET_HEADER matches WEBSERVER_SHARED_SECRET under a constant-time comparison. The trusted-peer check deliberately reads the real socket peer address rather than request.remote_addr, because ProxyFix rewrites the latter from the client-controlled X-Forwarded-For header and would otherwise allow an attacker to claim to be the trusted proxy. As defence in depth, login() now refuses any account whose auth_source is not 'webserver', so a misconfigured trust gate cannot be used to assume an internal or LDAP account. This issue affects pgAdmin 4: from 6.2 before 9.18.

### 45. CVE-2026-86533｜team-alembic / ash_authentication
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:46.467)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:46.467 / 2026-09-17T19:17:06.080
- **官方描述（原文）**：Insufficient Session Expiration vulnerability in team-alembic AshAuthentication and AshAuthentication Phoenix allows a revoked session to remain fully authenticated. A resource configured with session_identifier :jti and require_token_presence_for_authentication? disabled stores its session value as <jti>:<subject>. The jti is there so that signing out can revoke that one session. Neither reader consults it: AshAuthentication.Plug.Helpers.authenticate_resource_from_session/4 and AshAuthentication.Phoenix.LiveSession.on_mount/4 both split the value with split_identifier/2, discard the jti and pass the bare subject to AshAuthentication.subject_to_user/3, which reloads the record. The token-presence branch of each function does check its token, calling AshAuthentication.TokenResource.Actions.get_token/3 with the jti and the purpose user. Because the revocation record is never read, neither its revoked state nor its expiry constrains the session, so a session captured before sign-out keeps working. This issue affects ash_authentication: from 4.9.1 before 4.15.0 and from 5.0.0-rc.0 before 5.0.0-rc.14; ash_authentication_phoenix: from 2.10.0 before 2.17.4 and from 3.0.0-rc.0 before 3.0.0-rc.11.

### 46. CVE-2026-85889｜Microsoft / Azure AI Foundry
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T23:18:53.217)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T23:18:53.217 / 2026-09-17T23:18:53.217
- **官方描述（原文）**：Missing authentication for critical function in Azure AI Foundry allows an unauthorized attacker to elevate privileges over a network.

### 47. CVE-2026-85885｜Microsoft / Microsoft 365 Copilot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T23:18:53.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T23:18:53.080 / 2026-09-17T23:18:53.080
- **官方描述（原文）**：Improper neutralization of special elements used in a command ('command injection') in M365 Copilot allows an authorized attacker to elevate privileges over a network.

### 48. CVE-2026-85878｜Microsoft / Azure HorizonDB
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T00:17:47.777)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T00:17:47.777 / 2026-09-18T00:17:47.777
- **官方描述（原文）**：Improper authorization in Azure Database for PostgreSQL allows an authorized attacker to elevate privileges over a network.

### 49. CVE-2026-85500｜team-alembic / ash_authentication
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:46.050)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:46.050 / 2026-09-17T19:17:05.520
- **官方描述（原文）**：Authentication Bypass by Primary Weakness vulnerability in team-alembic AshAuthentication allows an unconfirmed user to obtain a session, defeating a mandatory email confirmation requirement. AshAuthentication.Strategy.Password.Actions.check_user/2 decides whether the attribute named by require_confirmed_with is set using a bare is_nil(Map.get(user, value)). When that attribute is not selected on the loaded record Map.get/2 returns %Ash.NotLoaded{}, and when a field policy denies it for the current actor it returns %Ash.ForbiddenField{}. Neither is nil, so the rejection branch is skipped and sign-i require_confirmed_with is enforced in two places, and neither holds in every configuration. sign_in_with_token and register are checked only inside AshAuthentication.Strategy.Password.Actions, not on the action itself, so any caller that invokes the action directly skips the check. An API layer such as AshGraphql or AshJsonApi invokes the action directly, so this applies to the default configuration. Where a check does run it compares the confirmation attribute against nil. That attribute holds %Ash.NotLoaded{} or %Ash.ForbiddenField{} when it sets select_by_default?: false, when an API layer narrows the read's select, or when a field policy hides it from the sign-in actor. Neither struct is nil, so those configurations read every user as confirmed. This issue affects ash_authentication: from 4.3.8 before 4.15.0 and from 5.0.0-rc.0 before 5.0.0-rc.14.

### 50. CVE-2026-83944｜Microsoft / Azure Logic Apps
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T23:18:51.257)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T23:18:51.257 / 2026-09-17T23:18:51.257
- **官方描述（原文）**：Improper access control in Azure Logic Apps allows an unauthorized attacker to elevate privileges over a network.

### 51. CVE-2026-82761｜team-alembic / ash_authentication
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:33.423)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:33.423 / 2026-09-17T19:17:04.677
- **官方描述（原文）**：Time-of-check Time-of-use (TOCTOU) Race Condition vulnerability in team-alembic AshAuthentication allows an attacker holding a leaked magic link to replay its single-use token and authenticate as the target subject. A magic link configured with single_use_token?, which is the default, is meant to be redeemable exactly once, but nothing serialises the token's validity check against its consumption, so concurrent redemptions of one token all succeed and each yields a full user token. Sign-in verifies the JWT with Jwt.verify/4 and revokes it only afterwards: AshAuthentication.Strategy.MagicLink.SignInPreparation revokes in a Query.after_action callback, and AshAuthentication.Strategy.MagicLink.SignInChange in an after_transaction hook that runs once the sign-in has already committed. AshAuthentication.TokenResource.Actions.revoke/3 writes the revocation as an upsert, so a concurrent duplicate revocation silently succeeds instead of conflicting and no request ever loses the race. This issue affects ash_authentication: from 3.9.0 before 4.15.0 and from 5.0.0-rc.0 before 5.0.0-rc.14.

### 52. CVE-2026-79752｜cakephp / cakephp
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T15:16:51.673)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T15:16:51.673 / 2026-09-17T16:17:44.693
- **官方描述（原文）**：CakePHP is a rapid development framework for PHP. Prior to 4.5.12, 4.6.5, 5.1.9, 5.2.14, and 5.3.7, FunctionsBuilder::cast, FunctionsBuilder::extract, FunctionsBuilder::datePart, and FunctionsBuilder::dateAdd in src/Database/FunctionsBuilder.php accept user-controlled dataType, part, or unit values and incorporate them into generated SQL as unescaped structural fragments. An application that passes untrusted input to these parameters can permit SQL injection with confidentiality, integrity, and availability impact according to the database connection's privileges. This issue is fixed in versions 4.5.12, 4.6.5, 5.1.9, 5.2.14, and 5.3.7.

### 53. CVE-2026-77903｜Microsoft / Microsoft Dataverse
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T23:18:44.993)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T23:18:44.993 / 2026-09-17T23:18:44.993
- **官方描述（原文）**：Authentication bypass by spoofing in Microsoft Dataverse allows an unauthorized attacker to elevate privileges over a network.

### 54. CVE-2026-76949｜team-alembic / ash_authentication
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T22:17:03.883)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T22:17:03.883 / 2026-09-17T22:17:03.883
- **官方描述（原文）**：Authentication Bypass by Spoofing vulnerability in team-alembic ash_authentication allows an attacker who can plant a remember-me cookie in a victim's browser to replace that victim's authenticated session with one for the attacker's own account. AshAuthentication.Plug.Helpers.sign_in_using_remember_me/3 skips re-authenticating an already-signed-in visitor by checking the session for "<subject_name>_token", but store_in_session/2 writes that key only when require_token_presence_for_authentication? is enabled and otherwise writes the bare subject name. At the default setting the guard therefore reads a key that is never written, its already-signed-in branch is unreachable, and the remember-me sign-in runs on every request through the per-request browser pipeline plug. A planted remember-me cookie is consequently honoured even for a visitor holding a live authenticated session, so whatever the victim enters afterwards lands in data the attacker controls. The read path in authenticate_resource_from_session/4 selects the key correctly, so the guard and the reader disagree about which key holds the session. This issue affects ash_authentication: from 4.10.0 before 4.15.0 and from 5.0.0-rc.0 before 5.0.0-rc.14.

### 55. CVE-2026-76834｜b2evolution / b2evolution CMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T16:17:42.270)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T16:17:42.270 / 2026-09-17T16:17:42.270
- **官方描述（原文）**：b2evolution CMS versions 6.7.8 through 7.2.5 contain an incomplete fix for CVE-2016-8901 where the serialized-array object check in param_check_serialized_array() fails to reject payloads with negative integer array keys. Unauthenticated attackers can submit crafted serialized PHP objects via POST requests to htsrv/call_plugin.php that bypass validation and reach unserialize(), instantiating arbitrary PHP objects with attacker-chosen properties that may enable code execution if suitable POP gadget chains exist.

### 56. CVE-2026-70200｜Microsoft / Azure Logic Apps
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T23:18:36.113)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T23:18:36.113 / 2026-09-17T23:18:36.113
- **官方描述（原文）**：Improper limitation of a pathname to a restricted directory ('path traversal') in Azure Logic Apps allows an unauthorized attacker to elevate privileges over a network.

### 57. CVE-2026-70009｜Microsoft / Azure ARC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T23:18:35.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T23:18:35.560 / 2026-09-17T23:18:35.560
- **官方描述（原文）**：Improper limitation of a pathname to a restricted directory ('path traversal') in Azure Arc allows an unauthorized attacker to elevate privileges over a network.

### 58. CVE-2026-69865｜Microsoft / Azure Container Registry
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T23:18:34.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T23:18:34.670 / 2026-09-17T23:18:34.670
- **官方描述（原文）**：Authorization bypass through user-controlled key in Microsoft Container Registry allows an unauthorized attacker to elevate privileges over a network.

### 59. CVE-2026-69843｜Microsoft / Microsoft Fabric
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T00:17:24.923)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T00:17:24.923 / 2026-09-18T00:17:24.923
- **官方描述（原文）**：Authentication bypass by spoofing in Microsoft Fabric allows an unauthorized attacker to elevate privileges over a network.

### 60. CVE-2026-69399｜Microsoft / Azure ARC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T23:18:18.793)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T23:18:18.793 / 2026-09-17T23:18:18.793
- **官方描述（原文）**：Azure Arc Elevation of Privilege Vulnerability

### 61. CVE-2026-62874｜Microsoft / Azure Billing
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T00:16:57.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T00:16:57.930 / 2026-09-18T00:16:57.930
- **官方描述（原文）**：Insufficient verification of data authenticity in Azure Billing allows an unauthorized attacker to elevate privileges over a network.

### 62. CVE-2026-62108｜miniOrange / Headless Single Sign On
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:15.263)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:15.263 / 2026-09-17T21:12:30.593
- **官方描述（原文）**：Unauthenticated Broken Authentication in Headless Single Sign On <= 1.7.0 versions.

### 63. CVE-2026-62104｜superweby / Migratico Lite
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:15.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:15.130 / 2026-09-17T21:12:30.593
- **官方描述（原文）**：Unauthenticated Remote Code Execution (RCE) in Migratico Lite <= 2.6.8 versions.

### 64. CVE-2026-62101｜Chris Åkerfeldt Wendel / EduAdmin Booking
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:14.977)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:14.977 / 2026-09-17T21:12:30.593
- **官方描述（原文）**：Unauthenticated Broken Authentication in EduAdmin Booking <= 5.4.2 versions.

### 65. CVE-2026-54767｜LabRedesCefetRJ / WeGIA
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T22:17:03.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T22:17:03.470 / 2026-09-17T22:17:03.597
- **官方描述（原文）**：WeGIA is a web manager for charitable institutions. Prior to 3.8.5, web/html/socio/sistema/controller/deletar_socios.php exposes an unauthenticated GET endpoint whose chave parameter is checked only against a hardcoded chave_correta value embedded in the public source repository. A remote attacker who obtains that value can reach the endpoint's TRUNCATE TABLE operations for the endereco, pessoafisica, pessoajuridica, and socio tables without an administrative session or application authorization, permanently destroying member and contributor records. The attack requires the affected tables to exist and the web process database account to possess truncation privileges. This issue is fixed in version 3.8.5.

### 66. CVE-2026-54752｜netbox-community / devicetype-library
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T20:16:52.877)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T20:16:52.877 / 2026-09-17T20:16:52.877
- **官方描述（原文）**：NetBox Device Type Library is a collection of community-sourced device type definitions for import into NetBox. The validation test harness can deserialize pull-request-controlled tracked pickle cache files through pickle.load in the read_pickle_data function in tests/pickle_operations.py. An unauthenticated contributor can change USE_LOCAL_KNOWN_SLUGS in tests/test_configuration.py and supply a crafted tests/known-modules.pickle or tests/known-racks.pickle file that tests/definitions_test.py loads when pytest runs. Deserialization invokes attacker-controlled object reduction behavior, allowing arbitrary code execution in the GitHub Actions runner or in a maintainer process that runs the tests, with the confidentiality, integrity, and availability of reachable resources at risk. This vulnerability is fixed with commit 1c6f7e2b93589b965318c6e67ac3504831f0e71e.

### 67. CVE-2026-54734｜prebid / prebid-server-java
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T22:17:03.317)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T22:17:03.317 / 2026-09-17T22:17:03.317
- **官方描述（原文）**：Prebid Server Java is the Java version of Prebid Server. Prior to 3.43.0, certain bidder adapters interpolate user-supplied parameters into outbound request URLs without using HttpUtil to validate the resulting domain or path segment. A malicious actor who can supply bid-request parameters can cause the server to send HTTP requests to unintended destinations, potentially reaching internal network services, metadata endpoints, or other sensitive server endpoints with the server's network access. This issue is fixed in version 3.43.0.

### 68. CVE-2026-54670｜LabRedesCefetRJ / WeGIA
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T22:17:02.983)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T22:17:02.983 / 2026-09-17T22:17:03.110
- **官方描述（原文）**：WeGIA is a web manager for charitable institutions. Prior to 3.8.5, the contribution request dispatcher in web/html/contribuicao/controller/control.php accepts attacker-controlled nomeClasse and metodo values without a complete controller and method allowlist, exempts sensitive ContribuicaoLogController operations from authentication, and constructs a controller include path without canonical directory containment. An unauthenticated remote attacker can invoke getContribuicoesLogJSON, sincronizarStatus, registrarFaturas, and other sensitive methods to disclose contribution and donation records or trigger financial workflow operations. A traversal-shaped nomeClasse value can also cause require_once to include an accessible PHP or configuration file outside the intended controller directory, exposing source code, credentials, or other sensitive local data. This issue is fixed in version 3.8.5.

### 69. CVE-2026-54627｜HappySeaFox / sail
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T20:16:52.117)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T20:16:52.117 / 2026-09-17T20:16:52.117
- **官方描述（原文）**：SAIL is a cross-platform library for loading and saving images with support for animation, metadata, and ICC profiles. In 0.9.10 and earlier, psd_private_sail_pixel_format() in src/sail-codecs/psd/helpers.c resolves a one-channel PSD in Bitmap color mode to SAIL_PIXEL_FORMAT_BPP1_INDEXED without requiring the file depth to be one, so the pixel buffer uses one-bit rows while sail_codec_load_frame_v8_psd() in src/sail-codecs/psd/psd.c accepts depth == 8 and writes one attacker-controlled byte per pixel. Loading a crafted PSD through sail_load_from_file() or sail_load_from_memory() therefore writes beyond each heap row, causing memory corruption, a reliable crash, or potential code execution. This mode/depth mismatch is distinct from GHSA-rcqx-gc76-r9mv and GHSA-wcj8-hxxf-pq2c. This issue is fixed in version 1.0.0.

### 70. CVE-2026-54618｜jimprosser / obsidian-web-mcp
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T20:16:51.823)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T20:16:51.823 / 2026-09-17T20:16:51.823
- **官方描述（原文）**：Obsidian Web MCP is a secure remote MCP server for Obsidian vaults. Prior to 0.2.0, /oauth/authorize issues an authorization code without a login, consent, or session check, and /oauth/token can exchange that code for the static VAULT_MCP_TOKEN without authenticating a client. An unauthenticated remote caller who can reach the intended tunnel deployment can therefore call /mcp and use vault_read, vault_write, vault_search, vault_list, vault_move, and vault_delete against the entire vault. Optional PKCE does not prevent an attacker-initiated flow, and unauthenticated /oauth/register also exposes a client_credentials path by returning the configured VAULT_OAUTH_CLIENT_SECRET. This issue is fixed in version 0.2.0.

### 71. CVE-2026-54617｜GravitLauncher / Launcher
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T19:16:51.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T19:16:51.003 / 2026-09-17T19:16:51.003
- **官方描述（原文）**：GravitLauncher is an open-source Minecraft launcher based on sashok724's v3. Prior to 5.7.12, an unauthenticated remote actor can send a raw HTTP request target without a leading slash to the default LaunchServer file server on port 9274. FileServerHandler.channelRead0 in components/launchserver/src/main/java/pro/gravit/launchserver/socket/handlers/fileserver/FileServerHandler.java strips the first request-target character and resolves the remaining path against updatesDir without re-normalizing and verifying containment. This leaves parent-directory components in a no-leading-slash request and allows reading any file accessible to the LaunchServer process, including .keys/ecdsa_id, .keys/legacySalt, and LaunchServer.json. Disclosure of those files can expose signing keys, refresh-token material, and database credentials, enabling forged administrative access tokens and full authentication bypass. A normalizing L7 proxy may block the primary request form, but direct exposure and L4/TCP proxies remain affected, and netty.fileServerEnabled is enabled by default. This issue is fixed in 5.7.12.

### 72. CVE-2026-54501｜webrecorder / browsertrix
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T21:17:15.707)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T21:17:15.707 / 2026-09-17T21:17:15.707
- **官方描述（原文）**：Browsertrix is a high-fidelity, browser-based crawling service for web archiving that can be self-hosted or used through Webrecorder's hosted instance. From 1.15.0 until 1.22.8, Browsertrix improperly sanitizes Git URLs specified as Custom Behaviors, allowing command injection through /api/orgs/*/crawlconfigs/validate/custom-behavior. A user with crawler or administrator permission on the specific instance can supply a crafted Git URL that executes arbitrary operating-system commands in the backend pod. Open registration or hosted free-trial access can make the required role broadly obtainable. Successful exploitation can expose, modify, or delete application database records, archived items, browser profiles, storage data, proxy credentials, and other configured service data. This issue is fixed in version 1.22.8.

### 73. CVE-2026-54460｜open-reception / appointment-booking-software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T21:17:15.557)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T21:17:15.557 / 2026-09-17T21:17:15.557
- **官方描述（原文）**：OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to 1.1.1, POST /api/auth/passkeys accepts a request-body userId and attacker-supplied passkey without an authenticated session, does not call WebAuthnService.verifyRegistration, and does not bind enrollment to locals.user.id. An unauthenticated attacker who knows the public tenant ID and the target staff email can use the public booking bootstrap and GET /api/tenants/[id]/appointments/staff-public-keys to obtain candidate userId values. The attacker first causes UserService.addAdditionalPasskey to store a controlled public key for a candidate userId, then attempts login with the target email; the login check compares verificationResult.userId with the email-resolved account and reveals whether the injected credential belongs to that target. Repeating this injection-before-login sequence identifies the matching userId, and the normal login endpoint accepts the attacker's assertion for the stored key and creates a STAFF session. The session can expose tenant data and reveal TENANT_ADMIN identifiers for further takeover; GLOBAL_ADMIN accounts are not reachable through this tenant-scoped path. A hijacked TENANT_ADMIN can modify or delete tenant resources and key shares, potentially making appointment data permanently undecryptable and taking booking services offline. This issue is fixed in version 1.1.1.

### 74. CVE-2026-54237｜wavelog / wavelog
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T21:17:14.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T21:17:14.980 / 2026-09-17T21:17:14.980
- **官方描述（原文）**：Wavelog is web-based amateur radio logging software. From 1.8 until 2.4.2, Wavelog exposes /install/ajax.php and /install/includes/interface_assets/triggers.php after installation without an installation lock or permission check. Unsanitized input reaches write_config() and write_configfile() in install/includes/core/core_class.php, allowing a remote unauthenticated attacker to read or write log files and place attacker-controlled content into PHP configuration files. The resulting PHP configuration content can execute on the server. This issue is fixed in version 2.4.2.

### 75. CVE-2026-54053｜brufdev / many-notes
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T18:16:45.857)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T18:16:45.857 / 2026-09-17T18:16:45.857
- **官方描述（原文）**：Many Notes is a Markdown note-taking web application designed for simplicity. Prior to 0.16.0, the ZIP vault import implemented in app/Actions/ProcessImportedVault.php accepts archive filenames containing parent-directory traversal segments. An authenticated user can write arbitrary files outside the importing user's vault and into other users' vaults, including overwriting existing files. Disguised SVG content can be placed in another user's vault and execute stored cross-site scripting when the victim opens that vault. This issue is fixed in version 0.16.0.

### 76. CVE-2026-45143｜chamilo / chamilo-lms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T21:17:12.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T21:17:12.600 / 2026-09-17T21:17:12.600
- **官方描述（原文）**：Chamilo LMS is an open-source learning management system. From 2.0.0 through at least 2.1.0, Chamilo LMS stores private Message.content without server-side sanitization and renders it as HTML in assets/vue/views/message/MessageShow.vue and public/main/template/default/message/view_message.html.twig. An authenticated low-privilege user, including a student, can directly address crafted message content to an administrator because the message creation flow permits a sender to select another user as the recipient. The content executes in the recipient's browser when the recipient opens the routine inbox or message view, without requiring a link click, and can expose session credentials or permit actions as the administrator. This vulnerability is fixed in 2.0.1.

### 77. CVE-2026-45140｜chamilo / chamilo-lms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T21:17:12.440)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T21:17:12.440 / 2026-09-17T21:17:12.440
- **官方描述（原文）**：Chamilo LMS is an open-source learning management system. Prior to 2.0.1, Chamilo LMS allows an unauthenticated remote attacker to execute arbitrary code on the server. The authoritative advisory does not identify the affected endpoint, component, input, or exploitation mechanism. This issue is fixed in version 2.0.1.

### 78. CVE-2026-92936｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:17:58.320)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:17:58.320 / 2026-09-17T16:18:34.377
- **官方描述（原文）**：vm2 versions 3.11.0 through 3.11.6 leak absolute host filesystem paths to sandboxed code through error stack formatting. Attacker-supplied code can force the host-realm source transformer to throw a SyntaxError (for example by calling eval with malformed source) and then read the error's .stack property; the bridge forwards the .stack read to the host-realm formatter, bypassing the sandbox-side host-path redaction introduced for GHSA-v27g-jcqj-v8rw. The returned stack string discloses absolute paths from vm2, Node.js internals, and the embedding application's own source tree, along with host function names. Default new VM() and new NodeVM() configurations are affected without any special options, and the issue persists when string eval is disabled because the host-side transformer throws before eval is handled. The impact is information disclosure only; no code execution results. Fixed in vm2 3.11.7.

### 79. CVE-2026-92926｜code-projects / Matrimonial System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T18:17:14.930)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T18:17:14.930 / 2026-09-17T21:12:30.593
- **官方描述（原文）**：A vulnerability has been found in code-projects Matrimonial System 1.0. This vulnerability affects the function writepartnerprefs of the file /partner_preference.php. Such manipulation of the argument education leads to sql injection. The attack can be executed remotely. The exploit has been disclosed to the public and may be used.

### 80. CVE-2026-89038｜Verizon / Verizon Cloud for Android
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T18:17:13.983)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T18:17:13.983 / 2026-09-17T20:18:52.403
- **官方描述（原文）**：Verizon Cloud for Android (com.vcast.mediamanager) before 26.7.10 contains a path traversal vulnerability that allows co-resident malicious applications to write attacker-controlled bytes outside the intended staging directory by supplying a crafted _display_name value containing path-traversal sequences through exported activities OneTouchUploadActivity and PrintShopCloudActivity. Attackers can exploit the unsanitized filename concatenation in the file-staging sink via ACTION_SEND or ACTION_SEND_MULTIPLE intents to achieve arbitrary file write and inject attacker-controlled content into the authenticated user's Verizon Cloud account without user interaction.

### 81. CVE-2026-86000｜facelessuser / soupsieve
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T16:18:16.757)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T16:18:16.757 / 2026-09-17T16:18:16.757
- **官方描述（原文）**：Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4. Prior to 2.9, the selector parser in src/soupsieve/css_parser.py defines IDENTIFIER with adjacent quantified groups over overlapping character classes, and VALUE embeds IDENTIFIER for attribute selectors. When an attacker-controlled selector contains a long identifier or unquoted attribute-value run followed by input that makes the overall match fail, the regular expression engine explores quadratically many splits between the overlapping groups. User-controlled selectors can reach this path through soupsieve.compile(), soupsieve.select(), or BeautifulSoup.select(), while applications using only hard-coded selectors are unaffected. The resulting CPU consumption can hold the Python GIL, exhaust application workers, and stall a service; successful plain identifier matches are linear, and the issue does not cause memory corruption or code execution. The issue is fixed in version 2.9.

### 82. CVE-2026-61793｜nuxt-modules / og-image
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T15:16:48.987)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T15:16:48.987 / 2026-09-17T16:17:33.890
- **官方描述（原文）**：Nuxt OG Image generates OG Images with Vue templates in Nuxt. From 6.0.2 until 6.7.0, nuxt-og-image exposes the unauthenticated /_og/d/** route when the documented defaults security.strict = false and security.secret = "" are used, and base64url-decodes the fonts parameter through decodeOgImageParams. Attacker-controlled fonts[].path values flow through loadDefinedFonts into the font-assets/node.js binding, which performs a server-side fetch without validating the URL scheme, origin, resolved address, or redirects. This permits blind requests to loopback, private, link-local, cloud metadata, and other internal HTTP services, while differences in the outer response status and timing can reveal service reachability. Slow targets can also occupy OG image render workers for the configured fetch and render timeouts. This issue is fixed in version 6.7.0.

### 83. CVE-2026-54546｜dfpc-coe / CloudTAK
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T18:16:46.207)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.0 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T18:16:46.207 / 2026-09-17T18:16:46.207
- **官方描述（原文）**：CloudTAK is a browser-based Common Operating Picture and situational awareness tool compatible with TAK. Prior to 13.22.1, the authenticated PUT /api/basemap endpoint passes an attacker-controlled URL through importBasemapURL() in api/routes/basemap.ts to fetch(url) without resolved-address classification or redirect revalidation. BasemapProtocol.isValidURL in api/lib/interface-basemap.ts checks only the HTTP or HTTPS scheme and is not applied on the vulnerable import path. Direct internal addresses, alternate IP encodings, and redirects to internal addresses can reach cloud metadata, loopback, private, and CGNAT HTTP services. The OptionalTileJSON response reflects fields including name, attribution, and tiles[0] to the caller, making the request forgery full-read rather than blind and enabling cloud credential theft and internal service disclosure. This issue is fixed in version 13.22.1.

### 84. CVE-2026-44235｜alanxz / rabbitmq-c
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T18:16:43.850)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T18:16:43.850 / 2026-09-17T18:16:43.850
- **官方描述（原文）**：rabbitmq-c is a C-language AMQP client library for RabbitMQ. Prior to 0.16.0, a malicious AMQP server can send an undersized HEADER or METHOD frame during client login and cause unsigned size_t underflow in amqp_handle_input() in librabbitmq/amqp_connection.c. The parser subtracts HEADER_SIZE, fixed per-frame fields, and FOOTER_SIZE from state->target_size without first checking the minimum frame length. The wrapped encoded.len value is passed through amqp_decode_properties() to amqp_decode_table_internal(), where it defeats bounds checks and causes an out-of-bounds read and process crash. An on-path attacker can also trigger the issue when AMQP traffic is not protected by TLS with certificate validation. The demonstrated impact is denial of service, with no reliable memory disclosure or code execution shown. This issue is fixed in version 0.16.0.

### 85. CVE-2026-92992｜Dromara / mayfly-go
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T19:17:07.430)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T19:17:07.430 / 2026-09-17T21:12:30.593
- **官方描述（原文）**：A security vulnerability has been detected in Dromara mayfly-go up to 1.11.5. The affected element is an unknown function of the file server/internal/ai/api/ai.go of the component AI Assistant. The manipulation leads to missing authorization. Remote exploitation of the attack is possible. The exploit has been disclosed publicly and may be used. The identifier of the patch is 74bcb926eb4f5f94e7681144d7bf2168a0ec7cde. Applying a patch is the recommended action to fix this issue. The whitelist bypass is one-token wide. Any compound command containing curl, wget or sed auto-runs without approval; approval is granted by the same session user (self-approval). This issue got fixed with a silent patch.

### 86. CVE-2026-92962｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T14:18:02.610)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T14:18:02.610 / 2026-09-17T16:18:34.940
- **官方描述（原文）**：vm2 is a sandbox for running untrusted JavaScript. In vm2 versions up to and including 3.11.3, the defaultSandboxPrepareStackTrace function in lib/setup-sandbox.js builds its output array using prototype-walking index assignment (lines[lines.length] = value) rather than a prototype-bypassing define-property primitive. Because this bridge-internal array is allocated in the sandbox realm, code inside the sandbox can install an accessor on Array.prototype for the relevant index; the accessor is then invoked whenever the sandbox reads error.stack (or otherwise triggers Error.prepareStackTrace), allowing sandbox code to observe and intercept each stack-trace line written by the bridge. The same pattern is used in the error-handling (catch) branch. The values written are formatted strings only, so the practical impact is limited to an information side channel and a violation of vm2's bridge-container defense invariant rather than a sandbox escape; the vendor rates the issue Low. The issue is fixed in vm2 3.11.4, which installs each entry as an own data property via Reflect.defineProperty.

### 87. CVE-2026-79419｜未確認 / 未確認
- **Delta event**：CVSS_CHANGED (from=6.1; to=8.7)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 8.7 (HIGH)
- **EPSS**：0.00192 / percentile=0.09101
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-04T16:18:00.250 / 2026-09-17T19:20:50.983
- **官方描述（原文）**：A reflected cross-site scripting (XSS) vulnerability exists in EMX Tecnologia Gestao X Business Suite 8.4 and earlier. The vulnerability is caused by insufficient validation and sanitization of the mensagem parameter in the /Configuracao/Imagens.aspx endpoint, allowing an authenticated attacker to inject arbitrary JavaScript code that is reflected and executed in the context of a victim's browser.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-87886｜Acronis / Backup
- **Title**：Acronis Backup Incorrect Default Permissions Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Acronis Backup plugin for cPanel & WHM and extension for Plesk contains an incorrect default permissions vulnerability that could allow for privilege escalation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-92960 | P3 / 38 | patriksimek / vm2 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92957 | P3 / 38 | patriksimek / vm2 | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92955 | P3 / 38 | patriksimek / vm2 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92950 | P3 / 38 | patriksimek / vm2 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92947 | P3 / 38 | patriksimek / vm2 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92941 | P3 / 38 | patriksimek / vm2 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92939 | P3 / 38 | patriksimek / vm2 | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92934 | P3 / 38 | patriksimek / vm2 | v4.0 9.5 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63472 | P3 / 38 | vendurehq / vendure | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-54626 | P3 / 38 | HappySeaFox / sail | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-47252 | P3 / 38 | julien040 / anyquery | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-20284 | WATCH / 28 | Cisco / Cisco Identity Services Engine Software | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93014 | WATCH / 30 | RosarioSIS / RosarioSIS | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92985 | WATCH / 30 | siyuan-note / siyuan | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92971 | WATCH / 30 | InternLM / lmdeploy | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92952 | WATCH / 30 | patriksimek / vm2 | v4.0 8.9 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89418 | WATCH / 30 | Google / protobuf-javascript (aka google-protobuf npm package) | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-86038 | WATCH / 30 | libp2p / js-libp2p | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-85715 | WATCH / 30 | mattiasw / ExifReader | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77614 | WATCH / 30 | opencast / opencast | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63460 | WATCH / 30 | vendurehq / vendure | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-54504 | WATCH / 30 | andrea9293 / mcp-documentation-server | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-54446 | WATCH / 30 | Labs64 / NetLicensing-MCP | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-52851 | WATCH / 30 | traccar / traccar | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-50285 | WATCH / 30 | pomerium / pomerium | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93467 | WATCH / 28 | HGiga / OAKlouds-custom_page-2.0 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93393 | WATCH / 28 | MongoDB Inc. / C Driver | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92956 | WATCH / 28 | patriksimek / vm2 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-92954 | WATCH / 28 | patriksimek / vm2 | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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
- EPSS 未確認：30；Exploitation status 未確認：3。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-18T05:24:29.078693+00:00`；Delta generated at：`2026-09-18T05:24:29.078693+00:00`。

---

## 可驗證資料來源

- **CVE-2026-87886** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87886) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (security-advisory.acronis.com)](https://security-advisory.acronis.com/advisories/SEC-10986) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-20284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20284)
- **CVE-2026-92960** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92960)
- **CVE-2026-92957** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92957)
- **CVE-2026-92955** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92955)
- **CVE-2026-92950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92950)
- **CVE-2026-92947** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92947)
- **CVE-2026-92941** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92941)
- **CVE-2026-92939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92939)
- **CVE-2026-92934** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92934)
- **CVE-2026-63472** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63472)
- **CVE-2026-54626** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54626)
- **CVE-2026-47252** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47252)
- **CVE-2026-93014** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93014)
- **CVE-2026-92985** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92985)
- **CVE-2026-92971** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92971)
- **CVE-2026-92952** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92952)
- **CVE-2026-89418** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89418)
- **CVE-2026-86038** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86038)
- **CVE-2026-85715** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85715)
- **CVE-2026-77614** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77614)
- **CVE-2026-63460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63460)
- **CVE-2026-54504** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54504)
- **CVE-2026-54446** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54446)
- **CVE-2026-52851** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-52851)
- **CVE-2026-50285** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-50285)
- **CVE-2026-93467** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93467)
- **CVE-2026-93393** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93393)
- **CVE-2026-92956** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92956)
- **CVE-2026-92954** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92954)
- **CVE-2026-92953** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92953)
- **CVE-2026-92951** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92951)
- **CVE-2026-92948** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92948)
- **CVE-2026-92946** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92946)
- **CVE-2026-92944** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92944)
- **CVE-2026-92943** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92943)
- **CVE-2026-92940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92940)
- **CVE-2026-92938** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92938)
- **CVE-2026-92937** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92937)
- **CVE-2026-92935** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92935)
- **CVE-2026-91039** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91039)
- **CVE-2026-88952** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88952)
- **CVE-2026-87701** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87701)
- **CVE-2026-86863** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86863)
- **CVE-2026-86533** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86533)
- **CVE-2026-85889** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85889)
- **CVE-2026-85885** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85885)
- **CVE-2026-85878** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85878)
- **CVE-2026-85500** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85500)
- **CVE-2026-83944** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83944)
- **CVE-2026-82761** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82761)
- **CVE-2026-79752** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79752)
- **CVE-2026-77903** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77903)
- **CVE-2026-76949** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76949)
- **CVE-2026-76834** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76834)
- **CVE-2026-70200** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70200)
- **CVE-2026-70009** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70009)
- **CVE-2026-69865** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69865)
- **CVE-2026-69843** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69843)
- **CVE-2026-69399** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69399)
- **CVE-2026-62874** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62874)
- **CVE-2026-62108** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62108)
- **CVE-2026-62104** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62104)
- **CVE-2026-62101** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62101)
- **CVE-2026-54767** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54767)
- **CVE-2026-54752** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54752)
- **CVE-2026-54734** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54734)
- **CVE-2026-54670** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54670)
- **CVE-2026-54627** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54627)
- **CVE-2026-54618** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54618)
- **CVE-2026-54617** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54617)
- **CVE-2026-54501** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54501)
- **CVE-2026-54460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54460)
- **CVE-2026-54237** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54237)
- **CVE-2026-54053** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54053)
- **CVE-2026-45143** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45143)
- **CVE-2026-45140** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45140)
- **CVE-2026-92936** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92936)
- **CVE-2026-92926** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92926)
- **CVE-2026-89038** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89038)
- **CVE-2026-86000** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86000)
- **CVE-2026-61793** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61793)
- **CVE-2026-54546** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54546)
- **CVE-2026-44235** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-44235)
- **CVE-2026-92992** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92992)
- **CVE-2026-92962** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92962)
- **CVE-2026-79419** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79419) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79419)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
