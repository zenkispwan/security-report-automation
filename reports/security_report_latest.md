# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**131** 筆符合目前門檻的重要變化；事件統計：EPSS_INCREASED=1、NEW_CVE=126、NEW_KEV=4。
- Intelligence 候選：**30** 筆；P1 **5**、P2 **0**、P3 **14**、WATCH **11**。
- Baseline：state / generated_at=2026-11-18T08:05:07.825955+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-90817、CVE-2026-90436、CVE-2026-40217、CVE-2024-10441、CVE-2026-116779。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **131** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-90817｜Vanderbilt University / Research Electronic Data Capture (REDCap)
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.03749 / percentile=0.90092
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-11-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-20T13:17:44.973 / 2026-11-19T05:18:41.563
- **官方描述（原文）**：Vanderbilt University Research Electronic Data Capture (REDCap) contains a code injection vulnerability which could allow an unauthenticated attacker to execute arbitrary code on the server. An attacker could exploit this via crafted HTTP requests that access an unintended controller route from a public survey context and supply a crafted file-path or stream parameter during data import processing. Exploitation requires knowledge of a valid public survey hash.

### 2. CVE-2026-90436｜Apache / Axis
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01128 / percentile=0.67007
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-11-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-06T16:18:59.763 / 2026-11-19T05:18:41.280
- **官方描述（原文）**：Apache Axis contains an unsafe reflection vulnerability that could allow an unauthenticated remote attacker to execute arbitrary code via a crafted SOAP fault message that causes Axis to load and instantiate an attacker-specified class when a suitable class is available on the application classpath. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.

### 3. CVE-2026-40217｜BerriAI / LiteLLM
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.1702 / percentile=0.97134
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-12-02
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-04-10T14:16:36.307 / 2026-11-19T05:18:39.853
- **官方描述（原文）**：BerriAI LiteLLM contains an unprotected alternate channel vulnerability that could allow remote attackers to execute arbitrary code via bytecode rewriting at the /guardrails/test_custom_code URI.

### 4. CVE-2024-10441｜Synology / DiskStation Manager (DSM)
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01251 / percentile=0.70014
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-11-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2025-03-19T02:15:27.120 / 2026-11-19T05:18:23.700
- **官方描述（原文）**：Synology DSM contains an improper encoding or escaping of output vulnerability in the system plugin daemon in Synology BeeStation OS (BSM) that could allow a remote attacker to execute arbitrary code via unspecified vectors.

### 5. CVE-2026-116779｜SignalWire / FreeSwitch
- **Delta event**：EPSS_INCREASED (from=0.02473; to=0.22081)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.22081 / percentile=0.97713
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-05T20:17:44.790 / 2026-11-10T05:17:57.830
- **官方描述（原文）**：SignalWire FreeSwitch contains a code injection vulnerability that permits configuration and credential disclosure, arbitrary call control, and command execution.

### 6. CVE-2026-76807｜Doist / todoist-mcp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T20:19:13.090)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T20:19:13.090 / 2026-11-18T21:18:03.043
- **官方描述（原文）**：Todoist MCP Server provides tools that allow AI agents to access and modify a Todoist account. Prior to 10.3.3, the optional todoist-mcp-http server accepts browser-origin requests to POST /mcp without validating the Host and Origin headers or authenticating the browser caller. A malicious website can use DNS rebinding to reach the loopback listener and invoke MCP tools through StreamableHTTPServerTransport, which uses the server-held Todoist API key. This exposes Todoist account data and permits operations such as task creation, updates, completion, and deletion. The stdio transport is not browser-reachable and is not affected by this attack path. This issue is fixed in version 10.3.3.

### 7. CVE-2026-130682｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:11.990)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:11.990 / 2026-11-18T14:17:37.167
- **官方描述（原文）**：SiYuan before 3.8.10 persists a table block's caption attribute into IAL properties without HTML sanitization, causing stored cross-site scripting upon import or sync. Attackers can inject an entity-encoded caption with an onerror handler that executes in the Electron client's nodeIntegration context to achieve remote code execution.

### 8. CVE-2026-130678｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:11.277)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:11.277 / 2026-11-18T16:18:13.133
- **官方描述（原文）**：SiYuan before 3.8.10 contains a stored cross-site scripting vulnerability that allows attackers to execute script by storing malicious Attribute View column names rendered unescaped in col.ts. Attackers can inject HTML via addAttributeViewKey, .sy.zip import, or sync, and when a victim adds or duplicates the column, insertAdjacentHTML runs JavaScript with Node.js privileges for desktop code execution.

### 9. CVE-2026-130650｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:06.260)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:06.260 / 2026-11-18T14:17:36.207
- **官方描述（原文）**：WWBN AVideo through c3edcc274c389816d434acadac07ee78eaf330c1 contains a cross-site scripting vulnerability because the default node socket server relays autoEvalCodeOnHTML without the PHP-only filter. Unauthenticated attackers can obtain an anonymous socket token and send a spoofed MSG_BATCH message to trigger client eval() in administrators' browsers for account takeover.

### 10. CVE-2026-130648｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:05.910)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:05.910 / 2026-11-18T19:17:43.430
- **官方描述（原文）**：WWBN AVideo from 6.5 contains a stored cross-site scripting vulnerability that allows users with upload permission to inject script by submitting a javascript: scheme videoLink for embed videos. The unvalidated URL is rendered into an iframe src in videoEmbeded.php and PlayerSkins.php, executing for viewers including administrators and enabling creation of new administrator accounts.

### 11. CVE-2026-130156｜morpheus65535 / bazarr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T17:17:38.673)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T17:17:38.673 / 2026-11-18T21:17:49.697
- **官方描述（原文）**：Bazarr is a companion application to Sonarr and Radarr. Prior to 1.6.3-beta.11, the /api/subtitles/subtitles-info handler uses SubtitleNameContents.get() in subtitles_contents.py and reads the caller-supplied subtitlePath after checking only its subtitle extension; because the resolved path is not confined to files indexed by Bazarr, traversal can read files outside the media library. The /api/subtitles/subtitles handler in subtitles.py passes caller-supplied path and reference to sync and translation without per-path authorization, allowing an out-of-library reference file to be read and output to overwrite a file outside the media library. The authenticate decorator gates both endpoints when API authentication is enabled, while auth = None allows access without credentials. Both paths can affect only files that the Bazarr process can read or write. This issue is fixed in version 1.6.3-beta.11.

### 12. CVE-2026-126755｜ArangoDB / ArangoDB
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:09.083)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:09.083 / 2026-11-18T18:19:04.090
- **官方描述（原文）**：ArangoDB before 3.12.11 contains an authentication bypass vulnerability caused by a parser differential between the raw path authentication gate and the URL-decoded dispatch logic. Attackers can send requests with a %5f-encoded leading underscore to endpoints like /_db/_system/%5fapi/simple/first-example to reach /_api/* actions as superuser without authentication. Exploitation evidence was first observed by the Shadowserver Foundation on 2026-09-16.

### 13. CVE-2026-126752｜dagu-org / Dagu
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:08.590)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:08.590 / 2026-11-18T17:17:35.470
- **官方描述（原文）**：Dagu 1.23.0 before 2.0.0 defaults auth.mode to none, allowing unauthenticated attackers to execute OS commands through the /api/v2/dag-runs endpoint. Attackers can send a POST request with an inline spec defining steps containing arbitrary shell commands to achieve remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2026-03-11.

### 14. CVE-2023-54419｜cym1102 / nginxWebUI
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:53.547)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:53.547 / 2026-11-18T17:17:26.577
- **官方描述（原文）**：nginxWebUI 3.0.0 before 3.5.8 contains an authentication bypass vulnerability that allows unauthenticated attackers to reach the /AdminPage/conf/runCmd endpoint by using a case-variant path that evades the case-sensitive /adminPage/ login filter. Attackers can pass OS commands through the cmd parameter, which are executed via /bin/sh with insufficient filtering of & and $() characters, achieving remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 15. CVE-2022-51027｜FIT2CLOUD / MeterSphere
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:51.580)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:51.580 / 2026-11-18T17:17:25.010
- **官方描述（原文）**：MeterSphere versions 1.13.0 before 1.14.7 and 1.15.0 before 1.16.4 contain a pre-authentication code injection vulnerability due to the /plugin/** endpoints being exposed with anonymous access. Attackers can upload a malicious jar via POST /plugin/add and invoke it through POST /plugin/customMethod using the 'entry' and 'request' parameters, which are passed to Class.forName and method invocation for remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 16. CVE-2021-48025｜Jiaxing Xiangtian Information Technology / OpenSNS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:50.927)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:50.927 / 2026-11-18T17:17:24.793
- **官方描述（原文）**：OpenSNS 3.2.1 contains an unauthenticated code injection vulnerability in the shareBox method of ShareController that allows attackers to invoke arbitrary model methods via the query parameter. Attackers can send crafted GET requests to /index.php?s=weibo/Share/shareBox abusing parse_str and ShareModel::getInfo to reach Schedule::runSchedule and execute code through assert. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 17. CVE-2021-48023｜Weaver Network Co., Ltd. / E-cology
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:50.763)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:50.763 / 2026-11-18T18:17:32.743
- **官方描述（原文）**：Weaver E-cology 9.0 contains an unrestricted file upload vulnerability in /page/exportImport/uploadOperation.jsp that allows unauthenticated attackers to upload arbitrary JSP files. Attackers can send a crafted multipart POST request with a JSP webshell written to /page/exportImport/fileTransfer/ to achieve remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-20.

### 18. CVE-2019-25782｜TopThink / ThinkPHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:48.667)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:48.667 / 2026-11-18T18:17:32.423
- **官方描述（原文）**：ThinkPHP 5.0.0 before 5.0.24 contains a code injection vulnerability that allows unauthenticated attackers to execute commands by setting _method=__construct in POST data to overwrite the Request filter property. Attackers can send POST requests to endpoints reached via ?s=captcha or ?s=index/index/index with filter[]=system and server[REQUEST_METHOD] values to execute arbitrary system commands. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 19. CVE-2016-20105｜Lucee / Lucee Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:47.940)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:47.940 / 2026-11-18T18:17:32.227
- **官方描述（原文）**：Lucee Server versions 5.0.0.0 before 5.3.4.46 contain an insecure default configuration that allows unauthenticated attackers to set the initial admin password via the first-run form on /lucee/admin/web.cfm and /lucee/admin/server.cfm. Attackers can access the 'New Password' set-password form before any password is configured to seize administrative control of the server. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-24.

### 20. CVE-2026-76100｜own-pay / OwnPay
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T21:18:02.883)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T21:18:02.883 / 2026-11-18T21:18:02.883
- **官方描述（原文）**：OwnPay is a self-hosted open-source payment gateway automation platform. In 0.2.0 and earlier, modules/gateways/alipay/AlipayGateway.php fails open when an Alipay callback lacks a signature or the merchant has no configured public key because verify(array $callbackData, array $credentials) falls back to an undefined mode credential that defaults to test mode, while verifyWebhook() returns true unconditionally. An unauthenticated request to POST /webhook/{gateway} can provide a pending order reference and matching amount, pass both verification gates without a valid payment signature, and cause the order and corresponding payment-received ledger entries to be marked completed. No fixed version is available as of this review.

### 21. CVE-2026-59975｜danielklecha / SharpIppNext
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T21:18:00.500)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T21:18:00.500 / 2026-11-18T21:18:00.500
- **官方描述（原文）**：SharpIppNext is a .NET Standard library for building Internet Printing Protocol clients and servers. Prior to 4.1.0, server-side SharpIppNext implementations using SharpIppServer.ReceiveRequestAsync or SharpIppServer.ReceiveRawRequestAsync pass incoming data to IppProtocol.ReadIppRequestAsync in SharpIpp/Protocol/IppProtocol.cs, where ReadDocumentStream is enabled by default and the remaining document body is copied with CopyToAsync into a MemoryStream without a size limit. An unauthenticated remote client can send an arbitrarily large IPP document body, exhausting process memory and causing an out-of-memory failure or service termination. Client-only implementations using SharpIppClient are not affected. This issue is fixed in version 4.1.0.

### 22. CVE-2026-30502｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:15.847)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:15.847 / 2026-11-18T20:19:09.780
- **官方描述（原文）**：A Cross-Site Scripting (XSS) vulnerability in OpenKM v6.3.12 allows attackers to execute arbitrary Javascript in the context of the user's browser via a crafted input injected into the Content parameter.

### 23. CVE-2026-130753｜heymrun / heym
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:45.753)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:45.753 / 2026-11-18T21:17:49.807
- **官方描述（原文）**：heym before 0.0.142 contains a remote code execution vulnerability in the Playwright step-mode node where _resolve_expressions_in_code substitutes workflow values directly into generated Python source. Authenticated non-admin users can craft step field values that break out of string literals to execute arbitrary Python as root inside the backend container.

### 24. CVE-2026-128669｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T20:18:59.397)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T20:18:59.397 / 2026-11-18T20:18:59.397
- **官方描述（原文）**：A Session Fixation vulnerability exists in the admin login endpoint (/admin/index.php) of PHPGurukul News Portal Project V4.1. The application fails to regenerate the session identifier (PHPSESSID) upon successful authentication. A remote attacker can exploit this by setting a known session ID in the victim's browser prior to login. Once the victim authenticates, the attacker can reuse the fixed session ID to hijack the victim's authenticated session.

### 25. CVE-2026-128664｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:40.040)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:40.040 / 2026-11-18T20:18:58.970
- **官方描述（原文）**：An insecure password reset vulnerability in the Admin Password Recovery Module of PHPGurukul News Portal Project v4.1 allows unauthenticated remote attackers to change an administrator or sub-administrator account password by providing the corresponding username and email address. The application does not require verification of account ownership through an email token, OTP, or another authentication mechanism before updating the password, potentially resulting in account takeover.

### 26. CVE-2022-51034｜Tangshan Pingsheng Electronic Technology Development Co., Ltd. / Reservoir Safety Supervision Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:52.700)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:52.700 / 2026-11-18T18:17:33.173
- **官方描述（原文）**：Tangshan Pingsheng Reservoir Safety Supervision Platform builds through 2022-11-30 contain an unauthenticated SQL injection vulnerability in the simcardId parameter of /WebServices/SIMMaintainService.asmx/GetAllRechargeRecordsBySIMCardId. Attackers can send crafted POST requests with time-based MSSQL payloads to extract database information including user, version, and database name. Exploitation evidence was first observed by the Shadowserver Foundation on 2024-07-30.

### 27. CVE-2022-51030｜Qibosoft / QiboCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:52.063)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:52.063 / 2026-11-18T18:17:33.037
- **官方描述（原文）**：QiboCMS V7 contains an arbitrary file download vulnerability in inc/job/download.php that allows unauthenticated attackers to read files by supplying a base64-encoded url parameter to /do/job.php?job=download. Attackers can bypass the .php extension check using the Windows 'ph<' wildcard to download sensitive files such as configuration files containing database credentials. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-18.

### 28. CVE-2016-20106｜NUUO / NVRmini 2
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:48.120)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:48.120 / 2026-11-18T17:17:24.253
- **官方描述（原文）**：NUUO NVRmini 2 through 3.0.8 contains a file disclosure vulnerability that allows unauthenticated attackers to read web-root files by passing a filename to the 'css' parameter of css_parser.php. Attackers can retrieve PHP source files confined to the document root, exposing hardcoded credentials and sensitive application logic. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-17.

### 29. CVE-2026-95787｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T14:17:45.533)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T14:17:45.533 / 2026-11-19T05:18:43.053
- **官方描述（原文）**：Vulnerabilities in the PAPI protocol of AOS-10 could allow an unauthenticated remote attacker to circumvent existing authentication controls. Successful exploitation could allow an attacker to gain administrative access, modify system configurations, and access or manipulate sensitive data.

### 30. CVE-2026-95645｜Zohocorp / DDI Central
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T09:17:44.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T09:17:44.810 / 2026-11-18T19:18:10.973
- **官方描述（原文）**：Zohocorp Manageengine DDI Central build below 6500 are affected by a authenticated command injection vulnerability in the Windows DDI Agent's clear_blocked_domains functionality, allowing specially crafted blocked-domain values to trigger arbitrary command execution on Windows systems.

### 31. CVE-2026-95643｜Zohocorp / DDI Central
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T09:17:44.657)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T09:17:44.657 / 2026-11-18T19:18:10.607
- **官方描述（原文）**：Zohocorp Manageengine DDI Central build below 6500 are affected by a authenticated PowerShell command injection vulnerability in the Telnet connectivity feature, allowing specially crafted IPv6 scope identifiers to execute arbitrary commands on managed Windows nodes.

### 32. CVE-2026-77297｜FabianRolfMatthiasNoll / MyMangaDB
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T21:18:03.643)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T21:18:03.643 / 2026-11-18T21:18:03.643
- **官方描述（原文）**：MyMangaDB is a self-hosted manga collection manager with automatic metadata, MyAnimeList import, Docker support, and collection statistics. Prior to 2.7.2, the unauthenticated /api/v1/database/import handler in backend/app/api/v1/endpoints/database.py accepts a ZIP archive and moves an included database file to DATABASE_PATH while also replacing IMAGE_PATH content. An attacker can supply a database containing an attacker-controlled users table and administrative account, then authenticate as that account; invalid replacement data can also destroy application data or availability. This issue is fixed in version 2.7.2.

### 33. CVE-2026-77296｜FabianRolfMatthiasNoll / MyMangaDB
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T21:18:03.497)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T21:18:03.497 / 2026-11-18T21:18:03.497
- **官方描述（原文）**：MyMangaDB is a self-hosted manga collection manager with automatic metadata, MyAnimeList import, Docker support, and collection statistics. Prior to 2.7.2, the unauthenticated /api/v1/images/manga/save handler in backend/app/api/v1/endpoints/image.py accepts a client-controlled filename and joins it to IMAGE_SAVE_PATH without confining the result. Traversal sequences can escape the image directory and overwrite process-writable files, including DATABASE_PATH for the live SQLite database, while the client-supplied image content type does not validate the uploaded bytes. An attacker can replace the database to plant an administrative user and can overwrite other writable files, causing full application compromise and availability loss. This issue is fixed in version 2.7.2.

### 34. CVE-2026-75521｜mirendev / runtime
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:18:08.200)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:18:08.200 / 2026-11-18T19:18:08.200
- **官方描述（原文）**：Miren Runtime provides the runtime component for the Miren application platform. Prior to 0.11.1, the QUIC/HTTP3 RPC server on the default port 8443 uses tls.RequestClientCert and does not verify that presented certificates chain to the configured cluster certificate authority. The RPC authenticators derive a caller identity from PeerCertificates[0].Subject.CommonName without requiring a non-empty VerifiedChains value, and certificate identities bypass all RBAC checks. A network attacker who can reach the listener can present a self-signed certificate with an issuer distinguished name matching the public cluster CA subject and gain cluster superuser access, allowing disclosure, modification, or disruption of applications, sandboxes, disks, credentials, and other managed resources. This issue is fixed in version 0.11.1.

### 35. CVE-2026-73969｜ansibleguy76 / ansibleforms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T21:18:02.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T21:18:02.120 / 2026-11-18T21:18:02.120
- **官方描述（原文）**：AnsibleForms is a self-hosted web application that turns automation into self-service forms. Prior to 6.2.1, AnsibleForms uses a public hard-coded fallback JWT signing secret from server/config/auth.config.js when ACCESS_TOKEN_SECRET is unset. An unauthenticated attacker can sign a self-contained token with privileged claims because server/src/auth/auth_jwt.js verifies the signature without reloading the user from the database, and server/src/lib/middleware.js trusts the token's roles and options for authorization. A forged token can therefore be accepted as an administrator session, resulting in authentication bypass and full privileged API access. This issue is fixed in version 6.2.1.

### 36. CVE-2026-71499｜hefy2027 / cf-manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:18:07.890)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:18:07.890 / 2026-11-18T21:18:01.590
- **官方描述（原文）**：cf-manager is an all-in-one dashboard for managing multiple Cloudflare accounts and services. Prior to 1.1.2, worker/src/routes/workers.ts uses bare fetch(url) calls to retrieve user-supplied URLs and deploys the returned content as a Worker script using stored Cloudflare credentials. The multipart and JSON branches of POST /api/:accountId/workers and POST /api/batch-deploy accept URLs without protocol, destination, redirect, content-type, or response-size validation. An attacker with deployment API access, or unauthenticated access when API_SECRET is not configured, can make cf-manager access internal resources or fetch attacker-controlled JavaScript and execute it in the victim Cloudflare Workers account. This issue is fixed in version 1.1.2.

### 37. CVE-2026-63413｜janephp / janephp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T22:17:22.850)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T22:17:22.850 / 2026-11-18T22:17:22.850
- **官方描述（原文）**：Jane is a set of PHP libraries that generates models and API clients from JSON Schema and OpenAPI specifications. Prior to 7.12.0, the Jane open-api-3 generator emits an OpenAPI header parameter name verbatim as an array key in generated Client/Endpoint method docblocks. A header parameter name containing a PHPDoc closing delimiter can terminate the comment early and place attacker-controlled PHP in class-body position, including an __construct method that runs when the generated Client is instantiated. Exploitation requires generating a client from an attacker-influenced OpenAPI document and then using the generated SDK, and can execute arbitrary PHP with the consuming application's privileges. This issue is fixed in version 7.12.0.

### 38. CVE-2026-63412｜janephp / janephp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T22:17:22.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T22:17:22.710 / 2026-11-18T22:17:22.710
- **官方描述（原文）**：Jane is a set of PHP libraries that generates models and API clients from JSON Schema and OpenAPI specifications. Prior to 7.12.0, the Jane open-api-3 generator emits an OpenAPI query parameter name verbatim as an array key in generated Client/Endpoint method docblocks. A query parameter name containing a PHPDoc closing delimiter can terminate the comment early and place attacker-controlled PHP in class-body position, including an __construct method that runs when the generated Client is instantiated. Exploitation requires generating a client from an attacker-influenced OpenAPI document and then using the generated SDK, and can execute arbitrary PHP with the consuming application's privileges. This issue is fixed in version 7.12.0.

### 39. CVE-2026-63411｜janephp / janephp
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T22:17:22.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T22:17:22.550 / 2026-11-18T22:17:22.550
- **官方描述（原文）**：Jane is a set of PHP libraries that generates models and API clients from JSON Schema and OpenAPI specifications. Prior to 7.12.0, the Jane open-api-3 generator emits an OpenAPI parameter description verbatim in generated Client/Endpoint method docblocks. A parameter description containing a PHPDoc closing delimiter can terminate the comment early and place attacker-controlled PHP in class-body position, including an __construct method that runs when the generated Client is instantiated. Exploitation requires generating a client from an attacker-influenced OpenAPI document and then using the generated SDK, and can execute arbitrary PHP with the consuming application's privileges. This issue is fixed in version 7.12.0.

### 40. CVE-2026-63189｜n4ze3m / dialoqbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:16.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:16.520 / 2026-11-18T18:19:50.253
- **官方描述（原文）**：Dialoqbase is an application for creating chatbots. Prior to 1.11.5, the unauthenticated GET /api/v1/view/* route in server/src/routes/api/v1/view/root.ts resolves its attacker-controlled wildcard path without normalization or containment, allowing traversal outside the intended uploads directory and arbitrary server file reads. Reading environment files can disclose DB_SECRET_KEY, the application’s JWT signing key, which permits forged administrator tokens and takeover of bots, conversations, integrations, and stored third-party credentials. This issue is fixed in version 1.11.5.

### 41. CVE-2026-61532｜chamilo / chamilo-lms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:18:06.843)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:18:06.843 / 2026-11-18T19:18:06.843
- **官方描述（原文）**：Chamilo LMS is an open-source learning management system. Prior to 1.11.40 and 2.0.3, src/Chamilo/CourseBundle/Component/CourseCopy/CourseRestorer.php and src/CourseBundle/Component/CourseCopy/CourseRestorer.php use paths supplied by an imported legacy course backup without consistently confining them to the extraction directory. A course teacher can import a crafted backup containing parent-directory path segments, causing file operations to write attacker-controlled content outside the intended destination, including PHP-executable or automatically loaded locations. This can result in code execution as the PHP process and compromise course data, user data, credentials, and the host. This issue is fixed in versions 1.11.40 and 2.0.3.

### 42. CVE-2026-55508｜wavelog / wavelog
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T21:18:00.170)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T21:18:00.170 / 2026-11-18T21:18:00.300
- **官方描述（原文）**：Wavelog is web-based amateur radio logging software. Prior to 2.5, the callsign parameter accepted by POST /oqrs/search_log in application/controllers/Oqrs.php search_log() reaches application/models/Oqrs_model.php search_log(), where it is concatenated directly into a raw SQL WHERE clause without parameter binding. An unauthenticated remote attacker can use UNION-based SQL injection to read arbitrary application database records, including account data, password hashes, API keys, station credentials, reset tokens, QSO data, and station metadata. Disclosure of password reset tokens can be combined with the forgot_password workflow to take over accounts, including administrator accounts. This issue is fixed in version 2.5.

### 43. CVE-2026-55506｜wavelog / wavelog
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T21:17:59.833)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T21:17:59.833 / 2026-11-18T21:17:59.963
- **官方描述（原文）**：Wavelog is web-based amateur radio logging software. Prior to 2.5, the filename parameter accepted by POST /qsl/addQsoToQsl in application/controllers/Qsl.php addQsoToQsl() is stored without rejecting directory separators or relative path components, and POST /qsl/delete reaches application/models/Qsl_model.php deleteQsl(), which passes the planted qsl_images filename to unlink(). A standard authenticated user can associate the malicious filename with the user's own QSO, satisfy the ownership check, escape the per-user QSL image directory, and delete files writable by the PHP worker. Deleting configuration or operational files can cause denial of service, while deleting installer gate files can reopen the unauthenticated installer and enable application identity takeover through attacker-controlled database configuration. This issue is fixed in version 2.5.

### 44. CVE-2026-55171｜OSC / ondemand
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T21:17:59.350)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T21:17:59.350 / 2026-11-18T21:17:59.350
- **官方描述（原文）**：Open OnDemand is an open-source high-performance computing portal. Prior to Open OnDemand 4.1.6 and 4.2.3, and prior to ood-ansible 4.2.1, the portal generator defaults OIDCCryptoPassphrase to SHA1(servername), and the templates/ood_portal.yml.j2 role checks a different variable from the documented passphrase setting. Administrators who set ood_oidc_crypto_passphrase can therefore believe a strong secret is configured while the deployment continues to use an attacker-derivable value. In OIDCSessionType client-cookie deployments, an unauthenticated remote attacker can derive the encryption key and forge a mod_auth_openidc_session cookie for another user, while server-cache deployments permit lower-impact tampering with protected OIDC state and nonce cookies. This issue is fixed in Open OnDemand versions 4.1.6 and 4.2.3 and ood-ansible version 4.2.1.

### 45. CVE-2026-19707｜Airlock by Ergon / Airlock Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T10:16:55.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T10:16:55.237 / 2026-11-18T20:19:09.637
- **官方描述（原文）**：A bug in the Airlock Gateway (8.5.2 and earlier, and 8.6.0) allows attacker-controlled HTML in a backend response to exploit the Smart Form Protection feature, possibly leading to a Denial of Service (DoS) or Remote Code Execution (RCE) attack against the Airlock Gateway. The issue has been fixed in Airlock Gateway version 8.5.3 and 8.6.1. For an attack to be executable, the Airlock Gateway needs to have 'Smart Form Protection' (or the corresponding expert settings) enabled on a mapping whose backend returns a response containing certain multi-byte HTML character references. The buffer overflow then happens during the parsing of that HTML response. Such a response can come either from a malicious or compromised backend, or from an otherwise trusted backend that returns attacker-supplied HTML, e.g. an application that stores and serves plain user-provided HTML files. Successfully exploiting the vulnerability can enable an attacker to perform a DoS attack or, in the worst case, an RCE attack against the Airlock Gateway in front of the affected backend. Compromising the functionality of the Airlock Gateway could in this way also affect the availability and protection of other well-intentioned backends deployed behind the same Gateway.

### 46. CVE-2026-132808｜Ubiquiti Inc / UniFi Access Application
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T05:18:39.513)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T05:18:39.513 / 2026-11-19T05:18:39.513
- **官方描述（原文）**：A malicious actor with access to the network and low privileges could exploit an Incorrect Authorization vulnerability found in UniFi Access Application to execute arbitrary commands on certain adopted UniFi Access devices.

### 47. CVE-2026-132807｜Ubiquiti Inc / UniFi Access Application
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T05:18:39.360)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T05:18:39.360 / 2026-11-19T05:18:39.360
- **官方描述（原文）**：A malicious actor with access to the network and under certain conditions could exploit an Improper Certificate Validation vulnerability found in UniFi Access Application to obtain sensitive information from and make unauthorized changes to an adopted UniFi Access device.

### 48. CVE-2026-132804｜Ubiquiti Inc / UniFi Access Application
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T05:18:38.833)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T05:18:38.833 / 2026-11-19T05:18:38.833
- **官方描述（原文）**：A malicious actor with access to the network and low privileges could exploit a Server-Side Request Forgery (SSRF) vulnerability found in UniFi Access Application to escalate privileges within UniFi OS.

### 49. CVE-2026-132803｜Ubiquiti Inc / UniFi Access Application
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T05:18:38.673)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T05:18:38.673 / 2026-11-19T05:18:38.673
- **官方描述（原文）**：A malicious actor with access to the network and low privileges could exploit a series of authenticated SQL Injection vulnerabilities found in UniFi Access Application to escalate privileges on the host device.

### 50. CVE-2026-132802｜Ubiquiti Inc / UniFi Access Application
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T05:18:38.507)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T05:18:38.507 / 2026-11-19T05:18:38.507
- **官方描述（原文）**：A malicious actor with access to the network and low privileges could exploit an Improper Link Resolution Before File Access vulnerability found in UniFi Access Application to execute arbitrary code with root privileges on the host device.

### 51. CVE-2026-132622｜GearUP / Hyperev
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T04:17:27.700)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T04:17:27.700 / 2026-11-19T04:17:27.853
- **官方描述（原文）**：A vulnerability was found in GearUP Hyperev up to 20261020. This impacts the function get_wlan_sitesurvey of the file ld/utils.lua of the component WLAN Site Survey. Performing a manipulation of the argument line results in os command injection. The attack is possible to be carried out remotely. The vendor was contacted early about this disclosure but did not respond in any way.

### 52. CVE-2026-132234｜JetBrains / TeamCity
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T17:17:44.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T17:17:44.980 / 2026-11-19T05:18:36.783
- **官方描述（原文）**：In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via argument injection in Mercurial VCS root settings

### 53. CVE-2026-132233｜JetBrains / TeamCity
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T17:17:44.853)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T17:17:44.853 / 2026-11-19T05:18:36.640
- **官方描述（原文）**：In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via build attribute injection

### 54. CVE-2026-132232｜JetBrains / TeamCity
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T17:17:44.733)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T17:17:44.733 / 2026-11-19T05:18:36.497
- **官方描述（原文）**：In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via argument injection in Perforce settings

### 55. CVE-2026-132231｜JetBrains / TeamCity
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T17:17:44.593)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T17:17:44.593 / 2026-11-19T05:18:36.357
- **官方描述（原文）**：In JetBrains TeamCity before 2026.1.3, 2025.11.7 remote code execution was possible via best-fit character mapping in Perforce settings

### 56. CVE-2026-132209｜winCRM / winSAT.exe
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T17:17:42.890)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T17:17:42.890 / 2026-11-18T19:17:58.193
- **官方描述（原文）**：Hardcoded credentials in the executable file. These can be extracted using the “Strings.exe” tool and could allow an attacker unauthorized access to the database and SMTP server. winSAT.exe

### 57. CVE-2026-132208｜winCRM / winCRM.exe
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T17:17:42.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T17:17:42.760 / 2026-11-18T19:17:58.030
- **官方描述（原文）**：Hardcoded credentials in the executable file. These can be extracted using the “Strings.exe” tool and could allow an attacker unauthorized access to the database and SMTP server. winCRM.exe

### 58. CVE-2026-131914｜Idunno / AntiCsrf
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T02:17:20.360)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T02:17:20.360 / 2026-11-19T02:17:20.360
- **官方描述（原文）**：Deserialization of untrusted data in double-submit cookie vs. form field validation in Idunno.AntiCsrf versions through 0.9.1 Beta on ASP.NET allows remote unauthenticated attackers to execute code via object injection

### 59. CVE-2026-130786｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:55.157)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:55.157 / 2026-11-18T19:17:55.273
- **官方描述（原文）**：Incus before 7.6.0 contains a configuration injection vulnerability that allows users who can launch instances from controlled images to inject LXC directives by embedding line breaks in OCI config.json values or oci.entrypoint and oci.cwd keys. Attackers can add liblxc hooks or crafted tmpfs lxc.mount.entry fields to run commands as root on the host or bind-mount host paths, even from restricted projects.

### 60. CVE-2026-130784｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:54.837)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:54.837 / 2026-11-18T19:17:54.953
- **官方描述（原文）**：Incus before 7.6.0 contains an authorization bypass vulnerability that allows restricted clients to create and access default project resources by exploiting entitlement checks against the requested project. Attackers can create bridge networks with raw.dnsmasq directives to execute code as root on the host, or manipulate inherited resources via the ?project= parameter.

### 61. CVE-2026-130783｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:54.683)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:54.683 / 2026-11-18T19:17:54.797
- **官方描述（原文）**：Incus before 7.6.0 exposes certificate and cluster join token secrets through the default project event stream and skips authorization when cancelling operations without associated permissions. Restricted clients can subscribe to operation events to capture certificate tokens and enroll unrestricted certificates, gaining full server access, or cancel token operations by UUID.

### 62. CVE-2026-130780｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:54.067)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:54.067 / 2026-11-18T19:17:54.220
- **官方描述（原文）**：Incus before 7.6.0 contains a path traversal vulnerability that allows malicious migration peers to write outside intended directories by supplying unvalidated dependent volume and snapshot names in the migration offer header. Attackers controlling a migration source can create root-owned volumes with attacker content at arbitrary host paths, compromising hosts using dir storage pools, bypassing restricted.storage-pools.access, or crashing the daemon.

### 63. CVE-2026-130778｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:53.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:53.607 / 2026-11-18T19:17:53.767
- **官方描述（原文）**：Incus before 7.6.0 contains an authentication bypass vulnerability that allows remote attackers to authenticate as any trusted certificate by appending its public certificate to their presented TLS client chain. Attackers can append the server's or a cluster member's certificate to gain cluster-level access, bypass authorization, modify trust store entries, and influence scriptlet-based authorization decisions.

### 64. CVE-2026-130774｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:52.023)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:52.023 / 2026-11-18T19:17:52.237
- **官方描述（原文）**：Incus before 7.6.0 contains a privilege escalation vulnerability: rebuilding a never-started unprivileged container makes it boot without a user namespace. Root processes inside the container run as host uid 0, keeping capabilities like sys_module, with no device cgroup restriction, letting them load kernel modules and compromise the host.

### 65. CVE-2026-130773｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:51.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:51.587 / 2026-11-18T21:17:50.403
- **官方描述（原文）**：Incus before 7.6.0 contains an authorization bypass that allows restricted project users to create resources in the unrestricted default project by targeting projects lacking features.* flags. Attackers can create bridge networks with raw.dnsmasq dhcp-script injection to run scripts as root, or custom volumes with block.create_options mkfs arguments to read host files.

### 66. CVE-2026-130770｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:50.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:50.250 / 2026-11-18T19:17:50.633
- **官方描述（原文）**：Incus before 7.6.0 creates the NBD servers used for virtual machine migration and disk export on abstract unix sockets, which have no permission checks and whose names are visible in /proc/net/unix. A local unprivileged user can connect while an operation runs to read or modify the VM disk, gaining code execution in the guest on a migration's receiving side.

### 67. CVE-2026-130759｜fleetdm / fleet
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:46.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:46.750 / 2026-11-18T19:17:46.750
- **官方描述（原文）**：Fleet from 4.71.0 before 4.88.2 contains an authentication bypass vulnerability in the SAML SSO callback that looks up sessions using unvalidated client-supplied identifiers. Users able to run live queries or enroll secret holders can plant attacker-controlled identity provider metadata in the session store, then present a self-signed SAML response to log in as a global admin.

### 68. CVE-2026-130757｜fleetdm / fleet
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:46.437)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:46.437 / 2026-11-18T21:17:49.930
- **官方描述（原文）**：Fleet before 4.92.0 contains an improper authentication vulnerability that allows attackers to reuse case-mutated security tokens because MySQL token columns used case-insensitive collation. Attackers holding a case-normalized invite or email-change token can redirect a victim's email for account takeover or redeem invites with roles up to Global Admin.

### 69. CVE-2026-130756｜pnpm / exe
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:46.287)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:46.287 / 2026-11-18T19:17:46.287
- **官方描述（原文）**：pnpm exe before 10.34.8 embeds an outdated Node.js runtime that still trusts compromised eMudhra intermediate CA certificates during registry TLS connections. Network attackers holding a recovered intermediate key can intercept standalone pnpm registry fetches and serve forged package metadata or tarballs.

### 70. CVE-2026-130754｜laradashboard / laradashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:45.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:45.940 / 2026-11-18T19:17:46.077
- **官方描述（原文）**：All versions of LaraDashboard contain an authentication bypass in SocialAuthService::findOrCreateUser(), which links a social login to an existing account by email without checking that the OAuth provider verified that email. Unauthenticated attackers using an OAuth/OIDC provider that asserts a victim's email can log in as any user, including Superadmin, and keep persistent access through a linked social_accounts entry.

### 71. CVE-2026-130747｜getgrav / grav
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:22.197)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:22.197 / 2026-11-18T18:19:12.900
- **官方描述（原文）**：Grav before 1.7.53.7 and 2.x before 2.2.18 contains an authentication bypass vulnerability that allows anonymous visitors to create super-admin accounts because UserCollection::count() uses an unescaped glob() pattern. On installs whose path contains brackets or a backslash, the account count returns zero, so attackers can send requests to POST /api/v1/auth/setup or the classic admin registration form to create or overwrite administrator accounts.

### 72. CVE-2026-130735｜getgrav / grav
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:20.010)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:20.010 / 2026-11-18T18:19:12.507
- **官方描述（原文）**：Grav from 2.0.0 before 2.2.18 contains a Twig injection vulnerability that allows media-only accounts and anonymous uploaders to execute Twig by placing delimiters in image titles, alt text, class, id, or file names. Attackers can combine injected Twig with the autoescape tag to serve script to every page visitor, including super admins, or expose unpublished page content.

### 73. CVE-2026-130733｜getgrav / grav
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:19.627)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:19.627 / 2026-11-18T12:17:19.770
- **官方描述（原文）**：Grav from 2.0.0 before 2.2.18 contains an authorization bypass vulnerability that allows publishers to overwrite pages their per-page permissions deny by abusing FolderStorage key delimiter collisions and PageStorage folder reconstruction. Attackers can rename a folder like locked*** or save from a page with an unusual prefix width through a front-end Flex pages form, replacing protected content and permissions to access the protected subtree.

### 74. CVE-2026-130730｜nocodb / nocodb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:19.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:19.130 / 2026-11-18T12:17:19.130
- **官方描述（原文）**：NocoDB before 2026.10.1 contains an authentication bypass vulnerability that allows OAuth token holders to act as full sessions because OAuth access tokens are signed with the instance JWT secret. Attackers can present a narrowly scoped OAuth token to the session strategy, short-lived-token exchange, or NocoSocket handshake to gain the granting user's full privileges.

### 75. CVE-2026-130716｜nocodb / nocodb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:17.010)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:17.010 / 2026-11-18T14:17:38.230
- **官方描述（原文）**：NocoDB before 2026.08.0 contains a stored cross-site scripting vulnerability that allows authenticated Creator or Editor users to execute script by injecting markup into fields rendered through URL() formulas. The canvas grid renderer assigns unsanitized formula output to innerHTML, letting attackers steal session tokens from localStorage and take over accounts of users viewing the table.

### 76. CVE-2026-130712｜nocodb / nocodb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:16.390)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:16.390 / 2026-11-18T14:17:38.093
- **官方描述（原文）**：NocoDB before 2026.08.1 contains an authorization bypass vulnerability that allows authenticated Creators to access another tenant's external database by reusing a victim source id when adding a source. Because NcConnectionMgrv2 caches connections by bare source id, attackers can reflect the victim's cached database schema and read, update, and insert records through their own base models.

### 77. CVE-2026-130706｜nocodb / nocodb
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:15.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:15.490 / 2026-11-18T20:19:00.393
- **官方描述（原文）**：NocoDB before 2026.09.0 contains an sql injection vulnerability that allows authenticated Creator or Owner users to inject raw SQL by persisting a crafted formula parsed_tree reused without revalidation. Attackers can bypass the SQLite metadata path guard with an alias to plant the tree, escalating to super administrator or executing OS commands on external PostgreSQL hosts.

### 78. CVE-2026-130683｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:12.160)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:12.160 / 2026-11-18T12:17:12.283
- **官方描述（原文）**：SiYuan before 3.8.10 uses an incomplete deny-list in IsSensitivePath that omits shell-initialization files such as .zshenv and .bash_profile, as well as ~/.local. Authenticated administrators can call /api/file/copyFile with an absolute destination outside the workspace to write payloads there, which execute as the user on the next shell or login.

### 79. CVE-2026-130681｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:11.817)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:11.817 / 2026-11-18T18:19:10.610
- **官方描述（原文）**：SiYuan before 3.8.10 contains a stored cross-site scripting vulnerability, an incomplete fix for CVE-2026-44670, because renderAVAttribute() inserts an Attribute View name unescaped into the database row attribute panel header. Attackers who can persist the name, such as via the setAttrViewName action, can inject an onerror handler that runs OS commands through Node.js when a desktop user opens the panel.

### 80. CVE-2026-130680｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:11.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:11.630 / 2026-11-18T19:17:45.060
- **官方描述（原文）**：SiYuan from 3.3.0 before 3.8.10 contains a stored cross-site scripting vulnerability that allows attackers to inject HTML via unescaped checkbox column names in Gallery and Kanban AttributeView renderers. Attackers can share a crafted .sy.zip document whose rendering in the Electron desktop client with nodeIntegration enabled executes Node.js and host OS commands.

### 81. CVE-2026-130679｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:11.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:11.450 / 2026-11-18T12:17:11.580
- **官方描述（原文）**：SiYuan before 3.8.10 contains a stored cross-site scripting vulnerability in genAVValueHTML() that allows attackers who can store Attribute View asset values to inject script through an unescaped image src attribute. Attackers can store an image URL containing a double quote and onerror handler that executes OS commands via Node.js in the desktop app when victims open the bound note or row attribute panel.

### 82. CVE-2026-130675｜craftcms / cms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:10.783)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:10.783 / 2026-11-18T12:17:10.903
- **官方描述（原文）**：Craft CMS from 5.0.0 before 5.11.4 contains a remote code execution vulnerability in ImageTransforms::normalizeTransform() that allows attackers to instantiate arbitrary classes by supplying class:null with a __class key. Attackers can reach the method through Craft Commerce's payments/pay redirect template calling customer.photo.getUrl() with a crafted transform to instantiate classes like yii\rbac\PhpManager and execute PHP.

### 83. CVE-2026-130674｜craftcms / cms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:10.403)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:10.403 / 2026-11-18T14:17:37.030
- **官方描述（原文）**：Craft CMS from 5.0.0 before 5.11.4 contains an incomplete blocklist fix that allows attackers who can author entry type title formats to write arbitrary files using ZipArchive or XMLWriter classes. Attackers can abuse the non-sandboxed renderObjectTemplate() renderer to write attacker-controlled content into the web docroot, achieving remote code execution.

### 84. CVE-2026-130154｜Zyrabit-tech / zyrabit-SLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T17:17:38.513)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T17:17:38.513 / 2026-11-18T17:17:38.513
- **官方描述（原文）**：Zyrabit Platform provides sovereign AI infrastructure for enterprise retrieval-augmented generation. Prior to 2.4.4, import_to_vault(source_path, destination_name) accepts both caller-controlled paths, but the content-pattern guard does not confine destination_name. The vulnerable tool is implemented in zyrabit-slm/api-rag/app/domain/services/mcp_service.py, where Path(DOCS_DIR) / destination_name is passed to shutil.copy2, allowing traversal or an absolute destination to write outside the vault. An unrestricted source_path can be copied into the vault and retrieved through secure_query, disclosing files readable by the service; files that do not match the executable-pattern filter pass that filter. When ENABLE_LEGACY_EXTENSIONS=true, zyrabit-slm/api-rag/app/main.py registers POST /mcp/rpc without get_current_user, allowing unauthenticated network tool calls; this optional exposure is disabled by default and is not required for local invocation. If an attacker can stage chosen source content and write to an execution-triggered destination, the advisory describes conditional process execution. This issue is fixed in version 2.4.4.

### 85. CVE-2026-129991｜Dokploy / dokploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T23:17:19.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T23:17:19.090 / 2026-11-18T23:17:19.230
- **官方描述（原文）**：Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, the backup prefix field is only checked for a nonempty value, and normalizeS3Path preserves shell metacharacters before the prefix is interpolated into rclone upload and retention-cleanup command strings. An authenticated organization member with backup permission for a service can execute arbitrary commands as root on the Dokploy host or configured remote server when a PostgreSQL, MySQL, MariaDB, MongoDB, libSQL, Compose, or web-server backup runs manually, on schedule, or performs retention cleanup. This issue is fixed in version 0.31.1.

### 86. CVE-2026-129989｜Dokploy / dokploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T23:17:18.737)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T23:17:18.737 / 2026-11-18T23:17:18.883
- **官方描述（原文）**：Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, the Nixpacks publishDirectory build setting accepts shell metacharacters and is interpolated into a docker cp command executed through child_process.exec. An authenticated user with access to an application can execute arbitrary commands on the Dokploy host when triggering a Nixpacks deployment, leading to host compromise through the privileged Docker environment. This issue is fixed in version 0.31.1.

### 87. CVE-2026-129987｜Dokploy / dokploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T22:17:18.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T22:17:18.237 / 2026-11-18T22:17:18.373
- **官方描述（原文）**：Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, the database password validation used by the MySQL, PostgreSQL, MariaDB, MongoDB, and Redis change-password procedures permits backticks, and the procedures interpolate attacker-controlled passwords into Bash command strings. An authenticated user who can update a database password can trigger command substitution before the database command runs, resulting in arbitrary operating-system command execution with the Dokploy process privileges, which are typically root. This issue is fixed in version 0.31.1.

### 88. CVE-2026-129986｜Dokploy / dokploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T23:17:18.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T23:17:18.550 / 2026-11-18T23:17:18.697
- **官方描述（原文）**：Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, mount.deleteFileMount passes a path containing the user-controlled filePath to the local removeFileOrDirectory helper, which interpolates it unquoted into rm -rf, while the remote branch is quoted. An authenticated member with file-mount create and delete permissions can execute arbitrary commands in the host context immediately when deleting a local file mount, without requiring a running container. This issue is fixed in version 0.31.1.

### 89. CVE-2026-129961｜LMS / LMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T13:17:26.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T13:17:26.990 / 2026-11-18T21:17:48.810
- **官方描述（原文）**：LMS (Lan Management System) is vulnerable to Remote Code Execution in its e-mail-based Helpdesk ticket intake. The mail parser does not reject Apache .htaccess configuration files or PHP-executable files when saving ticket attachments. A remote unauthenticated attacker can e-mail a Helpdesk ticket with such an attachment; in the default configuration, anyone can request the uploaded file's URL which executes attacker-supplied code with the privileges of the web server process. No operator interaction or LMS client session is required. The issue was fixed in commit d5059b1.

### 90. CVE-2026-129316｜Dokploy / dokploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T23:17:18.187)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T23:17:18.187 / 2026-11-18T23:17:18.337
- **官方描述（原文）**：Dokploy is a free, self-hostable Platform as a Service (PaaS). From 0.29.13 until 0.31.0, the Docker terminal, container-log, and monitoring WebSocket handlers accept a caller-controlled serviceId as authorization but do not consistently bind the requested containerId or appName to that service. A member with read access to any service can consequently target unrelated containers, obtain a root shell in the Dokploy panel container, read other tenants' logs and statistics, and use the mounted Docker socket to compromise the host. This issue is fixed in version 0.31.0.

### 91. CVE-2026-127143｜LMS / LMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T13:17:25.153)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T13:17:25.153 / 2026-11-18T21:17:48.033
- **官方描述（原文）**：LMS (Lan Management System) is vulnerable to privilege escalation in the lmsd daemon. The daemon loads the libraries listed in the LMS database without checking that they come from a trusted location. An attacker with access to the web server process or with write access to the LMS database can register a malicious library and trigger a configuration reload, causing lmsd to load and execute it. Because the example systemd unit does not set a separate user, lmsd runs as root, allowing the attacker to execute arbitrary code with root privileges. This issue was fixed in commit 89dd3f7. The lmsd component was removed. For existing installations that use lmsd, the recommended solution is to disable and remove this component.

### 92. CVE-2026-124990｜masteriyo / Masteriyo LMS – LMS Course Builder, Quizzes & Certificates
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:05.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:05.313 / 2026-11-18T18:19:03.240
- **官方描述（原文）**：The Masteriyo LMS – LMS Course Builder, Quizzes & Certificates plugin for WordPress is vulnerable to PHP Object Injection in versions up to, and including, 3.5.1 via deserialization of untrusted input in the course importer. The set_post_metas() method calls maybe_unserialize() on attacker-controlled postmeta string values parsed from the uploaded JSON import file. This makes it possible for unauthenticated attackers to inject arbitrary PHP Objects. Exploitation by unauthenticated attackers requires that the site has enable_instructor_registration=true AND enable_guest_checkout=true AND at least one purchasable course exists. Install.php sets enable_instructor_registration=false on fresh installs, so this is a non-default configuration. On a default installation, where that is not configured, the vulnerability requires attackers with author-level access and above.

### 93. CVE-2026-123637｜F5 / BIG-IP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:04.500)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:04.500 / 2026-11-19T05:18:31.037
- **官方描述（原文）**：When BIG-IP APM is provisioned and a per-request policy that includes the Client Information agent and Endpoint Security agents is applied to a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE). Impact: Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system and may allow the attacker to perform RCE. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 94. CVE-2026-123634｜F5 / NGINX Plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:04.353)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:04.353 / 2026-11-19T05:18:30.860
- **官方描述（原文）**：This issue occurs when NGINX Plus or NGINX Open Source is configured as a proxy, the proxied server name includes variables, and a Server Side Includes (SSI) or mirror directive sends a subrequest to a location that resolves the same server name. Under these conditions, a specially crafted HTTP request may cause a use-after-free condition in a worker process. An attacker may also be able to execute code if Address Space Layout Randomization (ASLR) is disabled or the attacker can bypass ASLR. Impact: An attacker could leverage this vulnerability to crash the NGINX worker process, corrupt its memory, or perform remote code execution (RCE) Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 95. CVE-2026-123633｜F5 / NGINX Open Source
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:04.207)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:04.207 / 2026-11-19T06:16:53.710
- **官方描述（原文）**：When NGINX Plus or NGINX Open Source is configured to use HTTP/2 for client connections and proxy client requests to a backend, a specially crafted request can result in use-after-free in the worker process, if this process is running low on worker_connections. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. Impact: This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or may allow a code execution. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 96. CVE-2026-123007｜F5 / NGINX Plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:04.047)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:04.047 / 2026-11-19T06:16:53.520
- **官方描述（原文）**：This issue affects NGINX Plus or NGINX Open Source configurations that use HTTP/2. When NGINX processes undisclosed traffic, the flow control window can exceed the allowed threshold, potentially resulting in a heap buffer overflow typically followed by an NGINX worker segmentation fault. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. Impact: An attacker could leverage this vulnerability to crash the NGINX worker process, corrupt its memory, or potentially execute code remotely. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 97. CVE-2026-121810｜F5 / NGINX Plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:03.763)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:03.763 / 2026-11-19T05:18:30.267
- **官方描述（原文）**：Description: This issue affects NGINX Plus and NGINX Open Source configurations that use HTTP/3. A remote, unauthenticated attacker can cause a use-after-free condition in the NGINX worker process, leading to a restart. Exploitation also depends on conditions beyond the attacker’s control. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. Impact: This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or to possibly trigger a code execution. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 98. CVE-2026-121805｜F5 / BIG-IP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:03.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:03.607 / 2026-11-19T05:18:30.070
- **官方描述（原文）**：Description: When an iRule that processes client traffic using the PEM::subscriber command is configured on a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE). Impact: Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system and may perform RCE. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 99. CVE-2026-120722｜F5 / BIG-IP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:03.150)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:03.150 / 2026-11-19T05:18:29.900
- **官方描述（原文）**：Description: When an iRule that processes client traffic using the DNS::scrape command is configured on a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE). Impact: Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system. In addition, the attacker may be able to perform RCE. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 100. CVE-2026-120718｜F5 / BIG-IP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:03.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:03.013 / 2026-11-18T17:17:29.837
- **官方描述（原文）**：Description: BIG-IP iControl REST tokens may not expire as expected in all scenarios. Impact: An attacker who has obtained a token may be able to extend its expiry lifetime unless the token owner deletes it. There is no data plane exposure; this is a control plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 101. CVE-2026-120292｜F5 / BIG-IP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:02.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:02.110 / 2026-11-19T05:18:29.740
- **官方描述（原文）**：Description: When an HTTP profile and an iRule using the MR::message route command are configured on a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE) Impact: Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system and may allow the attacker to perform RCE. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 102. CVE-2026-120285｜F5 / BIG-IP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:01.957)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:01.957 / 2026-11-19T05:18:29.570
- **官方描述（原文）**：Description When an HTTP profile and an iRule containing the PSC::ip_address command are configured on a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE). Impact Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system and may allow the attacker to perform RCE. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 103. CVE-2026-116953｜F5 / BIG-IP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:18:00.197)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:18:00.197 / 2026-11-19T05:18:29.403
- **官方描述（原文）**：Description: When an iRule that processes client traffic using the GENERICMESSAGE::route command is configured on a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE). Impact: Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system and may allow the attacker to perform RCE. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 104. CVE-2026-116449｜Dell / PowerStore 500T
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:59.947)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:59.947 / 2026-11-19T05:18:29.240
- **官方描述（原文）**：Dell PowerStore SDNAS contains an OS Command Injection vulnerability that could allow an attacker with internal network access to execute arbitrary commands as root on the NAS node.

### 105. CVE-2026-116448｜Dell / PowerStore 500T
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T15:17:33.083)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T15:17:33.083 / 2026-11-19T05:18:29.090
- **官方描述（原文）**：Dell PowerStore SDNAS contains an OS Command Injection vulnerability that could allow an attacker with internal network access to execute arbitrary commands as root on the NAS node.

### 106. CVE-2026-116446｜Dell / PowerStore 500T
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T15:17:32.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T15:17:32.780 / 2026-11-18T18:18:20.570
- **官方描述（原文）**：Dell PowerStore SDNAS contains an out-of-bounds memory vulnerability in the NAS NFS service that an unauthenticated remote attacker could exploit to cause a denial of service.

### 107. CVE-2026-116443｜Dell / PowerStore 500T
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:59.803)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:59.803 / 2026-11-19T05:18:28.783
- **官方描述（原文）**：Dell PowerStore SDNAS contains a stack-based buffer overflow in the NAS TFTP service that could allow an unauthenticated remote attacker to cause a denial of service or potential code execution.

### 108. CVE-2026-116441｜Dell / PowerStore 500T
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T17:17:28.430)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T17:17:28.430 / 2026-11-19T05:18:28.450
- **官方描述（原文）**：Dell PowerStore SDNAS contains an out-of-bounds write vulnerability in the storage-processor interconnect driver that could allow a malicious peer to execute code with system privileges.

### 109. CVE-2026-113425｜F5 / NGINX Plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:59.493)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:59.493 / 2026-11-19T05:18:25.493
- **官方描述（原文）**：When NGINX Plus or NGINX Open Source is configured as a mail proxy, undisclosed traffic can cause a use-after-free in an nginx worker process. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. Impact: A remote unauthenticated attacker may crash an nginx worker process or corrupt its memory, disrupting service. Remote code execution is a potential impact. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 110. CVE-2026-111508｜Dell / PowerStore 500T
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T12:17:01.917)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T12:17:01.917 / 2026-11-19T05:18:25.133
- **官方描述（原文）**：Dell PowerStore contains an OS Command Injection vulnerability. Exploitation could lead to arbitrary command execution with root privileges on the appliance.

### 111. CVE-2026-110811｜trustpayments / Trust Payments Gateway for WooCommerce (JavaScript Library)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T14:17:26.020)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T14:17:26.020 / 2026-11-18T16:17:59.137
- **官方描述（原文）**：The Trust Payments Gateway for WooCommerce (JavaScript Library) plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 1.3.8. The vulnerability exists because the `new_customer_account()` function stores the raw return value of `wp_create_user()` — including a `WP_Error` object returned on username collision — into the order's `tp_userid` post meta before the `is_wp_error()` guard is evaluated; the `add_customer_details_to_thankyou_page()` callback subsequently reads that meta and casts it with `(int)`, causing PHP to coerce any object to integer `1`, after which `wp_set_current_user(1)` and `wp_set_auth_cookie(1)` are called unconditionally. This makes it possible for unauthenticated attackers to authenticate as WordPress user ID 1 — the bootstrap site administrator or, on multisite, a network super-admin — by supplying the `new_username` parameter matching any existing login during checkout and visiting the resulting thank-you page. Exploitation requires the Trust Payments gateway to be active and the attacker to complete a paid order on their own account; the ID 1 administrator username is additionally enumerable via standard WordPress user enumeration techniques.

### 112. CVE-2026-110486｜Eclipse Foundation / Eclipse Mosquitto
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T11:17:37.963)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T11:17:37.963 / 2026-11-18T11:17:37.963
- **官方描述（原文）**：In Eclipse Mosquitto versions 2.1 through 2.1.2, a listener configured with `protocol websockets` mishandles empty WebSocket data frames. `net__read_ws()` in `lib/net_ws.c` returns the number of framing bytes consumed (the 4 masking-key bytes) for a data frame with a zero-length payload, without writing any bytes to the caller’s buffer. The MQTT packet reader in `packet__read_single()` (`lib/packet_mosq.c`) trusts that return value as a payload byte count. A remote client can therefore advance the read position over an uninitialised heap allocation, causing the broker to process and forward uninitialised heap memory (information disclosure, including heap and libc pointers), and can underflow the unsigned `to_process` counter so that subsequent attacker-controlled frame data is written past the end of the allocation (heap out-of-bounds write). The out-of-bounds write is reachable from the CONNECT packet before any authentication check, so an unauthenticated client can corrupt the heap and crash the broker even when `allow_anonymous false` is set. Combining the disclosure and the write allows remote code execution as the broker’s user by any client able to establish a session.

### 113. CVE-2026-110461｜Comelit Group S.p.A. / 1456B Multi-User Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-19T07:17:08.770)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-19T07:17:08.770 / 2026-11-19T07:17:08.770
- **官方描述（原文）**：The Comelit 1456B Multi-User Gateway, in firmware versions up to and including 2.10.0, is configured with static default passwords for multiple privileged roles. None of these passwords are required to be changed during initial configuration, and they remain at their default values unless the administrator changes them manually. An attacker with network access to the device can authenticate using these default credentials and gain administrative control.

### 114. CVE-2026-110009｜unzerplugins / Unzer Payments
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T14:17:25.860)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T14:17:25.860 / 2026-11-18T23:17:16.233
- **官方描述（原文）**：The Unzer Payments plugin for WordPress is vulnerable to Authentication Bypass leading to Account Takeover in all versions up to, and including, 2.2.1. The vulnerability exists because the Google Pay Express Checkout endpoint (`/?wc-api=google_pay_express`), handled by `startCheckoutDataWithNormalizedCustomerData`, accepts an attacker-controlled `paymentData.email` value and passes it to `createOrGetGuestCustomer()`, which resolves the submitted email to any existing WordPress user via `get_user_by('email', ...)` and then calls `wp_set_current_user()` and `wp_set_auth_cookie()` for the resolved user ID without verifying ownership of the email address, a password, a nonce, an authentication token, or any proof of payment from the payment provider. This makes it possible for unauthenticated attackers to log in as any existing WordPress user — including administrators — by submitting that user's known email address, receiving valid `wordpress_logged_in_*` session cookies for the targeted account and achieving full site takeover. The endpoint is entirely unprotected with no capability check, nonce validation, or payment-provider signature verification applied, and administrator email addresses are frequently discoverable via the WordPress REST API user enumeration endpoint (`/wp-json/wp/v2/users`), author archive pages, Gravatar lookups, or site contact footers.

### 115. CVE-2026-109857｜CAST Software / Imaging
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T13:17:23.637)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T13:17:23.637 / 2026-11-18T21:17:44.847
- **官方描述（原文）**：CAST Imaging is vulnerable to authentication bypass in the TenantFilter class. The TenantFilter processes the X-ISSUER-LOCATION HTTP header and dynamically registers an OpenID Connect issuer based on its value. An unauthenticated remote attacker can register a malicious identity provider, create users matching existing administrative usernames, and obtain valid JWTs which will be accepted by the application. This results in complete authentication bypass and privilege escalation to administrative access. The vulnerability has only been confirmed in version 3.6.2 but may also affect other versions. The vendor did not provide the affected version range, but assured that the vulnerability is fixed "in newer versions".

### 116. CVE-2023-54422｜iDocView / iDocView
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:54.023)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:54.023 / 2026-11-18T18:17:33.457
- **官方描述（原文）**：iDocView before 13.10.1_20231115 contains an unrestricted file upload vulnerability in the /html/2word endpoint that allows unauthenticated attackers to write arbitrary files by supplying a malicious url parameter. Attackers can send a crafted GET request with the url parameter to download linked resources with an unsanitized path and unblocked .jsp extension, achieving remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-11-22.

### 117. CVE-2018-25443｜Baidu / UEditor
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:48.500)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:48.500 / 2026-11-18T16:17:48.500
- **官方描述（原文）**：Baidu UEditor 1.4.0 through 1.4.3.3 contains an unrestricted file upload vulnerability in the catchimage action of /ueditor/net/controller.ashx that only validates the Content-Type header. Unauthenticated attackers can supply a source[] URL like x.jpg?.aspx to retain a malicious extension and write an executable .aspx file for remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-17.

### 118. CVE-2012-20007｜TopThink / ThinkPHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:47.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:47.560 / 2026-11-18T16:17:47.560
- **官方描述（原文）**：ThinkPHP 2.0 through 2.2 and 3.0 Lite mode contains an eval injection vulnerability in the Dispatcher PATH_INFO parsing, which uses preg_replace with the /e modifier and a double-quoted replacement. Unauthenticated attackers can send crafted requests to index.php with a malicious 's' parameter containing PHP expressions to execute arbitrary code on the server. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 119. CVE-2026-73504｜ing-bank / cassandra-jdbc-wrapper
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T20:19:12.780)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T20:19:12.780 / 2026-11-18T21:18:01.700
- **官方描述（原文）**：cassandra-jdbc-wrapper provides a JDBC-compliant API over the Java driver for Apache Cassandra. Prior to 4.16.4 and 5.0.2, DriverUtil.toStringWithoutSensitiveValues() and DriverUtil.redactSensitiveValuesInJdbcUrl() redact the password property but not the equally sensitive token property used for DataStax Astra and other token-based authentication. When DEBUG logging is enabled, SessionHolder passes connection properties and JDBC URLs containing token through these helpers, causing the live token to be written in plaintext when connections are acquired or released. An attacker who can read those logs can use the token to access Cassandra data and operations authorized to that credential. This issue is fixed in versions 4.16.4 and 5.0.2.

### 120. CVE-2026-63483｜nordic-institute / X-Road
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T20:19:10.703)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.6 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T20:19:10.703 / 2026-11-18T21:18:00.917
- **官方描述（原文）**：X-Road is open-source data exchange layer software. Prior to 7.8.2 and 7.7.3, the Configuration Proxy uses attacker-controlled Content-location metadata from a validly signed federated global configuration part when constructing an output path without verifying that the resulting path remains inside the intended configuration output directory. A malicious or compromised federated ecosystem can provide an absolute path or directory traversal sequence during the normal refresh cycle, causing the Configuration Proxy to create a new file with attacker-controlled content under the permissions of the non-privileged xroad process. The vulnerability can poison downstream global configuration or create files in other writable locations, but it does not overwrite existing files. This issue is fixed in versions 7.8.2 and 7.7.3.

### 121. CVE-2026-132123｜modified-shop / modified-shop
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T13:17:27.617)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 4.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T13:17:27.617 / 2026-11-18T14:17:44.207
- **官方描述（原文）**：modified eCommerce Shopsoftware through 3.3.0 contains a stored cross-site scripting vulnerability that allows authenticated administrators to inject scripts via the cross_sell_group_name parameter in admin/cross_sell_groups.php. Attackers with per-page access to cross-selling groups can store a script payload that executes in other administrators' browsers, including full administrators, when they view the group listing.

### 122. CVE-2026-132122｜splx-ai / agentic-radar
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T13:17:27.467)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.7 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T13:17:27.467 / 2026-11-18T18:19:15.097
- **官方描述（原文）**：agentic-radar 0.7.0 before 0.14.2 contains an untrusted configuration loading vulnerability that allows malicious repositories to inject environment variables by having load_dotenv() in agentic_radar/cli.py load the scanned repository's .env file. Attackers can set OPENAI_BASE_URL to an attacker-controlled host so that scan openai-agents or --harden-prompts send requests carrying the user's OpenAI API key to the attacker.

### 123. CVE-2026-132049｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T11:17:38.660)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T11:17:38.660 / 2026-11-18T19:17:57.850
- **官方描述（原文）**：A flaw was found in lldpd. The service fails to verify that Link Layer Discovery Protocol - Media Endpoint Discovery (LLDP-MED) location records received from network neighbors match their declared lengths. An adjacent attacker on the local network can exploit this flaw by sending crafted packets, causing client applications using the liblldpctl library to read past buffer boundaries when parsing location data. This issue can lead to an information disclosure of adjacent process memory.

### 124. CVE-2026-130789｜SemanticMediaWiki / SemanticMediaWiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:55.657)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:55.657 / 2026-11-18T21:17:50.887
- **官方描述（原文）**：SemanticMediaWiki from 7.3.0 before 7.4.0 contains a missing authorization vulnerability in the smwtask API check-query task that allows unauthenticated attackers to bypass object-level authorization by relying on the wiki-wide edit right. Attackers can supply arbitrary subject titles, including protected pages, to run synchronous Semantic MediaWiki queries with caller-controlled conditions, limit, offset, and querymode parameters.

### 125. CVE-2026-130777｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:53.163)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:53.163 / 2026-11-18T21:17:50.527
- **官方描述（原文）**：Incus before 7.6.0 contains an information disclosure vulnerability that allows project-restricted authenticated clients to receive other projects' OVN ACL logs because these events are broadcast with an empty project. Attackers can subscribe to network-acl events on one accessible project to observe internal IPs, ports, protocols, and allow/drop decisions across all projects.

### 126. CVE-2026-128717｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T15:17:35.050)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T15:17:35.050 / 2026-11-18T19:17:40.393
- **官方描述（原文）**：An issue in PHPGurukul Employee Leaves Management System (ELMS) Version 2.1 allows a remote attacker to escalate privileges via the PHP session management mechanism

### 127. CVE-2026-128665｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T19:17:40.160)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T19:17:40.160 / 2026-11-18T21:17:48.330
- **官方描述（原文）**：A stored cross-site scripting (XSS) vulnerability in the Public News Article Rendering Module of PHPGurukul News Portal Project v4.1 allows authenticated attackers with administrative or sub-administrative privileges to inject arbitrary HTML and JavaScript through the postdescription parameter when creating or editing news articles. The application renders the stored post content without proper output encoding in news-details.php, allowing injected JavaScript to execute in the browsers of users who visit the affected article.

### 128. CVE-2022-51031｜PMB Services / PMB
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:52.230)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:52.230 / 2026-11-18T17:17:25.287
- **官方描述（原文）**：PMB 7.3.1 before 7.3.15 and 7.4.x before 7.4.5 contains a reflected cross-site scripting vulnerability that allows unauthenticated attackers to inject script through unescaped POST parameter names. Attackers can send crafted parameter names to opac_css/index.php extended_search, which empr.inc.php and languages.inc.php reflect into hidden form inputs to execute JavaScript. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-23.

### 129. CVE-2021-48028｜Public Knowledge Project / Open Journal Systems
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:51.407)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:51.407 / 2026-11-18T18:17:32.883
- **官方描述（原文）**：Open Journal Systems 2.1.0 before 3.0.0 contains an open redirect vulnerability that allows unauthenticated attackers to redirect users to external domains by abusing the source parameter. Attackers can send GET requests to /index.php/index/user/setLocale/<locale> with a source value beginning with '@', which UserHandler.inc.php appends to the server host, redirecting victims to attacker-controlled sites for phishing. Exploitation evidence was first observed by the Shadowserver Foundation on 2024-12-05.

### 130. CVE-2019-25783｜Tiny Tiny RSS / Tiny Tiny RSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:48.843)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:48.843 / 2026-11-18T17:17:24.457
- **官方描述（原文）**：Tiny Tiny RSS before commit c68ac04 (2019-03-03) contains an open redirect vulnerability that allows unauthenticated attackers to redirect users through the unvalidated 'return' parameter. Attackers can craft requests to /public.php?op=login with an absolute external URL in 'return', which is placed in the Location header to send victims to attacker-controlled sites. Exploitation evidence was first observed by the Shadowserver Foundation on 2026-02-26.

### 131. CVE-2010-20126｜Daniel K. Imori / Virtual Keyboard plugin for SquirrelMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T16:17:46.437)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T16:17:46.437 / 2026-11-18T17:17:22.250
- **官方描述（原文）**：Virtual Keyboard plugin for SquirrelMail through 0.9.1 contains a reflected cross-site scripting vulnerability that allows unauthenticated attackers to inject script by supplying unsanitized input in the passformname parameter. Attackers can craft GET requests to /plugins/vkeyboard/vkeyboard.php with script payloads in passformname to execute code in victims' browsers and steal session cookies. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-23.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-90817｜Vanderbilt University / Research Electronic Data Capture (REDCap)
- **Title**：Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.03749 / percentile=0.90092
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-11-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Vanderbilt University Research Electronic Data Capture (REDCap) contains a code injection vulnerability which could allow an unauthenticated attacker to execute arbitrary code on the server. An attacker could exploit this via crafted HTTP requests that access an unintended controller route from a public survey context and supply a crafted file-path or stream parameter during data import processing. Exploitation requires knowledge of a valid public survey hash.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-90436｜Apache / Axis
- **Title**：Apache Axis Unsafe Reflection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01128 / percentile=0.67007
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-11-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apache Axis contains an unsafe reflection vulnerability that could allow an unauthenticated remote attacker to execute arbitrary code via a crafted SOAP fault message that causes Axis to load and instantiate an attacker-specified class when a suitable class is available on the application classpath. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-40217｜BerriAI / LiteLLM
- **Title**：BerriAI LiteLLM Unprotected Alternate Channel Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.1702 / percentile=0.97134
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-12-02
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：BerriAI LiteLLM contains an unprotected alternate channel vulnerability that could allow remote attackers to execute arbitrary code via bytecode rewriting at the /guardrails/test_custom_code URI.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2024-10441｜Synology / DiskStation Manager (DSM)
- **Title**：Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01251 / percentile=0.70014
- **CISA KEV**：listed=true / date_added=2026-11-18 / due_date=2026-11-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Synology DSM contains an improper encoding or escaping of output vulnerability in the system plugin daemon in Synology BeeStation OS (BSM) that could allow a remote attacker to execute arbitrary code via unspecified vectors.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-116779｜SignalWire / FreeSwitch
- **Title**：SignalWire FreeSwitch Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.22081 / percentile=0.97713
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：SignalWire FreeSwitch contains a code injection vulnerability that permits configuration and credential disclosure, arbitrary call control, and command execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-76807 | P3 / 38 | Doist / todoist-mcp | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-130682 | P3 / 38 | siyuan-note / siyuan | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-130678 | P3 / 38 | siyuan-note / siyuan | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-130650 | P3 / 38 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-130648 | P3 / 38 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-130156 | P3 / 38 | morpheus65535 / bazarr | v3.1 9.4 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-126755 | P3 / 38 | ArangoDB / ArangoDB | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-126752 | P3 / 38 | dagu-org / Dagu | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2023-54419 | P3 / 38 | cym1102 / nginxWebUI | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2022-51027 | P3 / 38 | FIT2CLOUD / MeterSphere | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2021-48025 | P3 / 38 | Jiaxing Xiangtian Information Technology / OpenSNS | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2021-48023 | P3 / 38 | Weaver Network Co., Ltd. / E-cology | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2019-25782 | P3 / 38 | TopThink / ThinkPHP | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2016-20105 | P3 / 38 | Lucee / Lucee Server | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-76100 | WATCH / 30 | own-pay / OwnPay | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-59975 | WATCH / 30 | danielklecha / SharpIppNext | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-30502 | WATCH / 30 | 未確認 / 未確認 | v3.1 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-130753 | WATCH / 30 | heymrun / heym | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-128669 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-128664 | WATCH / 30 | 未確認 / 未確認 | v3.1 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2022-51034 | WATCH / 30 | Tangshan Pingsheng Electronic Technology Development Co., Ltd. / Reservoir Safety Supervision Platform | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2022-51030 | WATCH / 30 | Qibosoft / QiboCMS | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2016-20106 | WATCH / 30 | NUUO / NVRmini 2 | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-95787 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95645 | WATCH / 28 | Zohocorp / DDI Central | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：3；缺少 Product：3；缺少 Title：25。
- EPSS 未確認：25；Exploitation status 未確認：0。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-19T08:11:03.488229+00:00`；Delta generated at：`2026-11-19T08:11:03.488229+00:00`。

---

## 可驗證資料來源

- **CVE-2026-90817** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90817) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90817) · [Vendor / Advisory (projectredcap.org)](https://projectredcap.org/resources/community) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-90436** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90436) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90436) · [Vendor / Advisory (lists.apache.org)](https://lists.apache.org/thread/8slf0j9gz35z56t0glt5h0ncwlbn4bdz) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-40217** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-40217) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-40217) · [Vendor / Advisory (github.com)](https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2024-10441** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-10441) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2024-10441) · [Vendor / Advisory (synology.com)](https://www.synology.com/zh-tw/security/advisory/Synology_SA_24_20) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-116779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116779) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116779) · [Vendor / Advisory (github.com)](https://github.com/signalwire/freeswitch/security/advisories/GHSA-mg63-h38w-8p9p) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-76807** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76807)
- **CVE-2026-130682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130682)
- **CVE-2026-130678** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130678)
- **CVE-2026-130650** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130650)
- **CVE-2026-130648** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130648)
- **CVE-2026-130156** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130156)
- **CVE-2026-126755** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126755)
- **CVE-2026-126752** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126752)
- **CVE-2023-54419** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-54419)
- **CVE-2022-51027** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-51027)
- **CVE-2021-48025** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-48025)
- **CVE-2021-48023** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-48023)
- **CVE-2019-25782** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-25782)
- **CVE-2016-20105** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-20105)
- **CVE-2026-76100** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76100)
- **CVE-2026-59975** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59975)
- **CVE-2026-30502** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-30502)
- **CVE-2026-130753** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130753)
- **CVE-2026-128669** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128669)
- **CVE-2026-128664** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128664)
- **CVE-2022-51034** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-51034)
- **CVE-2022-51030** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-51030)
- **CVE-2016-20106** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-20106)
- **CVE-2026-95787** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95787)
- **CVE-2026-95645** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95645)
- **CVE-2026-95643** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95643)
- **CVE-2026-77297** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77297)
- **CVE-2026-77296** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77296)
- **CVE-2026-75521** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75521)
- **CVE-2026-73969** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73969)
- **CVE-2026-71499** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71499)
- **CVE-2026-63413** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63413)
- **CVE-2026-63412** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63412)
- **CVE-2026-63411** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63411)
- **CVE-2026-63189** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63189)
- **CVE-2026-61532** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61532)
- **CVE-2026-55508** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55508)
- **CVE-2026-55506** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55506)
- **CVE-2026-55171** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55171)
- **CVE-2026-19707** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19707)
- **CVE-2026-132808** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132808)
- **CVE-2026-132807** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132807)
- **CVE-2026-132804** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132804)
- **CVE-2026-132803** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132803)
- **CVE-2026-132802** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132802)
- **CVE-2026-132622** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132622)
- **CVE-2026-132234** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132234)
- **CVE-2026-132233** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132233)
- **CVE-2026-132232** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132232)
- **CVE-2026-132231** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132231)
- **CVE-2026-132209** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132209)
- **CVE-2026-132208** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132208)
- **CVE-2026-131914** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131914)
- **CVE-2026-130786** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130786)
- **CVE-2026-130784** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130784)
- **CVE-2026-130783** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130783)
- **CVE-2026-130780** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130780)
- **CVE-2026-130778** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130778)
- **CVE-2026-130774** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130774)
- **CVE-2026-130773** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130773)
- **CVE-2026-130770** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130770)
- **CVE-2026-130759** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130759)
- **CVE-2026-130757** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130757)
- **CVE-2026-130756** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130756)
- **CVE-2026-130754** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130754)
- **CVE-2026-130747** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130747)
- **CVE-2026-130735** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130735)
- **CVE-2026-130733** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130733)
- **CVE-2026-130730** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130730)
- **CVE-2026-130716** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130716)
- **CVE-2026-130712** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130712)
- **CVE-2026-130706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130706)
- **CVE-2026-130683** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130683)
- **CVE-2026-130681** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130681)
- **CVE-2026-130680** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130680)
- **CVE-2026-130679** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130679)
- **CVE-2026-130675** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130675)
- **CVE-2026-130674** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130674)
- **CVE-2026-130154** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130154)
- **CVE-2026-129991** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129991)
- **CVE-2026-129989** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129989)
- **CVE-2026-129987** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129987)
- **CVE-2026-129986** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129986)
- **CVE-2026-129961** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129961)
- **CVE-2026-129316** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129316)
- **CVE-2026-127143** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127143)
- **CVE-2026-124990** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124990)
- **CVE-2026-123637** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123637)
- **CVE-2026-123634** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123634)
- **CVE-2026-123633** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123633)
- **CVE-2026-123007** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123007)
- **CVE-2026-121810** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121810)
- **CVE-2026-121805** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121805)
- **CVE-2026-120722** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120722)
- **CVE-2026-120718** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120718)
- **CVE-2026-120292** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120292)
- **CVE-2026-120285** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120285)
- **CVE-2026-116953** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116953)
- **CVE-2026-116449** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116449)
- **CVE-2026-116448** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116448)
- **CVE-2026-116446** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116446)
- **CVE-2026-116443** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116443)
- **CVE-2026-116441** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116441)
- **CVE-2026-113425** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113425)
- **CVE-2026-111508** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111508)
- **CVE-2026-110811** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110811)
- **CVE-2026-110486** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110486)
- **CVE-2026-110461** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110461)
- **CVE-2026-110009** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110009)
- **CVE-2026-109857** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109857)
- **CVE-2023-54422** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-54422)
- **CVE-2018-25443** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2018-25443)
- **CVE-2012-20007** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2012-20007)
- **CVE-2026-73504** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73504)
- **CVE-2026-63483** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63483)
- **CVE-2026-132123** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132123)
- **CVE-2026-132122** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132122)
- **CVE-2026-132049** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132049)
- **CVE-2026-130789** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130789)
- **CVE-2026-130777** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130777)
- **CVE-2026-128717** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128717)
- **CVE-2026-128665** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128665)
- **CVE-2022-51031** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-51031)
- **CVE-2021-48028** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-48028)
- **CVE-2019-25783** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-25783)
- **CVE-2010-20126** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2010-20126)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
