# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**236** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=236。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **3**、WATCH **27**。
- Baseline：state / generated_at=2026-09-15T05:36:01.496229+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **200** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-91932｜FlowiseAI / Flowise
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:44.030)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:44.030 / 2026-09-15T17:17:40.043
- **官方描述（原文）**：Flowise before 3.1.4 contains a validation bypass vulnerability in MCP server configuration allowing authenticated attackers remote code execution through an unvalidated cwd parameter. Attackers can bypass path validation using clean filenames in the args array while controlling the working directory to execute malicious code.

### 2. CVE-2024-14029｜tornadoweb / tornado
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:06.893)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:06.893 / 2026-09-15T18:17:11.567
- **官方描述（原文）**：Tornado before 6.4.1 ignores duplicate Transfer-Encoding: chunked headers, treating requests as having no message body and parsing the chunked body as a subsequent request. Attackers can exploit this inconsistency when Tornado is deployed behind proxies to perform HTTP request smuggling, enabling access control bypass, cache poisoning, or connection desynchronization.

### 3. CVE-2023-54398｜Yonyou / U8 Cloud
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T17:17:08.343)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T17:17:08.343 / 2026-09-15T18:17:10.417
- **官方描述（原文）**：Yonyou U8 Cloud contains an unauthenticated Java deserialization vulnerability in the nc.impl.pub.filesystem.FileManageServlet component that allows remote unauthenticated attackers to execute arbitrary OS commands by sending a serialized payload via POST request. Attackers can exploit the doAction method, which passes raw HTTP request body data directly to ObjectInputStream.readObject() without filtering, to achieve remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2025-02-13.

### 4. CVE-2026-91994｜semaphoreui / semaphore
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T12:17:54.793)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T12:17:54.793 / 2026-09-15T13:16:47.380
- **官方描述（原文）**：Semaphore UI through 2.19.12 exempts GET and HEAD requests from project resource permission checks in GetMustCanMiddleware. Attackers with guest or task_runner roles can read all project environments including plaintext secrets, credentials, and passwords via GET requests to the environment endpoint.

### 5. CVE-2026-91990｜tornadoweb / tornado
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:58.147)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:58.147 / 2026-09-15T17:17:44.627
- **官方描述（原文）**：Tornado before 6.5.8 contains a memory amplification vulnerability in parse_multipart_form_data that splits multipart data before validating the max_parts limit. Attackers can send crafted multipart requests with many parts to create large transient lists, exhausting server memory and causing denial of service.

### 6. CVE-2026-91985｜go-vikunja / vikunja
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:57.010)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:57.010 / 2026-09-15T17:17:44.127
- **官方描述（原文）**：Vikunja before 2.6.0 fails to properly restrict access to the link-share hash field in single-share read endpoints, allowing read-only members to obtain the share's secret credential. Attackers can exchange the disclosed hash for a link-share JWT at the share's permission level to escalate privileges and perform unauthorized writes or administrative actions.

### 7. CVE-2026-91973｜go-vikunja / vikunja
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:54.230)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:54.230 / 2026-09-15T16:17:54.230
- **官方描述（原文）**：Vikunja before 2.6.0 contains an authentication bypass vulnerability in CalDAV BasicAuth endpoints that lack rate limiting protection. Remote unauthenticated attackers can issue unbounded credential-guessing requests against /dav, /.well-known, and /feeds routes to bypass the instance's anti-brute-force controls and compromise password-only accounts.

### 8. CVE-2026-91970｜go-vikunja / vikunja
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:53.803)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:53.803 / 2026-09-15T17:17:43.110
- **官方描述（原文）**：Vikunja versions before 2.6.0 contain a resource exhaustion vulnerability in the Planka migrator that fails to enforce aggregate memory budgets during migration jobs. Authenticated attackers can submit migration requests pointing to attacker-controlled servers advertising numerous size-compliant attachments, exhausting worker memory and causing denial of service for all users.

### 9. CVE-2026-91968｜go-vikunja / vikunja
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:53.093)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:53.093 / 2026-09-15T16:17:53.093
- **官方描述（原文）**：vikunja versions before 2.6.0 contain a resource exhaustion vulnerability in the task-filter endpoint that accepts deeply nested filter expressions without recursion depth limits. Authenticated attackers can supply thousands of nested parentheses in the filter query parameter to exhaust memory and terminate the API process.

### 10. CVE-2026-91965｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:52.643)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:52.643 / 2026-09-15T17:17:42.600
- **官方描述（原文）**：WWBN AVideo through 29.0 fails to enforce user-group restrictions in the plugin/Live/stats.json.php and plugin/Live/calendar.json.php endpoints. Unauthenticated attackers can retrieve restricted live transmission details including stream keys, titles, descriptions, owner information, and direct HLS playback URLs by accessing these endpoints.

### 11. CVE-2026-91963｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:51.907)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:51.907 / 2026-09-15T16:17:51.907
- **官方描述（原文）**：FreeRDP versions before 3.31.0 contain an uninitialized heap memory disclosure vulnerability in the urbdrc USB redirection channel. A malicious RDP server can induce failing USB transfers to read uninitialized heap memory from the client, defeating ASLR and enabling remote code execution when chained with memory corruption vulnerabilities.

### 12. CVE-2026-91960｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:51.070)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:51.070 / 2026-09-15T16:17:51.070
- **官方描述（原文）**：FreeRDP versions before 3.31.0 contain an integer overflow in WinPR's Stream_EnsureRemainingCapacity function that allows remote attackers to cause denial of service. A malicious RD Gateway peer can send a WebSocket Ping frame with a crafted 64-bit extended payload length to trigger integer wraparound, resulting in a double free that crashes the FreeRDP client during connection.

### 13. CVE-2026-91955｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:49.963)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:49.963 / 2026-09-15T16:17:49.963
- **官方描述（原文）**：FreeRDP before 3.31.0 fails to validate client-supplied DesktopWidth and DesktopHeight values during GCC negotiation, allowing remote attackers to crash the server. Attackers can send crafted RDP packets with zero or oversized dimensions to trigger division-by-zero or assertion failures in multifragment update capability calculations, terminating the server process.

### 14. CVE-2026-91953｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:49.657)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:49.657 / 2026-09-15T17:17:41.587
- **官方描述（原文）**：FreeRDP versions before 3.31.0 contain a heap buffer overflow vulnerability in nego_send_negotiation_request() that fails to validate the LB_LOAD_BALANCE_INFO field length before writing to a fixed 512-byte buffer. A malicious RDP server or man-in-the-middle can send a Server Redirection PDU with an oversized LB_LOAD_BALANCE_INFO value to overflow the buffer with attacker-controlled content, causing denial of service or heap corruption before authentication completes.

### 15. CVE-2026-91950｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:48.800)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:48.800 / 2026-09-15T16:17:48.800
- **官方描述（原文）**：FreeRDP before 3.31.0 contains an out-of-bounds read vulnerability in the rdpdr_dump_packet function due to 32-bit unsigned integer wraparound in buffer bounds validation. A malicious RDP server can send a crafted RDPDR packet with computerNameLen set to 0xFFFFFFF0 to bypass bounds checks and trigger memory reads past the packet buffer, causing client crashes or heap disclosure in logs.

### 16. CVE-2026-91945｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:46.657)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:46.657 / 2026-09-15T16:17:46.657
- **官方描述（原文）**：FreeRDP versions before 3.31.0 contain an out-of-bounds read vulnerability in smartcard response decoders that fail to validate ATR length fields against fixed inline arrays. Authenticated RDP clients can send oversized ATR lengths in PAKID_CORE_DEVICE_IOCOMPLETION responses to trigger reads past stack or heap objects, causing process termination.

### 17. CVE-2026-91943｜unclecode / crawl4ai
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:46.290)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:46.290 / 2026-09-15T17:17:40.553
- **官方描述（原文）**：Crawl4AI before 0.9.3 contains a server-side request forgery vulnerability in PDFContentScrapingStrategy where _get_pdf_path() re-downloads targets with Python requests without egress validation. Authenticated attackers can supply URLs that redirect to internal addresses or use DNS rebinding to access internal services, exfiltrating responses through PDF text extraction in crawl results.

### 18. CVE-2026-91940｜unclecode / crawl4ai
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:45.460)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:45.460 / 2026-09-15T16:17:45.460
- **官方描述（原文）**：crawl4ai before 0.9.3 contains an arbitrary file write vulnerability in PDFContentScrapingStrategy where the _filter_untrusted_fields function fails to validate untrusted configuration fields. Attackers can submit crafted config bodies with malicious image_save_dir paths to write attacker-controlled bytes into any directory accessible to the service account.

### 19. CVE-2026-91925｜polyaxon / polyaxon
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:13.220)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:13.220 / 2026-09-15T13:16:46.980
- **官方描述（原文）**：Polyaxon through 2.16.4 renders operation specification fields with an unsandboxed Jinja2 environment during server-side run preparation, allowing authenticated users to execute arbitrary code. Attackers can submit runs with Jinja2 payloads in queue, namespace, conditions, presets, or dependencies fields to execute operating system commands in the scheduler process context, exposing database credentials and service tokens.

### 20. CVE-2026-91003｜D-Link / DI-8300
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T06:17:01.387)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：0.00512 / percentile=0.42167
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T06:17:01.387 / 2026-09-15T15:17:31.133
- **官方描述（原文）**：A flaw has been found in D-Link DI-8300 16.07. The affected element is the function rzgl_asp of the file /rzgl.asp of the component CGI Service. This manipulation of the argument redirct_url causes stack-based buffer overflow. Remote exploitation of the attack is possible. The exploit has been published and may be used.

### 21. CVE-2026-91001｜D-Link / DI-8400
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T06:16:59.970)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：0.00484 / percentile=0.40372
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T06:16:59.970 / 2026-09-15T15:17:30.983
- **官方描述（原文）**：A security flaw has been discovered in D-Link DI-8400 16.07. This affects the function ddns_asp of the file /ddns.asp of the component DDNS Configuration. Performing a manipulation of the argument serv/user/host/wild/mx/bmx/cust/ip results in stack-based buffer overflow. The attack can be initiated remotely. The exploit has been released to the public and may be used for attacks.

### 22. CVE-2026-88616｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T15:17:24.887)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T15:17:24.887 / 2026-09-15T20:19:19.003
- **官方描述（原文）**：An issue in RuoYi-Vue-Plus 6.0.0 allows a remote attacker to execute arbitrary code via the FlwTaskController.java component, and the FlwTaskServiceImpl.completeTask, CompleteExecuteComponent.process, Warm-Flow TaskService.skip, POST /workflow/task/completeTask components

### 23. CVE-2026-85013｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:34.543)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:34.543 / 2026-09-15T18:19:34.813
- **官方描述（原文）**：A flaw was found in environment-modules. A local attacker can exploit this vulnerability by placing a maliciously named modulefile in a location visible to the victim's `MODULEPATH`. When the victim uses Bash completion for `module` or `ml` commands, the malicious module name, containing shell metacharacters, is evaluated as a command. This can lead to arbitrary command execution in the completing user's shell, impacting their confidentiality, integrity, and availability.

### 24. CVE-2026-79425｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T15:17:21.947)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T15:17:21.947 / 2026-09-15T19:17:40.427
- **官方描述（原文）**：An authenticated Server-Side Request Forgery (SSRF) in the /adminapi/file/online_upload component of CRMEB v6.0.0 allows attackers to scan internal resources via a crafted POST request.

### 25. CVE-2026-79410｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T19:17:39.943)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T19:17:39.943 / 2026-09-15T20:17:57.927
- **官方描述（原文）**：Improper validation of the quantity parameter in the add-to-cart path of Webkul Bagisto v2.4.9 allows authenticated attackers to reduce their order total below the legitimate price of shippable goods.

### 26. CVE-2026-59160｜DerYeger / yeger
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T17:17:23.410)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T17:17:23.410 / 2026-09-15T18:17:26.587
- **官方描述（原文）**：Yeger is a monorepo for npm packages maintained under the yeger scope. Prior to 2.8.9, the turbo-graph package starts its embedded Next.js server from packages/turbo-graph/src/index.ts on all interfaces, including 0.0.0.0:29312 by default, while the GET handler for /api/run in packages/turbo-graph-ui/app/api/run/route.ts has no authentication, authorization, CSRF protection, or task allowlist. The handler accepts the tasks, filter, and force query parameters, and buildResponseFromArgs passes attacker-selected task names to spawn() as Turbo CLI arguments. An adjacent-network attacker can execute any task defined in the victim repository's turbo.json with the privileges of the developer OS user, potentially exposing secrets, modifying files or infrastructure, or causing destructive availability effects. The use of an argument array prevents traditional shell metacharacter injection but does not prevent unauthorized execution of defined tasks. This issue is fixed in version 2.8.9.

### 27. CVE-2026-58485｜ihor-sokoliuk / mcp-searxng
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T18:17:26.040)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T18:17:26.040 / 2026-09-15T19:17:31.393
- **官方描述（原文）**：mcp-searxng is a Model Context Protocol server that gives AI assistants web search and URL-reading capabilities through SearXNG. Prior to 1.7.1, web_url_read receives its caller-controlled URL through src/index.ts and validates only the literal hostname in assertUrlAllowed() within src/url-reader.ts before undiciFetch() performs operating-system DNS resolution. A public-looking attacker-controlled hostname that resolves to a private, loopback, link-local, or cloud-metadata address therefore passes the lexical check and causes the MCP server to connect to the internal destination. In the default HTTP configuration, an unauthenticated network client can use this path to read internal services, expose credentials or service tokens, and enumerate reachable internal hosts; in STDIO deployments, prompt-influenced tool selection can provide the malicious URL. Direct private IP literals are blocked, and MCP_HTTP_ALLOW_PRIVATE_URLS remains an explicit opt-out. This issue is fixed in version 1.7.1.

### 28. CVE-2026-58483｜ihor-sokoliuk / mcp-searxng
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T18:17:25.873)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T18:17:25.873 / 2026-09-15T19:17:31.290
- **官方描述（原文）**：mcp-searxng is a Model Context Protocol server that gives AI assistants web search and URL-reading capabilities through SearXNG. Prior to 1.7.1, web_url_read in src/index.ts passes a caller-supplied URL to readUrlContent() in src/url-reader.ts, where checkContentLength() treats a missing Content-Length header as an inconclusive preflight and the normal and error paths then consume the complete body with response.text(). A server that omits Content-Length can therefore bypass URL_READ_MAX_CONTENT_LENGTH_BYTES and force unbounded memory use. The resulting string is also processed by NodeHtmlMarkdown.translate(), increasing CPU consumption and allowing an unauthenticated HTTP client to cause denial of service. This issue is fixed in version 1.7.1.

### 29. CVE-2026-57137｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:11.030)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00442 / percentile=0.37448
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:11.030 / 2026-09-15T14:45:28.563
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. From 1.4.0 until 1.7.2, createAgentLoop() in src/praisonai-ts/src/ai/agent-loop.ts passes executable tools to generateText() before invoking the onToolCall approval callback. Because the wrapped AI SDK executes tool handlers during generation, a callback that returns false records tool_rejected only after the denied tool has already produced side effects and populated toolResults. Applications using onToolCall as a human or policy approval boundary can therefore execute rejected file, command, API, or data-modifying operations. This issue is fixed in version 1.7.2.

### 30. CVE-2026-57136｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:10.883)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00764 / percentile=0.53496
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:10.883 / 2026-09-15T14:45:28.563
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. From 1.2.3 until 1.7.2, CommandValidator in src/praisonai-ts/src/cli/features/sandbox-executor.ts validates only the first whitespace-delimited executable against allowedCommands, then SandboxExecutor passes the complete command string to sh -c. A command beginning with an allowed executable can append a non-allowlisted command through shell metacharacters, causing arbitrary commands to run with the PraisonAI process privileges. This issue is fixed in version 1.7.2.

### 31. CVE-2026-57135｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:10.733)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.6 (HIGH)
- **EPSS**：0.00412 / percentile=0.34728
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:10.733 / 2026-09-15T14:45:28.563
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. From 1.2.3 until 1.7.2, SandboxExecutor network-isolated mode in src/praisonai-ts/src/cli/features/sandbox-executor.ts uses buildEnv() only to inject invalid http_proxy and https_proxy environment variables and does not establish an operating-system network boundary. Programs that ignore those proxy variables can open sockets directly, allowing supposedly isolated commands to reach localhost, internal services, cloud metadata, or external hosts and potentially exfiltrate data. An initial remediation was released in version 1.7.2.

### 32. CVE-2026-57134｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:10.583)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：0.00429 / percentile=0.36343
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:10.583 / 2026-09-15T14:45:28.563
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. From 1.5.1 until 1.7.2, MCPSecurity.evaluatePolicy() in src/praisonai-ts/src/mcp/security.ts invokes the configured credential validator only when AuthMethod is api-key or bearer. Basic and OAuth policies accept any non-empty Authorization header without calling auth.validate(), then return an authenticated result, allowing callers with invalid credentials to access MCP tools and resources protected by those policies. This issue is fixed in version 1.7.2.

### 33. CVE-2026-56829｜shopperlabs / shopper
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T18:17:24.957)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T18:17:24.957 / 2026-09-15T19:17:23.530
- **官方描述（原文）**：Shopper is a Headless e-commerce Admin Panel. Prior to 2.9.2, packages/admin/src/Livewire/Components/Products/VariantStock.php exposes stockAction() without edit_product_variants authorization and leaves public $variant client mutable because it lacks the Livewire Locked attribute. Any authenticated admin-panel user, including staff with only browse_products, can select an arbitrary product variant and inventory location through component state, then submit a positive or negative quantity adjustment. This permits browse-only staff to inflate stock, reduce stock, or force out-of-stock states for variants outside the current page. This issue is fixed in version 2.9.2.

### 34. CVE-2026-56827｜shopperlabs / shopper
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T18:17:24.823)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T18:17:24.823 / 2026-09-15T19:17:23.360
- **官方描述（原文）**：Shopper is a Headless e-commerce Admin Panel. Prior to 2.9.2, groupedBulkActions in packages/admin/src/Livewire/Pages/Attribute/Browse.php, packages/admin/src/Livewire/Pages/Tag/Index.php, packages/admin/src/Livewire/Pages/Brand/Index.php, packages/admin/src/Livewire/Pages/Category/Index.php, and packages/admin/src/Livewire/Pages/Supplier/Index.php omit server-side authorization while the pages require only browse_attributes, browse_tags, browse_brands, browse_categories, or browse_suppliers. A browse-only staff user can invoke DeleteBulkAction to mass delete attributes or tags and can invoke BulkAction::make('enabled') or BulkAction::make('disabled') to change attribute, brand, category, or supplier visibility. These operations can break product variants and substantially disrupt storefront catalog visibility. Per-record actions and the comparison pages identified by the advisory are correctly authorized and are not affected. This issue is fixed in version 2.9.2.

### 35. CVE-2026-55692｜StarCitizenWiki / mediawiki-extensions-EmbedVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T17:17:22.330)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T17:17:22.330 / 2026-09-15T19:17:22.670
- **官方描述（原文）**：The EmbedVideo Extension is a MediaWiki extension which adds a parser function called #ev and various parser tags for embedding video clips from various video sharing services. Prior to 4.1.0, with the default $wgEmbedVideoRequireConsent configuration enabled, includes/EmbedService/EmbedHtmlFormatter.php places JSON returned through includes/EmbedService/AbstractEmbedService.php into the data-mw-iframeconfig attribute without safely escaping single quotes. Attacker-controlled archiveorg identifiers and wistia or sharepoint URLs accepted by the affected service validators can cause getUrl() output to terminate the attribute and inject event-handler attributes into the generated figure element. A user able to edit a wiki page can store JavaScript that executes in the wiki origin when visitors render the page. This issue is fixed in version 4.1.0.

### 36. CVE-2026-52484｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T18:17:22.010)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T18:17:22.010 / 2026-09-15T19:17:20.073
- **官方描述（原文）**：An issue in MitraStar GPT-2742GX4X5v6-SV GL_g2.5_100XNT0b23_3 allows an authenticated attacker to execute arbitrary code via the /cgi-bin/device-management-utilities-internet.cgi component

### 37. CVE-2026-91998｜casdoor / casdoor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T12:17:55.407)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T12:17:55.407 / 2026-09-15T12:17:55.407
- **官方描述（原文）**：Casdoor through 4.4.0 contains an authorization bypass vulnerability in the /api/mcp endpoint that allows attackers with any application's clientId and clientSecret to gain unrestricted access to user administration across all organizations. Attackers can enumerate user records including password salts and email addresses, create administrator accounts, modify existing users, and delete them in any organization by supplying legitimate credentials from a single application.

### 38. CVE-2026-91995｜pig-mesh / pig
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T12:17:54.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T12:17:54.943 / 2026-09-15T12:17:54.943
- **官方描述（原文）**：pig before 4.1.0 contains an authentication bypass vulnerability in the /register/password endpoint where password verification results are discarded, allowing any value as the current password. Remote attackers can submit a username with an incorrect current password to overwrite any account credential including the admin account and gain full administrative control.

### 39. CVE-2026-91988｜dep0we / atomic-agents-stack
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:57.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:57.450 / 2026-09-15T16:17:57.450
- **官方描述（原文）**：atomic-agents-stack before 1.1.0 accepts cleartext HTTP schemes in the HTTP MCP server-registry backend factory, allowing network man-in-the-middle attackers to rewrite catalog responses. Attackers can inject arbitrary command and argument values that are spawned as local subprocesses by MCPClientPool to achieve code execution on the agent host.

### 40. CVE-2026-91949｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:48.653)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:48.653 / 2026-09-15T16:17:48.653
- **官方描述（原文）**：FreeRDP server versions before 3.31.0 contain a protocol negotiation bypass vulnerability that allows unauthenticated attackers to establish RDSTLS connections despite server policy disabling them. Attackers can send incompatible protocol requests, receive negotiation failures, then complete TLS handshake and enter RDSTLS to bypass pre-authentication transport restrictions.

### 41. CVE-2026-91939｜Cotonti / Cotonti
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T21:16:48.957)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T21:16:48.957 / 2026-09-15T21:16:48.957
- **官方描述（原文）**：Cotonti 1.0.0 Comments plugin passes the ci GET parameter to unserialize() without allowed_classes restriction, allowing unauthenticated attackers to instantiate arbitrary PHP classes with attacker-controlled properties. Attackers can exploit PHP object injection through crafted serialized payloads to trigger gadget chains and achieve database manipulation or code execution.

### 42. CVE-2026-91931｜FlowiseAI / Flowise
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:43.883)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:43.883 / 2026-09-15T16:17:43.883
- **官方描述（原文）**：Flowise before 3.1.4 contains a remote code execution vulnerability in the Custom MCP node that allows authenticated attackers to execute arbitrary code by supplying npx package names in the mcpServerConfig parameter. Attackers can invoke npx with attacker-controlled npm packages to execute code on the Flowise server.

### 43. CVE-2026-91749｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T21:16:48.833)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T21:16:48.833 / 2026-09-16T00:17:29.510
- **官方描述（原文）**：Use after free in Workers in Google Chrome prior to 153.0.8010.47 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 44. CVE-2026-91728｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T21:16:46.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T21:16:46.130 / 2026-09-16T00:17:22.110
- **官方描述（原文）**：Integer overflow in V8 in Google Chrome prior to 153.0.8010.47 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 45. CVE-2026-90711｜proxy-addr / proxy-addr
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T07:16:33.683)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00187 / percentile=0.08526
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T07:16:33.683 / 2026-09-15T15:17:29.273
- **官方描述（原文）**：proxy-addr is a Node.js module that determines a request's client address behind trusted reverse proxies, and it backs Express req.ip and req.ips. In versions 1.1.0 through 2.0.7, a trust subnet written in IPv4-mapped IPv6 notation with an IPv4-sized prefix, such as ::ffff:10.0.0.0/8 instead of the correct ::ffff:10.0.0.0/104, is accepted without error but trusts every IPv4 address on the internet rather than the block it names. Because the socket peer then becomes trusted at hop 0, any unauthenticated client can supply an arbitrary X-Forwarded-For header and control the address the application reads, which defeats IP-based access control, rate limiting, geolocation, and audit logging. This is a fail-open regression introduced in version 1.1.0. The issue is fixed in proxy-addr 2.0.8, and users should upgrade to 2.0.8 or later. As a workaround, ensure any IPv4-mapped IPv6 trust subnet uses a prefix length of at least 97, or express the range in plain IPv4 notation.

### 46. CVE-2026-89308｜TREXOM / TrxTimeATTENDANCE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T12:17:53.603)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T12:17:53.603 / 2026-09-15T13:16:45.543
- **官方描述（原文）**：An unauthenticated OS command injection vulnerability exists in the ping.php endpoint, allowing remote attackers to execute arbitrary commands on the underlying operating system and achieve remote code execution.

### 47. CVE-2026-89040｜Tencent / Mass Service Engine in Cluster (MSEC)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:20.240)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:20.240 / 2026-09-15T20:19:20.240
- **官方描述（原文）**：Tencent Mass Service Engine in Cluster (MSEC) allows a remote, unauthenticated attacker to send a crafted POST request including ../ and gain root access on the target device. An attacker who uploads a webshell can execute arbitrary code as root.

### 48. CVE-2026-89026｜Issabel Foundation / Issabel Framework
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T17:17:33.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T17:17:33.510 / 2026-09-15T17:17:33.510
- **官方描述（原文）**：The Issabel Framework, the web framework supporting Issabel PBX software, before commit b97dbaf contains a hard-coded HS256 JWT signing key in the pbxapi index.php file that is identical across every installation, allowing unauthenticated remote attackers to forge valid bearer tokens. Attackers can use the forged token to call the manager originate endpoint with the System application parameter, causing Asterisk to execute arbitrary OS commands as the Asterisk user. Exploitation evidence was first observed by the Shadowserver Foundation on 2026-09-09.

### 49. CVE-2026-89022｜bookstackapp / bookstack
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T17:17:33.360)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T17:17:33.360 / 2026-09-15T19:17:45.647
- **官方描述（原文）**：BookStack before 26.05.5 contains an authentication bypass vulnerability in its social login implementation that allows unauthenticated attackers to sign in as arbitrary users by authenticating through a different social provider sharing the same driver_id namespace. Attackers can authenticate at one enabled social provider using a user ID that matches an account linked to a different social provider, bypassing credential verification entirely because the SocialAuthService::handleLoginCallback query ignores the driver column when retrieving linked account records.

### 50. CVE-2026-87230｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:11.513)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:11.513 / 2026-09-15T20:19:11.513
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Financial Management. While the vulnerability is in Oracle Hyperion Financial Management, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Financial Management accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Financial Management accessible data. CVSS 3.1 Base Score 10.0 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N).

### 51. CVE-2026-87223｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:10.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:10.630 / 2026-09-15T20:19:10.630
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Financial Management. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Financial Management accessible data and unauthorized ability to cause a hang or frequently repeatable crash (complete DOS) of Oracle Hyperion Financial Management. CVSS 3.1 Base Score 9.1 (Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H).

### 52. CVE-2026-87217｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:09.983)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:09.983 / 2026-09-15T23:19:13.370
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Financial Management. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Financial Management accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Financial Management accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 53. CVE-2026-87214｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:09.660)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:09.660 / 2026-09-15T20:19:09.660
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle Hyperion Financial Management. While the vulnerability is in Oracle Hyperion Financial Management, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Financial Management. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 54. CVE-2026-87189｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:06.840)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:06.840 / 2026-09-15T20:19:06.840
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows high privileged attacker with network access via Oracle Net to compromise Oracle Hyperion Financial Management. While the vulnerability is in Oracle Hyperion Financial Management, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Financial Management. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 55. CVE-2026-87188｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:06.727)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:06.727 / 2026-09-15T23:19:13.243
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Financial Management. Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Financial Management. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 56. CVE-2026-87186｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:06.507)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:06.507 / 2026-09-15T20:19:06.507
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with access to the physical communication segment attached to the hardware where the Oracle Hyperion Financial Management executes to compromise Oracle Hyperion Financial Management. While the vulnerability is in Oracle Hyperion Financial Management, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Financial Management. CVSS 3.1 Base Score 9.6 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 57. CVE-2026-87184｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:06.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:06.290 / 2026-09-15T23:19:13.113
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via SQL to compromise Oracle Hyperion Financial Management. Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Financial Management. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 58. CVE-2026-87176｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:05.403)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:05.403 / 2026-09-15T23:19:12.983
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via TCP to compromise Oracle Hyperion Financial Management. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Financial Management accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Financial Management accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 59. CVE-2026-87175｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:05.297)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:05.297 / 2026-09-15T23:19:12.853
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via TCP to compromise Oracle Hyperion Financial Management. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Financial Management accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Financial Management accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 60. CVE-2026-87173｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:05.073)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:05.073 / 2026-09-15T23:19:12.723
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via TCP to compromise Oracle Hyperion Financial Management. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Financial Management accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Financial Management accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 61. CVE-2026-87172｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:04.970)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:04.970 / 2026-09-15T20:19:04.970
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Hyperion Financial Management. While the vulnerability is in Oracle Hyperion Financial Management, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Financial Management. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 62. CVE-2026-87170｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:19:04.747)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:19:04.747 / 2026-09-15T23:19:12.593
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Financial Management. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Financial Management accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Financial Management accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 63. CVE-2026-87129｜Oracle Corporation / Oracle Hyperion Data Relationship Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:59.933)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:59.933 / 2026-09-15T23:19:12.467
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Data Relationship Management. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Data Relationship Management accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Data Relationship Management accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 64. CVE-2026-87128｜Oracle Corporation / Oracle Hyperion Data Relationship Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:59.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:59.820 / 2026-09-15T23:19:12.333
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Data Relationship Management. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Data Relationship Management accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Data Relationship Management accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 65. CVE-2026-83462｜Oracle Corporation / Oracle Mobile Application Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:55.030)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:55.030 / 2026-09-15T23:19:06.670
- **官方描述（原文）**：Vulnerability in the Oracle Mobile Application Server product of Oracle E-Business Suite (component: MWA Terminal Server). Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows unauthenticated attacker with network access via TCP to compromise Oracle Mobile Application Server. Successful attacks of this vulnerability can result in takeover of Oracle Mobile Application Server. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 66. CVE-2026-83452｜Oracle Corporation / Oracle Document Management and Collaboration
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:53.950)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:53.950 / 2026-09-15T23:19:06.547
- **官方描述（原文）**：Vulnerability in the Oracle Document Management and Collaboration product of Oracle E-Business Suite (component: Internal Operations). Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Document Management and Collaboration. Successful attacks of this vulnerability can result in takeover of Oracle Document Management and Collaboration. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 67. CVE-2026-83355｜Oracle Corporation / Oracle Enterprise Manager for Fusion Middleware
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:49.020)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:49.020 / 2026-09-15T23:19:06.417
- **官方描述（原文）**：Vulnerability in the Oracle Enterprise Manager for Fusion Middleware product of Oracle Enterprise Manager (component: Metrics). Supported versions that are affected are 13.5 and 24.1. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Enterprise Manager for Fusion Middleware. Successful attacks of this vulnerability can result in takeover of Oracle Enterprise Manager for Fusion Middleware. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 68. CVE-2026-83339｜Oracle Corporation / Oracle WebCenter Enterprise Capture
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:47.243)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:47.243 / 2026-09-15T23:19:06.283
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Enterprise Capture. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 69. CVE-2026-83327｜Oracle Corporation / Oracle Applications Framework
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:45.880)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:45.880 / 2026-09-15T23:19:06.163
- **官方描述（原文）**：Vulnerability in the Oracle Applications Framework product of Oracle E-Business Suite (component: Personalization). Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows unauthenticated attacker with network access via SOAP to compromise Oracle Applications Framework. Successful attacks of this vulnerability can result in takeover of Oracle Applications Framework. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 70. CVE-2026-83283｜Oracle Corporation / Oracle Business Intelligence Enterprise Edition
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:40.927)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:40.927 / 2026-09-15T23:19:06.040
- **官方描述（原文）**：Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Platform Security). The supported version that is affected is 12.2.1.4.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Business Intelligence Enterprise Edition. Successful attacks of this vulnerability can result in takeover of Oracle Business Intelligence Enterprise Edition. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 71. CVE-2026-83282｜Oracle Corporation / Oracle Business Intelligence Enterprise Edition
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:40.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:40.820 / 2026-09-15T20:18:40.820
- **官方描述（原文）**：Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Platform Security). The supported version that is affected is 12.2.1.4.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Business Intelligence Enterprise Edition. While the vulnerability is in Oracle Business Intelligence Enterprise Edition, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Business Intelligence Enterprise Edition. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 72. CVE-2026-83269｜Oracle Corporation / Oracle BI Publisher
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:39.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:39.290 / 2026-09-15T23:19:05.917
- **官方描述（原文）**：Vulnerability in the Oracle BI Publisher product of Oracle Analytics (component: BI Platform Security). Supported versions that are affected are 8.2.0.0.0, 12.2.1.4.0 and 26.01.0.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle BI Publisher. Successful attacks of this vulnerability can result in takeover of Oracle BI Publisher. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 73. CVE-2026-83268｜Oracle Corporation / Oracle BI Publisher
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:39.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:39.180 / 2026-09-15T20:18:39.180
- **官方描述（原文）**：Vulnerability in the Oracle BI Publisher product of Oracle Analytics (component: BI Platform Security). Supported versions that are affected are 8.2.0.0.0, 12.2.1.4.0 and 26.01.0.0.0. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle BI Publisher. While the vulnerability is in Oracle BI Publisher, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle BI Publisher. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 74. CVE-2026-83261｜Oracle Corporation / Oracle Product Lifecycle Analytics
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:38.403)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:38.403 / 2026-09-15T23:19:05.790
- **官方描述（原文）**：Vulnerability in the Oracle Product Lifecycle Analytics product of Oracle Supply Chain (component: Core). The supported version that is affected is 3.6.1. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Product Lifecycle Analytics. Successful attacks of this vulnerability can result in takeover of Oracle Product Lifecycle Analytics. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 75. CVE-2026-83260｜Oracle Corporation / Oracle Agile PLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:38.293)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:38.293 / 2026-09-15T20:18:38.293
- **官方描述（原文）**：Vulnerability in the Oracle Agile PLM product of Oracle Supply Chain (component: Event Java PX). The supported version that is affected is 9.3.6. Easily exploitable vulnerability allows high privileged attacker with network access via T3, IIOP to compromise Oracle Agile PLM. While the vulnerability is in Oracle Agile PLM, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Agile PLM. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 76. CVE-2026-83232｜Oracle Corporation / Oracle Data Integrator
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:35.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:35.080 / 2026-09-15T23:19:05.673
- **官方描述（原文）**：Vulnerability in the Oracle Data Integrator product of Oracle Fusion Middleware (component: Console / Repository Explorer). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Data Integrator. Successful attacks of this vulnerability can result in takeover of Oracle Data Integrator. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 77. CVE-2026-83229｜Oracle Corporation / Siebel CRM Deployment
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:34.743)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:34.743 / 2026-09-15T20:18:34.743
- **官方描述（原文）**：Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Siebel Management Console). Supported versions that are affected are 17.0-26.7. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Siebel CRM Deployment. While the vulnerability is in Siebel CRM Deployment, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Siebel CRM Deployment. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 78. CVE-2026-83202｜Oracle Corporation / Siebel CRM Deployment
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:31.763)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:31.763 / 2026-09-15T23:19:05.550
- **官方描述（原文）**：Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Server Infrastructure). Supported versions that are affected are 17.0-26.7. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Siebel CRM Deployment. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Siebel CRM Deployment accessible data as well as unauthorized access to critical data or complete access to all Siebel CRM Deployment accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 79. CVE-2026-83201｜Oracle Corporation / Siebel CRM Deployment
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:31.640)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:31.640 / 2026-09-15T23:19:05.430
- **官方描述（原文）**：Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Server Infrastructure). Supported versions that are affected are 17.0-26.7. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Siebel CRM Deployment. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Siebel CRM Deployment accessible data as well as unauthorized access to critical data or complete access to all Siebel CRM Deployment accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 80. CVE-2026-83197｜Oracle Corporation / Siebel Apps - Financial Services
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:31.167)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:31.167 / 2026-09-15T20:18:31.167
- **官方描述（原文）**：Vulnerability in the Siebel Apps - Financial Services product of Oracle Siebel CRM (component: Financial Accounts). Supported versions that are affected are 17.0-26.7. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Siebel Apps - Financial Services. Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all Siebel Apps - Financial Services accessible data and unauthorized ability to cause a hang or frequently repeatable crash (complete DOS) of Siebel Apps - Financial Services. CVSS 3.1 Base Score 9.1 (Confidentiality and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H).

### 81. CVE-2026-83196｜Oracle Corporation / Siebel CRM Deployment
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:31.057)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:31.057 / 2026-09-15T20:18:31.057
- **官方描述（原文）**：Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Server Infrastructure). Supported versions that are affected are 17.0-26.7. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Siebel CRM Deployment. While the vulnerability is in Siebel CRM Deployment, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Siebel CRM Deployment. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 82. CVE-2026-83154｜Oracle Corporation / Siebel CRM End User
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:26.193)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:26.193 / 2026-09-15T23:19:05.310
- **官方描述（原文）**：Vulnerability in the Siebel CRM End User product of Oracle Siebel CRM (component: Open UI). Supported versions that are affected are 17.0-26.7. Easily exploitable vulnerability allows unauthenticated attacker with network access via SOAP to compromise Siebel CRM End User. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Siebel CRM End User accessible data as well as unauthorized access to critical data or complete access to all Siebel CRM End User accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 83. CVE-2026-83151｜Oracle Corporation / Service Delivery Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:25.857)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:25.857 / 2026-09-15T23:19:05.180
- **官方描述（原文）**：Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via SOAP to compromise Service Delivery Platform. Successful attacks of this vulnerability can result in takeover of Service Delivery Platform. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 84. CVE-2026-83149｜Oracle Corporation / Oracle Application Testing Suite
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:25.637)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:25.637 / 2026-09-15T20:18:25.637
- **官方描述（原文）**：Vulnerability in Oracle Application Testing Suite. The supported version that is affected is 13.3.0.1. Easily exploitable vulnerability allows low privileged attacker having Test Manager for Web Apps privilege with network access via HTTP to compromise Oracle Application Testing Suite. While the vulnerability is in Oracle Application Testing Suite, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all Oracle Application Testing Suite accessible data as well as unauthorized update, insert or delete access to some of Oracle Application Testing Suite accessible data and unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Application Testing Suite. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:L/A:L).

### 85. CVE-2026-83108｜Oracle Corporation / Oracle Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:21.000)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:21.000 / 2026-09-15T23:19:05.053
- **官方描述（原文）**：Vulnerability in the Oracle Forms product of Oracle Fusion Middleware (component: Forms Services, C/S, Charmode). Supported versions that are affected are 12.2.1.19.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Forms. Successful attacks of this vulnerability can result in takeover of Oracle Forms. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 86. CVE-2026-83107｜Oracle Corporation / Oracle Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:20.893)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:20.893 / 2026-09-15T20:18:20.893
- **官方描述（原文）**：Vulnerability in the Oracle Forms product of Oracle Fusion Middleware (component: Forms Services, C/S, Charmode). Supported versions that are affected are 12.2.1.19.0 and 14.1.2.0.0. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle Forms. While the vulnerability is in Oracle Forms, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Forms. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 87. CVE-2026-83105｜Oracle Corporation / Oracle Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:20.667)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:20.667 / 2026-09-15T20:18:20.667
- **官方描述（原文）**：Vulnerability in the Oracle Forms product of Oracle Fusion Middleware (component: Forms Services, C/S, Charmode). Supported versions that are affected are 12.2.1.19.0 and 14.1.2.0.0. Difficult to exploit vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Forms. While the vulnerability is in Oracle Forms, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Forms. CVSS 3.1 Base Score 9.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 88. CVE-2026-83104｜Oracle Corporation / Oracle Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:20.553)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:20.553 / 2026-09-15T23:19:04.933
- **官方描述（原文）**：Vulnerability in the Oracle Forms product of Oracle Fusion Middleware (component: Forms Services, C/S, Charmode). Supported versions that are affected are 12.2.1.19.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via TCP to compromise Oracle Forms. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Forms accessible data as well as unauthorized access to critical data or complete access to all Oracle Forms accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 89. CVE-2026-83103｜Oracle Corporation / Oracle Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:20.440)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:20.440 / 2026-09-15T20:18:20.440
- **官方描述（原文）**：Vulnerability in the Oracle Forms product of Oracle Fusion Middleware (component: Forms Services, C/S, Charmode). Supported versions that are affected are 12.2.1.19.0 and 14.1.2.0.0. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle Forms. While the vulnerability is in Oracle Forms, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Forms. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 90. CVE-2026-83100｜Oracle Corporation / Oracle Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:20.113)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:20.113 / 2026-09-15T23:19:04.800
- **官方描述（原文）**：Vulnerability in the Oracle Forms product of Oracle Fusion Middleware (component: Forms Services, C/S, Charmode). Supported versions that are affected are 12.2.1.19.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Forms. Successful attacks of this vulnerability can result in takeover of Oracle Forms. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 91. CVE-2026-83099｜Oracle Corporation / Oracle Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:20.007)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:20.007 / 2026-09-15T23:19:04.673
- **官方描述（原文）**：Vulnerability in the Oracle Forms product of Oracle Fusion Middleware (component: Forms Services, C/S, Charmode). Supported versions that are affected are 12.2.1.19.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Forms. While the vulnerability is in Oracle Forms, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Forms. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 92. CVE-2026-83098｜Oracle Corporation / Oracle Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:19.877)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:19.877 / 2026-09-15T23:19:04.550
- **官方描述（原文）**：Vulnerability in the Oracle Forms product of Oracle Fusion Middleware (component: Forms Services, C/S, Charmode). Supported versions that are affected are 12.2.1.19.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Forms. Successful attacks of this vulnerability can result in takeover of Oracle Forms. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 93. CVE-2026-83095｜Oracle Corporation / Oracle Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:19.427)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:19.427 / 2026-09-15T23:19:04.430
- **官方描述（原文）**：Vulnerability in the Oracle Forms product of Oracle Fusion Middleware (component: Forms Services, C/S, Charmode). Supported versions that are affected are 12.2.1.19.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Forms. Successful attacks of this vulnerability can result in takeover of Oracle Forms. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 94. CVE-2026-83094｜Oracle Corporation / Oracle Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:19.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:19.313 / 2026-09-15T23:19:04.307
- **官方描述（原文）**：Vulnerability in the Oracle Forms product of Oracle Fusion Middleware (component: Forms Services, C/S, Charmode). Supported versions that are affected are 12.2.1.19.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Forms. Successful attacks of this vulnerability can result in takeover of Oracle Forms. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 95. CVE-2026-83066｜Oracle Corporation / Oracle Internet Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:15.443)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:15.443 / 2026-09-15T23:19:04.180
- **官方描述（原文）**：Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle Internet Directory. Successful attacks of this vulnerability can result in takeover of Oracle Internet Directory. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 96. CVE-2026-83064｜Oracle Corporation / Oracle WebCenter Portal
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:15.150)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:15.150 / 2026-09-15T20:18:15.150
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle WebCenter Portal. While the vulnerability is in Oracle WebCenter Portal, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Portal. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 97. CVE-2026-83062｜Oracle Corporation / Oracle Internet Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:14.907)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:14.907 / 2026-09-15T23:19:04.057
- **官方描述（原文）**：Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via LDAP to compromise Oracle Internet Directory. Successful attacks of this vulnerability can result in takeover of Oracle Internet Directory. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 98. CVE-2026-83061｜Oracle Corporation / Oracle Internet Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:14.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:14.790 / 2026-09-15T23:19:03.933
- **官方描述（原文）**：Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via LDAP to compromise Oracle Internet Directory. Successful attacks of this vulnerability can result in takeover of Oracle Internet Directory. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 99. CVE-2026-83060｜Oracle Corporation / Oracle Internet Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:14.680)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:14.680 / 2026-09-15T23:19:03.807
- **官方描述（原文）**：Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via LDAP to compromise Oracle Internet Directory. Successful attacks of this vulnerability can result in takeover of Oracle Internet Directory. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 100. CVE-2026-83059｜Oracle Corporation / Oracle Internet Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:14.563)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:14.563 / 2026-09-15T23:19:03.680
- **官方描述（原文）**：Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via LDAP to compromise Oracle Internet Directory. While the vulnerability is in Oracle Internet Directory, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Internet Directory. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 101. CVE-2026-83058｜Oracle Corporation / Oracle Internet Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:14.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:14.450 / 2026-09-15T20:18:14.450
- **官方描述（原文）**：Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via LDAP to compromise Oracle Internet Directory. While the vulnerability is in Oracle Internet Directory, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Internet Directory. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 102. CVE-2026-83057｜Oracle Corporation / Oracle Internet Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:14.340)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:14.340 / 2026-09-15T20:18:14.340
- **官方描述（原文）**：Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via LDAP to compromise Oracle Internet Directory. While the vulnerability is in Oracle Internet Directory, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Internet Directory. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 103. CVE-2026-83056｜Oracle Corporation / Oracle Internet Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:14.230)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:14.230 / 2026-09-15T20:18:14.230
- **官方描述（原文）**：Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via LDAP to compromise Oracle Internet Directory. While the vulnerability is in Oracle Internet Directory, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Internet Directory. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 104. CVE-2026-83055｜Oracle Corporation / Oracle Internet Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:14.113)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:14.113 / 2026-09-15T20:18:14.113
- **官方描述（原文）**：Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via LDAP to compromise Oracle Internet Directory. While the vulnerability is in Oracle Internet Directory, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Internet Directory. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 105. CVE-2026-83054｜Oracle Corporation / Oracle Internet Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:14.000)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:14.000 / 2026-09-15T23:19:03.550
- **官方描述（原文）**：Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via LDAP to compromise Oracle Internet Directory. Successful attacks of this vulnerability can result in takeover of Oracle Internet Directory. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 106. CVE-2026-83043｜Oracle Corporation / Oracle WebCenter Portal
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:12.743)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:12.743 / 2026-09-15T20:18:12.743
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Composer). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Portal. Successful attacks require human interaction from a person other than the attacker and while the vulnerability is in Oracle WebCenter Portal, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Portal. CVSS 3.1 Base Score 9.6 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H).

### 107. CVE-2026-83042｜Oracle Corporation / Oracle Identity Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:12.633)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:12.633 / 2026-09-15T23:19:03.427
- **官方描述（原文）**：Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: OIM Legacy UI). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Identity Manager. Successful attacks of this vulnerability can result in takeover of Oracle Identity Manager. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 108. CVE-2026-83040｜Oracle Corporation / Oracle WebCenter Portal
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:12.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:12.410 / 2026-09-15T20:18:12.410
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Portlet Services). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via SOAP to compromise Oracle WebCenter Portal. Successful attacks require human interaction from a person other than the attacker and while the vulnerability is in Oracle WebCenter Portal, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Portal. CVSS 3.1 Base Score 9.6 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H).

### 109. CVE-2026-83039｜Oracle Corporation / Oracle WebCenter Portal
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:12.297)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:12.297 / 2026-09-15T20:18:12.297
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Composer). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle WebCenter Portal. While the vulnerability is in Oracle WebCenter Portal, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Portal. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 110. CVE-2026-83038｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:12.187)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:12.187 / 2026-09-15T20:18:12.187
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: TopLink Integration). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle WebLogic Server. While the vulnerability is in Oracle WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 111. CVE-2026-83037｜Oracle Corporation / Oracle WebCenter Sites
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:12.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:12.077 / 2026-09-15T23:19:03.297
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Sites. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Sites. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 112. CVE-2026-83036｜Oracle Corporation / Oracle WebCenter Sites
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:11.970)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:11.970 / 2026-09-15T23:19:03.170
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Sites. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Sites. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 113. CVE-2026-83035｜Oracle Corporation / Oracle WebCenter Sites
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:11.853)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:11.853 / 2026-09-15T23:19:03.043
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Sites. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Sites. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 114. CVE-2026-83031｜Oracle Corporation / Oracle WebCenter Sites
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:11.370)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:11.370 / 2026-09-15T20:18:11.370
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle WebCenter Sites. While the vulnerability is in Oracle WebCenter Sites, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Sites. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 115. CVE-2026-83029｜Oracle Corporation / Oracle Managed File Transfer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:11.037)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:11.037 / 2026-09-15T20:18:11.037
- **官方描述（原文）**：Vulnerability in the Oracle Managed File Transfer product of Oracle Fusion Middleware (component: MFT Runtime Server). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Managed File Transfer. While the vulnerability is in Oracle Managed File Transfer, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Managed File Transfer accessible data as well as unauthorized access to critical data or complete access to all Oracle Managed File Transfer accessible data. CVSS 3.1 Base Score 9.6 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:N).

### 116. CVE-2026-83027｜Oracle Corporation / Oracle Identity Manager Connector
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:10.757)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:10.757 / 2026-09-15T20:18:10.757
- **官方描述（原文）**：Vulnerability in the Oracle Identity Manager Connector product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with access to the physical communication segment attached to the hardware where the Oracle Identity Manager Connector executes to compromise Oracle Identity Manager Connector. While the vulnerability is in Oracle Identity Manager Connector, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Identity Manager Connector accessible data as well as unauthorized access to critical data or complete access to all Oracle Identity Manager Connector accessible data. CVSS 3.1 Base Score 9.3 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N).

### 117. CVE-2026-83021｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:09.777)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:09.777 / 2026-09-15T23:19:02.920
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Web Container). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebLogic Server. While the vulnerability is in Oracle WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 118. CVE-2026-83020｜Oracle Corporation / Oracle Platform Security for Java
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:09.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:09.060 / 2026-09-15T23:19:02.787
- **官方描述（原文）**：Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Thirdparty Jars). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Platform Security for Java. While the vulnerability is in Oracle Platform Security for Java, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Platform Security for Java. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 119. CVE-2026-83006｜Oracle Corporation / Oracle WebCenter Enterprise Capture
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:07.223)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:07.223 / 2026-09-15T20:18:07.223
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle WebCenter Enterprise Capture. While the vulnerability is in Oracle WebCenter Enterprise Capture, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Enterprise Capture. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 120. CVE-2026-83001｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:06.680)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:06.680 / 2026-09-15T20:18:06.680
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Access Manager. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 121. CVE-2026-83000｜Oracle Corporation / Service Delivery Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:06.570)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:06.570 / 2026-09-15T23:19:02.667
- **官方描述（原文）**：Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Service Delivery Platform. Successful attacks of this vulnerability can result in takeover of Service Delivery Platform. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 122. CVE-2026-82999｜Oracle Corporation / Service Delivery Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:06.460)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:06.460 / 2026-09-15T20:18:06.460
- **官方描述（原文）**：Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Service Delivery Platform. While the vulnerability is in Service Delivery Platform, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Service Delivery Platform. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 123. CVE-2026-82998｜Oracle Corporation / Service Delivery Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:06.343)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:06.343 / 2026-09-15T20:18:06.343
- **官方描述（原文）**：Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Service Delivery Platform. While the vulnerability is in Service Delivery Platform, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Service Delivery Platform. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 124. CVE-2026-82997｜Oracle Corporation / Service Delivery Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:06.233)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:06.233 / 2026-09-15T20:18:06.233
- **官方描述（原文）**：Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Service Delivery Platform. While the vulnerability is in Service Delivery Platform, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Service Delivery Platform. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 125. CVE-2026-82995｜Oracle Corporation / Oracle Platform Security for Java
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:06.010)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:06.010 / 2026-09-15T23:19:02.537
- **官方描述（原文）**：Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Thirdparty Jars). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via SOAP to compromise Oracle Platform Security for Java. Successful attacks of this vulnerability can result in takeover of Oracle Platform Security for Java. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 126. CVE-2026-82994｜Oracle Corporation / Oracle Platform Security for Java
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:18:05.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:18:05.900 / 2026-09-15T23:19:02.410
- **官方描述（原文）**：Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Thirdparty Jars). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via LDAP to compromise Oracle Platform Security for Java. Successful attacks of this vulnerability can result in takeover of Oracle Platform Security for Java. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 127. CVE-2026-81855｜Wärtsilä / FOS-Onboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T22:17:03.197)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T22:17:03.197 / 2026-09-15T22:17:03.197
- **官方描述（原文）**：A hardcoded cryptographic client authentication key vulnerability exists in the robot testing framework component of Wärtsilä FOS-Onboard.

### 128. CVE-2026-78225｜Wärtsilä / FOS-Onboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T22:17:02.870)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T22:17:02.870 / 2026-09-15T22:17:02.870
- **官方描述（原文）**：A hardcoded cryptographic server key vulnerability exists in the deployer-ng Update Controller component of Wärtsilä FOS-Onboard.

### 129. CVE-2026-77972｜Slab / safeurl
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:24.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:24.290 / 2026-09-15T16:17:24.290
- **官方描述（原文）**：Time-of-check Time-of-use (TOCTOU) Race Condition in Slab safeurl allows an attacker who controls a hostname's DNS responses to reach internal network destinations that validation rejected. Validation returns a verdict and not the address it approved, so the HTTP clients the library ships receive the original hostname and resolve it a second time when the request is made. An attacker who controls the authoritative DNS for a name can answer the first lookup with a permitted address and the second with a blocked one, and the request then reaches a destination validation never approved. The same window opens without an attacker whenever a name legitimately resolves to different addresses across lookups, such as short record lifetimes or rotation between several addresses. This issue affects safeurl: from 0.1.0 onward.

### 130. CVE-2026-77866｜Slab / safeurl
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:24.117)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:24.117 / 2026-09-15T16:17:24.117
- **官方描述（原文）**：Server-Side Request Forgery (SSRF) vulnerability in Slab safeurl allows an attacker who controls a validated URL to reach internal network destinations the library is configured to block. Only IPv4 addresses are matched against the reserved ranges and the blocklist. Every other address is treated as matching nothing, so a destination that is rejected in its IPv4 form is accepted when written as an IPv6 address, IPv6 entries in the blocklist never match, and a host that resolves to no IPv4 address is accepted regardless of where it points. Deployments that rely on the allowlist instead are unaffected, because there an unmatched address is rejected. This issue affects safeurl: from 0.1.0 onward.

### 131. CVE-2026-77179｜Docker / Docker Sandboxes
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T14:17:11.273)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T14:17:11.273 / 2026-09-15T22:17:02.733
- **官方描述（原文）**：On macOS, the virtio-fs host server used by Docker Sandboxes improperly follows symlinks when reopening an unlinked file from a stored path. A malicious guest can replace a parent directory with a symlink, escape the shared workspace, and read or modify arbitrary host files as the VMM user, potentially achieving host code execution.

### 132. CVE-2026-76675｜Hewlett Packard Enterprise (HPE) / EdgeConnect SD-WAN Gateways
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:49.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:49.320 / 2026-09-15T20:17:49.320
- **官方描述（原文）**：A command injection vulnerability exists in the command line interface of EdgeConnect SD-WAN Gateways. Successful exploitation could allow an authenticated remote attacker with high privileges to execute arbitrary commands on the underlying operating system leading to complete system compromise.

### 133. CVE-2026-76674｜Hewlett Packard Enterprise (HPE) / EdgeConnect SD-WAN Gateways
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:49.207)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:49.207 / 2026-09-15T20:17:49.207
- **官方描述（原文）**：Buffer overflow vulnerabilities exist in the underlying operating system of HPE Networking EdgeConnect SD-WAN Gateways that could allow an unauthenticated remote attacker to execute arbitrary code. Successful exploitation could allow an attacker to execute arbitrary commands on the underlying operating system leading to complete system compromise.

### 134. CVE-2026-76673｜Hewlett Packard Enterprise (HPE) / EdgeConnect SD-WAN Gateways
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:49.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:49.090 / 2026-09-15T20:17:49.090
- **官方描述（原文）**：Vulnerabilities have been identified in the API of EdgeConnect SD-WAN Orchestrator that could potentially allow an unauthenticated remote actor to circumvent existing authentication controls. Successful exploitation could allow an attacker to gain administrative privileges leading to complete compromise of the EdgeConnect SD-WAN Orchestrator host.

### 135. CVE-2026-76672｜Hewlett Packard Enterprise (HPE) / EdgeConnect SD-WAN Gateways
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:48.977)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:48.977 / 2026-09-15T20:17:48.977
- **官方描述（原文）**：A vulnerability exists in the SD-WAN Orchestrator that may lead to the exposure of sensitive configuration information. An authenticated remote attacker with read-only privileges could exploit this vulnerability by sending a specially crafted request to the cache synchronization endpoint. Successful exploitation could result in the disclosure of sensitive third-party API tokens and credentials, potentially enabling lateral movement to external security platforms.

### 136. CVE-2026-76670｜Hewlett Packard Enterprise (HPE) / EdgeConnect SD-WAN Gateways
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:48.833)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:48.833 / 2026-09-15T20:17:48.833
- **官方描述（原文）**：Privilege escalation vulnerabilities exist in the API of HPE Networking EdgeConnect SD-WAN Orchestrator. Successful exploitation could allow a remote low-privileged authenticated user to escalate their privileges to those of an administrative user, leading to complete system compromise.

### 137. CVE-2026-76669｜Hewlett Packard Enterprise (HPE) / EdgeConnect SD-WAN Gateways
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:48.627)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:48.627 / 2026-09-15T20:17:48.627
- **官方描述（原文）**：Privilege escalation vulnerabilities exist in the API of HPE Networking EdgeConnect SD-WAN Orchestrator. Successful exploitation could allow a remote low-privileged authenticated user to escalate their privileges to those of an administrative user, leading to complete system compromise.

### 138. CVE-2026-73963｜Oracle Corporation / Oracle WebCenter Portal
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:47.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:47.550 / 2026-09-15T23:18:48.607
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Portlet Services). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Portal. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Portal. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 139. CVE-2026-73962｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:47.433)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:47.433 / 2026-09-15T20:17:47.433
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTPS to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Access Manager accessible data as well as unauthorized access to critical data or complete access to all Oracle Access Manager accessible data. CVSS 3.1 Base Score 9.6 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:N).

### 140. CVE-2026-73961｜Oracle Corporation / Oracle JDeveloper
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:47.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:47.320 / 2026-09-15T23:18:48.487
- **官方描述（原文）**：Vulnerability in the Oracle JDeveloper product of Oracle Fusion Middleware (component: ADF Faces). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle JDeveloper. Successful attacks of this vulnerability can result in takeover of Oracle JDeveloper. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 141. CVE-2026-73957｜Oracle Corporation / Oracle WebCenter Portal
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:46.887)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:46.887 / 2026-09-15T20:17:46.887
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Portlet Services). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Portal. Successful attacks require human interaction from a person other than the attacker and while the vulnerability is in Oracle WebCenter Portal, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle WebCenter Portal accessible data as well as unauthorized access to critical data or complete access to all Oracle WebCenter Portal accessible data. CVSS 3.1 Base Score 9.3 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N).

### 142. CVE-2026-73956｜Oracle Corporation / Oracle WebCenter Portal
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:46.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:46.780 / 2026-09-15T23:18:48.360
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Composer). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Portal. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Portal. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 143. CVE-2026-73953｜Oracle Corporation / Oracle WebCenter Portal
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:46.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:46.457 / 2026-09-15T23:18:48.233
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Portlet Services). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Portal. Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Portal. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 144. CVE-2026-73952｜Oracle Corporation / Oracle WebCenter Portal
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:46.347)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:46.347 / 2026-09-15T23:18:48.077
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Portlet Services). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebCenter Portal. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle WebCenter Portal accessible data as well as unauthorized access to critical data or complete access to all Oracle WebCenter Portal accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 145. CVE-2026-73950｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:46.133)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:46.133 / 2026-09-15T23:18:47.843
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. Successful attacks of this vulnerability can result in takeover of Oracle Access Manager. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 146. CVE-2026-73948｜Oracle Corporation / Oracle WebCenter Portal
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:45.913)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:45.913 / 2026-09-15T20:17:45.913
- **官方描述（原文）**：Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Composer). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle WebCenter Portal. While the vulnerability is in Oracle WebCenter Portal, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebCenter Portal. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 147. CVE-2026-73947｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:45.803)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:45.803 / 2026-09-15T23:18:47.693
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. Successful attacks of this vulnerability can result in takeover of Oracle Access Manager. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 148. CVE-2026-73946｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:45.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:45.670 / 2026-09-15T20:17:45.670
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Access Manager. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

### 149. CVE-2026-73945｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:45.563)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:45.563 / 2026-09-15T20:17:45.563
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Access Manager. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 150. CVE-2026-73944｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:45.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:45.457 / 2026-09-15T23:18:47.567
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Access Manager accessible data as well as unauthorized access to critical data or complete access to all Oracle Access Manager accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 151. CVE-2026-73940｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:44.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:44.943 / 2026-09-15T23:18:46.880
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle Access Manager. Successful attacks of this vulnerability can result in takeover of Oracle Access Manager. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 152. CVE-2026-73807｜mySCADA Technologies / mySCADA myPRO
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T22:16:58.683)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T22:16:58.683 / 2026-09-15T22:16:58.683
- **官方描述（原文）**：The mySCADA myPRO Manager command API does not properly enforce authentication for privileged functions. An unauthenticated attacker with network access to the affected API could exploit this vulnerability to access privileged management functions.

### 153. CVE-2026-73458｜Arista Networks / EOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:43.160)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:43.160 / 2026-09-15T20:17:43.160
- **官方描述（原文）**：On affected platforms running Arista EOS with authenticated Bidirectional Forwarding Detection (BFD) sessions configured, a specially crafted packet can cause the BFD session(s) to go down. This may result in undesirable network changes because various routing protocols monitor status on BFD session(s).

### 154. CVE-2026-71163｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:42.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:42.490 / 2026-09-15T20:17:42.490
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Access Manager accessible data as well as unauthorized access to critical data or complete access to all Oracle Access Manager accessible data and unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Access Manager. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:L).

### 155. CVE-2026-71133｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:42.343)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:42.343 / 2026-09-15T23:18:17.843
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Access Manager. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 156. CVE-2026-70913｜Oracle Corporation / Oracle Identity Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:41.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:41.980 / 2026-09-15T23:18:16.820
- **官方描述（原文）**：Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Identity Manager. Successful attacks of this vulnerability can result in takeover of Oracle Identity Manager. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 157. CVE-2026-70757｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:41.863)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:41.863 / 2026-09-15T23:18:15.880
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server. Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 158. CVE-2026-70756｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:41.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:41.740 / 2026-09-15T23:18:15.380
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server. Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 159. CVE-2026-70748｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T20:17:41.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T20:17:41.470 / 2026-09-15T23:18:14.853
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server. Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 160. CVE-2026-69204｜http4s / http4s
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T19:17:37.580)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T19:17:37.580 / 2026-09-15T19:17:37.580
- **官方描述（原文）**：Http4s is a Scala interface for HTTP services. Prior to 0.23.35 and 1.0.0-M47, Ember HTTP/1.1 does not reject messages containing both Transfer-Encoding and Content-Length, so an intermediary and Ember can select different body framing rules. When ember-server is behind a keep-alive intermediary that forwards both headers and frames by Content-Length, an unauthenticated attacker can smuggle a second request, bypass intermediary access controls, poison caches, or cause a victim request to be joined to an attacker-controlled prefix. The shared response parser can also desynchronize an ember-client connection when a malicious or compromised upstream sends both headers. This issue is fixed in versions 0.23.35 and 1.0.0-M47.

### 161. CVE-2026-68491｜Webpros / SolusVM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T21:16:42.423)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T21:16:42.423 / 2026-09-15T21:16:42.423
- **官方描述（原文）**：An insufficient check allowed for the overwrite of arbitrary files via a symlink.

### 162. CVE-2026-66890｜Digital Watchdog / VMAX A1 G4 DVR
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T21:16:42.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T21:16:42.090 / 2026-09-15T21:16:42.090
- **官方描述（原文）**：The affected products use hard-coded credentials, which could allow remote access to files with root privileges where FTP is reachable.

### 163. CVE-2026-66887｜Digital Watchdog / VMAX A1 G4 DVR
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T21:16:41.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T21:16:41.930 / 2026-09-15T21:16:41.930
- **官方描述（原文）**：The affected products are missing authorization on state-changing CGIs and session checks are not performed.

### 164. CVE-2026-63696｜Dell / SmartFabric OS10 Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T15:17:20.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T15:17:20.527 / 2026-09-16T04:18:38.170
- **官方描述（原文）**：Dell SmartFabric OS10 Software, versions prior to 10.6.1.3, contains a Download of Code Without Integrity Check vulnerability. A high privileged attacker with remote access could potentially exploit this vulnerability, leading to Code execution.

### 165. CVE-2026-63695｜Dell / SmartFabric OS10 Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T15:17:20.390)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T15:17:20.390 / 2026-09-16T04:18:37.990
- **官方描述（原文）**：Dell SmartFabric OS10 Software, versions prior to 10.6.1.3, contains a Session Fixation vulnerability. An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to Session theft.

### 166. CVE-2026-62379｜OpenIdentityPlatform / OpenAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T10:17:06.107)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01089 / percentile=0.63528
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T10:17:06.107 / 2026-09-15T15:17:20.270
- **官方描述（原文）**：Open Access Management (OpenAM) is an access management solution. Prior to 16.1.2, the pre-authentication /authservice PLL endpoint accepts a CustomCallback XML element whose className value selects an arbitrary Java class for AuthXMLUtils to load and instantiate without verifying that it implements DSAMECallbackInterface. Default configurations expose the endpoint without authentication, allowing attacker-controlled class initialization and unsafe deserialization of a serialized Subject value to execute code in the server process. Enabling sunRemoteAuthSecurityEnabled does not prevent the vulnerable parsing and instantiation because its check occurs later. This issue is fixed in version 16.1.2.

### 167. CVE-2026-62263｜OpenIdentityPlatform / OpenAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T10:17:05.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00891 / percentile=0.57492
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T10:17:05.810 / 2026-09-15T14:17:03.660
- **官方描述（原文）**：Open Access Management (OpenAM) is an access management solution. Prior to 16.1.2, WebAuthnAuthentication.deserialize applies an ObjectInputFilter that allows every serialized object at depth greater than 1 and therefore constrains only an AuthenticatorImpl root object. A pre-authentication attacker can supply a userHandle whose serialized graph has a valid AuthenticatorImpl root and a nested gadget class, causing readObject or readResolve execution before the cast and assertion verification when a usable gadget is on the classpath. This bypasses the incomplete remediation for the earlier WebAuthn deserialization vulnerability. This issue is fixed in version 16.1.2.

### 168. CVE-2026-61667｜DIRACGrid / DIRAC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T18:17:27.050)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T18:17:27.050 / 2026-09-15T19:17:34.233
- **官方描述（原文）**：DIRAC is an interware, meaning a software framework for distributed computing. Prior to versions 8.0.79, 9.0.22, and 9.1.10, DataManagementSystem/Service/FileCatalogHandler.py checkDataset forwards an authenticated caller-controlled datasets value to DatasetManager.py __checkDataset, where datasetName is interpolated into an FC_MetaDatasets SQL query without parameterization. The injected query can control the returned MetaQuery value, which is passed to Python eval and permits command execution as the account running the DIRAC services. Successful exploitation can expose dirac.cfg, database passwords, stored proxies, and tokens, fully compromise the DIRAC system, and allow alteration of local log evidence. This issue is fixed in versions 8.0.79, 9.0.22, and 9.1.10.

### 169. CVE-2026-61568｜zereight / gitlab-mcp
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T21:16:41.570)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T21:16:41.570 / 2026-09-15T21:16:41.570
- **官方描述（原文）**：`@zereight/mcp-gitlab` is a Model Context Protocol server for GitLab. Versions prior to 2.1.30 expose the Streamable HTTP MCP endpoint without an effective Host or Origin allowlist. A malicious web page can use DNS rebinding to route browser requests to a victim's local MCP listener while preserving an attacker-controlled `Host` and `Origin`. The server accepts those headers and reaches the MCP initialization path instead of rejecting the request at the HTTP boundary. Version 2.1.30 contains a patch.

### 170. CVE-2026-61560｜zereight / gitlab-mcp
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T22:16:58.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T22:16:58.040 / 2026-09-15T22:16:58.040
- **官方描述（原文）**：`@zereight/mcp-gitlab` is a Model Context Protocol server for GitLab. Prior to version 2.1.27, the SSE transport mode (`SSE=true`) exposes all MCP tools without any authentication. The `upload_markdown` tool reads arbitrary files from the server's local filesystem via an unsanitized `file_path` parameter and uploads them to a GitLab project. Combined, any unauthenticated network-reachable attacker can read `/proc/self/environ` to steal the server's `GITLAB_PERSONAL_ACCESS_TOKEN` and achieve full GitLab account takeover. This is the default configuration for Docker deployments. Version 2.1.27 contains a patch.

### 171. CVE-2026-61559｜zereight / gitlab-mcp
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T21:16:41.390)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T21:16:41.390 / 2026-09-15T21:16:41.390
- **官方描述（原文）**：`@zereight/mcp-gitlab` is a Model Context Protocol server for GitLab. Starting in version 0.0.1 and prior to version 2.1.27, when the environment variable `ENABLE_DYNAMIC_API_URL=true` is set, the server reads the `X-GitLab-API-URL` HTTP request header and uses it as the base URL for all outbound GitLab API calls made within that request. The server validates that the value is a well-formed URL (`new URL(dynamicApiUrl)`) but applies no allowlist or hostname restriction. The server then attaches the victim's `Private-Token` to every outbound fetch that uses the redirected URL. Any caller who can reach the HTTP transport can set `X-GitLab-API-URL` to an attacker-controlled host. The next GitLab API call the server makes delivers the victim's token to that host. Version 2.1.27 contains a patch.

### 172. CVE-2026-61549｜woodpecker-ci / woodpecker
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T15:17:20.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T15:17:20.110 / 2026-09-16T04:18:37.707
- **官方描述（原文）**：Woodpecker is a CI/CD engine. From 1.0.0 until 3.16.0, pipeline/backend/kubernetes/backend_options.go defines backend_options.kubernetes.serviceAccountName, and the Kubernetes backend in pipeline/backend/kubernetes/pod.go copies that pipeline-step value directly into the pod specification without administrator authorization. Any user with Push permission on a connected repository can therefore run pipeline pods under an arbitrary ServiceAccount in the pipeline namespace and inherit that account's RBAC permissions. When a privileged ServiceAccount is reachable, the attacker can exfiltrate secrets such as database credentials, API keys, and TLS certificates and may take over the cluster. This issue is fixed in version 3.16.0.

### 173. CVE-2026-59971｜designcomputer / mysql_mcp_server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T15:17:19.947)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T15:17:19.947 / 2026-09-15T16:17:17.263
- **官方描述（原文）**：MySQL MCP Server is a Model Context Protocol server that enables secure interaction with MySQL databases. Prior to 0.4.2, setting MCP_TRANSPORT=sse causes src/mysql_mcp_server/server.py to construct SseServerTransport without security_settings or enable_dns_rebinding_protection, while the Starlette routes /, /sse, and /messages/ have no authentication and the service binds to 0.0.0.0 by default. A network attacker can directly reach execute_sql, or can use DNS rebinding to make a victim's browser relay same-origin requests to a locally bound service, and supply a query that reaches cursor.execute(query). This allows unauthenticated disclosure and modification of the configured database; when the MySQL account has FILE privileges, the same access can read or write server files and may enable code execution. The default stdio transport is not affected. This issue is fixed in 0.4.2.

### 174. CVE-2026-57148｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:11.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00528 / percentile=0.43216
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:11.910 / 2026-09-15T14:45:28.563
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to 0.1.6, praisonai_platform/services/auth_service.py falls back to the public dev-secret-change-me HS256 signing key when PLATFORM_JWT_SECRET is unset, while the startup and token-issuance guards are disabled because PLATFORM_ENV also defaults to dev. An unauthenticated attacker can sign a JWT containing an attacker-chosen sub value, and AuthService._verify_token() accepts it as an authenticated identity, enabling user or workspace-owner impersonation when a target identifier is known. This vulnerability is fixed in praisonai-platform 0.1.6.

### 175. CVE-2026-57147｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:11.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00512 / percentile=0.42169
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:11.760 / 2026-09-15T14:45:28.563
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to 0.1.6, praisonai_platform/services/auth_service.py assigns the public dev-secret-change-me value to JWT_SECRET when PLATFORM_JWT_SECRET is unset, and its production guard does not run when PLATFORM_ENV is also unset because that setting defaults to dev. A remote unauthenticated attacker can mint an HS256 token with an arbitrary sub and email, and the platform's AuthService._verify_token() and get_current_user dependency accept the forged identity for protected API routes. This vulnerability is fixed in praisonai-platform 0.1.6.

### 176. CVE-2026-57141｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:11.617)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.0077 / percentile=0.53702
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:11.617 / 2026-09-15T14:45:28.563
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to 1.7.2, the codeMode tool in src/praisonai-ts/src/tools/builtins/code-mode.ts executes model-generated JavaScript with new Function() and with(sandbox), while a regular-expression blocklist can be bypassed with Function('return this')() to recover the global object and by constructing the child_process module name dynamically. An attacker who can influence the code argument can access host process capabilities, read or write files, obtain environment credentials, and execute operating-system commands with the PraisonAI process privileges. This issue is fixed in version 1.7.2.

### 177. CVE-2026-57140｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:11.473)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00564 / percentile=0.45213
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:11.473 / 2026-09-15T14:45:28.563
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. From 1.6.0 until 1.7.2, AgentOS in src/praisonai-ts/src/os/agentos.ts uses the 0.0.0.0 default from src/praisonai-ts/src/os/config.ts and registers GET /api/agents and POST /api/chat without authentication middleware. A remote caller who can reach the service can obtain agent names, roles, and instruction prefixes and can invoke a selected agent, potentially reaching its tools, memory, external APIs, credentials, and workflow state. An initial remediation was released in version 1.7.2.

### 178. CVE-2026-57139｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:11.327)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00642 / percentile=0.4892
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:11.327 / 2026-09-15T14:45:28.563
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. From 1.5.0 until 1.7.2, MCPServer.startHttp() in src/praisonai-ts/src/mcp/server.ts binds without a host restriction and forwards every HTTP POST request to handleRequest() without authentication or authorization. Any network client that can reach the port can call tools/list, tools/call, resources/read, or prompts/get, causing registered handlers to run with server-side credentials and process privileges or disclose registered data. An initial remediation was released in version 1.7.2.

### 179. CVE-2026-57138｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:11.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00654 / percentile=0.49454
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:11.180 / 2026-09-15T14:45:28.563
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. From 1.4.0 until 1.7.2, codeMode in src/praisonai-ts/src/tools/builtins/code-mode.ts executes untrusted JavaScript with new Function() inside with(sandbox) and relies on a small source-code blocklist plus shadowed process and require properties. Code can use ({}).constructor.constructor to recover the real Function constructor, obtain process and process.mainModule.require, and reach host filesystem and subprocess APIs despite the advertised sandbox. Attackers who control codeMode input can read secrets, modify files, execute commands, or exhaust the host process. This issue is fixed in version 1.7.2.

### 180. CVE-2026-55211｜equinor / surfio
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T16:17:14.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T16:17:14.560 / 2026-09-15T16:17:14.560
- **官方描述（原文）**：Surfio is a library for reading and writing surface files. Prior to 0.0.19, surfio does not correctly validate size fields in IRAP files, leading to a buffer overflow when untrusted files are parsed. The severity assumes surfio is used to parse untrusted files in a networking context such as a web service. This issue is fixed in version 0.0.19.

### 181. CVE-2026-55158｜wktk / conflibot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T15:17:18.593)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T15:17:18.593 / 2026-09-15T15:17:18.593
- **官方描述（原文）**：Conflibot warns in advance when merging a pull request will cause conflicts in other open pull requests. Prior to 1.2.1, src/index.ts builds git checkout, git merge, and git format-patch commands by interpolating the attacker-controlled pull request head.ref value into strings passed to exec. In the documented pull_request_target configuration, an attacker can open a pull request, including from a fork, whose branch name contains shell metacharacters, and the workflow automatically interprets those characters as commands without maintainer interaction. The commands execute on a runner with base-repository secrets and a write-scoped GITHUB_TOKEN, allowing arbitrary command execution, secret or token exfiltration, unauthorized pushes, and other token abuse. The fixed implementations in src/index.ts and src/conflibot.ts use execFile or spawn argument arrays, and the v2 line also uses numeric pull-request refs rather than branch names. This issue is fixed in versions 1.2.1 and 2.0.0.

### 182. CVE-2026-54337｜ShaneIsrael / fireshare
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T21:16:36.920)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T21:16:36.920 / 2026-09-15T21:16:36.920
- **官方描述（原文）**：Fireshare facilitates self-hosted media and link sharing. Prior to version 1.6.14, an argument Injection in the video upload function allows unauthenticated attacker to write/overwrite system files. Version 1.6.14 fixes the issue.

### 183. CVE-2026-53710｜IBM / mcp-context-forge
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T17:17:19.117)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T17:17:19.117 / 2026-09-15T20:17:17.743
- **官方描述（原文）**：MCP Context Forge is an AI gateway, registry, and proxy for MCP, A2A, REST, and gRPC APIs. Prior to 1.0.2, the python_sandbox_server in mcp-servers/python/python_sandbox_server/src/python_sandbox_server/server_fastmcp.py exposes raw getattr through safe_builtins, omits a required _getattr_ guard, and relies on validate_code checks for literal dangerous dunder strings. An attacker can construct dunder names at runtime, traverse the Python class hierarchy, reach subprocess.Popen, and execute OS commands with the server process privileges through the execute_code MCP tool. The HTTP/SSE transport can expose this tool without authentication, while stdio-only deployments have reduced network reachability. The issue affects the python_sandbox_server subproject and does not directly affect the core Context Forge gateway or proxy components. This issue is fixed in version 1.0.2.

### 184. CVE-2026-53459｜maziggy / bambuddy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T18:17:22.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T18:17:22.120 / 2026-09-15T18:17:22.120
- **官方描述（原文）**：Bambuddy is a self-hosted print archive and management system for Bambu Lab 3D printers. Starting in version 0.1.6 and prior to version 0.2.4.4, a fail-open in the authentication code allows any attacker to bypass authentication by flooding a public endpoint to exhaust resources causing database access to fail, granting unauthenticated access to all protected endpoints. Version 0.2.4.4 patches the issue.

### 185. CVE-2026-52824｜kimai / kimai
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T11:17:09.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00379 / percentile=0.31444
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T11:17:09.543 / 2026-09-15T11:17:09.543
- **官方描述（原文）**：Kimai is an open-source time tracking application. Prior to 2.58.0, the official Docker image sets APP_SECRET to the public value change_this_to_something_unique in Dockerfile, and .docker/entrypoint.sh neither replaces nor rejects that value before Symfony uses it as kernel.secret. An unauthenticated attacker who reaches a deployment that did not override APP_SECRET, knows a username, correctly guesses the account ID associated with that username, and targets an account without active two-factor authentication can forge HMAC-protected authentication artifacts, including KIMAI_REMEMBER cookies and login links, to access the account without its password. The updated entrypoint generates and persists a random secret when no safe operator-provided value exists. This issue is fixed in version 2.58.0.

### 186. CVE-2026-48717｜OpenIdentityPlatform / OpenAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T10:17:05.377)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00529 / percentile=0.43255
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T10:17:05.377 / 2026-09-15T14:16:55.147
- **官方描述（原文）**：Open Access Management (OpenAM) is an access management solution. Prior to 16.1.1, AuthorizationCodeGrantTypeHandler requires a code_verifier only when the realm-wide codeVerifierEnforced setting is enabled, even when an authorization code stores a code_challenge. Because that setting is disabled by default, an attacker who intercepts a PKCE-protected authorization code can omit code_verifier and redeem the code, while an explicitly incorrect verifier is rejected. Public clients are directly affected, and confidential-client exploitation additionally requires client authentication material or another redemption context. This issue is fixed in version 16.1.1.

### 187. CVE-2026-46619｜OpenIdentityPlatform / OpenAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T10:17:04.770)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00992 / percentile=0.6068
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T10:17:04.770 / 2026-09-15T15:17:15.700
- **官方描述（原文）**：Open Access Management (OpenAM) is an access management solution. Prior to 16.1.1, MSISDNValidation in the MSISDN authentication module concatenates the request-supplied MSISDN value into an LDAP search filter without escaping, while the default empty trusted-gateway list allows all traffic. In a realm where an MSISDN module is enabled in a reachable authentication chain, an unauthenticated remote attacker can inject LDAP filter metacharacters, select an arbitrary matching user, and obtain a normal authenticated OpenAM session without a password. This issue is fixed in version 16.1.1.

### 188. CVE-2026-46495｜OpenIdentityPlatform / OpenDJ
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T15:17:15.493)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T15:17:15.493 / 2026-09-15T15:17:15.493
- **官方描述（原文）**：OpenDJ is an LDAPv3 compliant directory service. Prior to 5.1.1, the JMX RMI connector in opendj-server-legacy/src/main/java/org/opends/server/protocols/jmx/RmiConnector.java processes attacker-controlled credential objects before authentication without a restrictive jmx.remote.rmi.server.credentials.filter.pattern, and RmiAuthenticator.authenticate in opendj-server-legacy/src/main/java/org/opends/server/protocols/jmx/RmiAuthenticator.java accepts an unconstrained Object array rather than a two-element String[]. When the JMX Connection Handler is enabled and its TCP listener is reachable, an unauthenticated remote attacker can submit a crafted serialized Java object and achieve code execution in the OpenDJ server process. The handler is disabled by default, and successful exploitation depends on the runtime classpath and Java version; remote code execution was demonstrated against OpenDJ 4.4.15 on JDK 11 with Jackson 2.12.6.1. This issue is fixed in 5.1.1.

### 189. CVE-2026-46488｜motioneye-project / motioneye
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T17:17:15.200)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T17:17:15.200 / 2026-09-15T17:17:15.200
- **官方描述（原文）**：motionEye (mEye) is an online interface for a piece of software called "motion," which is a video surveillance program with motion detection. Prior to 0.44.0, motionEye accepts the client-controlled meye_username and meye_password_hash cookies as authentication material without server-side session validation. An unauthenticated attacker who knows a target username and corresponding hash can set the cookies manually or cause them to be loaded by submitting blank credentials through the switch-user authentication flow, after which the server authenticates the attacker as that user. The administrator username and password-hash value are stored in /etc/motioneye/motion.conf, which is globally readable by default, allowing a local shell user to obtain reusable administrator credential material. Successful impersonation can enable account lockout, password changes and persistence, data enumeration, data destruction, and data exfiltration. This issue is fixed in version 0.44.0.

### 190. CVE-2026-45579｜DIRACGrid / DIRAC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T18:17:21.427)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T18:17:21.427 / 2026-09-15T19:17:19.743
- **官方描述（原文）**：DIRAC is an interware, meaning a software framework for distributed computing. Prior to versions 8.0.79, 9.0.22, and 9.1.10, the RequestManagementSystem/Service/ReqManagerHandler.py export_getRequestCountersWeb function passes an authenticated caller-controlled groupingAttribute to RequestManagementSystem/DB/RequestDB.py getRequestCountersWeb. An unrecognized value is resolved against the Request object and evaluated as Python code, allowing a crafted dunder attribute expression to reach operating-system functions and execute commands as the account running the DIRAC services. Successful exploitation can expose dirac.cfg, database passwords, stored proxies, and tokens, fully compromise the DIRAC system, and allow alteration of local log evidence. This issue is fixed in versions 8.0.79, 9.0.22, and 9.1.10.

### 191. CVE-2026-45052｜OpenIdentityPlatform / OpenAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T10:17:04.307)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00554 / percentile=0.44665
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T10:17:04.307 / 2026-09-15T10:17:04.307
- **官方描述（原文）**：Open Access Management (OpenAM) is an access management solution. Prior to 16.1.1, the Liberty Web Services SOAP receiver permits unauthenticated remote requests to write persistent entries through SOAPReceiver and DiscoveryService into a user's Liberty Discovery store and the shared root-realm Discovery branch. The server-side handlers bypass requester LDAP and identity ACLs, and the global path uses an internal administrative token. Deployments that consume Liberty discovery data can subsequently use manipulated service-routing or security-mechanism records. This issue is fixed in version 16.1.1.

### 192. CVE-2026-45051｜OpenIdentityPlatform / OpenAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T10:17:04.153)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00688 / percentile=0.50848
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T10:17:04.153 / 2026-09-15T14:16:54.240
- **官方描述（原文）**：Open Access Management (OpenAM) is an access management solution. Prior to 16.1.1, WebAuthnAuthentication loads a serialized AuthenticatorImpl object graph from the configured userAttribute through loadAuthenticators without an ObjectInputFilter. Exploitation requires the WebAuthn flow to be reachable and an attacker to have previously written controlled data to that attribute through delegated administration, provisioning, directory access, legacy REST self-registration, or unsafe configuration. When those non-default conditions hold, the data is deserialized before assertion verification and can execute a classpath gadget in the application server process. This issue is fixed in version 16.1.1.

### 193. CVE-2026-39919｜Artifex Software / Ghostscript
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T15:17:14.723)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T15:17:14.723 / 2026-09-15T15:17:14.723
- **官方描述（原文）**：Ghostscript before 10.08.0 contains a heap-based buffer overflow vulnerability in the JPEG 2000 output adapter (base/sjpx_openjpeg.c) that allows attackers to cause memory corruption by supplying a crafted PDF containing a JPEG 2000 image with mismatched component subsampling factors. When image components declare different subsampling values, the non-samescale sub-byte-depth output path allocates a row buffer sized for packed output but writes a full byte per output column regardless of bit depth, overflowing the allocation and corrupting internal chunk-allocator metadata to achieve code execution.

### 194. CVE-2026-19773｜libwebsockets / libwebsockets
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T19:17:17.747)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T19:17:17.747 / 2026-09-16T04:18:01.260
- **官方描述（原文）**：libwebsockets HTTP/2 HPACK Path Header Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of libwebsockets. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of HTTP/2 HPACK path header. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process. Was ZDI-CAN-31036.

### 195. CVE-2026-15640｜Delinea / Secret Server (On-Prem)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T00:17:03.577)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T00:17:03.577 / 2026-09-16T00:17:03.577
- **官方描述（原文）**：Under certain conditions a valid SAML IdP response may be used to impersonate another Secret Server user.

### 196. CVE-2026-15639｜Delinea / Secret Server (On-Prem)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T00:17:03.453)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T00:17:03.453 / 2026-09-16T00:17:03.453
- **官方描述（原文）**：An attacker can craft a malicious link that, if used by a legitimate user, may cause the user's browser to run JavaScript supplied by the attacker.

### 197. CVE-2026-15638｜Delinea / Secret Server (On-Prem)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T00:17:02.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T00:17:02.600 / 2026-09-16T00:17:02.600
- **官方描述（原文）**：An unauthenticated user with access to Secret Server could leverage a padding oracle to decrypt or encrypt data using one of the server's cryptographic keys. The key itself is not exposed.

### 198. CVE-2026-14349｜themetechmount / TrueBooker – Appointment Booking and Scheduler System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T04:17:58.777)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T04:17:58.777 / 2026-09-16T04:17:58.777
- **官方描述（原文）**：The TrueBooker – Appointment Booking and Scheduler System plugin for WordPress is vulnerable to authorization bypass in all versions up to, and including, 1.2.3. This is due to the plugin not properly verifying that a user is authorized to perform an action. This makes it possible for unauthenticated attackers to modify the email address of arbitrary user accounts, including administrators, which can be leveraged to reset the account's password and gain access to it.

### 199. CVE-2026-12793｜jetmonsters / JetFormBuilder — Dynamic Blocks Form Builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-16T04:17:56.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-16T04:17:56.110 / 2026-09-16T04:17:56.110
- **官方描述（原文）**：The JetFormBuilder — Dynamic Blocks Form Builder plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 3.6.2. This is due to the plugin not validating that a submitted form ID belongs to a JetFormBuilder form before parsing the referenced post's content as form schema and executing an Advanced Validation server-side callback. This makes it possible for unauthenticated attackers to create a new administrator-level user account.

### 200. CVE-2026-12351｜IBM / MQ
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-15T18:17:13.727)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-15T18:17:13.727 / 2026-09-16T04:17:53.937
- **官方描述（原文）**：IBM MQ 9.3.0.0 through 9.3.0.41 LTS, 9.3.0.0 through 9.3.5.1 CD, 9.4.0.0 through 9.4.0.25 LTS, 9.4.0.0 through 9.4.5.1 LTS, and 10.0.0.0 could allow a remote attacker to execute arbitrary code due to unsafe JNDI lookup processing when the IVT application is deployed.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-91932 | P3 / 38 | FlowiseAI / Flowise | v4.0 9.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2024-14029 | P3 / 38 | tornadoweb / tornado | v4.0 9.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2023-54398 | P3 / 38 | Yonyou / U8 Cloud | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-91994 | WATCH / 30 | semaphoreui / semaphore | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91990 | WATCH / 30 | tornadoweb / tornado | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91985 | WATCH / 30 | go-vikunja / vikunja | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91973 | WATCH / 30 | go-vikunja / vikunja | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91970 | WATCH / 30 | go-vikunja / vikunja | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91968 | WATCH / 30 | go-vikunja / vikunja | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91965 | WATCH / 30 | WWBN / AVideo | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91963 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91960 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91955 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91953 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91950 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91945 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91943 | WATCH / 30 | unclecode / crawl4ai | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91940 | WATCH / 30 | unclecode / crawl4ai | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91925 | WATCH / 30 | polyaxon / polyaxon | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91003 | WATCH / 30 | D-Link / DI-8300 | v4.0 8.5 (HIGH) | 0.00512 / percentile=0.42167 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91001 | WATCH / 30 | D-Link / DI-8400 | v4.0 8.6 (HIGH) | 0.00484 / percentile=0.40372 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88616 | WATCH / 30 | 未確認 / 未確認 | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-85013 | WATCH / 30 | Red Hat / Red Hat Enterprise Linux 10 | v3.1 7.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79425 | WATCH / 30 | 未確認 / 未確認 | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79410 | WATCH / 30 | 未確認 / 未確認 | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-59160 | WATCH / 30 | DerYeger / yeger | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-58485 | WATCH / 30 | ihor-sokoliuk / mcp-searxng | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-58483 | WATCH / 30 | ihor-sokoliuk / mcp-searxng | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57137 | WATCH / 30 | MervinPraison / PraisonAI | v3.1 8.8 (HIGH) | 0.00442 / percentile=0.37448 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57136 | WATCH / 30 | MervinPraison / PraisonAI | v3.1 8.8 (HIGH) | 0.00764 / percentile=0.53496 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：3；缺少 Product：3；缺少 Title：30。
- EPSS 未確認：26；Exploitation status 未確認：0。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-16T05:30:26.871699+00:00`；Delta generated at：`2026-09-16T05:30:26.871699+00:00`。

---

## 可驗證資料來源

- **CVE-2026-91932** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91932)
- **CVE-2024-14029** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-14029)
- **CVE-2023-54398** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-54398)
- **CVE-2026-91994** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91994)
- **CVE-2026-91990** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91990)
- **CVE-2026-91985** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91985)
- **CVE-2026-91973** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91973)
- **CVE-2026-91970** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91970)
- **CVE-2026-91968** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91968)
- **CVE-2026-91965** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91965)
- **CVE-2026-91963** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91963)
- **CVE-2026-91960** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91960)
- **CVE-2026-91955** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91955)
- **CVE-2026-91953** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91953)
- **CVE-2026-91950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91950)
- **CVE-2026-91945** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91945)
- **CVE-2026-91943** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91943)
- **CVE-2026-91940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91940)
- **CVE-2026-91925** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91925)
- **CVE-2026-91003** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91003) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91003)
- **CVE-2026-91001** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91001) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91001)
- **CVE-2026-88616** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88616)
- **CVE-2026-85013** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85013)
- **CVE-2026-79425** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79425)
- **CVE-2026-79410** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79410)
- **CVE-2026-59160** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59160)
- **CVE-2026-58485** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58485)
- **CVE-2026-58483** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58483)
- **CVE-2026-57137** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57137) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-57137)
- **CVE-2026-57136** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57136) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-57136)
- **CVE-2026-57135** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57135) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-57135)
- **CVE-2026-57134** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57134) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-57134)
- **CVE-2026-56829** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56829)
- **CVE-2026-56827** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56827)
- **CVE-2026-55692** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55692)
- **CVE-2026-52484** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-52484)
- **CVE-2026-91998** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91998)
- **CVE-2026-91995** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91995)
- **CVE-2026-91988** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91988)
- **CVE-2026-91949** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91949)
- **CVE-2026-91939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91939)
- **CVE-2026-91931** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91931)
- **CVE-2026-91749** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91749)
- **CVE-2026-91728** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91728)
- **CVE-2026-90711** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90711) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90711)
- **CVE-2026-89308** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89308)
- **CVE-2026-89040** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89040)
- **CVE-2026-89026** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89026)
- **CVE-2026-89022** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89022)
- **CVE-2026-87230** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87230)
- **CVE-2026-87223** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87223)
- **CVE-2026-87217** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87217)
- **CVE-2026-87214** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87214)
- **CVE-2026-87189** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87189)
- **CVE-2026-87188** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87188)
- **CVE-2026-87186** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87186)
- **CVE-2026-87184** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87184)
- **CVE-2026-87176** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87176)
- **CVE-2026-87175** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87175)
- **CVE-2026-87173** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87173)
- **CVE-2026-87172** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87172)
- **CVE-2026-87170** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87170)
- **CVE-2026-87129** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87129)
- **CVE-2026-87128** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87128)
- **CVE-2026-83462** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83462)
- **CVE-2026-83452** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83452)
- **CVE-2026-83355** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83355)
- **CVE-2026-83339** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83339)
- **CVE-2026-83327** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83327)
- **CVE-2026-83283** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83283)
- **CVE-2026-83282** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83282)
- **CVE-2026-83269** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83269)
- **CVE-2026-83268** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83268)
- **CVE-2026-83261** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83261)
- **CVE-2026-83260** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83260)
- **CVE-2026-83232** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83232)
- **CVE-2026-83229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83229)
- **CVE-2026-83202** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83202)
- **CVE-2026-83201** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83201)
- **CVE-2026-83197** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83197)
- **CVE-2026-83196** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83196)
- **CVE-2026-83154** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83154)
- **CVE-2026-83151** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83151)
- **CVE-2026-83149** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83149)
- **CVE-2026-83108** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83108)
- **CVE-2026-83107** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83107)
- **CVE-2026-83105** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83105)
- **CVE-2026-83104** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83104)
- **CVE-2026-83103** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83103)
- **CVE-2026-83100** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83100)
- **CVE-2026-83099** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83099)
- **CVE-2026-83098** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83098)
- **CVE-2026-83095** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83095)
- **CVE-2026-83094** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83094)
- **CVE-2026-83066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83066)
- **CVE-2026-83064** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83064)
- **CVE-2026-83062** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83062)
- **CVE-2026-83061** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83061)
- **CVE-2026-83060** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83060)
- **CVE-2026-83059** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83059)
- **CVE-2026-83058** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83058)
- **CVE-2026-83057** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83057)
- **CVE-2026-83056** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83056)
- **CVE-2026-83055** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83055)
- **CVE-2026-83054** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83054)
- **CVE-2026-83043** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83043)
- **CVE-2026-83042** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83042)
- **CVE-2026-83040** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83040)
- **CVE-2026-83039** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83039)
- **CVE-2026-83038** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83038)
- **CVE-2026-83037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83037)
- **CVE-2026-83036** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83036)
- **CVE-2026-83035** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83035)
- **CVE-2026-83031** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83031)
- **CVE-2026-83029** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83029)
- **CVE-2026-83027** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83027)
- **CVE-2026-83021** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83021)
- **CVE-2026-83020** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83020)
- **CVE-2026-83006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83006)
- **CVE-2026-83001** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83001)
- **CVE-2026-83000** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83000)
- **CVE-2026-82999** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82999)
- **CVE-2026-82998** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82998)
- **CVE-2026-82997** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82997)
- **CVE-2026-82995** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82995)
- **CVE-2026-82994** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82994)
- **CVE-2026-81855** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81855)
- **CVE-2026-78225** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78225)
- **CVE-2026-77972** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77972)
- **CVE-2026-77866** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77866)
- **CVE-2026-77179** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77179)
- **CVE-2026-76675** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76675)
- **CVE-2026-76674** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76674)
- **CVE-2026-76673** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76673)
- **CVE-2026-76672** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76672)
- **CVE-2026-76670** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76670)
- **CVE-2026-76669** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76669)
- **CVE-2026-73963** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73963)
- **CVE-2026-73962** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73962)
- **CVE-2026-73961** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73961)
- **CVE-2026-73957** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73957)
- **CVE-2026-73956** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73956)
- **CVE-2026-73953** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73953)
- **CVE-2026-73952** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73952)
- **CVE-2026-73950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73950)
- **CVE-2026-73948** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73948)
- **CVE-2026-73947** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73947)
- **CVE-2026-73946** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73946)
- **CVE-2026-73945** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73945)
- **CVE-2026-73944** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73944)
- **CVE-2026-73940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73940)
- **CVE-2026-73807** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73807)
- **CVE-2026-73458** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73458)
- **CVE-2026-71163** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71163)
- **CVE-2026-71133** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71133)
- **CVE-2026-70913** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70913)
- **CVE-2026-70757** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70757)
- **CVE-2026-70756** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70756)
- **CVE-2026-70748** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70748)
- **CVE-2026-69204** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69204)
- **CVE-2026-68491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-68491)
- **CVE-2026-66890** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66890)
- **CVE-2026-66887** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66887)
- **CVE-2026-63696** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63696)
- **CVE-2026-63695** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63695)
- **CVE-2026-62379** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62379) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-62379)
- **CVE-2026-62263** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62263) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-62263)
- **CVE-2026-61667** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61667)
- **CVE-2026-61568** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61568)
- **CVE-2026-61560** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61560)
- **CVE-2026-61559** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61559)
- **CVE-2026-61549** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61549)
- **CVE-2026-59971** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59971)
- **CVE-2026-57148** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57148) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-57148)
- **CVE-2026-57147** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57147) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-57147)
- **CVE-2026-57141** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57141) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-57141)
- **CVE-2026-57140** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57140) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-57140)
- **CVE-2026-57139** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57139) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-57139)
- **CVE-2026-57138** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57138) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-57138)
- **CVE-2026-55211** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55211)
- **CVE-2026-55158** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55158)
- **CVE-2026-54337** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54337)
- **CVE-2026-53710** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53710)
- **CVE-2026-53459** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53459)
- **CVE-2026-52824** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-52824) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-52824)
- **CVE-2026-48717** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48717) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48717)
- **CVE-2026-46619** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46619) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-46619)
- **CVE-2026-46495** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46495)
- **CVE-2026-46488** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46488)
- **CVE-2026-45579** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45579)
- **CVE-2026-45052** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45052) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-45052)
- **CVE-2026-45051** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45051) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-45051)
- **CVE-2026-39919** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-39919)
- **CVE-2026-19773** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19773)
- **CVE-2026-15640** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15640)
- **CVE-2026-15639** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15639)
- **CVE-2026-15638** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15638)
- **CVE-2026-14349** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14349)
- **CVE-2026-12793** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12793)
- **CVE-2026-12351** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12351)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
