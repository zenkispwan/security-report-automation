# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**66** 筆符合目前門檻的重要變化；事件統計：EPSS_INCREASED=1、NEW_CVE=63、NEW_KEV=2。
- Intelligence 候選：**30** 筆；P1 **3**、P2 **0**、P3 **7**、WATCH **20**。
- Baseline：state / generated_at=2026-09-10T13:45:25.158574+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-86060、CVE-2026-67277、CVE-2026-20079。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **66** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-86060｜MikroTik / RouterOS
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-10 / due_date=2026-09-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-05T20:17:18.703 / 2026-09-11T04:18:02.840
- **官方描述（原文）**：MikroTik RouterOS contains an improper neutralization of argument delimiters in a command vulnerability which allows an attacked to change the trusted RouterOS policy mask, leading to privilege escalation.

### 2. CVE-2026-67277｜MikroTik / RouterOS
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-10 / due_date=2026-09-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-05T20:17:18.120 / 2026-09-11T04:17:44.900
- **官方描述（原文）**：MikroTik RouterOS contains a missing authenticaion for critical function vulnerability which allows kernel memory disclosure and denial of service in the btest service.

### 3. CVE-2026-20079｜Cisco / Secure Firewall Management Center (FMC) and Security Cloud Control (SCC) Firewall Management
- **Delta event**：EPSS_INCREASED (from=0.35946; to=0.74697)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.74697 / percentile=0.9947
- **CISA KEV**：listed=true / date_added=2026-09-09 / due_date=2026-09-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-03-04T18:16:24.230 / 2026-09-10T12:48:17.580
- **官方描述（原文）**：Cisco Secure Firewall Management Center (FMC) Software and Cisco Security Cloud Control (SCC) Firewall Management contain an authentication Bypass using an alternate path or channel vulnerability that could allow an unauthenticated, remote attacker to bypass authentication and execute script files on an affected device to obtain root access to the underlying operating system.

### 4. CVE-2026-89086｜OCaml / jose
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T20:17:32.113)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T20:17:32.113 / 2026-09-10T21:17:52.570
- **官方描述（原文）**：In the jose package before 0.11.0 for OCaml, library calls to validate an RSA signature only confirm that PKCS #1 decoding succeeds, and proceed to declare the signature valid without the required steps that involve the public key.

### 5. CVE-2026-89043｜krakenjs / passport-saml-encrypted
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T18:18:16.073)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T18:18:16.073 / 2026-09-10T19:58:20.507
- **官方描述（原文）**：passport-saml-encrypted through 0.1.13 contains an XML signature wrapping vulnerability where signature verification and assertion extraction use independent XPath lookups with no cross-validation. Attackers holding any validly signed SAML message can prepend a forged unsigned assertion that gets accepted as the verified identity while the genuine signature validates against the original assertion.

### 6. CVE-2026-88869｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:14.637)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:14.637 / 2026-09-10T16:18:10.990
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a stored cross-site scripting vulnerability in the AD_Server plugin's log.php endpoint that fails to escape the label parameter before storage. An unauthenticated attacker can inject malicious HTML through the label parameter, which is later rendered unsanitized in the admin Ad Types report using jQuery .html(), allowing execution of arbitrary JavaScript in an administrator's browser session.

### 7. CVE-2026-88867｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:12.920)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:12.920 / 2026-09-10T15:17:57.280
- **官方描述（原文）**：WWBN AVideo, in versions up to and including commit c3edcc274c389816d434acadac07ee78eaf330c1, contains a stored cross-site scripting vulnerability. objects/categoryAddNew.json.php passes the POST parameters `name` and `iconClass` to Category::setName() and Category::setIconClass(), which store the values without sanitization (setName only truncates to 45 characters). The category name is later echoed as HTML text and iconClass is echoed into a class attribute in view/modeYoutubeBottom.php and in Gallery cards (plugin/Gallery/functions.php). When the CustomizeUser option usersCanCreateNewCategories is enabled, any authenticated user with canUpload permission (granted by default via self-registration) can create a category containing a JavaScript payload; the payload then executes in the browser of any visitor, including administrators, who views a watch page or gallery entry for a video assigned to that category, allowing actions such as authenticated requests with the victim's session. The issue was unpatched at the time of reporting.

### 8. CVE-2026-88864｜Cap-go / capgo.app
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:12.187)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:12.187 / 2026-09-10T15:17:57.103
- **官方描述（原文）**：Capgo (capgo.app) fails to restrict direct write access to the public.sso_providers table exposed through Supabase PostgREST. A holder of an ordinary Capgo full API key can insert a row with status='active' and enforce_sso=true, bypassing the intended backend SSO provisioning route (supabase/functions/_backend/private/sso/providers.ts) and its controls: the Enterprise plan requirement, SSO provider creation via the Supabase Management API, DNS TXT domain-ownership verification, the pending_verification → verified → active status transition, and issuance of a trusted provider ID by Supabase Auth. The forged row is trusted by SSO discovery and enforcement logic, including the unauthenticated login preflight endpoint /private/sso/check-domain, which then reports {"has_sso": true, "enforce_sso": true} for domains that were never verified, allowing attacker-controlled SSO enforcement to be asserted for arbitrary domains and disrupting normal login. All versions are affected; at the time of the advisory no patch was available.

### 9. CVE-2026-88044｜rclone / rclone
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T17:17:08.387)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T17:17:08.387 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：rclone is a command-line program to sync files and directories to and from different cloud storage providers. From 1.70.0 until 1.75.1, the serve/start RC interface accepts per-server proxyOpt.AuthProxy settings, and the FTP and S3 constructors in cmd/serve/ftp/ftp.go and cmd/serve/s3/server.go incorrectly check the process-global proxy.Opt.AuthProxy value instead. When the global value is empty, the request-local authentication proxy is ignored: FTP falls back to the fixed filesystem with username anonymous and any password, while S3 with AuthKey serves the fixed RC fs rather than the backend selected by the proxy. The dedicated command-line servers that configure the global option are not affected. This issue is fixed in version 1.75.1.

### 10. CVE-2026-88018｜rclone / rclone
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T16:18:08.913)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T16:18:08.913 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：rclone is a command-line program to sync files and directories to and from different cloud storage providers. Prior to 1.75.1, rclone serve s3 configured with --auth-proxy but without --auth-key allows authPairMiddleware to register any client-chosen accessKeyID with an empty ws.s3Secret. gofakes3 then verifies the request’s SigV4 signature against that same empty secret, while Server.auth passes the access key identifier as both the user and authentication value to the proxy without an independent per-identity secret. An unauthenticated network attacker can therefore choose an arbitrary access key, sign with an empty secret, and reach whatever backend the auth-proxy script resolves for that identity. This issue is fixed in version 1.75.1.

### 11. CVE-2026-89046｜luben / zstd-jni
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T18:18:16.560)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T18:18:16.560 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：zstd-jni versions 1.5.5-6 through 1.5.7-13 contain an out-of-bounds read vulnerability in Zstd.getFrameContentSize that fails to validate negative srcPosition arguments. Attackers can supply negative offset values that bypass bounds checks and reach the native frame-header parser, causing out-of-bounds memory reads that lead to information disclosure or JVM crashes.

### 12. CVE-2026-88937｜knowns-dev / knowns
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T16:18:12.273)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T16:18:12.273 / 2026-09-10T19:58:20.507
- **官方描述（原文）**：knowns through 0.33.0 fails to properly validate template destination paths in the code generation template engine, allowing attackers to read and write arbitrary files outside the project root. Attackers can supply malicious templates that traverse directories to overwrite shell profiles, steal credentials, or achieve persistent code execution on victim systems.

### 13. CVE-2026-88924｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T15:17:59.253)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.0 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T15:17:59.253 / 2026-09-10T19:55:45.477
- **官方描述（原文）**：A flaw was found in the admin backend of gvfs. The privileged gvfsd-admin daemon changes the ownership of newly created private D-Bus sockets by calling the link-following chown() function on a pathname inside a user-controlled directory. A local attacker can exploit this via a Time-of-Check Time-of-Use (TOCTOU) race condition and exchange the socket pathname with a symbolic link pointing to an arbitrary root-owned file (such as /etc/pam.d/su). The daemon subsequently follows the symlink and changes the ownership of the targeted root-owned file to the attacker's user ID. This allows an authenticated local attacker to modify critical system files, leading to a full local privilege escalation to root.

### 14. CVE-2026-88898｜AppFlowy-IO / AppFlowy-Cloud
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T15:17:59.107)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T15:17:59.107 / 2026-09-10T16:18:11.997
- **官方描述（原文）**：AppFlowy-Cloud versions 0.7.2 through 0.9.64 fail to authorize callers against the workspace in the bulk publish endpoint path, allowing authenticated users to publish content into other tenants' namespaces. Attackers can write published views with attacker-controlled title, body and metadata into victim workspaces to deface public pages or host phishing content on trusted URLs.

### 15. CVE-2026-88874｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:15.593)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:15.593 / 2026-09-10T16:18:11.233
- **官方描述（原文）**：AVideo through revision c3edcc274c389816d434acadac07ee78eaf330c1 (master, 2026-08-23) does not enforce the Live stream password check on the stats endpoint or on the HLS origin. Live::_getStats() (plugin/Live/Live.php) returns a password-protected transmission's RTMP stream key, its isPasswordProtected flag, and its HLS (m3u8) URL to unauthenticated callers, in both the public applications list and the hidden_applications branch used when canSeeLiveFromLiveKey() fails. Separately, the shipped NGINX configuration (deploy/nginx/nginx.conf) serves the .m3u8 playlist, the AES-128 key, and the transport-stream segments from the /live location without any auth_request (the auth_key_check directive in the .key location is commented out). A remote, unauthenticated attacker can therefore retrieve the stream key and decryption key and watch a password-protected live transmission without supplying the configured password. No patched version was available at the time of the advisory.

### 16. CVE-2026-88872｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:15.243)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:15.243 / 2026-09-10T15:17:57.537
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a cross-site request forgery vulnerability in the setPassword.json.php endpoint that allows unauthenticated attackers to modify any user's channel password by sending a GET request. Attackers can craft a malicious webpage that, when visited by an authenticated administrator, sets or clears any user's channel password without CSRF token validation.

### 17. CVE-2026-88862｜Cap-go / capgo.app
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:11.820)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:11.820 / 2026-09-10T15:17:56.617
- **官方描述（原文）**：Capgo (capgo.app) backend through 12.242.4 does not validate parent-child delegation when processing the x-limited-key-id header. checkKeyByIdPg() in supabase/functions/_backend/utils/hono_middleware.ts resolves the attacker-supplied numeric API key ID using only the key ID, its expiration state, and the authenticating key's user_id, while hasLimitedRbacSubkeyScope() accepts any key with a non-organization (e.g., app-scoped) RBAC binding and validateSubkeyUser() only compares owning user IDs. Because Capgo treats API keys as independent RBAC principals with separate role bindings, an authenticated apikey_manager API key with no application access can supply the numeric ID of a more privileged same-owner key and have the middleware replace the authenticated principal and effective API-key secret with that key (setSubkeyAuthContext), exercising an app_admin sibling's permissions without knowing or submitting its secret. The issue was reproduced on release 12.242.4 (commit b3d02cdbc23ac59990785acacd1f113c07458568) after the fix for GHSA-8h52-44r7-w343; at the time of the advisory no patched version was available.

### 18. CVE-2026-88060｜angular / angular
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T19:17:42.107)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T19:17:42.107 / 2026-09-10T20:17:31.417
- **官方描述（原文）**：Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.30, 21.2.22, and 22.1.4, Angular server-side rendering (SSR) in @angular/platform-server serializes untrusted input inside template content nested in fallback raw-content elements such as noscript, iframe, noembed, and noframes. The Domino serializer's fallbackRawContentTags traversal stopped at the DocumentFragment used by template.content, so matching closing tags in xmp, style, script, comments, or text nodes were not escaped. Standard interpolation with comments or text nodes is reachable without relaxed schemas; literal xmp or style requires CUSTOM_ELEMENTS_SCHEMA or NO_ERRORS_SCHEMA, while Renderer2 imperative DOM construction is unconditionally affected. When HTML5 RAWTEXT browser parsing encounters the unescaped closing tag, it exits the fallback container and interprets trailing markup as active DOM elements, enabling arbitrary JavaScript execution. This issue is fixed in versions 20.3.30, 21.2.22, and 22.1.4.

### 19. CVE-2026-88049｜tesseract-ocr / tesseract
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T17:17:09.087)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T17:17:09.087 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：Tesseract is an open source OCR engine. In version 5.5.3 and earlier, prior .traineddata hardening added bounds checks to NetworkIO::CopyTimeStepGeneral and NetworkIO::Randomize in src/lstm/networkio.cpp but left NetworkIO::WriteTimeStepPart and NetworkIO::AddTimeStepPart unchecked. In LSTM::Forward in src/lstm/lstm.cpp, source_ is sized from the independently deserialized na_ field while the WriteTimeStepPart count is ns_, which comes from the CI gate WeightMatrix dim1() value. A crafted NT_LSTM layer can make ns_ much larger than na_, causing a heap out-of-bounds write during the first recognition step on the default LSTM engine and resulting in heap corruption, a crash, or potentially controlled corruption. No fixed release is available as of this review.

### 20. CVE-2026-88045｜rclone / rclone
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T17:17:08.530)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T17:17:08.530 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：rclone is a command-line program to sync files and directories to and from different cloud storage providers. From 1.75.0 until 1.75.1, the serve S3 streamed multipart path in cmd/serve/s3/multipart.go passes attacker-controlled contentLength to multipart.NewRW().Reserve before reading request-body bytes. waitForTurn admits the current part and one oversized part when the buffer is empty despite --multipart-streaming-buffer-limit, and lib/pool allocates 1 MiB pages according to Content-Length or X-Amz-Decoded-Content-Length. A network client can retain or multiply these reservations without sending the declared body, exhausting process or host memory or permanently blocking request handlers. Anonymous S3 deployments require no credentials, while deployments using auth_key require an accepted S3 key. This issue is fixed in version 1.75.1.

### 21. CVE-2026-73699｜FileRun / FileRun
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T17:17:06.083)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T17:17:06.083 / 2026-09-10T19:58:20.507
- **官方描述（原文）**：FileRun before 2026.3.0 contains a PHP object injection vulnerability that allows authenticated attackers to execute arbitrary code by exploiting incorrect options passed to unserialize() in the Perms::getPerms() method, where a positional array is used instead of the required named-key array to disable class instantiation. Attackers with database write access can inject a serialized gadget chain into the permissions table columns processed on every authenticated page load to write arbitrary files, such as PHP webshells, to web-accessible paths.

### 22. CVE-2026-64838｜ICEcoder / ICEcoder
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:03.823)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:03.823 / 2026-09-10T19:58:20.507
- **官方描述（原文）**：ICEcoder versions through 8.1 fail to properly validate the oldFileName parameter in file move and rename operations, allowing authenticated users to relocate files from outside the document root. Attackers can use path traversal sequences in oldFileName to move files writable by the PHP process into the web-accessible project directory, disclosing file contents and deleting originals.

### 23. CVE-2026-45747｜OISF / suricata
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T15:17:34.997)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T15:17:34.997 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：Suricata is a network Intrusion Detection System, Intrusion Prevention System and Network Security Monitoring engine. Prior to version 7.0.16, the Lua TLS certificate information helper could dereference NULL certificate fields when a Lua script requested certificate information for TLS traffic where some certificate fields were absent. Crafted TLS traffic processed by a deployment using affected Lua TLS scripting could crash Suricata, resulting in denial of service. Version 7.0.16 contains a fix. As a workaround, avoid Lua scripts that call TLS certificate information helpers on untrusted traffic (`TlsGetCertInfo` function), or update scripts to handle missing certificate fields where possible.

### 24. CVE-2026-89094｜Forgejo / Forgejo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T21:17:53.160)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T21:17:53.160 / 2026-09-10T21:17:53.160
- **官方描述（原文）**：Forgejo before 16.0.4 allows remote code execution via a crafted template repository because template expansion on files in .forgejo/template is mishandled.

### 25. CVE-2026-89042｜krakenjs / passport-saml-encrypted
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T18:18:15.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T18:18:15.910 / 2026-09-10T19:58:20.507
- **官方描述（原文）**：passport-saml-encrypted through 0.1.13 makes SAML signature verification conditional on an optional cert option, allowing attackers to bypass authentication by submitting unsigned SAML responses. Attackers can post forged SAML responses with arbitrary NameID and attributes to the assertion consumer service endpoint to receive authenticated profiles without valid signatures.

### 26. CVE-2026-88899｜knowns-dev / knowns
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T16:18:12.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T16:18:12.120 / 2026-09-10T19:58:20.507
- **官方描述（原文）**：knowns versions before 0.31.0 fail to properly validate the x-opencode-directory request header in the /api/opencode proxy endpoint. Remote attackers can supply arbitrary directory paths to execute file operations outside the project root on the host system.

### 27. CVE-2026-88887｜renovatebot / renovate
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:17.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:17.693 / 2026-09-10T15:17:58.380
- **官方描述（原文）**：Renovate is a dependency update automation tool. When listing tags/digests for a container image, Renovate follows pagination links supplied by the remote registry in the HTTP Link header and attaches the registry credentials to the follow-up request without verifying that the pagination URL has the same origin as the original registry. A malicious or compromised container registry can therefore specify a Link header pointing to an attacker-controlled host and receive the credentials Renovate uses for that registry. Exploitation requires that the target has container (Docker) dependencies and is already interacting with the malicious or compromised registry. This is fixed in Renovate 44.11.2 (npm and renovate/renovate images), Mend Renovate CE/EE 15.4.0 and the mend-renovate-enterprise-edition Helm chart 10.4.0; the same-origin check can be disabled with RENOVATE_X_DOCKER_PAGINATION_ALLOW_CROSS_ORIGIN.

### 28. CVE-2026-88882｜renovatebot / renovate
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:16.823)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:16.823 / 2026-09-10T15:17:58.050
- **官方描述（原文）**：Renovate is a dependency update automation tool. In versions before 44.11.2 (and Mend Renovate CE/EE images and charts before 15.4.0, and mend-renovate-enterprise-edition helm chart before 10.4.0), when listing new package versions from a NuGet registry Renovate follows pagination URLs supplied by the registry in the HTTP `Link` header without verifying that the target has the same origin as the configured registry. Registry credentials are attached to the request for the 'next' page, so a malicious or compromised NuGet registry can return a `Link` header pointing at an attacker-controlled server and cause Renovate to send the registry credentials to that server. Exploitation requires the remote registry to be malicious or compromised; such a registry would normally already have received the credentials on the initial request, so the issue primarily allows the credentials to be delivered to an additional, attacker-chosen host. The fix restricts pagination to the same origin; the previous behaviour can be re-enabled with the RENOVATE_X_NUGET_PAGINATION_ALLOW_CROSS_ORIGIN option.

### 29. CVE-2026-88881｜renovatebot / renovate
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:16.650)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:16.650 / 2026-09-10T14:50:07.813
- **官方描述（原文）**：Renovate, a dependency update tool, follows pagination links supplied by the GitHub server in the HTTP `Link` header when interacting with GitHub.com, GitHub Enterprise Cloud, or GitHub Enterprise Server, and sends the credentials configured for that host to the URL given as the 'next' page. Because the pagination URL is not validated against the host originally contacted, a malicious or compromised GitHub server can return a `Link` header pointing to an attacker-controlled host and cause Renovate to disclose those credentials to it. Exploitation requires that the GitHub server Renovate talks to (as the repository host or as a datasource such as github-releases, github-tags, or git-refs) is already malicious or compromised. The issue is fixed in renovate 44.11.3 (npm and renovate/renovate container images), Mend Renovate CE/EE images and the mend-renovate-ce helm chart 15.4.0, and the mend-renovate-enterprise-edition helm chart 10.4.0. There is no workaround; the pre-existing RENOVATE_X_REBASE_PAGINATION_LINKS option disables the new host check and should only be used with servers that intentionally use different pagination hosts.

### 30. CVE-2026-88880｜renovatebot / renovate
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:16.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:16.480 / 2026-09-10T14:50:07.813
- **官方描述（原文）**：Renovate before 44.11.3 fails to validate Link header destinations when following GitLab server pagination, allowing malicious servers to redirect credential-bearing requests. Attackers controlling a compromised GitLab server can specify a Link header pointing to attacker-controlled infrastructure to exfiltrate authentication credentials.

### 31. CVE-2026-88877｜traefik / traefik
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:16.023)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:16.023 / 2026-09-10T15:17:57.790
- **官方描述（原文）**：Traefik is a HTTP reverse proxy and load balancer. In versions >= v3.7.0 and <= v3.7.11, the Kubernetes ingress-nginx provider mishandles Ingresses that carry both an authentication annotation and the nginx.ingress.kubernetes.io/from-to-www-redirect annotation. For such Ingresses the provider creates an additional 'sibling' router that matches on the host alone, carries only the RedirectRegex middleware, and still points at the parent router's protected backend service. Because RedirectRegex is not a terminal handler, a request its pattern does not match is forwarded to the backend, and because the redirect pattern only accepts a numeric port while Traefik's host matcher canonicalizes the authority via net.SplitHostPort, a request with a non-numeric or empty port (for example 'Host: www.example.com:x') selects the sibling router, misses the redirect, and is proxied to the protected backend with none of the Ingress's annotation-derived middlewares applied. This discards not only authentication (e.g. BasicAuth) but every annotation-derived middleware, including source-IP allowlisting. Traefik v2 and v3 releases before v3.7.0 are not affected. The issue is fixed in v3.7.12.

### 32. CVE-2026-88868｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:13.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:13.490 / 2026-09-10T15:17:57.413
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a stored cross-site scripting vulnerability in the LiveLinks plugin where title and description fields are stored without sanitization. A user with canStream permission can inject malicious scripts that execute in the browser of every visitor viewing the live-link page, including administrators, within the site origin.

### 33. CVE-2026-88866｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:12.773)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:12.773 / 2026-09-10T15:13:07.090
- **官方描述（原文）**：WWBN AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a stored cross-site scripting vulnerability in the LoginControl plugin that fails to encode the User-Agent header before storing it in login history. Attackers with any valid login account can inject malicious scripts in the User-Agent header that execute in administrator browsers when viewing the Login History page, allowing script execution within the administrator session.

### 34. CVE-2026-88860｜Cap-go / capgo.app
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:11.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:11.527 / 2026-09-10T15:13:07.090
- **官方描述（原文）**：Capgo fails to clean up channel permission overrides when a user's last organization role binding is deleted, leaving stale overrides active. Attackers can retain channel-specific permissions after their base RBAC access has been revoked to perform unauthorized actions like changing production OTA versions.

### 35. CVE-2026-88062｜diegosouzapw / OmniRoute
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T20:17:31.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T20:17:31.693 / 2026-09-10T20:17:31.693
- **官方描述（原文）**：OmniRoute is an open-source AI gateway providing a single endpoint for multiple model providers. In 3.8.49 and earlier, the OmniRoute POST /api/acp/agents custom ACP agent endpoint accepted attacker-controlled binary and versionCommand values and used only a self-consistency check before execFileSync executed the selected interpreter and arguments. The same request called refreshAgentCache, and resolveVersionProbe accepted the matched command before the execFileSync sink ran it. The tokenizeVersionCommand function and DISALLOWED_VERSION_COMMAND_CHARS filter rejected a limited set of shell metacharacters but still allowed interpreter evaluation arguments. The isAuthenticated function relied on isAuthRequired, which accepted anonymous requests when requireLogin was false, while api/acp/ was absent from LOCAL_ONLY_API_PREFIXES and SPAWN_CAPABLE_PREFIXES. With requireLogin=false or during a fresh-instance bootstrap window, a remote anonymous request could supply an interpreter evaluation argument and execute arbitrary code in the server container. With requireLogin=true and a configured management password, exploitation instead required a management session or management-scoped API key. No fixed version is available as of this review.

### 36. CVE-2026-88007｜traefik / traefik
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T15:17:56.183)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T15:17:56.183 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：Traefik is an open source HTTP reverse proxy and load balancer. From 2.11.0 until 2.11.57 and 3.7.13, the HTTP/3 entrypoint ConnContext does not call service.AddTransportOnContext, so kerberosRoundTripper uses a shared backend transport instead of a transport dedicated to each frontend connection. With HTTP/3 enabled, a backend using connection-bound NTLM or Negotiate authentication, and backend keep-alive, an unrelated client can reuse a backend connection authenticated for a victim, read victim-only data, and act as that victim without the victim credentials. This issue is fixed in 2.11.57 and 3.7.13.

### 37. CVE-2026-8778｜mulika / MIPL Grouped Checkout Fields for WooCommerce. Customize & Organize Checkout Fields.
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T04:18:04.617)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T04:18:04.617 / 2026-09-11T04:18:04.617
- **官方描述（原文）**：The MIPL Grouped Checkout Fields for WooCommerce – Customize & Organize Checkout Fields. plugin for WordPress is vulnerable to arbitrary file uploads due to missing file type validation in the `mipl_wc_upload_file` function in all versions up to, and including, 1.2.1. This makes it possible for unauthenticated attackers to upload arbitrary files on the affected site's server which may make remote code execution possible.

### 38. CVE-2026-85025｜IBM / Langflow OSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T21:17:51.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T21:17:51.990 / 2026-09-10T21:34:14.253
- **官方描述（原文）**：IBM Langflow OSS 1.0.0 through 1.11.5 Langflow could allow an unauthenticated attacker to execute arbitrary code and access or modify chat sessions through publicly shared MCP project endpoints due to improper enforcement of public-flow security restrictions and session isolation controls.

### 39. CVE-2026-82107｜IBM / DataStage on Cloud Pak for Data
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T22:17:04.220)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T22:17:04.220 / 2026-09-10T22:17:04.220
- **官方描述（原文）**：IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to obtain sensitive information and bypass security restrictions due to improper authentication.

### 40. CVE-2026-82100｜IBM / DataStage on Cloud Pak for Data
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T22:17:04.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T22:17:04.090 / 2026-09-10T22:17:04.090
- **官方描述（原文）**：IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to cause a denial of service due to a path traversal vulnerability.

### 41. CVE-2026-81800｜Par avisverifies / Verified Reviews (Avis Vérifiés)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T15:17:46.360)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T15:17:46.360 / 2026-09-10T15:43:28.913
- **官方描述（原文）**：Unauthenticated SQL Injection in Verified Reviews (Avis Vérifiés) <= 2.4.6 versions.

### 42. CVE-2026-81468｜Dell / ThinOS 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T16:17:58.157)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T16:17:58.157 / 2026-09-11T04:17:58.087
- **官方描述（原文）**：Dell ThinOS 10, versions prior to 2605_10. 2616, contains an Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability. A high privileged attacker with remote access could potentially exploit this vulnerability, leading to Command execution.

### 43. CVE-2026-81467｜Dell / ThinOS 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T16:17:58.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T16:17:58.040 / 2026-09-11T04:17:57.980
- **官方描述（原文）**：Dell ThinOS 10, versions prior to 2605_10. 2616, contains an Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability. An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to Command execution.

### 44. CVE-2026-81204｜IBM / Langflow OSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T22:17:01.580)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T22:17:01.580 / 2026-09-10T22:17:01.580
- **官方描述（原文）**：IBM Langflow OSS 1.0.0 through 1.11.5 could allow a remote attacker to execute arbitrary code due to code injection during graph construction.

### 45. CVE-2026-81048｜Dell / ThinOS 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T16:17:57.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T16:17:57.543 / 2026-09-11T04:17:57.060
- **官方描述（原文）**：Dell ThinOS 10, versions prior to 2605_10.2616, contain an Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability. An unauthenticated attacker with adjacent network access could potentially exploit this vulnerability, leading to Remote Code execution

### 46. CVE-2026-81046｜Dell / ThinOS 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T16:17:57.417)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T16:17:57.417 / 2026-09-11T04:17:56.037
- **官方描述（原文）**：Dell ThinOS 10, versions prior to 2605_10.2616, contain a Protection Mechanism Failure vulnerability. An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to Arbitrary Code Execution within the application context.

### 47. CVE-2026-80424｜IBM / DataStage on Cloud Pak for Data
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T22:17:01.163)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T22:17:01.163 / 2026-09-10T22:17:01.163
- **官方描述（原文）**：IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to create arbitrary files due to path traversal during archive extraction.

### 48. CVE-2026-79724｜IBM / Langflow OSS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T22:17:00.530)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T22:17:00.530 / 2026-09-10T22:17:00.530
- **官方描述（原文）**：IBM Langflow OSS 1.0.0 through 1.11.5 could allow a remote attacker to execute arbitrary OS commands due to improper neutralization of special elements used in an OS command.

### 49. CVE-2026-78573｜IBM / ContextForge MCP Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T22:16:59.987)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T22:16:59.987 / 2026-09-10T22:16:59.987
- **官方描述（原文）**：IBM ContextForge MCP Gateway 1.0.0 through 1.0.7 could allow a remote attacker to gain administrative access due to the use of default credentials.

### 50. CVE-2026-75940｜Lenovo / Health Application
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T21:17:44.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T21:17:44.080 / 2026-09-10T21:34:43.440
- **官方描述（原文）**：A vulnerability was reported in Lenovo Health Android Application, distributed exclusively in the Chinese market, that could allow an attacker to access sensitive health-related information.

### 51. CVE-2026-68488｜WebPros / Plesk
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T17:17:05.437)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T17:17:05.437 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：A Time-of-check Time-of-use (TOCTOU) race condition leading to insecure symlink following in Plesk causes local privilege escalation to root via arbitrary file/directory ownership takeover.

### 52. CVE-2026-68487｜WebPros / Plesk
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T17:17:05.310)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T17:17:05.310 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：Path traversal in Plesk's Backup Manager causes arbitrary file write as root by an authenticated customer.

### 53. CVE-2026-65639｜WebPros / ConfigServer Security & Firewall
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T17:17:05.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T17:17:05.190 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：OS command injection in the advanced-rule parser of ConfigServer Security & Firewall allows a remote attacker who controls a configured allow/deny feed to execute arbitrary commands as root, due to insufficient validation of feed-supplied rule data. The vulnerability affects versions of the software originally distributed by ConfigServer, as well as versions of the WebPros-maintained fork that contain the vulnerable code. WebPros has addressed the vulnerability in version 16.30. Other forks or independently maintained versions of ConfigServer Security & Firewall (CSF) may also be affected and should be evaluated independently.

### 54. CVE-2026-65638｜WebPros / ConfigServer Security & Firewall
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T17:17:05.063)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T17:17:05.063 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：Improper escaping of a request URL in ConfigServer Security & Firewall allows an unauthenticated remote attacker to execute arbitrary commands as the CSF service account via shell command injection. The vulnerability affects versions of the software originally distributed by ConfigServer, as well as versions of the WebPros-maintained fork that contain the vulnerable code. WebPros has addressed the vulnerability in version 16.30. Other forks or independently maintained versions of ConfigServer Security & Firewall (CSF) may also be affected and should be evaluated independently.

### 55. CVE-2026-52098｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T17:17:04.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T17:17:04.940 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：An issue in Flowise 3.1.2 allows a remote attacker to execute arbitrary code via the /api/v1/prediction/<flowId> endpoint

### 56. CVE-2026-45764｜OISF / suricata
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T22:16:56.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T22:16:56.250 / 2026-09-10T22:16:56.250
- **官方描述（原文）**：Suricata is a network Intrusion Detection System, Intrusion Prevention System and Network Security Monitoring engine. Prior to versions 7.0.16 and 8.0.5, a protocol change while processing HTTP/2 traffic could lead to type confusion in Suricata. Crafted traffic may cause Suricata to crash, resulting in denial of service. Versions 7.0.16 and 8.0.5 contain a fix. As a workaround, disable HTTP/2 parsing if it is not required.

### 57. CVE-2026-19646｜IBM / Common Licensing
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T22:16:55.697)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T22:16:55.697 / 2026-09-10T22:16:55.697
- **官方描述（原文）**：IBM Common Licensing Agent 9.0, Agent 9.0.0.1, Agent 9.0.0.2, ART 9.0, ART 9.0.0.1, and ART 9.0.0.2 could allow a remote attacker to redirect users to an arbitrary domain due to improper validation of the HTTP Host header.

### 58. CVE-2026-88940｜knowns-dev / knowns
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T16:18:12.710)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T16:18:12.710 / 2026-09-10T19:58:20.507
- **官方描述（原文）**：knowns through 0.33.0 fails to validate the path query parameter in the workspace browse endpoint, allowing remote attackers to enumerate arbitrary directories on the host filesystem. Attackers can traverse the directory structure to locate project directories and identify targets for further exploitation.

### 59. CVE-2026-88894｜grokability / snipe-it
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:18.760)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:18.760 / 2026-09-10T16:18:11.870
- **官方描述（原文）**：Snipe-IT's predefined kit checkout path does not enforce Full Multiple Company Support (FMCS) tenant isolation on the checkout target. Unlike the single, bulk, API, accessory, license and consumable checkout paths, App\Services\PredefinedKitCheckoutService never calls $item->canCheckoutTo($target); it only performs the actor-vs-item policy check and an availability check before persisting the checkout. With FMCS enabled, a non-superuser who belongs to at least two companies and holds the assets.checkout permission can POST to /kits/{kit}/checkout with a user_id belonging only to company B and have a company-A asset (and likewise kit licenses, consumables and accessories) assigned to that user, bypassing the company-mismatch check that blocks the same operation on every other checkout path. The issue is fixed in Snipe-IT 8.7.2; it was runtime-verified on v8.6.3 and code-inspected on v8.7.1, and the affected service has lacked the check since 2019, so earlier FMCS deployments are likely also affected.

### 60. CVE-2026-88892｜Openpanel-dev / openpanel
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:18.480)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:18.480 / 2026-09-10T15:17:58.693
- **官方描述（原文）**：OpenPanel is an analytics platform. In all versions (no patched release available at time of publication), the data importer fetches a caller-supplied URL with plain fetch instead of the project's existing SSRF guard (apps/api/src/utils/safe-fetch.ts). In packages/importer/src/providers/umami.ts, parseRemoteFile calls fetch() on config.fileUrl, which is validated only by z.string().url(), so values such as http://127.0.0.1:9911/ or http://169.254.169.254/latest/meta-data/ are accepted; the shared createFileImportConfig factory gives the plausible provider the same field. An authenticated organization member — including a default 'member' with no project_access rows, for whom the intended access-level check is skipped because getProjectAccess returns boolean true rather than a level object — can therefore make the server connect to any address reachable from it. The resulting HTTP status and status text are persisted as Import.errorMessage and returned by import.get to the same user, providing a scanning oracle for internal hosts, ports and paths; if an internal response parses as Umami CSV, its rows are ingested as events and become readable in the attacker's analytics views.

### 61. CVE-2026-88055｜Mintplex-Labs / anything-llm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T18:18:14.743)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T18:18:14.743 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：AnythingLLM is an application that turns pieces of content into context that any LLM can use as references during chatting. In 1.16.1 and earlier, the manager role can store meta_page_title or meta_page_favicon through /api/admin/system-preferences, and MetaGenerator inserts those values into production homepage HTML without escaping attribute values or text content. The values pass unchanged through server/models/systemSettings.js and reach MetaGenerator.generate() in server/index.js. #assembleMeta() in server/utils/boot/MetaGenerator.js concatenates the stored values into HTML. When an administrator visits the homepage /, injected JavaScript can read the administrator JWT and use it to create API keys, access or modify workspace and chat data, delete users, and perform other administrator actions. server/endpoints/admin.js accepts the manager-controlled settings before server/models/systemSettings.js returns them unchanged. No fixed version is available as of this review.

### 62. CVE-2026-88054｜tesseract-ocr / tesseract
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T18:18:14.600)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T18:18:14.600 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：Tesseract is an open source OCR engine. In version 5.5.3 and earlier, Plumbing::DeSerialize in src/lstm/plumbing.cpp rejects excessively large network stacks but accepts a zero-length stack for NT_SERIES, NT_PARALLEL, or NT_REVERSED layers in a crafted .traineddata model. During LSTMRecognizer initialization in src/lstm/lstmrecognizer.cpp, CacheXScaleFactor(XScaleFactor()) reaches Series::CacheXScaleFactor in src/lstm/series.cpp, which dereferences stack_[0] on the empty vector and invokes a virtual method through an invalid Network pointer. This causes a deterministic crash and denial of service at model load. No fixed release is available as of this review.

### 63. CVE-2026-88050｜tesseract-ocr / tesseract
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T17:17:09.223)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T17:17:09.223 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：Tesseract is an open source OCR engine. In version 5.5.3 and earlier, RecodedCharID::DeSerialize in src/ccutil/unicharcompress.h validates length_ but accepts negative code_ values from a crafted .traineddata recoder component. UnicharCompress::ComputeCodeRange in src/ccutil/unicharcompress.cpp can consequently produce code_range_ equal to zero, after which SetupDecoder indexes is_valid_start_ with the negative code on a size-zero vector. The resulting out-of-bounds bit write uses a large wrapped index and reliably causes a wild-address crash or allocation failure on the default LSTM engine. No fixed release is available as of this review.

### 64. CVE-2026-88015｜rclone / rclone
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T16:18:08.490)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T16:18:08.490 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：rclone is a command-line program to sync files and directories to and from different cloud storage providers. Prior to 1.75.1, backend/local with --links or links=true exposes symlink targets as .rclonelink objects, and fs.RangeOption.Decode can pass an unchecked positive Range start through Object.Open and openTranslatedLink. The function slices the target string as linkdst[offset:], so a Range start larger than the target length causes a deterministic slice-bounds panic when lib/http/serve exposes the object through HTTP or WebDAV. Go net/http normally recovers the panic per connection, causing request-level denial of service rather than terminating the entire process. This issue is fixed in version 1.75.1.

### 65. CVE-2026-88790｜proma-ai / Proma
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T14:17:11.307)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 0.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T14:17:11.307 / 2026-09-10T18:18:15.513
- **官方描述（原文）**：A security vulnerability has been detected in proma-ai Proma up to 0.19.37. Affected is the function resolveTargetPath of the file apps/electron/src/main/lib/file-preview-service.ts of the component File Preview Service. Such manipulation of the argument file_path leads to path traversal. Local access is required to approach this attack. The exploit has been disclosed publicly and may be used. Upgrading to version 0.19.52 is able to address this issue. The name of the patch is b7bf78ab74b1552c92fc98c7db9a8a8d92c631df. It is suggested to upgrade the affected component. The PoC's candidateBasePaths parameter name does not match the current IPC API (0.19.52 uses FileAccessOptions with internal getPreviewCandidateBasePaths()). The reporter likely targeted 0.16.3 where the IPC handler accepted raw string[] base paths. The core vulnerability - basename-collision fallback - is independent of the parameter name and is confirmed in source.

### 66. CVE-2026-88013｜rclone / rclone
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T16:18:08.203)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.7 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T16:18:08.203 / 2026-09-10T19:54:25.810
- **官方描述（原文）**：rclone is a command-line program to sync files and directories to and from different cloud storage providers. From 1.49.0 until 1.75.1, the HTTP backend attaches headers configured through --http-headers or headers= to requests in backend/http/http.go, while its fshttp.NewClient client follows redirects without a backend-specific http.Client.CheckRedirect policy. A configured remote that redirects to another host can therefore cause custom secrets such as X-Api-Key to be resent to that untrusted destination, and a same-host HTTPS-to-HTTP redirect can expose Authorization or Cookie headers in cleartext. Listing, stat, download, mount, and serve operations can trigger the leak during normal use. This issue is fixed in version 1.75.1.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-86060｜MikroTik / RouterOS
- **Title**：MikroTik RouterOS Improper Neutralization of Argument Delimiters in a Command Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-10 / due_date=2026-09-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：MikroTik RouterOS contains an improper neutralization of argument delimiters in a command vulnerability which allows an attacked to change the trusted RouterOS policy mask, leading to privilege escalation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-67277｜MikroTik / RouterOS
- **Title**：MikroTik RouterOS Missing Authentication for Critical Function Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-10 / due_date=2026-09-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：MikroTik RouterOS contains a missing authenticaion for critical function vulnerability which allows kernel memory disclosure and denial of service in the btest service.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-20079｜Cisco / Secure Firewall Management Center (FMC) and Security Cloud Control (SCC) Firewall Management
- **Title**：Cisco Firewall Management Center Authentication Bypass Using an Alternate Path or Channel Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.74697 / percentile=0.9947
- **CISA KEV**：listed=true / date_added=2026-09-09 / due_date=2026-09-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Secure Firewall Management Center (FMC) Software and Cisco Security Cloud Control (SCC) Firewall Management contain an authentication Bypass using an alternate path or channel vulnerability that could allow an unauthenticated, remote attacker to bypass authentication and execute script files on an affected device to obtain root access to the underlying operating system.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-89086 | P3 / 38 | OCaml / jose | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89043 | P3 / 38 | krakenjs / passport-saml-encrypted | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88869 | P3 / 38 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88867 | P3 / 38 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88864 | P3 / 38 | Cap-go / capgo.app | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88044 | P3 / 38 | rclone / rclone | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88018 | P3 / 38 | rclone / rclone | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-89046 | WATCH / 30 | luben / zstd-jni | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88937 | WATCH / 30 | knowns-dev / knowns | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88924 | WATCH / 30 | Red Hat / Red Hat Enterprise Linux 10 | v3.1 7.0 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88898 | WATCH / 30 | AppFlowy-IO / AppFlowy-Cloud | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88874 | WATCH / 30 | WWBN / AVideo | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88872 | WATCH / 30 | WWBN / AVideo | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88862 | WATCH / 30 | Cap-go / capgo.app | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88060 | WATCH / 30 | angular / angular | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88049 | WATCH / 30 | tesseract-ocr / tesseract | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88045 | WATCH / 30 | rclone / rclone | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-73699 | WATCH / 30 | FileRun / FileRun | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-64838 | WATCH / 30 | ICEcoder / ICEcoder | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-45747 | WATCH / 30 | OISF / suricata | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89094 | WATCH / 28 | Forgejo / Forgejo | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89042 | WATCH / 28 | krakenjs / passport-saml-encrypted | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-88899 | WATCH / 28 | knowns-dev / knowns | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-88887 | WATCH / 28 | renovatebot / renovate | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-88882 | WATCH / 28 | renovatebot / renovate | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-88881 | WATCH / 28 | renovatebot / renovate | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-88880 | WATCH / 28 | renovatebot / renovate | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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
- EPSS 未確認：29；Exploitation status 未確認：5。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-11T05:26:50.375581+00:00`；Delta generated at：`2026-09-11T05:26:50.375581+00:00`。

---

## 可驗證資料來源

- **CVE-2026-86060** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86060) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-67277** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67277) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (mikrotik.com)](https://mikrotik.com/supportsec/september-2026-vulnerability/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-20079** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20079) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20079) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-89086** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89086)
- **CVE-2026-89043** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89043)
- **CVE-2026-88869** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88869)
- **CVE-2026-88867** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88867)
- **CVE-2026-88864** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88864)
- **CVE-2026-88044** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88044)
- **CVE-2026-88018** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88018)
- **CVE-2026-89046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89046)
- **CVE-2026-88937** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88937)
- **CVE-2026-88924** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88924)
- **CVE-2026-88898** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88898)
- **CVE-2026-88874** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88874)
- **CVE-2026-88872** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88872)
- **CVE-2026-88862** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88862)
- **CVE-2026-88060** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88060)
- **CVE-2026-88049** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88049)
- **CVE-2026-88045** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88045)
- **CVE-2026-73699** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73699)
- **CVE-2026-64838** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-64838)
- **CVE-2026-45747** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45747)
- **CVE-2026-89094** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89094)
- **CVE-2026-89042** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89042)
- **CVE-2026-88899** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88899)
- **CVE-2026-88887** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88887)
- **CVE-2026-88882** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88882)
- **CVE-2026-88881** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88881)
- **CVE-2026-88880** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88880)
- **CVE-2026-88877** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88877)
- **CVE-2026-88868** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88868)
- **CVE-2026-88866** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88866)
- **CVE-2026-88860** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88860)
- **CVE-2026-88062** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88062)
- **CVE-2026-88007** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88007)
- **CVE-2026-8778** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-8778)
- **CVE-2026-85025** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85025)
- **CVE-2026-82107** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82107)
- **CVE-2026-82100** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82100)
- **CVE-2026-81800** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81800)
- **CVE-2026-81468** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81468)
- **CVE-2026-81467** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81467)
- **CVE-2026-81204** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81204)
- **CVE-2026-81048** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81048)
- **CVE-2026-81046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81046)
- **CVE-2026-80424** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80424)
- **CVE-2026-79724** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79724)
- **CVE-2026-78573** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78573)
- **CVE-2026-75940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75940)
- **CVE-2026-68488** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-68488)
- **CVE-2026-68487** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-68487)
- **CVE-2026-65639** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65639)
- **CVE-2026-65638** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65638)
- **CVE-2026-52098** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-52098)
- **CVE-2026-45764** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45764)
- **CVE-2026-19646** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19646)
- **CVE-2026-88940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88940)
- **CVE-2026-88894** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88894)
- **CVE-2026-88892** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88892)
- **CVE-2026-88055** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88055)
- **CVE-2026-88054** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88054)
- **CVE-2026-88050** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88050)
- **CVE-2026-88015** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88015)
- **CVE-2026-88790** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88790)
- **CVE-2026-88013** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88013)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
