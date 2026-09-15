# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**106** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=106、NEW_KEV=1。
- Intelligence 候選：**30** 筆；P1 **1**、P2 **0**、P3 **7**、WATCH **22**。
- Baseline：state / generated_at=2026-09-14T05:34:43.748576+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-76461。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **106** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-76461｜Cisco / Secure Email Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:51.113)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-14 / due_date=2026-09-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-14T17:17:51.113 / 2026-09-15T04:18:15.100
- **官方描述（原文）**：Cisco AsyncOS software for Cisco Secure Email Gateway (SEG) contains a SQL injection vulnerability that could allow an unauthenticated, remote attacker to execute arbitrary commands with root privileges on the underlying operating system.

### 2. CVE-2026-90942｜casdoor / casdoor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T18:20:28.720)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T18:20:28.720 / 2026-09-14T19:18:13.480
- **官方描述（原文）**：Casdoor through 4.4.0 fails to properly mask the instance-wide built-in certificate private key in /api/get-certs and /api/get-cert endpoints, allowing organization administrators to retrieve it. Attackers can use the exposed private key to forge JWT tokens for any user in any organization, including global administrators.

### 3. CVE-2026-90919｜ModelTC / LightLLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T12:17:51.807)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T12:17:51.807 / 2026-09-14T15:17:13.630
- **官方描述（原文）**：LightLLM through 1.2.0 contains a remote code execution vulnerability in the Config Server's unauthenticated /visual_register WebSocket endpoint that passes the first client frame directly to pickle.loads(). Attackers can reach the Config Server port and send a malicious serialized payload with a __reduce__ method to execute arbitrary code with Config Server process privileges.

### 4. CVE-2026-61534｜confetti / yayson
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:16.847)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:16.847 / 2026-09-14T20:16:48.813
- **官方描述（原文）**：Yayson is a library for serializing and reading JSON API data in JavaScript. Prior to 4.3.0, Store and LegacyStore use attacker-controlled JSON:API type, id, and relationship names as keys in plain-object lookup tables in src/yayson/store.ts and src/yayson/legacy-store.ts. A document whose type is __proto__ causes model-cache writes to modify Object.prototype, with the attacker controlling the polluted property name through id and its value through attributes. The malicious type can also be supplied by an included resource, and LegacyStore is reachable when a configured types mapping resolves to __proto__. Unsafe relationship names including __proto__, constructor, and prototype provide additional document-derived member paths. The resulting process-wide prototype pollution can cause denial of service and logic corruption; authorization bypass or code execution depends on suitable gadgets in the consuming application. This issue is fixed in version 4.3.0.

### 5. CVE-2026-57131｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:14.710)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:14.710 / 2026-09-14T17:17:48.970
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to 4.6.58, praisonai.jobs.server.create_app mounts praisonai.jobs.router.create_router under /api/v1/runs without authentication or per-job authorization. Network clients can submit attacker-controlled prompts and agent configuration, list and read jobs, stream results, and cancel or delete other jobs, exposing service credentials and connected tool capabilities to unauthorized agent execution. This vulnerability is fixed in 4.6.58.

### 6. CVE-2026-57127｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:13.557)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:13.557 / 2026-09-14T17:17:48.840
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to 4.6.58, recipe serve installs APIKeyAuthMiddleware or JWTAuthMiddleware when an operator selects api-key or JWT authentication, but each middleware forwards requests when PRAISONAI_API_KEY or PRAISONAI_JWT_SECRET and the corresponding recipe value are absent. Unauthenticated clients can then reach recipe execution, input, and output surfaces and may trigger connected tools despite the operator explicitly enabling authentication. This issue is fixed in 4.6.58.

### 7. CVE-2026-57125｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:05.900)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:05.900 / 2026-09-14T20:16:48.303
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to praisonai 4.6.59 and praisonaiagents 1.6.59, the unauthenticated POST /api/v1/runs Jobs API accepts attacker-controlled agent_yaml, and the approve field can mark execute_command as YAML-approved before @require_approval checks critical tools. This chain allows a remote caller to cause a configured language model agent to invoke arbitrary operating-system commands without credentials or operator interaction. This vulnerability is fixed in praisonai 4.6.59 and praisonaiagents 1.6.59 as fixed versions.

### 8. CVE-2026-57124｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:13.417)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:13.417 / 2026-09-14T19:17:35.167
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to 4.6.59, the default UI host applications expose POST /api/mcp/connect without mandatory authentication and accept caller-controlled command and args values that PraisonAIUI passes to StdioMCPClient to start a local process. Because the UI commands bind to 0.0.0.0 by default, a reachable unauthenticated client can execute commands as the UI service account even when the MCP handshake later fails. This vulnerability is fixed in 4.6.59.

### 9. CVE-2026-91080｜adnanh / webhook
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T18:20:29.760)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T18:20:29.760 / 2026-09-14T19:18:14.500
- **官方描述（原文）**：webhook through 2.8.3 reads the entire request body into memory before evaluating trigger rules, allowing unauthenticated attackers to exhaust memory by sending oversized bodies. Attackers can send multi-gigabyte request bodies with invalid signatures to trigger out-of-memory conditions and crash the service.

### 10. CVE-2026-90946｜AsyncFuncAI / deepwiki-open
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T18:20:29.180)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T18:20:29.180 / 2026-09-14T19:18:13.990
- **官方描述（原文）**：DeepWiki-Open through commit d92819a contains an arbitrary file read vulnerability in the unauthenticated /ws/chat WebSocket endpoint that accepts repo_url as a filesystem path with no containment. Attackers can supply arbitrary directory paths to read all files with supported extensions including Python, JavaScript, YAML, and JSON files containing hardcoded secrets and credentials.

### 11. CVE-2026-90944｜krayin / laravel-crm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T18:20:28.877)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T18:20:28.877 / 2026-09-14T21:17:43.157
- **官方描述（原文）**：Krayin CRM through 2.2.6 exposes the POST /admin/mail/inbound-parse endpoint without authentication, allowing unauthenticated attackers to inject arbitrary emails into the CRM inbox. Attackers can supply crafted RFC 2822 messages with forged sender information and headers to insert emails with any subject and body, including replies to existing conversation threads.

### 12. CVE-2026-90939｜201206030 / novel-plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T14:17:20.240)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T14:17:20.240 / 2026-09-14T15:17:14.117
- **官方描述（原文）**：novel-plus through 5.3.3 contains an information disclosure vulnerability in the /sys/user/list endpoint that lacks proper permission annotations. Authenticated attackers can retrieve password hashes and personal data including email addresses and phone numbers for users within their data scope, enabling offline hash cracking and account takeover.

### 13. CVE-2026-90938｜langbot-app / LangBot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:19:32.430)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:19:32.430 / 2026-09-14T14:17:20.117
- **官方描述（原文）**：LangBot's plugin runtime (pip package langbot_plugin) through 0.4.17 starts a debug WebSocket server on 0.0.0.0:5401 (/plugin/ws) whose authentication is gated on plugin_debug_key, which defaults to an empty string and is never set by the upstream repository, Docker image, or docker-compose (which additionally publishes port 5401 to the host); the key check is therefore skipped entirely. Any remote attacker able to reach the port can register an arbitrary "debug plugin" without credentials. Because events are broadcast to all initialized plugins without filtering, the attacker's plugin receives the full context of every IM message event (including private chats, message chains, and user/sender IDs in plaintext) and can inject forged replies, send messages as any configured bot, enumerate bot UUIDs, invoke configured LLM models, read knowledge-base contents, and register malicious tools that feed every user's LLM pipeline. Registering with "prod_mode": true causes later legitimate installations of a plugin with the same author/name to be rejected, resulting in persistent denial of service. No patched version was available at the time of publication.

### 14. CVE-2026-90933｜laradashboard / laradashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:19:31.680)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:19:31.680 / 2026-09-14T14:17:19.997
- **官方描述（原文）**：laradashboard through 1.2.2 contains a missing authorization vulnerability in the Local License API endpoints that allows any authenticated user to read, overwrite, and delete premium module license keys. Attackers with low-privileged accounts can access GET /api/admin/licenses/show, POST /api/admin/licenses/store, and POST /api/admin/licenses/remove endpoints to disclose confidential license keys, inject attacker-controlled values, or delete stored licenses entirely.

### 15. CVE-2026-90930｜filebrowser / filebrowser
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:19:31.190)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:19:31.190 / 2026-09-14T15:17:13.793
- **官方描述（原文）**：File Browser through 2.63.23 applies path rules to the requested lexical path but resolves symbolic links without reapplying rules to the target, allowing authenticated users to bypass deny rules. Attackers can read and overwrite rule-denied files by accessing them through in-scope symbolic link aliases that resolve to denied paths.

### 16. CVE-2026-90928｜filebrowser / filebrowser
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:19:30.870)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:19:30.870 / 2026-09-14T14:17:19.880
- **官方描述（原文）**：File Browser through 2.63.23 contains a memory exhaustion vulnerability in the subtitle conversion endpoint that loads entire subtitle files into memory without size limits. Authenticated attackers with download permission can request conversion of large .srt, .ass, or .ssa files and exhaust server memory through concurrent requests, causing denial of service.

### 17. CVE-2026-90699｜D-Link / DWR-M920
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T09:17:02.530)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：0.01593 / percentile=0.74312
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T09:17:02.530 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A weakness has been identified in D-Link DWR-M920 1.1.7. This issue affects the function sub_41E60C of the file /boafrm/formPinManageSetup. This manipulation of the argument newPin causes os command injection. The attack can be initiated remotely. The exploit has been made available to the public and could be used for attacks.

### 18. CVE-2026-77884｜Brain Trust / Gallery - Private Photo Vault
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T19:17:44.700)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T19:17:44.700 / 2026-09-14T19:17:44.700
- **官方描述（原文）**：Gallery - Private Photo Vault 1.0.41 starts an unauthenticated HTTP server that is reachable from the local network. The server listens on TCP port 8080 and serves files and directory listings from Android external storage.

### 19. CVE-2026-70658｜pay-rails / pay
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T18:19:45.213)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T18:19:45.213 / 2026-09-14T19:17:40.293
- **官方描述（原文）**：Pay is a payments engine for Ruby on Rails 6.0 and higher. Prior to 11.6.2, Pay::Webhooks::PaddleBillingController#valid_signature? in app/controllers/pay/webhooks/paddle_billing_controller.rb compares the computed 64-character SHA-256 HMAC with the attacker-controlled h1 token from the Paddle-Signature header using Ruby String#==. An unauthenticated remote attacker who can repeatedly submit requests to /pay/webhooks/paddle_billing and obtain sufficiently precise timing measurements can infer matching digest prefixes and recover a valid signature. A forged accepted webhook is enqueued through Pay::Webhooks::ProcessJob and can cause a host application to update billing state, provision paid features, record refunds, or trigger customer notifications. This issue is fixed in version 11.6.2.

### 20. CVE-2026-57579｜AlchemyCMS / alchemy_cms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:49.267)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T17:17:49.267 / 2026-09-14T18:17:58.063
- **官方描述（原文）**：Alchemy is an open source content management system engine written in Ruby on Rails. Prior to 7.4.15, 8.0.15, 8.1.14, and 8.2.6, the unauthenticated GET /api/pages/nested endpoint implemented by Api::PagesController#nested in app/controllers/alchemy/api/pages_controller.rb returns an unfiltered page tree because it performs no authorization and does not scope descendants by the caller's ability. Anonymous callers can retrieve restricted and unpublished page metadata that the sibling show action denies. When elements=true is supplied, PageTreeSerializer also returns element and ingredient content from restricted pages because PageTreePreloader and the serializer do not apply an ability check to those records. This issue is fixed in versions 7.4.15, 8.0.15, 8.1.14, and 8.2.6.

### 21. CVE-2026-57130｜MervinPraison / praisonaiagents
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:06.453)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:06.453 / 2026-09-14T15:17:06.453
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to praisonaiagents 1.6.59, src/praisonai-agents/praisonaiagents/tools/email_tools.py interpolates LLM-controlled from_addr, subject, and query values directly into quoted IMAP SEARCH criteria. Embedded quote, backslash, newline, or null characters can escape the intended criterion and alter IMAP operations when search_emails, reply_email, or archive_email is exposed to an agent with configured email credentials, allowing mailbox data access, modification, deletion, or connection disruption. This issue is fixed in praisonaiagents 1.6.59.

### 22. CVE-2026-57129｜MervinPraison / praisonaiagents
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:06.317)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:06.317 / 2026-09-14T16:17:14.220
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to praisonaiagents 1.6.59, MentionsParser._process_file_mention accepts file-mention values and falls back from workspace-relative resolution to Path(file_path) without traversal, symlink, or workspace-boundary validation. Prompt input from users, bots, or workflows can therefore read arbitrary files accessible to the process, including credentials, keys, environment files, source code, and system configuration. This issue is fixed in praisonaiagents 1.6.59.

### 23. CVE-2026-57126｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:06.040)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:06.040 / 2026-09-14T20:16:48.440
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to praisonaiagents 1.6.58, SpiderTools._validate_url calls _host_is_blocked, which checks literal host encodings but does not resolve DNS names before scrape_page, crawl, extract_links, extract_text, or URL-mention fetches connect. An attacker-controlled hostname resolving to a loopback, private, link-local, or cloud-metadata address therefore bypasses the SSRF policy without a rebinding race and can expose internal responses to the agent. This issue is fixed in praisonaiagents 1.6.58.

### 24. CVE-2026-56839｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:12.977)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:12.977 / 2026-09-14T17:17:48.710
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to 4.6.59, the CODE_TOOLS wrappers keep _workspace_root as None and pass workspace=None to read_file, search_replace, and apply_diff helpers that enforce path containment only for a truthy workspace. An application that exposes code_read_file, code_search_replace, or code_apply_diff before set_workspace can therefore let prompt-influenced calls read and modify files outside the intended project directory, while explicitly configured workspaces remain effective. This vulnerability is fixed in 4.6.59.

### 25. CVE-2026-55451｜locize / gettext-converter
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:48.383)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T17:17:48.383 / 2026-09-14T19:17:32.213
- **官方描述（原文）**：gettext-converter provides gettext resource conversion utilities for JavaScript. Prior to 1.3.3, js2i18next() in lib/js2i18next.js splits nested translation keys using options.keyseparator, whose default value consists of two number signs, and uses each segment as a dynamic object key without rejecting __proto__, constructor, or prototype. When an application converts untrusted PO or i18next translation data, a __proto__ segment resolves Object.prototype as the nested write target and Object.assign writes attacker-controlled translated properties onto the process-wide prototype. The resulting prototype pollution can cause denial of service and may enable application-dependent follow-on attacks. This issue is fixed in version 1.3.3.

### 26. CVE-2026-55072｜pimcore / pimcore
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:47.610)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T17:17:47.610 / 2026-09-14T18:17:54.270
- **官方描述（原文）**：Pimcore is an Open Source Data & Experience Management Platform. Prior to 2026.1.5, an authenticated user with the objects permission can submit a malicious ClassDefinition UID because the name and ID validation expressions in models/DataObject/ClassDefinition.php validate only the beginning of each value. When a data object of that class containing a Block field is loaded, Block::load in models/DataObject/ClassDefinition/Data/Block.php incorporates the stored class ID into an unquoted object table identifier, allowing the UID to supply SQL syntax. The resulting query can read or modify arbitrary Pimcore database tables, including disclosure of password hashes, and the flaw represents an incomplete validation hardening because earlier work added a start anchor without enforcing the end of the identifier. This issue is fixed in version 2026.1.5.

### 27. CVE-2026-47253｜julien040 / anyquery
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T20:16:44.070)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T20:16:44.070 / 2026-09-14T20:16:44.070
- **官方描述（原文）**：Anyquery is an SQL query engine built on top of SQLite. Prior to 0.4.5, the clear_plugin_cache(plugin) SQL scalar function in namespace/other_functions.go passes the caller-controlled plugin parameter through path.Join to os.RemoveAll without rejecting traversal segments. A low-privileged bearer-token holder can invoke the function through the /v1/query HTTP endpoint, causing path.Join to resolve .. segments outside $XDG_CACHE_HOME/anyquery/plugins/ and os.RemoveAll to recursively delete any reachable directory writable by the Anyquery server process. This causes permanent data loss and denial of service without disclosing file contents. This issue is fixed in version 0.4.5.

### 28. CVE-2026-90961｜MISP / MISP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T14:17:21.270)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T14:17:21.270 / 2026-09-14T14:17:21.270
- **官方描述（原文）**：The LdapAuth and LinOTPAuth authentication plugins in MISP contain an authentication bypass vulnerability. Both LdapAuthenticate and LinOTPAuthenticate replace CakePHP's FormAuthenticate class but fail to replicate its _checkFields() input validation guard. As a result, the email and password fields extracted from the login request are passed to downstream authentication logic without verifying that they are non-empty strings. In the LDAP authenticator, an empty or null password is forwarded to ldap_bind(). Per RFC 4513 section 5.1.2, a bind request with a valid DN and an empty password constitutes an unauthenticated bind, which many LDAP directory servers accept as successful. An attacker who knows any valid user email address in the directory can therefore authenticate as that user without possessing a password. Additionally, non-string values (null, false, arrays) are either coerced to empty strings by ldap_bind(), raise TypeErrors, or are misinterpreted as find conditions in _findUser(), all of which can lead to unintended authentication outcomes. In the LinOTP authenticator, the same missing guard allows non-string credentials to be concatenated into the LinOTP verification request, and in the mixed-authentication branch an empty password is accepted against a stored hash of the empty string. A secondary issue in the LDAP authenticator is that newly created user accounts (auto-provisioned on first LDAP login) were assigned an empty password. Because the save path skips validation, the empty string is hashed and stored. If the user later ceases to be found in LDAP and the mixed-authentication fallback is used, the stored hash of the empty string verifies against an empty password, again permitting unauthenticated access. The vulnerability requires that the affected plugin (LdapAuth or LinOTPAuth) is enabled on the MISP instance and that the attacker knows at least one valid email address registered in the directory or MISP user store. No prior authentication is required. Successful exploitation grants the attacker the full privileges of the impersonated user, which may include administrative access to threat intelligence data. Version affected: ≤2.5.45

### 29. CVE-2026-90945｜crawlab-team / crawlab
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T18:20:29.030)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T18:20:29.030 / 2026-09-14T18:20:29.030
- **官方描述（原文）**：Crawlab through 0.6.3 uses a hard-coded HMAC-SHA256 secret for JWT token signing that cannot be overridden via configuration or environment variables. Unauthenticated attackers can forge valid administrator tokens to access administrative APIs and execute code on worker nodes.

### 30. CVE-2026-90943｜parallax / filament-comments
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:41.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:41.693 / 2026-09-14T20:17:03.320
- **官方描述（原文）**：parallax filament-comments through 3.0.0 contains a stored cross-site scripting vulnerability in comment body rendering that allows authenticated panel users to inject malicious scripts. Attackers can store XSS payloads in comment bodies that execute in the browsers of other users viewing those comments, including administrators, enabling session token theft and unauthorized actions.

### 31. CVE-2026-90937｜froxlor / froxlor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:19:32.277)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:19:32.277 / 2026-09-14T13:19:32.277
- **官方描述（原文）**：froxlor versions before 2.2.5 fail to validate newline characters in subdomain redirect URLs, allowing authenticated customers to inject arbitrary nginx or Apache configuration directives. Attackers can supply URLs containing literal newlines that are written verbatim into vhost config files during cron rebuild, enabling web server configuration corruption, denial of service, or hijacking of HTTP responses across hosted domains.

### 32. CVE-2026-90898｜maximhq / Bifrost
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T11:17:08.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T11:17:08.237 / 2026-09-14T12:17:51.657
- **官方描述（原文）**：Bifrost registers MCP clients through its management API. A stdio client is a command plus args. Bifrost starts that program in the gateway the moment the client is added. No MCP handshake required. The default is governance.auth_config.is_enabled=false. Auth off means every caller is a local admin. One unauthenticated POST /api/mcp/client is enough to run a program as the Bifrost process user (appuser on the official image). transports/v2.1.0 refuses an unauthenticated stdio registration with 403. transports/v2.0.0 still allows it.

### 33. CVE-2026-90693｜D-Link / DIR-878
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T08:16:35.673)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00473 / percentile=0.39592
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T08:16:35.673 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A flaw has been found in D-Link DIR-878 120B05. This impacts the function SetWan3Settings of the component WAN Settings. This manipulation of the argument Primary/Secondary causes stack-based buffer overflow. Remote exploitation of the attack is possible.

### 34. CVE-2026-90692｜D-Link / DIR-878
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T07:17:25.263)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00473 / percentile=0.39592
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T07:17:25.263 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was detected in D-Link DIR-878 120B05. This affects the function SetDynamicDNSIPv6Settings of the component Dynamic DNS IPv6 Settings. The manipulation of the argument IPv6Address/Hostname results in stack-based buffer overflow. The attack may be launched remotely.

### 35. CVE-2026-87802｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T11:17:05.620)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T11:17:05.620 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Improper verification of cryptographic signature vulnerability in Apache Syncope. When SRA is configured for OAuth 2.0 without JWKS set URI assigned, an attacker can forge arbitrary JWTs to impersonate any user identity and permissions, gaining full access to services proxied by SRA. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 36. CVE-2026-87785｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T11:17:05.503)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T11:17:05.503 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Authentication bypass by spoofing vulnerability in Apache Syncope. When the configured JWKS settings for internal JWT authentication are disclosed (at least protocol and key), an attacker can spoof another user's privileges after completing a successful authentication and obtaining a valid JWT. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 37. CVE-2026-86460｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T11:17:05.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T11:17:05.250 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Cypher injection vulnerability in the Neo4j persistence layer when processing some FIQL search conditions. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 38. CVE-2026-85192｜regularlabs.com / Conditional Content Pro extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T07:17:22.757)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00485 / percentile=0.40317
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T07:17:22.757 / 2026-09-14T12:17:49.983
- **官方描述（原文）**：Joomla Extension - regularlabs.com - Authenticated, privileged remote code execution in Conditional Content extension for Joomla < 8.0.0 - Conditional Content Pro accepts inline PHP Condition Rules in article syntax. In affected versions, the PHP is passed to the Conditions evaluator without checking who authored the article. Joomla's normal Author text filter preserves the syntax, so publishing the article causes the code to run as the web-server process.

### 39. CVE-2026-82441｜Apache Software Foundation / Apache Storm Nimbus
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T14:17:12.590)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T14:17:12.590 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Description A submitted topology carries two lists of blobstore keys, `dependency_jars` and `dependency_artifacts`, which the client fills in after uploading the corresponding blobs. Nimbus performed no validation of their contents on the submission path, yet acts on them in two places. During cleanup of a finished topology, Nimbus deletes the keys named in those lists, and the deletion is performed as the Nimbus subject, for which the blobstore short-circuits its ACL check. A submitter who listed a key belonging to another topology, such as its `-stormjar.jar`, could therefore cause that blob to be deleted when their own topology was cleaned up. Separately, on acquiring leadership a Nimbus compares the dependency keys of all active topologies against the blobstore contents and surrenders leadership if any is missing. A single key that does not exist, on a single active topology, therefore causes every Nimbus to acquire leadership, surrender it and requeue indefinitely, leaving the cluster without a leader and unable to schedule, clean up or accept submissions. Mitigation Upgrade to 3.1.0, where a submission is refused unless every entry in both lists is a dependency blob key and exists in the blobstore. Note that this validates new submissions only; a topology stored by an affected version with an invalid list is unaffected by the upgrade. An operator whose cluster is failing to retain a leader should inspect the Nimbus log for the dependency keys reported as missing and remove or resubmit the topology naming them. Users who cannot upgrade immediately should restrict topology submission to trusted principals. Credit This issue was discovered by rzo1 while investigating an unrelated blobstore defect.

### 40. CVE-2026-82439｜Apache Software Foundation / Apache Storm DRPC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T14:17:12.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T14:17:12.470 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Description The DRPC server kept a map from function name to request queue and created an entry the first time a function name was seen. No code path ever removed an entry: request cleanup removed the request from its queue, and the shutdown path drained queues, but the queue object and its map entry remained for the life of the process. Function names come from the client and are not constrained to functions any topology has registered, so the number of retained entries is bounded only by the number of distinct names an attacker chooses to send, and each retained entry holds the name itself. `drpc.authorizer` is unset by default, so no credentials are required to reach the endpoint. The retained state is permanent rather than a transient load spike, so the effect accumulates until the DRPC server exhausts its heap. Mitigation Upgrade to 3.1.0, where a function's queue is removed once nothing is waiting in it. Users who cannot upgrade immediately should configure `drpc.authorizer` so that only trusted principals can reach the DRPC endpoints, and should ensure the DRPC ports are not reachable from untrusted networks. Credit The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.

### 41. CVE-2026-82435｜Apache Software Foundation / Apache Storm Worker
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:10.620)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:10.620 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Description The worker's Netty message decoder is installed ahead of the SASL authentication handlers in the pipeline and acts on frames before any authentication has taken place. It allocated buffers sized from a length field carried in the frame, so a single frame from an unauthenticated peer able to reach a worker slot port could drive a large allocation. `storm.messaging.netty.authentication` defaults to false, and the decoder runs before the handler that enforces it in any case, so no credentials are required. The attacker needs only TCP reachability to a worker port. The effect of a single frame at the default 768 MB worker heap has not been measured to distinguish sustained worker loss from transient garbage-collection pressure. The severity assigned to this advisory reflects the more conservative reading; consumers who require a precise figure should test against their own worker heap configuration. Mitigation Upgrade to 3.1.0, where frames are decoded only after the handshake completes. Users who cannot upgrade immediately should ensure that worker slot ports are reachable only from within the cluster, as the security model already recommends, and should enable `storm.messaging.netty.authentication` where the deployment permits it. Credit The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.

### 42. CVE-2026-82434｜Apache Software Foundation / Apache Storm Nimbus
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:10.453)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:10.453 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Description When ZooKeeper authentication is configured, Storm deliberately retains `storm.zookeeper.topology.auth.payload` in the topology configuration, because workers need it. Nimbus then served that configuration verbatim to any caller holding read-only topology permissions, so a user whose only grant was the ability to view a topology received its ZooKeeper credential. That credential is not read-only. The cluster state implementation uses write-capable ACLs for worker heartbeats, backpressure and error state, so a recipient can forge or remove that state for the topology concerned. It is not a write credential on assignments. The same advisory covers the submission client, which logged the generated payload at INFO on every submission that generated one, and the SASL handlers, which logged it at DEBUG. The credential therefore also reached any log aggregation or support bundle collected from the cluster. Mitigation Upgrade to 3.1.0, where the payload is removed from the configuration served to read-only callers and is no longer written to logs. Users who cannot upgrade immediately should rotate `storm.zookeeper.topology.auth.payload` for existing topologies, review retained logs and support bundles for the value, and restrict read-only topology permissions to trusted principals. Credit The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.

### 43. CVE-2026-82431｜Apache Software Foundation / Apache Storm Client
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:10.053)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:10.053 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Description `SimpleACLAuthorizer` evaluated the user-level command set by returning early when `nimbus.users` was empty, before `nimbus.groups` was considered. An operator who restricted cluster access by group alone, leaving `nimbus.users` unset, therefore received no restriction at all: every authenticated principal was permitted every user-level operation, including `submitTopology`, `beginFileUpload` and `getNimbusConf`. `docs/SECURITY.md` presents `nimbus.groups` as a supported way to lock down a cluster, so a deployment following the documentation could believe it was restricted while it was not. The failure is silent; nothing in the logs or the configuration indicates that the group list is being ignored. Both lists left empty continues to mean that no restriction is configured, which is the shipped default and is unchanged. Mitigation Upgrade to 3.1.0, where `nimbus.groups` is evaluated whether or not `nimbus.users` is set. Users who cannot upgrade immediately should additionally populate `nimbus.users` with the intended principals, since a non-empty user list causes the group list to be evaluated on affected versions. Operators should review Nimbus access logs for operations by principals outside the intended groups. Note that after upgrading, a cluster configured with `nimbus.groups` alone becomes restrictive for the first time. This includes `NimbusClient`, which calls `getLeader` on every connection, so clients outside the configured groups will begin to be refused. Credit The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.

### 44. CVE-2026-82232｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T11:17:05.123)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T11:17:05.123 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Apache Syncope. An administrator with adequate entitlements can achieve execution of arbitrary SQL via stacked queries, leveraging unsanitized sort clauses for Task search. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 45. CVE-2026-78330｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:18:47.123)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:18:47.123 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Incorrect privilege assignment vulnerability in Apache Syncope. When the configured JWKS settings for internal JWT authentication are disclosed (at least protocol and key), an attacker can obtain admin privileges after completing a successful authentication and obtaining a valid low-privileges JWT. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 46. CVE-2026-78299｜Eclipse Foundation / Eclipse Embedded CDT (C/C++ Development Tools)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:18:46.870)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:18:46.870 / 2026-09-14T20:16:52.980
- **官方描述（原文）**：In Eclipse Embedded CDT versions 6.0 to 6.7 if the CMSIS-Pack archive extracts a compromised CMSIS pack the archive extraction can extract files to locations outside of the pack, allowing writing of arbitrary files to other locations on disk.

### 47. CVE-2026-77181｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:18:46.623)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:18:46.623 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Incorrect Authorization vulnerability in Apache Syncope. An administrator with ClientApp's update entitlement is unable to perform the related operation, while ClientApp's create entitlement is checked both for create and update operations on ClientApp. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 48. CVE-2026-77051｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:18:46.363)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:18:46.363 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Syncope. An administrator with adequate entitlements can achieve execution of arbitrary SQL via stacked queries, leveraging unsanitized entityKey and opEvent parameters. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 49. CVE-2026-76443｜Cisco / Cisco Secure Email
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:50.970)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T17:17:50.970 / 2026-09-15T04:18:14.493
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Email Gateway and Cisco Secure Email and Web Manager engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76443 are related to issues with improper neutralization that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-707.

### 50. CVE-2026-76441｜Cisco / Cisco Secure Email and Web Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:50.673)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T17:17:50.673 / 2026-09-15T04:18:13.277
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Email Gateway and Cisco Secure Email and Web Manager engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76441 are related to issues with improper access control that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-284.

### 51. CVE-2026-76440｜Cisco / Cisco Secure Email
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:50.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T17:17:50.520 / 2026-09-15T04:18:12.660
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Email Gateway and Cisco Secure Email and Web Manager engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76440 are related to path traversal issues that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-23.

### 52. CVE-2026-75030｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:18:45.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:18:45.990 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Missing Authorization vulnerability in Apache Syncope. An administrator with task execution entitlements might be able to mass (de)provision group members, regardless of their group-related administration capabilities. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 53. CVE-2026-73668｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:18:45.437)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:18:45.437 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Incorrect Authorization vulnerability in Apache Syncope. An administrator with adequate entitlements in a given Realm may be able to read via REST the full Connector configuration, confidential properties included, scoped in another Realm and thus be able to effectively duplicate such Connector instance into the Realm they have administration rights for. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 54. CVE-2026-73579｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:18:45.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:18:45.313 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Incorrect Authorization vulnerability in Apache Syncope. Any search requests are transformed into SQL, Neo4J or Elasticsearch / Opensearch queries, depending on the actual deployment configuration. An important component of such transformation is the Realms filter, which ensures that the search results are matching the requester's permissions. For non-recursive search requests it is possible that such Realms filter is rendered as empty, thus voiding any restriction on requester privileges. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 55. CVE-2026-73470｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:18:45.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:18:45.190 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Improper Privilege Management vulnerability in Apache Syncope. Delegations can be created or updated with Roles not owned by the delegating User, or not for the same Realm subtree under the delegation management was granted for. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 56. CVE-2026-73370｜Apache Software Foundation / Apache Syncope
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T14:17:09.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T14:17:09.077 / 2026-09-14T20:58:48.430
- **官方描述（原文）**：Incorrect Authorization vulnerability in Apache Syncope. Delegated administration security checks performed by Reconciliation service's pull and push, being incomplete, could accept calls by administrator not provided with adequate entitlements. This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.7, from 4.1.0-M0 through 4.1.2. Users are recommended to upgrade to version 4.0.8 / 4.1.3, which fix this issue.

### 57. CVE-2026-67399｜WebPros / WHMCS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T21:17:25.423)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T21:17:25.423 / 2026-09-14T21:17:25.423
- **官方描述（原文）**：Deserialization of untrusted data in WHMCS 9.0.0 before 9.0.8 and 8.0.0 before 8.13.7 allows remote attackers to execute arbitrary code.

### 58. CVE-2026-65414｜Apple / iOS and iPadOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T21:17:25.057)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T21:17:25.057 / 2026-09-15T04:18:11.397
- **官方描述（原文）**：An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in iOS 26.7 and iPadOS 26.7, iOS 27 and iPadOS 27, macOS Golden Gate 27, macOS Sequoia 15.8, macOS Tahoe 26.7, tvOS 27, visionOS 27, watchOS 27. A remote attacker may be able to cause unexpected app termination or arbitrary code execution.

### 59. CVE-2026-59178｜esphome / device-builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T19:17:37.617)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T19:17:37.617 / 2026-09-14T19:17:37.617
- **官方描述（原文）**：ESPHome Device Builder Dashboard is a dashboard for the ESPHome home management software. Prior to version 1.0.12, the dashboard reads its authentication credentials from `$ESPHOME_USERNAME` and `$ESPHOME_PASSWORD`. Earlier versions, and the legacy `esphome` dashboard, read the bare `$USERNAME` and `$PASSWORD` instead. When the env vars were renamed the bare names were dropped with no fallback, so an operator who had protected their dashboard with `USERNAME` / `PASSWORD` (as the older getting started guide documented) loses authentication on upgrade and the dashboard starts open to anyone who can reach its port. The issue is fixed in 1.0.12. The bare `$USERNAME` / `$PASSWORD` are accepted again as a deprecated fallback so previously protected instances stay protected across the upgrade without operator intervention, with a loud deprecation warning at startup directing operators to rename them to `$ESPHOME_USERNAME` / `$ESPHOME_PASSWORD`. The fallback is gated on `$PASSWORD` being set and is only adopted as a pair, so the OS provided `$USERNAME` is never read on its own and the original collision footgun stays closed. A lone bare `$PASSWORD` with no username still fails loud as a credential mismatch rather than starting unauthenticated. This restores compatibility rather than failing closed on the legacy names, because the priority is that an instance which was protected before the upgrade stays protected without the operator having to act; the deprecation warning plus a future removal handles the migration. Operators should migrate to the `$ESPHOME_*` names. The esphome container delivers the fix in the 2026.6.2 release, which bumps its pinned `esphome-device-builder` version to 1.0.12. Without upgrading, restore authentication immediately by setting the new env vars to the same values, on any affected version. Alternatively, do not expose the dashboard port to untrusted networks, and check the startup logs for the `WITHOUT AUTHENTICATION` banner to confirm whether a given instance is currently open.

### 60. CVE-2026-57578｜riganti / dotvvm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T18:17:57.913)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T18:17:57.913 / 2026-09-14T19:17:36.643
- **官方描述（原文）**：DotVVM is an open source MVVM framework for web applications. Prior to 4.2.11, 4.3.15, and 5.0.0-preview09-final, AuthorizeActionFilter performs no authorization because its explicit ICommandActionFilter.OnCommandExecutingAsync, IViewModelActionFilter.OnViewModelCreatedAsync, and IPresenterActionFilter.OnPresenterExecutingAsync implementations return completed tasks instead of invoking the corresponding checks. Applications relying on this filter can therefore expose protected commands, view models, or presenters to unauthorized requests without any special bypass technique. AuthorizeAttribute correctly implements the same interfaces and can be used as a workaround. This issue is fixed in versions 4.2.11, 4.3.15, and 5.0.0-preview09-final.

### 61. CVE-2026-57145｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:15.017)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:15.017 / 2026-09-14T19:17:35.653
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to 4.6.62, src/praisonai/praisonai/tools/multiedit.py passes the LLM-controlled filepath parameter directly to open for reading and writing without traversal rejection, symlink resolution, a workspace boundary, or protected-path checks. Prompt-influenced agents can read files through edit and diff behavior or overwrite files accessible to the process, exposing secrets and enabling persistence or application tampering. This issue is fixed in 4.6.62.

### 62. CVE-2026-57123｜MervinPraison / praisonaiagents
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:05.753)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:05.753 / 2026-09-14T19:17:34.673
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to praisonaiagents 1.6.59, ToolsMCPServer.run_sse and launch_tools_mcp_server bind to 0.0.0.0 and create /sse and /messages/ routes without invoking the available SecurityConfig authentication, origin-validation, or DNS-rebinding controls. Any reachable client can list and invoke registered tools, and a browser can target a local instance through DNS rebinding, with impact determined by the registered file, shell, and code-execution tools. This vulnerability is fixed in praisonaiagents 1.6.59.

### 63. CVE-2026-55209｜equinor / resdata
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T20:16:47.487)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T20:16:47.487 / 2026-09-14T21:17:13.457
- **官方描述（原文）**：resdata is software for reading and writing result files from the Eclipse reservoir simulator. Prior to 6.2.9, resdata insufficiently validates numeric fields, grid dimensions, keyword sizes, and array indexes while parsing untrusted GRDECL files in lib/resdata/rd_kw_grdecl.cpp and lib/resdata/rd_grid.cpp. Malformed COORD, ZCORN, CORSNUM, ACTNUM, or MAPAXES data can reach rd_grid_alloc_GRDECL_kw__ with inconsistent lengths, while unbounded floating-point conversion can exceed the intended parser buffer. In a network service that accepts untrusted GRDECL files, these conditions can cause a classic buffer overflow, out-of-bounds reads, invalid array access, NULL pointer dereference, memory corruption, or service termination. This issue is fixed in version 6.2.9.

### 64. CVE-2026-54334｜theopolis / uefi-firmware-parser
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T20:16:46.143)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T20:16:46.143 / 2026-09-14T20:16:46.143
- **官方描述（原文）**：UEFI Firmware Parser parses BIOS, Intel ME, and UEFI firmware structures including volumes, file systems, and files. Prior to 1.14, ReadCLen() in uefi_firmware/compression/Tiano/Decompress.c reads Number from GetBits(Sd, CBIT) with CBIT = 9 and can obtain 511 entries for the 510-element Sd->mCLen heap array because its loop does not enforce Index < NC. The CharC == 2 run-length path can additionally request up to 531 zero writes through Sd->mCLen[Index++] = 0. The normal CompressedSection.process() to efi_compressor.TianoDecompress() to TianoDecompress() to DecodeC() to ReadCLen() parsing path therefore permits crafted Tiano or EFI compressed firmware to corrupt heap memory, deterministically crash the parsing process, and potentially execute code depending on build and runtime details. This issue is fixed in version 1.14.

### 65. CVE-2026-54333｜theopolis / uefi-firmware-parser
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T20:16:45.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T20:16:45.990 / 2026-09-14T20:16:45.990
- **官方描述（原文）**：UEFI Firmware Parser parses BIOS, Intel ME, and UEFI firmware structures including volumes, file systems, and files. Prior to 1.14, MakeTable() in uefi_firmware/compression/Tiano/Decompress.c does not validate that bit-length values read from a crafted Tiano or EFI compressed firmware bitstream remain within the expected range from 0 through 16. The normal CompressedSection.process() to efi_compressor.TianoDecompress() to TianoDecompress() to ReadPTLen() to MakeTable() parsing path can consequently write beyond the stack-allocated Count[17] array and related decode tables. The resulting stack corruption deterministically crashes the parsing process and may permit code execution depending on build and runtime details. This issue is fixed in version 1.14.

### 66. CVE-2026-53713｜envoyproxy / gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T21:17:12.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T21:17:12.520 / 2026-09-14T21:17:12.520
- **官方描述（原文）**：Envoy Gateway is an open source project for managing Envoy Proxy as a standalone or Kubernetes-based application gateway. Prior to 1.7.4 and 1.8.1, to_absolute_normalized_path in internal/gatewayapi/luavalidator/security.lua does not collapse redundant separators before is_critical_path evaluates Lua submitted through EnvoyExtensionPolicy during default Strict validation. Linux resolves a double-slash absolute path as the corresponding single-slash path, but the validator does not match the redundant-separator form, allowing submitted Lua to read arbitrary files from the gateway controller pod. Exposed files can include Kubernetes service-account tokens, TLS certificates, and process environment data, and the disclosed credentials can provide access to sensitive Kubernetes API Server or Gateway xDS server information. This issue is fixed in versions 1.7.4 and 1.8.1.

### 67. CVE-2026-50006｜julien040 / anyquery
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T20:16:44.637)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T20:16:44.637 / 2026-09-14T20:16:44.637
- **官方描述（原文）**：Anyquery is an SQL query engine built on top of SQLite. Prior to 0.4.5, anyquery server forwards unauthenticated SQL from its MySQL-compatible server port to SQLite without restricting ATTACH DATABASE filesystem targets. A remote attacker can select any path writable by the Anyquery server process, cause SQLite to create a database file there, and place attacker-controlled table content in that file. This permits arbitrary file creation or overwrite, causing filesystem integrity loss and denial of service; remote code execution is possible only when another service interprets the written file or the process has a suitably privileged writable target. This issue is fixed in version 0.4.5.

### 68. CVE-2026-21391｜Ping Identity / PingAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T12:17:38.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T12:17:38.810 / 2026-09-14T15:17:04.850
- **官方描述（原文）**：An improper validation vulnerability exists within PingAM where a well-crafted request allows arbitrary or protected ID Token claims to be set or overridden. In certain configurations this could allow an attacker to bypass authentication controls via spoofing leading to privilege escalation or impersonation.

### 69. CVE-2026-20353｜Cisco / Cisco Secure Email
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:43.000)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T17:17:43.000 / 2026-09-15T04:18:02.940
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Email Gateway and Cisco Secure Email and Web Manager engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-20353 are related to issues with improper control of a resource through its lifetime that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-664.

### 70. CVE-2026-16338｜IBM / DataStage on Cloud Pak for Data
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T20:16:40.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T20:16:40.410 / 2026-09-14T21:17:03.070
- **官方描述（原文）**：IBM DataStage on Cloud Pak for Data 5.4.0.0 IBM DataStage could allow a remote authenticated attacker to perform an arbitrary file write due to improper validation of file paths.

### 71. CVE-2026-12944｜IBM / Langflow OSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T22:16:56.950)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T22:16:56.950 / 2026-09-14T22:16:56.950
- **官方描述（原文）**：IBM Langflow OSS 1.0.0 through 1.10.0 can allow attackers to execute arbitrary Python code with root privileges (UID=0) on the Langflow server by submitting components containing socket or urllib imports. This enables: (1) AWS credential theft via IMDSv1 SSRF with full IAM role permissions, (2) arbitrary file exfiltration from the container filesystem, and (3) lateral movement to internal services (PostgreSQL, Redis) within the Docker network. The scanner incorrectly returns "validated": true, providing a false security signal.

### 72. CVE-2026-12258｜Hiperdino / REST API
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:17:33.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:17:33.290 / 2026-09-14T15:17:04.153
- **官方描述（原文）**：Inadequate access control in Hiperdino’s REST v1.0 API. The public endpoint ‘customer/check’ could allow an authenticated attacker to enter a telephone number or an email address. When the value entered belongs to a registered customer, the service returns the associated information (email address and telephone number). No authentication is required beyond a static bearer token, and there is no rate limiting or generic error handling. Successful exploitation of this vulnerability could allow a remote attacker to enumerate a user’s contact details, although this would require obtaining a valid static bearer token, constituting an information disclosure vulnerability.

### 73. CVE-2026-90936｜froxlor / froxlor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:19:32.130)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:19:32.130 / 2026-09-14T21:17:43.030
- **官方描述（原文）**：Froxlor before 2.3.7 fails to properly scope sender alias lookups to the current customer in customer_email.php. Authenticated attackers can enumerate global sender alias IDs and read other customers' allowed sender values by supplying arbitrary senderid parameters in delete confirmation requests.

### 74. CVE-2026-90935｜froxlor / froxlor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:19:31.987)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:19:31.987 / 2026-09-14T15:17:13.950
- **官方描述（原文）**：Froxlor before 2.3.7 fails to validate the mysql_server parameter against a customer's allowed_mysqlserver allowlist in the Mysqls.add API command. Attackers can supply a disallowed server index to create MySQL databases and users on forbidden servers, bypassing per-customer access controls.

### 75. CVE-2026-90931｜laradashboard / laradashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:19:31.350)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:19:31.350 / 2026-09-14T21:17:42.903
- **官方描述（原文）**：LaraDashboard versions 0.9.0 through 1.2.2 fail to sanitize SVG file content during media upload, allowing authenticated users with only the media.create permission to upload malicious SVG files containing script tags. When any user including administrators opens the stored SVG file served inline from the application origin, the embedded JavaScript executes in the dashboard context, enabling session hijacking and administrative account takeover.

### 76. CVE-2026-90808｜HKUDS / nanobot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T19:18:10.700)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T19:18:10.700 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was determined in HKUDS nanobot up to 0.2.1. Impacted is the function ExecTool._guard_command/ExecTool._spawn of the file nanobot/agent/tools/shell.py of the component ExecTool. This manipulation causes incomplete blacklist. It is possible to initiate the attack remotely. Patch name: af582246f141311d574551b7571a517bcc3df750. Applying a patch is the recommended action to fix this issue.

### 77. CVE-2026-90789｜itsourcecode / Leave Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:12.967)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:12.967 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A weakness has been identified in itsourcecode Leave Management System 1.0. Affected by this issue is some unknown functionality of the file /login.php. Executing a manipulation of the argument user_email can lead to sql injection. The attack may be launched remotely. The exploit has been made available to the public and could be used for attacks.

### 78. CVE-2026-90787｜Soarkey / StudentManagement
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T14:17:19.530)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T14:17:19.530 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was identified in Soarkey StudentManagement up to e08f7f1d5015af407aa4cca0ada3dea189b4937e. Affected is the function RegisterServlet.doPost of the file code/WebContent/register.html of the component Registration Workflow. Such manipulation of the argument level leads to improper privilege management. The attack can be launched remotely. The exploit is publicly available and might be used. This product does not use versioning. This is why information about affected and unaffected releases are unavailable. The project was informed of the problem early through an issue report but has not responded yet.

### 79. CVE-2026-90784｜Dvidelabs / flatcc
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:19:30.500)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:19:30.500 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability has been found in Dvidelabs flatcc up to 0.6.3. The impacted element is the function fb_clear_parser of the file src/Compiler/semantics.c. The manipulation leads to memory leak. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The identifier of the patch is 8dbc3419738da066151991fd2bf1d0c85591dea2. It is suggested to install a patch to address this issue.

### 80. CVE-2026-90715｜marcobambini / Gravity
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T13:19:30.080)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T13:19:30.080 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A security vulnerability has been detected in marcobambini Gravity up to 0.9.7. This affects an unknown function of the file src/utils/gravity_json.c of the component udp json-parser. Such manipulation leads to integer overflow. The attack may be performed from remote. The exploit has been disclosed publicly and may be used. Upgrading to version 0.9.8 mitigates this issue. The name of the patch is 9b337c3eae5833c3956bed1fc01c21c14fd443f2. Upgrading the affected component is recommended.

### 81. CVE-2026-90701｜subhajitkhan / online-clinic-management-system
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T10:17:05.233)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T10:17:05.233 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was detected in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a29a578. The affected element is an unknown function of the file listdoctor.php. Performing a manipulation of the argument searchtext results in sql injection. The attack may be initiated remotely. The exploit is now public and may be used. This product uses a rolling release model to deliver continuous updates. As a result, specific version information for affected or updated releases is not available. The project was informed of the problem early through an issue report but has not responded yet.

### 82. CVE-2026-90691｜0x4m4 / HexStrike AI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T07:17:25.080)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00429 / percentile=0.3622
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T07:17:25.080 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A security vulnerability has been detected in 0x4m4 HexStrike AI up to d689933ff579d839c676c82b231f8e98326c5f04. The impacted element is the function FileOperationsManager of the file hexstrike_server.py of the component API Files Endpoint. The manipulation of the argument filename leads to path traversal. The attack may be initiated remotely. The exploit has been disclosed publicly and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 83. CVE-2026-90686｜未確認 / GPAC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T06:16:58.507)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00496 / percentile=0.41119
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T06:16:58.507 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was found in GPAC up to f1219cde. This affects the function gf_bt_report of the file scene_manager/loader_bt.c of the component MP4Box. The manipulation results in memory corruption. The attack may be performed from remote. The exploit has been made public and could be used. Upgrading to version abi-16.23 is able to mitigate this issue. The patch is identified as afca1f1181668d85941d51ed1adf647807d5d975. It is suggested to upgrade the affected component.

### 84. CVE-2026-57128｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:06.177)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:06.177 / 2026-09-14T16:17:13.707
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to praisonaiagents 1.6.58, the SSE server in src/praisonai-agents/praisonaiagents/server/server.py does not consult ServerConfig.auth_token before handling /publish, /events, or /info requests. A network client that can reach the server can broadcast arbitrary events to connected clients and obtain server configuration and client-count information. This issue is fixed in praisonaiagents 1.6.58.

### 85. CVE-2026-55832｜sonos / tract
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T18:17:55.663)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T18:17:55.663 / 2026-09-14T19:17:32.717
- **官方描述（原文）**：Tract is a tiny, no-nonsense, self-contained TensorFlow and ONNX inference toolkit. Prior to 0.21.17, 0.22.3, and 0.23.2, the tract-onnx crate passes the attacker-controlled external_data location from an ONNX model through onnx/src/tensor.rs get_external_resources and joins the value to the model directory without rejecting absolute paths or parent directory components. Loading an untrusted model through model_for_path can therefore make onnx/src/data_resolver.rs MmapDataResolver open an arbitrary local file and place the file contents into model tensors or inference output. Attacker-controlled offset and length fields can also select an out-of-range mapping slice and cause a denial of service, but the flaw does not write files or execute code. This issue is fixed in versions 0.21.17, 0.22.3, and 0.23.2.

### 86. CVE-2026-55093｜sonos / tract
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T20:16:47.290)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T20:16:47.290 / 2026-09-14T20:16:47.290
- **官方描述（原文）**：Tract is a tiny, no-nonsense, self-contained TensorFlow and ONNX inference toolkit. Prior to 0.21.16, 0.22.2, and 0.23.1, tract-nnef uses unchecked usize multiplication in nnef/src/tensors.rs read_tensor for attacker-controlled tensor dimensions, the allocation size, and the reported tensor length. Loading a crafted NNEF archive through model_for_path or model_for_read reaches the default DatLoader and can make the wrapped size check accept a small allocation while data/src/tensor.rs as_slice_unchecked creates a much larger logical slice. Model construction through as_uniform can then read beyond the heap allocation and disclose adjacent data, and later access can terminate the process with a segmentation fault. The affected dense numeric tensor path does not include the independently guarded bool, String, or block-quant paths, and no out-of-bounds write or code execution was demonstrated. This issue is fixed in versions 0.21.16, 0.22.2, and 0.23.1.

### 87. CVE-2026-53708｜IBM / mcp-context-forge
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:11.883)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.6 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:11.883 / 2026-09-14T17:17:46.410
- **官方描述（原文）**：ContextForge is an AI gateway, registry, and proxy that provides centralized discovery, guardrails, and management for MCP, A2A, and REST or gRPC APIs. Prior to 1.0.3, the /admin/gateways/test call site in mcpgateway/admin.py calls validate_gateway_test_url() in mcpgateway/common/validators.py to resolve and reject private, loopback, link-local, and cloud-metadata addresses, but ResilientHttpClient later resolves the original hostname again without binding the validated address. When MCPGATEWAY_ADMIN_API_ENABLED is enabled, an attacker with a database-backed role containing explicit gateways.read permission can use DNS rebinding to return a public address during validation and a private or metadata address during connection, bypassing ssrf_blocked_networks and ssrf_dns_fail_closed because those controls apply only to the validation-time result. The endpoint's allow_admin_bypass=False setting means a bootstrap-only virtual platform-admin identity without a database role is not sufficient. Successful exploitation can reach internal services and cloud metadata, expose cloud credentials, access internal APIs, or probe internal network ports. This issue is fixed in version 1.0.3.

### 88. CVE-2026-53496｜mattiasw / ExifReader
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:46.213)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T17:17:46.213 / 2026-09-14T19:17:25.107
- **官方描述（原文）**：ExifReader is a JavaScript Exif information parser. Prior to 4.40.1, ExifReader.load() and the asynchronous file and URL loaders can pass attacker-supplied HEIC or AVIF data to the ISO-BMFF parser in src/image-header-iso-bmff.js, where findMetaBox() and parseBox() accept an eight-byte box header without confirming that fields required by the parsed box remain in the DataView. A valid ftyp box followed by an empty free or unknown box can cause an unchecked full-box version read, while a truncated extended-size box can make getBoxLength() and hasEmptyHighBits() read absent size fields. The resulting RangeError escapes the main parsing path and can abort an application request or worker when parse errors are not defensively caught, causing denial of service. This issue is fixed in version 4.40.1.

### 89. CVE-2026-47256｜open-telemetry / opentelemetry-collector-contrib
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T18:17:48.250)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T18:17:48.250 / 2026-09-14T19:17:22.573
- **官方描述（原文）**：OpenTelemetry, also known as OTel, is a vendor-neutral open source Observability framework for instrumenting, generating, collecting, and exporting telemetry data such as traces, metrics, and logs. Prior to 0.154.0, the Sentry exporter reads the remote OTLP sender-controlled service.name resource attribute in exporter/sentryexporter/sentry_exporter.go through extractProjectSlug and getOrCreateProjectEndpoint, passes the raw project slug to GetOTLPEndpoints and GetProjectKeys in exporter/sentryexporter/sentry_client.go, and interpolates it into a Sentry API URL without applying projectSlugRegexp through validateRoutingConfig at runtime in exporter/sentryexporter/config.go. Special characters can turn the expected path suffix into query data in all deployments or introduce slash and dot segments that traverse paths when the Sentry deployment normalizes them, while the Collector attaches its operator-configured bearer token to the request. A successful request can reach token-authorized administrative, organization, member, or key endpoints within the configured Sentry organization, and an attacker-controlled project slug can redirect subsequently exported telemetry. Sentry token middleware prevents cross-organization access. This issue is fixed in version 0.154.0.

### 90. CVE-2025-24890｜GitoxideLabs / gitoxide
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:05.117)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:05.117 / 2026-09-14T19:17:11.973
- **官方描述（原文）**：gitoxide is an implementation of git written in Rust. Prior to 0.13.3, the gix-sec crate on Windows incorrectly treats repositories controlled by another user as trusted when an administrator runs a dependent program with an unfiltered elevated token. In gix-sec/src/identity.rs, gix_sec::identity::is_path_owned_by_current_user obtains folder_owner and token_owner, but its administrator-specific IsWellKnownSid and CheckTokenMembership checks examine the running token rather than confirming the directory owner. This bypasses safe.directory-style protection for repositories owned and configured by a limited user, allowing repository configuration or hooks to execute commands with the administrator's privileges when an affected operation is performed. Exploitation requires Windows, an elevated administrator, a program that relies on gix-sec trust results, and interaction with a repository controlled by another user. An unelevated UAC process is not affected, and cloning is not affected because repository configuration and hooks are not copied. This issue is fixed in version 0.13.3.

### 91. CVE-2024-23176｜MediaWiki / MassMessage
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T07:17:16.097)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：0.00171 / percentile=0.06724
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T07:17:16.097 / 2026-09-14T16:17:04.980
- **官方描述（原文）**：An issue was discovered in the MassMessage extension in MediaWiki before 1.40.2. For a Special:MassMessage?uselang=x-xss URL, the i18n key massmessage-form-page-help allows XSS.

### 92. CVE-2023-40772｜DataEase / DataEase
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T06:16:54.053)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：0.01008 / percentile=0.61108
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T06:16:54.053 / 2026-09-14T16:17:04.723
- **官方描述（原文）**：A directory Traversal vulnerability in DataEase before 1.18.10 allows a remote attacker to obtain sensitive information via a a crafted request to the StaticResourceController.java component.

### 93. CVE-2026-90813｜cosmicstack-labs / mercury-agent
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T20:17:02.510)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T20:17:02.510 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was detected in cosmicstack-labs mercury-agent up to 1.1.13. Affected is the function checkShellCommand of the file src/capabilities/permissions.ts of the component Shell Command Execution. The manipulation results in incorrect behavior order: validate before canonicalize. The attack may be launched remotely. The exploit is now public and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 94. CVE-2026-90811｜cosmicstack-labs / mercury-agent
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T19:18:11.670)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T19:18:11.670 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A weakness has been identified in cosmicstack-labs mercury-agent up to 1.2.0. This affects the function PermissionManager.checkShellCommand of the file mercury-agent/src/capabilities/permissions.ts of the component Shell Permission Manifest. Executing a manipulation can lead to information disclosure. The attack is restricted to local execution. The exploit has been made available to the public and could be used for attacks. The project was informed of the problem early through an issue report but has not responded yet.

### 95. CVE-2026-90803｜GNU / Binutils
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:56.983)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T17:17:56.983 / 2026-09-14T20:55:24.127
- **官方描述（原文）**：A security vulnerability has been detected in GNU Binutils 2.47. Affected by this vulnerability is the function elf_x86_64_relocate_section of the file bfd/elf64-x86-64.c of the component ld. Such manipulation of the argument roff leads to buffer overflow. An attack has to be approached locally. The exploit has been disclosed publicly and may be used. Upgrading to version 2.48 addresses this issue. The name of the patch is 471130b39c03623ec6d78ece377ff4da3f6bfe7b. It is recommended to upgrade the affected component.

### 96. CVE-2026-90801｜GNU / Binutils
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T17:17:56.610)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T17:17:56.610 / 2026-09-14T20:55:24.127
- **官方描述（原文）**：A security flaw has been discovered in GNU Binutils 2.47. This impacts the function cache_bwrite of the file bfd/cache.c of the component ld. The manipulation of the argument nbytes results in buffer overflow. The attack requires a local approach. The exploit has been released to the public and may be used for attacks. The project was informed of the problem early through a bug report but has not responded yet.

### 97. CVE-2026-90794｜未確認 / GPAC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:41.290)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:41.290 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was found in GPAC up to f1219cde. The affected element is the function gf_sg_script_load of the file scenegraph/vrml_tools.c of the component MP4Box. Performing a manipulation results in use after free. It is possible to initiate the attack remotely. The exploit has been made public and could be used. Upgrading to version abi-16.23 is sufficient to fix this issue. The patch is named 9eb40df4448b88d6a6ce3454657c06f47eff0b24. It is advisable to upgrade the affected component.

### 98. CVE-2026-90792｜未確認 / GPAC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T16:17:40.907)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T16:17:40.907 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A flaw has been found in GPAC up to f1219cde. This issue affects the function gf_node_list_get_child of the file scenegraph/base_scenegraph.c of the component MP4Box. This manipulation of the argument Target causes null pointer dereference. The attack is possible to be carried out remotely. The exploit has been published and may be used. Upgrading to version abi-16.23 is capable of addressing this issue. Patch name: afca1f1181668d85941d51ed1adf647807d5d975. It is recommended to upgrade the affected component.

### 99. CVE-2026-90712｜Gitlawb / openclaude
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T12:17:51.223)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T12:17:51.223 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was identified in Gitlawb openclaude up to 0.30.0. Impacted is the function waitForCallback of the file src/services/api/xaiOAuthCallback.ts of the component xAI OAuth Callback Handler. The manipulation of the argument Error leads to denial of service. Remote exploitation of the attack is possible. The exploit is publicly available and might be used. The project was informed of the problem early through an issue report but has not responded yet.

### 100. CVE-2026-90709｜Yot / CMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T12:17:50.830)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T12:17:50.830 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A security vulnerability has been detected in Yot CMS up to 3.3.1. Affected by this issue is the function eval of the file modsys/console/admin.php of the component Admin Console. Such manipulation of the argument text leads to code injection. It is possible to launch the attack remotely. The exploit has been disclosed publicly and may be used.

### 101. CVE-2026-90706｜D-Link / DWR-M921
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T11:17:06.930)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T11:17:06.930 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was identified in D-Link DWR-M921 1.1.52. This impacts the function formWsc of the file /boafrm/formWsc. The manipulation of the argument targetAPSsid leads to os command injection. The attack is possible to be carried out remotely. The exploit is publicly available and might be used.

### 102. CVE-2026-90704｜D-Link / DWR-M921
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T10:17:05.767)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T10:17:05.767 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was found in D-Link DWR-M921 1.1.52. The impacted element is the function system of the file /boafrm/formDiskPartition. Performing a manipulation of the argument devicename results in command injection. Remote exploitation of the attack is possible. The exploit has been made public and could be used.

### 103. CVE-2026-90696｜SourceCodester / Inventory Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T09:17:01.950)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：0.00199 / percentile=0.09794
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T09:17:01.950 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability was determined in SourceCodester Inventory Management System 1.0. Affected by this issue is some unknown functionality of the file /api/products_handler.php of the component Product Management Module. Executing a manipulation of the argument Product_Name can lead to cross site scripting. The attack may be performed from remote. The exploit has been publicly disclosed and may be utilized.

### 104. CVE-2026-90694｜SourceCodester / Inventory Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T08:16:35.850)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：0.00199 / percentile=0.09794
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T08:16:35.850 / 2026-09-14T20:56:48.220
- **官方描述（原文）**：A vulnerability has been found in SourceCodester Inventory Management System 1.0. Affected is an unknown function of the file /api/customers_handler.php of the component Customer Management Module. Such manipulation of the argument Customer_Name leads to cross site scripting. The attack can be executed remotely. The exploit has been disclosed to the public and may be used.

### 105. CVE-2026-82019｜TripleLift / video-bundle.js
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T15:17:09.223)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T15:17:09.223 / 2026-09-14T16:17:19.513
- **官方描述（原文）**：TripleLift's ad rendering script (video-bundle.js) contains a DOM-based cross-site scripting vulnerability that allows unauthenticated attackers to execute arbitrary JavaScript in a publisher's domain by sending crafted postMessage payloads without origin validation. Attackers can cause a victim to visit an attacker-controlled page that sends malicious postMessage events to a publisher page running the ad script, enabling session hijacking and unauthorized DOM manipulation.

### 106. CVE-2023-37253｜MediaWiki / ProofreadPage
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T06:16:53.740)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.1 (LOW)
- **EPSS**：0.00197 / percentile=0.09576
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T06:16:53.740 / 2026-09-14T16:17:04.600
- **官方描述（原文）**：An issue was discovered in the ProofreadPage extension for MediaWiki through 1.39.3. It leaks information about a suppressed user via the API and config variables.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-76461｜Cisco / Secure Email Gateway
- **Title**：Cisco Secure Email Gateway SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-14 / due_date=2026-09-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco AsyncOS software for Cisco Secure Email Gateway (SEG) contains a SQL injection vulnerability that could allow an unauthenticated, remote attacker to execute arbitrary commands with root privileges on the underlying operating system.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-90942 | P3 / 38 | casdoor / casdoor | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90919 | P3 / 38 | ModelTC / LightLLM | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-61534 | P3 / 38 | confetti / yayson | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57131 | P3 / 38 | MervinPraison / PraisonAI | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57127 | P3 / 38 | MervinPraison / PraisonAI | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57125 | P3 / 38 | MervinPraison / PraisonAI | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57124 | P3 / 38 | MervinPraison / PraisonAI | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-91080 | WATCH / 30 | adnanh / webhook | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90946 | WATCH / 30 | AsyncFuncAI / deepwiki-open | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90944 | WATCH / 30 | krayin / laravel-crm | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90939 | WATCH / 30 | 201206030 / novel-plus | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90938 | WATCH / 30 | langbot-app / LangBot | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90933 | WATCH / 30 | laradashboard / laradashboard | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90930 | WATCH / 30 | filebrowser / filebrowser | v4.0 7.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90928 | WATCH / 30 | filebrowser / filebrowser | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90699 | WATCH / 30 | D-Link / DWR-M920 | v4.0 8.6 (HIGH) | 0.01593 / percentile=0.74312 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77884 | WATCH / 30 | Brain Trust / Gallery - Private Photo Vault | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-70658 | WATCH / 30 | pay-rails / pay | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57579 | WATCH / 30 | AlchemyCMS / alchemy_cms | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57130 | WATCH / 30 | MervinPraison / praisonaiagents | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57129 | WATCH / 30 | MervinPraison / praisonaiagents | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57126 | WATCH / 30 | MervinPraison / PraisonAI | v3.1 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-56839 | WATCH / 30 | MervinPraison / PraisonAI | v3.1 7.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55451 | WATCH / 30 | locize / gettext-converter | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55072 | WATCH / 30 | pimcore / pimcore | v3.1 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-47253 | WATCH / 30 | julien040 / anyquery | v3.1 7.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90961 | WATCH / 28 | MISP / MISP | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-90945 | WATCH / 28 | crawlab-team / crawlab | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-90943 | WATCH / 28 | parallax / filament-comments | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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
- EPSS 未確認：29；Exploitation status 未確認：1。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-15T05:36:01.496229+00:00`；Delta generated at：`2026-09-15T05:36:01.496229+00:00`。

---

## 可驗證資料來源

- **CVE-2026-76461** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76461) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-90942** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90942)
- **CVE-2026-90919** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90919)
- **CVE-2026-61534** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61534)
- **CVE-2026-57131** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57131)
- **CVE-2026-57127** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57127)
- **CVE-2026-57125** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57125)
- **CVE-2026-57124** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57124)
- **CVE-2026-91080** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91080)
- **CVE-2026-90946** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90946)
- **CVE-2026-90944** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90944)
- **CVE-2026-90939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90939)
- **CVE-2026-90938** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90938)
- **CVE-2026-90933** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90933)
- **CVE-2026-90930** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90930)
- **CVE-2026-90928** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90928)
- **CVE-2026-90699** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90699) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90699)
- **CVE-2026-77884** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77884)
- **CVE-2026-70658** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70658)
- **CVE-2026-57579** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57579)
- **CVE-2026-57130** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57130)
- **CVE-2026-57129** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57129)
- **CVE-2026-57126** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57126)
- **CVE-2026-56839** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56839)
- **CVE-2026-55451** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55451)
- **CVE-2026-55072** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55072)
- **CVE-2026-47253** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47253)
- **CVE-2026-90961** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90961)
- **CVE-2026-90945** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90945)
- **CVE-2026-90943** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90943)
- **CVE-2026-90937** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90937)
- **CVE-2026-90898** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90898)
- **CVE-2026-90693** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90693) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90693)
- **CVE-2026-90692** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90692) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90692)
- **CVE-2026-87802** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87802)
- **CVE-2026-87785** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87785)
- **CVE-2026-86460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86460)
- **CVE-2026-85192** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85192) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85192)
- **CVE-2026-82441** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82441)
- **CVE-2026-82439** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82439)
- **CVE-2026-82435** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82435)
- **CVE-2026-82434** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82434)
- **CVE-2026-82431** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82431)
- **CVE-2026-82232** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82232)
- **CVE-2026-78330** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78330)
- **CVE-2026-78299** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78299)
- **CVE-2026-77181** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77181)
- **CVE-2026-77051** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77051)
- **CVE-2026-76443** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76443)
- **CVE-2026-76441** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76441)
- **CVE-2026-76440** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76440)
- **CVE-2026-75030** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75030)
- **CVE-2026-73668** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73668)
- **CVE-2026-73579** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73579)
- **CVE-2026-73470** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73470)
- **CVE-2026-73370** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73370)
- **CVE-2026-67399** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67399)
- **CVE-2026-65414** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65414)
- **CVE-2026-59178** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59178)
- **CVE-2026-57578** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57578)
- **CVE-2026-57145** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57145)
- **CVE-2026-57123** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57123)
- **CVE-2026-55209** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55209)
- **CVE-2026-54334** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54334)
- **CVE-2026-54333** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54333)
- **CVE-2026-53713** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53713)
- **CVE-2026-50006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-50006)
- **CVE-2026-21391** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21391)
- **CVE-2026-20353** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20353)
- **CVE-2026-16338** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16338)
- **CVE-2026-12944** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12944)
- **CVE-2026-12258** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12258)
- **CVE-2026-90936** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90936)
- **CVE-2026-90935** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90935)
- **CVE-2026-90931** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90931)
- **CVE-2026-90808** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90808)
- **CVE-2026-90789** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90789)
- **CVE-2026-90787** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90787)
- **CVE-2026-90784** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90784)
- **CVE-2026-90715** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90715)
- **CVE-2026-90701** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90701)
- **CVE-2026-90691** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90691) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90691)
- **CVE-2026-90686** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90686) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90686)
- **CVE-2026-57128** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57128)
- **CVE-2026-55832** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55832)
- **CVE-2026-55093** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55093)
- **CVE-2026-53708** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53708)
- **CVE-2026-53496** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53496)
- **CVE-2026-47256** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47256)
- **CVE-2025-24890** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-24890)
- **CVE-2024-23176** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-23176) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2024-23176)
- **CVE-2023-40772** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-40772) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-40772)
- **CVE-2026-90813** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90813)
- **CVE-2026-90811** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90811)
- **CVE-2026-90803** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90803)
- **CVE-2026-90801** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90801)
- **CVE-2026-90794** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90794)
- **CVE-2026-90792** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90792)
- **CVE-2026-90712** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90712)
- **CVE-2026-90709** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90709)
- **CVE-2026-90706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90706)
- **CVE-2026-90704** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90704)
- **CVE-2026-90696** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90696) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90696)
- **CVE-2026-90694** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90694) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90694)
- **CVE-2026-82019** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82019)
- **CVE-2023-37253** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-37253) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-37253)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
