# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**54** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=54。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **3**、WATCH **27**。
- Baseline：state / generated_at=2026-11-05T07:35:16.367660+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **54** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-48705｜Project-MONAI / MONAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T21:18:50.270)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T21:18:50.270 / 2026-11-05T22:18:44.013
- **官方描述（原文）**：MONAI (Medical Open Network for AI) is an AI toolkit for health care imaging. Prior to 1.6.1, PydicomReader._get_affine() trusts non-finite values in the DICOM PixelSpacing, ImagePositionPatient, and ImageOrientationPatient fields and composes them into an affine matrix without validation. An unauthenticated attacker who can upload a crafted DICOM to a default MONAILabel deployment can propagate NaN or infinity values through LoadImaged, Spacingd, model inference, and output writing, causing inference failures, persistent datastore poisoning, or geometrically corrupted results. This issue is fixed in version 1.6.1.

### 2. CVE-2026-123198｜LMFDB / LMFDB
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T19:17:18.393)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T19:17:18.393 / 2026-11-05T21:18:45.820
- **官方描述（原文）**：LMFDB before commit 01829bd contains a server-side template injection vulnerability in the render_knowl function that allows unauthenticated attackers to inject Jinja expressions via request parameters. Attackers can supply crafted query-string values or 'content' data to /knowledge/render/<ID> to reach Python builtins and execute operating system commands as the web application account.

### 3. CVE-2026-102940｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T20:17:37.543)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T20:17:37.543 / 2026-11-05T21:18:34.653
- **官方描述（原文）**：OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.4.0, controllers/C_Document.class.php write actions, including move_action_process(), do not verify the caller's access to the source document, current patient and category, or destination patient and category before Document::change_patient() performs the mutation. A low-privilege authenticated user can reassign an arbitrary document to a patient or category the user can access and then retrieve it through the normally protected read path. The reassignment occurs before a later list rendering check, so a final HTTP 403 response does not mean the unauthorized write was blocked. This issue is fixed in version 8.4.0.

### 4. CVE-2026-87008｜vitali87 / code-graph-rag
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T21:18:54.370)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T21:18:54.370 / 2026-11-05T21:18:54.370
- **官方描述（原文）**：Code Graph RAG is an AI-powered knowledge graph and retrieval system for querying, understanding, and editing multi-language codebases. Prior to 0.0.589, AstGrepService in codebase_rag/tools/ast_grep_service.py enumerates files beneath project_root and relies on should_skip_path in codebase_rag/utils/path_utils.py to classify them, but the containment check operates on unresolved lexical paths. A symbolic link planted inside an analyzed repository can therefore reference a file outside the configured root while still appearing in scope. The structural_search tool follows the link and discloses readable content without an approval gate, while structural_replace with dry_run=False follows it and overwrites writable content; the MCP path invokes structural replacement without the agent-loop approval control. An attacker who causes a victim to analyze a repository containing such a link can read credentials, keys, environment files, or sibling source and can modify files accessible to the code-graph-rag process. This issue is fixed in version 0.0.589.

### 5. CVE-2026-75614｜esa / asn1scc
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T17:18:20.497)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T17:18:20.497 / 2026-11-05T19:17:26.937
- **官方描述（原文）**：ASN1SCC is an open source ASN.1 compiler for embedded systems. Prior to 4.7.0.1, BitStream_DecodeConstraintWholeNumber in asn1crt/asn1crt_encoding.c reads enough bits for a constrained integer but does not reject values above the declared range when the encoded range is not a power of two. Generated uPER and ACN decoders for variable-size SEQUENCE OF, OCTET STRING, BIT STRING, and string values use the invalid result as a loop or copy length, so a crafted over-range size field can write beyond a destination buffer. Decoding untrusted affected data can corrupt heap or stack memory, cause a crash, or potentially permit code execution. This issue is fixed in version 4.7.0.1.

### 6. CVE-2026-54912｜bytecodealliance / wasm-micro-runtime
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T18:17:08.523)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T18:17:08.523 / 2026-11-05T19:17:21.520
- **官方描述（原文）**：WebAssembly Micro Runtime (WAMR) is a lightweight standalone WebAssembly (Wasm) runtime. Prior to 2.4.5, the two-pass fast interpreter loader in core/iwasm/interpreter/wasm_loader.c can make inconsistent constant-table decisions between the sizing pass and the emitting pass. After duplicate constants inflate the first pass beyond the constant-slot limit, wasm_loader_get_const_offset emits later constants inline, but the between-pass sort and deduplication reduces the table so the second pass can choose table references and cause reserve_block_ret to emit additional copy operands that were not included in code_compiled_peak_size. A crafted module can therefore make the second pass write partially attacker-controlled compiled-code data beyond the heap buffer allocated from the first pass's size calculation during wasm_runtime_load, before guest code executes. This can corrupt host heap metadata and deterministically crash the process, causing denial of service; further consequences depend on the host application's heap layout. Builds using WAMR_BUILD_FAST_INTERP=1 are affected; disabling the fast interpreter avoids the vulnerable loader. This issue is fixed in version 2.4.5.

### 7. CVE-2026-54142｜tinyhumansai / openhuman
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T17:18:19.303)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T17:18:19.303 / 2026-11-05T19:17:21.320
- **官方描述（原文）**：OpenHuman is an open-source agent harness available as a desktop application and Rust library. Before 0.57.13, background synchronization for connected services such as email, Slack, and Notion stores raw external content and later places it in the model context of autonomous background agents without neutralizing embedded instructions. ApprovalGate treats tool calls without an interactive chat context as pre-authorized automation, so attacker-authored content processed during a background tick can influence the model to invoke Composio actions without presenting an approval request. An attacker who can deliver content to a connected account can use this path to send or forward data, post messages, create or modify third-party content, or disclose information from OpenHuman memory and integrations. The issue requires an active integration and successful model interpretation of the injected instructions. This issue is fixed in version 0.57.13.

### 8. CVE-2026-49272｜oauthlib / oauthlib
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T21:18:50.447)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T21:18:50.447 / 2026-11-05T22:18:44.593
- **官方描述（原文）**：OAuthLib is an implementation of the OAuth request-signing logic for Python 3.6+. From 3.3.0 until 4.0.1, OAuthLib's RFC 8628 device workflow does not require DeviceCodeGrant.validate_token_request to check that the device_code parameter is present and valid. A caller whose client request is accepted by the configured validator and who knows a valid client ID enabled for the device workflow can submit a missing or bogus device code to the token endpoint and obtain a bearer token without completing device authorization. This issue is fixed in version 4.0.1.

### 9. CVE-2026-123158｜OpenBSD / OpenSSH
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T16:17:47.110)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T16:17:47.110 / 2026-11-06T05:18:26.710
- **官方描述（原文）**：sshd in OpenSSH before 10.6p2 on Linux, when musl libc is used without PAM, lacks a workaround for a password authentication bypass (related to misinterpretation of whether a string is intended to be a password hash). For some configurations of accounts, any password between 256 and 1024 characters succeeds. An example of a platform using musl libc without PAM is Alpine Linux.

### 10. CVE-2026-120499｜h5io / h5io
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T17:18:00.097)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T17:18:00.097 / 2026-11-05T19:17:14.713
- **官方描述（原文）**：h5io before 0.2.6 contains a code injection vulnerability in read_hdf5() that allows attackers to execute arbitrary code by supplying a crafted HDF5 file. Attackers can store Python code in a node titled timezone, which _triage_read() passes to eval() with builtins reachable, name an arbitrary module in class or custom-object nodes that _import_class() imports, or place pickled objects in pd_dataframe or pd_series nodes that pandas deserializes on read.

### 11. CVE-2026-115573｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T20:17:42.803)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T20:17:42.803 / 2026-11-05T21:18:37.230
- **官方描述（原文）**：OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.3.0, library/classes/Controller.class.php allows explicit controller.php dispatch to controllers missing from CONTROLLER_ACL_MAP, and checkControllerAcl() returns without enforcing any permission for those entries. A low-privilege authenticated user can invoke C_X12Partner::edit_action_process() to create or alter insurance-routing hosts and credentials, or invoke C_PatientFinder::find_action_process() to enumerate patient names, dates of birth, and identifiers. The shared fail-open dispatcher root cause also exposes other administrative controllers that were intended to be reached through ACL-gated Practice Settings routes. This issue is fixed in version 8.3.0.

### 12. CVE-2026-96677｜Apache Software Foundation / Apache Juneau
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T12:17:51.620)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T12:17:51.620 / 2026-11-05T15:01:29.553
- **官方描述（原文）**：Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Juneau. HTML document serialization does not HTML-encode variable substitutions in the page chrome (header, nav, aside, footer and similar fields). Applications whose chrome includes request-derived variables, such as request headers, form data or path values, reflect those values unencoded, allowing cross-site scripting. The default chrome does not use request variables, so only applications that add them are affected. This issue affects Apache Juneau: through 9.2.0. Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### 13. CVE-2026-85076｜jhuckaby / Cronicle
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T21:18:54.217)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T21:18:54.217 / 2026-11-05T21:18:54.217
- **官方描述（原文）**：Cronicle is a multi-server task scheduler and runner, with a web based front-end UI. Prior to 0.9.124, an authenticated non-admin with run_events, create_events, or edit_events privilege can supply undeclared keys in event params through api_create_event, api_update_event, or api_run_event. lib/api.js and lib/api/event.js validate the parameter object without restricting its keys, and lib/job.js uppercases those keys and applies them to the child process environment after administrator-defined plugin variables. A key that collides with a security-sensitive environment variable can therefore override the plugin execution context and may cause privilege escalation, arbitrary code execution, data access, or service disruption depending on the plugin and runtime. This issue is fixed in version 0.9.124.

### 14. CVE-2026-83542｜Apache Software Foundation / Apache OFBiz
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T14:17:06.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T14:17:06.820 / 2026-11-06T05:18:36.020
- **官方描述（原文）**：Improper Control of Generation of Code ('Code Injection') in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote unauthenticated attacker to execute arbitrary code on the server by staging crafted widget XML in a multipart upload and overriding the mainDecoratorLocation used by a manager login route through an anonymous JSON request, causing OFBiz to load the staged XML through its live screen descriptor mechanism and evaluate an unsandboxed Groovy expression while rendering the authentication-failure page. Further validation established the following: -- The exploit does not require a malformed or incomplete multipart body: a well-formed multipart request that is kept in flight and then allowed to complete normally is sufficient. -- The screen loader reads the widget XML from a live process file descriptor while the upload is streaming, rather than from any file the attacker persists to disk. -- The same underlying issue is also reachable through the public, explicitly unauthenticated /sfa/control/editPortalPageColumnWidth route, returning command output directly in an HTTP 200 response — it is not limited to the login-failure rendering path used in the original report. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### 15. CVE-2026-82907｜Apache Software Foundation / Apache OFBiz
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T14:17:05.700)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T14:17:05.700 / 2026-11-06T05:18:30.963
- **官方描述（原文）**：Authentication Bypass by Capture-replay in ExternalLoginKeysManager in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote unauthenticated attacker who captures a live externalLoginKey value to obtain a complete, cookie-free, reusable session as the user who issued it, in every webapp that user can reach, because checkExternalLoginKey runs as a global preprocessor ahead of both the CSRF and authentication checks and accepts the key as a bearer credential that is never bound to a client, never expires, and is not invalidated after use, while the framework itself both appends live keys to every cross-webapp link it renders and, via WidgetWorker's unvalidated inter-app link target, lets an authenticated user's key be attached to an attacker-chosen absolute URL and delivered directly to the attacker's own server. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### 16. CVE-2026-77596｜kubeflow / pipelines
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T23:17:00.767)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T23:17:00.767 / 2026-11-05T23:17:00.767
- **官方描述（原文）**：Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, the multi-user HTTP endpoints POST /apis/v2beta1/pipelines/upload and POST /apis/v2beta1/pipelines/upload_version call canUploadVersionedPipeline, which returns without SubjectAccessReview when the target namespace is empty while REQUIRE_NAMESPACE_FOR_PIPELINES defaults to false. A low-privilege tenant can create shared pipelines or inject attacker-controlled versions into existing shared pipelines without the required write permission; if the API server is directly reachable without an authenticating proxy, an unauthenticated caller can exploit the same bypass, while deployments protected by such a proxy do not expose anonymous access. An enabled unpinned recurring run that follows the latest version can then execute the injected specification in another tenant's namespace under that workload's service account, while pinned or embedded-specification runs are not automatically substituted. This issue is fixed in version 2.18.0.

### 17. CVE-2026-73117｜Apache Software Foundation / Apache Juneau
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T12:17:51.473)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T12:17:51.473 / 2026-11-05T15:01:29.553
- **官方描述（原文）**：Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Response Splitting') vulnerability in Apache Juneau. The Apache Juneau REST server passed response header values and redirect targets to the servlet container unchecked. An application that sets a response header or redirect target from request data could let a remote client inject header lines (where the servlet container does not itself reject CR/LF) or redirect users to an arbitrary external site. The framework itself does not build headers or redirects from request data; exposure depends on application code. This issue affects Apache Juneau: through 9.2.0. Users are recommended to upgrade to version 9.2.1, which fixes the issue. Header values are now sanitized by default; applications that build redirect targets from request data must also switch from sendRedirect() to the new sendSafeRedirect().

### 18. CVE-2026-73116｜Apache Software Foundation / Apache Juneau
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T12:17:51.333)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T12:17:51.333 / 2026-11-05T15:01:29.553
- **官方描述（原文）**：Insufficiently Protected Credentials vulnerability in Apache Juneau. The Apache Juneau RestClient followed HTTP redirects while keeping credential headers from the original request, so a server that redirected the client to a different host or port, or from HTTPS to HTTP, could receive headers such as Authorization, Cookie, Proxy-Authorization and X-API-Key. This issue affects Apache Juneau: through 9.2.0. Users are recommended to upgrade to version 9.2.1, which fixes the issue. The fix applies to HTTP clients created by the RestClient builder; applications that supply their own HttpClient must disable automatic redirects or strip credential headers on cross-origin redirects themselves.

### 19. CVE-2026-73101｜Apache Software Foundation / Apache Juneau
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T12:17:51.197)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T12:17:51.197 / 2026-11-05T15:01:29.553
- **官方描述（原文）**：Generation of Error Message Containing Sensitive Information vulnerability in Apache Juneau. The REST server sends the internal exception class and message to clients in a "Thrown" response header on every error response, and can include internal exception messages in the error body, even when stack-trace rendering is disabled. This reveals implementation details to remote clients. This issue affects Apache Juneau: through 9.2.0. Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### 20. CVE-2026-73100｜Apache Software Foundation / Apache Juneau
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T12:17:51.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T12:17:51.060 / 2026-11-05T15:01:29.553
- **官方描述（原文）**：Insertion of Sensitive Information into Log File vulnerability in Apache Juneau. The default REST server call logger records request headers for requests that end in a server error, without redacting them. Any client able to cause a server error gets headers such as Authorization, Cookie, Proxy-Authorization and X-API-Key written in cleartext to the application log, exposing them to anyone who can read the logs. This issue affects Apache Juneau: through 9.2.0. Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### 21. CVE-2026-73099｜Apache Software Foundation / Apache Juneau
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T12:17:50.917)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T12:17:50.917 / 2026-11-05T19:17:26.810
- **官方描述（原文）**：Cross-Site Request Forgery (CSRF) vulnerability in Apache Juneau. The REST server accepts a "content" query parameter that replaces the request body, and this is enabled by default on every HTTP method, including GET. A cross-site link can therefore deliver an attacker-chosen request body to an endpoint without a CORS preflight, defeating protections that rely on the HTTP method or content type instead of an anti-CSRF token. This issue affects Apache Juneau: through 9.2.0. Users are recommended to upgrade to version 9.2.1, which fixes the issue. Applications that do not use the content parameter can also set disableContentParam to true.

### 22. CVE-2026-73098｜Apache Software Foundation / Apache Juneau
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T12:17:50.770)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T12:17:50.770 / 2026-11-05T19:17:26.667
- **官方描述（原文）**：Improper control of dynamically-loaded code vulnerability in Apache Juneau. When Apache Juneau parses a value into a property of type java.lang.Class (including parameterized forms), the default class swap loaded the named class with initialization enabled, so input naming a class on the application classpath ran that class's static initializer. The impact depends on the classes present in the deployment. This issue affects Apache Juneau: through 9.2.0. Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### 23. CVE-2026-71550｜SuiteCRM / SuiteCRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T19:17:26.357)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T19:17:26.357 / 2026-11-05T19:17:26.490
- **官方描述（原文）**：SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15.2 and 8.10.2, the workflow controller uses a path-traversal-capable aow_action value in require_once() without constraining the resolved file. The affected flow begins at modules/AOW_WorkFlow/controller.php and uses aow_action, and require_once() to carry attacker-controlled data or authorization state into the security-sensitive operation. An authenticated user with the WorkFlow role can include executable PHP, obtain server-side code execution, access CRM data and configuration secrets, and establish persistent access. This issue is fixed in versions 7.15.2 and 8.10.2.

### 24. CVE-2026-63774｜Subnet Solutions / PowerSYSTEM Center 2024
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T01:17:50.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T01:17:50.470 / 2026-11-06T01:17:50.470
- **官方描述（原文）**：Insufficient input validation in the PowerSYSTEM Center report designer allows an authenticated user to execute unauthorized SQL commands.

### 25. CVE-2026-63017｜Subnet Solutions / PowerSYSTEM Center 2020
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-06T01:17:50.297)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-06T01:17:50.297 / 2026-11-06T01:17:50.297
- **官方描述（原文）**：Incorrect authorization in PowerSYSTEM Center allows a low-privileged, authenticated user to access resources normally limited to administrators.

### 26. CVE-2026-54143｜tinyhumansai / openhuman
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T17:18:19.487)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T17:18:19.487 / 2026-11-05T17:18:19.487
- **官方描述（原文）**：OpenHuman is an open-source agent harness available as a desktop application and Rust library. Before version 0.57.13, an attacker who can send messages to a configured external channel can cause the agent to create persistent shell cron jobs without human approval. The scheduler later executes these jobs with the privileges of the OpenHuman runtime user. Command validation also permits leading environment assignments that can redirect allowed commands to executable helpers. The demonstrated exploit requires a suitable helper executable already present on the host. This can lead to unauthorized persistent command execution and compromise data and resources accessible to OpenHuman. This issue is fixed in version 0.57.13.

### 27. CVE-2026-54141｜tinyhumansai / openhuman
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T17:18:19.103)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T17:18:19.103 / 2026-11-05T17:18:19.103
- **官方描述（原文）**：OpenHuman is an open-source agent harness available as a desktop application and Rust library. Before 0.57.13, a remote direct message received through a configured Yuanbao channel is converted into a generic channel AgentTurnRequest that uses the default tool policy without establishing an interactive approval context. Under the default Supervised autonomy policy with Node enabled, node_exec is classified as a write operation that should prompt for approval, but ApprovalGate treats missing APPROVAL_CHAT_CONTEXT as a non-interactive turn and allows execution. Because Yuanbao direct messages are open by default, an external sender who can message the connected bot can influence the agent to execute JavaScript and operating-system commands as the OpenHuman user without an approval prompt. The issue requires a configured Yuanbao channel, the default approval-requiring policy state, Node availability, and successful model selection of node_exec. This issue is fixed in version 0.57.13.

### 28. CVE-2026-46350｜dcmjs-org / dcmjs
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T21:18:50.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T21:18:50.110 / 2026-11-05T21:18:50.110
- **官方描述（原文）**：dcmjs is a JavaScript implementation of DICOM manipulation. Prior to 0.52.0, the DecimalString and IntegerString implementations in src/ValueRepresentation.js sanitize text with a permissive regular expression and pass the result to JavaScript's Number constructor without validating finiteness or the DICOM value-representation rules. Scientific notation overflow in a DS or IS field can produce positive or negative Infinity, while stripping alphabetic characters from signed infinity text can leave a sign-only string that converts to NaN. IntegerString also accepts exponent notation and values outside the DICOM signed 32-bit IS range. Applications that trust these parsed values can propagate invalid numbers into spatial geometry, display windowing, dose scaling, frame counts, rescaling, or volume reconstruction, causing incorrect calculations or disrupted processing. This issue is fixed in version 0.52.0.

### 29. CVE-2026-121489｜Apache Software Foundation / Apache Juneau
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T12:17:49.643)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T12:17:49.643 / 2026-11-05T15:01:29.553
- **官方描述（原文）**：Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Juneau. The microservice DirectoryResource does not keep request paths inside its configured root directory. When an application enables the resource's view, upload or delete settings (all off by default), a client can read, write or delete files outside the root, anywhere the server process has access. This issue affects Apache Juneau: through 9.2.0. Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### 30. CVE-2026-119757｜BTCPay Server / BTCPay Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T22:17:53.203)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T22:17:53.203 / 2026-11-05T22:17:53.203
- **官方描述（原文）**：BTCPay Server before 2.4.2, including 2.4.2 release candidates, contains an information disclosure vulnerability that allows unauthenticated remote attackers to retrieve .macaroon credential files for an LND (Lightning Network Daemon) node. Attackers can use the exposed macaroon to gain full control of the LND node, including moving funds, resulting in theft of funds from affected deployments.

### 31. CVE-2026-119344｜ultravioletrs / cocos
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T16:17:40.373)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T16:17:40.373 / 2026-11-05T16:17:40.373
- **官方描述（原文）**：Cocos AI is a confidential computing system for AI. In version 0.8.2 and earlier, Cocos AI accepts trusted execution environment attestation Evidence when firmware patch levels and software measurements match, without binding the Evidence to an allowed platform owner or unique machine identity and without enforcing revocation. A remote attacker who controls or compromises another platform trusted by the same verifier can substitute valid Evidence from that platform and cause authorization of the wrong platform. This vulnerability is addressed in 0.9.0. However, this vulnerability can't be patched in source code alone, since the vulnerability arises from the confidential computing threat model itself.

### 32. CVE-2026-117691｜Red Hat / Red Hat Build of Keycloak
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T14:17:01.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T14:17:01.320 / 2026-11-05T17:17:44.750
- **官方描述（原文）**：A flaw was found in the SAML HTTP-Redirect binding implementation of Keycloak. The issue occurs because the server processes percent-encoded parameter names (like %53AMLResponse) while the signature verification logic only checks literal parameter names. An attacker can use this discrepancy to provide a crafted, unsigned SAML message that the server processes instead of a legitimately signed one, leading to full account takeover of federated users.

### 33. CVE-2026-116790｜signalwire / freeswitch
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T20:17:46.557)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T20:17:46.557 / 2026-11-05T22:38:13.080
- **官方描述（原文）**：FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to a software implementation that runs on any commodity hardware. Prior to 1.11.2, FreeSWITCH's inbound ICE handling accepted every connectivity check without cryptographically validating its STUN MESSAGE-INTEGRITY attribute. A network peer able to reach an ICE-enabled leg's media port could forge an ICE connectivity check without SDP credentials, nominate its own address, redirect RTP and DTLS traffic, and terminate the legitimate media path. On unencrypted legs this enables eavesdropping and media injection, while all WebRTC and SIP legs that negotiate ICE are in scope. Version 1.11.2 introduces the remediation, which requires ice_verify_message_integrity=true.

### 34. CVE-2026-116785｜signalwire / freeswitch
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T20:17:45.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T20:17:45.730 / 2026-11-05T22:38:13.080
- **官方描述（原文）**：FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to a software implementation that runs on any commodity hardware. Prior to 1.11.2, ws_read_frame() decoded a WebSocket frame's 64-bit extended payload length with a 32-bit byte swap and narrowed the result into a signed length. A value whose surviving low word became negative bypassed the signed size check and was reinterpreted as an enormous unsigned count, causing client bytes to overwrite memory beyond the 64 KiB receive buffer. Any client completing a /socket WebSocket upgrade on an enabled mod_xml_rpc endpoint reached the parser before HTTP authentication; both the module and WebSocket endpoint are disabled by default. The heap overwrite can corrupt connection pointers and crash FreeSWITCH, ending every concurrent session, although remote code execution has not been demonstrated. This issue is fixed in version 1.11.2.

### 35. CVE-2026-116779｜signalwire / freeswitch
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T20:17:44.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T20:17:44.790 / 2026-11-05T22:38:13.080
- **官方描述（原文）**：FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to a software implementation that runs on any commodity hardware. Prior to 1.11.3, sofia_presence_handle_sip_i_message() split the To user of an inbound SIP MESSAGE on a plus sign and treated the left side as a chat protocol selector. Selecting the api chat proto reached switch_api_execute(), allowing a peer whose MESSAGE was accepted to run FreeSWITCH API commands, including operating-system command sinks, with the daemon's privileges. Inbound chat is enabled on the stock internal and external profiles, and any authenticated profile account is sufficient; stock directory users without password material can also remove that barrier in affected configurations. The flaw permits configuration and credential disclosure, arbitrary call control, and command execution, and exploitation has been observed in the wild. This issue is fixed in version 1.11.3.

### 36. CVE-2026-111494｜TPC Software / Matchpoint
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T22:17:44.193)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T22:17:44.193 / 2026-11-05T22:36:02.320
- **官方描述（原文）**：Incorrect validation of TLS certificates in the MatchPoint Android app due to a TrustManager that accepts any certificate and a permissive hostname validator. Additionally, the app allows unencrypted HTTP traffic. An attacker capable of intercepting the victim's traffic could read and modify communications, including credentials and personal data.

### 37. CVE-2026-111490｜TPC Software / Matchpoint
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T22:17:43.597)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T22:17:43.597 / 2026-11-05T22:36:02.320
- **官方描述（原文）**：Insecure direct object reference (IDOR) vulnerability in the MatchPoint API, which relies on the `actingasuser` HTTP header without verifying the requester's authorization for the specified user. Manipulation of sequential identifiers allows access to personal, banking, and financial data, private messages, and QR codes for physical access, as well as the ability to modify third-party accounts, change passwords, impersonate users, and transfer virtual balances.

### 38. CVE-2026-111489｜TPC Software / Matchpoint
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T22:17:43.447)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T22:17:43.447 / 2026-11-05T22:36:02.320
- **官方描述（原文）**：A static credential embedded in the mobile app has been reported to return the 'autorizado' token on the MatchPoint platform. The report states that this token grants unauthenticated access to API services.

### 39. CVE-2026-100358｜SuiteCRM / SuiteCRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T19:16:55.400)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T19:16:55.400 / 2026-11-05T19:16:57.233
- **官方描述（原文）**：SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. Prior to 7.15.2 and 8.10.2, the Studio Dropdown Editor passes $dropdown_name through html_entity_decode() and writes the result verbatim into a PHP language file under custom/ that is included on later page loads. An administrator can inject persistent PHP that executes as the web-server account, survives cache clears, and compromises application and host confidentiality, integrity, and availability. This issue is fixed in versions 7.15.2 and 8.10.2.

### 40. CVE-2026-100109｜Unknown / Security For WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T08:17:01.870)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.8 (CRITICAL)
- **EPSS**：0.00369 / percentile=0.30959
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T08:17:01.870 / 2026-11-05T20:17:36.783
- **官方描述（原文）**：The Security For WooCommerce WordPress plugin from 1.0.10 to 1.0.16 does not perform capability checks when creating users through an action available to unauthenticated visitors, and lets the caller choose the new account's role, allowing unauthenticated attackers to create administrator accounts and take over the site.

### 41. CVE-2026-97371｜ntop / ntopng
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T17:18:22.323)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T17:18:22.323 / 2026-11-05T21:18:54.760
- **官方描述（原文）**：ntopng is a web-based network traffic monitoring application. Prior to 6.7.260721, ndpi_get_custom_category_match writes a four-byte nDPI protocol-category value through a pointer to the two-byte id variable in IpAddress::reloadBlacklist in src/IpAddress.cpp during packet dissection and host initialization. A remote unauthenticated attacker on a monitored network segment can send packets that match custom-category rules, causing stack corruption and denial of service without user interaction. This issue is fixed in version 6.7.260721.

### 42. CVE-2026-54442｜NationalSecurityAgency / emissary
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T21:18:51.240)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T21:18:51.240 / 2026-11-05T21:18:51.240
- **官方描述（原文）**：Emissary is a P2P based data-driven workflow engine. Prior to 8.51.0, the VALID_LINK validation in src/main/java/emissary/server/mvc/NavAction.java accepts protocol-relative URLs when processing configured navigation links. Browser URL normalization can interpret these accepted strings as external origins. The authoritative advisory attributes open redirect, server-side request forgery, and cloud metadata access to this bypass, but it identifies neither the server-side dereference path nor how navigation-link processing reaches that path. This issue is fixed in version 8.51.0.

### 43. CVE-2026-49405｜tinyhumansai / openhuman
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T17:18:18.457)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.2 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T17:18:18.457 / 2026-11-05T19:17:21.127
- **官方描述（原文）**：OpenHuman is an open-source agent harness available as a desktop application and Rust library. Before 0.56.0, the local server exposes the server-sent events endpoint at /events without bearer authentication, permits cross-origin browser access, and uses only a caller-supplied client_id to select WebChannelEvent objects from the process-wide event bus. An unauthenticated local client, or an attacker-hosted web page opened by the victim, can subscribe to another client's stream by supplying a known or guessed identifier; the fixed system identifier makes the proactive-message stream predictable. The exposed events can include complete assistant responses, streamed message content, tool names, tool arguments, and raw tool outputs intended for the local user interface. This issue is fixed in version 0.56.0.

### 44. CVE-2026-123206｜aozorae / EdgeChat
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T19:17:20.043)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T19:17:20.043 / 2026-11-05T19:17:20.043
- **官方描述（原文）**：EdgeChat before 2.20.3 contains a missing authentication vulnerability in the GET /files/:key route that allows unauthenticated or banned users to download decrypted public-channel attachments because canAccessFile() accepts a null user id. Attackers holding an attachment object key can omit or supply an invalid token to retrieve plaintext attachments without a session or channel membership.

### 45. CVE-2026-123019｜eosphoros-ai / DB-GPT
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T12:17:50.193)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T12:17:50.193 / 2026-11-05T21:18:45.360
- **官方描述（原文）**：A weakness has been identified in eosphoros-ai DB-GPT up to 0.8.2. Impacted is the function exec_module of the file hf_adapter.py of the component HuggingFace Adapter. Executing a manipulation of the argument trust_remote_code can lead to inclusion of functionality from untrusted control sphere. The attack can be launched remotely. The exploit has been made available to the public and could be used for attacks. The project was informed of the problem early through an issue report but has not responded yet.

### 46. CVE-2026-123018｜eosphoros-ai / DB-GPT
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T12:17:49.940)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T12:17:49.940 / 2026-11-05T21:18:45.220
- **官方描述（原文）**：A security flaw has been discovered in eosphoros-ai DB-GPT up to 0.8.2. This issue affects the function execute_code of the file code_utils.py of the component CodeAction. Performing a manipulation results in code injection. The attack can be initiated remotely. The exploit has been released to the public and may be used for attacks. The project was informed of the problem early through an issue report but has not responded yet.

### 47. CVE-2026-122330｜Blosc / c-blosc2
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T16:17:46.197)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T16:17:46.197 / 2026-11-05T21:18:44.943
- **官方描述（原文）**：Blosc c-blosc2 before 3.5.0 contains a divide-by-zero vulnerability in blosc2_schunk_get_slice_buffer() in blosc/schunk.c that allows attackers to crash applications by supplying crafted frames with unchecked zero chunksize or blocksize values. Attackers can provide a malicious Blosc2 frame opened via blosc2_schunk_open() or blosc2_schunk_from_buffer() and read as a slice, raising SIGFPE and terminating the process.

### 48. CVE-2026-122326｜Chevereto / Chevereto
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T16:17:45.503)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T16:17:45.503 / 2026-11-05T21:18:44.783
- **官方描述（原文）**：Chevereto before 4.5.8 contains an authorization bypass vulnerability in the get-album-contents action of the /json route that allows unauthenticated attackers to list private albums by supplying another user's album id. Attackers with a session token from any public page and an album's encoded id can obtain image filenames, viewer and direct file URLs, and download private images.

### 49. CVE-2026-104867｜immich-app / immich
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T17:17:32.687)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T17:17:32.687 / 2026-11-05T19:17:07.373
- **官方描述（原文）**：Immich is a high-performance self-hosted photo and video management solution. From 3.0.0 until 3.2.0, the GET /api/admin/users/{id}/calendar-heatmap route in server/src/controllers/user-admin.controller.ts uses the ordinary Permission.UserRead permission without an admin-route requirement, and UserAdminService.getCalendarHeatmap in server/src/services/user-admin.service.ts does not compare the authenticated user with the requested user identifier or perform a separate access check. Any authenticated non-admin user can therefore request another account's upload or capture-date activity heatmap for an arbitrary date range. AssetRepository.getCalendarHeatmap in server/src/repositories/asset.repository.ts filters by owner, date, and deletion state but not visibility, so the returned daily counts and total count include archived and locked assets. The route exposes counts and activity dates but does not return asset metadata or content, and it does not affect integrity or availability. This issue is fixed in version 3.2.0.

### 50. CVE-2026-104135｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T20:17:38.980)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T20:17:38.980 / 2026-11-05T21:18:34.890
- **官方描述（原文）**：OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.3.0, library/ajax/payment_ajax.php validates a CSRF token but performs no AclMain authorization check before executing a wildcard search of patient_data. Any authenticated user, including a non-clinical role, can enumerate patient identifiers, full names, and dates of birth through the set_patient branch. This issue is fixed in version 8.3.0.

### 51. CVE-2026-103939｜openemr / openemr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T20:17:38.510)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T20:17:38.510 / 2026-11-05T21:18:34.773
- **官方描述（原文）**：OpenEMR is a free and open source electronic health records and medical practice management application. Prior to 8.3.0, interface/modules/custom_modules/oe-module-weno/scripts/file_download.php has no ACL or CSRF check and ignores the result of validateAdminCredentials(). When the Weno module is enabled, the default GET path calls PharmacyService::removeWenoPharmacies() before attempting a refetch, allowing any authenticated user to truncate the weno_pharmacy table and allowing a cross-site request to trigger the same operation through a logged-in victim. A failed later download can leave the e-prescribing pharmacy directory empty and unavailable. This issue is fixed in version 8.3.0.

### 52. CVE-2026-123020｜eosphoros-ai / DB-GPT
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T13:17:07.280)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T13:17:07.280 / 2026-11-05T21:18:45.510
- **官方描述（原文）**：A security vulnerability has been detected in eosphoros-ai DB-GPT up to 0.8.1. The affected element is the function FileBasedSkill.get_prompt of the file packages/dbgpt-core/src/dbgpt/agent/skill/claude_skill/__init__.py of the component Jinja2 Template Handler. The manipulation leads to improper neutralization of special elements used in a template engine. The attack may be initiated remotely. The exploit has been disclosed publicly and may be used. Upgrading to version 0.8.2 is sufficient to fix this issue. The identifier of the patch is a9e7a3c026d114fcfb4ffe3eaf78851a636ded16. It is suggested to upgrade the affected component.

### 53. CVE-2026-118517｜sensiolabs / symfony
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T17:17:53.147)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T17:17:53.147 / 2026-11-05T17:17:53.147
- **官方描述（原文）**：The Symfony HtmlSanitizer component UrlSanitizer parses URLs differently from browsers, allowing the allowLinkHosts() and allowMediaHosts() checks to be bypassed for URLs without a well-formed authority, resulting in untrusted hosts being referenced in sanitized output in Symfony versions 6.1.x prior to 6.4.50, 7.x prior to 7.4.23, and 8.x prior to 8.1.11. UrlSanitizer parses URLs with league/uri, which follows RFC 3986, while browsers follow the WHATWG URL standard. For URLs without a well-formed authority, such as http:evil.example, ///evil.example, or https://://evil.example/ the sanitizer finds no host, whereas browsers resolve them to evil.example. The guard added for CVE-2026-45066 missed the zero-slash form, and the host 0 was also skipped because PHP treats it as falsy. This is exploitable when a host allow-list is combined with allowRelativeLinks(true) or allowRelativeMedias(true). The default configuration is not affected.

### 54. CVE-2026-111062｜Eugeny / russh
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T21:18:35.607)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T21:18:35.607 / 2026-11-05T22:17:43.317
- **官方描述（原文）**：russh is a Rust SSH client and server library. From version 0.34.0-beta.1 until version 0.64.0, its SSH server does not require the signature algorithm in a public-key authentication signature to match the algorithm named in the authentication request. A client possessing an authorized RSA private key can announce rsa-sha2-512 while supplying a valid ssh-rsa SHA-1 signature, bypassing restrictions or producing misleading audit records when applications rely on the requested algorithm. A valid private-key signature remains required, and russh clients are not affected. This issue is fixed in version 0.64.0.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-48705 | P3 / 38 | Project-MONAI / MONAI | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-123198 | P3 / 38 | LMFDB / LMFDB | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102940 | P3 / 38 | openemr / openemr | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-87008 | WATCH / 30 | vitali87 / code-graph-rag | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-75614 | WATCH / 30 | esa / asn1scc | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-54912 | WATCH / 30 | bytecodealliance / wasm-micro-runtime | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-54142 | WATCH / 30 | tinyhumansai / openhuman | v3.1 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-49272 | WATCH / 30 | oauthlib / oauthlib | v3.1 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-123158 | WATCH / 30 | OpenBSD / OpenSSH | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-120499 | WATCH / 30 | h5io / h5io | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-115573 | WATCH / 30 | openemr / openemr | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-96677 | WATCH / 28 | Apache Software Foundation / Apache Juneau | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-85076 | WATCH / 28 | jhuckaby / Cronicle | v4.0 9.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-83542 | WATCH / 28 | Apache Software Foundation / Apache OFBiz | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-82907 | WATCH / 28 | Apache Software Foundation / Apache OFBiz | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-77596 | WATCH / 28 | kubeflow / pipelines | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-73117 | WATCH / 28 | Apache Software Foundation / Apache Juneau | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-73116 | WATCH / 28 | Apache Software Foundation / Apache Juneau | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-73101 | WATCH / 28 | Apache Software Foundation / Apache Juneau | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-73100 | WATCH / 28 | Apache Software Foundation / Apache Juneau | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-73099 | WATCH / 28 | Apache Software Foundation / Apache Juneau | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-73098 | WATCH / 28 | Apache Software Foundation / Apache Juneau | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-71550 | WATCH / 28 | SuiteCRM / SuiteCRM | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-63774 | WATCH / 28 | Subnet Solutions / PowerSYSTEM Center 2024 | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-63017 | WATCH / 28 | Subnet Solutions / PowerSYSTEM Center 2020 | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-54143 | WATCH / 28 | tinyhumansai / openhuman | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-54141 | WATCH / 28 | tinyhumansai / openhuman | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-46350 | WATCH / 28 | dcmjs-org / dcmjs | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-121489 | WATCH / 28 | Apache Software Foundation / Apache Juneau | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-119757 | WATCH / 28 | BTCPay Server / BTCPay Server | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：30。
- EPSS 未確認：30；Exploitation status 未確認：15。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-06T07:30:24.056900+00:00`；Delta generated at：`2026-11-06T07:30:24.056900+00:00`。

---

## 可驗證資料來源

- **CVE-2026-48705** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48705)
- **CVE-2026-123198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123198)
- **CVE-2026-102940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102940)
- **CVE-2026-87008** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87008)
- **CVE-2026-75614** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75614)
- **CVE-2026-54912** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54912)
- **CVE-2026-54142** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54142)
- **CVE-2026-49272** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-49272)
- **CVE-2026-123158** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123158)
- **CVE-2026-120499** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120499)
- **CVE-2026-115573** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115573)
- **CVE-2026-96677** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96677)
- **CVE-2026-85076** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85076)
- **CVE-2026-83542** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83542)
- **CVE-2026-82907** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82907)
- **CVE-2026-77596** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77596)
- **CVE-2026-73117** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73117)
- **CVE-2026-73116** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73116)
- **CVE-2026-73101** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73101)
- **CVE-2026-73100** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73100)
- **CVE-2026-73099** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73099)
- **CVE-2026-73098** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73098)
- **CVE-2026-71550** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71550)
- **CVE-2026-63774** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63774)
- **CVE-2026-63017** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63017)
- **CVE-2026-54143** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54143)
- **CVE-2026-54141** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54141)
- **CVE-2026-46350** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46350)
- **CVE-2026-121489** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121489)
- **CVE-2026-119757** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119757)
- **CVE-2026-119344** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119344)
- **CVE-2026-117691** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-117691)
- **CVE-2026-116790** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116790)
- **CVE-2026-116785** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116785)
- **CVE-2026-116779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116779)
- **CVE-2026-111494** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111494)
- **CVE-2026-111490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111490)
- **CVE-2026-111489** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111489)
- **CVE-2026-100358** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100358)
- **CVE-2026-100109** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100109) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-100109)
- **CVE-2026-97371** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97371)
- **CVE-2026-54442** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54442)
- **CVE-2026-49405** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-49405)
- **CVE-2026-123206** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123206)
- **CVE-2026-123019** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123019)
- **CVE-2026-123018** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123018)
- **CVE-2026-122330** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122330)
- **CVE-2026-122326** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122326)
- **CVE-2026-104867** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104867)
- **CVE-2026-104135** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104135)
- **CVE-2026-103939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103939)
- **CVE-2026-123020** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123020)
- **CVE-2026-118517** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118517)
- **CVE-2026-111062** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111062)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
