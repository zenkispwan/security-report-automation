# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**56** 筆符合目前門檻的重要變化；事件統計：EPSS_INCREASED=1、NEW_CVE=53、NEW_KEV=2。
- Intelligence 候選：**30** 筆；P1 **3**、P2 **0**、P3 **4**、WATCH **23**。
- Baseline：state / generated_at=2026-09-24T05:39:42.995467+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-71362、CVE-2026-5430、CVE-2026-85046。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **56** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-71362｜Adobe / Commerce and Magento
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.02335 / percentile=0.82839
- **CISA KEV**：listed=true / date_added=2026-09-24 / due_date=2026-09-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-08-11T18:18:21.610 / 2026-09-25T04:17:40.903
- **官方描述（原文）**：Adobe Commerce and Magento contains an incorrect authorization vulnerability that could allow an attacker to leverage this vulnerability to gain elevated access to sensitive resources without any user interaction.

### 2. CVE-2026-5430｜WSO2 / Multiple Products
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00374 / percentile=0.28583
- **CISA KEV**：listed=true / date_added=2026-09-24 / due_date=2026-09-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-08-06T08:16:33.240 / 2026-09-25T04:17:36.437
- **官方描述（原文）**：WSO2 API Control Plane, API Manager, Traffic Manager & Universal Gateway contain a path traversal vulnerability that could allow for unrestricted file upload and lead to remote code execution.

### 3. CVE-2026-85046｜Google / Chromium V8
- **Delta event**：EPSS_INCREASED (from=0.01462; to=0.48881)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.48881 / percentile=0.98838
- **CISA KEV**：listed=true / date_added=2026-09-04 / due_date=2026-09-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-03T20:17:24.210 / 2026-09-21T13:17:10.970
- **官方描述（原文）**：Google Chromium V8 contains a type confusion vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.

### 4. CVE-2026-97360｜rejetto / hfs2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T14:18:22.703)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T14:18:22.703 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：HFS2 version 2.4.0 and earlier contains an unauthenticated arbitrary file access vulnerability that allows unauthenticated attackers to read, write, append, and delete files anywhere the HFS service account has filesystem access outside the shared folder. Attackers can exploit the macro dispatcher's lack of authorization model combined with the path resolver's failure to confine absolute paths to manipulate the template engine and compromise the confidentiality, integrity, and availability of the host.

### 5. CVE-2026-93425｜Dokploy / dokploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T16:17:25.990)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T16:17:25.990 / 2026-09-24T18:19:07.280
- **官方描述（原文）**：Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the patch.readRepoDirectories tRPC procedure passes the user-controlled repoPath value from apps/dokploy/server/api/routers/patch.ts into a shell command in packages/server/src/services/patch-repo.ts without safe argument quoting. An authenticated organization member with service:read permission can inject shell metacharacters into repoPath and execute arbitrary commands through child_process.exec as root in the Dokploy container. The supplied service identifier is used only to resolve the server and does not constrain repoPath. Because the standard deployment mounts /var/run/docker.sock, container-root command execution can be used to control Docker and compromise the host and its managed applications. This issue is fixed in version 0.29.13.

### 6. CVE-2026-61742｜bytebase / dbhub
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T18:17:16.173)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T18:17:16.173 / 2026-09-24T18:17:16.173
- **官方描述（原文）**：DBHub is a database MCP server for Postgres, MySQL, SQL Server, Oracle, MariaDB, SQLite. Versions prior to 0.22.5 expose an unauthenticated HTTP MCP endpoint when started with the documented HTTP transport mode, for example `--transport http --port 8080`. The HTTP server attempts to protect browser-origin access by checking whether the `Origin` hostname equals the `Host` hostname, then reflecting the validated `Origin` into `Access-Control-Allow-Origin`. This does not stop DNS rebinding. After an attacker-controlled hostname rebinds to a victim-accessible DBHub HTTP server, both `Origin` and `Host` can contain the attacker-controlled hostname, so DBHub accepts the request and dispatches MCP tool calls. As a result, a malicious website can deterministically invoke DBHub MCP tools from the victim's browser without prompt injection or model involvement. With the default demo configuration this can read and write the demo SQLite database; with a real configured database, the same primitive can read, enumerate, and potentially write database contents depending on DBHub's configured tool permissions and database credentials. Version 0.22.5 fixes the issue.

### 7. CVE-2026-61732｜BitterSecurity / Decepticon
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T18:17:15.860)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T18:17:15.860 / 2026-09-24T19:17:14.910
- **官方描述（原文）**：Decepticon is an autonomous hacking agent for red teams. Versions prior to 1.1.17 wrap web crawl results — the output of agent reconnaissance against target services — into LLM messages without neutralizing ChatML special-token literals. Under the BYOK (Bring Your Own Key) deployment model, users configure their own LLM credentials to any OpenAI-compatible endpoint. Most open-source and self-deployed model providers (vLLM, SGLang, Ollama, LM Studio, text-generation-webui, etc.) do not filter special-token literals from user content in their default configurations. Those literals are parsed into structural role-boundary token IDs, meaning an attacker string planted in a target web page forges a new operator turn the model treats as authoritative, bypassing Decepticon's agent guardrails and resulting in arbitrary command execution inside the Kali Linux sandbox. Version 1.1.17 patches the issue.

### 8. CVE-2026-97362｜rejetto / hfs2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T15:18:01.393)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T15:18:01.393 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：HFS2 version 2.4.0 and earlier contains a denial of service vulnerability that allows unauthenticated attackers to cause a complete and persistent loss of availability by sending a single crafted request. Attackers can trigger a hung serving thread that enters a busy loop, rendering the entire file server unresponsive to all clients without self-recovery until an operator manually restarts the service.

### 9. CVE-2026-88390｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T17:17:08.143)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:08.143 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：An out-of-bounds write vulnerability in jslGetTokenValueAsString() in Espruino 2v29 (commit bffc6d0) allows crafted JavaScript input containing an overlong token to trigger a one-byte write beyond the JsLex.token buffer in RELEASE/NO_ASSERT builds. The out-of-bounds write corrupts the adjacent tokenValue pointer, resulting in memory corruption and potentially causing application crashes or denial of service.

### 10. CVE-2026-88382｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T17:17:07.670)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:07.670 / 2026-09-24T21:00:46.893
- **官方描述（原文）**：hiredis commit 29ea279 (post-v1.5.0) contains an uncontrolled memory allocation vulnerability in its RESP aggregate parser.

### 11. CVE-2026-88376｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T17:17:07.313)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:07.313 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：Bento4 1.6.0.0 contains an integer underflow vulnerability in AP4_AvccAtom::Create() and AP4_HvccAtom::Create(). A specially crafted MP4 file containing an avcC or hvcC atom with a declared size smaller than the atom header size can cause the payload-size calculation to wrap to a large unsigned value. The resulting invalid buffer allocation and copy operations can cause application termination, leading to denial of service.

### 12. CVE-2026-88372｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T17:17:07.083)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:07.083 / 2026-09-24T21:04:40.340
- **官方描述（原文）**：libsndfile 1.2.2 contains an integer overflow vulnerability in mat4_read_header() when parsing crafted MAT4 (MATLAB v4) files.

### 13. CVE-2026-88368｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T16:17:13.730)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T16:17:13.730 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：NanoSVG commit 239e102ec contains an incorrect numeric conversion vulnerability in the rasterizer's nsvg__addActive() function. A specially crafted SVG document containing sufficiently large geometry coordinates can cause fixed-point-scaled edge coordinates to exceed the range representable by int. The rasterizer subsequently converts these values to int without range validation, resulting in undefined behavior and possible process termination, leading to denial of service.

### 14. CVE-2026-88357｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T16:17:12.957)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T16:17:12.957 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：nDPI 5.1.0 contains a memory access issue in the DNS dissector and serializer deserialization code. Specially crafted network input can cause byte-buffer addresses at odd offsets to be cast to uint16_t or wider integer pointers and directly dereferenced without alignment checks. This results in undefined behavior and can cause process termination in UBSan-instrumented builds or on strict-alignment architectures, leading to denial of service.

### 15. CVE-2026-79764｜Termix-SSH / Termix
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T17:17:06.510)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:06.510 / 2026-09-24T19:39:45.600
- **官方描述（原文）**：Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 2.5.0 until 2.5.1, the /homepage/proxy endpoint accepts an authenticated user's url query parameter and passes it to http.get or https.get without destination restrictions. In src/backend/database/routes/homepage-proxy-routes.ts, new URL performs only syntactic validation, allowing requests to loopback, RFC1918, link-local, and cloud metadata destinations. The endpoint returns the complete fetched JSON response, so a low-privilege or self-registered account can exfiltrate internal service data and cloud credentials. This issue is fixed in version 2.5.1.

### 16. CVE-2026-77581｜alam00000 / bentopdf
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T16:17:10.943)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T16:17:10.943 / 2026-09-24T16:17:10.943
- **官方描述（原文）**：BentoPDF is a client-side PDF toolkit that is self hostable. In 2.8.6 and earlier, the certificate and timestamp CORS proxy in cloudflare/cors-proxy-worker.js uses isPrivateOrReservedHost() to validate a supplied hostname separately from the DNS resolution used by fetch(targetUrl), allowing an attacker-controlled hostname to resolve to an internal or reserved destination after validation. A certificate-like path can satisfy ALLOWED_PATH_PATTERNS, and direct clients can forge the browser-oriented Origin header. Deployments without PROXY_SECRET skip the optional signature check, while the signature is an anti-abuse measure rather than a destination-security boundary. The proxy has a 10 MB response limit and can relay response bodies from reachable destinations. The advisory identifies both the official Worker deployment and self-hosted instances as impacted where the Worker execution environment can reach internal or reserved destinations. This vulnerability is fixed in 2.8.7.

### 17. CVE-2026-77294｜mauriceboe / TREK
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T19:17:16.570)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T19:17:16.570 / 2026-09-24T19:17:16.570
- **官方描述（原文）**：TREK is a collaborative travel planner. Prior to 3.3.0, TREK allows an authenticated user to store an attacker-controlled llm_base_url through the settings API when the LLM_PARSING feature is enabled. Write permission to the target trip instance is required to trigger the vulnerable AI-assisted import path. The value is consumed by the clients in server/src/nest/llm-parse/clients/openai-compatible.client.ts, server/src/nest/llm-parse/clients/anthropic.client.ts, and server/src/nest/llm-parse/router/ollama-format.client.ts without applying the server-side request forgery guard. Triggering AI-assisted trip parsing causes the server to request the supplied destination, and upstream error response text can be returned in parsing warnings. This permits internal service discovery and access to link-local cloud metadata, with possible disclosure of infrastructure credentials and subsequent modification of protected cloud resources. This issue is fixed in version 3.3.0.

### 18. CVE-2026-77293｜mauriceboe / TREK
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T19:17:16.397)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T19:17:16.397 / 2026-09-24T19:17:16.397
- **官方描述（原文）**：TREK is a collaborative travel planner. Prior to 3.3.0, the DELETE /api/trips/:tripId/collab/notes/:noteId/files/:fileId endpoint authorizes an authenticated user against the attacker-controlled tripId but deleteNoteFile in server/src/services/collabService.ts resolves the target only by note and file identifiers without requiring the file to belong to that trip. A user with edit access to any trip can submit identifiers belonging to another user's trip and permanently delete that note-file attachment. Sequential identifiers make broad targeting practical, while attachment read operations remain trip-scoped and are not affected. This issue is fixed in version 3.3.0.

### 19. CVE-2026-63203｜logto-io / logto
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T16:17:08.700)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T16:17:08.700 / 2026-09-24T16:17:08.837
- **官方描述（原文）**：Logto is the modern, open-source auth infrastructure for SaaS and AI apps. From 1.31.0 until 1.42.0, the Account API handlers in packages/core/src/routes/account/third-party-tokens.ts allow a caller holding a same-user access token with only the openid scope to retrieve stored social or enterprise SSO provider access tokens through GET /api/my-account/identities/{target}/access-token or GET /api/my-account/sso-identities/{connectorId}/access-token. The handlers authenticate the user but do not require the identities scope that protects neighboring identity-detail operations, bypassing the intended Account API consent boundary. Exploitation requires federated token-set storage to be enabled and the affected user to have authenticated through a supported connector. A low-trust application can use the disclosed provider token against upstream APIs within that token's granted scopes. This issue is fixed in version 1.42.0.

### 20. CVE-2026-62368｜grokability / snipe-it
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T17:17:05.207)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:05.207 / 2026-09-24T18:17:17.453
- **官方描述（原文）**：Snipe-IT is an IT asset/license management system. Prior to 8.7.0, a user with the customfields.create permission can store markup in CustomField.name, and app/Presenters/AssetPresenter.php assigns that value as an unescaped bootstrap-table header title. When another user opens an asset-list page associated with the fieldset, the stored markup executes on page load in that user's Snipe-IT session. This can expose same-origin data and perform authenticated actions with the victim's privileges, including privilege escalation when a superuser views the affected list. This issue is fixed in version 8.7.0.

### 21. CVE-2026-61816｜zbateson / mail-mime-parser
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T18:17:17.303)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T18:17:17.303 / 2026-09-24T19:17:15.240
- **官方描述（原文）**：zbateson/mail-mime-parser is a mail mime parser alternative to PHP's imap* functions and Pear libraries for reading messages in Internet Message Format RFC 822. Starting in version 2.0.0 and prior to version 3.0.6 and 4.0.2, an uncontrolled resource consumption / algorithmic complexity vulnerability (CWE-400) affects any application that parses untrusted email with this library. Three independent parsing paths are super-linear in cost, so a byte-size cap on the caller side does **not** bound the work done. A crafted message under 2 MB can consume seconds of CPU or hundreds of megabytes to multiple gigabytes of memory (leading to an out-of-memory kill), enabling denial of service. The parse is lazy, but the cost is paid on the first `getAllParts()` or content read. This is fxed in 4.0.2 and 3.0.6. The fixes add configurable limits on multipart nesting depth and on header count / total header size (recording a parse error past the threshold rather than throwing), and change sibling append to O(n). Users should upgrade to one of these (or later) versions. Versions 2.x are also affected but are end-of-life and will not receive patches; users on those lines should upgrade to a fixed release. (Versions prior to 2.0 used a different parser and are not affected by all three paths.) These costs are super-linear, so an input byte-size cap alone does not bound them. Until upgrading, restrict exposure of the parser to untrusted input, and run parsing under a constrained memory_limit and execution time limit so a malicious message fails its own request rather than exhausting the host.

### 22. CVE-2026-56736｜thorsten / phpMyFAQ
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T15:17:24.100)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T15:17:24.100 / 2026-09-24T15:17:24.240
- **官方描述（原文）**：phpMyFAQ is an open source FAQ web application. A stored cross-site scripting (XSS) vulnerability in versions prior to 4.2.0-alpha allows any unauthenticated user (or low-privileged registered user) to inject arbitrary JavaScript that executes in an administrator's browser when they review or edit a user-submitted FAQ entry. This leads to admin account takeover via session theft. The vulnerability exists because `html_entity_decode()` converts HTML entities into executable HTML after `strip_tags()` has already passed them through, and the admin template renders the content with Twig's `|raw` filter without any output sanitization. Version 4.2.0-alpha fixes the issue.

### 23. CVE-2026-97413｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T17:17:18.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:18.990 / 2026-09-25T05:17:04.603
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: RDMA/rtrs-srv: Fix integer underflow in process_read and process_write usr_len is read from a network-supplied message field (le16_to_cpu) and used to compute data_len = off - usr_len without validating that usr_len <= off. A malicious RDMA client can send usr_len > off causing an integer underflow, resulting in data_len wrapping to a huge size_t value which is then passed to the rdma_ev callback as a memory length, leading to out-of-bounds memory access. Fix by reading and validating usr_len <= off before rtrs_srv_get_ops_ids() in both process_read() and process_write(), ensuring the early return path acquires no reference and has no resource leak.

### 24. CVE-2026-97404｜OpenStack / Zaqar
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T15:18:01.537)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T15:18:01.537 / 2026-09-24T21:08:22.573
- **官方描述（原文）**：In OpenStack Zaqar before 22.0.2, WSGI transport mishandles the URL-Signature header. By sending a request with an empty URL-Signature header, an unauthenticated remote attacker who knows a target project's UUID may bypass both Keystone authentication and pre-signed URL verification, resulting in the ability to read, enumerate, create, and delete that project's queues, messages, claims, and subscriptions. By additionally claiming an administrative role, the attacker may also perform administrative operations, such as managing pools and flavors in admin_mode deployments. Only deployments using the WSGI transport with an authentication strategy configured are affected; the websocket transport is not affected.

### 25. CVE-2026-97359｜rejetto / hfs2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T14:18:22.533)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T14:18:22.533 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：HFS2 version 2.4.0 and earlier contains a template injection vulnerability in the multipart upload handler that allows unauthenticated attackers to achieve remote code execution by embedding malicious template syntax in a filename. Attackers can craft a filename containing a closing template quoting sequence followed by an exec macro, which bypasses the authorization check in the dispatcher to execute arbitrary commands on the underlying host system.

### 26. CVE-2026-93291｜Eufy / Omni C20
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T20:17:34.463)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T20:17:34.463 / 2026-09-24T21:25:27.050
- **官方描述（原文）**：Omni C20 lacks proper certificate validation which could allow an attacker to perform a man-in-the-middle attack which could allow them to execute arbitrary code.

### 27. CVE-2026-93289｜Eufy / Omni C20
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T20:17:34.137)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T20:17:34.137 / 2026-09-24T21:25:27.050
- **官方描述（原文）**：The affected products are vulnerable to command injection attack that could allow an unauthenticated attacker to execute system commands during the pairing process.

### 28. CVE-2026-93228｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T16:17:18.253)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T16:17:18.253 / 2026-09-25T05:17:00.567
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: svcrdma: Reject Write/Reply chunks with segcount 0 A peer can send a Write or Reply chunk whose segcount field is zero. xdr_check_write_chunk() only rejects segcount > rc_maxpages, so zero passes the range check, and xdr_inline_decode(stream, 0) returns the current (non-NULL) cursor without advancing. The function returns true and pcl_alloc_write() then links a struct svc_rdma_chunk with ch_segcount == 0 onto rc_write_pcl or rc_reply_pcl. An earlier patch in this series made pcl_for_each_segment() safe for ch_segcount == 0, so this no longer drives the memory walk it used to. Rejecting the malformed frame at the decode boundary is still worthwhile as defense in depth: it keeps degenerate zero-segment chunks off the parsed chunk lists entirely, so any future consumer that walks ch_segments directly cannot observe one, and it makes the zero-floor easy to backport to trees where the macro change is more intrusive. RFC 8166 has no meaning for a Write/Reply chunk that describes no remote buffer, so no legitimate client is affected. xdr_check_reply_chunk() funnels Reply chunks through xdr_check_write_chunk() and inherits the same rejection. pcl_alloc_write() also links each chunk onto the parsed chunk list before filling its segment array. If a future change weakens the segcount-0 rejection, an incomplete chunk is visible to consumers during the fill loop. Reorder so that list_add_tail() follows the segment fill loop, ensuring only fully-populated chunks appear on the list.

### 29. CVE-2026-93207｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T16:17:15.357)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T16:17:15.357 / 2026-09-25T05:16:58.630
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: SUNRPC: Zero rpc_gss_wire_cred at svcauth_gss_decode_credbody() entry svcauth_gss_decode_credbody() writes the caller's rpc_gss_wire_cred field by field and assigns gc_ctx.len only on the success tail. The caller storage is svcdata->clcred, which lives in the per-svc_rqst gss_svc_data and is reused across requests. Early decode failures leave partially decoded state mixed with residue from the prior request. The trailing body_len tightness check is the sharpest case: xdr_stream_decode_opaque_inline() has already written gc_ctx.data with a borrowed inline pointer into the current request's XDR pages, but gc_ctx.len retains its prior value. Once the request pages are released the pooled clcred carries a dangling pointer paired with a stale length. Zero the caller's rpc_gss_wire_cred at function entry so that every early-return path leaves a deterministic all-zero cred. On the trailing tightness-check path, gc_ctx.len is now zero instead of stale, which neuters length-driven consumers such as gss_svc_searchbyctx() that would otherwise walk the dangling data pointer.

### 30. CVE-2026-91187｜dashbit / nimble_zta
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T14:18:18.667)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T14:18:18.667 / 2026-09-24T19:39:45.600
- **官方描述（原文）**：Improper Verification of Cryptographic Signature vulnerability in dashbit nimble_zta allows an unauthenticated remote attacker to authenticate as an arbitrary Cloudflare service token. Applications using the Cloudflare Zero Trust authentication strategy are affected. verify_token/2 in lib/nimble_zta/cloudflare.ex matches the result of JOSE.JWT.verify/2 against {_, token, _s}, which discards the boolean verification result and returns the decoded token after a failed signature check. The attacker sends a forged JWT in the cf-access-jwt-assertion header, carrying the expected iss claim and the seven service token claims. verify_iss/2 reads the iss claim from the forged token, so it rejects nothing, and the service token path then returns those claims as the authenticated identity. This issue affects nimble_zta: from 0.1.2 before 0.1.3.

### 31. CVE-2026-90481｜PortSwigger / Burp Suite DAST
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T15:17:51.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T15:17:51.760 / 2026-09-24T21:08:22.573
- **官方描述（原文）**：In PortSwigger Burp Suite DAST (formerly Burp Suite Enterprise Edition) before 2026.8, an authentication bypass can occur via an alternate path or channel.

### 32. CVE-2026-86860｜ServiceNow / ServiceNow AI Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T19:17:18.733)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T19:17:18.733 / 2026-09-25T04:17:48.557
- **官方描述（原文）**：ServiceNow has remediated a missing authorization vulnerability that was identified in the ServiceNow AI Platform. This vulnerability could enable an unauthenticated user, in certain circumstances, to extract instance data beyond what was intended, resulting in privilege escalation. ServiceNow deployed a security update to hosted instances and ServiceNow provided the update to our partners and self-hosted customers. We are not currently aware of malicious exploitation against ServiceNow instances. We recommend customers promptly apply appropriate updates or upgrade to a patched release if they have not already done so.

### 33. CVE-2026-81630｜Botslab / G980H
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T21:18:48.737)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T21:18:48.737 / 2026-09-24T21:25:27.050
- **官方描述（原文）**：The Botslab G980H dash camera firmware does not adequately verify the authenticity of firmware updates. The update process retrieves firmware through an unprotected connection and relies on an integrity value supplied with the firmware instead of a trusted cryptographic signature. A suitably positioned attacker who intercepts a firmware download, or an authenticated attacker who submits a crafted update, could install modified firmware and execute unauthorized code on the device.

### 34. CVE-2026-81549｜IBM / DataStage on Cloud Pak for Data
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T15:17:39.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T15:17:39.897 / 2026-09-24T19:41:16.513
- **官方描述（原文）**：IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to obtain sensitive information due to improper validation of the X-Forwarded-Proto header.

### 35. CVE-2026-79766｜Termix-SSH / Termix
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T17:17:06.650)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:06.650 / 2026-09-24T17:17:06.650
- **官方描述（原文）**：Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 2.4.1 until 2.5.1, an authenticated Termix administrator can store attacker-controlled domain and email values through PATCH /users/acme-ssl-settings and trigger their interpolation into a certbot shell command through POST /users/acme-ssl-request. In src/backend/database/routes/acme-ssl-routes.ts, child_process.execSync invokes /bin/sh -c with those values only wrapped in double quotes, so shell metacharacters can execute arbitrary operating-system commands as the Termix backend process. Both HTTP webroot and DNS Cloudflare challenge modes are affected, and compromise exposes Termix databases, process secrets, stored credentials, and network reachability. This issue is fixed in version 2.5.1.

### 36. CVE-2026-78312｜Deltaww / DIAEnergie
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T09:17:08.553)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00345 / percentile=0.2517
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T09:17:08.553 / 2026-09-24T19:39:45.600
- **官方描述（原文）**：Path Traversal in DIAEnergie. This issue affects DIAEnergie: before 1.11.00.022.

### 37. CVE-2026-78308｜Deltaww / DIAEnergie
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T09:17:08.043)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00346 / percentile=0.25343
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T09:17:08.043 / 2026-09-24T19:39:45.600
- **官方描述（原文）**：Improper Authentication vulnerability in DIAEnergie allows Authentication Bypass. This issue affects DIAEnergie: before 1.11.00.022.

### 38. CVE-2026-61741｜http4s / http4s-scala-xml
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T18:17:16.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T18:17:16.013 / 2026-09-24T18:17:16.013
- **官方描述（原文）**：http4s-scala-xml provides `EntityDecoder[F, scala.xml.Elem]` instances that parse XML message bodies. Prior to versions 0.24.1 and 1.0.0-M39, these decoders used a `javax.xml.parsers.SAXParserFactory` obtained from `SAXParserFactory.newInstance` without any security configuration. With the JDK's default settings, the parser resolves DOCTYPE declarations, external general and parameter entities, and external DTDs.An application that uses these decoders to parse untrusted XML is vulnerable to XML External Entity (XXE) attacks. An attacker can craft a request that discloses local files readable by the service process, performs server-side request forgery (SSRF) against internal network resources, and/or causes denial of service through entity expansion. Versions 0.24.1 and 1.0.0-M39 fix the issue.

### 39. CVE-2026-61604｜ixofoundation / ixo-blockchain
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T18:17:15.707)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T18:17:15.707 / 2026-09-24T19:17:14.790
- **官方描述（原文）**：The ixo Blockchain is a Layer 1 blockchain that runs on both Testnet and Mainnet. Prior to version 8.0.0, the x/bonds module moved funds from an address that was resolved from a DID verification method, without verifying that the resolved address belonged to the transaction signer. Affected handlers included MsgMakeOutcomePayment, MsgBuy, MsgSell, MsgSwap, and MsgWithdrawShare, as well as the batch order processor. Because any account may list an arbitrary blockchainAccountID as a verification method on a DID it controls (without the consent of that address's owner), an attacker could register victims' addresses as verification methods on their own DID and then move the victims' balances into a bond the attacker controlled — later withdrawing and bridging the proceeds off-chain. This was exploited on ixo mainnet (ixo-5) on 2026-06-20. The attack required no victim keys, signatures, or system compromise — any account holding a balance in a token a bond could use was at risk. This was fixed in v8.0.0, delivered via the on-chain v8 software-upgrade. The x/bonds module is disabled: every bonds message is rejected on all routes (top-level, authz, CosmWasm, and ICA), and the bonds batch EndBlocker is a no-op so no further reserve movements can occur. All node operators and validators must upgrade to v8.0.0. The flaw is in chain state-machine logic and can only be remediated by running the patched binary. There is no application-level workaround. The vulnerability is in consensus logic; remediation requires the network to run the patched (v8.0.0) binary. The bonds module remains disabled in v8.0.0 and will only be re-enabled in a future release once the signer-authorization model has been corrected.

### 40. CVE-2026-19072｜Rapid7 / Velociraptor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T13:17:09.500)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T13:17:09.500 / 2026-09-25T04:17:34.920
- **官方描述（原文）**：Velociraptor stores the compiled VQL in the hunt object internally to avoid having to recompile the artifacts for each endpoint in the hunt. Although the field "compiled_collector_args" is an internal field, Velociraptor allowed the field to be set from a user API call. This allows another user who can schedule a hunt (minimal role of "investigator" ) to set the compiled VQL statements for the hunt bypassing any ACL checks that would normally be applied. This flaw can then be escalated to allow the "investigator" user to run arbitrary VQL statements as an administrator user on the Velociraptor server.

### 41. CVE-2026-13249｜Honeywell / PD45 Industrial Printer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T19:17:13.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T19:17:13.080 / 2026-09-24T20:43:32.537
- **官方描述（原文）**：An unauthenticated Remote Code Execution via Arbitrary File Upload vulnerability in the web management interface in Honeywell PD45 Industrial Printer version F10.19.010040, allows upload of attacker controlled files without requiring authentication. An attacker could potentially exploit this vulnerability, leading to the execution of malicious files and commands. Honeywell also recommends updating to the most recent firmware version, Honeywell PD45 Industrial Printer firmware F10.22.030745, which includes a fix for this vulnerability.

### 42. CVE-2026-13016｜ServiceNow / ServiceNow AI Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T19:17:11.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T19:17:11.820 / 2026-09-24T21:00:46.893
- **官方描述（原文）**：ServiceNow has remediated a SQL injection vulnerability that was identified in the ServiceNow AI Platform. This vulnerability could enable an unauthenticated user, in certain circumstances, to execute arbitrary SQL statements against the instance's underlying database and gain access to, or modify, instance data beyond what was intended. ServiceNow deployed a security update to hosted instances and ServiceNow provided the update to our partners and self-hosted customers. We are not currently aware of malicious exploitation against ServiceNow instances. We recommend customers promptly apply appropriate updates or upgrade to a patched release if they have not already done so.

### 43. CVE-2026-12227｜visualcomposer / Visual Composer Website Builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T10:17:32.623)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00769 / percentile=0.53634
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T10:17:32.623 / 2026-09-24T16:17:06.650
- **官方描述（原文）**：The Visual Composer Website Builder plugin for WordPress is vulnerable to Local File Inclusion in all versions up to, and including, 45.16.0 via the `vcv-template` parameter. This makes it possible for unauthenticated attackers to include and execute arbitrary files on the server, allowing the execution of any PHP code in those files. This can be used to bypass access controls, obtain sensitive data, or achieve code execution in cases where images and other “safe” file types can be uploaded and included.

### 44. CVE-2026-97182｜halo-dev / Halo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T13:17:19.507)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T13:17:19.507 / 2026-09-24T15:18:01.087
- **官方描述（原文）**：A security vulnerability has been detected in halo-dev Halo up to 2.25.4/2.26.1. Affected is an unknown function of the file application/src/main/java/run/halo/app/content/comment/ReplyNotificationSubscriptionHelper.java of the component SpEL Handler. Such manipulation leads to improper neutralization. The attack may be performed from remote. The exploit has been disclosed publicly and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 45. CVE-2026-97062｜Webkul / Aureus ERP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T14:18:22.317)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T14:18:22.317 / 2026-09-24T15:18:00.963
- **官方描述（原文）**：Aureus ERP through 1.6.0 stores uploaded SVG files on its public disk and serves them from the application origin, allowing authenticated users to upload malicious SVG files containing JavaScript. Attackers can craft SVG files with script elements that execute in the application's origin when the file URL is opened directly, enabling session cookie theft and CSRF token exfiltration.

### 46. CVE-2026-97058｜alexei / sprintf-js
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T14:18:21.840)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T14:18:21.840 / 2026-09-24T21:08:22.573
- **官方描述（原文）**：sprintf-js through 1.1.3 passes unbounded precision specifiers to toFixed, toExponential, and toPrecision methods without validation, causing uncaught RangeError exceptions. Attackers who control format strings can inject precision values exceeding ECMAScript limits to abort calling operations with minimal payload.

### 47. CVE-2026-88384｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T17:17:07.907)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:07.907 / 2026-09-24T21:08:22.573
- **官方描述（原文）**：OpenEXR 3.4.14 contains a NULL Pointer Dereference in the C++ attribute parsing path. A specially crafted EXR file containing an unknown-type attribute with dataSize set to zero causes the parser to create an opaque attribute with a NULL packed_data pointer. The OpaqueAttribute constructor passes the NULL pointer to memcpy() without validating the zero-size condition, resulting in undefined behavior and process termination, leading to denial of service.

### 48. CVE-2026-79758｜Termix-SSH / Termix
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T16:17:11.107)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T16:17:11.107 / 2026-09-24T19:39:45.600
- **官方描述（原文）**：Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 1.8.0 until 2.5.1, authenticated Termix users can access the server-stats API without per-host authorization. GET /status returns statuses for hosts the requester cannot access, GET /status/:id accepts an attacker-supplied numeric host identifier, and POST /clear-connections permits a regular user to clear the global SSH connection pool. The affected src/backend/ssh/server-stats.ts routes expose host online or offline state and lastChecked timestamps and can disrupt other users' active sessions or pooled connections. Unauthenticated requests remain blocked, but authentication alone does not preserve tenant isolation. This issue is fixed in version 2.5.1.

### 49. CVE-2026-61811｜wazuh / wazuh
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T18:17:16.990)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T18:17:16.990 / 2026-09-24T19:17:15.127
- **官方描述（原文）**：Wazuh is an open-source security platform providing unified XDR and SIEM protection for endpoints and cloud workloads. From 3.8.0 until 4.14.7, the _getattributes() function in src/os_xml/os_xml.c recursively processes every XML attribute without a depth limit while allocating two large local buffers in each stack frame. An enrolled agent can submit a Windows EventChannel event containing an element with enough attributes to exhaust the analysisd worker-thread stack, trigger a segmentation fault, and interrupt log ingestion. The element-depth limit in _ReadElem() does not constrain the number of attributes on one element, so it does not prevent this condition. This issue is fixed in version 4.14.7.

### 50. CVE-2026-48540｜krayin / laravel-crm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T20:17:29.117)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T20:17:29.117 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：Krayin CRM through 2.2.6 contains a stored client-side template injection vulnerability that allows authenticated attackers to execute arbitrary JavaScript in other users' browsers by injecting Vue.js template expressions into the lead title field. Attackers can craft a lead title containing double-brace template syntax that reaches the Vue template compiler, enabling prototype chain traversal to retrieve the Function constructor and execute attacker-supplied JavaScript in the application origin for every user who views the affected lead record.

### 51. CVE-2026-47132｜thorsten / phpMyFAQ
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T17:17:04.723)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:04.723 / 2026-09-24T18:17:13.453
- **官方描述（原文）**：phpMyFAQ is an open source FAQ web application. Prior to version 4.2.0-alpha, an authenticated SQL LIKE wildcard injection vulnerability in phpMyFAQ’s chat user search allows any logged-in user to bypass the intended display-name search filter and enumerate active users. The endpoint escapes SQL string syntax but does not escape `%` and `_`, which remain active `LIKE` wildcards. Version 4.2.0-alpha patches the issue.

### 52. CVE-2026-4637｜Paessler GmbH / PRTG Network Monitor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T10:17:37.813)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T10:17:37.813 / 2026-09-24T20:43:32.537
- **官方描述（原文）**：Paessler PRTG Network Monitor before version 26.2.120.1449 is affected by a reflected Cross-Site Scripting (XSS) vulnerability. When a request is made for a non-existent resource ending in \".htm\", the web interface returns an HTTP 403 \"Forbidden Path\" error page that echoes the requested URL path into the HTML response body without proper output encoding or sanitization. An unauthenticated, remote attacker can craft a URL containing an HTML/JavaScript payload in the path (e.g. https:////welcome.htm) and, once a victim with an active PRTG session opens the crafted link, execute arbitrary JavaScript in the security context of the PRTG web interface. Because the PRTG session cookie is not protected with the HttpOnly attribute, successful exploitation allows the attacker to read and exfiltrate the victim's session cookie, potentially leading to session hijacking.

### 53. CVE-2026-97323｜YunaiV / ruoyi-vue-pro
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T19:17:21.820)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T19:17:21.820 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：A vulnerability was determined in YunaiV/zhijiantianya ruoyi-vue-pro up to 2026.08. This impacts the function getOriginalFilename of the file yudao-module-mp/src/main/java/cn/iocoder/yudao/module/mp/service/material/MpMaterialServiceImpl.java of the component File Upload. Executing a manipulation can lead to path traversal. It is possible to launch the attack remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 54. CVE-2026-97321｜YunaiV / ruoyi-vue-pro
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T19:17:21.430)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T19:17:21.430 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：A vulnerability has been found in YunaiV/zhijiantianya ruoyi-vue-pro up to 2026.08. The impacted element is the function GoViewDataServiceImpl.getDataBySQL of the file yudao-module-report/src/main/java/cn/iocoder/yudao/module/report/service/goview/GoViewDataServiceImpl.java of the component GoView Data Endpoint. Such manipulation of the argument sql leads to sql injection. The attack may be performed from remote. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 55. CVE-2026-97232｜volotat / Anagnorisis
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T18:19:09.217)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T18:19:09.217 / 2026-09-24T21:08:55.030
- **官方描述（原文）**：A vulnerability was determined in volotat Anagnorisis up to 0.4.2. Affected by this vulnerability is the function get_file_content/save_file_content/move_files/start_streaming of the file page.html. This manipulation causes path traversal. The attack can be initiated remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 56. CVE-2026-97179｜未確認 / O2OA
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T11:17:06.600)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T11:17:06.600 / 2026-09-24T16:17:28.597
- **官方描述（原文）**：A security vulnerability has been detected in O2OA up to 9.5.3/10.0.2. This vulnerability affects the function list of the file o2server/x_base_core_project/src/main/java/com/x/base/core/project/connection/CipherConnectionAction.java of the component Cipher Connection Handler. Such manipulation of the argument fileUrl leads to information disclosure. It is possible to launch the attack remotely. The exploit has been disclosed publicly and may be used. The vendor was contacted early about this disclosure but did not respond in any way.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-71362｜Adobe / Commerce and Magento
- **Title**：Adobe Commerce and Magento Incorrect Authorization Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.02335 / percentile=0.82839
- **CISA KEV**：listed=true / date_added=2026-09-24 / due_date=2026-09-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Adobe Commerce and Magento contains an incorrect authorization vulnerability that could allow an attacker to leverage this vulnerability to gain elevated access to sensitive resources without any user interaction.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-5430｜WSO2 / Multiple Products
- **Title**：WSO2 Multiple Products Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00374 / percentile=0.28583
- **CISA KEV**：listed=true / date_added=2026-09-24 / due_date=2026-09-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WSO2 API Control Plane, API Manager, Traffic Manager & Universal Gateway contain a path traversal vulnerability that could allow for unrestricted file upload and lead to remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-85046｜Google / Chromium V8
- **Title**：Google Chromium V8 Type Confusion Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.48881 / percentile=0.98838
- **CISA KEV**：listed=true / date_added=2026-09-04 / due_date=2026-09-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium V8 contains a type confusion vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-97360 | P3 / 38 | rejetto / hfs2 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93425 | P3 / 38 | Dokploy / dokploy | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-61742 | P3 / 38 | bytebase / dbhub | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-61732 | P3 / 38 | BitterSecurity / Decepticon | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-97362 | WATCH / 30 | rejetto / hfs2 | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88390 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88382 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88376 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88372 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88368 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88357 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79764 | WATCH / 30 | Termix-SSH / Termix | v3.1 7.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77581 | WATCH / 30 | alam00000 / bentopdf | v3.1 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77294 | WATCH / 30 | mauriceboe / TREK | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77293 | WATCH / 30 | mauriceboe / TREK | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63203 | WATCH / 30 | logto-io / logto | v3.1 7.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-62368 | WATCH / 30 | grokability / snipe-it | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-61816 | WATCH / 30 | zbateson / mail-mime-parser | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-56736 | WATCH / 30 | thorsten / phpMyFAQ | v3.1 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97413 | WATCH / 28 | Linux / Linux | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-97404 | WATCH / 28 | OpenStack / Zaqar | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-97359 | WATCH / 28 | rejetto / hfs2 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93291 | WATCH / 28 | Eufy / Omni C20 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93289 | WATCH / 28 | Eufy / Omni C20 | v4.0 9.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93228 | WATCH / 28 | Linux / Linux | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93207 | WATCH / 28 | Linux / Linux | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-91187 | WATCH / 28 | dashbit / nimble_zta | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：6；缺少 Product：6；缺少 Title：27。
- EPSS 未確認：27；Exploitation status 未確認：5。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-25T05:38:02.420690+00:00`；Delta generated at：`2026-09-25T05:38:02.420690+00:00`。

---

## 可驗證資料來源

- **CVE-2026-71362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71362) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-71362) · [Vendor / Advisory (helpx.adobe.com)](https://helpx.adobe.com/security/products/magento/apsb26-92.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-5430** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-5430) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-5430) · [Vendor / Advisory (security.docs.wso2.com)](https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85046) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85046) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-97360** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97360)
- **CVE-2026-93425** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93425)
- **CVE-2026-61742** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61742)
- **CVE-2026-61732** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61732)
- **CVE-2026-97362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97362)
- **CVE-2026-88390** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88390)
- **CVE-2026-88382** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88382)
- **CVE-2026-88376** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88376)
- **CVE-2026-88372** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88372)
- **CVE-2026-88368** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88368)
- **CVE-2026-88357** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88357)
- **CVE-2026-79764** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79764)
- **CVE-2026-77581** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77581)
- **CVE-2026-77294** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77294)
- **CVE-2026-77293** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77293)
- **CVE-2026-63203** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63203)
- **CVE-2026-62368** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62368)
- **CVE-2026-61816** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61816)
- **CVE-2026-56736** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56736)
- **CVE-2026-97413** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97413)
- **CVE-2026-97404** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97404)
- **CVE-2026-97359** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97359)
- **CVE-2026-93291** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93291)
- **CVE-2026-93289** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93289)
- **CVE-2026-93228** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93228)
- **CVE-2026-93207** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93207)
- **CVE-2026-91187** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91187)
- **CVE-2026-90481** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90481)
- **CVE-2026-86860** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86860)
- **CVE-2026-81630** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81630)
- **CVE-2026-81549** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81549)
- **CVE-2026-79766** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79766)
- **CVE-2026-78312** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78312) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-78312)
- **CVE-2026-78308** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78308) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-78308)
- **CVE-2026-61741** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61741)
- **CVE-2026-61604** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61604)
- **CVE-2026-19072** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19072)
- **CVE-2026-13249** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13249)
- **CVE-2026-13016** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13016)
- **CVE-2026-12227** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12227) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-12227)
- **CVE-2026-97182** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97182)
- **CVE-2026-97062** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97062)
- **CVE-2026-97058** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97058)
- **CVE-2026-88384** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88384)
- **CVE-2026-79758** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79758)
- **CVE-2026-61811** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61811)
- **CVE-2026-48540** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48540)
- **CVE-2026-47132** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47132)
- **CVE-2026-4637** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-4637)
- **CVE-2026-97323** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97323)
- **CVE-2026-97321** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97321)
- **CVE-2026-97232** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97232)
- **CVE-2026-97179** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97179)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
