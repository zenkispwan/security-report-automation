# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**123** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=2、NEW_CVE=119、NEW_KEV=3。
- Intelligence 候選：**30** 筆；P1 **4**、P2 **0**、P3 **0**、WATCH **26**。
- Baseline：state / generated_at=2026-09-16T05:30:26.871699+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-76460、CVE-2026-58704、CVE-2026-87886、CVE-2026-20284。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **123** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-76460｜Cisco / Identity Services Engine
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T21:17:21.430)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-16T21:17:21.430 / 2026-09-17T04:18:01.527
- **官方描述（原文）**：Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) contain an incorrect use of privileged APIs vulnerability that could allow an unauthenticated, remote attacker to gain unauthorized access to the affected device by bypassing the web-based management interface.

### 2. CVE-2026-58704｜Google / Pixel
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00112 / percentile=0.01564
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-15T19:17:32.297 / 2026-09-17T04:17:54.930
- **官方描述（原文）**：Google Pixel devices contain an improper authorization vulnerability in the cellular modem. A logic error may allow an attacker to bypass permission checks and escalate privileges.

### 3. CVE-2026-87886｜Acronis / Backup
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 85；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、DELTA_NEW_KEV(+15)
- **CVSS**：未確認
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：未確認 / 未確認
- **官方描述（原文）**：Acronis Backup plugin for cPanel & WHM and extension for Plesk contains an incorrect default permissions vulnerability that could allow for privilege escalation.

### 4. CVE-2026-20284｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T21:17:09.090)
- **Risk**：P1 / score 53；reasons：ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=active / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T21:17:09.090 / 2026-09-17T04:17:40.157
- **官方描述（原文）**：A vulnerability in the SXP REST API of Cisco ISE could allow an authenticated, remote attacker to conduct SQL injection attacks. This vulnerability is due to insufficient validation of user-supplied input in REST API calls. An attacker could exploit this vulnerability by sending crafted input to an affected device. A successful exploit could allow the attacker to view or modify data on the underlying database for the affected device. In single-node deployments, successful exploitation of this vulnerability could cause the affected ISE node to become unavailable, resulting in a DoS condition. In that condition, endpoints that have not already authenticated would be unable to access the network until the node is restored. To exploit this vulnerability, the attacker must have valid administrative credentials, have the SXP service enabled, and have at least one SXP connection configured.

### 5. CVE-2026-92719｜quickwit-oss / quickwit
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T18:17:22.837)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T18:17:22.837 / 2026-09-16T18:17:22.837
- **官方描述（原文）**：Quickwit through 0.9.0 fails to validate the host and scheme of the queue_url parameter in SQS file sources, allowing attackers to make the node issue requests to arbitrary internal addresses. Attackers can supply a malicious queue_url to the create-source API to scan internal networks and fingerprint services based on connection response differences.

### 6. CVE-2026-92604｜StamusNetworks / scirius
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T18:17:22.083)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T18:17:22.083 / 2026-09-16T18:17:22.083
- **官方描述（原文）**：Scirius through 3.8.0 contains an arbitrary file write vulnerability in the PCAP filestore upload endpoint that allows default User role users to write attacker-controlled JSON content to filesystem paths. Attackers can supply path traversal sequences in the uploaded document's _id field to escape the intended directory and write files with .json extension to arbitrary locations as root.

### 7. CVE-2026-92601｜stylefeng / Guns
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:18:20.453)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:18:20.453 / 2026-09-16T18:17:21.957
- **官方描述（原文）**：Guns through 8.3.5 contains an improper access control vulnerability in SysNoticeController where requiredPermission defaults to false and is not overridden by any action methods. Authenticated users without assigned roles can exploit this to create, edit, delete, publish and retract system-wide notices affecting arbitrary users and departments.

### 8. CVE-2026-92566｜datageartech / datagear
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:19:02.127)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:19:02.127 / 2026-09-16T16:17:23.267
- **官方描述（原文）**：DataGear through 6.0.0 contains a server-side request forgery vulnerability in the /dataSet/preview/Http endpoint that allows unauthenticated attackers to execute arbitrary HTTP requests by supplying a caller-controlled URI. Attackers can issue GET, POST, PUT, PATCH, or DELETE requests to internal endpoints and cloud metadata services, receiving full response bodies without authentication or validation.

### 9. CVE-2026-92469｜zlt2000 / microservices-platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T14:17:17.767)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T14:17:17.767 / 2026-09-16T18:17:21.720
- **官方描述（原文）**：zlt2000 microservices-platform through 6.0.0 contains an authorization bypass vulnerability in the file-center module DELETE /files/{id} endpoint that performs no ownership validation. Authenticated attackers can enumerate file identifiers via GET /files and delete arbitrary users' files and metadata by supplying their identifiers to the delete endpoint.

### 10. CVE-2026-92466｜zlt2000 / microservices-platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T14:17:17.313)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T14:17:17.313 / 2026-09-16T19:47:01.197
- **官方描述（原文）**：zlt2000 microservices-platform through 6.0.0 contains a missing authorization vulnerability where the zlt.security.auth.urlPermission.enable flag defaults to false, disabling all permission checks after authentication. Authenticated users with no roles can access administrative APIs including user management, role assignment, and Elasticsearch index operations by bypassing the disabled authorization enforcement.

### 11. CVE-2026-92459｜guchengwuyue / yshop-crm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T12:17:07.330)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T12:17:07.330 / 2026-09-16T18:17:21.517
- **官方描述（原文）**：yshop-crm through 2.1.3 contains a missing authorization vulnerability in the CrmCluesController receiveCustomer endpoint that allows authenticated back-office users to claim sales leads without proper permission checks. Attackers can invoke the lead-claim endpoint to reassign leads from other employees to themselves by overwriting the ownerUserId field, with no access logging or quota validation to prevent bulk lead theft.

### 12. CVE-2026-92456｜guchengwuyue / yshop-crm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T12:17:06.900)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T12:17:06.900 / 2026-09-16T19:47:01.197
- **官方描述（原文）**：yshop-crm through 2.1.3 fails to enforce authorization on the saveRedisSet and getRedisSet endpoints in CrmCustomerController, allowing any authenticated back-office user to read and modify installation-wide lead-allocation and customer auto-recycling policy. Attackers can invoke these endpoints to manipulate shared Redis keys controlling customer auto-recycling behavior, causing mass customer data deletion, disabling lead recycling, or blocking customer creation across the deployment.

### 13. CVE-2026-92398｜Ruijie / RG-EW3000GX
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:18:19.417)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:18:19.417 / 2026-09-16T18:17:19.550
- **官方描述（原文）**：A vulnerability was found in Ruijie RG-EW3000GX EW_3.0(1)B11P380. Affected by this issue is some unknown functionality of the file /etc/rg_config/admin of the component user_list_note Module. Performing a manipulation of the argument Name results in os command injection. It is possible to initiate the attack remotely. The exploit has been made public and could be used.

### 14. CVE-2026-92397｜Ruijie / RG-EW3000GX
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T16:17:22.960)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T16:17:22.960 / 2026-09-16T20:17:48.090
- **官方描述（原文）**：A vulnerability has been found in Ruijie RG-EW3000GX EW_3.0(1)B11P380. Affected by this vulnerability is the function cc_set of the file unifyframe-sgi.elf of the component configChange. Such manipulation of the argument data.url leads to os command injection. The attack may be performed from remote. The exploit has been disclosed to the public and may be used.

### 15. CVE-2026-86043｜zalando / skipper
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T19:17:51.993)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T19:17:51.993 / 2026-09-16T20:17:36.343
- **官方描述（原文）**：Skipper is an HTTP router and reverse proxy for service composition. Prior to version 0.27.37, the opaAuthorizeRequestWithBody filter can authorize an oversized request after Skipper truncates the body presented to Open Policy Agent because the input.truncated_body signal is derived from Content-Length rather than the actual read result. In filters/openpolicyagent/openpolicyagent.go, ExtractHttpBodyOptionally truncates bodies at maxBodyBytes, while filters/openpolicyagent/internal/envoy/skipperadapter.go copies the request headers without adding a Content-Length value that reflects the truncation. For an HTTP/1.1 request using Transfer-Encoding: chunked or an HTTP/2 request without Content-Length, a body-inspecting policy that follows the prior mitigation and permits input.truncated_body equal to false can evaluate only the truncated prefix, allow the request, and then forward the full oversized body to the protected upstream. This residual issue is distinct from CVE-2026-50197. This issue is fixed in version 0.27.37.

### 16. CVE-2026-85731｜oras-project / oras-go
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:18:15.833)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:18:15.833 / 2026-09-16T18:17:17.963
- **官方描述（原文）**：oras-go is a Go library for managing OCI artifacts. Prior to 2.6.2, content/file.Store extraction of OCI layers marked with io.deis.oras.content.unpack=true can write outside the store working directory. The pushDir path through extractTarDirectory and ensureLinkPath validates symlink targets lexically, resolveRelToBase skips its parent-symlink walk for root-level entries, and writeFile follows a terminal symlink when opening a regular file. A malicious archive can therefore create a symlink chain whose lexical target remains inside the extraction root but whose resolved target is an attacker-selected absolute path, then overwrite that target with a same-named regular-file entry even when AllowPathTraversalOnWrite is false. Pulling an attacker-controlled artifact can create or overwrite any file writable by the process and may lead to code execution. This issue is fixed in version 2.6.2.

### 17. CVE-2026-84997｜reactphp / http
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:18:00.863)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:18:00.863 / 2026-09-16T15:18:00.863
- **官方描述（原文）**：react/http is an event-driven, streaming HTTP client and server implementation for ReactPHP. From 0.6.0 until 1.11.1, React\Http\Io\ChunkedDecoder could enter an infinite loop while processing a malformed Transfer-Encoding: chunked body because handleData required its buffer to shrink on every iteration. An incomplete terminal-chunk trailer without CRLF left the buffer unchanged after strpos returned false, and exactly two non-CRLF bytes after a completed non-terminal chunk bypassed both the error and wait guards. The affected decoder processes request bodies for React\Http\HttpServer and response bodies for React\Http\Browser, allowing a malicious client to freeze a server or a malicious or compromised server to freeze a client. A reverse proxy that normalizes inbound requests may protect the server direction but does not protect outbound Browser requests. This issue is fixed in version 1.11.1.

### 18. CVE-2026-63128｜modelcontextprotocol / rust-sdk
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:17:39.960)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:17:39.960 / 2026-09-16T16:17:14.440
- **官方描述（原文）**：RMCP is an official Rust SDK for the Model Context Protocol. Prior to 2.0.0, the rmcp crate's stateful Streamable HTTP server in crates/rmcp/src/transport/streamable_http_server/tower.rs allows an unauthenticated client to send a well-formed JSON-RPC POST that is not an initialization request, or an initialization request with a mismatched protocol header, causing StreamableHttpService::handle_post to call LocalSessionManager.create_session before validating the message. An early validation failure returns without removing the inserted LocalSessionHandle from LocalSessionManager.sessions, permanently retaining session and channel state for the server process lifetime. Repeated requests can grow the shared session table without bound, degrade legitimate-client latency through lock contention, exhaust memory, and terminate the server. This issue is fixed in version 2.0.0.

### 19. CVE-2026-63127｜modelcontextprotocol / rust-sdk
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:17:39.817)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:17:39.817 / 2026-09-16T16:17:14.323
- **官方描述（原文）**：RMCP is an official Rust SDK for the Model Context Protocol. Prior to 2.0.0, the rmcp crate's OAuth implementation in crates/rmcp/src/transport/auth.rs omits the RFC 9728 resource field from ResourceServerMetadata and allows discover_oauth_server_via_resource_metadata to use protected-resource metadata without confirming that the returned resource identifier exactly matches the configured MCP server. A malicious MCP server can publish metadata for a different legitimate MCP resource and its authorization server, causing a victim who connects and completes the authorization flow to obtain a legitimate access token that the client subsequently sends to the malicious server. The attacker can capture the token and impersonate the victim against the legitimate MCP resource within the token's granted scopes. This issue is fixed in version 2.0.0.

### 20. CVE-2026-63126｜square / wire
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T19:17:24.013)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T19:17:24.013 / 2026-09-16T20:17:26.370
- **官方描述（原文）**：Wire provides gRPC and protocol buffers for Android, Kotlin, Swift, and Java. Prior to 6.4.5 and 7.0.0-alpha04, Wire protobuf readers do not consistently validate attacker-controlled lengths against the current logical message boundary before advancing cursors, pointers, limits, slices, or allocations. In Kotlin, ProtoAdapter.decode(ByteArray) and ProtoAdapter.decode(ByteString) use ByteArrayProtoReader32.internalNextLengthDelimited(), where a positive oversized length can wrap pos + length to a negative limit and escape the existing negative-length check. Related ProtoReader, ReadBuffer.readVarint(), ReadBuffer.verifyAdditional(count:), packed-repeated, nested-message, and ProtoDecoder.decodeSizeDelimited(_:from:) paths can cross logical boundaries, perform pointer arithmetic, reserve capacity, or convert an unrepresentable size before proving the requested bytes exist. An attacker who supplies malformed protobuf bytes can cause unchecked exceptions, traps, out-of-bounds behavior, or excessive allocation, resulting in denial of service without known confidentiality, integrity, or code-execution impact. This issue is fixed in versions 6.4.5 and 7.0.0-alpha04.

### 21. CVE-2026-59974｜stanfordnlp / stanza
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:17:28.877)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:17:28.877 / 2026-09-16T18:17:10.320
- **官方描述（原文）**：Stanza is a Stanford NLP Python library for tokenization, sentence segmentation, NER, and parsing of many human languages. Prior to 1.14.0, stanza.resources.common.unzip in stanza/resources/common.py passes downloaded model and resource archives to zipfile.ZipFile.extractall without validating member paths, and the vulnerable extraction path is reachable through stanza.download and stanza.install_corenlp. A malicious archive containing parent-directory traversal entries can write outside the intended model directory, allowing files writable by the Stanza process to be overwritten and potentially enabling code execution through modified shell configuration, SSH authorization data, Python packages, or executable scripts. This issue is fixed in version 1.14.0.

### 22. CVE-2026-92808｜Altium / Altium Enterprise Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:49.117)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:49.117 / 2026-09-16T20:17:49.117
- **官方描述（原文）**：A server-side request forgery (SSRF) vulnerability exists in the UnifiedLogin service of Altium Enterprise Server. An unauthenticated network attacker can cause the server to issue outbound HTTP requests to a destination of the attacker's choosing, including internal services that are reachable only from the server itself. One such internal service exposes server configuration and credential material without authentication, relying only on the request originating locally. Because the forged requests originate from the server process, that check is satisfied. An unauthenticated attacker can therefore retrieve stored credentials and use them to obtain an administrative session, resulting in full compromise of the server and all of its services. Altium 365 cloud deployments are not affected, as the affected endpoint is disabled in cloud mode.

### 23. CVE-2026-92805｜uvdesk / community-skeleton
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T21:17:30.267)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T21:17:30.267 / 2026-09-16T21:17:30.267
- **官方描述（原文）**：UVdesk Community Skeleton through 1.1.8 fails to authenticate or validate installation state on wizard endpoints in ConfigureHelpdesk controller actions. Unauthenticated attackers can repoint the database and create super administrator accounts by submitting crafted requests to wizard endpoints, gaining full control of the instance.

### 24. CVE-2026-92787｜feast-dev / feast
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T21:17:28.023)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T21:17:28.023 / 2026-09-16T21:17:28.023
- **官方描述（原文）**：Feast through 0.66.0 fails to verify JWT token signatures before establishing user identity, allowing attackers to bypass all role-based access control by presenting an unverified token with a hardcoded claim value. Attackers can obtain trusted internal identity and gain unchecked read and write access to all entities, feature views, data sources, and permission policies on the server.

### 25. CVE-2026-92785｜Angel-ML / angel
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T21:17:27.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T21:17:27.730 / 2026-09-16T21:17:27.730
- **官方描述（原文）**：Angel through 3.3.0 deserializes untrusted setAlgoMetrics payload using Kryo without class registration or allowlist validation. Unauthenticated network attackers can instantiate arbitrary classes or exhaust coordinator memory by sending crafted serialized objects to the master RPC endpoint.

### 26. CVE-2026-92749｜chaitin / SafeLine
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T21:17:23.563)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T21:17:23.563 / 2026-09-16T21:17:23.563
- **官方描述（原文）**：SafeLine through 9.4.1 derives the management console session-signing secret from a time-seeded math/rand generator, allowing attackers to reconstruct the key offline. Unauthenticated remote attackers who can bound the install timestamp can regenerate the secret and forge valid administrator session cookies to gain control of protected sites.

### 27. CVE-2026-92720｜kubero-dev / kubero
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T18:17:22.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T18:17:22.990 / 2026-09-16T18:17:22.990
- **官方描述（原文）**：Kubero through 3.1.1 fails to apply authentication guards to the notifications API endpoints, allowing unauthenticated attackers to read webhook secrets and service URLs. Attackers can retrieve stored credentials and register malicious webhooks to intercept pipeline events or suppress alerting by deleting existing configurations.

### 28. CVE-2026-92717｜cobbr / Covenant
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T18:17:22.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T18:17:22.540 / 2026-09-16T18:17:22.540
- **官方描述（原文）**：Covenant through 0.6 registers the CovenantHub SignalR hub without an Authorize attribute, allowing unauthenticated callers to invoke CreateHttpListener and receive a signed JWT token. Attackers can use the obtained token to authenticate against the entire operator API and access grunts, credentials, binaries, events, and the operator roster.

### 29. CVE-2026-92578｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T22:18:28.053)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T22:18:28.053 / 2026-09-16T22:18:28.053
- **官方描述（原文）**：WWBN AVideo through 29.0 contains an authentication bypass vulnerability where the stored password hash is accepted as a valid login credential through two independent code paths in loginFromRequest() and encryptPasswordVerify(). Attackers who obtain the stored users.password hash value can authenticate as any user by submitting the hash directly to login endpoints, completely bypassing password verification.

### 30. CVE-2026-92576｜HKUDS / nanobot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T22:18:27.757)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T22:18:27.757 / 2026-09-16T22:18:27.870
- **官方描述（原文）**：HKUDS nanobot before 0.3.0 contains a server-side request forgery vulnerability in the WebFetchTool component where the _validate_url() function fails to block internal IP ranges and private addresses. Attackers can send messages instructing the bot to fetch cloud metadata endpoints, localhost services, and RFC 1918 addresses to extract IAM credentials and internal service data.

### 31. CVE-2026-92395｜@fastify/proxy-addr / @fastify/proxy-addr
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:19:01.857)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:19:01.857 / 2026-09-16T19:40:00.317
- **官方描述（原文）**：@fastify/proxy-addr is a Fastify plugin that determines a request's client address behind trusted reverse proxies, and it backs Fastify request.ip and request.ips. In versions 3.0.0 through 5.1.0, a trust subnet written in IPv4-mapped IPv6 notation with an IPv4-sized prefix, such as ::ffff:10.0.0.0/8 instead of the correct ::ffff:10.0.0.0/104, is accepted without error but trusts every IPv4 address on the internet rather than the block it names. Because the socket peer then becomes trusted at hop 0, any unauthenticated client can supply an arbitrary X-Forwarded-For header and control the address the application reads, which defeats IP-based access control, rate limiting, geolocation, and audit logging. The plugin inherited this defect from the upstream proxy-addr module (CVE-2026-90711). The issue is fixed in @fastify/proxy-addr 5.1.1, and users should upgrade to 5.1.1 or later. As a workaround, ensure any IPv4-mapped IPv6 trust subnet uses a prefix length of at least 97, or express the range in plain IPv4 notation.

### 32. CVE-2026-91843｜checkpoint / Quantum Security Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T14:17:13.947)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T14:17:13.947 / 2026-09-17T04:18:10.730
- **官方描述（原文）**：A stack overflow during the unauthenticated login process may allow an attacker to run arbitrary code remotely with root privileges.

### 33. CVE-2026-91106｜HP Inc. / HP Linux Imaging and Printing Software (HPLIP)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T19:18:03.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T19:18:03.587 / 2026-09-17T04:18:04.313
- **官方描述（原文）**：HP has identified and remediated multiple externally reported vulnerabilities within HPLIP. The findings affect several software components that could potentially enable remote code execution, privilege escalation, denial of service, information disclosure, or unauthorized file modification under certain conditions.

### 34. CVE-2026-91104｜HP Inc. / HP Linux Imaging and Printing Software (HPLIP)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T19:18:03.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T19:18:03.320 / 2026-09-17T04:18:03.750
- **官方描述（原文）**：HP has identified and remediated multiple externally reported vulnerabilities within HPLIP. The findings affect several software components that could potentially enable remote code execution, privilege escalation, denial of service, information disclosure, or unauthorized file modification under certain conditions.

### 35. CVE-2026-90049｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:18.263)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:18.263 / 2026-09-16T15:18:27.710
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: net: skbuff: don't skb_tx_error() the source skb in skb_zerocopy() skb_zerocopy() copies frags from @from into @to. On an skb_orphan_frags() failure it calls skb_tx_error(@from), a destructive operation on the source skb the copy helper does not own. That completes @from's zerocopy uarg and clears SKBFL_ALL_ZEROCOPY, including the SKBFL_SHARED_FRAG page-ownership marker. Both callers already report the failure on their own drop path. nfnetlink_queue does it at nla_put_failure, and Open vSwitch does it in the flow-miss drop arm of ovs_dp_process_packet(), so nothing is lost by dropping it here. On Open vSwitch's OVS_ACTION_ATTR_USERSPACE path the skb is not freed on this error: do_execute_actions() ignores output_userspace()'s return value and, unless the upcall was the last action, keeps forwarding the same skb through the flow's remaining actions. The uarg is completed while that skb is still in flight, telling the producer its buffers are free, and SKBFL_SHARED_FRAG is cleared on an skb the rest of the stack still handles. That flag is what makes esp_input() call skb_cow_data() instead of decrypting in place, so a later local ESP delivery can decrypt over frags the skb does not own privately. Leave error reporting to the callers.

### 36. CVE-2026-90048｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:18.140)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:18.140 / 2026-09-16T15:18:27.570
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: fs/ntfs3: fix slab-out-of-bounds write in ni_create_attr_list() ni_create_attr_list() allocates a fixed buffer of al_aligned(record_size) (== record_size) bytes and then walks every attribute of the primary MFT record, writing one ATTR_LIST_ENTRY per attribute and advancing the cursor by le_size(name_len), with no check against the end of the buffer; the total size is only computed after the loop. A minimum-size resident attribute occupies SIZEOF_RESIDENT (0x18 = 24) bytes on disk, but an unnamed attribute expands to le_size(0) (0x20 = 32) bytes in the list. Because the number of attributes in a record is not bounded (mi_enum_attr() accepts arbitrarily many equal-type, nameless minimum-size attributes), a crafted record packed with such attributes produces a list larger than record_size and overflows the heap buffer. This is reachable from a crafted, loop-mounted NTFS image: opening the file and adding an attribute (e.g. via setxattr) drives ntfs_set_ea() -> ni_insert_resident() -> ni_insert_attr() -> ni_ins_attr_ext() -> ni_create_attr_list(). BUG: KASAN: slab-out-of-bounds in ni_create_attr_list+0xc48/0x1058 Write of size 4 at addr ffff000008984c00 by task setfattr/345 ni_create_attr_list+0xc48/0x1058 ni_ins_attr_ext+0x510/0x7c0 ni_insert_attr+0x3f8/0x70c ni_insert_resident+0xc8/0x3b0 ntfs_set_ea+0x66c/0xd28 ntfs_setxattr+0x4d8/0x5b0 __arm64_sys_setxattr+0xa4/0x124 Allocated by task 345: ni_create_attr_list+0x188/0x1058 The buggy address belongs to the cache kmalloc-1k of size 1024 (the write lands at object+1024). Size the buffer from the actual attributes instead of assuming a single record_size is always enough.

### 37. CVE-2026-90042｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:17.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:17.450 / 2026-09-16T15:18:26.873
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: ceph: properly decrypt filenames in vmalloc() buffers The fscrypt subsystem uses the scatterlist crypto API, inheriting its requirement that any buffers are in the linear mapping region. However, the messenger client uses kvmalloc() to create buffers for messages, which will occasionally place those buffers in the vmalloc() region when physical memory fragmentation doesn't permit a large enough kmalloc(). The various callers of ceph_fname_to_usr() directly pass (slices of) raw messages from the MDS without considering that the messages may be in vmalloc() buffers, resulting in oopses especially on non-x86 platforms (see 'Closes:' for more details and a reproducer). Make ceph_fname_to_usr() explicitly tolerant of vmalloc()-allocated fname->ctext, fname->name, and/or oname->name buffers, using `tname` (which, when non-null, must be a linear address; when null, is briefly allocated as necessary) as a bounce buffer to avoid passing any inappropriate addresses to fscrypt_fname_disk_to_usr(). Additionally change parse_reply_info_readdir() -- the only function to supply its own `tname` -- to follow the new "tname must never come from vmalloc()" rule by passing NULL when the message is not in the linear region. Though this causes a per-dentry kmalloc()+kfree(), this overhead exists only when processing the minority of messages that spill into vmalloc(). My (crude) testing puts this at only about 1 in 8,000 readdir messages. Still, if the overhead proves unreasonable in the future, it is easy enough to mitigate: a future change could allocate a bounce buffer in parse_reply_info_readdir() and use that as `tname` instead.

### 38. CVE-2026-90038｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:17.010)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:17.010 / 2026-09-16T15:18:26.650
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: NFSD: Prevent client use-after-free during export state revocation nfsd4_revoke_export_states() has the same use-after-free as nfsd4_revoke_states(): it drops nn->client_lock across revoke_one_stid() and the following read of clp->cl_minorversion, but the stateid reference it holds does not pin the client. A teardown racing the dropped lock can free the client while revoke_one_stid() still dereferences it. exportfs -u drives this path through NFSD_CMD_UNLOCK_EXPORT, so an administrator removing an export can race a client expiry. Skip a client that is already expiring and otherwise pin it with cl_rpc_users under client_lock before dropping the lock, matching nfsd4_revoke_states().

### 39. CVE-2026-90037｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:16.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:16.910 / 2026-09-16T15:18:26.540
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: NFSD: Prevent client use-after-free during close_lru reaping An nfs4_openowner left on nn->close_lru after its final CLOSE keeps its last closed stateid in oo_last_closed_stid, holding only a raw pointer to its nfs4_client. The laundromat reaps timed-out entries, drops nn->client_lock, and calls nfs4_put_stid(), which dereferences the client through cl_lock. Nothing pins the client across that window, so a concurrent force_expire_client() can free it and nfs4_put_stid() reads freed memory. __destroy_client() hits the same race, walking clp->cl_openowners without cl_lock. Pin the client with cl_rpc_users before dropping client_lock, and skip clients already expiring. __destroy_client() then cleans up its own close_lru entries through release_last_closed_stateid(), so teardown no longer races the laundromat.

### 40. CVE-2026-90036｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:16.803)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:16.803 / 2026-09-16T15:18:26.420
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: NFSD: Prevent client use-after-free during blocked-lock reaping A bare lock owner -- its only remaining reference a blocked lock on nn->blocked_locks_lru -- holds a raw pointer to its nfs4_client but no reference keeping the client alive. When the per-net laundromat reaps such a lock, freeing the nbl drops the owner reference held through flc_owner, and the final nfs4_put_stateowner() takes the client's cl_lock. Because the laundromat detaches the nbl first, __destroy_client() no longer finds it, so a concurrent force_expire_client() can free the client before nfs4_put_stateowner() runs, dereferencing cl_lock in freed memory. Pin the client with cl_rpc_users before dropping nn->blocked_locks_lock, and skip clients already expiring, whose blocked locks __destroy_client() frees while holding an owner reference. Take nn->client_lock outside nn->blocked_locks_lock. Every other site holds nn->blocked_locks_lock as a leaf, acquiring no further lock, so placing nn->client_lock outside it cannot form a lock-order cycle.

### 41. CVE-2026-90012｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:13.890)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:13.890 / 2026-09-16T15:18:24.870
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: spi: Fix DMA mapping ownership on partial map failure If RX mapping fails after TX mapping succeeds, __spi_map_msg() unmaps TX but leaves tx_sg_mapped set. If TX mapping fails on a later transfer, mappings created for earlier transfers remain active. In both cases, cur_{tx,rx}_dma_dev have not yet been updated because they are assigned only after every transfer has been mapped. The subsequent spi_unmap_msg() may therefore unmap the TX mapping again or release earlier mappings using a NULL or stale device. Using a NULL device can trigger an oops. An empty SG table does not prevent the NULL dereference because dma_unmap_sg_attrs() accesses the device before checking the entry count. Publish both mapping devices before mapping starts and unwind all failures through __spi_unmap_msg(). This clears the mapping flags and releases each mapping once with the device that created it. Publishing the devices before the loop also refreshes them when no transfer needs mapping. No mapping flag is set in that case, so current users do not use the pointers as mapping owners.

### 42. CVE-2026-90011｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:13.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:13.760 / 2026-09-16T15:18:24.763
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: scsi: target: iscsi: Reserve a terminator byte for the login payload iscsi_target_check_login_request() rejects a login PDU whose DataSegmentLength exceeds MAX_KEY_VALUE_PAIRS, but the test is '>' and login->req_buf is allocated with exactly MAX_KEY_VALUE_PAIRS bytes. Since iscsit_get_login_rx() receives payload_length + padding bytes, where padding = ((-payload_length) & 3); any payload_length from 8189 to 8192 fills the whole 8192 byte buffer. The write stays in bounds, but no byte is left for a NUL terminator. The buffer is subsequently consumed as a C string. In the CHAP path chap_check_algorithm() calls kstrdup(a_str), and extract_param() calls strstr(in_buf, pattern) followed by strlen_semi(), none of which take a length. convert_null_to_semi() additionally rewrites every embedded NUL to ';', so even a payload made of well formed NUL separated key=value records is left without a terminator. These walk past the end of the object into adjacent slab memory. It is reachable by an unauthenticated initiator against a portal configured for CHAP; when authentication is not required iscsi_login_zero_tsih_s2() rewrites AuthMethod to None and the CHAP path is never entered. Allocate one extra byte. kzalloc() zeroes it and nothing ever writes to it, as every writer copies to offset 0 for at most MAX_KEY_VALUE_PAIRS bytes, so the buffer is always terminated.

### 43. CVE-2026-89990｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:10.133)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:10.133 / 2026-09-16T15:18:22.800
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: ceph: lock mutex in ceph_mds_check_access() MDS session OPEN handling replaces mdsc->s_cap_auths under mdsc->mutex, freeing the previous array and its strings. ceph_mds_check_access() traverses this array without holding the mutex. A concurrent session reopen can therefore free the array while it is being inspected, resulting in a use-after-free like this: Unable to handle kernel paging request at virtual address 003aaad64b2c8bb9 [...] Internal error: Oops: 0000000096000004 [#1] SMP Modules linked in: CPU: 56 UID: 2953037534 PID: 1253231 Comm: php-cgi8.4 Not tainted 6.18.45-i2-ampere #1146 NONE [..] pc : ceph_mds_check_access+0xd4/0x550 lr : ceph_mds_check_access+0xc8/0x550 [...] Call trace: ceph_mds_check_access+0xd4/0x550 (P) ceph_atomic_open+0x138/0xbe8 path_openat+0xa24/0xfa8 do_filp_open+0x94/0x158 do_sys_openat2+0x88/0xf8

### 44. CVE-2026-89972｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:07.953)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:07.953 / 2026-09-16T15:18:21.637
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: nvme: add missing SRCU grace period in error path nvme_alloc_ns() error path at out_unlink_ns removes ns from the namespace head siblings list with list_del_rcu(&ns->siblings) but does not wait for SRCU readers before freeing the namespace struct. Multipath code iterates the head->list under srcu_read_lock() in nvme_find_path() and nvme_mpath_revalidate_paths(), so a concurrent reader can still hold a reference to ns when kfree(ns) runs. The normal removal path in nvme_ns_remove() correctly calls synchronize_srcu(&ns->head->srcu) after list_del_rcu() to wait for in-progress readers. Add the same grace period in the error path.

### 45. CVE-2026-89970｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:07.660)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:07.660 / 2026-09-16T15:18:21.387
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: nvmet-auth: Synchronize timeout work during SQ teardown nvmet_auth_sq_free() cancels auth_expired_work with cancel_delayed_work(). If the work has already started, cancellation does not wait for the callback. Transport teardown can consequently free or reuse the queue containing struct nvmet_sq while nvmet_auth_expired_work() still accesses that SQ. Add a teardown-specific helper that synchronously drains the delayed work before freeing authentication state, and use it from nvmet_sq_destroy(). Keep the non-synchronous helper for in-band authentication state cleanup, where the SQ owner remains alive.

### 46. CVE-2026-89969｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:07.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:07.527 / 2026-09-16T15:18:21.240
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: nvmet-tcp: fix out-of-bounds write when receiving an over-long PDU nvmet_tcp_try_recv_pdu() reads a PDU header into the fixed 128-byte queue->pdu union, then computes the remaining payload length as queue->left = hdr->hlen - queue->offset + hdgst; and reads that many more bytes into &queue->pdu + queue->offset, without ever bounding the result against sizeof(queue->pdu). A struct nvme_tcp_icreq_pdu is itself 128 bytes, exactly the size of the union. Once a header digest has been negotiated (hdgst = 4), a second ICReq passes the hlen == nvmet_tcp_pdu_size() check but yields queue->left = 128 - 8 + 4 = 124, so bytes 8..132 are written into the 128-byte buffer -- 4 bytes past its end, over queue->hdr_digest and queue->data_digest. Those bytes are attacker-controlled (an ICReq carries no digest), and the duplicate ICReq is only rejected later, after the overflow. A remote unauthenticated host can thus corrupt kernel memory adjacent to the receive buffer. Reject any PDU whose declared length would read past the end of queue->pdu before the second recv.

### 47. CVE-2026-89930｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:02.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:02.290 / 2026-09-16T15:18:18.933
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: KVM: nVMX: Service local TLB flushes on failed nested VM-Enter KVM services local TLB flushes on "full" nested VM-Exits (through __nested_vmx_vmexit()), but not if a nested VM-Enter fails (e.g. due to failed VMCS checks in nested_vmx_enter_non_root_mode()). However, it is possible that KVM had queued TLB flushes that need to be performed, even if the nested VM-Enter was not successful. For example, if VPID is disabled for L2 (via nested_vmx_transition_tlb_flush(), or if via the MSR load lists, as the SDM says: If any MSR is being loaded in such a way that would architecturally require a TLB flush, the TLBs are updated so that, after VM entry, the logical processor will not use any translations that were cached before the transition. The SDM is unclear about when the TLB flush should occur, and whether or not a failed VM entry would flush the TLB, so it is safer to always do the TLB flush in this case. More concretely, KVM also updates the last VPID L1 used for L2 in nested_vmx_transition_tlb_flush() (i.e. last_vpid), even if the VM entry ultimately fails. With the current code, KVM could miss a TLB flush if L1 changes L2's VPID, then does a failed VM entry followed by a successful one, as the failed VM entry would update last_vpid but not actually flush the TLB. Servicing local TLB flushes on failed VM entries makes sure that the TLB is always flushed when last_vpid is updated.

### 48. CVE-2026-89918｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:00.867)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:00.867 / 2026-09-16T15:18:18.010
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: KVM: arm64: Correctly handle end of VA space TLBI invalidation Our TLB invalidation by VA code is based on comparing two ranges, one defined by the TLB, and one defined by the TLBI instruction. Each range is defined by a start and a size. However, the way the comparison is done doesn't account for address rollover, as it compares an address with (base + size). This works nicely until this expression represent the last page/block in the TTBR1 VA space, as the result is a big fat 0. And a failed TLB invalidation. Rewrite the comparison in a way that is immune to the address rollover (making the end address inclusive instead of exclusive), and move this into a common helper that is used by both VA and IPA invalidations, as suggested by Hyunwoo Kim (although the IPA version didn't suffer from this particular problem, obviously).

### 49. CVE-2026-89916｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:00.657)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:00.657 / 2026-09-16T15:18:17.883
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: KVM: arm64: Make VNCR invalidation participate in MMU invalidation retry A VNCR TLB invalidation can occur on one vcpu while another vcpu is faulting in this same page. Without correctly handling this, we can end up with the following scenario: - vcpu A walks the PTs to translate VNCR - before vcpu A is able to grab the MMU lock to insert the TLB, vcpu B updates the S1 PTs with an invalid entry, and issues a TLBI S1E2 for this VA - vcpu A inserts the TLB for something that is now invalid This isn't a new problem, and we manage S2 by having the MMU notifier to bump up mmu_invalidate_seq on invalidation so that the fault can be replayed. We can perform something similar here, and extend invalidate_vncr_va() to update the same counter, clearly indicating that the context has changed under our feet. This is safe as the invalidation always happen while holding the MMU lock for write, and that we sample the sequence number before walking S1.

### 50. CVE-2026-89915｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:00.553)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:00.553 / 2026-09-16T15:18:17.760
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: KVM: arm64: Remove VM-wide VNCR mapping counter The global VNCR mapping counter is used to decide whether an L1 provided VNCR page is mapped in L0 on any CPU at the point of dealing with a TLB invalidation. It is incremented when a mapping is made in the fixmap, and decremented when unmapped. As it turns out, this tracking has several flaws: - we are trying to invalidate TLBs, and the mapping is only an opportunistic consequence of the TLB. Checking this counter to decide whether a TLB needs to be invalidated may result in missed invalidations. - an L1 vcpu invalidating its own TLB (a very likely case) will not succeed in invalidating the VNCR pseudo TLB because that page is not mapped in L0 at this stage. Given that this tracking fails at delivering the minimum guarantees that are required and is only a performance optimisation, remove it completely.

### 51. CVE-2026-89914｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:17:00.443)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:17:00.443 / 2026-09-16T15:18:17.647
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: KVM: arm64: Sign-extend VA for range-based TLBI invalidation When the decode_range_tlbi() helper was moved to be used for S1 TLBIs, the required sign extension was omitted. Add it. As a result, special care must be taken to not overflow PA bits when this is used for S2 invalidation.

### 52. CVE-2026-89857｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:16:53.573)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:16:53.573 / 2026-09-16T15:18:13.657
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: scsi: qla2xxx: Hold qpair lock when sending NVMe LS reject qla_nvme_ls_reject_iocb() allocates from and advances the request ring through __qla2x00_alloc_iocbs() (which assumes the hardware_lock is held) and qla2x00_start_iocbs() (which advances the ring and rings the request-in doorbell), but takes no lock itself. Two of its callers invoke it without the producer lock held: - qla_nvme_xmt_ls_rsp(), the NVMe-FC .xmt_ls_rsp transport callback, on its error path, and - qla2xxx_process_purls_pkt(), run from the purex work/DPC context. Both use ha->base_qpair, whose qp_lock_ptr is hardware_lock, so they can run concurrently with normal I/O submission on the base ring and corrupt the ring producer state, leading to duplicated or dropped commands. The third caller, qla2xxx_process_purls_iocb(), runs inside qla24xx_process_response_queue() with the qpair lock already held and is safe; that is also why the lock cannot be taken inside the helper itself (it would recursively re-acquire hardware_lock on the response path). Take qp_lock_ptr around the two unlocked callers and document the helper as caller-locked. Both run in process context, so spin_lock_irqsave() is used and nothing in the locked region sleeps.

### 53. CVE-2026-89847｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:16:51.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:16:51.990 / 2026-09-16T15:18:12.967
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: scsi: qla2xxx: Avoid double completion in async IOCB timeout qla2x00_async_iocb_timeout() tries to abort a timed-out async IOCB. When qla24xx_async_abort_cmd() fails, both the SRB_LOGIN_CMD path and the SRB_CTRL_VP/default path scan outstanding_cmds[] for the SRB and then call sp->done(sp, QLA_FUNCTION_TIMEOUT) unconditionally, without checking whether the SRB was actually found and removed. If the response ISR completes the same handle first, it removes the SRB under qp_lock_ptr and runs sp->done() -> complete(sp->comp). The submitter qla24xx_control_vp() wakes from wait_for_completion(), clears sp->comp, drops its reference and returns, reclaiming the on-stack completion. The timer reference keeps the SRB alive across the timeout handler, but not the submitter's stack. The timeout then issues a second sp->done() -> qla_ctrlvp_sp_done(), which evaluates "if (sp->comp) complete(sp->comp)"; with the pointer loaded before the submitter's NULL store, complete() writes into the freed stack frame, a use-after-free. Track whether this path removed the SRB from outstanding_cmds and only call sp->done() when it did, so the command is completed exactly once by whichever path owns it. This mirrors the sp_found guard already used in qla24xx_abort_iocb_timeout().

### 54. CVE-2026-89846｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T11:16:51.853)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T11:16:51.853 / 2026-09-16T15:18:12.823
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: scsi: qla2xxx: Bound rsp_info_len to avoid OOB sense-data read In qla2x00_status_entry(), the FWI2 status path advances sense_data and shrinks par_sense_len by rsp_info_len: if (IS_FWI2_CAPABLE(ha)) { sense_data += rsp_info_len; par_sense_len -= rsp_info_len; } rsp_info_len is a 32-bit value taken directly from the target's FCP response (sf.rsp_data_len), while par_sense_len is the IOCB data area size (28 bytes for 24xx, 60 bytes for 29xx). A hostile or buggy target reporting an rsp_info_len larger than par_sense_len makes the unsigned subtraction underflow to a huge value and advances sense_data out of bounds. The underflowed par_sense_len then defeats the cap in qla2x00_handle_sense(): if (sense_len > par_sense_len) sense_len = par_sense_len; memcpy(cp->sense_buffer, sense_data, sense_len); so the memcpy reads up to SCSI_SENSE_BUFFERSIZE bytes from the out-of-bounds sense_data pointer, leaking adjacent response-ring/heap memory into the command's sense buffer. Clamp rsp_info_len to par_sense_len before the subtraction so par_sense_len can never underflow and sense_data stays within the IOCB data area. The fix sits before the comp_status switch, covering both qla2x00_handle_sense() call sites.

### 55. CVE-2026-89788｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T09:17:09.590)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00189 / percentile=0.08779
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T09:17:09.590 / 2026-09-16T15:18:09.007
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: ksmbd: fix tree connection use-after-free in smb2_tree_connect() ksmbd_tree_conn_connect() publishes a new tree connection in sess->tree_conns with a single reference and returns its pointer to smb2_tree_connect(). The handler continues to initialize the object and build the response after publication. A concurrent session logoff can erase the connection and drop that reference, freeing the object while the handler still uses it. BUG: KASAN: slab-use-after-free in smb2_tree_connect+0xe3d/0xf90 smb2_tree_connect (fs/smb/server/smb2pdu.c:2872) handle_ksmbd_work process_one_work worker_thread kthread After xa_store() succeeds, take a second reference before releasing tree_conns_lock. The original reference belongs to the xarray entry and the second belongs to the creating smb2_tree_connect() handler. Keep the references balanced in every path: - On normal exit or an error after publication, smb2_tree_connect() drops its creator reference. Error cleanup also calls ksmbd_tree_conn_disconnect(), which drops the xarray reference only if it removes the exact entry. - SMB2 TREE_DISCONNECT uses the same helper to remove the entry and drop its xarray reference. The request's existing lookup reference remains owned by the request and is released by the existing cleanup. - Session LOGOFF removes each entry and drops its xarray reference. If it wins the race, later cleanup sees that the entry is gone and does not drop that reference again. To enforce this ownership, claim the disconnected state and erase the exact entry atomically under tree_conns_lock. This guarantees one drop for the xarray reference and one drop by each in-flight user, regardless of which teardown path wins. If logoff removes the entry before initialization completes, fail the connect instead of marking the detached object TREE_CONNECTED.

### 56. CVE-2026-89786｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T09:17:09.330)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00205 / percentile=0.10809
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T09:17:09.330 / 2026-09-16T15:18:08.860
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: ext4: fix out-of-bounds read in ext4_read_inline_dir() ext4_read_inline_dir() can read a dirent header past the end of its inline buffer, triggering a slab-out-of-bounds read during getdents64(): BUG: KASAN: slab-out-of-bounds in __ext4_check_dir_entry Read of size 2 at addr ffff88800f3dd23c by task exploit/148 ... __ext4_check_dir_entry ext4_read_inline_dir iterate_dir The dirent payload lives in a buffer of exactly inline_size bytes: dir_buf = kmalloc(inline_size, GFP_NOFS); but iteration runs in a position space extra_offset bytes larger (extra_size = extra_offset + inline_size) so the synthetic "." and ".." land at their block-dir offsets. A dirent is formed at "dir_buf + pos - extra_offset", yet the ext4_check_dir_entry() length argument uses the larger extra_size. A position whose dirent header would extend past extra_size is therefore accepted, and the rescan loop's rec_len probe and ext4_check_dir_entry() dereference de->rec_len before the entry is rejected. Reject a position whose minimum-size dirent header would not fit within extra_size before forming de, in both the rescan and main loops, and pass inline_size rather than extra_size to ext4_check_dir_entry() so the length check matches the physical buffer.

### 57. CVE-2026-89783｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T09:17:08.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.0021 / percentile=0.11445
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T09:17:08.930 / 2026-09-16T15:18:08.720
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: xfrm6: fix out-of-bounds write in xfrm6_input_addr() when secpath is full The depth check in xfrm6_input_addr() is off by one: if (1 + sp->len == XFRM_MAX_DEPTH) goto drop; ... sp->xvec[sp->len++] = x; xfrm_input() can leave sp->len == XFRM_MAX_DEPTH, and the transport-mode receive path re-enters IPv6 input via xfrm_trans_reinject() with that secpath preserved. If the inner packet carries a destination-options HAO option or a type-2 routing header, xfrm6_input_addr() is called with sp->len == XFRM_MAX_DEPTH; the check (1 + 6 == 6) is false, so sp->xvec[sp->len++] writes one slot past the 6-element xvec[]. The write stays within the sec_path allocation (invisible to KASAN); UBSAN_BOUNDS flags it and panics under panic_on_warn. Use "sp->len >= XFRM_MAX_DEPTH", matching xfrm_input(). This also restores one chain level the old check rejected at sp->len == 5. UBSAN: array-index-out-of-bounds in net/ipv6/xfrm6_input.c:309:10 index 6 is out of range for type 'xfrm_state *[6]'

### 58. CVE-2026-89779｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T09:17:08.387)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00205 / percentile=0.10806
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T09:17:08.387 / 2026-09-16T15:18:07.320
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: fs/ntfs3: validate ef->size covers the record's name and value When an EA record has a non-zero ef->size, ntfs_read_ea() only checks that the record fits in the remaining buffer (ea_size > bytes), not that ef->size is large enough to hold the record's own name_len + 1 + elength. A crafted image can pass validation with, e.g., ef->size = 24 but elength = 0xffff. ntfs_get_ea() then trusts elength and copies it out of the undersized record, reading past the kmalloc(info->size) allocation and leaking heap memory to userspace via getxattr(): BUG: KASAN: slab-out-of-bounds in ntfs_get_ea (fs/ntfs3/xattr.c:302) Read of size 65535 at addr ffff888100794550 by task exploit __asan_memcpy (mm/kasan/shadow.c:105) ntfs_get_ea (fs/ntfs3/xattr.c:302) ntfs_getxattr (fs/ntfs3/xattr.c:848) __vfs_getxattr (fs/xattr.c:441) vfs_getxattr (fs/xattr.c:474) do_getxattr (fs/xattr.c:800) path_getxattrat (fs/xattr.c:868) do_syscall_64 (arch/x86/entry/syscall_64.c:94) The buggy address is located 80 bytes inside of allocated 84-byte region in cache kmalloc-96 Compute the size the record needs and require ef->size to cover it.

### 59. CVE-2026-89778｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T09:17:08.253)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00205 / percentile=0.10807
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T09:17:08.253 / 2026-09-16T15:18:07.167
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: isofs: fix out-of-bounds page array access on empty zisofs block zisofs_uncompress_block()'s empty-block fast path returns pcount << PAGE_SHIFT, ignoring the incoming poffset, unlike the decompression path which returns bytes produced relative to poffset. zisofs_fill_pages() uses that return to advance its page cursor, so when the zisofs block size is below PAGE_SIZE and a sub-page block leaves poffset partway into a page, a following empty block over-counts and advances pages[] one element past its end, after which "if (poffset && *pages)" reads pages[1] out of bounds. rock.c only rejects a block-size shift > 17, so a crafted "ZF" Rock Ridge record can set it below PAGE_SHIFT; the bug is reached by an ordinary read() of a compressed file on such a mounted ISO9660 image. Return the byte count relative to poffset and zero only [poffset, PAGE_SIZE) of the first page, matching the decompression path. The page-aligned case (poffset == 0) is unaffected. BUG: KASAN: slab-out-of-bounds in zisofs_read_folio (fs/isofs/compress.c:290) Read of size 8 at addr ffff88800f5eac48 by task exploit/142 zisofs_read_folio (fs/isofs/compress.c:290) read_pages (mm/readahead.c:184) ... filemap_read (mm/filemap.c:2814) vfs_read (fs/read_write.c:574) __x64_sys_pread64 (fs/read_write.c:769) do_syscall_64 (arch/x86/entry/syscall_64.c:94) entry_SYSCALL_64_after_hwframe (arch/x86/entry/entry_64.S:121) The buggy address is located 0 bytes to the right of the allocated 8-byte region in the kmalloc-8 cache

### 60. CVE-2026-89775｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T09:17:07.850)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.00184 / percentile=0.08235
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T09:17:07.850 / 2026-09-16T18:17:19.027
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: KVM: arm64: Handle negative S1 walk levels in VNCR TLB size evaluation Computing the effects of a TLB invalidation involves looking at the size of the mapping cached by the TLB. For S1 mappings such as VNCR, this is deducted from the combination of the base granule size and the mapping level. However, this implies that the S1 MMU is *on*. When the MMU is off, we indicate this with the level being set to a "creative" value of -127 (S1_MMU_DISABLED). This ends-up being misinterpreted by pgshift_level_to_ttl() as it doesn't handle negative levels at all (the level is immediately cast to a u8 and only the bottom two bits considered), leading to an invalidation size of 0. Not helpful. Tidy-up pgshift_level_to_ttl() to handle these negative levels, and ttl_to_size() to always return SZ_1G when no valid TTL is present. This allows the removal of open-coded checks for similar situations. Note that the check for a negative value not explicitely checking for S1_MMU_DISABLED is deliberate, so that actual negative levels introduced with LVA2 and D128 can take the same path if we ever support them.

### 61. CVE-2026-89083｜HP Inc / HP AC Print & Scan
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:38.703)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:38.703 / 2026-09-16T20:17:38.703
- **官方描述（原文）**：HP has identified potential security vulnerabilities in the HP Advance software that may enable elevation of privilege, remote code execution, or arbitrary file write under certain conditions, impacting the HP Advance server hosting the software.

### 62. CVE-2026-89082｜HP Inc / HP AC Print & Scan
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:38.573)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:38.573 / 2026-09-16T20:17:38.573
- **官方描述（原文）**：HP has identified potential security vulnerabilities in the HP Advance software that may enable elevation of privilege, remote code execution, or arbitrary file write under certain conditions, impacting the HP Advance server hosting the software.

### 63. CVE-2026-87796｜sh1zen / Multi Uploader for Gravity Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-17T05:17:02.123)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-17T05:17:02.123 / 2026-09-17T05:17:02.123
- **官方描述（原文）**：The Multi Uploader for Gravity Forms plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 1.1.9 via the move_file function. This is due to insufficient file type validation during chunked upload handling. This makes it possible for unauthenticated attackers to upload arbitrary files on the affected site's server which may make remote code execution possible.

### 64. CVE-2026-81642｜NLnet Labs / Unbound
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T09:17:06.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00521 / percentile=0.42976
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T09:17:06.320 / 2026-09-16T19:41:10.423
- **官方描述（原文）**：In NLnet Labs Unbound up to and including 1.26.0, a vulnerability was found in the DNSSEC validator that enables denial of service and possible remote code execution as a result of digesting DNSKEYs. A DNSKEY with an owner compression pointer to its own RDATA can overflow the digest buffer. Remote code execution is possible through attacker controlled data. An adversary can exploit the vulnerability by controlling a malicious zone and querying a vulnerable Unbound.

### 65. CVE-2026-77411｜rabbitmq / amqp091-go
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:17:50.563)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:17:50.563 / 2026-09-16T19:17:39.233
- **官方描述（原文）**：RabbitMQ amqp091-go is a Go AMQP 0.9.1 client. Prior to 1.13.0, readLongstr in read.go returns an empty string and a nil error when a declared AMQP longstr length exceeds 0x7FFFFFFF instead of returning ErrSyntax. The function leaves the declared field bytes unread, while readTable treats the operation as successful and continues parsing from the wrong offset. A malicious or compromised broker can provide an oversized longstr in a table field and desynchronize subsequent AMQP parsing, causing attacker-controlled trailing bytes to be interpreted as later fields or frames and disrupting connection integrity and availability. This issue is fixed in version 1.13.0.

### 66. CVE-2026-77408｜rabbitmq / amqp091-go
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:17:49.747)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:17:49.747 / 2026-09-16T15:17:49.747
- **官方描述（原文）**：RabbitMQ amqp091-go is a Go AMQP 0.9.1 client. Prior to 1.13.0, the writeShortstr function in write.go casts the byte length of AMQP shortstr property values to uint8 without first rejecting values longer than 255 bytes. An application that accepts an oversized CorrelationId, ReplyTo, MessageId, Expiration, UserId, AppId, ContentType, ContentEncoding, or Type value can therefore serialize a wrapped length and only a truncated prefix, while reporting no error. The resulting silent metadata corruption can break request and reply correlation, routing, tracing, and downstream message processing. This issue is fixed in version 1.13.0.

### 67. CVE-2026-77405｜rabbitmq / amqp091-go
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:17:47.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:17:47.980 / 2026-09-16T15:17:47.980
- **官方描述（原文）**：RabbitMQ amqp091-go is a Go AMQP 0.9.1 client. Prior to 1.13.0, tlsConfigFromURI in uri.go creates tls.Config values without setting MinVersion to tls.VersionTLS12. Builds using a Go runtime whose default permits TLS 1.0 or TLS 1.1 can therefore negotiate an obsolete protocol version when connecting through an amqps URI. A network attacker able to influence TLS negotiation with such a legacy build may weaken transport protection for AMQP messages and credentials. This issue is fixed in version 1.13.0.

### 68. CVE-2026-76423｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:28.717)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:28.717 / 2026-09-17T04:18:01.213
- **官方描述（原文）**：A vulnerability in the REST API of Cisco ISE and Cisco ISE-PIC could allow an unauthenticated, remote attacker to gain administrative access to an affected device. This vulnerability is due to the REST API web service being exposed with insufficient authorization checks. An attacker could exploit this vulnerability by sending a crafted HTTP request to the exposed REST API port. A successful exploit could allow the attacker to read and modify ISE configuration and identity data with administrative privileges.

### 69. CVE-2026-76420｜Cisco / Cisco Secure Firewall Management Center (FMC)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:18:09.330)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:18:09.330 / 2026-09-17T04:18:01.007
- **官方描述（原文）**：A vulnerability in the internal configuration of the Apache JServ Protocol (AJP)&nbsp;connector for Cisco Secure FMC Software could allow an unauthenticated, remote attacker to impersonate a peer device. This vulnerability is due to incorrect initialization of encryption parameters for the AJP connector at boot time. An attacker could exploit this vulnerability by sending crafted packets to the AJP connector. A&nbsp;successful exploit could allow the attacker to execute commands as root and&nbsp;gain full control over the FMC REST APIs on the affected device. Note: This vulnerability can be exploited only if the valid sftunnel connection between Cisco Secure FMC Software and Cisco Secure FTD Software is down.

### 70. CVE-2026-75513｜JasperFx / marten
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T21:17:13.440)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T21:17:13.440 / 2026-09-16T21:17:13.563
- **官方描述（原文）**：Marten is a .NET Transactional Document DB and Event Store on PostgreSQL. From version 7.0.0 until 9.13.0, several Marten LINQ and tenant-management paths interpolate runtime, potentially attacker-controlled strings into single-quoted SQL literals without escaping or parameterization. The primary confirmed vector is a dictionary indexer key used by Where filters in src/Marten/Linq/Members/Dictionaries/DictionaryItemMember.cs. Additional affected sinks include SelectParser.cs, DatabaseScopedTenantPartitions.cs, and DeleteAllForTenant.cs reached through IEventStore.DeleteProjectionProgressAsync, while DictionaryContainsKeyFilter.cs (Newtonsoft serializer only; System.Text.Json is not affected) handles ContainsKey calls. Events/Daemon/Internals/EventLoader.cs contains a related per-tenant partition-pruning literal that the advisory identifies as a defense-in-depth sink. A crafted single quote can escape the generated literal, enabling filter or multi-tenant authorization bypass and blind data exfiltration, and deployments that permit semicolon-batched Npgsql statements may also allow data modification. This issue is fixed in version 9.13.0.

### 71. CVE-2026-73461｜Arista Networks / EOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T09:17:05.147)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00298 / percentile=0.22515
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T09:17:05.147 / 2026-09-17T04:18:00.483
- **官方描述（原文）**：On affected EOS platforms with AAA-based gRPC authorization enabled for OpenConfig, gRPC requests of an authenticated user to OpenConfig may use the wrong privilege level, resulting in an authorization using the wrong AAA method list. This does not impact non-gRPC OpenConfig requests such as NETCONF.

### 72. CVE-2026-73456｜Arista Networks / EOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T19:17:32.270)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T19:17:32.270 / 2026-09-17T04:18:00.263
- **官方描述（原文）**：Under certain circumstances on affected platforms running Arista EOS with gRPC Network Packet Sampling Interface (gNPSI) enabled, an unauthenticated gNPSI client can craft a malicious request to allow arbitrary code execution, granting an attacker full administrative control over the compromised switch.

### 73. CVE-2026-73453｜Arista Networks / EOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T10:16:52.043)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.00746 / percentile=0.53063
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T10:16:52.043 / 2026-09-17T04:17:59.823
- **官方描述（原文）**：An unauthenticated P4Runtime (Programming Protocol-Independent Packet Processors Runtime) client can achieve arbitrary code execution under certain conditions on affected platforms running Arista EOS configured with P4Runtime. P4Runtime is disabled by default in Arista EOS. By crafting a malicious packet during the initiation of a P4Runtime session, an attacker can obtain complete administrative control over the compromised switch. This issue was discovered internally by Arista, and the company is not aware of any malicious exploitation of this vulnerability in customer networks.

### 74. CVE-2026-73447｜Arista Networks / EOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T07:16:37.087)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00756 / percentile=0.53407
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T07:16:37.087 / 2026-09-17T04:17:59.623
- **官方描述（原文）**：A privileged attacker can exploit certain operation to execute arbitrary commands with root privileges, leading to full device compromise. An authenticated user can exploit gRPC Network Security Interface (gNSI) Certz service on Arista EOS-based products to escalate privileges and execute arbitrary OS commands via a crafted Certz Rotate request. The Bootz service is also affected.

### 75. CVE-2026-73172｜Advantech / EKI-1242IEIMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T13:18:05.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T13:18:05.600 / 2026-09-16T19:41:10.423
- **官方描述（原文）**：Nozomi Networks Labs identified a CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in the edgserver management service of Advantech EKI-1242EIMS in firmware version V1.06.01 that allows a remote unauthenticated attacker to execute arbitrary OS commands as root via crafted requests to TCP port 5058.

### 76. CVE-2026-70416｜Dell / ObjectScale
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T16:17:14.953)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T16:17:14.953 / 2026-09-16T20:37:16.870
- **官方描述（原文）**：Dell ObjectScale, versions prior to 4.4.0.0, contains a Deserialization of Untrusted Data vulnerability. An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to Remote execution.

### 77. CVE-2026-61594｜djust-org / djust
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T22:17:03.047)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T22:17:03.047 / 2026-09-16T22:17:03.047
- **官方描述（原文）**：djust provides Phoenix LiveView-style reactive server-side rendering for Django with Rust-powered performance. Prior to version 1.0.7, the live (WebSocket) transport authorizes a mount via `check_view_auth`, not Django's `View.dispatch()` chain. As a result, standard Django authorization — `LoginRequiredMixin`, `PermissionRequiredMixin`, `UserPassesTestMixin`, `@method_decorator(login_required, name="dispatch")`, and custom `dispatch()` guards — and the djust admin extension's staff gate (applied only in the HTTP `as_view` wrapper) were enforced on the initial HTTP GET but silently bypassed over WebSocket, where all events and state flow. An anonymous or under-privileged client could open a WebSocket and mount such a view — including admin list/create/change/delete — and dispatch its handlers. This is fixed in djust 1.0.7. `check_view_auth` now honors the Django `AccessMixin` family on every transport; a new system check S004 fails loud at startup on auth patterns the runtime cannot safely replay (decorator/overridden-`dispatch` forms); and the admin base mixin declares `login_required = True` + an active-staff `check_permissions` gate. As a workaround, gate views using djust's `login_required` / `permission_required` / `check_permissions` attributes (honored on all transports) rather than HTTP-only mixins/decorators.

### 78. CVE-2026-58147｜WNC / T-Mobile 5G Box IDU
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T12:17:05.103)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T12:17:05.103 / 2026-09-16T19:14:25.980
- **官方描述（原文）**：WNC T-Mobile 5G Box IDU router contains an OS command injection vulnerability in the portal.cgi component's password change functionality. The application improperly neutralizes special elements in the http_passwd_hidden and http_passwdConfirm_hidden parameters, allowing an authenticated attacker to execute arbitrary commands on the underlying operating system with root privileges.This issue has been fixed in firmware version 1.1.0.651412

### 79. CVE-2026-58146｜WNC / T-Mobile 5G Box IDU
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T12:17:04.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T12:17:04.980 / 2026-09-16T19:14:25.980
- **官方描述（原文）**：WNC T-Mobile 5G Box IDU router is vulnerable to OS command injection vulnerability. The vulnerability exists within the /cgi-bin/portal.cgi endpoint, specifically through the cli_cookie POST parameter. The cli_cookie parameter value is directly concatenated into a find command string without proper sanitization. This allows a remote, unauthenticated attacker to inject and execute arbitrary shell commands as root on the underlying operating system. This issue has been fixed in firmware version 1.1.0.651412

### 80. CVE-2026-40855｜WNC / T-Mobile 5G Box IDU
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T12:17:03.673)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T12:17:03.673 / 2026-09-16T19:14:25.980
- **官方描述（原文）**：WNC T-Mobile 5G Box IDU router is vulnerable to a command injection. The vulnerability exists in the ping functionality within the /cgi-bin/portal.cgi endpoint, specifically affecting the ping_ip, ping_size, and ping_times POST parameters. The root cause is the failure to verify and sanitize user-supplied input before incorporating it into a system command. This allows an authenticated attacker to execute arbitrary commands on the shell and gain root access to the system.This issue has been fixed in firmware version 1.1.0.651412

### 81. CVE-2026-27565｜Pepperl+Fuchs / ICE2-8IOL1-G65L-V1D
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T08:16:39.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00941 / percentile=0.59232
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T08:16:39.740 / 2026-09-16T19:17:14.183
- **官方描述（原文）**：An unauthenticated remote attacker can upload a malicious IODD file that places and executes a shell script with root privileges. The shell script remains active even after a reboot.

### 82. CVE-2026-27546｜Pepperl+Fuchs / ICE2-8IOL1-G65L-V1D
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T08:16:36.850)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00953 / percentile=0.59597
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T08:16:36.850 / 2026-09-16T19:17:10.840
- **官方描述（原文）**：An unauthenticated remote attacker can exploit an authentication bypass in the _account_log function to log in as an admin, even when accounts are properly configured.

### 83. CVE-2026-20341｜Cisco / Cisco Secure Firewall Management Center (FMC)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:24.193)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:24.193 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：A vulnerability in the sftunnel inter-device communication protocol of Cisco Secure FMC Software could allow an authenticated, remote attacker to obtain&nbsp;root privileges. This vulnerability is due to unsecured deserialization of untrusted data over the sftunnel management connection. An attacker could exploit this vulnerability by sending crafted sftunnel remote procedure calls (RPCs). A successful exploit could allow the attacker to gain root privileges on a device that is running Cisco Secure FMC Software and its high-availability peer. To exploit this vulnerability, the attacker must have valid administrative credentials on a managed Cisco FTD device.

### 84. CVE-2026-20332｜Cisco / Cisco Secure Firewall Adaptive Security Appliance (ASA) Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T21:17:10.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T21:17:10.480 / 2026-09-17T04:17:44.230
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appliance Software, Cisco Secure Firewall Threat Defense Software and Cisco Secure Firewall Management Center Software engineering team has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. &nbsp; The vulnerabilities tracked by CVE-2026-20332 are related to improper access control issues that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-284.

### 85. CVE-2026-20331｜Cisco / Cisco Secure Firewall Adaptive Security Appliance (ASA) Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:17:17.107)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:17:17.107 / 2026-09-17T04:17:41.327
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appliance Software, Cisco Secure Firewall Threat Defense Software and Cisco Secure Firewall Management Center Software engineering team has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. &nbsp; The vulnerabilities tracked by CVE-2026-20331 are related to the failure of protection mechanisms issues that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-693.

### 86. CVE-2026-20330｜Cisco / Cisco Secure Firewall Adaptive Security Appliance (ASA) Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:23.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:23.810 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appliance Software, Cisco Secure Firewall Threat Defense Software and Cisco Secure Firewall Management Center Software engineering team has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. &nbsp; The vulnerabilities tracked by CVE-2026-20330 are related to improper neutralization issues that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-707.

### 87. CVE-2026-20329｜Cisco / Cisco Secure Firewall Adaptive Security Appliance (ASA) Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:23.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:23.600 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Adaptive Security Appliance Software, Cisco Secure Firewall Threat Defense Software and Cisco Secure Firewall Management Center Software engineering team has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. &nbsp; The vulnerabilities tracked by CVE-2026-20329 are related to issues concerning improper handling of exceptional conditions that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-703.

### 88. CVE-2026-20326｜Cisco / Cisco Nexus Dashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:23.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:23.480 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Nexus Dashboard engineering team has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-20326 are related to missing authentication for critical function issues that are grouped under the Common Weakness Enumeration (CWE) CWE-306.

### 89. CVE-2026-20325｜Cisco / Cisco Nexus Dashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:23.347)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:23.347 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Nexus Dashboard&nbsp;engineering team has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-20325 are related to improper neutralization of special elements used in a command issue that are grouped under the Common Weakness Enumeration (CWE) CWE-77.

### 90. CVE-2026-20324｜Cisco / Cisco Secure Firewall Management Center (FMC)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:23.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:23.180 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：A vulnerability in the sftunnel inter-device communication protocol of Cisco Secure Firewall Management Center (FMC) Software could allow an authenticated, remote attacker to execute arbitrary commands as root. This vulnerability exists because a registered sftunnel peer has incorrect permissions to write an arbitrary file to any location on the device. An attacker could exploit this vulnerability by hijacking the sftunnel communication connection or being a valid registered sftunnel peer and sending an sftunnel command to write a malicious file to the disk of an affected device. A successful exploit could allow the attacker to write a file to the device that is executed with root privileges. To exploit this vulnerability, the attacker must have valid user credentials on the affected device.

### 91. CVE-2026-20322｜Cisco / Cisco Nexus Dashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:23.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:23.040 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Nexus Dashboard&nbsp;engineering team has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-20322 are related to improper access control issues that are grouped under the Common Weakness Enumeration (CWE) CWE-284.

### 92. CVE-2026-20307｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:17:16.973)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:17:16.973 / 2026-09-17T04:17:40.957
- **官方描述（原文）**：A vulnerability in the web-based management interface of Cisco ISE could allow an authenticated, remote attacker to execute arbitrary commands on the underlying operating system of an affected device. To exploit this vulnerability, the attacker must have at least low-privileged administrative credentials. This vulnerability is due to insecure deserialization of a user-supplied Java byte stream. An attacker could exploit this vulnerability by sending a crafted serialized Java object to the web-based management interface of an affected device. A successful exploit could allow the attacker to execute arbitrary code on the device and elevate privileges to root. In single-node deployments, successful exploitation of this vulnerability could cause the affected ISE node to become unavailable, resulting in a denial of service (DoS) condition. In that condition, endpoints that have not already authenticated would be unable to access the network until the node is restored.

### 93. CVE-2026-20306｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:17:16.857)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:17:16.857 / 2026-09-17T04:17:40.777
- **官方描述（原文）**：A vulnerability in the REST API of Cisco ISE and ISE-PIC could allow an authenticated, remote attacker to perform command injection attacks on the underlying operating system and elevate privileges to root. To exploit this vulnerability, the attacker must have valid administrative credentials. This vulnerability is due to improper validation of user-supplied input. An attacker could exploit this vulnerability by sending crafted commands to the web-based management interface of an affected device. A successful exploit could allow the attacker to execute arbitrary code on the device and elevate privileges to root. In single-node deployments, successful exploitation of this vulnerability could cause the affected ISE node to become unavailable, resulting in a DoS condition. In that condition, endpoints that have not already authenticated would be unable to access the network until the node is restored.

### 94. CVE-2026-20305｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:17:16.707)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:17:16.707 / 2026-09-17T04:17:40.540
- **官方描述（原文）**：A vulnerability in the diagnostic tools of Cisco ISE and ISE-PIC could allow an authenticated, remote attacker to perform command injection attacks on the underlying operating system and elevate privileges to&nbsp;root. To exploit this vulnerability, the attacker must have valid administrative credentials. This vulnerability is due to improper validation of user-supplied input. An attacker could exploit this vulnerability by sending crafted commands to the web-based management interface of an affected device. A successful exploit could allow the attacker to execute arbitrary code on the device and elevate privileges to root. In single-node deployments, successful exploitation of this vulnerability could cause the affected ISE node to become unavailable, resulting in a denial of service (DoS) condition. In that condition, endpoints that have not already authenticated would be unable to access the network until the node is restored.

### 95. CVE-2026-20242｜Cisco / Cisco Secure Firewall Management Center (FMC)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:22.697)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:22.697 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：A vulnerability in the External Database Access feature of Cisco Secure Firewall Management Center (FMC) Software could allow an unauthenticated, remote attacker to execute arbitrary commands as&nbsp;root on an affected device. This vulnerability is due to insecure deserialization of a user-supplied Java byte stream from a host that is configured in the external database access list. An attacker could exploit this vulnerability by sending a crafted, serialized Java byte stream to a specific TCP port of an affected device. A successful exploit could allow the attacker to execute arbitrary commands on the device and elevate privileges to root. Notes: This vulnerability can be exploited only by an attacker who has control of a host in the external database access list. If the FMC management interface does not have public internet access, the attack surface that is associated with this vulnerability is reduced.

### 96. CVE-2026-20237｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:22.407)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:22.407 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC), engineering teams have conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-20237 are related to improper input validation issues that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-20.

### 97. CVE-2026-20234｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:17:16.537)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:17:16.537 / 2026-09-17T04:17:37.290
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) engineering teams have conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-20234 are related to insufficiently protected credentials issues that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-522.

### 98. CVE-2026-20211｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:22.200)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:22.200 / 2026-09-17T04:17:36.827
- **官方描述（原文）**：A vulnerability in Cisco ISE could allow an authenticated, remote attacker to execute arbitrary commands on the underlying operating system of an affected device. To exploit this vulnerability, the attacker must have valid high-privileged administrative credentials. This vulnerability is due to insecure deserialization of Java objects by the affected software. An attacker could exploit this vulnerability by sending a crafted serialized Java object to an affected device. A successful exploit could allow the attacker to obtain user-level access to the underlying operating system and then elevate privileges to&nbsp;root. In single-node deployments, successful exploitation of this vulnerability could cause the affected ISE node to become unavailable, resulting in a DoS condition. In that condition, endpoints that have not already authenticated would be unable to access the network until the node is restored.

### 99. CVE-2026-20194｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:22.047)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:22.047 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC), engineering teams have conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-20194 are related to incorrect resource transfer between spheres that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-669.

### 100. CVE-2026-20192｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:21.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:21.900 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) engineering teams have conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-20192 are related to improper access control issues that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-284.

### 101. CVE-2026-20176｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:21.747)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:21.747 / 2026-09-17T04:17:36.643
- **官方描述（原文）**：A vulnerability in Cisco ISE could allow an authenticated, remote attacker to execute arbitrary commands on the underlying operating system of an affected device. To exploit this vulnerability, the attacker must have valid high-privileged administrative credentials. This vulnerability is due to insufficient validation of user-supplied input. An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected device. A successful exploit could allow the attacker to obtain system-level access to the underlying operating system and then elevate privileges to root. In single-node deployments, successful exploitation of this vulnerability could cause the affected ISE node to become unavailable, resulting in a DoS condition. In that condition, endpoints that have not already authenticated would be unable to access the network until the node is restored.

### 102. CVE-2026-20130｜Cisco / Cisco Identity Services Engine Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T20:17:21.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T20:17:21.607 / 2026-09-16T20:35:23.620
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC), engineering teams have conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-20130 are related to improper neutralization of special elements issues that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-74.

### 103. CVE-2025-59953｜InternLM / lmdeploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T16:17:03.010)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T16:17:03.010 / 2026-09-16T16:17:03.010
- **官方描述（原文）**：LMDeploy is a toolkit for compressing, deploying, and serving large language models. Starting in version 0.9.1 and prior to version 0.10.2, the LMdeploy implements an rpc server (AsyncRPCServer in zmq_rpc.py) for supporting the RPC communications. In its core functionality call_and_response(), I found it will directly use the pickles.loads() to deserialize the received messages without any sanitization, hence resulting in a remote code execution vulnerability by this RPC server. Version 0.10.2 contains a patch.

### 104. CVE-2026-92568｜mlrun / mlrun
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:19:02.453)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:19:02.453 / 2026-09-16T16:17:23.393
- **官方描述（原文）**：MLRun through 1.11.0 contains a server-side request forgery vulnerability in the WebhookNotification handler that allows authenticated users to make the API server send arbitrary HTTP requests to internal addresses. Attackers can update a run with a malicious webhook notification that executes when the run reaches a terminal state, enabling requests to internal services, Kubernetes APIs, or cloud metadata endpoints from within the cluster.

### 105. CVE-2026-92461｜guchengwuyue / yshop-crm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T12:17:07.623)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T12:17:07.623 / 2026-09-16T19:47:01.197
- **官方描述（原文）**：yshop-crm through 2.1.3 contains a missing authorization vulnerability in the GET /admin-api/crm/flow/flow-users endpoint that allows any logged-in back-office user to access approval workflow data. Attackers can retrieve approval chain topology, step ordering, approver identifiers, and personal information including login names, nicknames, departments, email addresses, mobile numbers and last login IP addresses.

### 106. CVE-2026-92406｜SourceCodester / Inventory and Monitoring System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T18:17:20.233)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T18:17:20.233 / 2026-09-16T19:05:56.360
- **官方描述（原文）**：A vulnerability was detected in SourceCodester Inventory and Monitoring System 1.0. The impacted element is an unknown function of the file /admins/assessments/databank/btn_functions.php?action=add. Performing a manipulation of the argument difficulty_id results in sql injection. Remote exploitation of the attack is possible. The exploit is now public and may be used.

### 107. CVE-2026-92405｜SourceCodester / Inventory and Monitoring System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:18:20.127)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:18:20.127 / 2026-09-16T20:17:48.217
- **官方描述（原文）**：A security vulnerability has been detected in SourceCodester Inventory and Monitoring System 1.0. The affected element is an unknown function of the file /index.php. Such manipulation of the argument Username leads to sql injection. The attack may be launched remotely. The exploit has been disclosed publicly and may be used.

### 108. CVE-2026-92380｜未確認 / WuzhiCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:19:01.317)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:19:01.317 / 2026-09-16T17:53:40.500
- **官方描述（原文）**：A flaw has been found in WuzhiCMS up to 4.1.0. The impacted element is the function ckditor::saveRemote of the file coreframe/app/attachment/index.php of the component Remote Image Fetch. This manipulation of the argument source[] causes server-side request forgery. The attack can be initiated remotely. The exploit has been published and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 109. CVE-2026-92366｜code-projects / Matrimonial System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:19:01.130)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:19:01.130 / 2026-09-16T20:17:47.940
- **官方描述（原文）**：A vulnerability was determined in code-projects Matrimonial System 1.0. This affects an unknown part of the file /search.php of the component Regular Search. This manipulation of the argument sex/mothertongue/maritialstatus/country/state/religion/agemin/agemax causes sql injection. The attack can be initiated remotely. The exploit has been publicly disclosed and may be utilized.

### 110. CVE-2026-92091｜Red Hat / Red Hat Ansible Automation Platform 2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T08:16:40.583)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：0.00496 / percentile=0.41371
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T08:16:40.583 / 2026-09-16T19:42:43.623
- **官方描述（原文）**：A flaw was found in jwcrypto. The JWK.import_key() function validates the key_ops JWK member for duplicate values using an algorithm with O(n^2) time complexity, and the length of key_ops is not bounded. A remote, unauthenticated attacker can supply a JWK with a large key_ops array to an application that passes attacker-controlled key material to a public key-import API (reachable via ECDH-ES key agreement, OIDC dynamic client registration, DPoP, or ACME account key registration, among others) to consume excessive CPU time, resulting in a denial of service.

### 111. CVE-2026-86475｜Unknown / Appointment Hour Booking
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T07:16:37.780)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00255 / percentile=0.17245
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T07:16:37.780 / 2026-09-16T20:25:29.240
- **官方描述（原文）**：The Appointment Hour Booking WordPress plugin before 1.5.95 does not check every appointment in a booking submission against the capacity configured for its own slot, allowing unauthenticated visitors to take slots that are already fully booked.

### 112. CVE-2026-85732｜oras-project / oras-go
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T17:18:16.000)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.7 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T17:18:16.000 / 2026-09-16T18:17:18.070
- **官方描述（原文）**：oras-go is a Go library for managing OCI artifacts. Prior to 2.6.2, the parseLink function in registry/remote/utils.go accepts an absolute URL from a registry-controlled Link response header without validating its scheme, host, or port. Tags, Referrers, and Repositories pagination operations then issue a GET request to the attacker-selected URL from the victim's network, allowing blind server-side request forgery against internal services. The response body is not returned to the attacker, but timing and error differences can reveal service reachability, and credentials may be attached when the credential store has an entry for the target host. Exploitation requires a victim to perform a pagination-based listing operation against a malicious registry. The maintainer identifies this report as a duplicate of GHSA-3hr5-mjrr-hfjh and states that remediation is consolidated in that earlier advisory. The consolidated issue is fixed in version 2.6.2.

### 113. CVE-2026-84906｜Unknown / Eventin
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T07:16:37.677)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00144 / percentile=0.04053
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T07:16:37.677 / 2026-09-16T20:25:29.240
- **官方描述（原文）**：The Eventin WordPress plugin before 4.1.24 does not verify that a completed payment corresponds to the order it is applied to, confirming only that the payment gateway reports the transaction as successful, not its amount, currency, or which order it belongs to, allowing unauthenticated visitors to mark unpaid orders of any value as paid by replaying the transaction of a single genuine low-value payment.

### 114. CVE-2026-77360｜middleapi / orpc
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T19:17:38.020)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T19:17:38.020 / 2026-09-16T20:17:31.877
- **官方描述（原文）**：oRPC is an tool that helps build APIs that are end-to-end type-safe and adhere to OpenAPI standards. Prior to 1.14.8, the @orpc/server CORS plugin in packages/server/src/plugins/cors.ts copies a client's incoming Vary request header into the response instead of controlling Vary as a response-only header and using Origin for request-origin variation. In deployments behind a shared cache, CDN, or reverse proxy that keys responses using Vary, a client can inject arbitrary variation values, pollute cache keys, and cause inconsistent CORS enforcement for other clients. Default non-cached configurations have no established direct confidentiality, integrity, or availability impact. This issue is fixed in version 1.14.8.

### 115. CVE-2026-69147｜vllm-project / vllm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T18:17:11.770)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T18:17:11.770 / 2026-09-16T19:17:26.113
- **官方描述（原文）**：vLLM is an inference and serving engine for large language models. Prior to 0.28.0, request bodies for Chat Completions and Responses can set media_io_kwargs.video.video_backend to pynvvideocodec, and MediaConnector.fetch_video forwards that choice to VideoMediaIO even when startup configuration selected a software decoder. The engine's _reserve_mm_ipc_gpu_memory logic budgets decoder memory only from static configuration, so the request-selected VIDEO_LOADER_REGISTRY backend can create a CUDA context, decoder surfaces, and decoded-frame allocations that were not removed from the engine's KV-cache budget. An attacker able to submit video requests to a video-capable GPU deployment with PyNvVideoCodec installed can exhaust shared GPU memory, causing request failures, worker crashes, or denial of service. The first release containing the fix is version 0.28.0.

### 116. CVE-2026-19857｜Unknown / Formidable Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T07:16:36.720)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.8 (MEDIUM)
- **EPSS**：0.00188 / percentile=0.08687
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T07:16:36.720 / 2026-09-16T20:25:29.240
- **官方描述（原文）**：The Formidable Forms WordPress plugin before 6.35 does not prevent a request-derived value from reaching the WordPress shortcode parser when it substitutes a supported token into a form's custom HTML, allowing unauthenticated visitors to have arbitrary shortcodes, with attacker-chosen attributes, executed server-side on any page displaying an affected form.

### 117. CVE-2026-13407｜Unknown / Royal Addons for Elementor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T07:16:32.690)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：0.00217 / percentile=0.12292
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T07:16:32.690 / 2026-09-16T20:25:29.240
- **官方描述（原文）**：The Royal Elementor Addons WordPress plugin before 1.7.1067 does not properly sanitize and escape values submitted through its form widget before including them in the body of administrator notification emails, allowing unauthenticated attackers to inject arbitrary HTML into emails sent to the site administrator on form submission.

### 118. CVE-2026-92472｜未確認 / GPAC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T19:18:06.377)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T19:18:06.377 / 2026-09-16T20:17:48.483
- **官方描述（原文）**：A vulnerability was determined in GPAC 26.08-DEV. The affected element is the function gf_node_deactivate_ex of the file src/scenegraph/base_scenegraph.c of the component MP4Box. Executing a manipulation can lead to use after free. The attack needs to be launched locally. The exploit has been publicly disclosed and may be utilized. Upgrading to version abi-16.24 is sufficient to fix this issue. This patch is called e34f4ba349d55cd1849f0bcf4cf46552732e2db7. The affected component should be upgraded. This issue is distinct from CVE-2026-90827.

### 119. CVE-2026-92418｜ChangeWeDer / crm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T19:18:06.170)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T19:18:06.170 / 2026-09-16T20:17:48.350
- **官方描述（原文）**：A vulnerability was determined in ChangeWeDer crm up to c07bd4c97141521af6475034bc58523beed51bbd. This vulnerability affects unknown code of the file src/main/resources/public/js/customerServe/customer.serve.js of the component Save Endpoint. This manipulation of the argument customerName causes cross site scripting. Remote exploitation of the attack is possible. The exploit has been publicly disclosed and may be utilized. This product follows a rolling release approach for continuous delivery, so version details for affected or updated releases are not provided. The project was informed of the problem early through an issue report but has not responded yet.

### 120. CVE-2026-92383｜未確認 / PbootCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T15:19:01.673)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T15:19:01.673 / 2026-09-16T17:53:40.500
- **官方描述（原文）**：A security vulnerability has been detected in PbootCMS up to 3.2.24. This vulnerability affects the function UserController::del/UserController::mod of the file apps/admin/controller/system/UserController.php of the component User Management. Such manipulation leads to cross-site request forgery. The attack may be performed from remote. The exploit has been disclosed publicly and may be used. Upgrading to version 3.2.25 is able to resolve this issue. The name of the patch is c25241a0964742cefb7f698efbb6c38b868d6ff7. It is advisable to upgrade the affected component.

### 121. CVE-2026-92364｜itsourcecode / Leave Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T14:17:16.727)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T14:17:16.727 / 2026-09-16T17:53:40.500
- **官方描述（原文）**：A vulnerability has been found in itsourcecode Leave Management System 1.0. Affected by this vulnerability is an unknown functionality of the file /module/employee/index.php. The manipulation of the argument ID leads to sql injection. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used.

### 122. CVE-2026-89157｜PCRE / PCRE2
- **Delta event**：CVSS_CHANGED (from=5.7; to=7.4)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：0.00102 / percentile=0.01048
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T04:18:03.753 / 2026-09-16T19:25:08.880
- **官方描述（原文）**：PCRE2 before 10.48, on 32-bit platforms, has a pcre2_pattern_convert out-of-bounds write when an attacker can provide a large pattern.

### 123. CVE-2026-89160｜PCRE / PCRE2
- **Delta event**：CVSS_CHANGED (from=3.7; to=6.5)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：0.00221 / percentile=0.12821
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T04:18:04.343 / 2026-09-16T19:15:29.443
- **官方描述（原文）**：PCRE2 before 10.48 has a pcre2_match out-of-bounds read during the PCRE2_MATCH_INVALID_UTF matching of an invalid UTF subject.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-76460｜Cisco / Identity Services Engine
- **Title**：Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) contain an incorrect use of privileged APIs vulnerability that could allow an unauthenticated, remote attacker to gain unauthorized access to the affected device by bypassing the web-based management interface.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-58704｜Google / Pixel
- **Title**：Google Pixel Improper Authorization Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00112 / percentile=0.01564
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Pixel devices contain an improper authorization vulnerability in the cellular modem. A logic error may allow an attacker to bypass permission checks and escalate privileges.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-87886｜Acronis / Backup
- **Title**：Acronis Backup Incorrect Default Permissions Vulnerability
- **Risk**：P1 / score 85；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、DELTA_NEW_KEV(+15)
- **CVSS**：未確認
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Acronis Backup plugin for cPanel & WHM and extension for Plesk contains an incorrect default permissions vulnerability that could allow for privilege escalation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-20284｜Cisco / Cisco Identity Services Engine Software
- **Title**：未確認
- **Risk**：P1 / score 53；reasons：ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=active / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：A vulnerability in the SXP REST API of Cisco ISE could allow an authenticated, remote attacker to conduct SQL injection attacks. This vulnerability is due to insufficient validation of user-supplied input in REST API calls. An attacker could exploit this vulnerability by sending crafted input to an affected device. A successful exploit could allow the attacker to view or modify data on the underlying database for the affected device. In single-node deployments, successful exploitation of this vulnerability could cause the affected ISE node to become unavailable, resulting in a DoS condition. In that condition, endpoints that have not already authenticated would be unable to access the network until the node is restored. To exploit this vulnerability, the attacker must have valid administrative credentials, have the SXP service enabled, and have at least one SXP connection configured.
- **CISA Required Action（原文）**：未確認
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-92719 | WATCH / 30 | quickwit-oss / quickwit | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92604 | WATCH / 30 | StamusNetworks / scirius | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92601 | WATCH / 30 | stylefeng / Guns | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92566 | WATCH / 30 | datageartech / datagear | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92469 | WATCH / 30 | zlt2000 / microservices-platform | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92466 | WATCH / 30 | zlt2000 / microservices-platform | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92459 | WATCH / 30 | guchengwuyue / yshop-crm | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92456 | WATCH / 30 | guchengwuyue / yshop-crm | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92398 | WATCH / 30 | Ruijie / RG-EW3000GX | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92397 | WATCH / 30 | Ruijie / RG-EW3000GX | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-86043 | WATCH / 30 | zalando / skipper | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-85731 | WATCH / 30 | oras-project / oras-go | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-84997 | WATCH / 30 | reactphp / http | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63128 | WATCH / 30 | modelcontextprotocol / rust-sdk | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63127 | WATCH / 30 | modelcontextprotocol / rust-sdk | v3.1 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63126 | WATCH / 30 | square / wire | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-59974 | WATCH / 30 | stanfordnlp / stanza | v3.1 7.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92808 | WATCH / 28 | Altium / Altium Enterprise Server | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92805 | WATCH / 28 | uvdesk / community-skeleton | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92787 | WATCH / 28 | feast-dev / feast | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92785 | WATCH / 28 | Angel-ML / angel | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92749 | WATCH / 28 | chaitin / SafeLine | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92720 | WATCH / 28 | kubero-dev / kubero | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92717 | WATCH / 28 | cobbr / Covenant | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92578 | WATCH / 28 | WWBN / AVideo | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92576 | WATCH / 28 | HKUDS / nanobot | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：27。
- EPSS 未確認：29；Exploitation status 未確認：9。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-17T05:36:46.527188+00:00`；Delta generated at：`2026-09-17T05:36:46.527188+00:00`。

---

## 可驗證資料來源

- **CVE-2026-76460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-58704** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58704) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-58704) · [Vendor / Advisory (source.android.com)](https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87886** — [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (security-advisory.acronis.com)](https://security-advisory.acronis.com/advisories/SEC-10986) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87886)
- **CVE-2026-20284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20284)
- **CVE-2026-92719** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92719)
- **CVE-2026-92604** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92604)
- **CVE-2026-92601** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92601)
- **CVE-2026-92566** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92566)
- **CVE-2026-92469** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92469)
- **CVE-2026-92466** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92466)
- **CVE-2026-92459** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92459)
- **CVE-2026-92456** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92456)
- **CVE-2026-92398** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92398)
- **CVE-2026-92397** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92397)
- **CVE-2026-86043** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86043)
- **CVE-2026-85731** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85731)
- **CVE-2026-84997** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84997)
- **CVE-2026-63128** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63128)
- **CVE-2026-63127** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63127)
- **CVE-2026-63126** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63126)
- **CVE-2026-59974** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59974)
- **CVE-2026-92808** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92808)
- **CVE-2026-92805** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92805)
- **CVE-2026-92787** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92787)
- **CVE-2026-92785** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92785)
- **CVE-2026-92749** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92749)
- **CVE-2026-92720** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92720)
- **CVE-2026-92717** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92717)
- **CVE-2026-92578** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92578)
- **CVE-2026-92576** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92576)
- **CVE-2026-92395** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92395)
- **CVE-2026-91843** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91843)
- **CVE-2026-91106** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91106)
- **CVE-2026-91104** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91104)
- **CVE-2026-90049** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90049)
- **CVE-2026-90048** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90048)
- **CVE-2026-90042** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90042)
- **CVE-2026-90038** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90038)
- **CVE-2026-90037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90037)
- **CVE-2026-90036** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90036)
- **CVE-2026-90012** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90012)
- **CVE-2026-90011** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90011)
- **CVE-2026-89990** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89990)
- **CVE-2026-89972** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89972)
- **CVE-2026-89970** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89970)
- **CVE-2026-89969** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89969)
- **CVE-2026-89930** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89930)
- **CVE-2026-89918** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89918)
- **CVE-2026-89916** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89916)
- **CVE-2026-89915** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89915)
- **CVE-2026-89914** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89914)
- **CVE-2026-89857** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89857)
- **CVE-2026-89847** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89847)
- **CVE-2026-89846** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89846)
- **CVE-2026-89788** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89788) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89788)
- **CVE-2026-89786** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89786) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89786)
- **CVE-2026-89783** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89783) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89783)
- **CVE-2026-89779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89779) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89779)
- **CVE-2026-89778** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89778) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89778)
- **CVE-2026-89775** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89775) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89775)
- **CVE-2026-89083** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89083)
- **CVE-2026-89082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89082)
- **CVE-2026-87796** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87796)
- **CVE-2026-81642** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81642) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-81642)
- **CVE-2026-77411** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77411)
- **CVE-2026-77408** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77408)
- **CVE-2026-77405** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77405)
- **CVE-2026-76423** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76423)
- **CVE-2026-76420** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76420)
- **CVE-2026-75513** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75513)
- **CVE-2026-73461** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73461) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-73461)
- **CVE-2026-73456** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73456)
- **CVE-2026-73453** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73453) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-73453)
- **CVE-2026-73447** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73447) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-73447)
- **CVE-2026-73172** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73172)
- **CVE-2026-70416** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70416)
- **CVE-2026-61594** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61594)
- **CVE-2026-58147** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58147)
- **CVE-2026-58146** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58146)
- **CVE-2026-40855** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-40855)
- **CVE-2026-27565** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-27565) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-27565)
- **CVE-2026-27546** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-27546) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-27546)
- **CVE-2026-20341** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20341)
- **CVE-2026-20332** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20332)
- **CVE-2026-20331** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20331)
- **CVE-2026-20330** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20330)
- **CVE-2026-20329** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20329)
- **CVE-2026-20326** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20326)
- **CVE-2026-20325** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20325)
- **CVE-2026-20324** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20324)
- **CVE-2026-20322** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20322)
- **CVE-2026-20307** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20307)
- **CVE-2026-20306** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20306)
- **CVE-2026-20305** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20305)
- **CVE-2026-20242** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20242)
- **CVE-2026-20237** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20237)
- **CVE-2026-20234** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20234)
- **CVE-2026-20211** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20211)
- **CVE-2026-20194** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20194)
- **CVE-2026-20192** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20192)
- **CVE-2026-20176** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20176)
- **CVE-2026-20130** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20130)
- **CVE-2025-59953** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-59953)
- **CVE-2026-92568** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92568)
- **CVE-2026-92461** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92461)
- **CVE-2026-92406** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92406)
- **CVE-2026-92405** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92405)
- **CVE-2026-92380** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92380)
- **CVE-2026-92366** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92366)
- **CVE-2026-92091** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92091) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-92091)
- **CVE-2026-86475** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86475) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86475)
- **CVE-2026-85732** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85732)
- **CVE-2026-84906** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84906) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84906)
- **CVE-2026-77360** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77360)
- **CVE-2026-69147** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69147)
- **CVE-2026-19857** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19857) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-19857)
- **CVE-2026-13407** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13407) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-13407)
- **CVE-2026-92472** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92472)
- **CVE-2026-92418** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92418)
- **CVE-2026-92383** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92383)
- **CVE-2026-92364** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92364)
- **CVE-2026-89157** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89157) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89157)
- **CVE-2026-89160** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89160) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89160)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
