# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**182** 筆符合目前門檻的重要變化；事件統計：EPSS_INCREASED=2、NEW_CVE=177、NEW_KEV=4。
- Intelligence 候選：**30** 筆；P1 **6**、P2 **0**、P3 **19**、WATCH **5**。
- Baseline：state / generated_at=2026-11-19T08:11:03.488229+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-76466、CVE-2026-129448、CVE-2026-123890、CVE-2025-42884、CVE-2026-90817。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **182** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-76466｜Cisco / Expressway Series
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00417 / percentile=0.36836
- **CISA KEV**：listed=true / date_added=2026-11-20 / due_date=2026-11-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-21T17:19:06.813 / 2026-11-21T05:18:23.937
- **官方描述（原文）**：Cisco Expressway Series contains a use of hard-coded credentials vulnerability that allows an unauthenticated, remote attacker with persistent cookies and network access to execute commands as root on a clustered device via the database service.

### 2. CVE-2026-129448｜Apache / Roller
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01191 / percentile=0.68723
- **CISA KEV**：listed=true / date_added=2026-11-20 / due_date=2026-11-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-17T11:17:28.190 / 2026-11-21T05:18:11.013
- **官方描述（原文）**：Apache Roller contains a deserialization of untrusted data vulnerability that allows an unauthenticated remote attacker to execute arbitrary code via the XML-RPC endpoint, which accepts and deserializes vendor extension types before authentication. This CVE covers the same underlying vulnerability as CVE-2026-82384 but applies to a broader range of affected versions.

### 3. CVE-2026-123890｜Broadcom / VMware vCenter
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:25.407)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00843 / percentile=0.58845
- **CISA KEV**：listed=true / date_added=2026-11-20 / due_date=2026-11-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-19T15:17:25.407 / 2026-11-21T05:18:10.817
- **官方描述（原文）**：Broadcom VMware vCenter contains an authentication bypass using an alternate path or channel vulnerability in the VMware Directory Service that allows an unauthenticated attacker with network access to vCenter to bypass authentication and gain unauthorized access to the system.

### 4. CVE-2025-42884｜SAP / NetWeaver
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：0.00276 / percentile=0.2048
- **CISA KEV**：listed=true / date_added=2026-11-20 / due_date=2026-11-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2025-11-11T01:15:36.893 / 2026-11-21T05:18:10.650
- **官方描述（原文）**：SAP NetWeaver Enterprise Portal contains an improper neutralization of special elements in data query logic vulnerability that allows an unauthenticated attacker to disclose or modify server information via injected JNDI environment properties or a URL used during JNDI lookup operations.

### 5. CVE-2026-90817｜Vanderbilt University / Research Electronic Data Capture (REDCap)
- **Delta event**：EPSS_INCREASED (from=0.03749; to=0.25657)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.25657 / percentile=0.98008
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-11-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-20T13:17:44.973 / 2026-11-19T17:19:06.413
- **官方描述（原文）**：Vanderbilt University Research Electronic Data Capture (REDCap) contains a code injection vulnerability which could allow an unauthenticated attacker to execute arbitrary code on the server. An attacker could exploit this via crafted HTTP requests that access an unintended controller route from a public survey context and supply a crafted file-path or stream parameter during data import processing. Exploitation requires knowledge of a valid public survey hash.

### 6. CVE-2026-40217｜BerriAI / LiteLLM
- **Delta event**：EPSS_INCREASED (from=0.1702; to=0.68902)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.68902 / percentile=0.99365
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-12-02
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-04-10T14:16:36.307 / 2026-11-19T17:18:57.120
- **官方描述（原文）**：BerriAI LiteLLM contains an unprotected alternate channel vulnerability that could allow remote attackers to execute arbitrary code via bytecode rewriting at the /guardrails/test_custom_code URI.

### 7. CVE-2026-115560｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:24.610)
- **Risk**：P3 / score 53；reasons：CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.56429 / percentile=0.99079
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:24.610 / 2026-11-20T05:18:38.473
- **官方描述（原文）**：Session serializer mismatch can lead to remote code execution. Session upload progress, when enabled, can store attacker-controlled data in a session key using the php_binary or php_serialize session serializer. If the same session is later read with the php serializer, because session.serialize_handler is changed at runtime or differs between applications sharing a session store, bytes inside the key can be passed to the unserializer. A remote attacker able to submit a multipart upload can inject objects, which may lead to code execution when the reading application contains a suitable gadget chain, or to session corruption or denial of service. This issue affects PHP versions before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.

### 8. CVE-2026-129496｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:28.373)
- **Risk**：P3 / score 41；reasons：CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.09976 / percentile=0.95713
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:28.373 / 2026-11-20T05:18:41.503
- **官方描述（原文）**：Timezone cache use-after-free can lead to remote code execution. In non-thread-safe builds, a diagnostic written to a file-based error_log during module startup, for example for an invalid date.timezone value or a session configuration warning, causes the timezone cache to be allocated in startup memory that is freed while a reference to it is kept. A diagnostic raised early in the first request of a worker, such as the max_input_vars warning, then accesses the freed cache. On such a deployment an unauthenticated remote attacker can crash PHP-FPM, Apache mod_php or CGI workers with a crafted request. Arbitrary code execution may be possible and has been demonstrated with known memory addresses. This issue affects PHP versions before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.

### 9. CVE-2026-129474｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:28.110)
- **Risk**：P3 / score 41；reasons：CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.0865 / percentile=0.95237
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:28.110 / 2026-11-20T05:18:41.323
- **官方描述（原文）**：Use-after-free in magic method backtraces can lead to remote code execution. When collecting the arguments of a method call handled by __call() or __callStatic() for a backtrace, PHP can read stale values that may refer to freed memory. If a fatal error such as exceeding memory_limit occurs while an application enters such a call, with fatal_error_backtraces enabled (the default) and zend.exception_ignore_args disabled, a remote attacker who controls enough request data to influence memory allocation may cause memory corruption, crash the PHP worker or, with knowledge of memory addresses, execute arbitrary code. php.ini-production enables zend.exception_ignore_args, which prevents this. This issue affects PHP versions 8.5.* before 8.5.13.

### 10. CVE-2026-129289｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:27.523)
- **Risk**：P3 / score 41；reasons：CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.1704 / percentile=0.97149
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:27.523 / 2026-11-20T15:17:42.143
- **官方描述（原文）**：PHP-FPM request smuggling through an unread HTTP request body. PHP does not discard the unread part of an HTTP request body at request shutdown when the application has opened php://input without reading it to the end. When the front end reuses backend connections, which is not the default in nginx or Apache (for example nginx with fastcgi_keep_conn on, or Apache mod_proxy_fcgi with enablereuse=on), PHP-FPM can parse the leftover bytes as a new FastCGI request. An unauthenticated remote attacker can use a single crafted multipart/form-data request to forge a backend request with chosen parameters such as SCRIPT_FILENAME, REMOTE_ADDR and PHP_ADMIN_VALUE, which can lead to execution of attacker-controlled PHP code. With LSAPI, subsequent requests on the connection can be disrupted. This issue affects PHP versions before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.

### 11. CVE-2026-129182｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:27.390)
- **Risk**：P3 / score 41；reasons：CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.11007 / percentile=0.96007
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:27.390 / 2026-11-20T15:17:42.000
- **官方描述（原文）**：Use-after-free via repopulation of last_fatal_error_backtrace global after shutdown. A fatal error raised while modified INI settings are restored during request shutdown can repopulate the stored fatal error backtrace after the executor has been cleaned up. The request memory is then freed, and a diagnostic emitted before executor initialization in a later request handled by the same PHP-FPM or mod_php worker can access the stale backtrace. The shutdown error requires per-path configuration of max_memory_limit, or of zlib.output_compression together with output_handler (which .user.ini can also set). The early diagnostic requires Apache per-directory configuration or, for PHP-FPM, a PHP_VALUE or PHP_ADMIN_VALUE parameter sent by the front end. This can cause memory corruption and worker crashes, and may allow remote code execution. This issue affects PHP versions 8.5.* before 8.5.13.

### 12. CVE-2026-126714｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:26.167)
- **Risk**：P3 / score 41；reasons：CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.17587 / percentile=0.97213
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:26.167 / 2026-11-20T15:17:40.600
- **官方描述（原文）**：Partially overwritten session files can lead to remote code execution. The files session save handler, which is the default, writes updated session data into the existing session file without first clearing it. If a write is interrupted, the file can contain the beginning of the new session followed by the end of the old one, and bytes of an ordinary string can later be unserialized as objects. An attacker who can influence the session data, for example through session upload progress, and interrupt a write at a suitable point may inject objects, which can lead to code execution when the application contains a suitable gadget chain. Session data can also be corrupted. This issue affects PHP versions before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.

### 13. CVE-2026-94567｜nukeviet / nukeviet
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:56.790)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:56.790 / 2026-11-20T20:17:51.233
- **官方描述（原文）**：NukeViet CMS is a multi Content Management System. Prior to 4.5.12 and 4.6.02, an attacker with access to an SVG upload flow can hide a script element in an internal DTD entity. NukeViet\Files\Upload::check_svg_tmpfile() loads the document without entity expansion, leaving a DOMEntityReference, and sanitize_svg_dom() inspects only element nodes, while browsers expand the entity when the stored file is served as image/svg+xml. The SVG path also returned before verify_image() and preserved the original bytes, so the hidden script reached disk unchanged. Guest comment attachments make the upload unauthenticated only when a module's comment feature is open to the All or Guest group and allowattachcomm is enabled; module administrators can also use the file manager, allowing same-origin script execution in an administrator's session. This issue is fixed in versions 4.5.12 and 4.6.02.

### 14. CVE-2026-94565｜nukeviet / nukeviet
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:56.500)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:56.500 / 2026-11-20T20:17:50.583
- **官方描述（原文）**：NukeViet CMS is a multi Content Management System. From the 3.x release line until 4.6.01, an unauthenticated visitor can submit a Contact module message containing an event-handler attribute prefixed by a slash. NukeViet\Core\Request::filterTags() tokenizes attributes using only ASCII spaces, so it sees /onerror and misses the ^on denylist, while the browser treats the slash as a separator and activates onerror. The message is stored and rendered without output encoding in the administration panel, which lacks a Content Security Policy, allowing same-origin JavaScript execution when an administrator opens the message. This issue is fixed in version 4.6.01.

### 15. CVE-2026-77369｜daptin / daptin
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:18:59.850)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00397 / percentile=0.34807
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:18:59.850 / 2026-11-19T19:17:33.003
- **官方描述（原文）**：Daptin is a GraphQL/JSON-API headless CMS. From 0.11.4 until 0.12.30, the generic GET /yjs/:documentName WebSocket route in InitializeYjsResources requires a session but does not authorize the database resource selected by a typename.referenceId.columnName room name. The YJS initial-content provider then reads the selected file.* column without CanRead or CanUpdate checks, and bidirectional synchronization allows a low-privileged authenticated user to read or modify restricted row content. Unauthenticated requests are rejected, and standalone non-canonical room names remain shared-by-name rooms. This issue is fixed in version 0.12.30.

### 16. CVE-2026-77359｜datalayer / jupyter-mcp-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:18:59.520)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00503 / percentile=0.43944
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:18:59.520 / 2026-11-19T20:17:54.220
- **官方描述（原文）**：Jupyter MCP Server is a Model Context Protocol server for Jupyter. Prior to 1.0.3, standalone streamable-http mode validates Host and Origin values for /mcp but does not apply the same browser-origin controls to the state-changing /api/connect and /api/stop management routes. A malicious website can use DNS rebinding so that its hostname resolves to a loopback, LAN, VPN, or published-container MCP listener, then send a browser-shaped request that /api/connect accepts to replace runtime_url and document_url values and start a kernel client against attacker-controlled infrastructure. The attacker can thereby cause Jupyter API and WebSocket traffic to reach that infrastructure and can use /api/stop to stop the current notebook kernel. The default broad bind can increase exposure, but the vulnerability is the missing management-route origin boundary, not a lack of Host validation on /mcp. This issue is fixed in version 1.0.3.

### 17. CVE-2026-133872｜lesspass / lesspass
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T17:18:24.293)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T17:18:24.293 / 2026-11-20T20:17:36.573
- **官方描述（原文）**：LessPass self-hosted sync server backend before commit 9469b0c lacks rate limiting on the JWT login endpoints /tokens/auth/ and /auth/jwt/create/, allowing unlimited authentication attempts. Unauthenticated remote attackers can brute force passwords or perform credential stuffing against known account emails to obtain tokens granting read and write access to stored profiles.

### 18. CVE-2026-133493｜D-Link / DIR-600L
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T07:17:10.853)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.02514 / percentile=0.85187
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T07:17:10.853 / 2026-11-20T18:18:49.200
- **官方描述（原文）**：A vulnerability was identified in D-Link DIR-600L 2.17b02. Affected is the function genacgi_main of the file gena.cgi of the component GENA Handler. Such manipulation leads to os command injection. The attack can be launched remotely. The exploit is publicly available and might be used.

### 19. CVE-2026-133189｜Red Hat / Red Hat OpenStack Platform 13 (Queens)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:18:36.627)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.01467 / percentile=0.74348
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:18:36.627 / 2026-11-19T18:18:13.087
- **官方描述（原文）**：A command injection vulnerability was found in OpenStack Cinder's SSH-based storage-driver support. Incomplete validation of shell metacharacters allows an authenticated user who owns a volume on an affected backend to supply crafted connection information and inject additional commands into the storage array's management interface. Commands execute with the privileges of Cinder's configured backend account. This can disclose storage configuration information and, where that account has administrative permissions, could allow changes that affect the integrity or availability of other tenants' storage.

### 20. CVE-2026-130158｜lbr38 / repomanager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T19:17:25.680)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：0.00322 / percentile=0.25831
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T19:17:25.680 / 2026-11-20T21:17:34.437
- **官方描述（原文）**：RepoManager is a self-hosted deb/rpm package repository. Prior to 5.13.3, a registered host or a party with its host/API credential can submit package metadata. Inventory reporting accepts package name and version, while available-update reporting accepts package name, version, and repository; the repository field exists only on that path. RepoManager stores these values, and stored values are rendered on the host's package detail page without preventing stored HTML or JavaScript from executing. An administrator must later view the page for script execution. The script runs in the administrator's authenticated browser session and can expose administrative data or forge privileged requests; the advisory describes possible escalation through admin-only functionality. Fixed in 5.13.3.

### 21. CVE-2026-129175｜U.S. Department of the Interior / Unstable Slope Management Program
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T20:17:21.980)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T20:17:21.980 / 2026-11-20T20:17:21.980
- **官方描述（原文）**：U.S Department of the Interior Unstable Slope Management Program allows an unauthenticated user to inject unauthorized SQL commands that allow the attacker to gain root access and complete control over the database. Fixed on or around 2026-10-19.

### 22. CVE-2026-128138｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T18:18:06.150)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00914 / percentile=0.60974
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T18:18:06.150 / 2026-11-19T19:17:21.040
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. From 3.10.3 until 3.10.4, the NLTK 3.10.3 JVM hardening validates Java launcher tokens in the options channel but appends the caller-controlled cmd sequence without requiring its first token to be a main class. Supplying -jar or an @argfile through nltk.internals.java or StanfordSegmenter.java_class can therefore execute attacker-selected Java bytecode without the unsafe-JAR opt-in. This issue is fixed in version 3.10.4.

### 23. CVE-2026-120753｜Eclipse Foundation / Eclipse Ditto
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:25.013)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00782 / percentile=0.56908
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:25.013 / 2026-11-19T20:17:21.490
- **官方描述（原文）**：In Eclipse Ditto versions 1.1.0 to 3.9.8, when pre-authentication is enabled, the gateway service accepts the pre-authenticated subject not only from the `x-ditto-pre-authenticated` HTTP header set by a trusted reverse proxy, but also from an undocumented `x-ditto-pre-authenticated` URL query parameter that a client can set. A reverse proxy that only overwrites the header therefore does not stop clients from supplying their own subject. With the default configuration of the Ditto Helm chart (`global.jwtOnly: false`, which implicitly enables pre-authentication), the bundled nginx skips HTTP Basic authentication for any request with an `Authorization: Bearer` header and forwards it without the pre-authentication header. An unauthenticated remote attacker can send an invalid Bearer token together with the query parameter to authenticate as any chosen policy subject. Pre-authentication succeeds before the JWT is validated, so the attacker can read and modify Things and Policies with that subject's permissions. As a mitigation, disable pre-authentication in the gateway (`ENABLE_PRE_AUTHENTICATION=false`) or, when using the Helm chart, configure `global.jwtOnly: true`.

### 24. CVE-2026-115407｜Eclipse Foundation / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T17:18:07.373)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T17:18:07.373 / 2026-11-20T19:18:36.020
- **官方描述（原文）**：In `github.com/eclipse-keypont/crypto11/v2` versions `<= 2.0.0-rc8` (and the deprecated v1 module paths `github.com/eclipse-keypont/crypto11 <= 1.6.8`, `github.com/ThalesGroup/crypto11 <= 1.7.0-rc1` and `github.com/ThalesIgnite/crypto11 <= 1.2.5`), the `cipher.AEAD` returned by `SecretKey.NewGCM()` passes whatever nonce it is given straight to `CK_GCM_PARAMS` without checking its length against `NonceSize()`, and accepts an empty nonce. On a token that accepts a zero-length GCM IV — SoftHSM2 does — every `Seal` with an empty nonce encrypts under the same IV, reusing the keystream and exposing the GHASH authentication key, which allows forgeries. Separately, `Config.UseGCMIVFromHSM` sends a NULL IV with length zero to the token unless `GCMIVFromHSMControl.SupplyIvForHSMGCMEncrypt` is also set, so the token has nowhere to write the IV it generates: a `Seal` with a non-empty nonce panics after the plaintext has already been encrypted, and a `Seal` with an empty nonce returns ciphertext under an empty IV without error. On the v1 line HSM-IV mode additionally never copies the token-generated IV back to the caller, so the caller keeps its own nonce while the data was encrypted under another one.

### 25. CVE-2026-114516｜ether / etherpad
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:17:54.773)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01485 / percentile=0.74647
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:17:54.773 / 2026-11-20T14:17:43.853
- **官方描述（原文）**：Etherpad is a real-time collaborative editor. From 1.8.14 until 3.3.3, the pre-authentication /static/* plugin asset handler in src/node/utils/Minify.ts performs a backslash-to-forward-slash conversion after src/node/utils/sanitizePathname.ts has completed its POSIX path checks. On POSIX systems the sanitizer correctly treats backslashes as ordinary filename bytes, but the later conversion turns encoded backslash-separated parent-directory segments into traversal components without revalidation or containment. The expressPreSession registration and the always-present ep_etherpad-lite core pseudo-plugin make this path reachable without credentials, allowing a remote attacker to read any file available to the Etherpad process. Disclosed configuration or environment secrets can expose administrator credentials, after which the administrator plugin installer can provide in-process code execution and full server compromise. This issue is fixed in version 3.3.3.

### 26. CVE-2026-94564｜nukeviet / nukeviet
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:56.357)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:56.357 / 2026-11-20T20:17:49.947
- **官方描述（原文）**：NukeViet CMS is a multi Content Management System. Prior to 4.6.01, an unauthenticated visitor can submit Contact module content containing numeric HTML entities with more than eight leading zeros in a URL-bearing attribute. NukeViet\Core\Request::unhtmlentities() does not decode that form before filterAttr() checks for a javascript: scheme, but browsers decode it when rendering the stored content. With an allowed tag such as the default iframe, the reconstructed script URL executes in the administration origin when staff view the message, permitting session-riding actions while remaining unable to read the HttpOnly session cookie directly. This issue is fixed in version 4.6.01.

### 27. CVE-2026-86017｜isomorphic-git / isomorphic-git
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:55.490)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.0 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:55.490 / 2026-11-20T21:17:39.417
- **官方描述（原文）**：isomorphic-git is a pure JavaScript implementation of Git for Node.js and browsers. Prior to 1.38.8, git cherry-pick applies tree changes through applyTreeChanges in src/utils/walkerToTreeEntryMap.js without checking whether a leading path component is a symbolic link. If a victim worktree contains a tracked symlink to a location outside the worktree and a cherry-picked tree places a file beneath that path, the write follows the symlink and materializes attacker-controlled blob content at the external destination. This allows arbitrary file writes and can cause data tampering, code injection into interpreted files, privilege escalation, denial of service, or follow-on code execution depending on the selected target path. This issue is fixed in version 1.38.8.

### 28. CVE-2026-77355｜isomorphic-git / isomorphic-git
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:54.933)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:54.933 / 2026-11-20T20:17:48.373
- **官方描述（原文）**：isomorphic-git is a pure JavaScript implementation of Git for Node.js and browsers. Prior to 1.38.7, tree-entry validation in src/models/GitTree.js does not reject the Windows NTFS reserved pathname alias .git::$INDEX_ALLOCATION. When clone() or checkout materializes an attacker-controlled tree containing this alias on Windows using an NTFS filesystem, the alias resolves to the active .git directory and permits writes to trusted repository metadata instead of a normal worktree directory. A malicious repository or object stream can therefore poison repository configuration, hooks, refs, attributes, or other gitdir state. Strict hosting that rejects hasDotgit objects can block the crafted tree, and non-NTFS systems do not interpret the pathname as the active gitdir. isomorphic-git performs the gitdir write but does not itself execute the written hook or configuration; a later native Git or compatible-tool action, such as processing a poisoned core.fsmonitor value, can execute configured commands as the victim developer or CI identity. This issue is fixed in version 1.38.7.

### 29. CVE-2026-77329｜mihai-dinculescu / tapo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T17:18:26.917)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T17:18:26.917 / 2026-11-20T21:17:39.293
- **官方描述（原文）**：Tapo provides Rust and Python APIs and an MCP server for TP-Link Tapo smart devices. From 0.3.1 until 0.5.0, the Streamable HTTP implementation in tapo-mcp/src/server.rs calls disable_allowed_hosts() without replacement Host or Origin validation, while TAPO_MCP_API_KEY remains optional for a listener that can bind to all interfaces. A malicious website can use DNS rebinding to send same-origin browser requests to the victim's local or LAN Tapo MCP listener when it runs without an API key. The attacker can invoke exposed tools including control_device for smart-device actuation and take_snapshot for configured cameras. Deployments with TAPO_MCP_API_KEY set are not affected by the unauthenticated path, and exploitation requires a running listener configured with real Tapo credentials and devices, plus victim interaction with the malicious site. This issue is fixed in version 0.5.0.

### 30. CVE-2026-77326｜MapServer / MapServer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:54.110)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:54.110 / 2026-11-20T20:17:43.973
- **官方描述（原文）**：MapServer is a system for developing web-based GIS applications. From 8.2.0 until 8.6.5, an unauthenticated attacker can send a WMS GetLegendGraphic request with a nonempty BBOX and repeated LAYER parameters to trigger a heap buffer overflow in msWMSDispatch() in src/mapwms.cpp. The handler appends synthesized entries to cgiRequestObj.ParamNames and cgiRequestObj.ParamValues at NumParams without retaining the arrays' capacity or reallocating them, while incrementing NumParams inside the loop. Once the parser's hidden capacity is exhausted, the writes pass the heap allocation boundary. A single request can corrupt heap memory and crash the process; code execution may be possible but was not demonstrated. This issue is fixed in version 8.6.5.

### 31. CVE-2026-77324｜MapServer / MapServer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:53.793)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:53.793 / 2026-11-20T21:17:39.170
- **官方描述（原文）**：MapServer is a system for developing web-based GIS applications. From 4.4.0 until 8.6.5, an unauthenticated remote attacker can send a WCS GetCoverage XML POST request whose BoundingBox element omits the crs attribute, causing xmlGetProp() in src/mapwcs.cpp to return null. msWCSParseRequest() then calls string functions on the null value before normal WCS exception handling, crashing the CGI or FastCGI worker. The analogous KVP or GET path is not affected because it obtains a count-validated, non-null token. A single request can terminate one worker, and repeated requests can exhaust a fixed worker pool and deny service. This issue is fixed in version 8.6.5.

### 32. CVE-2026-77318｜datalayer / jupyter-mcp-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:18:59.027)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.3 (HIGH)
- **EPSS**：0.00505 / percentile=0.44078
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:18:59.027 / 2026-11-19T19:17:32.883
- **官方描述（原文）**：Jupyter MCP Server is a Model Context Protocol server for Jupyter. Prior to 1.0.3, standalone streamable-http mode can enforce MCP_TOKEN on /mcp while leaving the state-changing /api/connect and /api/stop management routes unauthenticated. An unauthenticated network caller can use /api/connect to replace runtime_url and document_url values and their tokens, reset ServerContext, and start a kernel client against attacker-controlled infrastructure, causing the server to send Jupyter API and WebSocket traffic to that backend. The caller can also use /api/stop to stop the current notebook kernel. This boundary failure does not require explicit insecure no-auth mode and occurs outside normal MCP JSON-RPC tool dispatch. This issue is fixed in version 1.0.3.

### 33. CVE-2026-77313｜flytohub / flyto-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:18:44.183)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：0.0028 / percentile=0.21015
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:18:44.183 / 2026-11-20T17:18:26.793
- **官方描述（原文）**：Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, validate_url_ssrf in src/core/utils.py resolves and checks a hostname but returns the hostname URL rather than the validated address, and session.get in http.get performs an independent DNS lookup when connecting. A low-privileged caller with control of the hostname's DNS can make the first lookup return a public address and the connection-time lookup return an internal address, bypassing the SSRF guard for all modules that call it and exposing readable internal or metadata-service responses. Successful exploitation requires attacker-controlled DNS and a successful timing-dependent answer change between the two lookups. This issue is fixed in version 2.26.8.

### 34. CVE-2026-77309｜NASA-AMMOS / AIT-GUI
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T18:18:55.847)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T18:18:55.847 / 2026-11-20T19:18:53.477
- **官方描述（原文）**：AIT GUI provides a framework for building custom websites for real-time telemetry monitoring, commanding, and other mission operations. From 1.0.0 until 2.5.1, POST /tlm/query in ait/gui/__init__.py writes attacker-controlled field data to fields_in.txt, and its no-PCAP error path can abort before deleting that file. The unauthenticated POST /script/run route accepts a scriptPath that resolves outside ScriptRoot, reads the selected file, and executes it as Python. A network-reachable attacker can obtain the ordinary session cookie without credentials, combine the two routes, and execute arbitrary Python code with the AIT-GUI server process privileges. This issue is fixed in version 2.5.1.

### 35. CVE-2026-63202｜netty / netty-incubator-codec-ohttp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:18:07.520)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00335 / percentile=0.27513
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:18:07.520 / 2026-11-20T14:17:53.427
- **官方描述（原文）**：netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.0.23.Final, BinaryHttpParser.readFieldSection in codec-bhttp/src/main/java/io/netty/incubator/codec/bhttp/BinaryHttpParser.java loops while fieldSectionLength is nonzero and relies on disabled-by-default assertions to require BinaryHttpParser.readFieldLine to return a value and consume bytes. A corrupt field line can consume more bytes than its understated declared section length and drive the counter negative, or a truncated field line can return without consuming data and leave the parser in the same state. An unauthenticated OHTTP peer can encrypt such Binary HTTP content under the gateway public configuration, reach OHttpRequestResponseContext.ContentDecoder.decodeChunk, and permanently pin a Netty event-loop thread at full CPU before application business logic. Multiple requests can exhaust the event-loop group and deny service until restart. This issue is fixed in version 0.0.23.Final.

### 36. CVE-2026-62255｜samtools / htslib
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T16:21:37.430)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T16:21:37.430 / 2026-11-19T21:45:07.307
- **官方描述（原文）**：HTSlib is a library for reading and writing bioinformatics file formats. Prior to 1.21.2, 1.22.3, 1.23.2, and 1.24, cram_index_load does not verify that the number of reference sequences in a CRAM .crai index does not exceed the CRAM header reference count. A malformed index can drive unbounded index-array allocation, and when the number of references in the index is within two of INT_MAX, the growth calculation can wrap, read beyond a heap buffer, and use the resulting value as a pointer for an unchecked memory write. Any region query can trigger the flaw, causing denial of service or memory corruption. This issue is fixed in versions 1.21.2, 1.22.3, 1.23.2, and 1.24.

### 37. CVE-2026-61798｜netty / netty-incubator-codec-ohttp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:18:06.490)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:18:06.490 / 2026-11-20T14:17:53.310
- **官方描述（原文）**：netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.0.23.Final, BoringSSLAsymmetricCipherKeyPair.toString in codec-ohttp-hpke-classes-boringssl/src/main/java/io/netty/incubator/codec/hpke/boringssl/BoringSSLAsymmetricCipherKeyPair.java includes its private parameter, BoringSSLAsymmetricKeyParameter.toString in codec-ohttp-hpke-classes-boringssl/src/main/java/io/netty/incubator/codec/hpke/boringssl/BoringSSLAsymmetricKeyParameter.java renders the complete private-key byte array when isPrivate is true, and BoringSSL.EVP_HPKE_KEY_init_or_throw in codec-ohttp-hpke-classes-boringssl/src/main/java/io/netty/incubator/codec/hpke/boringssl/BoringSSL.java includes rejected privateKeyBytes in an exception message. Applications that log affected key-pair objects or initialization exceptions can persist complete HPKE private key material in logs or telemetry. Anyone who can read those records can recover the key and may compromise OHTTP message confidentiality or authenticity expectations while the key remains usable. This issue is fixed in version 0.0.23.Final.

### 38. CVE-2026-59988｜tony / django-docutils
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:18:58.550)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：0.0044 / percentile=0.39151
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:18:58.550 / 2026-11-20T22:17:51.047
- **官方描述（原文）**：django-docutils provides reStructuredText support for Django. Prior to 0.30.0, public rendering paths including publish_doctree, publish_html_from_source, publish_html_from_doctree, publish_parts_from_doctree, the {% rst %} template tag, the rst template filter, DocutilsTemplates, and DocutilsView pass lower-trust reStructuredText to Docutils without disabling file_insertion_enabled, raw_enabled, ambient docutils.conf processing, or unsafe URI schemes and without consistently sanitizing doctrees. An attacker who can influence rendered reStructuredText can use include or csv-table directives to read local files or cause server-side URL requests, or use raw HTML and unsafe URI output to inject stored script-capable content. Applications that render only trusted static reStructuredText are not affected unless attackers can influence it. This issue is fixed in version 0.30.0.

### 39. CVE-2026-55372｜nukeviet / nukeviet
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:52.607)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:52.607 / 2026-11-20T19:18:52.607
- **官方描述（原文）**：NukeViet CMS is a multi Content Management System. Prior to 4.5.09, an unauthenticated attacker can submit the __serverInfoUpdate=1 field while controlling X-Forwarded-Host and X-Forwarded-Proto. NukeViet\Core\Server::standardizeHost() did not validate the forwarded host against my_domains, and a trailing slash could preserve an attacker-selected port that server_info_update() used to construct a cURL request in includes/ini.php before authentication. The blind, HEAD-only request uses a fixed path, but it permits internal host and port discovery and can poison cached server_headers. This issue is fixed in version 4.5.09.

### 40. CVE-2026-48118｜nukeviet / nukeviet
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:51.957)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:51.957 / 2026-11-20T19:18:51.957
- **官方描述（原文）**：NukeViet CMS is a multi Content Management System. Prior to 4.5.09, the Comment module accepts attacker-controlled base64 content in the status_comment parameter through modules/comment/funcs/main.php; modules/comment/comment.php decodes it with nv_base64_decode() and assigns it to STATUS_COMMENT without output escaping. The required checkss token was derived from the site-wide NV_CACHE_PREFIX rather than NV_CHECK_SESSION, so a token disclosed in public comment markup could be reused across sessions in a crafted URL. An unauthenticated attacker can therefore cause decoded HTML or JavaScript to render in a victim's browser and perform phishing or same-origin actions. This issue is fixed in version 4.5.09.

### 41. CVE-2026-45356｜Netatalk / netatalk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T18:18:53.130)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T18:18:53.130 / 2026-11-20T20:17:41.400
- **官方描述（原文）**：Netatalk is a Free and Open Source file server suite for Unix-like operating systems. Prior to 4.4.3, the afpd Spotlight RPC unmarshalling loop in etc/afpd/spotlight_marshalling.c subtracts an attacker-controlled subcount from the unsigned count variable in sl_unpack_loop without verifying that subcount is not larger. An authenticated AFP client can place an excessive element count in the sl_unpack_ints, sl_unpack_uuid, sl_unpack_floats, or sl_unpack_date handler, or in a null element, so the subtraction wraps near UINT_MAX and the loop continues reading heap memory at increasing offsets up to toc_offset, which is capped at 65000. The out-of-bounds values can be stored in dalloc structures and returned in the Spotlight RPC response, disclosing heap contents. This issue is fixed in version 4.4.3.

### 42. CVE-2026-45355｜Netatalk / netatalk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T18:18:52.967)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T18:18:52.967 / 2026-11-20T19:18:51.833
- **官方描述（原文）**：Netatalk is a Free and Open Source file server suite for Unix-like operating systems. Prior to 4.4.3, the afpd Spotlight RPC string unmarshalling path in etc/afpd/spotlight_marshalling.c uses sl_unpack_cpx to calculate slen from qlen and the attacker-controlled used_in_last_block value without preventing a negative result. An authenticated AFP client can send a complex string or UTF-16 string element that makes slen negative, and the implicit conversion to size_t causes dalloc_strndup or convert_string_allocate to read beyond the heap buffer. The out-of-bounds read can expose heap data through the RPC response or crash the worker process. This issue is fixed in version 4.4.3.

### 43. CVE-2026-133707｜ropensci / targets
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T13:18:46.853)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T13:18:46.853 / 2026-11-20T14:17:52.917
- **官方描述（原文）**：The targets R package before 1.12.1 contains a code execution vulnerability that allows attackers to run arbitrary R code by planting format functions in the data store metadata file. Attackers can supply a crafted _targets data store whose custom format or CAS repository functions are passed to eval(parse()), executing code when victims call tar_read(), tar_load() or tar_workspace().

### 44. CVE-2026-133680｜D-Link / DCS-935L
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T20:17:35.750)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T20:17:35.750 / 2026-11-20T20:17:35.970
- **官方描述（原文）**：A vulnerability was found in D-Link DCS-935L 1.10.01. This affects the function loginRouter of the file web/cgi-bin/localrecording/setconf.cgi of the component Local Recording CGI. Performing a manipulation of the argument account/password results in os command injection. Remote exploitation of the attack is possible. The exploit has been made public and could be used.

### 45. CVE-2026-133501｜未確認 / Gladys Assistant
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T09:20:07.277)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：0.00766 / percentile=0.564
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T09:20:07.277 / 2026-11-20T15:17:49.133
- **官方描述（原文）**：A security flaw has been discovered in Gladys Assistant up to 4.71.0. This impacts an unknown function of the file server/lib/gateway/gateway.downloadBackup.js of the component Backup Restore Handler. The manipulation results in path traversal. The attack can be launched remotely. The exploit has been released to the public and may be used for attacks. Upgrading to version 4.72.0 will fix this issue. It is recommended to upgrade the affected component.

### 46. CVE-2026-133476｜Dolibarr / Dolibarr ERP/CRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:18:04.370)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00442 / percentile=0.39251
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:18:04.370 / 2026-11-20T14:17:51.030
- **官方描述（原文）**：In Dolibarr before 24.0.3, dolForgeSQLCriteriaCallback() in htdocs/core/lib/functions.lib.php allows account takeover because it strips only a single table-name prefix from a Universal Search Filter (sqlfilters) operand before checking it against the forbidden-field denylist (pass, pass_crypted, api_key). MariaDB and MySQL accept a two-level qualification such as schema.alias.column, so an operand of the form dolibarr.u.pass_crypted survives the check and is emitted into the WHERE clause. A remote authenticated user holding only the holiday read and readall permissions, which confer no user-management or administrative access, can use the resulting boolean oracle at GET /api/index.php/holidays to recover any user's bcrypt password hash and api_key one character at a time, including an administrator's. Because api_key is accepted directly by the REST API as a bearer credential, this yields full administrative control of the application. This bypasses the fix for CVE-2026-89012, which added only a strtolower() call and did not address prefix depth. The same denylist also omits pass_temp, which stores a password in cleartext, as well as national_registration_number, salary, birth, address, personal_mobile and note_private.

### 47. CVE-2026-133235｜TandoorRecipes / recipes
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T16:21:26.227)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：0.0044 / percentile=0.39151
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T16:21:26.227 / 2026-11-19T19:17:28.773
- **官方描述（原文）**：Tandoor Recipes before 2.7.4 contains a server-side request forgery vulnerability that allows space admins to reach internal hosts because Nextcloud.get_client builds WebDAV clients from Storage.url without calling safe_request. Attackers can create a NEXTCLOUD storage via POST /api/storage/ pointing at internal hosts, import a file, then call GET /api/get_recipe_file/<id>/ to read internal service or cloud metadata responses.

### 48. CVE-2026-133173｜opsre / WatchAlert
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:37.410)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00497 / percentile=0.43505
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:37.410 / 2026-11-19T19:17:28.250
- **官方描述（原文）**：WatchAlert 2.0.0 through 3.9.20 contains an insecure direct object reference vulnerability in the /api/w8t/datasource/dataSourceGet endpoint that lets authenticated users read other tenants' datasources because lookups omit tenant_id filtering. Tenant members with datasource view permission can request another tenant's datasource ID to obtain basic auth passwords, AWS and Alibaba Cloud keys, and Kubernetes kubeconfigs.

### 49. CVE-2026-133113｜gogs / gogs
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T14:17:28.367)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00375 / percentile=0.32304
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T14:17:28.367 / 2026-11-19T21:45:07.273
- **官方描述（原文）**：Gogs through 0.14.4 contains an authorization bypass vulnerability that allows collaborators with write access to push to protected branches by merging pull requests. Because MergePullRequest skips branch protection checks and PullRequest.Merge omits hook environment variables, attackers can merge commits into branches restricted to allowlisted users.

### 50. CVE-2026-132275｜deeplook / svglib
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T17:18:12.567)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T17:18:12.567 / 2026-11-20T19:18:46.433
- **官方描述（原文）**：svglib reads SVG files and converts them to other formats. Prior to 2.3.1, the svg2rlg() renderer recursively expands nested SVG <use> references by deep-copying each referenced subtree; SvgRenderer.renderUse() in src/svglib/svglib.py calls xlink_href_target(), which rejects direct cycles but permits acyclic reference graphs with repeated fan-out. A small attacker-controlled SVG can therefore trigger exponentially increasing node expansion, consuming excessive CPU and memory in any application that renders it without a non-default option; HTML-to-PDF workflows using xhtml2pdf can reach the same renderer when an embedded data:image/svg+xml image in an HTML img element is passed to pisa.CreatePDF(). This issue is fixed in 2.3.1.

### 51. CVE-2026-132039｜Eclipse Foundation / Eclipse Ditto
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:32.450)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00489 / percentile=0.42984
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:32.450 / 2026-11-19T15:17:32.450
- **官方描述（原文）**：In Eclipse Ditto versions before 3.9.9, Thing events delivered via WebSocket, Server-Sent Events and connections disclose field values which the policy does not allow the subscriber to read. A READ revoke for one subject of the subscriber's authorization context is not applied when another of its subjects is granted READ. For subscribers with partial READ access, subscription RQL filters, the SSE `_context`, `thing-json` placeholders and extra fields are evaluated on the unfiltered event. This allows an authenticated subscriber with at least partial READ access to a Thing to obtain the values of fields it may not read when events for that Thing are emitted.

### 52. CVE-2026-130160｜lbr38 / repomanager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T19:17:25.967)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00539 / percentile=0.46266
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T19:17:25.967 / 2026-11-19T20:17:28.210
- **官方描述（原文）**：RepoManager is a self-hosted deb/rpm package repository. Prior to 5.13.3, an authenticated user can supply a user-controlled, array-valued GPG key identifier to the key deletion action. Validate::string() filters HTML characters but not shell metacharacters. The user-controlled identifier reaches the delete action without shell-safe encoding. controllers/Gpg.php contains the vulnerable deletion path. Process::execute() passes the command string through proc_open() and /bin/sh -c, allowing the attacker to execute arbitrary OS commands as the web/PHP process. This can expose secrets or poison packages. Authentication is required, but the advisory makes an administrator-only restriction conditional on the intended access policy and does not establish an administrator role as a prerequisite. Fixed in 5.13.3.

### 53. CVE-2026-129700｜Eclipse Foundation / Eclipse Ditto
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:29.067)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:29.067 / 2026-11-19T20:17:25.483
- **官方描述（原文）**：In Eclipse Ditto versions 2.4.0 to 3.9.8, Thing fields a requester is not allowed to read can be disclosed through the `condition` and `live-channel-condition` headers, which are evaluated against the full Thing: the READ check of `live-channel-condition` is skipped when a `condition` header is also present on Thing query commands (3.0.0 to 3.9.8); both headers are evaluated without any authorization on WoT Thing Description requests (`Accept: application/td+json`) when WoT TD permission filtering is not active (by default in 3.0.0 to 3.8.14, in 2.4.x with WoT integration enabled, and in 3.9.x with filtering disabled); the `condition` of live messages and live events is evaluated without a READ check, and of claim messages without any permission (3.1.0 to 3.9.8); and the twin response of a Thing query with a non-matching `live-channel-condition` is returned without filtering it by the policy (3.0.0 to 3.9.8). This allows an authenticated user to read Thing fields they are not allowed to read, in some cases without any permission on the Thing.

### 54. CVE-2026-129699｜Eclipse Foundation / Eclipse Ditto
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:28.930)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:28.930 / 2026-11-19T20:17:25.360
- **官方描述（原文）**：In Eclipse Ditto versions 2.0.0 to 3.8.14 and 3.9.0 to 3.9.8, the authorization check for JSON merge patch commands on Things (HTTP `PATCH` / Ditto Protocol `merge`) does not check permissions for fields deleted or set to an empty object by the patch: fields with a `null` value or an empty object value (`{}`) are skipped by the check, and Ditto's regex-based key deletion with the documented `{{ ~<regex>~ }}` syntax is not recognized as a deletion. An authenticated user with WRITE permission on any part of a Thing can therefore delete other attributes, features and the definition of that Thing, or overwrite or create fields as empty objects, including parts the policy revokes or never grants WRITE on. -->

### 55. CVE-2026-129229｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T18:18:07.940)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00691 / percentile=0.53742
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T18:18:07.940 / 2026-11-20T22:17:49.180
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. From 3.10.0 until 3.10.4, TokenSearcher.findall and Text.findall accept caller-controlled regular expressions with an unbounded number of capturing groups throughout the affected range. Starting in 3.10.3, nltk.redos.compile and RegexpTokenizer expose the same compile-time vector. The third-party regex engine compiles group-dense patterns with roughly quadratic cost before the match-time timeout begins, allowing a small unauthenticated request to exhaust CPU and deny service. This issue is fixed in version 3.10.4.

### 56. CVE-2026-129179｜U.S. Department of the Interior / Unstable Slope Management Program
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T20:17:22.727)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T20:17:22.727 / 2026-11-20T20:17:22.727
- **官方描述（原文）**：U.S Department of the Interior Unstable Slope Management Program allows attackers with valid local application credentials to establish an application session by sending JSON POST requests to the application's login endpoint without a Referrer header or completing the intended Keycloak flow. Fixed on or around 2026-10-19.

### 57. CVE-2026-129178｜U.S. Department of the Interior / Unstable Slope Management Program
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T20:17:22.563)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T20:17:22.563 / 2026-11-20T20:17:22.563
- **官方描述（原文）**：U.S Department of the Interior Unstable Slope Management Program stores local user passwords as unsalted MD5 hashes. Fixed on or around 2026-10-19.

### 58. CVE-2026-129177｜U.S. Department of the Interior / Unstable Slope Management Program
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T20:17:22.390)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T20:17:22.390 / 2026-11-20T20:17:22.390
- **官方描述（原文）**：U.S Department of the Interior Unstable Slope Management Program contains a vulnerable endpoint that allows an unauthenticated attacker, without a cookie header, to send a POST request resulting in the creation of a new user. Fixed on or around 2026-10-19.

### 59. CVE-2026-129176｜U.S. Department of the Interior / Unstable Slope Management Program
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T20:17:22.207)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T20:17:22.207 / 2026-11-20T20:17:22.207
- **官方描述（原文）**：U.S Department of the Interior Unstable Slope Management Program accepts a POST request from an unauthenticated user, with no cookie header, to a specific endpoint allowing for the deletion of specified users. Fixed on or around 2026-10-19.

### 60. CVE-2026-128139｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T18:18:06.303)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00668 / percentile=0.5285
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T18:18:06.303 / 2026-11-20T22:17:48.923
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. From 3.6 to 3.10.3, XMLCorpusView._read_xml_fragment accumulates 1 KiB blocks and repeatedly applies whole-buffer XML validation while a comment or CDATA terminator remains ahead. A large comment in an attacker-controlled corpus file causes quadratic CPU consumption through documented XML corpus readers across the affected range. On 3.6 and 3.9.2, a large CDATA section incurs the quadratic scan before rejection, while on 3.10.3 both comment and CDATA documents are read successfully. This vulnerability is fixed in 3.10.4.

### 61. CVE-2026-122244｜Budibase / budibase
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T17:18:07.970)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T17:18:07.970 / 2026-11-20T19:18:37.957
- **官方描述（原文）**：Budibase is an open-source low-code platform. Prior to 3.50.0, a BASIC application user, or an unauthenticated visitor to a public write form, can store markup in a shared external datasource that a builder or administrator later evaluates in any Handlebars binding Preview that surfaces the value, including the Data-section Formula column editor or any binding drawer. jsonFormatter.format() in packages/frontend-core/src/utils/jsonFormatter.ts leaves raw strings and object keys unescaped, while packages/builder/src/components/common/bindings/EvaluationSidePanel.svelte inserts the formatted result as raw HTML. The Handlebars SafeString path preserves the attacker-controlled value, and the Builder origin lacks a Content-Security-Policy that would block the resulting script. This permits stored script execution in the higher-privileged builder or administrator session rather than the writer's own role, allowing privileged Builder API actions and workspace data access. This issue is fixed in versions 3.50.0 and 4.0.0.

### 62. CVE-2026-95517｜Apache Software Foundation / Apache Tomcat
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:19:56.293)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00056 / percentile=3e-05
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:19:56.293 / 2026-11-20T19:18:57.390
- **官方描述（原文）**：Reliance on obfuscation or encryption of Security-Relevant inputs without integrity checking, Improper validation of integrity check value, Cleartext transmission of sensitive information vulnerability in the EncryptInterceptor of Apache Tomcat. This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.27, from 10.1.0-M1 through 10.1.61, from 9.0.13 through 9.0.123. The following versions were EOL at the time the CVE was created but are known to be affected: from 8.5.38 through 8.5.100, from 7.0.100 through 7.0.109. Other unsupported versions may also be affected. Users are recommended to upgrade to version 11.0.29, 10.1.62 or 9.0.124 and switch to TLS-PSK to encrypt cluster communication, which fixes the issue. Note: Tomcat 11.0.28 was not released

### 63. CVE-2026-87977｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T21:18:06.517)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00484 / percentile=0.42621
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T21:18:06.517 / 2026-11-20T05:18:57.807
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is vulnerable to SQL injection in the edge-controller component. An unauthenticated remote attacker could exploit this vulnerability to access or modify sensitive database information.

### 64. CVE-2026-86130｜WatchGuard / Dimension
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T19:17:35.673)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00691 / percentile=0.53763
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T19:17:35.673 / 2026-11-19T20:17:54.837
- **官方描述（原文）**：A missing authentication vulnerability in WatchGuard Dimension's log collection service allows a remote, unauthenticated attacker to execute arbitrary SQL statements and ultimately execute arbitrary code as the Dimension WebUI process user by sending specially crafted network requests.

### 65. CVE-2026-86094｜WatchGuard / Dimension
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T19:17:35.420)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00401 / percentile=0.35253
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T19:17:35.420 / 2026-11-19T20:17:54.577
- **官方描述（原文）**：WatchGuard Dimension records unredacted session identifiers for logged-in users in its web UI diagnostic log. A low-privileged Dimension Administrator can retrieve this log and extract a Super Administrator's session token while that administrator is logged in, enabling account takeover. This vulnerability is a secondary unmitigated attack path for CVE-2026-78174.

### 66. CVE-2026-84322｜WatchGuard / Dimension
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T19:17:35.287)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00298 / percentile=0.22983
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T19:17:35.287 / 2026-11-19T20:17:54.460
- **官方描述（原文）**：WatchGuard Dimension returns unredacted session identifiers for logged-in users in a management API response. A low-privileged Dimension Administrator can retrieve the active session IDs of other administrators, including Super Administrators, while they are logged in, enabling account takeover.

### 67. CVE-2026-84236｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T21:18:06.053)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00627 / percentile=0.50984
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T21:18:06.053 / 2026-11-20T14:17:54.540
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is vulnerable to insecure deserialization in the SharePoint Tap MulticastTransceiver component. An unauthenticated remote attacker could exploit this vulnerability to execute arbitrary code on the affected system.

### 68. CVE-2026-82339｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T21:18:05.050)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00397 / percentile=0.34778
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T21:18:05.050 / 2026-11-20T14:17:54.160
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is vulnerable to missing authentication in the SharePoint S-TAP RelayService, allowing an unauthenticated network attacker to inject forged audit events and access the active monitoring policy.

### 69. CVE-2026-80188｜BuddyBoss / BuddyBoss Addons
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T14:17:54.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T14:17:54.003 / 2026-11-20T18:18:56.737
- **官方描述（原文）**：The BuddyBoss Addons plugin for WordPress is vulnerable to Authentication Bypass leading to Account Takeover in versions up to, and including, 1.2.1. This is due to the Social Login REST endpoint trusting unverified Apple and Facebook identity-token claims and linking an attacker-controlled provider identifier to an existing WordPress user selected by the token’s email claim. This makes it possible for unauthenticated attackers who know a user’s email address to associate their provider identity with that account, including administrator accounts, and subsequently authenticate as the victim. Successful exploitation requires the BuddyBoss Platform plugin to be installed and active, with the Social Login module and selected provider enabled and configured. On sites with the separate BuddyBoss App JWT component, the vulnerable REST request can return an application token immediately.

### 70. CVE-2026-77367｜daptin / daptin
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:18:59.677)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00604 / percentile=0.49859
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:18:59.677 / 2026-11-19T21:18:04.470
- **官方描述（原文）**：Daptin is a GraphQL/JSON-API headless CMS. Prior to 0.12.30, the generic GET /api/{entity} list endpoint accepts attacker-controlled sort values in PaginatedFindAllWithoutFilters in server/resource/resource_findallpaginated.go without validating the requested column against the table schema. The code uses those values for SELECT and ORDER BY identifier construction, so an embedded identifier quote can terminate the quoted identifier and make the remainder parse as SQL, allowing an unauthenticated attacker to extract unauthorized table data through blind or error-based behavior or repeatedly trigger query failures. This issue is fixed in version 0.12.30.

### 71. CVE-2026-77338｜Oak-and-Sprout / sprout-track
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:18:59.367)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00369 / percentile=0.31564
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:18:59.367 / 2026-11-19T21:18:04.330
- **官方描述（原文）**：Sprout Track is a self-hosted baby tracking application. Prior to 1.3.5, Sprout Track uses a publicly known hardcoded signing secret when JWT_SECRET is unset, and standard setup does not generate a unique secret. On a network-reachable affected deployment, an unauthenticated attacker can sign JWTs with arbitrary claims, including system-administrator claims, to access administrative functionality and read or modify family, child activity, account, and email data. Deployments with a strong unique JWT_SECRET are not affected. Managed and hosted instances were reported remediated. This issue is fixed in version 1.3.5.

### 72. CVE-2026-77312｜flytohub / flyto-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:18:44.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00748 / percentile=0.5582
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:18:44.013 / 2026-11-19T22:18:44.013
- **官方描述（原文）**：Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, the earlier CVE-2026-67429 remediation applied validate_path_with_env_config() to only a hand-picked set of file-writing modules, leaving data.csv.write in src/core/modules/atomic/data/csv_write.py, data.json_to_csv in src/core/modules/atomic/data/json_to_csv.py, file.copy in src/core/modules/atomic/file/copy.py, and file.move in src/core/modules/atomic/file/move.py outside the FLYTO_SANDBOX_DIR confinement boundary. The advisory also identifies unguarded modules across the broader data.*, file.*, and report-writer families. data.csv.write relies on a .. substring denylist that does not reject absolute paths, while the other named modules accept caller-controlled output or destination paths without the canonical guard. A caller able to execute modules or recipes can therefore write attacker-controlled content outside the configured sandbox, potentially overwriting application code, recipes, startup files, scheduled-task files, or authorization files and gaining code execution on the host. This issue is fixed in version 2.26.8.

### 73. CVE-2026-76536｜Splunk / Splunk Enterprise
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T20:17:52.850)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.0031 / percentile=0.24452
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T20:17:52.850 / 2026-11-20T20:17:43.687
- **官方描述（原文）**：In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could use an empty clustering shared secret to read and modify clustering configuration through the cluster configuration Representational State Transfer (REST) API endpoint on a standalone instance. This could expose clustering configuration, persist attacker-controlled clustering settings, and disrupt clustering operations. The vulnerability is possible because Splunk Enterprise accepts the empty clustering shared secret as a shared-authentication candidate on a standalone instance when clustering is turned off.

### 74. CVE-2026-76535｜Splunk / Splunk Enterprise
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T20:17:52.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00367 / percentile=0.31305
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T20:17:52.730 / 2026-11-20T14:17:53.670
- **官方描述（原文）**：In Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could run arbitrary Search Processing Language (SPL) searches through RapidDiag task collection as an authenticated user. With this access, the user could read or modify data and configuration available to that authenticated user. The vulnerability is possible because Splunk Enterprise accepts an empty shared secret when it authenticates RapidDiag task-collection requests. For more information see Using RapidDiag (https://help.splunk.com/en/splunk-enterprise/administer/troubleshoot/9.3/contact-splunk-support/using-rapiddiag) in the Splunk documentation.

### 75. CVE-2026-65094｜NVIDIA / VIRTIO-Net GA
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T03:17:36.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：0.00278 / percentile=0.2068
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T03:17:36.693 / 2026-11-20T18:18:55.723
- **官方描述（原文）**：NVIDIA VIRTIO-Net for Bluefield contains a vulnerability in Virtio-Net where a VM user may cause a Write-What-Where condition by crafted message. A successful exploit of this vulnerability may lead to Code Execution in Virtio-Net scope.

### 76. CVE-2026-62318｜Netatalk / netatalk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T18:18:54.807)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T18:18:54.807 / 2026-11-20T18:18:54.937
- **官方描述（原文）**：Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 2.0.0 until 4.5.1, the DHX2 and DHX2-PAM authentication state machine in etc/uams/uams_dhx2_pam.c permits logincont1 to be invoked again with the same FPLoginCont retID after it has released the global gcry_mpi_t Ra object. When DHX2 or DHX2PAM is enabled in the UAM list, a remote attacker without valid AFP credentials can repeat the first continuation step, causing gcry_mpi_powm to dereference the freed Ra value and gcry_mpi_release to free it again in a privileged afpd worker. The demonstrated result is a repeatable pre-authentication worker crash, and the use-after-free and double-free provide a plausible allocator exploitation primitive although code execution was not demonstrated. This issue is fixed in version 4.5.1.

### 77. CVE-2026-14914｜Tegsoft Yönetim ve Bilişim Hizmetleri Tic. Ltd. Şti. / Tegsoft Contact Center
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T14:17:53.043)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T14:17:53.043 / 2026-11-20T17:18:25.580
- **官方描述（原文）**：Unrestricted upload of file with dangerous type vulnerability in Tegsoft Yönetim ve Bilişim Hizmetleri Tic. Ltd. Şti. Tegsoft Contact Center allows Upload a Web Shell to a Web Server. This issue affects Tegsoft Contact Center: before latest-202611161510.

### 78. CVE-2026-14492｜revmakx / WP Duplicate – WordPress Migration Plugin
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T10:17:28.927)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T10:17:28.927 / 2026-11-20T20:17:39.997
- **官方描述（原文）**：The WP Duplicate – WordPress Migration Plugin plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, 1.1.11 via the save_single_batch_file function. This is due to a PHP type-juggling authentication bypass via loose != comparison with no is_string() guard, combined with unsanitized base64-decoded path construction in save_single_batch_file() lacking any directory traversal containment. This makes it possible for authenticated attackers, with custom-level access and above, to execute code on the server. Exploitation requires that the site owner has completed the plugin's initial setup so that the site_type and prod_key_random_id options are non-empty, though any non-empty secret value is bypassable via the type-juggling flaw.

### 79. CVE-2026-133968｜Project-MONIA / MONAI Label
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:51.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:51.670 / 2026-11-20T22:17:50.750
- **官方描述（原文）**：monailabel (aka MONAI Label) through 0.8.5 allows directory traversal, with resultant remote code execution, via the image parameter to the PUT /datastore/image endpoint, as exploited in the wild starting in September 2026.

### 80. CVE-2026-133949｜Pip maintainers / pip
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:51.517)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:51.517 / 2026-11-20T20:17:37.170
- **官方描述（原文）**：pip prior to v26.2.2 the certifi bundled with pip contains the compromised eMudhra certificates. Upgrading to a secure version of pip should be done either by first upgrading Python to a version that rejects the compromised intermediates (CVE-2026-115557) or use hash pinning with a known-secure version of pip. pip is not vulnerable when using a Python version that rejects the compromised certificates. See the references below for more information.

### 81. CVE-2026-133648｜flowintel / flowintel
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T11:18:33.157)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T11:18:33.157 / 2026-11-20T19:18:48.873
- **官方描述（原文）**：Flowintel disabled TLS certificate verification for all MISP API connections and used unverified SSL contexts for IMAP and SMTP STARTTLS mail connections. This allowed an on-path (man-in-the-middle) attacker positioned between Flowintel and its MISP or mail servers to impersonate the remote server and intercept sensitive data. Affected connections include: - All MISP HTTPS API calls (event retrieval, attribute search, event creation, connectivity checks, and API validation) - SMTP STARTTLS connections used for sending email notifications - IMAP TLS connections used for fetching mail archives and testing connectivity An attacker who can observe or intercept network traffic between Flowintel and the MISP or mail server could: - Capture MISP API keys and mail credentials (SMTP/IMAP passwords) - Read all threat intelligence data exchanged (events, attributes, objects, reports) - Inject or modify threat intelligence data returned to Flowintel The vulnerability required no authentication on the part of the attacker and no user interaction; it was exploitable by any party with a network position between Flowintel and its configured MISP or mail endpoints. Affected versions: Flowintel prior to 4.1.0.

### 82. CVE-2026-133528｜BeamNG GmbH / BeamNG.drive
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T01:17:10.633)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00129 / percentile=0.02615
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T01:17:10.633 / 2026-11-20T01:17:10.633
- **官方描述（原文）**：BeamNG.drive before 0.40.6 contains an out-of-bounds write vulnerability because JIT-compiled LuaJIT traces omit FFI array bounds checks, letting untrusted Lua escape the sandbox. Attackers supplying a malicious mod can JIT-compile an FFI store loop, write out of range using a tostring() address leak, re-enable ffi.load, and run commands as the game user.

### 83. CVE-2026-133325｜Apache Software Foundation / Apache Tomcat
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:18:04.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00179 / percentile=0.077
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:18:04.090 / 2026-11-21T05:18:22.160
- **官方描述（原文）**：Key exchange without entity authentication vulnerability in Apache Tomcat allowed an unauthenticated node to join a cluster when the cluster was secured with TLS 1.3 and TLS-PSK. This issue affects Apache Tomcat: 11.0.28-11.0.29, 10.1.62, 9.0.124. Users are recommended to switch to TLS 1.2 and TLS-PSK or upgrade to version 11.0.30, 10.1.63 or 9.0.125 (when released), which fix the issue.

### 84. CVE-2026-133323｜Mitel / MiCollab
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:18:52.880)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.01662 / percentile=0.77275
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:18:52.880 / 2026-11-19T18:18:13.373
- **官方描述（原文）**：A vulnerability in the Audio, Web, and Video Conferencing (AWV) component of Mitel MiCollab through 10.3 (10.3.0.18) could allow an unauthenticated attacker to conduct a blind command injection attack due to insufficient parameter sanitization. A successful exploit could allow an attacker to execute arbitrary commands within the context of the system. This is MTLVULN-1864.

### 85. CVE-2026-133310｜Wing FTP Software / Wing FTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:18:52.597)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00445 / percentile=0.39587
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:18:52.597 / 2026-11-19T19:17:30.197
- **官方描述（原文）**：Wing FTP Server before 8.2.8 contains a file mask bypass vulnerability allowing attackers to upload restricted files via an embedded NUL byte in Upload Link filenames. Attackers can plant a Lua session file with a chosen UID and send a matching UID cookie to execute operating system commands as the service account.

### 86. CVE-2026-133303｜Mitel / MiCollab
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:18:51.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：0.0055 / percentile=0.46915
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:18:51.670 / 2026-11-19T17:18:51.670
- **官方描述（原文）**：A vulnerability in the Audio, Web, and Video Conferencing (AWV) component of Mitel MiCollab through 10.3 (10.3.0.18) could allow an unauthenticated attacker to leverage pre-staged malicious content to conduct an XML injection attack due to insufficient parameter validation. A successful exploit could allow an attacker to execute arbitrary commands within the context of the system. This is MTLVULN-1862.

### 87. CVE-2026-133212｜@fastify/reply-from / @fastify/reply-from
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T18:18:47.127)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T18:18:47.127 / 2026-11-20T19:18:46.543
- **官方描述（原文）**：@fastify/reply-from is a Fastify plugin that forwards an incoming HTTP request to an upstream server. In versions before 12.9.1, when the plugin forwards a request whose body is not written to the upstream connection, such as a GET, HEAD, or TRACE request that carried a body, or a request with a falsy JSON body, it still forwards the client's Content-Length header while sending no body. The upstream server then treats the bytes of the following request as the unfinished body, which an attacker can use to desynchronize the connection and smuggle a request. The issue is fixed in @fastify/reply-from 12.9.1, and users should upgrade to 12.9.1 or later.

### 88. CVE-2026-133185｜elazarl / goproxy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:39.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.003 / percentile=0.23216
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:39.470 / 2026-11-19T19:17:28.380
- **官方描述（原文）**：Goproxy before 1.9.4 contains a weak key generation vulnerability in NewCounterEncryptorRandFromKey that derives RSA and Ed25519 leaf certificate private keys from public data due to misuse of hash.Sum. Attackers with the CA certificate and one observed leaf certificate can regenerate that host's leaf private key and impersonate the host to clients trusting the proxy CA.

### 89. CVE-2026-132891｜JetBrains / TeamCity
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T11:16:55.263)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00742 / percentile=0.556
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T11:16:55.263 / 2026-11-20T05:18:45.970
- **官方描述（原文）**：In JetBrains TeamCity before 2026.2, 2026.1.4, 2025.11.8 remote code execution was possible via external pull requests

### 90. CVE-2026-132660｜EnterpriseDB / Postgres Enterprise Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T15:17:47.800)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T15:17:47.800 / 2026-11-21T05:18:21.860
- **官方描述（原文）**：In Postgres Enterprise Manager (PEM), several SECURITY DEFINER functions in the pem schema of the PEM backend database are owned by a superuser but do not set a safe search_path. Any PEM user who can connect to the PEM backend database can create objects that these functions use in place of the intended ones, and so run arbitrary SQL with superuser privileges. Temporary objects can be used for this on every supported PostgreSQL version, and objects in the public schema on PostgreSQL 14 backends and backends upgraded from PostgreSQL 14. From PEM 10.6.1, these functions run with a fixed search_path.

### 91. CVE-2026-132659｜EnterpriseDB / Postgres Enterprise Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T15:17:47.637)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T15:17:47.637 / 2026-11-21T05:18:21.597
- **官方描述（原文）**：In Postgres Enterprise Manager (PEM), the row-level security policies on pem.job and pem.jobstep that apply to PEM agents do not limit an agent to its own jobs. An attacker who controls one monitored host, and so its PEM agent certificate, can create, change or delete jobs for every other agent, including the agent on the PEM server. Agents run SQL job steps with the database credentials of the server they monitor, and shell job steps where batch jobs are enabled, so compromising one monitored host can give superuser SQL access to every monitored database and to the PEM backend. From PEM 10.6.1, PEM agents can no longer create jobs or change job definitions or job steps.

### 92. CVE-2026-132658｜EnterpriseDB / Postgres Enterprise Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T15:17:47.477)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T15:17:47.477 / 2026-11-21T05:18:21.293
- **官方描述（原文）**：In Postgres Enterprise Manager (PEM), the pem_agent role, which every PEM agent login inherits, is a member of the PostgreSQL pg_read_server_files and pg_write_server_files roles on the PEM backend database. An attacker who controls any monitored host, and so its PEM agent certificate, can read and write files on the PEM server host as the postgres operating system user. This includes the PEM certificate authority key, which lets the attacker issue certificates for other agents and act as them. From PEM 10.6.1, PEM agents no longer hold these roles.

### 93. CVE-2026-131287｜Splunk / Splunk SOAR
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T20:17:44.650)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00335 / percentile=0.27615
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T20:17:44.650 / 2026-11-20T05:18:44.967
- **官方描述（原文）**：In Splunk SOAR versions below 8.8.0, a user that holds a role with the Playbooks view, edit, execute, and delete permissions could cause existing cross-repository playbook references to run attacker-controlled playbook code. The vulnerability is possible because Splunk SOAR can bind existing cross-repository playbook references to a different source control repository when a deleted repository name is reused.

### 94. CVE-2026-131253｜Splunk / Splunk SOAR
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T20:17:40.407)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00708 / percentile=0.54359
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T20:17:40.407 / 2026-11-20T05:18:43.277
- **官方描述（原文）**：In Splunk SOAR versions below 8.8.0, an authenticated user that holds a role with the Apps edit, Containers edit, and Playbooks execute permissions could use the App Wizard to execute arbitrary code as the user account that runs Splunk SOAR. This could compromise the confidentiality, integrity, and availability of the Splunk SOAR instance. The vulnerability exists because the App Wizard does not validate user-supplied identifiers before incorporating them into generated connector code.

### 95. CVE-2026-131202｜Splunk / Splunk Enterprise Security
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T20:17:33.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00691 / percentile=0.53745
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T20:17:33.250 / 2026-11-21T05:18:12.753
- **官方描述（原文）**：In Splunk Enterprise Security versions below 8.7.0, a user who holds the "ess_admin" Splunk Enterprise Security role could execute arbitrary code on the search head as the user account running Splunk Enterprise by combining lookup file upload and Configuration Checker functionality. The vulnerability is possible because Splunk Enterprise Security does not restrict lookup upload file types or keep Configuration Checker module paths within the intended directory. For more information see Users and roles for Splunk Enterprise Security (https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security) and Create and manage lookups in Splunk Enterprise Security (https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.7/managing-security-content/create-and-manage-lookups-in-splunk-enterprise-security) in the Splunk documentation.

### 96. CVE-2026-129938｜MongoDB / C# Driver
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T20:17:27.663)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00362 / percentile=0.3083
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T20:17:27.663 / 2026-11-19T21:17:52.027
- **官方描述（原文）**：An improper neutralization of delimiters in the MongoDB C# driver's DNS SRV connection-string resolution lets an unauthenticated party who can answer the client's DNS SRV query place a host outside the trusted domain into the client's server list. When an application resolves the connection string through the affected API and connects with the result, application data, authentication credentials and query results may pass through that host. This may result in unintended disclosure of data and credentials and in forged query results.

### 97. CVE-2026-129932｜MongoDB / Java Driver
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T21:17:51.217)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00177 / percentile=0.07501
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T21:17:51.217 / 2026-11-19T21:17:51.217
- **官方描述（原文）**：The MongoDB Java driver applies its DNS seedlist domain restriction to a record value that is later re-interpreted differently when the connection target is parsed, so the name that is checked and the name that is used can differ. An unauthenticated party who can set or forge the DNS service record for the seed domain in a connection string can cause the driver to direct its session to an unrelated host and to complete certificate verification against that host instead. This may result in unintended disclosure of application data and of configured database credentials, and in unintended content being returned to the application as query results.

### 98. CVE-2026-129713｜Danfoss / AK-SM8xxA
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T11:18:30.953)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T11:18:30.953 / 2026-11-20T11:18:30.953
- **官方描述（原文）**：A stack-based buffer overflow in an unauthenticated CGI handler of the Danfoss AK-SM 8xxA Series controller allows remote attackers to send specially crafted HTTP/S POST requests, leading to memory corruption, webserver restart and hypothetically potential arbitrary code execution with webserver privileges. Authentication is not required to exploit this vulnerability.

### 99. CVE-2026-129481｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:28.240)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.04524 / percentile=0.91757
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:28.240 / 2026-11-19T21:45:12.277
- **官方描述（原文）**：Use-after-free after interrupted session shutdown. The session extension records the filename of the executing script when a session starts. If a fatal error occurs in an application callback while the session variables are destroyed at shutdown, such as stream_close() of a user-defined stream wrapper, the pointer is retained after the request memory is freed, and a later request handled by the same worker can free the stale string. An attacker who can trigger such a failing cleanup may crash the worker or corrupt memory; code execution has not been demonstrated. This requires the filename to be allocated in request memory, for example when the script is not cached by OPcache. This issue affects PHP versions 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.

### 100. CVE-2026-129411｜vi-solutions / Visforms extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:17:58.280)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00405 / percentile=0.3566
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:17:58.280 / 2026-11-19T21:45:07.230
- **官方描述（原文）**：Joomla Extension - vi-solutions - Unauthenticated SQL injection in frontend data view filters in Visforms extension 1.0.0-5.6.4, 6.0.0-6.2.1 - Sorting, location radius and published filters of the frontend data view were not properly sanitized, allowing SQL injection, partly without authentication.

### 101. CVE-2026-129410｜vi-solutions / Visforms extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:17:58.147)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00427 / percentile=0.37799
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:17:58.147 / 2026-11-19T21:45:07.213
- **官方描述（原文）**：Joomla Extension - vi-solutions - Code injection via calculation formulas in Visforms extension 1.0.0-5.6.4, 6.0.0-6.2.1 - Calculation field formulas were executed using PHP eval() without validating their content, allowing backend users with field edit permissions to execute arbitrary PHP code.

### 102. CVE-2026-129402｜vi-solutions / Visforms extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:17:57.757)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.0037 / percentile=0.31663
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:17:57.757 / 2026-11-19T21:45:12.330
- **官方描述（原文）**：Joomla Extension - vi-solutions - Unauthenticated SQL injection in reload task in Visforms extension 1.0.0-5.6.4, 6.0.0-6.2.1 - Input placeholders in SQL field statements were inserted without quoting in the public reload task, allowing unauthenticated SQL injection in read queries.

### 103. CVE-2026-129396｜vi-solutions / Visforms extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:17:57.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00628 / percentile=0.51028
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:17:57.070 / 2026-11-19T21:45:08.400
- **官方描述（原文）**：Joomla Extension - vi-solutions - Arbitrary file write leading to remote code execution in CSS editor in Visforms extension 1.0.0-5.6.3, 6.0.0-6.2.0 - The CSS editor did not restrict file names, extensions and paths of created and saved files, allowing privileged backend users to write arbitrary PHP files.

### 104. CVE-2026-129073｜miniOrange / miniorange otp verification
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T13:18:37.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T13:18:37.040 / 2026-11-20T18:18:43.027
- **官方描述（原文）**：Authentication Bypass Using an Alternate Path or Channel vulnerability in miniOrange miniorange otp verification miniorange-otp-verification allows Authentication Abuse.This issue affects miniorange otp verification: from n/a through 5.6.1.

### 105. CVE-2026-129056｜Paul Ryan / Authorizer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T08:18:28.333)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00507 / percentile=0.44159
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T08:18:28.333 / 2026-11-20T20:17:20.980
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in Paul Ryan Authorizer authorizer allows Privilege Escalation.This issue affects Authorizer: from n/a before 3.17.2.

### 106. CVE-2026-129048｜Jacob N. Breetvelt / WP Photo Album Plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T08:17:11.650)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00288 / percentile=0.2184
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T08:17:11.650 / 2026-11-20T20:17:20.473
- **官方描述（原文）**：Improper Control of Generation of Code ('Code Injection') vulnerability in Jacob N. Breetvelt WP Photo Album Plus wp-photo-album-plus allows Remote Code Inclusion.This issue affects WP Photo Album Plus: from n/a through 9.3.06.003.

### 107. CVE-2026-129043｜Tribulant Software / Newsletters
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T14:17:45.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T14:17:45.410 / 2026-11-20T20:17:20.207
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Tribulant Software Newsletters newsletters-lite allows SQL Injection.This issue affects Newsletters: from n/a through 4.18.2.

### 108. CVE-2026-129039｜Tribulant Software / Newsletters
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T14:17:45.273)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T14:17:45.273 / 2026-11-20T20:17:19.633
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Tribulant Software Newsletters newsletters-lite allows Object Injection.This issue affects Newsletters: from n/a through 4.18.2.

### 109. CVE-2026-127057｜Danfoss / AK-SC 355
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T11:18:30.617)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T11:18:30.617 / 2026-11-20T17:18:08.720
- **官方描述（原文）**：The Danfoss legacy AK-SC 355 and AK-SM 800 Series are vulnerable to unauthorized access when default credentials or known passwords are used for authentication. These products were manufactured with default credentials documented in the product manual. All versions are affected.

### 110. CVE-2026-127027｜Analogic / Poste.io
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T15:17:40.763)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T15:17:40.763 / 2026-11-20T17:18:08.600
- **官方描述（原文）**：Poste.io is vulnerable to remote code execution in DMARC report processing. Email sent to dmarc-reports@<domain> is saved without sender verification. Script that runs as root unpacks the attachments using unsafe shell commands, allowing command injection through crafted attachments (e.g. file names or archive contents). A remote unauthenticated attacker who can send an email to the server's port 25 can execute arbitrary commands as root within the Poste.io container. This issue was fixed in version 2.5.22.

### 111. CVE-2026-126088｜Autonomy Logic / OpenPLC Runtime
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T19:17:18.967)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00268 / percentile=0.1931
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T19:17:18.967 / 2026-11-19T20:17:22.267
- **官方描述（原文）**：In Autonomy Logic OpenPLC Runtime versions 4.2.4 and prior, a race condition allows multiple concurrent requests to pass the existence check before any user is committed, resulting in several unauthenticated admin accounts being created.

### 112. CVE-2026-126054｜Google Cloud / Dataform
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T15:17:39.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T15:17:39.943 / 2026-11-20T19:18:39.637
- **官方描述（原文）**：A Path Traversal vulnerability in workspace directory handling and Git integration in Google Cloud Dataform, BigQuery Studio and Colab Enterprise on Google Cloud Platform allows an authenticated remote attacker to read private files and create arbitrary files across tenant repositories using crafted workspace operations and Git integration requests. This vulnerability was patched on 10 October 2026, and no customer action is needed.

### 113. CVE-2026-124772｜XOne / XOneManager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T11:18:30.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T11:18:30.480 / 2026-11-20T19:18:38.850
- **官方描述（原文）**：Authorization bypass in the publication of XOneManager 3.8.3.0 updates. During testing, the server accepted initial requests from an authenticated project member with read-only access without verifying publication permissions. If the workflow is completed, updates with modified content could be distributed to managed devices.

### 114. CVE-2026-124770｜XOne / XOneManager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T11:18:30.210)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T11:18:30.210 / 2026-11-20T19:18:38.730
- **官方描述（原文）**：Authorization bypass in the ‘tablesData’ operation of the POST request to ‘/xmanagercore/api/services/’ in XOneManager 3.8.3.0. An authenticated project member can execute SQL queries using ‘filter’ without the server verifying their execution permissions. The queries use the service account’s permissions. During testing, databases outside the project were queried, including the authentication database.

### 115. CVE-2026-123058｜JTL-Software GmbH / JTL-Shop
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T12:18:39.513)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00582 / percentile=0.4872
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T12:18:39.513 / 2026-11-19T20:17:21.717
- **官方描述（原文）**：The web installer of JTL-Shop executes its state-changing installation tasks without checking whether the shop is already installed, and was not removed or locked after the installation. An unauthenticated remote attacker who can reach the installer directory can supply their own database credentials, create administrator and synchronisation accounts and overwrite the shop configuration. This can lead to a full takeover of the shop, including code execution on the server.

### 116. CVE-2026-121385｜Unknown / User Registration Aide
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T06:17:19.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00179 / percentile=0.07635
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T06:17:19.693 / 2026-11-20T19:18:37.440
- **官方描述（原文）**：The User Registration Aide WordPress plugin through 1.5.3.8 does not verify the current password or a reset token before changing a user's password, allowing unauthenticated attackers who know a user's username and email address to change the password of any account, including administrators, and take it over.

### 117. CVE-2026-120681｜kitae-park / Mang Board
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T10:17:08.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T10:17:08.647 / 2026-11-20T20:17:13.497
- **官方描述（原文）**：The Mang Board plugin for WordPress is vulnerable to authorization bypass in all versions up to, and including, 2.4.7. This is due to the plugin not properly verifying that a user is authorized to perform an action. This makes it possible for unauthenticated attackers to delete any board post — including administrator-owned content — along with its associated comments and file links. A nonce sufficient to pass the initial nonce check is publicly exposed on any board listing page, meaning no prior authentication or privileged access is required to initiate the exploit.

### 118. CVE-2026-120539｜seventhqueen / Restrictions for BuddyPress
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-21T06:16:33.227)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-21T06:16:33.227 / 2026-11-21T06:16:33.343
- **官方描述（原文）**：The Restrictions for BuddyPress plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, 1.5.4 This is due to the plugin splicing the attacker-controlled request URI into a PHP expression inside a double-quoted string and evaluating it with eval(). Because PHP interpolates double-quoted strings, a payload of the form {${...}} in the URL path is executed during interpolation, so no quote breakout is required and WordPress' slashing does not mitigate it. This makes it possible for unauthenticated attackers to execute arbitrary code on the server with a single GET request. The affected conditions ship enabled by default and are evaluated before any logged-in check, so no plugin configuration is needed; the site must have BuddyPress and Paid Memberships Pro active alongside this plugin.

### 119. CVE-2026-118028｜Apache Software Foundation / Apache Tomcat
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:17:58.893)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00162 / percentile=0.05532
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:17:58.893 / 2026-11-20T19:18:36.960
- **官方描述（原文）**：Execution After Redirect (EAR) vulnerability in Apache Tomcat in RedirectValve affecting flags [F], [G] and [R]. This issue affects Apache Tomcat: from 11.0.0-M18 through 11.0.27, from 10.1.20 through 10.1.61, from 9.0.87 through 9.0.123. The following versions were EOL at the time the CVE was created but are known to be affected: 8.5.100. Other unsupported versions may also be affected. Users are recommended to upgrade to version 11.0.29, 10.1.62, 9.0.124, which fixes the issue. Note: Tomcat 11.0.28 was not released

### 120. CVE-2026-116561｜Apache Software Foundation / Apache Tomcat
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:17:58.393)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00188 / percentile=0.08587
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:17:58.393 / 2026-11-20T19:18:36.303
- **官方描述（原文）**：Improper cleanup on thrown exception vulnerability in Apache Tomcat meant that an HTTP 200 response was sent rather than an HTTP 500 response after a AuthException was thrown during Jakarta Authentication secureResponse(). This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.27, from 10.1.0-M1 through 10.1.61, from 9.0.0.M1 through 9.0.123. The following versions were EOL at the time the CVE was created but are known to be affected: from 8.5.0 through 8.5.100. Other unsupported versions may also be affected. Users are recommended to upgrade to version 11.0.29, 10.0.62 or 9.0.124, which fix the issue. Note: Tomcat 11.0.28 was not released

### 121. CVE-2026-116440｜Dell / PowerStore 500T
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T13:17:27.983)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00838 / percentile=0.58679
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T13:17:27.983 / 2026-11-20T05:18:38.857
- **官方描述（原文）**：Dell PowerStore SDNAS contains a buffer overflow vulnerability that could allow an unauthenticated remote attacker to cause a denial of service or potential code execution on the NAS node.

### 122. CVE-2026-116439｜Dell / PowerStore 500T
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T13:17:27.837)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00632 / percentile=0.51223
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T13:17:27.837 / 2026-11-20T05:18:38.703
- **官方描述（原文）**：Dell PowerStore SDNAS contains a path traversal vulnerability that could allow an unauthenticated attacker to read, modify, or delete arbitrary files on the NAS node.

### 123. CVE-2026-111509｜Dell / PowerStore 500T
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T13:17:27.513)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00427 / percentile=0.37809
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T13:17:27.513 / 2026-11-19T16:18:33.930
- **官方描述（原文）**：Dell PowerStore SDNAS contains a cryptographically weak PRNG vulnerability that could allow a network attacker to decrypt or tamper with NAS SSH/SFTP sessions.

### 124. CVE-2026-104099｜fabiolb / fabio
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T20:17:13.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00477 / percentile=0.42108
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T20:17:13.897 / 2026-11-19T21:17:41.080
- **官方描述（原文）**：Fabio is an HTTP(S) and TCP router for deploying applications managed by consul. Prior to 1.7.3, route/table.go selects targets using raw req.URL.Path, while proxy/http_proxy.go applies per-route ACL and basic-auth checks to the selected target and forwards the raw path to the origin. Dot-segment, encoded-dot, or repeated-slash variants can fall through to a less restrictive route that reaches the same backend; the backend then normalizes the path and serves the protected resource without the configured access controls. A less restrictive fallback route must reach the same backend; without one, the request returns 404. This issue is fixed in version 1.7.3.

### 125. CVE-2026-101340｜NLnet Labs / Net::DNS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T13:18:34.770)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T13:18:34.770 / 2026-11-20T19:18:34.150
- **官方描述（原文）**：Net::DNS uses a 16-bit query ID to match responses to the corresponding requests. In versions up to and including 1.57, the ID is obtained from Perl's built-in rand() function. An attacker that can observe the sequence of query IDs is able to expose the internal state of the PNRG and hence predict query IDs before they are transmitted. The victim Net::DNS instance is then exposed to forged responses injected by the attacker. Note that the deduplication cache in 1.57 has no impact on the feasibility of this attack.

### 126. CVE-2026-94566｜nukeviet / nukeviet
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:56.647)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:56.647 / 2026-11-20T20:17:50.980
- **官方描述（原文）**：NukeViet CMS is a multi Content Management System. In 4.6.00, an unauthenticated attacker can rotate X-Forwarded-For because vendor/vinades/nukeviet/Core/Ips.php accepts forwarded client-IP headers without first confirming that REMOTE_ADDR is a trusted proxy. The resulting NV_CLIENT_IP keys the administrator login blocker in includes/core/admin_login.php; changing only the header value bypasses that lockout and permits effectively unlimited password guesses. The same spoofable address is also consumed by the user login blocker in modules/users/funcs/login.php, IP restrictions, bans, flood controls, and security logs, but those additional code-level effects were not dynamically demonstrated. This issue is fixed in version 4.6.01.

### 127. CVE-2026-77382｜aszepieniec / falcon-rust
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:19:00.740)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：0.00274 / percentile=0.20213
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:19:00.740 / 2026-11-19T19:17:33.490
- **官方描述（原文）**：falcon-rust is a Rust implementation of the Falcon post-quantum signature scheme. Prior to 0.2.0, the discrete-Gaussian sampler in src/samplerz.rs evaluates approx_exp, ber_exp, and sampler_z acceptance probabilities with FixedPoint64 values having only 32 fractional bits. The scaling in approx_exp quantizes its input and limits relative precision to about 2^-33, below Falcon's required bound, causing reference known-answer vectors to diverge and invalidating the proof assumption that secret-dependent signature and key distributions are negligibly close to the ideal discrete Gaussian. This is a cryptographic-soundness defect and no practical key-recovery attack has been demonstrated. This issue is fixed in version 0.2.0.

### 128. CVE-2026-77380｜bolt / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:19:00.597)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.2 (MEDIUM)
- **EPSS**：0.00366 / percentile=0.31252
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:19:00.597 / 2026-11-19T19:17:33.363
- **官方描述（原文）**：Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.5, the /bolt/async/upload-url and /bolt/async/embed endpoints validate only a submitted URL before fetching it server-side. The fetchers then follow redirects without revalidating each destination, allowing an authenticated user to bypass UrlSafetyChecker and cause the server to request internal or cloud-metadata addresses. This issue is fixed in version 6.1.5.

### 129. CVE-2026-77379｜bolt / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:19:00.450)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00442 / percentile=0.39322
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:19:00.450 / 2026-11-19T19:17:33.243
- **官方描述（原文）**：Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.4, the public Relation API lacks an access-control filter. Unauthenticated users can query its REST endpoints and GraphQL endpoints to discover metadata about unpublished, draft, and viewless content. This issue is fixed in version 6.1.4.

### 130. CVE-2026-77349｜cody-hutson / pmo-platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T18:18:56.127)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.0 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T18:18:56.127 / 2026-11-20T20:17:47.960
- **官方描述（原文）**：pmo-platform is a modular PMO and release-management platform for Claude Code. From 3.48 until 3.69.1, release/skills/pmo-skill-refiner/eval-viewer/generate_review.py reads untrusted model or skill output from workspace/run*/outputs/ and embeds it with json.dumps into viewer.html inside an inline script without escaping HTML metacharacters. A crafted output can close the script element and execute JavaScript when an operator generates and opens the viewer. The maintainer also confirmed that DOM-based injection through renderGrades and renderBenchmark innerHTML survives transport-only escaping, so affected render sinks must neutralize the content. Executed script can read embedded prompts and outputs, alter the viewer DOM, or modify saved feedback. This issue is fixed in version 3.69.1.

### 131. CVE-2026-77327｜MapServer / MapServer
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T19:18:54.270)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T19:18:54.270 / 2026-11-20T20:17:44.160
- **官方描述（原文）**：MapServer is a system for developing web-based GIS applications. Prior to 8.6.5, MapServer's MySQL JOIN implementation in src/mapjoin.c copies the source layer attribute selected by JOIN ... FROM into joininfo->target and inserts it into the query built by msMySQLJoinNext() without parameterization or SQL escaping. When MySQL JOIN support is enabled, an attacker who can control that source feature attribute, including through imported shapefile or DBF data or another untrusted spatial source, can inject SQL operators or expressions that change the intended JOIN predicate. This can bypass the intended key comparison and expose unrelated records from the MySQL or MariaDB JOIN table through output templates, query responses, or downstream application logic. This issue is fixed in version 8.6.5.

### 132. CVE-2026-77314｜flytohub / flyto-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:18:44.330)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.3 (MEDIUM)
- **EPSS**：0.00324 / percentile=0.26099
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:18:44.330 / 2026-11-20T21:17:39.053
- **官方描述（原文）**：Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, the MCP run_recipe tool in src/core/mcp_handler.py accepts a caller-controlled recipe_name that load_recipe() in src/cli/recipe.py appends to the src/recipes path without resolved-path containment. Parent-directory segments can therefore make Flyto load and execute a YAML workflow outside the bundled recipe directory, bypassing the boundary represented by list_recipes(). This does not necessarily provide unrestricted code execution because available workflow modules remain subject to Flyto's module policy, but it permits unintended execution of allowed browser, network, file, and data-processing modules. This issue is fixed in version 2.26.8.

### 133. CVE-2026-69133｜netty / netty-incubator-codec-ohttp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:18:08.440)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00304 / percentile=0.23817
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:18:08.440 / 2026-11-20T17:18:26.447
- **官方描述（原文）**：netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. From 0.0.20.Final until 0.0.27.Final, OHttpClientCodec in codec-ohttp/src/main/java/io/netty/incubator/codec/ohttp/OHttpClientCodec.java and OHttpServerCodec in codec-ohttp/src/main/java/io/netty/incubator/codec/ohttp/OHttpServerCodec.java retain the consumed outer cumulationBuffer after a valid OHTTP exchange completes, even though OHttpRequestResponseContext.destroy in codec-ohttp/src/main/java/io/netty/incubator/codec/ohttp/OHttpRequestResponseContext.java releases the inner Binary HTTP cumulation and the channel remains active. A peer can complete a large request or response and leave the keep-alive connection idle, causing the client and server handlers to retain the current high-water pooled or direct buffer capacity until later inbound content replaces it or the handler is removed. Many long-lived idle connections can pin substantial memory and create availability pressure. The issue does not cause unbounded growth for repeated exchanges on a single channel. This issue is fixed in version 0.0.27.Final.

### 134. CVE-2026-61799｜netty / netty-incubator-codec-ohttp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:18:06.667)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:18:06.667 / 2026-11-20T17:18:26.313
- **官方描述（原文）**：netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.0.23.Final, BinaryHttpParser in codec-bhttp/src/main/java/io/netty/incubator/codec/bhttp/BinaryHttpParser.java accumulates attacker-controlled Binary HTTP variable-length integers into the int offset sumBytes. BinaryHttpParser.readRequestHead, BinaryHttpParser.readFieldLine, and BinaryHttpParser.getIndeterminateLength can narrow long lengths into that offset, causing integer wraparound before buffer indices are calculated. A remote peer that supplies a valid large encoded length to BinaryHttpParser or BinaryHttpDecoder can trigger an unchecked bounds exception from a small malformed message, fail or close the channel, and repeatedly cause denial of service. Java and Netty bounds checks prevent memory corruption, and no information disclosure was observed. This issue is fixed in version 0.0.23.Final.

### 135. CVE-2026-59968｜Kovah / LinkAce
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T18:18:54.480)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T18:18:54.480 / 2026-11-20T19:18:52.783
- **官方描述（原文）**：LinkAce is a self-hosted archive to collect website links. Prior to 2.5.9, the authenticated GET /api/v2/lists/{list}/links endpoint in app/Http/Controllers/API/ListLinksController.php authorizes access only to the parent list and then returns its links without applying visibleForUser(). Because another user's INTERNAL or PUBLIC list may legitimately contain PRIVATE links, a normal authenticated user who may view the list can also receive those private link records, including their URLs, titles, descriptions, icons, and timestamps. Equivalent web, tag, notes, and feed handlers apply the per-link visibility scope, so this API handler is the affected exception. This issue is fixed in version 2.5.9.

### 136. CVE-2026-54046｜LibreChat-AI / LibreChat
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T20:17:43.173)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T20:17:43.173 / 2026-11-20T21:17:38.723
- **官方描述（原文）**：LibreChat is an enhanced ChatGPT clone that supports multiple AI providers. Prior to 0.8.7, unauthenticated POST /api/user/verify requests in api/server/routes/user.js call api/server/services/AuthService.js verifyEmail and return distinct responses for unknown, verified, and unverified email addresses and the route lacks request throttling. A remote attacker can submit candidate addresses with invalid tokens to enumerate registered accounts and verification state, supporting targeted phishing or credential attacks. This issue is fixed in version 0.8.7.

### 137. CVE-2026-133706｜azu / request-filtering-agent
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T13:18:46.707)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T13:18:46.707 / 2026-11-20T14:17:52.790
- **官方描述（原文）**：request-filtering-agent before 3.2.2 contains a server-side request forgery filter bypass because address validation in src/request-filtering-agent.ts treats IPv4-compatible IPv6 addresses in the ::/96 range as public unicast. Attackers controlling a fetched URL can use addresses like ::7f00:1 or ::a9fe:a9fe to reach loopback or link-local services, including cloud metadata endpoints.

### 138. CVE-2026-133704｜penpot / penpot
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T13:18:46.380)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T13:18:46.380 / 2026-11-20T21:17:35.833
- **官方描述（原文）**：Penpot 2.18.0 before 2.18.2 contains a stored cross-site scripting vulnerability that allows authenticated users with edit rights to bypass the sanitize-svg-element blocklist using namespace-prefixed SVG elements. Attackers can upload SVGs containing elements like x:script or attributes like x:onload, which are served inline as image/svg+xml to run JavaScript in victims' Penpot sessions.

### 139. CVE-2026-133703｜open5gs / open5gs
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T13:18:46.213)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T13:18:46.213 / 2026-11-20T15:17:50.857
- **官方描述（原文）**：Open5GS AMF through 2.8.0 contains a resource leak vulnerability that allows authenticated UEs to exhaust the session pool by triggering failed DNN or S-NSSAI validation. Attackers can repeat PDU Session Establishment Requests with different PDU Session Identity values, leaving stale amf_sess contexts that degrade service for other subscribers.

### 140. CVE-2026-133502｜blinkospace / blinko
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T09:20:07.503)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00719 / percentile=0.54793
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T09:20:07.503 / 2026-11-20T18:18:49.863
- **官方描述（原文）**：A weakness has been identified in blinkospace blinko up to 1.8.8. Affected is an unknown function of the file /api/auth/verify-2fa of the component 2FA Endpoint. This manipulation of the argument userId causes improper authentication. The attack may be initiated remotely. The exploit has been made available to the public and could be used for attacks. Upgrading to version 1.8.9 is able to address this issue. Patch name: 80e1c4ffaffe66a97df2b5d85fad864ff3691dc8. Upgrading the affected component is advised.

### 141. CVE-2026-133492｜TRENDnet / TEW-657BRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T07:17:05.930)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00414 / percentile=0.36643
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T07:17:05.930 / 2026-11-20T14:17:51.460
- **官方描述（原文）**：A vulnerability has been found in TRENDnet TEW-657BRM 1.00.1. The impacted element is an unknown function of the file /usr/www/images/.svn/entries of the component mini_httpd. The manipulation leads to information disclosure. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The vendor explains: "I am not able to confirm if such vulnerability exists as the product has been EOL for more than 15 years. We will send out an announcement letting customers know." This vulnerability only affects products that are no longer supported by the maintainer.

### 142. CVE-2026-133478｜rajesh2211 / Doctor-Appointment-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T03:17:34.977)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00259 / percentile=0.17968
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T03:17:34.977 / 2026-11-20T18:18:48.727
- **官方描述（原文）**：A security vulnerability has been detected in rajesh2211 Doctor-Appointment-System up to ee974dcf4c50da85e6ea026e27f4370e9468b3cc. Affected is an unknown function of the file AppointmentSystem/AppointmentSystem/Connectivity.php of the component Login. The manipulation of the argument User leads to sql injection. It is possible to initiate the attack remotely. The exploit has been disclosed publicly and may be used. This product is using a rolling release to provide continious delivery. Therefore, no version details for affected nor updated releases are available.

### 143. CVE-2026-133237｜manyfold3d / manyfold
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T16:21:26.660)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.00424 / percentile=0.3759
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T16:21:26.660 / 2026-11-19T19:17:28.903
- **官方描述（原文）**：Manyfold 0.124.0 before 0.154.2 contains a server-side request forgery vulnerability that allows unauthenticated remote attackers to make the instance fetch internal URLs by supplying malicious ActivityPub actor icon.url and image.url fields. Attackers can deliver Create or Update activities to the inbox, causing the Shrine remote_url plugin to request internal or cloud metadata hosts and store responses as creator avatar or banner attachments.

### 144. CVE-2026-133217｜OSGeo / shapelib
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T22:18:03.733)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 4.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T22:18:03.733 / 2026-11-20T17:18:17.950
- **官方描述（原文）**：A weakness has been identified in OSGeo shapelib up to 1.6.3. This vulnerability affects the function DBFCloneEmpty of the file dbfopen.c. This manipulation causes null pointer dereference. It is possible to launch the attack on the local host. Patch name: f79050a900d2a05529501b2b714b8f89067db071. It is recommended to apply a patch to fix this issue.

### 145. CVE-2026-133169｜modified-shop / modified-shop
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:36.800)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 4.8 (MEDIUM)
- **EPSS**：0.00342 / percentile=0.28466
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:36.800 / 2026-11-19T19:17:27.997
- **官方描述（原文）**：modified eCommerce Shopsoftware through 3.3.0 contains a stored cross-site scripting vulnerability that allows authenticated administrators to inject scripts via the unsanitized products_model field. Attackers with product editing permission can store JavaScript that executes in browsers of other administrators, storefront visitors, and customers viewing carts and order history.

### 146. CVE-2026-132276｜facelessuser / wcmatch
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T17:18:12.723)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T17:18:12.723 / 2026-11-20T20:17:34.707
- **官方描述（原文）**：wcmatch is a Python library for wildcard file-name matching. Prior to 11.2, under the default flags, matching a non-matching attacker-controlled name against an application-supplied pattern containing several star wildcards separated by literals makes the lazy .? and [^/]? segments, including _STAR and _PATH_STAR emitted by _handle_star() in wcmatch/_wcparse.py, backtrack across possible splits, so a single comparison can consume prolonged CPU time. The pattern remains a developer-controlled constant and only the name is attacker-controlled; affected paths include fnmatch.fnmatch(), glob.globmatch(), and filesystem glob scans where another user can create names, without enabling extglob or any non-default flag. This issue is fixed in 11.2.

### 147. CVE-2026-132043｜Eclipse Foundation / Eclipse Yasson
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T09:17:43.620)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：0.00222 / percentile=0.1307
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T09:17:43.620 / 2026-11-19T16:20:10.337
- **官方描述（原文）**：In Eclipse Yasson versions 3.0 to 3.0.5, a race condition (CWE-362) exists in the handling of @JsonbNumberFormat. Yasson creates one java.text.NumberFormat instance per annotated property and shares it across all threads that use the same Jsonb instance. NumberFormat is not thread-safe, and the deserializer called parse() on it without synchronization. When multiple threads deserialize concurrently, a thread can receive a numeric value that belongs to another thread's input, receive an incorrect value, or fail with an exception. A remote attacker who can send concurrent requests to an application that deserializes untrusted JSON this way may cause incorrect data to be processed or cause another user's value to be returned. Exploitation requires that the application use @JsonbNumberFormat with a shared Jsonb instance and that the attacker win a timing race. This issue is fixed in version 3.0.6 by synchronizing access to the shared NumberFormat instances.

### 148. CVE-2026-130161｜alexbates / Tamari
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T20:17:28.320)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00468 / percentile=0.41378
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T20:17:28.320 / 2026-11-19T22:18:00.927
- **官方描述（原文）**：Tamari is a fully-featured recipe manager web application built using Python and the Flask Framework. Prior to 1.7.2, an authenticated user can bypass the recipe-autofill SSRF check by submitting a hostname under the user's control through the Autofill from URL feature; the hostname can resolve to a public address during validation and a private or internal address during the later connection. In app/myrecipes/routes.py, is_safe_autofill_url validates the first DNS response, but recipe autofill passes the original URL to requests.get, which independently resolves the hostname and can connect to the internal address. The fetched response is parsed into recipe fields, enabling internal-service reconnaissance and potential data exposure; no redirect is required, and disabling redirects does not stop this DNS-rebinding bypass. This issue is fixed in 1.7.2.

### 149. CVE-2026-129232｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T17:17:56.083)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00469 / percentile=0.41452
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T17:17:56.083 / 2026-11-20T22:17:49.433
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. Prior to 3.10.4, XMLCorpusView.read_block rebuilds the full root-to-node context path with "/".join(context) for every start tag while searching for a matching element. Deeply nested attacker-influenced corpus XML therefore causes quadratic pure-Python work and can pin a processing worker, resulting in denial of service. This issue is fixed in version 3.10.4.

### 150. CVE-2026-129231｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T18:18:08.253)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00396 / percentile=0.3473
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T18:18:08.253 / 2026-11-20T22:17:49.300
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. Prior to 3.10.4, SeekableUnicodeStreamReader.readline appends each new block to a growing character buffer and reruns splitlines over the entire buffer on every iteration. An attacker-controlled corpus file containing one very long unterminated line therefore causes quadratic CPU consumption in line-oriented corpus readers and can deny service. This issue is fixed in version 3.10.4.

### 151. CVE-2026-129230｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T18:18:08.100)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00237 / percentile=0.15055
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T18:18:08.100 / 2026-11-19T19:17:22.020
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. Prior to 3.10.4, WordNet Synset.max_depth, min_depth, hypernym_paths, and hypernym_distances recursively follow attacker-controlled corpus pointers without a visited-node set or depth cap. A cyclic or excessively deep hypernym graph can raise RecursionError and terminate traversal APIs and similarity operations that depend on them. This issue is fixed in version 3.10.4.

### 152. CVE-2026-129228｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T19:17:21.840)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00469 / percentile=0.41452
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T19:17:21.840 / 2026-11-19T20:17:23.770
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. Prior to 3.10.4, ToolboxSettings.parse builds a deeply nested attacker-controlled settings tree iteratively, but the later public helpers to_settings_string, remove_blanks, add_default_fields, sort_fields, and add_blank_lines recursively traverse that tree without a depth bound. Invoking any of those helpers on input nested beyond the interpreter recursion limit can raise RecursionError and abort the operation or request worker. This issue is fixed in version 3.10.4.

### 153. CVE-2026-129225｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T18:18:07.470)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00479 / percentile=0.42285
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T18:18:07.470 / 2026-11-19T19:17:21.627
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. In 3.10.3 and earlier, DependencyGraph._tree and triples recurse once per dependency edge without a depth bound, and get_cycle_path also lacks a visited-set termination guard. A deeply chained or cyclic attacker-controlled CoNLL or Malt-TAB dependency structure can raise RecursionError and abort a parse worker. This issue is fixed in version 3.10.4.

### 154. CVE-2026-129224｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T19:17:21.473)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00536 / percentile=0.46094
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T19:17:21.473 / 2026-11-19T20:17:23.643
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. Prior to 3.10.4, the CCG lexicon parser's matchBrackets and augParseCategory functions recursively process nested parenthesized categories without a depth bound. An attacker-controlled lexicon string with excessive nesting can raise RecursionError through nltk.ccg.lexicon.fromstring and terminate the parse operation or request worker. This issue is fixed in version 3.10.4.

### 155. CVE-2026-129221｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T18:18:06.953)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：0.00439 / percentile=0.39059
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T18:18:06.953 / 2026-11-19T19:17:21.367
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. Prior to 3.10.4, nltk.classify.weka.ARFF_Formatter writes attacker-controlled class labels into the Weka ARFF @ATTRIBUTE '-label-' declaration without safely formatting the label tokens. Crafted labels can alter the generated ARFF schema or records, corrupting classifier input and causing integrity loss or processing failure. This issue is fixed in version 3.10.4.

### 156. CVE-2026-129174｜U.S. Department of the Interior / Unstable Slope Management Program
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T20:17:21.377)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T20:17:21.377 / 2026-11-20T20:17:21.377
- **官方描述（原文）**：U.S Department of the Interior Unstable Slope Management Program allows a remote, unauthenticated attacker to access a vulnerable endpoint that returns a list of application users and their permissions in plaintext. Fixed on or around 2026-10-19.

### 157. CVE-2026-128140｜nltk / nltk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T18:18:06.453)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：0.00356 / percentile=0.30067
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T18:18:06.453 / 2026-11-19T19:17:21.153
- **官方描述（原文）**：NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. From 3.6.7 until 3.10.4, nltk.downloader follows collection membership without tracking already visited collection nodes. A self-referencing or mutually referencing collection index can therefore make the package-closure walk loop indefinitely while its queue and memory usage grow, denying service when a victim processes the attacker-influenced index. This issue is fixed in version 3.10.4.

### 158. CVE-2026-115565｜webflorist / storyblok-backup
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T19:17:18.167)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.7 (MEDIUM)
- **EPSS**：0.00359 / percentile=0.30464
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T19:17:18.167 / 2026-11-19T20:17:19.683
- **官方描述（原文）**：storyblok-backup is an npx CLI tool to create backups of a Storyblok space and restore individual resources. Prior to 0.7.1, the writeJson function used the editable Storyblok component name field as a filename without path containment. A person with component-management access in a Storyblok space could store a component name containing path traversal sequences; when another user later ran a backup for that space, the stored name escaped the configured backup directory and caused a JSON file to be written outside it on the backup host. Depending on the path chosen and the backup process's permissions, this could overwrite existing files at attacker-chosen locations. The vulnerability is specific to components: stories and datasources use numeric identifiers, and asset names are reduced to a final path segment. This issue is fixed in version 0.7.1.

### 159. CVE-2026-115409｜Eclipse Foundation / Eclipse KeyPont
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T10:17:07.660)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T10:17:07.660 / 2026-11-20T19:18:36.160
- **官方描述（原文）**：In `github.com/eclipse-keypont/crypto11/v2` versions `<= 2.0.0-rc8` (and the deprecated v1 module paths `github.com/eclipse-keypont/crypto11 <= 1.6.8`, `github.com/ThalesGroup/crypto11 <= 1.7.0-rc1` and `github.com/ThalesIgnite/crypto11 <= 1.2.5`), the key-pair and certificate lookup functions (`FindKeyPair`, `FindKeyPairs`, `FindKeyPairsWithAttributes`, `FindAllKeyPairs`, the `FindRSAKeyPair*` family and `FindAllPairedCertificates`) pair a private key with a public key object, or with a certificate, by `CKA_ID`/`CKA_LABEL` alone, take the first match the token returns, and never verify that it belongs to the private key. PKCS#11 permits a session that has not logged in to create public token objects, so anyone able to open a session on the token — without the PIN — can plant a public key or certificate carrying a victim key's `CKA_ID` and label, and crypto11 may return it as that key's public half. An application that publishes or trusts `Signer.Public()` (a JWKS endpoint, a key registry, `authorized_keys`, a CSR) then publishes the attacker's key, and relying parties accept anything the attacker signs as coming from the service. On the v1 line the lookup also falls back to a class-and-key-type-only search when the private key has no `CKA_ID`, pairing a label-only private key with the first public key of its type on the token. The v1 module paths are deprecated and will not be fixed; users should migrate to github.com/eclipse-keypont/crypto11/v2 version 2.0.0-rc9 or later.

### 160. CVE-2026-110780｜Netatalk / netatalk
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T18:18:35.720)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T18:18:35.720 / 2026-11-20T19:18:35.003
- **官方描述（原文）**：Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 3.1.0 until 4.5.2, the Spotlight RPC consumer handlers sl_rpc_fetchAttributeNamesForOIDArray, sl_rpc_storeAttributesForOIDArray, and sl_rpc_fetchAttributesForOIDArray in etc/afpd/spotlight.c dereference the first element of a decoded sl_cnids_t without checking whether the inner CNID array is empty. An authenticated AFP client, or a guest when guest AFP access is enabled, can send a crafted SPOTLIGHT_CMD_RPC whose outer CNIDS length is greater than 16 while its inner count is zero, causing sl_unpack_cnids to create an empty DALLOC_CTX and the consumer to dereference dd_talloc_array[0]. The affected afpd child crashes, normally limiting denial of service to the attacker's session, and no memory write or code execution was demonstrated. This issue is fixed in version 4.5.2.

### 161. CVE-2026-104185｜Kovah / LinkAce
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T18:18:35.130)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T18:18:35.130 / 2026-11-20T20:17:07.253
- **官方描述（原文）**：LinkAce is a self-hosted archive to collect website links. Prior to 2.6.0, the HTML bookmark import action in app/Actions/ImportHtmlBookmarks.php uses the global Link::whereUrl() lookup instead of restricting duplicate detection to the importing user. An authenticated user can submit a chosen URL and distinguish the skipped response count from the queued count to learn whether any account has saved that URL, including as a PRIVATE bookmark. The oracle reveals URL existence but does not directly return the bookmark contents or owner. This issue is fixed in version 2.6.0.

### 162. CVE-2026-103033｜altcha-org / altcha-lib-go
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T21:17:40.930)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00332 / percentile=0.27042
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T21:17:40.930 / 2026-11-20T17:17:58.297
- **官方描述（原文）**：ALTCHA is a Go library for creating and verifying ALTCHA challenges. Prior to 2.1.0, parseServerSignature can leave ServerSignatureVerificationData.Extra uninitialized when url.ParseQuery returns partial values and an error for a malformed percent escape in VerificationData. A later write of an unknown parsed key to the nil map panics before VerifyServerSignature or VerifyServerSignatureSafe completes signature verification, so an unauthenticated client can abort a request. Standard net/http recovers the request goroutine, while application goroutines or frameworks without recovery can crash the process. This issue is fixed in version 2.1.0.

### 163. CVE-2025-71474｜gkostka / lwext4
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T01:17:08.690)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.00121 / percentile=0.01987
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T01:17:08.690 / 2026-11-20T14:17:42.473
- **官方描述（原文）**：lwext4 through 1.0.0 contains an out-of-bounds write vulnerability in ext4_fs_init_block_bitmap() that allows attackers to corrupt heap memory via crafted superblock geometry fields. Attackers can supply an ext4 image with oversized s_reserved_gdt_blocks and BLOCK_UNINIT groups to write past the bitmap buffer, crashing applications that mount it.

### 164. CVE-2026-92613｜Eclipse Foundation / Eclipse iceoryx™
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T10:17:29.493)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.0 (LOW)
- **EPSS**：0.00201 / percentile=0.10151
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T10:17:29.493 / 2026-11-19T16:22:07.143
- **官方描述（原文）**：In Eclipse iceoryx-rs, versions 0.0.11 to 0.0.13 and 0.1.0 as well as on the latest main branch. `SampleReceiver::<T>::take()` and `Sample::<T>::deref()` are safe functions that hand the caller a `&T` pointing at a chunk written by another iceoryx process, but the subscriber path neither requires `T: ShmSend` nor verifies that the received chunk is at least `size_of::<T>()` bytes / `align_of::<T>()`-aligned. A peer process that publishes an undersized chunk, or any chunk at all when the subscriber chose a pointer-bearing `T`, drives a `#![forbid(unsafe_code)]` subscriber into out-of-bounds reads of adjacent shared-memory chunks or dereference of a publisher-controlled pointer. Resolution: It will not be fixed since this is a known limitation in iceoryx as it is the users responsibility to specify the same data type on sender and receiver side. [iceoryx2](https://github.com/eclipse-iceoryx/iceoryx2) is the successor of iceoryx-rs where the API is designed to prevent this by default. It is strongly recommended to migrate to iceoryx2 which is actively maintained and receives security support. The iceoryx-rs package has officially reached End-of-life and will not receive any features, bugfixes or security fixes.

### 165. CVE-2026-54041｜LibreChat-AI / LibreChat
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T20:17:42.260)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T20:17:42.260 / 2026-11-20T21:17:38.290
- **官方描述（原文）**：LibreChat is an enhanced ChatGPT clone that supports multiple AI providers. Prior to 0.8.6, the POST /api/auth/login local-login validation path in api/strategies/localStrategy.js logs req.body, including the submitted plaintext password, during a Zod validation failure. The standard browser form validation makes this path less likely through the normal interface, but a direct invalid login request can reach it, and the logging formatter does not redact the password stored in metadata. A principal with access to application stdout, error logs, or journal output can recover the submitted credential. This issue is fixed in version 0.8.6.

### 166. CVE-2026-133701｜free5gc / smf
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T13:18:45.910)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T13:18:45.910 / 2026-11-20T14:17:52.660
- **官方描述（原文）**：free5GC SMF through 1.4.6 contains a resource exhaustion vulnerability in HandlePDUSessionSMContextLocalRelease that orphans SM contexts and UE IP addresses when PFCP session deletion fails. Attackers can send repeated PDU session establishment requests reusing an existing SUPI and PDU Session ID during PFCP deletion failures to exhaust the DNN's UE IP pool.

### 167. CVE-2026-133699｜free5gc / smf
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T13:18:45.607)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T13:18:45.607 / 2026-11-20T15:17:50.723
- **官方描述（原文）**：free5GC SMF through 1.4.6 contains a resource exhaustion vulnerability because sendPDUSessionEstablishmentAccept returns early without calling RemoveSMContextFromAllNF on failures. Authenticated UEs repeatedly establishing PDU sessions during NRF or AMF failures leak SM contexts, UE IP addresses and TEIDs, exhausting the DNN IP pool.

### 168. CVE-2026-133629｜Sunnet / CTMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T15:17:50.453)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T15:17:50.453 / 2026-11-20T18:18:51.280
- **官方描述（原文）**：A vulnerability was determined in Sunnet CTMS up to 10.11. Impacted is an unknown function of the file /cltcms/api/external-training/ext-course of the component External Training Application Form Feature. This manipulation of the argument memberids causes improper control of resource identifiers. Remote exploitation of the attack is possible. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 169. CVE-2026-133612｜SqueezeAILab / SqueezeLLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T15:17:49.593)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T15:17:49.593 / 2026-11-20T17:18:19.487
- **官方描述（原文）**：A weakness has been identified in SqueezeAILab SqueezeLLM up to a5fd71f353bf569feb7b55737c1c1493e78e8f31. This vulnerability affects the function vecquant4matmul_spmv_hybrid_nuq_perchannel of the file quant_cuda_kernel.cu of the component CUDA Matvec Kernel. Executing a manipulation of the argument full_row_indices can lead to out-of-bounds write. The attack can be launched remotely. The exploit has been made available to the public and could be used for attacks. This product does not use versioning. This is why information about affected and unaffected releases are unavailable. The project was informed of the problem early through an issue report but has not responded yet.

### 170. CVE-2026-133503｜ModelCloud / GPTQModel
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T09:20:07.717)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T09:20:07.717 / 2026-11-20T14:17:51.760
- **官方描述（原文）**：A security vulnerability has been detected in ModelCloud GPTQModel up to 7.6.0. Affected by this vulnerability is the function gptqmodel.adapter.remote.resolve_path of the file gptqmodel/adapter/remote.py of the component Adapter Resolution Pipeline. Such manipulation of the argument adapter.path leads to improper input validation. The attack may be launched remotely. The exploit has been disclosed publicly and may be used. Upgrading to version 7.7.0 addresses this issue. The name of the patch is ed99ac8d59940bf27bb24ce2e80002ae9e44469f. It is advisable to upgrade the affected component.

### 171. CVE-2026-133499｜Vahe1994 / AQLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T08:18:33.450)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：0.00348 / percentile=0.2911
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T08:18:33.450 / 2026-11-20T17:18:19.037
- **官方描述（原文）**：A vulnerability was found in Vahe1994 AQLM up to e79a896ed6656fe4ed06193d42d004e7d0bbdbb2. The affected element is an unknown function of the file inference_kernels/triton_kernel.py of the component Triton Kernel. Performing a manipulation of the argument codes results in out-of-bounds read. It is possible to initiate the attack remotely. The exploit has been made public and could be used. This product is using a rolling release to provide continious delivery. Therefore, no version details for affected nor updated releases are available. The project was informed of the problem early through an issue report but has not responded yet.

### 172. CVE-2026-133497｜itsourcecode / Banking Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T08:18:33.070)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00492 / percentile=0.4322
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T08:18:33.070 / 2026-11-20T14:17:51.617
- **官方描述（原文）**：A vulnerability was detected in itsourcecode Banking Management System 1.0. This vulnerability affects unknown code of the file navbar.php. The manipulation of the argument page results in cross site scripting. The attack can be executed remotely. The exploit is now public and may be used.

### 173. CVE-2026-133490｜declare-lab / tango
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T06:17:21.600)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00331 / percentile=0.26965
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T06:17:21.600 / 2026-11-20T17:18:18.737
- **官方描述（原文）**：A vulnerability was detected in declare-lab tango up to 34ecd38898508017ca937508a047b42817d2b070. Impacted is the function Tango.__init__ of the file tango.py of the component Model Loading. Performing a manipulation of the argument scheduler_name results in improper input validation. The attack is possible to be carried out remotely. The exploit is now public and may be used. This product adopts a rolling release strategy to maintain continuous delivery. Therefore, version details for affected or updated releases cannot be specified. The project was informed of the problem early through an issue report but has not responded yet.

### 174. CVE-2026-133489｜XiangLi1999 / Diffusion-LM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T06:17:21.407)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00457 / percentile=0.40532
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T06:17:21.407 / 2026-11-20T18:18:49.053
- **官方描述（原文）**：A security vulnerability has been detected in XiangLi1999 Diffusion-LM up to 759889d58ef38e2eed41a8c34db8032e072826f4. This issue affects the function main of the file improved-diffusion/scripts/text_sample.py. Such manipulation of the argument out_dir leads to path traversal. The attack can be executed remotely. The exploit has been disclosed publicly and may be used. This product implements a rolling release for ongoing delivery, which means version information for affected or updated releases is unavailable. The project was informed of the problem early through an issue report but has not responded yet.

### 175. CVE-2026-133488｜XiangLi1999 / Diffusion-LM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T06:17:21.167)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.01114 / percentile=0.66831
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T06:17:21.167 / 2026-11-20T14:17:51.313
- **官方描述（原文）**：A weakness has been identified in XiangLi1999 Diffusion-LM up to 759889d58ef38e2eed41a8c34db8032e072826f4. This vulnerability affects the function os.system of the file improved-diffusion/scripts/infill.py. This manipulation of the argument notes causes os command injection. Remote exploitation of the attack is possible. The exploit has been made available to the public and could be used for attacks. This product follows a rolling release approach for continuous delivery, so version details for affected or updated releases are not provided. The project was informed of the problem early through an issue report but has not responded yet.

### 176. CVE-2026-133486｜hasan-py / Hayroo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T05:18:54.053)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00295 / percentile=0.22666
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T05:18:54.053 / 2026-11-20T17:18:18.570
- **官方描述（原文）**：A vulnerability was identified in hasan-py Hayroo up to fd0fbe763153f72bfaa04ed1e1e4a1bb6f7c61df. Affected by this issue is the function Product.deleteImages of the file server/controller/products.js of the component Image Deletion Handler. The manipulation leads to path traversal. The attack may be initiated remotely. The exploit is publicly available and might be used. This product uses a rolling release model to deliver continuous updates. As a result, specific version information for affected or updated releases is not available. The identifier of the patch is 9714947bb43ec8559287aa3962b70a7be8c8d6b1. It is recommended to apply a patch to fix this issue.

### 177. CVE-2026-133484｜ByteDance / Lark Desktop
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T05:18:53.680)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：0.00145 / percentile=0.03863
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T05:18:53.680 / 2026-11-20T18:18:48.893
- **官方描述（原文）**：A vulnerability was found in ByteDance Lark Desktop 8.0.0.14. This vulnerability affects the function FUN_18001b770/FUN_18001ba40 in the library backend.dll. Performing a manipulation of the argument day results in signed to unsigned conversion error. The attack needs to be approached locally. The exploit has been made public and could be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 178. CVE-2026-133482｜hrshadhin / CloudSchool
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T04:17:09.733)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：0.00202 / percentile=0.10313
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T04:17:09.733 / 2026-11-20T15:17:48.987
- **官方描述（原文）**：A vulnerability has been found in hrshadhin CloudSchool up to 3.0.1. This affects the function EventController@store of the file app/Http/Controllers/Backend/EventController.php of the component Admin Content Management. Such manipulation of the argument data leads to cross site scripting. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 179. CVE-2026-133479｜WebKul / QloApps
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-20T03:17:35.177)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：0.00388 / percentile=0.33782
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-20T03:17:35.177 / 2026-11-20T17:18:18.410
- **官方描述（原文）**：A vulnerability was detected in WebKul QloApps up to 1.8.0. Affected by this vulnerability is the function postProcessDownload/installTheme of the file controllers/admin/AdminModulesController.php of the component Archive Import. The manipulation results in path traversal. It is possible to launch the attack remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 180. CVE-2026-133233｜quasarframework / quasar
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T16:21:25.870)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：0.00361 / percentile=0.30689
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T16:21:25.870 / 2026-11-19T19:17:28.647
- **官方描述（原文）**：Quasar before 2.35.3 contains a DOM clobbering vulnerability that allows attackers to break native wrapper detection by injecting HTML elements named Capacitor, cordova, or StatusBar. Attackers can place markup such as a div with id Capacitor into server-rendered or pre-rendered HTML so app.use(Quasar) throws and the application never mounts, or openURL() and AddressbarColor.set() throw.

### 181. CVE-2026-129916｜Eclipse Foundation / Eclipse Ditto
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:29.360)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：0.00387 / percentile=0.33644
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:29.360 / 2026-11-19T20:17:25.760
- **官方描述（原文）**：In Eclipse Ditto versions 3.9.0 to 3.9.8, the resolved policy view (`GET /api/2/policies/{policyId}?policy-view=resolved`) does not restrict merged policy content to what the caller may read in the policy it originates from. Imported and namespace-root entries are returned in full as soon as the caller may read any part of them in the source policy, entries of transitive imports and of the imports of namespace-root policies are only checked against the intermediate policy, and content copied into an entry by `references`, also from another entry of the same policy, is not checked against the referenced entry. An authenticated caller with READ on a policy can therefore read subjects, resources and granted/revoked permissions of policy entries that are hidden from them, including by explicit revokes, when reading the originating policy directly.

### 182. CVE-2026-129702｜Eclipse Foundation / Eclipse Ditto
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T15:17:29.203)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：0.00356 / percentile=0.30129
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T15:17:29.203 / 2026-11-19T20:17:25.620
- **官方描述（原文）**：In Eclipse Ditto versions before 3.8.15 and 3.9.0 to 3.9.8, the policy enforcers do not let a revoke win over a grant in two kinds of permission checks. Checks of several permissions at once compare the highest grant weight with the highest revoke weight across all requested permissions instead of per permission, so the "check permissions" API (`POST /api/2/checkPermissions`, available since 3.7.0) can report a set of permissions as granted although one of them is revoked. Partial permission checks, which authorize retrieving Things and Policies and determine the receivers of events, count a grant on a sub-resource although the same permission is revoked on that sub-resource for another subject of the same authorization context (or, with the memory-optimized policy evaluator, for the same subject). A requester can thereby learn about the existence of Things and Policies and receive metadata without any readable content, and an application relying on the check permissions result may grant access the policy denies. The content of retrieved Things and Policies is still filtered correctly, and modifications are not affected.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-76466｜Cisco / Expressway Series
- **Title**：Cisco Expressway Series Use of Hard-coded Credentials Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00417 / percentile=0.36836
- **CISA KEV**：listed=true / date_added=2026-11-20 / due_date=2026-11-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Expressway Series contains a use of hard-coded credentials vulnerability that allows an unauthenticated, remote attacker with persistent cookies and network access to execute commands as root on a clustered device via the database service.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-129448｜Apache / Roller
- **Title**：Apache Roller Deserialization of Untrusted Data Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01191 / percentile=0.68723
- **CISA KEV**：listed=true / date_added=2026-11-20 / due_date=2026-11-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apache Roller contains a deserialization of untrusted data vulnerability that allows an unauthenticated remote attacker to execute arbitrary code via the XML-RPC endpoint, which accepts and deserializes vendor extension types before authentication. This CVE covers the same underlying vulnerability as CVE-2026-82384 but applies to a broader range of affected versions.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-123890｜Broadcom / VMware vCenter
- **Title**：VMWare vCenter Authentication Bypass Using an Alternate Path or Channel Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00843 / percentile=0.58845
- **CISA KEV**：listed=true / date_added=2026-11-20 / due_date=2026-11-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Broadcom VMware vCenter contains an authentication bypass using an alternate path or channel vulnerability in the VMware Directory Service that allows an unauthenticated attacker with network access to vCenter to bypass authentication and gain unauthorized access to the system.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2025-42884｜SAP / NetWeaver
- **Title**：SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：0.00276 / percentile=0.2048
- **CISA KEV**：listed=true / date_added=2026-11-20 / due_date=2026-11-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：SAP NetWeaver Enterprise Portal contains an improper neutralization of special elements in data query logic vulnerability that allows an unauthenticated attacker to disclose or modify server information via injected JNDI environment properties or a URL used during JNDI lookup operations.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-90817｜Vanderbilt University / Research Electronic Data Capture (REDCap)
- **Title**：Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.25657 / percentile=0.98008
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-11-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Vanderbilt University Research Electronic Data Capture (REDCap) contains a code injection vulnerability which could allow an unauthenticated attacker to execute arbitrary code on the server. An attacker could exploit this via crafted HTTP requests that access an unintended controller route from a public survey context and supply a crafted file-path or stream parameter during data import processing. Exploitation requires knowledge of a valid public survey hash.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-40217｜BerriAI / LiteLLM
- **Title**：BerriAI LiteLLM Unprotected Alternate Channel Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.68902 / percentile=0.99365
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-12-02
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：BerriAI LiteLLM contains an unprotected alternate channel vulnerability that could allow remote attackers to execute arbitrary code via bytecode rewriting at the /guardrails/test_custom_code URI.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-115560 | P3 / 53 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.56429 / percentile=0.99079 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-129496 | P3 / 41 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.09976 / percentile=0.95713 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-129474 | P3 / 41 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.0865 / percentile=0.95237 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-129289 | P3 / 41 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.1704 / percentile=0.97149 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-129182 | P3 / 41 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.11007 / percentile=0.96007 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-126714 | P3 / 41 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.17587 / percentile=0.97213 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-94567 | P3 / 38 | nukeviet / nukeviet | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-94565 | P3 / 38 | nukeviet / nukeviet | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77369 | P3 / 38 | daptin / daptin | v3.1 9.6 (CRITICAL) | 0.00397 / percentile=0.34807 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77359 | P3 / 38 | datalayer / jupyter-mcp-server | v4.0 9.3 (CRITICAL) | 0.00503 / percentile=0.43944 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-133872 | P3 / 38 | lesspass / lesspass | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-133493 | P3 / 38 | D-Link / DIR-600L | v4.0 9.3 (CRITICAL) | 0.02514 / percentile=0.85187 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-133189 | P3 / 38 | Red Hat / Red Hat OpenStack Platform 13 (Queens) | v3.1 9.6 (CRITICAL) | 0.01467 / percentile=0.74348 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-130158 | P3 / 38 | lbr38 / repomanager | v3.1 9.0 (CRITICAL) | 0.00322 / percentile=0.25831 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-129175 | P3 / 38 | U.S. Department of the Interior / Unstable Slope Management Program | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-128138 | P3 / 38 | nltk / nltk | v3.1 9.8 (CRITICAL) | 0.00914 / percentile=0.60974 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-120753 | P3 / 38 | Eclipse Foundation / Eclipse Ditto | v4.0 9.1 (CRITICAL) | 0.00782 / percentile=0.56908 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-115407 | P3 / 38 | Eclipse Foundation / 未確認 | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-114516 | P3 / 38 | ether / etherpad | v3.1 9.8 (CRITICAL) | 0.01485 / percentile=0.74647 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-94564 | WATCH / 30 | nukeviet / nukeviet | v3.1 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-86017 | WATCH / 30 | isomorphic-git / isomorphic-git | v3.1 8.0 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77355 | WATCH / 30 | isomorphic-git / isomorphic-git | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77329 | WATCH / 30 | mihai-dinculescu / tapo | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77326 | WATCH / 30 | MapServer / MapServer | v3.1 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：1；缺少 Title：24。
- EPSS 未確認：10；Exploitation status 未確認：0。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-21T07:52:47.622763+00:00`；Delta generated at：`2026-11-21T07:52:47.622763+00:00`。

---

## 可驗證資料來源

- **CVE-2026-76466** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76466) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76466) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-129448** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129448) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129448) · [Vendor / Advisory (lists.apache.org)](https://lists.apache.org/thread/cc0jck13nb9vvcmzxzwotr6n16mx28z9) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-123890** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123890) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-123890) · [Vendor / Advisory (support.broadcom.com)](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-42884** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-42884) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-42884) · [Vendor / Advisory (support.sap.com)](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/bulletin-2025.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-90817** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90817) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90817) · [Vendor / Advisory (projectredcap.org)](https://projectredcap.org/resources/community) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-40217** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-40217) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-40217) · [Vendor / Advisory (github.com)](https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-115560** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115560) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115560)
- **CVE-2026-129496** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129496) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129496)
- **CVE-2026-129474** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129474) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129474)
- **CVE-2026-129289** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129289) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129289)
- **CVE-2026-129182** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129182) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129182)
- **CVE-2026-126714** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126714) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126714)
- **CVE-2026-94567** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94567)
- **CVE-2026-94565** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94565)
- **CVE-2026-77369** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77369) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77369)
- **CVE-2026-77359** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77359) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77359)
- **CVE-2026-133872** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133872)
- **CVE-2026-133493** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133493) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133493)
- **CVE-2026-133189** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133189) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133189)
- **CVE-2026-130158** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130158) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-130158)
- **CVE-2026-129175** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129175)
- **CVE-2026-128138** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128138) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128138)
- **CVE-2026-120753** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120753) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-120753)
- **CVE-2026-115407** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115407)
- **CVE-2026-114516** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114516) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114516)
- **CVE-2026-94564** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94564)
- **CVE-2026-86017** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86017)
- **CVE-2026-77355** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77355)
- **CVE-2026-77329** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77329)
- **CVE-2026-77326** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77326)
- **CVE-2026-77324** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77324)
- **CVE-2026-77318** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77318) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77318)
- **CVE-2026-77313** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77313) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77313)
- **CVE-2026-77309** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77309)
- **CVE-2026-63202** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63202) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63202)
- **CVE-2026-62255** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62255)
- **CVE-2026-61798** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61798)
- **CVE-2026-59988** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59988) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-59988)
- **CVE-2026-55372** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55372)
- **CVE-2026-48118** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48118)
- **CVE-2026-45356** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45356)
- **CVE-2026-45355** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45355)
- **CVE-2026-133707** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133707)
- **CVE-2026-133680** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133680)
- **CVE-2026-133501** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133501) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133501)
- **CVE-2026-133476** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133476) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133476)
- **CVE-2026-133235** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133235) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133235)
- **CVE-2026-133173** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133173) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133173)
- **CVE-2026-133113** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133113) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133113)
- **CVE-2026-132275** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132275)
- **CVE-2026-132039** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132039) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-132039)
- **CVE-2026-130160** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130160) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-130160)
- **CVE-2026-129700** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129700)
- **CVE-2026-129699** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129699)
- **CVE-2026-129229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129229) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129229)
- **CVE-2026-129179** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129179)
- **CVE-2026-129178** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129178)
- **CVE-2026-129177** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129177)
- **CVE-2026-129176** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129176)
- **CVE-2026-128139** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128139) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128139)
- **CVE-2026-122244** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122244)
- **CVE-2026-95517** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95517) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95517)
- **CVE-2026-87977** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87977) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87977)
- **CVE-2026-86130** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86130) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86130)
- **CVE-2026-86094** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86094) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86094)
- **CVE-2026-84322** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84322) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84322)
- **CVE-2026-84236** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84236) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84236)
- **CVE-2026-82339** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82339) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-82339)
- **CVE-2026-80188** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80188)
- **CVE-2026-77367** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77367) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77367)
- **CVE-2026-77338** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77338) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77338)
- **CVE-2026-77312** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77312) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77312)
- **CVE-2026-76536** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76536) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76536)
- **CVE-2026-76535** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76535) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76535)
- **CVE-2026-65094** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65094) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65094)
- **CVE-2026-62318** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62318)
- **CVE-2026-14914** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14914)
- **CVE-2026-14492** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14492)
- **CVE-2026-133968** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133968)
- **CVE-2026-133949** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133949)
- **CVE-2026-133648** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133648)
- **CVE-2026-133528** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133528) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133528)
- **CVE-2026-133325** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133325) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133325)
- **CVE-2026-133323** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133323) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133323)
- **CVE-2026-133310** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133310) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133310)
- **CVE-2026-133303** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133303) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133303)
- **CVE-2026-133212** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133212)
- **CVE-2026-133185** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133185) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133185)
- **CVE-2026-132891** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132891) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-132891)
- **CVE-2026-132660** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132660)
- **CVE-2026-132659** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132659)
- **CVE-2026-132658** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132658)
- **CVE-2026-131287** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131287) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-131287)
- **CVE-2026-131253** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131253) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-131253)
- **CVE-2026-131202** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131202) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-131202)
- **CVE-2026-129938** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129938) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129938)
- **CVE-2026-129932** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129932) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129932)
- **CVE-2026-129713** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129713)
- **CVE-2026-129481** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129481) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129481)
- **CVE-2026-129411** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129411) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129411)
- **CVE-2026-129410** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129410) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129410)
- **CVE-2026-129402** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129402) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129402)
- **CVE-2026-129396** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129396) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129396)
- **CVE-2026-129073** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129073)
- **CVE-2026-129056** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129056) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129056)
- **CVE-2026-129048** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129048) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129048)
- **CVE-2026-129043** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129043)
- **CVE-2026-129039** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129039)
- **CVE-2026-127057** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127057)
- **CVE-2026-127027** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127027)
- **CVE-2026-126088** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126088) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-126088)
- **CVE-2026-126054** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126054)
- **CVE-2026-124772** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124772)
- **CVE-2026-124770** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124770)
- **CVE-2026-123058** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123058) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-123058)
- **CVE-2026-121385** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121385) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-121385)
- **CVE-2026-120681** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120681)
- **CVE-2026-120539** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120539)
- **CVE-2026-118028** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118028) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-118028)
- **CVE-2026-116561** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116561) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116561)
- **CVE-2026-116440** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116440) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116440)
- **CVE-2026-116439** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116439) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116439)
- **CVE-2026-111509** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111509) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111509)
- **CVE-2026-104099** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104099) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-104099)
- **CVE-2026-101340** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101340)
- **CVE-2026-94566** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94566)
- **CVE-2026-77382** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77382) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77382)
- **CVE-2026-77380** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77380) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77380)
- **CVE-2026-77379** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77379) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77379)
- **CVE-2026-77349** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77349)
- **CVE-2026-77327** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77327)
- **CVE-2026-77314** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77314) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77314)
- **CVE-2026-69133** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69133) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-69133)
- **CVE-2026-61799** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61799)
- **CVE-2026-59968** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59968)
- **CVE-2026-54046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54046)
- **CVE-2026-133706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133706)
- **CVE-2026-133704** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133704)
- **CVE-2026-133703** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133703)
- **CVE-2026-133502** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133502) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133502)
- **CVE-2026-133492** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133492) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133492)
- **CVE-2026-133478** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133478) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133478)
- **CVE-2026-133237** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133237) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133237)
- **CVE-2026-133217** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133217)
- **CVE-2026-133169** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133169) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133169)
- **CVE-2026-132276** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132276)
- **CVE-2026-132043** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132043) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-132043)
- **CVE-2026-130161** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130161) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-130161)
- **CVE-2026-129232** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129232) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129232)
- **CVE-2026-129231** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129231) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129231)
- **CVE-2026-129230** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129230) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129230)
- **CVE-2026-129228** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129228) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129228)
- **CVE-2026-129225** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129225) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129225)
- **CVE-2026-129224** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129224) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129224)
- **CVE-2026-129221** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129221) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129221)
- **CVE-2026-129174** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129174)
- **CVE-2026-128140** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128140) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-128140)
- **CVE-2026-115565** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115565) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115565)
- **CVE-2026-115409** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115409)
- **CVE-2026-110780** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110780)
- **CVE-2026-104185** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104185)
- **CVE-2026-103033** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103033) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-103033)
- **CVE-2025-71474** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-71474) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-71474)
- **CVE-2026-92613** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92613) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-92613)
- **CVE-2026-54041** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54041)
- **CVE-2026-133701** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133701)
- **CVE-2026-133699** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133699)
- **CVE-2026-133629** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133629)
- **CVE-2026-133612** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133612)
- **CVE-2026-133503** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133503)
- **CVE-2026-133499** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133499) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133499)
- **CVE-2026-133497** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133497) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133497)
- **CVE-2026-133490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133490) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133490)
- **CVE-2026-133489** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133489) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133489)
- **CVE-2026-133488** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133488) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133488)
- **CVE-2026-133486** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133486) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133486)
- **CVE-2026-133484** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133484) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133484)
- **CVE-2026-133482** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133482) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133482)
- **CVE-2026-133479** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133479) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133479)
- **CVE-2026-133233** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133233) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-133233)
- **CVE-2026-129916** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129916) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129916)
- **CVE-2026-129702** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129702) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-129702)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
