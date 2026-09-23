# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**117** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=116、NEW_KEV=4。
- Intelligence 候選：**30** 筆；P1 **4**、P2 **0**、P3 **5**、WATCH **21**。
- Baseline：state / generated_at=2026-09-22T05:38:29.007634+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-94127、CVE-2026-93952、CVE-2026-93616、CVE-2026-85102。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **117** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-94127｜F5 / BIG-IP APM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T15:17:24.313)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-22T15:17:24.313 / 2026-09-23T04:17:58.180
- **官方描述（原文）**：F5 BIG-IP APM contains a heap-based buffer overflow vulnerability when access policy and an OAuth profile are configured on a virtual server. This vulnerability could allow an unauthenticated attacker to perform remote code execution.

### 2. CVE-2026-93952｜Arista / VeloCloud Orchestrator
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T08:16:43.047)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-22T08:16:43.047 / 2026-09-23T04:17:58.007
- **官方描述（原文）**：Arista VeloCloud Orchestrator (VCO) on-prem contains an improper input validation vulnerability that may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator.

### 3. CVE-2026-93616｜Check Point / Multiple Products
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T13:17:11.963)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-22T13:17:11.963 / 2026-09-23T04:17:57.453
- **官方描述（原文）**：Check Point Security Management Server, Multi-Domain Security Management Server, Log Server, Multi-Domain Log Server, and SmartEvent contain a path traversal vulnerability that allows an unauthenticated attacker to upload and execute arbitrary scripts.

### 4. CVE-2026-85102｜Check Point / Multiple Products
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00329 / percentile=0.26293
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-09T13:20:43.793 / 2026-09-23T04:17:56.393
- **官方描述（原文）**：Check Point Security Gateway and Check Point Spark Firewall using Site to Site VPN or Remote Access VPN contain an improper certificate validation vulnerability which could allow an unauthenticated remote attacker to execute arbitrary code on the Gateway.

### 5. CVE-2026-95675｜D-LINK / DAP-1360
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T14:17:22.230)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T14:17:22.230 / 2026-09-22T20:25:55.870
- **官方描述（原文）**：D-Link DAP-1360 firmware version 6.14 and earlier contains an unauthenticated remote code execution vulnerability that allows remote attackers to execute arbitrary commands as root by sending crafted requests to the device's web management interface without valid credentials. Attackers can fully compromise the device to persistently modify its configuration and use it as a pivot point into the local network.

### 6. CVE-2026-93088｜SGLang / SGLang
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T15:17:21.433)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T15:17:21.433 / 2026-09-22T19:16:57.450
- **官方描述（原文）**：SGLang's multimodal generation runtime is vulnerable to unauthenticated arbitrary code execution because the disaggregated-diffusion orchestrator's DiffusionServer binds an unauthenticated ZeroMQ ROUTER socket to a network interface and passes the final frame of received multipart messages directly to pickle.loads() before any validation occurs.

### 7. CVE-2026-91130｜home-assistant / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:56.700)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:56.700 / 2026-09-22T20:17:11.607
- **官方描述（原文）**：Home Assistant is open source home automation software focused on local control and privacy. Prior to 2026.7.0, the Statistics Graph card in src/components/chart/statistics-chart.ts passed entity names through getStatisticLabel and computeStateName and interpolated param.seriesName into ECharts tooltip HTML without escaping. An authenticated user or an integration that supplies a malicious default entity name could cause script-related HTML to execute when a viewer hovered over a data point. Mean, State, Sum, and Change fields in the default Line chart configuration were affected, while Bar charts were not. This issue is fixed in version 2026.7.0.

### 8. CVE-2026-86059｜Dokploy / dokploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T17:17:27.690)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T17:17:27.690 / 2026-09-22T18:17:24.473
- **官方描述（原文）**：Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, Dokploy organization members without Git provider access can retrieve plaintext provider credentials through github.one, gitlab.one, gitea.one, and bitbucket.one because those protected procedures return full provider rows without applying getAccessibleGitProviderIds or an organization check. The application.one route also returns nested GitHub, GitLab, Gitea, and Bitbucket relations from findApplicationById with GitHub App private keys, OAuth tokens, client secrets, webhook secrets, and app passwords even when hasGitProviderAccess is false. A member with application read access or a provider identifier can therefore bypass per-member provider assignment and use the exposed credentials to access private repositories or manipulate external workflows. This issue is fixed in version 0.29.13.

### 9. CVE-2026-77254｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:49.693)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:49.693 / 2026-09-22T19:16:49.693
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, requests to the HTTP MCP endpoint without a per-user identity are allowed to reach tool handlers, which then use globally configured Jira or Confluence credentials. A network caller can perform operations with the operator account's permissions unless the deployment has an independent authentication boundary. The advisory traces the vulnerable input and processing flow through streamable-http, UserTokenMiddleware, _get_fetcher, and global credentials, which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 10. CVE-2026-94462｜spree / spree
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:59.497)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:59.497 / 2026-09-22T20:17:13.130
- **官方描述（原文）**：Spree is an open source e-commerce solution built with Ruby on Rails. From 5.4.0 until 5.4.4 and 5.5.4, PATCH /api/v3/store/carts/:id/associate in Spree::Api::V3::Store::CartsController#associate uses find_cart_for_association to locate a cart by prefixed_id but does not require a cart token or otherwise verify possession of the selected guest cart. An authenticated customer can derive reversible prefixed cart IDs, associate an eligible guest cart with the attacker's account, and receive billing and shipping address data from the cart. Exploitation requires a guest cart with address data on a store that does not require login for checkout, and reassignment can also disrupt the guest's in-progress cart. This issue is fixed in versions 5.4.4 and 5.5.4.

### 11. CVE-2026-89420｜ZenHive / mpp
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T12:17:14.370)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T12:17:14.370 / 2026-09-22T19:09:32.273
- **官方描述（原文）**：Improper Validation of Specified Quantity in Input in ZenHive mpp allows a client holding an open payment channel to obtain paid resources without being charged. MPP.Session.Actions.accept_voucher/3 in lib/mpp/session/actions.ex treats a voucher whose cumulativeAmount equals the channel's already-accepted cumulative amount as an idempotent success, returning the channel unchanged without calling maybe_spend/2. The credential verifies, the protected resource is served, and spent and units stay where they were. Because the server issues a fresh challenge per request and the credential replay store keys on challenge id and payload, the same signed voucher can be re-presented under every new challenge, so one paid voucher yields an unbounded number of paid units. The path is reachable from any method built on MPP.Session.Method through the Plug, MCP, JSON-RPC and WebSocket transports. This issue affects mpp: from 0.14.0 before 0.16.2.

### 12. CVE-2026-89407｜FasterXML / jackson-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T15:17:21.053)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T15:17:21.053 / 2026-09-22T20:00:03.713
- **官方描述（原文）**：NumberInput.looksLikeValidNumber() in FasterXML jackson-core pre-validates "stringified numbers" with two regular expressions: PATTERN_FLOAT ([+-]?[0-9]*[\.]?[0-9]+([eE][+-]?[0-9]+)?), present since 2.17.0, and PATTERN_FLOAT_TRAILING_DOT, added in 2.17.2. PATTERN_FLOAT places adjacent quantifiers over the same character class -- an optional [0-9]* run, an optional dot, then a required [0-9]+ run -- so input that ultimately fails to match forces Java's backtracking engine to retry every possible split point of the digit run. Matching cost therefore grows with the square of the input length. An attacker who can supply JSON that an application deserializes into a numeric target type reaches this method through jackson-databind's default String-to-number coercion (StdDeserializer and NumberDeserializers for BigDecimal, BigInteger, Double and Float). Because StreamReadConstraints.maxStringLength defaults to 20,000,000 characters, no constraint bounds the input before it reaches the regex. Testing by the reporter confirmed O(n^2) growth across five consecutive input-size doublings, with a single 160,000-character string consuming roughly 74 seconds in one call; a small number of concurrent requests of ordinary body size can therefore exhaust a server's request-handling thread pool. The affected method does not exist before 2.17.0, so 2.16.x and earlier releases are not affected. The fix replaces both regular expressions with a hand-rolled single-pass scan.

### 13. CVE-2026-88419｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T20:17:11.083)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T20:17:11.083 / 2026-09-22T20:17:11.083
- **官方描述（原文）**：An unrestricted upload of files with a dangerous type in the thumbnail-upload endpoint (/index.php?m=member&f=article&v=thumbUpload) of WuzhiCMS 5.0.0 allows an authenticated low-privileged member to upload a crafted .php file and execute arbitrary PHP code on the server, because the stored file extension is taken verbatim from the client-supplied filename with no extension allowlist or content validation and the file is written to the web-accessible uploadfile/ directory, from which the web server executes PHP.

### 14. CVE-2026-85279｜notepad-plus-plus / notepad-plus-plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:23.213)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:23.213 / 2026-09-22T19:16:54.623
- **官方描述（原文）**：Notepad++ is a free and open-source source code editor. Prior to 8.9.8, Notepad++ contains a stack buffer overflow in PluginsManager::loadPluginFromPath in PowerEditor/src/MISC/PluginsManager/PluginsManager.cpp because the plugin-supplied GetLexerCount() result controls a loop that writes to containers[30] without enforcing NB_MAX_EXTERNAL_LANG. A malicious or compromised plugin that reports more than 30 lexers can write beyond the stack array and corrupt control data, which can permit arbitrary code execution in the Notepad++ process context. This issue is fixed in version 8.9.8.

### 15. CVE-2026-77274｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:19.253)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:19.253 / 2026-09-22T19:16:51.330
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, validate_url_for_ssrf has a backslash authority confusion because it interprets the authority differently from the Requests connection layer in the header-based Jira and Confluence URL authentication flow. A crafted URL can validate as an external hostname while the HTTP client connects to an internal host, permitting server-side requests to protected network resources. This issue is fixed in version 0.22.0.

### 16. CVE-2026-77256｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:50.007)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:50.007 / 2026-09-22T20:17:07.960
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, the plaintext OAuth fallback file containing refresh and access tokens is written with permissions inherited from the process umask. Under common or permissive configurations, other local users can read the backup and retain Atlassian access through the refresh token. The advisory traces the vulnerable input and processing flow through OAuthConfig._save_tokens_to_file, refresh_token, access_token, and umask, which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 17. CVE-2026-77253｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:49.540)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:49.540 / 2026-09-22T19:16:49.540
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, Jira and Confluence attachment upload tools accept arbitrary local filesystem paths and send the selected bytes to Atlassian. In HTTP or multi-user deployments, a caller can cross the client-to-server filesystem boundary and disclose configuration, credentials, mounted secrets, or other files readable by the MCP process. The advisory traces the vulnerable input and processing flow through jira_upload_attachment, confluence_upload_attachment, file_path, and server-local filesystem, which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 18. CVE-2026-77247｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:48.877)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:48.877 / 2026-09-22T19:16:48.877
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, Jira and Confluence upload tools interpret caller-controlled path arguments on the MCP server and open those files before sending them as attachments. In remote or multi-user deployments, a permitted client can disclose host files without shell or direct filesystem access. The advisory traces the vulnerable input and processing flow through AttachmentsMixin.upload_attachment, AttachmentsMixin.upload_attachments, file_path, file_paths, and jira update_issue, which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 19. CVE-2026-77243｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:17.410)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:17.410 / 2026-09-22T19:16:48.617
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, ENABLED_TOOLS and TOOLSETS are applied when tools are listed but are not rechecked when a tools/call request is dispatched. A client that knows a hidden tool name can directly invoke excluded read, write, or delete tools despite the operator's configured least-privilege restrictions. The advisory traces the vulnerable input and processing flow through ENABLED_TOOLS, TOOLSETS, tools/list, tools/call, and _call_tool_mcp, which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 20. CVE-2026-77242｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:16.430)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:16.430 / 2026-09-22T19:16:48.503
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, validate_url_for_ssrf checks a hostname's resolved addresses, but Requests and urllib3 resolve the hostname again when connecting. A caller can use a short-lived DNS answer that is public during validation and private during connection, preserving unauthenticated access to internal or metadata endpoints despite the earlier CVE-2026-27826 remediation. The advisory traces the vulnerable input and processing flow through validate_url_for_ssrf, _check_dns_resolution, socket.getaddrinfo, and _make_ssrf_safe_hook, which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 21. CVE-2026-75607｜blakeblackshear / frigate
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:17:54.430)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:17:54.430 / 2026-09-22T16:17:54.570
- **官方描述（原文）**：Frigate is an open source network video recorder. Prior to 0.17.2, the WebSocket handler in frigate/comms/ws.py forwards attacker-selected message topics to the dispatcher without checking the authenticated user's role because the nginx authentication subrequest does not provide role-aware authorization to the handler. Any authenticated viewer can send admin-only topics such as restart, notifications/set, and camera detection, recording, snapshot, audio, motion, and enablement settings, causing service restarts or disabling security monitoring functions. Authentication must be enabled and valid viewer credentials are required. This issue is fixed in version 0.17.2.

### 22. CVE-2026-63104｜usekaneo / kaneo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T20:17:04.597)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T20:17:04.597 / 2026-09-22T20:53:07.383
- **官方描述（原文）**：Kaneo versions 2.3.12 before 2.12.2 contain a missing authorization vulnerability that allows authenticated workspace members with viewer or member roles to delete and modify tasks beyond their assigned permissions by exploiting the bulk task endpoint that omits workspace permission checks. Attackers can send requests to the PATCH /api/task/bulk endpoint, which verifies only workspace membership without calling the role-based permission check enforced on all other task endpoints, to permanently delete all tasks or modify task status, priority, assignee, due date, and labels in a workspace.

### 23. CVE-2026-59991｜psd-tools / psd-tools
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T20:17:04.123)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T20:17:04.123 / 2026-09-22T20:17:04.123
- **官方描述（原文）**：psd-tools is a Python package for working with Adobe Photoshop PSD files. Prior to 1.17.4, PSDImage.composite() and PSDImage.numpy() allocated output buffers from attacker-controlled PSD header geometry, including width, height, channels, depth, and per-layer rectangles, before validating those values against the available file data. A tiny crafted PSD could therefore cause multi-gigabyte memory allocation, and PSDImage.composite() could return a black image with only a warning instead of raising an exception. Services that composite untrusted PSD files could be terminated by out-of-memory handling. This issue is fixed in version 1.17.4.

### 24. CVE-2026-13087｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T17:17:23.807)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T17:17:23.807 / 2026-09-22T19:37:36.747
- **官方描述（原文）**：A heap out-of-bounds write vulnerability was found in the Linux kernel's RPC-over-RDMA server reply path in net/sunrpc/xprtrdma/svc_rdma_sendto.c. When a crafted RPC-over-RDMA client sends a large NFS READ request with an empty Write list and no Reply chunk, the server linearizes the entire multi-page reply into a fixed-size 4096-byte heap buffer without bounds checking, resulting in a kernel heap overflow. This can lead to denial of service via kernel crash or potential code execution through corruption of adjacent kernel heap objects.

### 25. CVE-2026-96257｜Fast / FAC1203R Gigabit Edition
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T03:17:06.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T03:17:06.077 / 2026-09-23T03:17:06.077
- **官方描述（原文）**：A flaw has been found in Fast FAC1203R Gigabit Edition 2.0.4. Affected by this issue is the function copy_msg_element of the component Device Discovery Service. Executing a manipulation can lead to stack-based buffer overflow. The attack can be executed remotely. The exploit has been published and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 26. CVE-2026-95654｜David-Crty / Databasement
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:18.770)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:18.770 / 2026-09-22T16:18:18.770
- **官方描述（原文）**：Databasement before 1.7.14 validates invitation tokens only when the acceptance page loads, caching the authorization decision without re-checking token validity during acceptance. Attackers with a leaked or forwarded invitation link can load the page while pending, then accept the invitation after the legitimate user has already accepted it to overwrite the account password and gain authenticated access to managed database credentials and secrets.

### 27. CVE-2026-94456｜GitroomHQ / postiz-app
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T17:17:31.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T17:17:31.670 / 2026-09-22T19:37:36.747
- **官方描述（原文）**：Postiz generates security-sensitive credentials using `Math.random()` instead of a cryptographically secure source. The same helper is used for OAuth access tokens, authorization codes, client secrets, organization API keys, and PKCE verifiers, meaning these credentials depend entirely on V8’s deterministic xorshift128+ PRNG state. An unauthenticated OAuth dynamic client registration endpoint exposes freshly generated client credentials, giving attackers enough consecutive PRNG output to reconstruct that internal state. Once recovered, they can deterministically derive past and future values produced by the same generator, potentially compromising credentials belonging to other users and organizations.

### 28. CVE-2026-93556｜Kompini / Tankuam Places
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T09:17:05.800)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00305 / percentile=0.23439
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T09:17:05.800 / 2026-09-22T19:41:38.447
- **官方描述（原文）**：The ‘/password/guardarClau/recover’ endpoint accepts the ‘usuariId’ parameter, which specifies the account whose password is to be changed. The JWT token for the recovery process is not validated against the user specified in that parameter. An unauthenticated attacker could manipulate the identifier and reset the password for any account, including administrative accounts, which could allow them to take control of the account.

### 29. CVE-2026-89422｜Erlang / OTP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T09:17:05.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00368 / percentile=0.30701
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T09:17:05.540 / 2026-09-22T19:09:32.273
- **官方描述（原文）**：Key Exchange without Entity Authentication vulnerability in Erlang/OTP ssl allows a peer that answers a TLS 1.3 client connection to impersonate the intended server. A pre_shared_key extension in the ServerHello that the client never offered causes the client to complete the handshake without validating the server's certificate, so ssl:connect returns {ok, Socket} against a peer holding no certificate, no private key and no prior session. tls_client_connection_1_3:handle_server_hello/2 passes the received extension to tls_gen_connection_1_3:handle_resumption/2, which sets resumption = true on its mere presence without checking that the client offered a PSK. tls_handshake_1_3:get_pre_shared_key/4 meanwhile falls back to the all-zero "no PSK" value and keys the handshake with the ordinary non-PSK schedule, so the attacker's own ephemeral key suffices. The resumption flag then routes maybe_resumption/1 straight to wait_finished, skipping the certificate-handling states, so certificate path validation, verify_fun, hostname verification, partial_chain, CRL checking and OCSP stapling are all bypassed. The default client configuration is affected; clients restricted to TLS 1.2 are not. This issue affects OTP from OTP 22.2 before OTP 27.3.4.18, OTP 28.5.0.7, and OTP 29.1.1, corresponding to ssl from 9.5 before 11.2.12.13, 11.6.0.6, and 11.7.7.

### 30. CVE-2026-89276｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:29.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:29.550 / 2026-09-22T19:05:50.323
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 31. CVE-2026-89275｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:29.407)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:29.407 / 2026-09-22T19:05:50.323
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 32. CVE-2026-87121｜lwIP / TCP/IP Stack MQTT
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T20:17:09.967)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T20:17:09.967 / 2026-09-22T21:17:32.930
- **官方描述（原文）**：lwIP TCP/IP Stack MQTT is vulnerable to an out-of-bounds write, which may allow an attacker to gain full code execution on the device.

### 33. CVE-2026-87080｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T08:16:40.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00148 / percentile=0.04415
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T08:16:40.750 / 2026-09-22T19:07:00.983
- **官方描述（原文）**：Net::IDN::Punycode::PP versions before 2.590 for Perl decode a truncated label to a name containing a character it never encoded in decode_punycode. The pure-Perl decoder reads one digit at a time with four-argument substr and tests the result with defined to detect the end of the input. substr on an exhausted string returns the empty string rather than undef, so decoding continues past the end. The empty string converts to a digit value below the range, reducing the accumulator, and the decoder derives one extra code point and its position from it. The result is deterministic. The XS backend rejects the same label. Net::IDN::Punycode uses this backend wherever the XS does not build. The two backends disagree about what such a label means, so a sender can pick a label that one installation resolves to a name and another rejects.

### 34. CVE-2026-87078｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T08:16:40.530)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00154 / percentile=0.04983
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T08:16:40.530 / 2026-09-22T19:07:00.983
- **官方描述（原文）**：Net::IDN::Punycode versions from 2.302 before 2.590 for Perl leak the output buffer on every rejected label in decode_punycode. The XS backend allocates the scalar it returns before it validates the input, sizing the buffer at twice the input length. The scalar is released only on the success path, so each of the three croaks that reject a label leaves the scalar and its buffer allocated. Nothing bounds the label length in the to-Unicode direction, since the 63-byte DNS limit is checked only when converting to ASCII. Only the XS backend is affected. A sender who supplies invalid labels grows the process by twice the label length per rejected call, with no successful call needed.

### 35. CVE-2026-85734｜HKUDS / LightRAG
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T17:17:27.367)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T17:17:27.367 / 2026-09-22T18:17:23.530
- **官方描述（原文）**：LightRAG provides simple and fast retrieval-augmented generation. Prior to 1.5.5, the POST /login endpoint in lightrag/api/lightrag_server.py does not impose a rate limit, account lockout, delay, or counter for failed authentication attempts. A network attacker can submit password guesses at full request speed until a valid account password is found. Successful credential recovery grants authenticated access to documents, the knowledge graph, and administrative operations. This issue is fixed in version 1.5.5.

### 36. CVE-2026-84412｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:22.923)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:22.923 / 2026-09-22T19:16:54.513
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 37. CVE-2026-84388｜Fortinet / FortiPAM Chrome Extension
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T15:17:18.950)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T15:17:18.950 / 2026-09-22T19:09:58.680
- **官方描述（原文）**：A improper restriction of rendered ui layers or frames vulnerability in Fortinet FortiPAM Chrome Extension 8.0 all versions, FortiPAM Chrome Extension 7.4 all versions may allow attacker to information disclosure via remote unauthenticated attack

### 38. CVE-2026-83660｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:22.673)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:22.673 / 2026-09-22T19:05:50.323
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation. Exploitation of this issue does not require user interaction. Scope is changed.

### 39. CVE-2026-82443｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:21.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:21.790 / 2026-09-22T19:16:53.647
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation. A low-privileged attacker could exploit this vulnerability to gain elevated access to internal resources. Exploitation of this issue does not require user interaction. Scope is changed.

### 40. CVE-2026-82013｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:21.657)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:21.657 / 2026-09-22T19:05:50.323
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation. A low-privileged attacker could exploit this vulnerability to gain elevated access to internal resources. Exploitation of this issue does not require user interaction. Scope is changed.

### 41. CVE-2026-82011｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:21.523)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:21.523 / 2026-09-22T19:05:50.323
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in a Security feature bypass. A low-privileged attacker could leverage this vulnerability to bypass security measures and gain unauthorized read and limited write access. Exploitation of this issue does not require user interaction. Scope is changed.

### 42. CVE-2026-82010｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:21.377)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:21.377 / 2026-09-22T19:16:53.537
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 43. CVE-2026-82009｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:21.220)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:21.220 / 2026-09-22T19:05:50.323
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution in the context of the current user. An attacker with high privileges could exploit this vulnerability to execute arbitrary SQL commands. Exploitation of this issue does not require user interaction. Scope is changed.

### 44. CVE-2026-82008｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:21.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:21.077 / 2026-09-22T19:16:53.427
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 45. CVE-2026-82000｜Adobe / AEM 6.5 Forms JEE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:53.297)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:53.297 / 2026-09-23T04:17:53.247
- **官方描述（原文）**：Adobe Experience Manager Forms JEE is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation. A low-privileged attacker could exploit this vulnerability to gain elevated access to internal resources. Exploitation of this issue does not require user interaction. Scope is changed.

### 46. CVE-2026-81995｜Adobe / AEM 6.5 Forms JEE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:52.917)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:52.917 / 2026-09-23T04:17:52.727
- **官方描述（原文）**：Adobe Experience Manager Forms JEE is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in the context of the current user. An attacker with high privileges could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 47. CVE-2026-80156｜LANTRONIX / SLC8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:02.083)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:02.083 / 2026-09-22T20:25:55.870
- **官方描述（原文）**：Lantronix SLC8000 before firmware v9.7.0.5, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB882/SLCx-03/SLCx-02 contain a path traversal vulnerability in the web management portal upload endpoint that allows authenticated attackers to write arbitrary data to any location on the device's filesystem, leading to remote code execution. The upload filename validation strips backslash characters but does not subsequently check for forward slashes when a backslash is detected; by supplying a filename containing both characters an attacker writes outside the intended upload directory to any writable path. Attackers can use this vulnerability to achieve complete loss of confidentiality, integrity, and availability on the affected device and potentially impact downstream serial-connected devices.

### 48. CVE-2026-80155｜LANTRONIX / SLC8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:01.917)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:01.917 / 2026-09-22T20:25:55.870
- **官方描述（原文）**：Lantronix SLC8000 before firmware v9.7.0.5, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB882/SLCx-03/SLCx-02 contain an authentication bypass vulnerability in the web management portal upload endpoint that allows unauthenticated attackers to read sensitive configuration files and upload files to arbitrary filesystem locations, leading to remote code execution. The web configuration server constructs the session cookie file path using snprintf with a fixed-size buffer; by supplying a cookie value of a specific length an attacker causes the path to truncate at the required delimiter and leverages path traversal to redirect authentication validation to an arbitrary on-disk file such as the local user database, bypassing all session checks. Attackers can use this vulnerability to achieve complete loss of confidentiality, integrity, and availability on the affected device and potentially impact downstream serial-connected devices.

### 49. CVE-2026-80152｜LANTRONIX / SLC8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:01.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:01.607 / 2026-09-22T20:25:55.870
- **官方描述（原文）**：Lantronix SLC8000 before firmware v9.7.0.3, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB882/SLCx-03/SLCx-02 contain a command injection vulnerability that allows authenticated attackers with the services permission to execute arbitrary shell commands as root by exploiting the set script schedule command that passes unsanitized user input to a system() call. Attackers with the services permission can authenticate to the terminal or CLI interface and inject malicious commands through the unsanitized parameter to achieve complete loss of confidentiality, integrity, and availability on the affected device and potentially impact downstream serial-attached devices.

### 50. CVE-2026-80151｜LANTRONIX / SLC8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:01.460)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:01.460 / 2026-09-22T20:25:55.870
- **官方描述（原文）**：Lantronix SLC8000 before firmware v9.7.0.3, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB882/SLCx-03/SLCx-02 contain a command injection vulnerability that allows authenticated attackers with the services permission to execute arbitrary shell commands as root by exploiting the set nfs download command that passes unsanitized user input to a system() call. Attackers with the services permission can authenticate to the terminal or CLI interface and inject malicious commands through the unsanitized parameter to achieve complete loss of confidentiality, integrity, and availability on the affected device and potentially impact downstream serial-attached devices.

### 51. CVE-2026-80147｜LANTRONIX / SLC8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:00.863)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:00.863 / 2026-09-22T20:25:55.870
- **官方描述（原文）**：Lantronix SLC8000 before firmware v9.7.0.2, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB882/SLCx-03/SLCx-02 contain a stack-based buffer overflow vulnerability that allows authenticated attackers to potentially execute arbitrary code by exploiting an undocumented mfc eeprom write command that copies unbounded user input into a bounded stack buffer before passing it to a system() call. Attackers can authenticate as any user to the terminal or CLI interface and supply an oversized input to trigger the overflow, potentially achieving complete loss of confidentiality, integrity, and availability on the affected device and impacting downstream serial-attached devices.

### 52. CVE-2026-80146｜LANTRONIX / SLC8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:00.720)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:00.720 / 2026-09-22T20:25:55.870
- **官方描述（原文）**：Lantronix SLC8000 before firmware v9.7.0.2, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB882/SLCx-03/SLCx-02 contain a stack-based buffer overflow vulnerability that allows authenticated attackers to potentially execute arbitrary code by exploiting an undocumented mfc eeprom read command that copies unbounded user input into a bounded stack buffer before passing it to a system() call. Attackers can authenticate as any user to the terminal or CLI interface and supply an oversized input to trigger the overflow, potentially achieving complete loss of confidentiality, integrity, and availability on the affected device and impacting downstream serial-attached devices.

### 53. CVE-2026-80145｜LANTRONIX / SLC8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:00.570)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:00.570 / 2026-09-22T20:25:55.870
- **官方描述（原文）**：Lantronix SLC8000 before firmware v9.7.0.2, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB882/SLCx-03/SLCx-02 contain a command injection vulnerability that allows authenticated attackers with the services permission to execute arbitrary shell commands as root by exploiting the set cifs password command that passes unsanitized user input to a system() call. Attackers with the services permission can authenticate to the terminal or CLI interface and inject malicious commands through the unsanitized parameter to achieve complete loss of confidentiality, integrity, and availability on the affected device and potentially impact downstream serial-attached devices.

### 54. CVE-2026-80144｜LANTRONIX / SLC8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:17:59.303)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:17:59.303 / 2026-09-22T20:25:55.870
- **官方描述（原文）**：Lantronix SLC8000 before firmware v9.7.0.2, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB882/SLCx-03/SLCx-02 contain a command injection vulnerability that allows authenticated attackers to execute arbitrary shell commands as root by exploiting an undocumented mfc eeprom write command that passes unsanitized user input to a system() call. Attackers can authenticate as any user to the terminal or CLI interface and inject malicious commands through the unsanitized parameter to achieve complete loss of confidentiality, integrity, and availability on the affected device and potentially impact downstream serial-attached devices.

### 55. CVE-2026-80143｜LANTRONIX / SLC8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:17:57.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:17:57.543 / 2026-09-22T20:25:55.870
- **官方描述（原文）**：Lantronix SLC8000 before firmware v9.7.0.2, EMG8500/EMG7500 before firmware v9.7.0.1, and all firmware versions of SLB882/SLCx-03/SLCx-02 contain a command injection vulnerability that allows authenticated attackers to execute arbitrary shell commands as root by exploiting an undocumented mfc eeprom read command that passes unsanitized user input to a system() call. Attackers can authenticate as any user to the terminal or CLI interface and inject malicious commands through the unsanitized parameter to achieve complete loss of confidentiality, integrity, and availability on the affected device and potentially impact downstream serial-attached devices.

### 56. CVE-2026-79313｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T15:17:15.467)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T15:17:15.467 / 2026-09-22T20:17:08.790
- **官方描述（原文）**：webpy web.py 0.76 is vulnerable to Insufficient Session Expiration. The application's session management relies on periodic cleanup to expire sessions instead of checking the last-access time when a session is loaded. As a result, an expired session whose record has not yet been cleaned up can still be replayed and used, allowing an attacker holding a previously valid session cookie to continue accessing protected resources after the configured idle timeout.

### 57. CVE-2026-7866｜RTI / Connext Professional
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:19.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:19.940 / 2026-09-23T04:17:46.510
- **官方描述（原文）**：Stack-based Buffer Overflow vulnerability in RTI Connext Professional (Core Libraries) allows Overflow Buffers. This issue affects Connext Professional: from 7.4.0 before 7.7.0.1, from 7.0.0 before 7.3.1.6, from 6.1.0 before 6.1.*, from 6.0.0 before 6.0.*, from 5.3.0 before 5.3.*, from 5.2.0 before 5.2.*, from 4.3x before 5.1.*.

### 58. CVE-2026-77987｜GitHub / Enterprise Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T21:17:32.653)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T21:17:32.653 / 2026-09-22T21:17:32.653
- **官方描述（原文）**：A server-side request forgery (SSRF) vulnerability was identified in the notebook viewer of GitHub Enterprise Server. The notebook viewer validated the scheme and host of a user-supplied URL but did not validate the port, allowing requests to be directed to internal services listening on other ports of the same appliance. Response bodies were not returned to the requester, but response timing acted as an oracle that allowed instance secrets to be extracted character by character. An extracted secret could then be used in a separate interaction with an internal service to obtain remote code execution on the appliance. Exploitation required network access to the instance and was unauthenticated when private mode was disabled, or required any authenticated user when private mode was enabled. This vulnerability affected GitHub Enterprise Server versions 3.17 through 3.22 and was fixed in versions 3.22.1, 3.21.6, 3.20.8, 3.19.12, 3.18.15, and 3.17.21. This vulnerability was reported through the GitHub Bug Bounty program.

### 59. CVE-2026-77621｜vectordotdev / vector
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:17:55.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:17:55.670 / 2026-09-22T16:17:55.670
- **官方描述（原文）**：Vector is a high-performance observability data pipeline. From 0.10.0 until 0.57.0, the file sink renders its templated path from event fields and opens the result without confining it to an intended directory. When an untrusted source supplies an event field used by the path template, the value can contain an absolute path or parent-directory traversal, causing Vector to create parent directories and create or overwrite files outside the intended location with the Vector process privileges. The resulting file write can modify sensitive files and can lead to code execution when a scheduled task, authorization file, or subsequently executed script is targeted. This issue is fixed in version 0.57.0.

### 60. CVE-2026-77244｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:17.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:17.560 / 2026-09-22T18:17:17.560
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, the HTTP transport accepts requests without a verified user identity and downstream fetcher construction falls back to the operator's globally configured Jira or Confluence credentials. A network client that can reach the MCP endpoint can invoke Atlassian tools as the operator, including read and write operations available to that account. The advisory traces the vulnerable input and processing flow through UserTokenMiddleware, AtlassianOpaqueTokenVerifier, _get_fetcher, and streamable-http, which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 61. CVE-2026-76709｜Hewlett Packard Enterprise (HPE) / ALE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T20:17:06.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T20:17:06.750 / 2026-09-22T20:17:06.750
- **官方描述（原文）**：A vulnerability exists in the internal administrative component of Analytics and Location Engine (ALE). Successful exploitation of this vulnerability could allow an unauthenticated remote attacker to gain unauthorized write access to the file system with elevated privileges, potentially resulting in full system compromise.

### 62. CVE-2026-76708｜Hewlett Packard Enterprise (HPE) / ALE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T20:17:06.620)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T20:17:06.620 / 2026-09-22T20:17:06.620
- **官方描述（原文）**：A vulnerability exists in the Analytics and Location Engine (ALE) where the application and underlying operating system use default, hard-coded credentials for several administrative and system accounts. An unauthenticated remote attacker could exploit this vulnerability by attempting to log in using these known default credentials. Successful exploitation could result in an attacker gaining unauthorized access to the application's management interface and the underlying operating system, potentially leading to full system compromise.

### 63. CVE-2026-75745｜Adobe / AEM 6.5 Forms JEE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:47.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:47.510 / 2026-09-22T19:23:57.800
- **官方描述（原文）**：Adobe Experience Manager Forms JEE is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 64. CVE-2026-75728｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:16.293)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:16.293 / 2026-09-22T19:05:50.323
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction.

### 65. CVE-2026-75723｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:16.163)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:16.163 / 2026-09-22T19:16:47.140
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 66. CVE-2026-75721｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:16.033)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:16.033 / 2026-09-22T19:05:50.323
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 67. CVE-2026-75703｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:15.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:15.900 / 2026-09-22T19:16:47.037
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 68. CVE-2026-75699｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:15.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:15.760 / 2026-09-22T19:05:50.323
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 69. CVE-2026-75698｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:46.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:46.910 / 2026-09-22T19:23:57.800
- **官方描述（原文）**：Adobe Connect is affected by a reflected Cross-Site Scripting (XSS) vulnerability. An attacker could exploit this vulnerability to inject malicious scripts into a web page, potentially gaining elevated access or control over the victim's account or session. Exploitation of this issue requires user interaction in that a victim must visit a maliciously crafted URL or interact with a compromised web page. Scope is changed.

### 70. CVE-2026-75697｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:46.770)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:46.770 / 2026-09-22T20:17:06.173
- **官方描述（原文）**：Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to inject malicious scripts into vulnerable form fields. Malicious JavaScript may be executed in a victim's browser when they browse to the page containing the vulnerable field, potentially gaining elevated access or control over the victim's account or session. Scope is changed.

### 71. CVE-2026-75689｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:46.643)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:46.643 / 2026-09-22T19:23:57.800
- **官方描述（原文）**：Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to inject malicious scripts into vulnerable form fields. Malicious JavaScript may be executed in a victim's browser when they browse to the page containing the vulnerable field, potentially gaining elevated access or control over the victim's account or session. Scope is changed.

### 72. CVE-2026-75686｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:46.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:46.520 / 2026-09-23T04:17:46.240
- **官方描述（原文）**：Adobe Connect is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue requires user interaction in that a victim must visit a maliciously crafted URL or interact with a compromised web page. Scope is changed.

### 73. CVE-2026-75684｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:46.393)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:46.393 / 2026-09-22T19:23:57.800
- **官方描述（原文）**：Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to inject malicious scripts into vulnerable form fields. Malicious JavaScript may be executed in a victim's browser when they browse to the page containing the vulnerable field, potentially gaining elevated access or control over the victim's account or session. Scope is changed.

### 74. CVE-2026-75682｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:46.260)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:46.260 / 2026-09-23T04:17:45.537
- **官方描述（原文）**：Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary SQL commands, potentially gaining elevated access or control over the victim's account or session. Exploitation of this issue does not require user interaction. Scope is changed.

### 75. CVE-2026-74849｜Zohocorp / ManageEngine ADSelfService Plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T12:17:14.007)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T12:17:14.007 / 2026-09-23T04:17:44.340
- **官方描述（原文）**：Zohocorp ManageEngine ADSelfService Plus versions before build 7001 are vulnerable to a remote code execution vulnerability in the GINA client.

### 76. CVE-2026-73369｜Adobe / Adobe Campaign Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:15.300)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:15.300 / 2026-09-22T19:05:50.323
- **官方描述（原文）**：Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 77. CVE-2026-65113｜NVIDIA / Infrastructure Controller
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T15:17:11.513)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T15:17:11.513 / 2026-09-22T19:37:36.747
- **官方描述（原文）**：NVIDIA Infrastructure Controller for Linux contains a vulnerability where an attacker could cause use of hard-coded credentials. A successful exploit of this vulnerability might lead to escalation of privileges, data tampering, denial of service, and information disclosure.

### 78. CVE-2026-63374｜agronholm / anyio
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:17:50.680)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:17:50.680 / 2026-09-22T16:17:50.680
- **官方描述（原文）**：AnyIO is a high level asynchronous concurrency and networking framework that works on top of either Trio or asyncio. Prior to 4.14.2, connect_tcp() and TLSStream.wrap() can validate internationalized host names after the standard library converts them with IDNA 2003 instead of IDNA 2008. When a connection to a non-ASCII domain is hijacked or redirected, an attacker can obtain a legitimate certificate for the different ASCII hostname produced by IDNA 2003 and present it to the client, causing the malicious endpoint's certificate to validate. This issue is fixed in version 4.14.2.

### 79. CVE-2026-57149｜plone / plone.app.portlets
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:43.893)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:43.893 / 2026-09-22T20:17:03.850
- **官方描述（原文）**：plone.app.portlets.portlets provides a Plone-specific user interface for plone.portlets, as well as a standard set of portlets that ship with Plone. Starting in version 5.0.0 and prior to versions 5.0.8, 6.0.4, and 7.0.2, the Classic portlet (plone.app.portlets.portlets.classic) used its user-supplied template/macro fields to build a TALES path expression that was then evaluated by the TAL path() helper. Because the value was interpreted as a full TALES expression, a user able to add or edit a Classic portlet could supply a crafted value that escapes simple path traversal and is evaluated as arbitrary code. This is exploitable by any authenticated user who can configure a Classic portlet - which, with the default role map, includes regular users on their personal dashboard. The result is code execution in the context of the Plone process, i.e. a privilege escalation across the trust boundary between an authenticated web user and the server-side process. The problem has been patched in `plone.app.portlets` 5.0.8, 6.0.4, and 7.0.2. Some workarounds are available. Restrict who can manage portlets: remove the `plone.app.portlets.ManageOwnPortlets` permission from untrusted roles, and limit Manage portlets to trusted administrators (usually this is already restricted to the Manager and Site Administrator roles). Where the Classic portlet is not needed, unregister it so it cannot be added. This would need to be done by editing a `portlets.xml` in your own code. One may also effectively disable showing the classic portlet by customising its template. In the Zope Management Interface go to the `portal_view_customizations` tool, locate the `classic.pt` template and click it. Click the Customize button. Remove all text and replace it with `<div>The classic portlet was disabled.</div>`. (This is not a recommended way of customizing a template, but in this case it is quite effective.)

### 80. CVE-2026-47116｜LTSecurity / LTK3500SF
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T20:17:03.583)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T20:17:03.583 / 2026-09-22T20:17:03.583
- **官方描述（原文）**：LTSecurity LTK3500SF contains a hard-coded credentials vulnerability where root and guest account passwords are stored as reversible hashes in /etc/shadow, recoverable using dictionary-based cracking tools. Attackers can use the recovered credentials to authenticate via Telnet or SSH and obtain full root-level access to the operating system.

### 81. CVE-2026-43642｜Softaculous / Virtualizor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:14.533)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:14.533 / 2026-09-22T20:43:58.793
- **官方描述（原文）**：Softaculous Virtualizor before 3.2.9 (Patch 9) and 3.0.0 contains a PHP object injection vulnerability in the billing module handler that allows unauthenticated remote attackers to supply arbitrary serialized PHP objects for deserialization by setting the act parameter to login with the from_billing_module parameter present. Attackers can pass malicious serialized data through the billing_data POST field to the unserialize() function without allowed_classes restrictions, enabling exploitation of available POP chains to achieve remote code execution as root.

### 82. CVE-2026-43641｜Softaculous / Virtualizor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:14.357)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:14.357 / 2026-09-22T20:43:58.793
- **官方描述（原文）**：Softaculous Virtualizor before 3.2.9 (Patch 9) and 3.0.0 contains an OS command injection vulnerability in the billing module handler that allows unauthenticated remote attackers to execute arbitrary commands as root by bypassing authentication through specific parameter combinations. Attackers can deserialize a crafted billing_data POST field and inject shell payloads through the uid field, which is passed unmodified to proc_open() via vexec(), yielding complete control of the host and all managed VPS instances.

### 83. CVE-2026-28324｜SolarWinds / Observability Self-Hosted
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T20:17:03.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T20:17:03.250 / 2026-09-22T20:17:03.250
- **官方描述（原文）**：SolarWinds Observability Self-Hosted was found to be affected by an unauthenticated remote code execution vulnerability due to the insufficient integrity checks. Installations configured in a non-default and non-secure configuration are affected.

### 84. CVE-2026-25254｜Qualcomm, Inc. / Snapdragon
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T10:17:08.583)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T10:17:08.583 / 2026-09-22T19:37:36.747
- **官方描述（原文）**：Improper authorization leads to Remote Code Execution via SocketIO interface.

### 85. CVE-2026-19202｜Google / mcp-toolbox-sdk-python
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T22:17:11.707)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T22:17:11.707 / 2026-09-22T22:17:11.707
- **官方描述（原文）**：A caching flaw in the toolbox-core package of the mcp-toolbox-sdk-python SDK causes the same Google ID token to be cached and reused across different audiences. If an application uses the SDK to authenticate to two or more different audiences within the same process, the module-level token cache fails to key its cached tokens by the requested audience. Consequently, a valid, unexpired token minted for a sensitive service (Service A) can be retrieved from the cache and sent to a secondary service (Service B). An attacker who operates, compromises, or monitors traffic to Service B can capture this token and replay it to impersonate the victim application against Service A.

### 86. CVE-2026-18461｜RTI / Connext Professional
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:12.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:12.077 / 2026-09-22T19:37:36.747
- **官方描述（原文）**：Use of Externally-Controlled Format String vulnerability in RTI Connext Professional (Core Libraries) allows Format String Injection. This issue affects Connext Professional: from 7.5.0 before 7.7.0.1, from 7.3.0.10 before 7.3.1.6.

### 87. CVE-2026-18169｜IBM / Financial Transaction Manager (FTM) for RedHat OpenShift
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T23:17:06.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T23:17:06.730 / 2026-09-22T23:17:06.730
- **官方描述（原文）**：IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote authenticated attacker to obtain sensitive information due to improper validation of symbolic links.

### 88. CVE-2026-18163｜IBM / Financial Transaction Manager (FTM) for RedHat OpenShift
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T23:17:06.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T23:17:06.600 / 2026-09-22T23:17:06.600
- **官方描述（原文）**：IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to execute arbitrary code due to improper deserialization of untrusted data.

### 89. CVE-2026-18162｜IBM / Financial Transaction Manager (FTM) for RedHat OpenShift
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T23:17:06.463)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T23:17:06.463 / 2026-09-22T23:17:06.463
- **官方描述（原文）**：IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to execute arbitrary code due to improper neutralization of user-controlled input within the new Function constructor.

### 90. CVE-2026-17645｜IBM / Financial Transaction Manager (FTM) for RedHat OpenShift
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T22:17:08.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T22:17:08.730 / 2026-09-22T22:17:08.730
- **官方描述（原文）**：IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote authenticated attacker to gain elevated privileges due to improper privilege management.

### 91. CVE-2026-17635｜IBM / Financial Transaction Manager (FTM) for RedHat OpenShift
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T22:17:08.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T22:17:08.077 / 2026-09-22T22:17:08.077
- **官方描述（原文）**：IBM Financial Transaction Manager (FTM) for RedHat OpenShift could allow a remote attacker to perform unauthorized actions due to improper configuration of HTTP method-based security constraints.

### 92. CVE-2026-17472｜IBM / Concert
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T22:17:07.683)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T22:17:07.683 / 2026-09-22T22:17:07.683
- **官方描述（原文）**：IBM Concert 1.0.0 through 3.0.0 could allow a remote authenticated attacker to access or modify unauthorized resources due to the use of wildcards in RBAC permission definitions.

### 93. CVE-2026-16346｜IBM / DataStage on Cloud Pak for Data
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T22:17:06.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T22:17:06.607 / 2026-09-22T22:17:06.607
- **官方描述（原文）**：IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands due to improper neutralization of special elements used in an OS command.

### 94. CVE-2026-12718｜Karel Electronic Industry and Trade Inc. / KarelIPS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T14:17:12.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T14:17:12.490 / 2026-09-22T19:07:00.983
- **官方描述（原文）**：Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Karel Electronic Industry and Trade Inc. KarelIPS allows Blind SQL Injection. This issue affects KarelIPS: through 22092026. NOTE: The vendor was contacted and it was learned that the product is not supported.

### 95. CVE-2016-15059｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T08:16:34.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T08:16:34.520 / 2026-09-22T19:07:00.983
- **官方描述（原文）**：Net::IDN::Punycode versions before 2.301 for Perl allow a heap buffer overflow via unchecked writes past the output buffer in encode_punycode. The XS backend builds the encoded label in the string buffer of the scalar it returns, sized from the input length. The loop that emits the digits of each code point checks for room before every write, but the write of the last digit of each round and the write of the terminating NUL do not, so an input whose encoded form fills the buffer writes past its end. Only the XS backend is affected. Encoding an attacker-supplied string corrupts the heap.

### 96. CVE-2026-95656｜dgtlmoon / changedetection.io
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:36.947)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:36.947 / 2026-09-22T19:04:55.677
- **官方描述（原文）**：A vulnerability was found in dgtlmoon changedetection.io up to 50389b07. This vulnerability affects the function add_watch_ui_snapshot of the file changedetectionio/blueprint/add_watch_ui/__init__.py of the component Preview Endpoint. Performing a manipulation of the argument url results in server-side request forgery. The attack can be initiated remotely. The exploit has been made public and could be used. Upgrading to version 0.60.1 is able to resolve this issue. The patch is named 71d332d5a0d3da2a0fe89a392413bf4b7d27c84e. The affected component should be upgraded. Was fixed upstream.

### 97. CVE-2026-95271｜dgtlmoon / changedetection.io
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T13:17:12.767)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T13:17:12.767 / 2026-09-22T19:04:55.677
- **官方描述（原文）**：A vulnerability has been found in dgtlmoon changedetection.io up to 0.60.7. The impacted element is the function check_authentication of the file changedetectionio/flask_app.py of the component Authentication Hook. Such manipulation leads to improper authentication. The attack may be performed from remote. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 98. CVE-2026-90462｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:08.137)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:08.137 / 2026-09-22T19:37:36.747
- **官方描述（原文）**：A flaw was found in SSSD. When configured with the LDAP access provider and `ldap_access_order` including `ppolicy` or `lockout`, a fail-open condition in the LDAP ppolicy access check can occur if a user lookup returns zero results. This can incorrectly return success and cache an allow decision, permitting continued authorization for a deleted or deprovisioned user. A remote attacker with prior valid account context could exploit this to maintain access to information and potentially make limited modifications to resources that should no longer be available.

### 99. CVE-2026-86062｜HKUDS / LightRAG
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T17:17:27.863)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T17:17:27.863 / 2026-09-22T19:16:54.870
- **官方描述（原文）**：LightRAG provides simple and fast retrieval-augmented generation. Prior to 1.5.5, lightrag_webui/src/components/retrieval/ChatMessage.tsx renders answer and thinking content with react-markdown, rehypeRaw, and skipHtml=false without an HTML sanitizer. An attacker who can add a document can store raw HTML that is returned through the query path and rendered as active content by MessageMarkdown. A user who later retrieves the content can execute attacker-controlled JavaScript through elements such as an iframe srcdoc; the additional Mermaid securityLevel: loose rendering path also injects generated SVG through innerHTML. The script runs in the LightRAG WebUI origin and can read the API token in localStorage and perform API actions as the victim. This issue is fixed in version 1.5.5.

### 100. CVE-2026-86056｜notepad-plus-plus / notepad-plus-plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:24.087)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:24.087 / 2026-09-22T18:17:24.087
- **官方描述（原文）**：Notepad++ is a free and open-source source code editor. Prior to 8.9.8, the NPPM_SAVESESSION handler in PowerEditor/src/NppBigSwitch.cpp converts lParam to a sessionInfo pointer and dereferences its nbFile, files, and sessionFilePathName members without checking for null. A process running at the same or a higher Windows integrity level on the same desktop can send NPPM_SAVESESSION with a null lParam, immediately terminating Notepad++ and causing denial of service and loss of unsaved documents. This issue is fixed in version 8.9.8.

### 101. CVE-2026-85709｜HKUDS / LightRAG
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T17:17:27.020)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T17:17:27.020 / 2026-09-22T19:16:54.750
- **官方描述（原文）**：LightRAG provides simple and fast retrieval-augmented generation. Prior to 1.5.5, the LightRAG API server returns raw Python exception text from error handlers in document_routes.py, graph_routes.py, query_routes.py, ollama_api.py, and lightrag_server.py. The detail=str(e), detail=str(exc), and equivalent formatted-message paths expose server filesystem paths, database host, port, user, and database names, language-model provider diagnostics, configuration details, and Python library internals to a network client that can trigger an error. The default unauthenticated configuration makes those responses reachable without credentials, and URI-configured backends can disclose connection strings containing credentials depending on the underlying driver error. This issue is fixed in version 1.5.5.

### 102. CVE-2026-83600｜netdata / netdata
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T17:17:26.103)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T17:17:26.103 / 2026-09-22T19:16:53.760
- **官方描述（原文）**：Netdata is an open source observability tool. Prior to 2.10.4, an authenticated child agent can send an oversized CHART SLOT value that str2ull_encoded passes to pluginsd_rrdset_cache_put_to_slot in src/plugins.d/pluginsd_internals.h. The accepted slot drives reallocz to request an approximately 16 GiB chart-pointer array, and allocation failure invokes fatal and aborts the parent Netdata agent, repeatedly disabling centralized monitoring while stream access persists. This issue is fixed in version 2.10.4 and nightly build 2.10.0-782-nightly.

### 103. CVE-2026-81879｜radareorg / radare2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:02.617)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:02.617 / 2026-09-22T16:18:02.617
- **官方描述（原文）**：radare2 is a UNIX-like reverse engineering framework and command-line toolset. Prior to 6.2.0, radare2's ELF PN_XNUM handling was vulnerable because the ELF parser allocated the program-header array using the resolved PN_XNUM count but several consumers still iterated with the original e_phnum value of 65535. The vulnerability is triggered by processing a crafted ELF file with e_phnum = 0xffff and a much smaller resolved count in shdr[0].sh_info. Consumers iterated beyond the allocated program-header array. This can cause a heap out-of-bounds read and process termination, resulting in denial of service; memory disclosure and code execution have not been demonstrated. This issue is fixed in version 6.2.0.

### 104. CVE-2026-81878｜radareorg / radare2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:02.457)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:02.457 / 2026-09-22T18:17:20.517
- **官方描述（原文）**：radare2 is a UNIX-like reverse engineering framework and command-line toolset. Prior to 6.2.0, radare2's CPython bytecode .pyc marshal parser was vulnerable because the CPython marshal readers accepted a 32-bit string length without rejecting values that overflow the size-plus-one allocation. The vulnerability is triggered by opening or inspecting a crafted .pyc file through r2 or rabin2. A length of 0xffffffff wrapped the allocation to zero before the common byte reader wrote attacker-controlled data and fill bytes beyond the heap allocation. This can cause heap memory corruption and denial of service; arbitrary code execution is possible but has not been demonstrated. This issue is fixed in version 6.2.0.

### 105. CVE-2026-77270｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:18.947)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:18.947 / 2026-09-22T19:16:51.067
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, the Jira and Confluence attachment upload tools treat caller-controlled file_path values as trusted server-local paths. The server opens the selected file and uploads it to an Atlassian issue or page, allowing an MCP caller with upload access to disclose any file readable by the server process. The advisory traces the vulnerable input and processing flow through confluence_upload_attachment, jira_upload_attachment, file_path, and open(file_path, "rb"), which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 106. CVE-2026-77266｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T19:16:50.627)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:50.627 / 2026-09-22T20:17:08.080
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, upload_attachment accepts absolute paths and traversal sequences without constraining the resolved path to the server workspace. An MCP caller with attachment access can read a chosen server-local file and exfiltrate it through Jira or Confluence. The advisory traces the vulnerable input and processing flow through upload_attachment, file_path, and path traversal, which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 107. CVE-2026-77250｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:17.720)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:17.720 / 2026-09-22T19:16:49.427
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, OAuthConfig writes a plaintext fallback file containing access and refresh tokens under the user's .mcp-atlassian directory using process-default permissions. On systems with a permissive umask, same-group or other local users and processes can read the persisted tokens and reuse the associated Atlassian access. The advisory traces the vulnerable input and processing flow through OAuthConfig._save_tokens, ~/.mcp-atlassian/oauth-<client_id>.json, access_token, and refresh_token, which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 108. CVE-2026-75510｜novuhq / novu
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:17:53.950)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:17:53.950 / 2026-09-22T16:17:53.950
- **官方描述（原文）**：Novu provides an API for sending notifications through multiple channels. Prior to 3.18.0, Novu's @novu/js In-App Inbox and the @novu/react Inbox component accept a notification call-to-action redirect.url from the v1 cta.data object and pass it through apps/api/src/app/inbox/utils/notification-mapper.ts and packages/js/src/ui/components/Notification/DefaultNotification.tsx to the navigate function in packages/js/src/ui/context/InboxContext.tsx without validating its URL scheme. An authenticated organization member or environment API-key holder can store a javascript: redirect with target _self in an in-app workflow. When a recipient using a Chromium-based browser clicks the notification, window.open executes the redirect in the current inbox-hosting origin, which can expose session material and permit authenticated actions in a customer application or the self-hosted Novu dashboard. This issue is fixed in version 3.18.0.

### 109. CVE-2026-56682｜decolua / 9router
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T17:17:24.290)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T17:17:24.290 / 2026-09-22T18:17:15.100
- **官方描述（原文）**：9Router is an AI router & token saver. Prior to 0.5.6, 9Router deployments that allow requests to reach Next.js without the sanitizing custom-server.js wrapper use the client-supplied X-9r-Real-Ip value as the bucket key in getClientIp, checkLock, and recordFail in src/lib/auth/loginLimiter.js for POST /api/auth/login. A remote unauthenticated attacker can rotate the header on every password guess so each request uses a new failed-attempt bucket and the five-attempt progressive lockout never returns HTTP 429. This permits unthrottled password guessing against the dashboard login and can lead to an administrative session if the password is recovered. This issue is fixed in version 0.5.6.

### 110. CVE-2026-95660｜Moonshot AI / Kimi Code
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T18:17:37.750)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:37.750 / 2026-09-22T19:16:59.953
- **官方描述（原文）**：A security flaw has been discovered in Moonshot AI Kimi Code up to 0.31.0. The affected element is an unknown function of the file agent-core-v2/src/agent/mcp/config-loader.ts of the component MCP Configuration Loader. The manipulation results in os command injection. The attack may be launched remotely. The exploit has been released to the public and may be used for attacks. Upgrading to version 0.31.1 is sufficient to fix this issue. It is recommended to upgrade the affected component. Beyond the trust prompt, the fix resolves fd/stty binaries to absolute paths specifically "so untrusted workspaces cannot plant bare-name executables before confirmation," fixing a secondary $PATH path-planting vector alongside the primary untrusted-.mcp.json auto-spawn.

### 111. CVE-2026-95501｜mtrano / APENCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T15:17:25.450)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T15:17:25.450 / 2026-09-22T19:16:59.807
- **官方描述（原文）**：A vulnerability was found in mtrano APENCMS up to 6546096d354153309693efabb9a0d824628ed4f5. The affected element is the function eval of the file cms/weasel.php of the component Template Engine. The manipulation of the argument $_CMS['site'] results in code injection. The attack may be performed from remote. The exploit has been made public and could be used. This product utilizes a rolling release system for continuous delivery, and as such, version information for affected or updated releases is not disclosed. The vendor was contacted early about this disclosure but did not respond in any way.

### 112. CVE-2026-95273｜dgtlmoon / changedetection.io
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T13:17:13.123)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T13:17:13.123 / 2026-09-22T19:04:55.677
- **官方描述（原文）**：A vulnerability was determined in dgtlmoon changedetection.io up to 0.60.7. This impacts the function static_content of the file changedetectionio/flask_app.py of the component visual_selector_data. Executing a manipulation of the argument filename can lead to path traversal. It is possible to launch the attack remotely. The exploit has been publicly disclosed and may be utilized. Distinct from CVE-2026-25527, which fixed a different parameter (group) in the same function. The vendor was contacted early about this disclosure but did not respond in any way.

### 113. CVE-2026-95272｜dgtlmoon / changedetection.io
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T13:17:12.950)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T13:17:12.950 / 2026-09-22T19:04:55.677
- **官方描述（原文）**：A vulnerability was found in dgtlmoon changedetection.io up to 0.60.7. This affects the function static_content of the file changedetectionio/flask_app.py of the component Screenshot Handler. Performing a manipulation of the argument filename results in path traversal. It is possible to initiate the attack remotely. The attack is considered to have high complexity. The exploitability is reported as difficult. The exploit has been made public and could be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 114. CVE-2026-95270｜dgtlmoon / changedetection.io
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T12:17:14.557)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T12:17:14.557 / 2026-09-22T19:04:55.677
- **官方描述（原文）**：A flaw has been found in dgtlmoon changedetection.io up to 0.60.7. The affected element is the function check_password of the file changedetectionio/flask_app.py of the component Hash Comparison. This manipulation of the argument Password causes observable timing discrepancy. The attack is possible to be carried out remotely. A high degree of complexity is needed for the attack. The exploitability is described as difficult. The exploit has been published and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 115. CVE-2026-86698｜hexpm / hexpm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:05.993)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:05.993 / 2026-09-22T19:16:54.993
- **官方描述（原文）**：Insufficient Session Expiration vulnerability in OAuth token issuance in hexpm hexpm allows a user whose organization membership or session has ended to keep reading the organization's private packages and their documentation tarballs via a retained refresh token. generate_refresh_token/4 in lib/hexpm/oauth/jwt.ex signs the refresh token with the same iss, aud and scope claims as the access token, so it carries the same repository:<org> scopes. The CDN service that serves private repositories verifies the signature and time claims and then authorizes from the scope claim, with no database lookup and no way to tell the two token kinds apart. Removing a member or revoking a session therefore takes effect at the CDN only when the 30 day refresh token expires, instead of after the 30 minute access token lifetime. Access is read-only and limited to organizations the account belonged to when the token was granted. This issue affects hex.pm: from 2025-10-10 before 2026-09-22.

### 116. CVE-2026-81884｜radareorg / radare2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:03.347)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 2.5 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:03.347 / 2026-09-22T16:18:03.347
- **官方描述（原文）**：radare2 is a UNIX-like reverse engineering framework and command-line toolset. Prior to 6.2.0, radare2's Mach-O LC_DATA_IN_CODE parser was vulnerable because the Mach-O LC_DATA_IN_CODE parser trusted dataoff and datasize and allowed a final partial record to be processed. The vulnerability is triggered by opening a crafted Mach-O file while the non-default bin.verbose option is enabled. When datasize was not a multiple of data_in_code_entry, the last iteration read beyond the allocated buffer. This can cause a heap out-of-bounds read and possible process termination; no attacker-observable memory disclosure has been demonstrated. This issue is fixed in version 6.2.0.

### 117. CVE-2026-81883｜radareorg / radare2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-22T16:18:03.200)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T16:18:03.200 / 2026-09-22T17:17:25.560
- **官方描述（原文）**：radare2 is a UNIX-like reverse engineering framework and command-line toolset. Prior to 6.2.0, radare2's Lua 5.3 bytecode function parser was vulnerable because the Lua 5.3 bytecode function parser read fixed function-metadata fields immediately after a function-name string without checking the remaining buffer length. The vulnerability is triggered by opening or inspecting a crafted Lua 5.3 bytecode file whose function-name string ends at the input-buffer boundary. The parser read two integers and three one-byte fields beyond the allocated input buffer. This can cause invalid parser results or process termination; no attacker-observable memory disclosure has been demonstrated. This issue is fixed in version 6.2.0.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-94127｜F5 / BIG-IP APM
- **Title**：F5 BIG-IP APM Heap-based Buffer Overflow Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：F5 BIG-IP APM contains a heap-based buffer overflow vulnerability when access policy and an OAuth profile are configured on a virtual server. This vulnerability could allow an unauthenticated attacker to perform remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-93952｜Arista / VeloCloud Orchestrator
- **Title**：Arista VeloCloud Orchestrator Improper Input Validation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Arista VeloCloud Orchestrator (VCO) on-prem contains an improper input validation vulnerability that may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-93616｜Check Point / Multiple Products
- **Title**：Check Point Multiple Products Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Check Point Security Management Server, Multi-Domain Security Management Server, Log Server, Multi-Domain Log Server, and SmartEvent contain a path traversal vulnerability that allows an unauthenticated attacker to upload and execute arbitrary scripts.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-85102｜Check Point / Multiple Products
- **Title**：Check Point Multiple Products Improper Certificate Validation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00329 / percentile=0.26293
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Check Point Security Gateway and Check Point Spark Firewall using Site to Site VPN or Remote Access VPN contain an improper certificate validation vulnerability which could allow an unauthenticated remote attacker to execute arbitrary code on the Gateway.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-95675 | P3 / 38 | D-LINK / DAP-1360 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93088 | P3 / 38 | SGLang / SGLang | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91130 | P3 / 38 | home-assistant / core | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-86059 | P3 / 38 | Dokploy / dokploy | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77254 | P3 / 38 | sooperset / mcp-atlassian | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-94462 | WATCH / 30 | spree / spree | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89420 | WATCH / 30 | ZenHive / mpp | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89407 | WATCH / 30 | FasterXML / jackson-core | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88419 | WATCH / 30 | 未確認 / 未確認 | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-85279 | WATCH / 30 | notepad-plus-plus / notepad-plus-plus | v3.1 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77274 | WATCH / 30 | sooperset / mcp-atlassian | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77256 | WATCH / 30 | sooperset / mcp-atlassian | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77253 | WATCH / 30 | sooperset / mcp-atlassian | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77247 | WATCH / 30 | sooperset / mcp-atlassian | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77243 | WATCH / 30 | sooperset / mcp-atlassian | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77242 | WATCH / 30 | sooperset / mcp-atlassian | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-75607 | WATCH / 30 | blakeblackshear / frigate | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63104 | WATCH / 30 | usekaneo / kaneo | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-59991 | WATCH / 30 | psd-tools / psd-tools | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-13087 | WATCH / 30 | Red Hat / Red Hat Enterprise Linux 10 | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-96257 | WATCH / 28 | Fast / FAC1203R Gigabit Edition | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-95654 | WATCH / 28 | David-Crty / Databasement | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-94456 | WATCH / 28 | GitroomHQ / postiz-app | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93556 | WATCH / 28 | Kompini / Tankuam Places | v4.0 9.3 (CRITICAL) | 0.00305 / percentile=0.23439 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-89422 | WATCH / 28 | Erlang / OTP | v4.0 9.3 (CRITICAL) | 0.00368 / percentile=0.30701 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-89276 | WATCH / 28 | Adobe / Adobe Campaign Classic | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：1；缺少 Product：1；缺少 Title：26。
- EPSS 未確認：27；Exploitation status 未確認：2。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-23T05:23:24.189900+00:00`；Delta generated at：`2026-09-23T05:23:24.189900+00:00`。

---

## 可驗證資料來源

- **CVE-2026-94127** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94127) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (my.f5.com)](https://my.f5.com/manage/s/article/K000162605) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-93952** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93952) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (arista.com)](https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-93616** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93616) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (support.checkpoint.com)](https://support.checkpoint.com/results/sk/sk1000171/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85102** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85102) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85102) · [Vendor / Advisory (support.checkpoint.com)](https://support.checkpoint.com/results/sk/sk1000117) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-95675** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95675)
- **CVE-2026-93088** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93088)
- **CVE-2026-91130** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91130)
- **CVE-2026-86059** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86059)
- **CVE-2026-77254** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77254)
- **CVE-2026-94462** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94462)
- **CVE-2026-89420** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89420)
- **CVE-2026-89407** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89407)
- **CVE-2026-88419** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88419)
- **CVE-2026-85279** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85279)
- **CVE-2026-77274** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77274)
- **CVE-2026-77256** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77256)
- **CVE-2026-77253** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77253)
- **CVE-2026-77247** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77247)
- **CVE-2026-77243** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77243)
- **CVE-2026-77242** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77242)
- **CVE-2026-75607** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75607)
- **CVE-2026-63104** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63104)
- **CVE-2026-59991** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59991)
- **CVE-2026-13087** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13087)
- **CVE-2026-96257** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96257)
- **CVE-2026-95654** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95654)
- **CVE-2026-94456** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94456)
- **CVE-2026-93556** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93556) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93556)
- **CVE-2026-89422** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89422) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89422)
- **CVE-2026-89276** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89276)
- **CVE-2026-89275** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89275)
- **CVE-2026-87121** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87121)
- **CVE-2026-87080** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87080) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87080)
- **CVE-2026-87078** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87078) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87078)
- **CVE-2026-85734** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85734)
- **CVE-2026-84412** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84412)
- **CVE-2026-84388** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84388)
- **CVE-2026-83660** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83660)
- **CVE-2026-82443** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82443)
- **CVE-2026-82013** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82013)
- **CVE-2026-82011** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82011)
- **CVE-2026-82010** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82010)
- **CVE-2026-82009** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82009)
- **CVE-2026-82008** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82008)
- **CVE-2026-82000** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82000)
- **CVE-2026-81995** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81995)
- **CVE-2026-80156** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80156)
- **CVE-2026-80155** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80155)
- **CVE-2026-80152** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80152)
- **CVE-2026-80151** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80151)
- **CVE-2026-80147** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80147)
- **CVE-2026-80146** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80146)
- **CVE-2026-80145** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80145)
- **CVE-2026-80144** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80144)
- **CVE-2026-80143** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80143)
- **CVE-2026-79313** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79313)
- **CVE-2026-7866** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-7866)
- **CVE-2026-77987** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77987)
- **CVE-2026-77621** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77621)
- **CVE-2026-77244** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77244)
- **CVE-2026-76709** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76709)
- **CVE-2026-76708** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76708)
- **CVE-2026-75745** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75745)
- **CVE-2026-75728** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75728)
- **CVE-2026-75723** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75723)
- **CVE-2026-75721** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75721)
- **CVE-2026-75703** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75703)
- **CVE-2026-75699** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75699)
- **CVE-2026-75698** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75698)
- **CVE-2026-75697** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75697)
- **CVE-2026-75689** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75689)
- **CVE-2026-75686** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75686)
- **CVE-2026-75684** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75684)
- **CVE-2026-75682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75682)
- **CVE-2026-74849** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-74849)
- **CVE-2026-73369** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73369)
- **CVE-2026-65113** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65113)
- **CVE-2026-63374** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63374)
- **CVE-2026-57149** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57149)
- **CVE-2026-47116** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47116)
- **CVE-2026-43642** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-43642)
- **CVE-2026-43641** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-43641)
- **CVE-2026-28324** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-28324)
- **CVE-2026-25254** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-25254)
- **CVE-2026-19202** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19202)
- **CVE-2026-18461** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18461)
- **CVE-2026-18169** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18169)
- **CVE-2026-18163** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18163)
- **CVE-2026-18162** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18162)
- **CVE-2026-17645** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17645)
- **CVE-2026-17635** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17635)
- **CVE-2026-17472** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17472)
- **CVE-2026-16346** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16346)
- **CVE-2026-12718** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12718)
- **CVE-2016-15059** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-15059)
- **CVE-2026-95656** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95656)
- **CVE-2026-95271** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95271)
- **CVE-2026-90462** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90462)
- **CVE-2026-86062** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86062)
- **CVE-2026-86056** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86056)
- **CVE-2026-85709** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85709)
- **CVE-2026-83600** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83600)
- **CVE-2026-81879** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81879)
- **CVE-2026-81878** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81878)
- **CVE-2026-77270** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77270)
- **CVE-2026-77266** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77266)
- **CVE-2026-77250** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77250)
- **CVE-2026-75510** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75510)
- **CVE-2026-56682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56682)
- **CVE-2026-95660** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95660)
- **CVE-2026-95501** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95501)
- **CVE-2026-95273** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95273)
- **CVE-2026-95272** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95272)
- **CVE-2026-95270** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95270)
- **CVE-2026-86698** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86698)
- **CVE-2026-81884** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81884)
- **CVE-2026-81883** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81883)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
