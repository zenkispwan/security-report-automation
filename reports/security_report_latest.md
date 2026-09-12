# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**56** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=53、NEW_KEV=4。
- Intelligence 候選：**30** 筆；P1 **4**、P2 **0**、P3 **7**、WATCH **19**。
- Baseline：state / generated_at=2026-09-11T05:26:50.375581+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-85706、CVE-2026-84869、CVE-2026-42018、CVE-2026-42016。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **56** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-85706｜GitLab / Community Edition and Enterprise Edition
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T03:16:30.473)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-12T03:16:30.473 / 2026-09-12T04:16:44.907
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contains a path traversal vulnerability that allows an unauthenticated user to read arbitrary files due to an improper path confinement and missing authentication enforcement in the repository commits API.

### 2. CVE-2026-84869｜ConnectWise / ScreenConnect
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00382 / percentile=0.31639
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-08T20:18:51.147 / 2026-09-12T04:16:42.757
- **官方描述（原文）**：ConnectWise ScreenConnect contains both an improper privilege management and missing authorization vulnerability that may allow an attacker to file transfer and execution through an active remote sessions without authorization or host confirmation.

### 3. CVE-2026-42018｜JFrog / Artifactory
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-08-12T18:17:29.473 / 2026-09-12T04:16:33.587
- **官方描述（原文）**：JFrog Artifactory contains an improper authentication vulnerability that could return an internal anonymous-user token to an unauthenticated caller when anonymous access is disabled, potentially exposing sensitive resources.

### 4. CVE-2026-42016｜JFrog / Artifactory
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-07-27T20:16:39.613 / 2026-09-12T04:16:32.483
- **官方描述（原文）**：JFrog Artifactory contains an incorrect authorization vulnerability that allows leads to privilege escalation attack due to a validation check of the token signature/issuer and not the token’s scope.

### 5. CVE-2026-89256｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:56.003)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:56.003 / 2026-09-11T20:19:23.217
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a stored cross-site scripting vulnerability in the Bookmark plugin where chapter names are not encoded before being concatenated into public watch-page HTML. A video owner can inject malicious scripts via the bookmark name parameter, and every visitor of that video executes the payload in the AVideo origin.

### 6. CVE-2026-89255｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:55.850)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:55.850 / 2026-09-11T15:21:12.850
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a stored cross-site scripting vulnerability in the LoginControl plugin that fails to HTML-encode PGP public keys echoed into a textarea element. An authenticated attacker can inject malicious JavaScript by submitting a crafted public key, which executes in an administrator's session when viewing the user's profile tab.

### 7. CVE-2026-89253｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:55.533)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:55.533 / 2026-09-11T15:21:12.850
- **官方描述（原文）**：WWBN AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a stored cross-site scripting vulnerability in the user 'donationLink' profile field. User::setDonationLink() (objects/user.php) stores the value and save() validates it only with filter_var(..., FILTER_VALIDATE_URL), which accepts strings such as http://evil.example/"onmouseover=alert(document.domain)//, while getDonationLink() applies only strip_tags() and does not encode double quotes. plugin/CustomizeUser/actionButton.php echoes the value unencoded into an <a href="..."> attribute, and that button is included from view/modeYoutubeBottom.php on the watch page when the CustomizeUser option allowDonationLink is enabled. An authenticated user who updates their own profile via objects/userUpdate.json.php can therefore break out of the href attribute and inject an event handler that executes JavaScript in the browser of any visitor—including an administrator—who views the attacker's videos and interacts with (for example, hovers over) the donation button. The issue was unfixed at the time of reporting.

### 8. CVE-2026-89243｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:53.960)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:53.960 / 2026-09-11T15:21:12.850
- **官方描述（原文）**：WWBN AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a stored cross-site scripting vulnerability in UserGroups::setGroup_name() that fails to sanitize group_name input. Administrators with canAdminUserGroups permission can inject malicious HTML and JavaScript that executes in the browser when other administrators access the user manager interface.

### 9. CVE-2026-89010｜WAVLINK Technology / WN535M1
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T15:17:08.357)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T15:17:08.357 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：WAVLINK WN535M1 and WN535M3 routers running firmware prior to M35M1_V250922 contain an unauthenticated OS command injection vulnerability that allows remote attackers to execute arbitrary commands as root by sending crafted filenames to the sync_server daemon on TCP port 13136. The daemon interpolates attacker-controlled filename input containing shell metacharacters into a shell command string via sprintf() and passes it to system() without sanitization, enabling root-level command execution on the device.

### 10. CVE-2026-72710｜SPIP / SPIP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T17:18:58.907)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T17:18:58.907 / 2026-09-11T21:17:13.967
- **官方描述（原文）**：SPIP before 4.4.18 contains a remote code execution vulnerability in the editer_objet action where the arg parameter resolves SQL table names without enforcing an editable columns allowlist, allowing attackers with a valid nonce to inject attacker-controlled rows into the spip_jobs table. Attackers can supply arg=job/0 with crafted fonction and args values, which are later unserialized and executed when the cron job queue is drained, resulting in arbitrary PHP function execution on the underlying system.

### 11. CVE-2026-72709｜SPIP / SPIP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T17:18:58.760)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T17:18:58.760 / 2026-09-11T18:16:57.770
- **官方描述（原文）**：SPIP before 4.4.18 contains a missing authorization vulnerability in the administrative action endpoints under ecrire/action/ that allows unauthenticated attackers to perform privileged actions by supplying a valid HMAC-SHA256 nonce without any server-side permission check via autoriser(). Attackers can obtain a valid nonce, compute it for any action as the anonymous user, and invoke the editer_auteur action directly over HTTP to reset the password of any user account, including the administrator.

### 12. CVE-2026-89262｜moxi624 / MoguBlog
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T16:17:50.907)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T16:17:50.907 / 2026-09-11T19:17:47.577
- **官方描述（原文）**：MoguBlog through 6.2 contains an authorization bypass vulnerability in the comment deletion endpoint that performs ownership checks against request-body fields instead of the authenticated principal. Attackers can delete arbitrary comments and their replies by supplying comment UIDs and author UIDs obtained from unauthenticated listing endpoints.

### 13. CVE-2026-89260｜moxi624 / MoguBlog
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T16:17:50.560)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T16:17:50.560 / 2026-09-11T21:17:58.153
- **官方描述（原文）**：MoguBlog through 6.2 contains an XML external entity injection vulnerability in the WeChat callback handler at POST /wechat/wechatCheck. The WechatRestApi.index() method passes the raw request body to SignUtil.xmlToMap(), which uses an unhardened dom4j SAXReader without DTD or external-entity restrictions. Unauthenticated remote attackers can submit DOCTYPE declarations with external parameter entities to read arbitrary local files or trigger outbound HTTP requests, with resolved entities reflected in error responses.

### 14. CVE-2026-89251｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:55.223)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:55.223 / 2026-09-11T19:17:47.450
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 fails to validate ad impressions in plugin/AD_Server/log.php, allowing logged-in users to submit arbitrary label values that trigger unverified wallet credits to campaign video owners. Attackers can repeatedly POST label=start requests to mint YPTWallet balance for any campaign video without proof an ad actually played.

### 15. CVE-2026-89250｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:55.063)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:55.063 / 2026-09-11T15:21:12.850
- **官方描述（原文）**：WWBN AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains an unauthenticated file read vulnerability in the getRecordedFile.php endpoint that streams recorded FLV files from the temporary directory. Attackers can request the endpoint with a known or guessed stream key to download recorded live video files without authentication or authorization checks.

### 16. CVE-2026-89245｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:54.270)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:54.270 / 2026-09-11T15:21:12.850
- **官方描述（原文）**：WWBN AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a cross-site request forgery vulnerability in playlistRemove.php that allows attackers to delete playlists by skipping CSRF protection checks. Attackers can craft a malicious form that submits a POST request to playlistRemove.php, causing a victim's playlist to be deleted when they visit the attacker's page while logged in.

### 17. CVE-2026-89146｜libp2p / libp2p-rendezvous
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T11:16:57.867)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T11:16:57.867 / 2026-09-11T19:17:47.180
- **官方描述（原文）**：libp2p-rendezvous through 0.17.1 fails to validate registration TTL values in discovery responses, allowing attackers to trigger timer arithmetic overflow. A malicious rendezvous server can send a discovery response with an unbounded TTL value that causes the client node process to panic when computing the expiry timer.

### 18. CVE-2026-71416｜headroomlabs-ai / headroom
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T14:17:32.390)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T14:17:32.390 / 2026-09-11T15:17:03.373
- **官方描述（原文）**：Headroom compresses data before the data reaches a large language model. Prior to version 0.35.0, the Headroom WebSocket server does not validate the `Origin` header of incoming client WebSocket requests before forwarding the request to the upstream server, allowing malicious WebSocket clients to perform arbitrary LLM requests without authentication. This can be exploited by a malicious WebSocket client executed in a traditional or headless browser such as lightpanda, if the browser has access to the Headroom proxy and the OpenAI API key is stored in the `OPENAI_API_KEY` environment variable. Version 0.35.0 fixes the issue.

### 19. CVE-2026-68497｜FasterXML / jackson-databind
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T16:17:39.610)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T16:17:39.610 / 2026-09-11T17:17:46.393
- **官方描述（原文）**：jackson-databind binds a JSON string to a javax.xml.datatype.Duration or javax.xml.datatype.XMLGregorianCalendar field by passing the raw string verbatim to DatatypeFactory.newDuration(value) or newXMLGregorianCalendar(value) in CoreXMLDeserializers.Std._deserialize. These deserializers are registered by default with no opt-in, so a plain ObjectMapper or JsonMapper with no polymorphic typing and no special configuration reaches this path. The XML Schema lexical grammar permits numeric components of arbitrary length, which the JDK materializes through the native BigInteger(String) and BigDecimal(String) constructors, both quadratic in digit count. Because the digits sit inside a JSON string token rather than a JSON number token, jackson-core's StreamReadConstraints.maxNumberLength guard never applies; jackson's own NumberDeserializers call validateIntegerLength or validateFPLength before parsing a stringified number, but the XML datatype deserializer omits that pre-check. An unauthenticated attacker can therefore submit a single request of a few megabytes, such as a Duration value consisting of the letter P followed by several million digits and the letter Y, and force tens of seconds to several minutes of single-threaded CPU work; a handful of concurrent requests can saturate a server's worker threads. This affects com.fasterxml.jackson.core:jackson-databind from 2.0.0 before 2.18.10, from 2.19.0 before 2.21.6, and from 2.22.0 before 2.22.2, and tools.jackson.core:jackson-databind from 3.0.0 before 3.1.6 and from 3.2.0 before 3.2.2. Users should upgrade to 2.18.10, 2.21.6, 2.22.2, 3.1.6, or 3.2.2.

### 20. CVE-2026-90456｜CISA / Malcolm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T22:16:47.993)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T22:16:47.993 / 2026-09-11T22:16:47.993
- **官方描述（原文）**：An example environment-configuration file for a bundled inventory-management component ships with a fixed, publicly-known administrative password. A deployment that copies this example file into active configuration without running the setup routine that regenerates credentials will expose that component's administrative interface to anyone aware of the default value.

### 21. CVE-2026-89259｜gohugoio / hugo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:56.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:56.480 / 2026-09-11T21:17:57.873
- **官方描述（原文）**：Hugo is a static site generator. From v0.161.0, Hugo executes Node tools under Node's permission model, but TailwindCSS — included in the default security.exec.allow list — requires a highly permissive configuration (--allow-addons, --allow-child-process, --allow-worker). As a result, the restrictions intended by the fix for GHSA-x597-9fr4-5857 could still be bypassed, allowing a Node tool invoked during a build to read and write files outside the project's working directory. Affected versions are those after v0.43; the issue was fixed in v0.165.0 by removing tailwindcss from the default security.exec.allow list. Users who do not use TailwindCSS, or who only build trusted sites, are not affected. As a workaround, users can define a restrictive security.exec.allow list in hugo.toml.

### 22. CVE-2026-89258｜gohugoio / hugo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:56.310)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:56.310 / 2026-09-11T15:21:12.850
- **官方描述（原文）**：Hugo is a static site generator. In versions after v0.123.0 and before v0.165.0, symlinks in parent directories were not dropped during direct resource lookups, allowing path confinement to be bypassed. An attacker who can place — or who convinces a site author to place — a symlink inside a mounted directory (for example, in a locally vendored theme under themes/) can cause functions that perform direct lookups, such as resources.Get and os.ReadFile, to follow that symlink and read files outside the intended project boundaries, disclosing their contents in the built site. Themes mounted as Go modules fetched from GitHub have symlinks stripped on download and are not affected, and multi-directory walks (e.g. content/asset walking) are not affected. This issue is an incomplete-fix follow-up to GHSA-c3wq-j5vh-68rc and GHSA-fw87-fv5r-9fpw; it is fixed in v0.165.0.

### 23. CVE-2026-89254｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:55.690)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:55.690 / 2026-09-11T21:17:57.507
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a stored cross-site scripting vulnerability in the CustomizeUser plugin where the field_name parameter is stored raw without sanitization. Administrators can inject malicious scripts via the add.json.php endpoint that execute when viewing extra info pages or profile forms that render the typeToHTML function.

### 24. CVE-2026-89249｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:54.890)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:54.890 / 2026-09-11T21:17:57.147
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a stored cross-site scripting vulnerability in the YPTWallet plugin where user-supplied CryptoWallet values are base64-encoded but not HTML-escaped before storage in wallet_log.information. Administrators viewing pending withdrawal requests in pendingRequests.php execute the stored markup in their session, allowing attackers to perform administrative actions via same-origin fetch requests.

### 25. CVE-2026-89212｜Perforce / Akana
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T14:17:36.847)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T14:17:36.847 / 2026-09-11T14:17:36.847
- **官方描述（原文）**：A flaw resulting in XML external entity (XXE) was found in Akana API Platform in which references were improperly restricted during XML-to-JSON processing. The issue affects Akana versions 2026.1, 2025.1.1, and all versions before 2024.1.6 (including older unsupported versions of Akana) and has been fixed as a security patch in the latest release of supported versions.

### 26. CVE-2026-87988｜mistralai / mistral-vibe
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T15:17:07.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T15:17:07.930 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：An arbitrary file access vulnerability in Mistral Vibe allows an attacker to bypass workspace restrictions through commands classified as unconditionally allowed. Missing path validation for these commands enables access to files outside the active workspace without user approval.

### 27. CVE-2026-87987｜mistralai / mistral-vibe
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T15:17:07.793)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T15:17:07.793 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：An arbitrary code execution vulnerability in Mistral Vibe allows an attacker to bypass command permission checks using environment variable assignments preceding allowlisted commands. These assignments are excluded from inspection, enabling attacker-controlled environment variables to cause arbitrary code execution without user approval.

### 28. CVE-2026-87986｜mistralai / mistral-vibe
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T15:17:07.653)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T15:17:07.653 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：An arbitrary code execution vulnerability in Mistral Vibe allows an attacker to bypass command permission checks using shell constructs it's parser cannot interpret. Unparsed portions are omitted from inspection, enabling embedded commands to execute on the user's system without approval.

### 29. CVE-2026-87985｜mistralai / mistral-vibe
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T15:17:07.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T15:17:07.520 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：An arbitrary code execution vulnerability in Mistral Vibe allows an attacker to bypass command permission checks using ANSI-C quoted arguments. These arguments are not properly inspected, enabling a crafted allowlisted command to execute arbitrary code on the user's system without approval.

### 30. CVE-2026-87984｜mistralai / mistral-vibe
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T15:17:07.383)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T15:17:07.383 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：An arbitrary file write vulnerability in Mistral Vibe, introduced in version 1.3.4, allows an attacker to create or overwrite files outside the active workspace without user approval. Shell redirection destinations are omitted from permission checks, enabling otherwise allowlisted commands to write to arbitrary paths accessible to the Vibe process.

### 31. CVE-2026-87983｜mistralai / mistral-vibe
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T15:17:07.240)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T15:17:07.240 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：An arbitrary file read vulnerability in Mistral Vibe, introduced in version 2.6.0, allows an attacker to bypass workspace restrictions using quoted absolute paths in allowlisted shell commands. Improper handling of quotation marks during path validation enables files outside the active workspace to be read without user approval.

### 32. CVE-2026-87719｜GitLab / GitLab
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-12T03:16:31.477)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-12T03:16:31.477 / 2026-09-12T03:16:31.477
- **官方描述（原文）**：GitLab has remediated an issue in GitLab EE affecting all versions from 18.3 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2 that under certain conditions could allow an authenticated user with Duo Chat access to obtain Advanced Search instance configurations and sensitive credentials using a specially crafted GraphQL subscription argument to bypass serialization and perform server object lookup.

### 33. CVE-2026-84390｜Fortinet / FortiMonitorOnSight
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T13:18:18.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T13:18:18.980 / 2026-09-11T18:24:59.400
- **官方描述（原文）**：A inclusion of sensitive information in source code vulnerability in Fortinet FortiMonitorOnSight 7.2.4 through 7.2.7, FortiMonitorOnSight 7.2.0 through 7.2.2 may allow attacker to improper access control via <insert attack vector here>

### 34. CVE-2026-82617｜Apache Software Foundation / Apache OpenNLP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T18:16:59.443)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T18:16:59.443 / 2026-09-11T21:17:25.553
- **官方描述（原文）**：The two built-in name-finder patterns exposed by opennlp.tools.namefind.RegexNameFinderFactory - DEFAULT_REGEX_NAME_FINDER.EMAIL and DEFAULT_REGEX_NAME_FINDER.URL - contain ambiguous nested quantifiers. An application that obtains these finders through RegexNameFinderFactory.getDefaultRegexNameFinders(...) and then applies them to untrusted text through RegexNameFinder.find(String[]) or RegexNameFinder.find(String) can be driven into super-linear backtracking or into unbounded matcher recursion by a small crafted input. For the EMAIL pattern, a long run of local-part characters that is never followed by an @ forces the matcher to re-scan to end-of-input from every starting offset. Cost grows quadratically with input length: an input of approximately 32 KB consumes several seconds of CPU in a single find() call and returns no match, and each doubling of the input multiplies the cost roughly four-fold. For the URL pattern, the query-string sub-expression nests a capturing repetition inside an outer repetition. The JDK matcher recurses once per query token, so an input of approximately 4 KB containing many &-separated tokens exhausts the thread stack and causes java.lang.StackOverflowError to propagate out of find(), terminating the calling thread. On a thread created with a smaller stack (for example -Xss512k, typical of server worker pools) approximately 1 KB is sufficient. In both cases an attacker who can supply text for analysis can convert a single request into seconds to minutes of pinned CPU, or into an abrupt thread death, denying service to the embedding application. No authentication, special configuration, or model file is required beyond the application having selected one of the two built-in finders. This issue affects Apache OpenNLP: from 2.0.0 through 2.5.11; from 3.0.0-M1 through 3.0.0-M5. Users are recommended to upgrade to version 2.5.12, or to 3.0.0-M6 for users tracking the 3.0.0 milestone line, which fix the issue.

### 35. CVE-2026-80462｜Progress Software / Chef Automate
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T13:18:18.300)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T13:18:18.300 / 2026-09-11T13:18:18.300
- **官方描述（原文）**：A vulnerability in the Chef Automate API gateway and identity validation path may allow an unauthenticated actor to gain elevated access to protected Chef Automate functionality under specific conditions.

### 36. CVE-2026-79395｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T19:17:46.367)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T19:17:46.367 / 2026-09-11T20:18:54.030
- **官方描述（原文）**：An improper authentication vulnerability in the WS-Security (wsse:UsernameToken) verification routine within the Sofia IPC daemon in Xiongmai IP Camera XM530 firmware HMT.CM2005-v220608.1837 and earlier allows remote attackers to bypass authentication and execute privileged ONVIF actions (including PTZ control, stream URL retrieval, and system reboot) via a crafted SOAP request supplying the admin username with any arbitrary password when the account's stored password is empty.

### 37. CVE-2026-71644｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T14:17:32.667)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T14:17:32.667 / 2026-09-11T16:17:47.023
- **官方描述（原文）**：An issue in Robotics-STAR-Lab (SYSU STAR Group) RACER Tested affected version: commit abcdef1234567890 allows an attacker to cause unsafe trajectory planning and potential UAV collisions via a missing default case in the FSM that stops publishing swarm trajectories when the drone enters IDLE

### 38. CVE-2026-62105｜ThemeRex / ThemeREX Addons
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T19:17:43.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T19:17:43.337 / 2026-09-11T21:17:02.457
- **官方描述（原文）**：Unauthenticated PHP Object Injection in ThemeREX Addons < 2.45.0 versions.

### 39. CVE-2026-62103｜wpeverest / Everest Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T19:17:43.207)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T19:17:43.207 / 2026-09-11T21:17:11.897
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Everest Forms <= 3.6.0 versions.

### 40. CVE-2026-54072｜authorizerdev / authorizer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T19:17:42.663)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T19:17:42.663 / 2026-09-11T19:17:42.663
- **官方描述（原文）**：Authorizer is an open-source, self-hostable authentication and authorization server. Prior to version 2.2.1, the `/authorize` endpoint accepts any `redirect_uri` without validating it against `AllowedOrigins`. When `response_type=token` or `response_type=id_token`, the server appends `access_token`, `id_token`, and `refresh_token` as query parameters and issues a 302 redirect to the attacker-supplied URL. An unauthenticated attacker can obtain the required `client_id` from the public `/graphql?query={meta{client_id}}` endpoint. A partial fix was applied in v2.0.1 to other handlers (`oauth_login`, `verify_email`, `magic_link_login`, `forgot_password`, `invite_members`, `oauth_callback`) but `/authorize` was not included. Version 2.2.1 contains a more complete fix.

### 41. CVE-2026-54047｜LaciSynchroni / server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T17:17:10.477)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T17:17:10.477 / 2026-09-11T20:17:14.213
- **官方描述（原文）**：Laci Synchroni is a decentralized mod and appearance sync server and plugin for Dalamud. Versions of the backend prior to 1.2.3 have an improper authentication vulnerability in the application's OAuth2 login flow. The application relies on client-side state by trusting the `UID` field inside the `Authentications` object of a user's local `config.json` file. By manually editing this local file on their PC prior to logging in, a user can supply an arbitrary UID. Because the server fails to validate that the authenticated OAuth2 identity matches the requested UID, an attacker can fully impersonate any target user and perform actions on their behalf. This issue has been resolved in version 1.2.3. The patch modifies `AuthorizeOauthAsync` inside the `SecretKeyAuthenticatorService` to strictly bind the lookup of the requested User ID (`requestedUid`) to the record of the successfully authenticated identity (`primaryUid`). The server will no longer load or return session tokens for a requested UID unless it matches the verified, authenticated database record. No known workarounds are available.

### 42. CVE-2026-53952｜GetSimpleCMS-CE / GetSimpleCMS-CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T20:17:14.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T20:17:14.060 / 2026-09-11T20:17:14.060
- **官方描述（原文）**：GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. A logic flaw in GetSimple CMS (v3.4.0a and below) and GetSimpleCMS-CE (v3.3.22 and below) allows unauthenticated attackers to create a new administrator account. The application features an automated security control designed to delete the sensitive `admin/setup.php` file post-installation. However, this control is neutralized by a self-exclusion bug within the deletion logic, leaving the setup script accessible for unauthorized account creation even after a legitimate installation is completed. As of time of publication, no known patched versions are available.

### 43. CVE-2026-47839｜Cloud Foundry Foundation / UAA
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T10:16:51.567)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00317 / percentile=0.2435
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T10:16:51.567 / 2026-09-11T15:17:02.193
- **官方描述（原文）**：A vulnerability allows users authenticating through a federated OIDC provider to obtain the uaa.admin scope despite operators restricting that provider through externalGroupsWhitelist configuration. The issue occurs specifically when an OIDC identity provider uses groupMappingMode: AS_SCOPES with a wildcard externalGroupsWhitelist entry.

### 44. CVE-2026-3869｜Schneider Electric / Modicon M580
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T16:17:06.200)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T16:17:06.200 / 2026-09-11T20:17:13.140
- **官方描述（原文）**：CWE-303 : Incorrect Implementation of Authentication Algorithm vulnerability exists that could cause loss of confidentiality, integrity and availability of the PLC provided an application project with a lower application level is running on the PLC.

### 45. CVE-2026-38056｜ST Engineering iDirect / Evolution iQ‑Series terminals
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T15:17:01.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T15:17:01.070 / 2026-09-11T16:17:05.940
- **官方描述（原文）**：A local privilege escalation vulnerability exists in the iDirect iQ200 VSAT terminal running firmware 23.0.1.0. The iQ200 is a rackmount satellite modem deployed across oil and gas, maritime, defense, and remote infrastructure as the primary, and often sole communications link for offshore rigs, vessels, and remote sites. Important context: the device ships from the factory with a pre-configured low-privilege local user account. This account is intended for field technicians who need shell access for maintenance and diagnostics but should not have full administrative control over the device. This built-in account provides the initial access required to exploit this vulnerability. No additional credentials need to be obtained or brute-forced.

### 46. CVE-2026-14563｜Unknown / advanced-customized-prompts
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T07:16:46.177)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00136 / percentile=0.03384
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T07:16:46.177 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：The advanced-customized-prompts WordPress plugin through 1.0.1 does not verify the password before issuing an authenticated session for a supplied email address in an unauthenticated action, allowing unauthenticated attackers to log in as any registered user, including administrators, or to create arbitrary new accounts.

### 47. CVE-2026-14560｜Unknown / teddy-bear-customize-addon
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T07:16:45.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00228 / percentile=0.13467
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T07:16:45.980 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：The teddy-bear-customize-addon WordPress plugin through 1.0.5 does not properly validate uploaded files, relying on a client-supplied content type and preserving the original filename, allowing unauthenticated attackers to upload arbitrary PHP files and execute code on the server.

### 48. CVE-2026-14559｜Unknown / teddy-bear-customize-addon
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T07:16:45.877)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00136 / percentile=0.03384
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T07:16:45.877 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：The teddy-bear-customize-addon WordPress plugin through 1.0.5 does not verify a user's password before authenticating them, allowing unauthenticated attackers to log in as any registered user, including administrators, by supplying only that user's email address.

### 49. CVE-2026-89265｜moxi624 / MoguBlog
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T16:17:51.337)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T16:17:51.337 / 2026-09-11T21:17:58.457
- **官方描述（原文）**：MoguBlog through 6.2 contains an authorization bypass vulnerability in the POST /pictureSort/getPictureSortByUid endpoint, which omits the @AuthorityVerify annotation required to enforce role-based permissions. Authenticated back-office users without image-category permissions can supply a category uid to retrieve restricted image-category records including metadata such as name, cover file uid, sort order and timestamps.

### 50. CVE-2026-89264｜moxi624 / MoguBlog
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T16:17:51.193)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T16:17:51.193 / 2026-09-11T17:35:21.440
- **官方描述（原文）**：MoguBlog through 6.2 fails to validate the comment author identity in the POST /web/comment/add endpoint, allowing authenticated users to post comments attributed to any other user. Attackers can supply arbitrary userUid values in the request body to impersonate other accounts including administrators.

### 51. CVE-2026-89261｜moxi624 / MoguBlog
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T16:17:50.740)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T16:17:50.740 / 2026-09-11T20:19:23.350
- **官方描述（原文）**：MoguBlog through 6.2 exposes Elasticsearch index management endpoints in the mogu_search service without authentication, allowing remote attackers to delete, recreate, or alter the blog search index. Attackers can invoke POST endpoints to wipe the entire search index, delete specific documents, or inject malicious index entries, causing search functionality to return incorrect or no results.

### 52. CVE-2026-89248｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:54.730)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:54.730 / 2026-09-11T15:21:12.850
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 is missing an authentication/authorization check in plugin/WebRTC/status.json.php. When the WebRTC plugin is present, any unauthenticated remote user can request /plugin/WebRTC/status.json.php and receive JSON containing the absolute filesystem path of the WebRTC2RTMP helper binary (revealing the document-root path), the configured WebRTC port, file_exists/is_executable status for the binary, the contents of the WebRTC log/JSON files (videos/WebRTC2RTMP.log) when present, and whether the configured port is reachable on loopback (127.0.0.1) and on the public address. The endpoint performs no User::isLogged(), User::isAdmin(), or forbiddenPage() check. The issue was unfixed at the time of reporting.

### 53. CVE-2026-89246｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:54.423)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:54.423 / 2026-09-11T19:17:47.320
- **官方描述（原文）**：WWBN AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a CSV formula injection vulnerability in the myComments.download.php endpoint that fails to sanitize spreadsheet formula prefixes in comment text. Authenticated users can inject formulas starting with =, +, -, or @ characters that execute when administrators or video owners open the exported CSV file in spreadsheet applications.

### 54. CVE-2026-89241｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:53.650)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:53.650 / 2026-09-11T20:19:23.087
- **官方描述（原文）**：WWBN AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a reflected cross-site scripting vulnerability in confirmLivePassword.php that copies REQUEST_URI into a form action attribute without encoding. Attackers can craft a malicious URL with a quote character to break out of the action attribute and inject event handlers that execute in the victim's browser within the site origin.

### 55. CVE-2026-89240｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:53.493)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:53.493 / 2026-09-11T15:21:12.850
- **官方描述（原文）**：WWBN AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains a reflected cross-site scripting vulnerability in plugin/Live/confirmLivePassword.php. The script interpolates the unauthenticated GET parameter u (which is not covered by $securityFilter) directly into an <img src="..."> attribute without URL- or HTML-encoding. A remote attacker can craft a link containing a double-quote character in u (with a non-empty key parameter and no valid c parameter) to close the src attribute and inject an additional tag with an onerror handler, executing arbitrary JavaScript in the site's origin in the browser of any user, including an administrator, who opens the link. No patched version was available at the time of the advisory.

### 56. CVE-2026-89148｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-11T12:16:53.170)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-11T12:16:53.170 / 2026-09-11T15:21:12.850
- **官方描述（原文）**：AVideo through commit c3edcc274c389816d434acadac07ee78eaf330c1 contains an open redirect in objects/playlistSort.php. Because the endpoint is not a *.json.php script, AVideo's automatic CSRF guard (autoCSRFGuard()/forbidIfIsUntrustedRequest()) does not run, and when the request includes the sort parameter the script issues a Location header set to the unvalidated $_SERVER['HTTP_REFERER'] value without calling isSafeRedirectURL(). A remote unauthenticated attacker can therefore induce a logged-in user who can manage the targeted playlist to submit a cross-origin POST with a crafted Referer, causing the victim's playlist to be reordered and the victim's browser to be redirected from a trusted AVideo URL to an attacker-controlled site for phishing. No patched version is available.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-85706｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contains a path traversal vulnerability that allows an unauthenticated user to read arbitrary files due to an improper path confinement and missing authentication enforcement in the repository commits API.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-84869｜ConnectWise / ScreenConnect
- **Title**：ConnectWise ScreenConnect Improper Privilege Management and Missing Authorization Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00382 / percentile=0.31639
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：ConnectWise ScreenConnect contains both an improper privilege management and missing authorization vulnerability that may allow an attacker to file transfer and execution through an active remote sessions without authorization or host confirmation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-42018｜JFrog / Artifactory
- **Title**：JFrog Artifactory Improper Authentication Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JFrog Artifactory contains an improper authentication vulnerability that could return an internal anonymous-user token to an unauthenticated caller when anonymous access is disabled, potentially exposing sensitive resources.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-42016｜JFrog / Artifactory
- **Title**：JFrog Artifactory Incorrect Authorization Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JFrog Artifactory contains an incorrect authorization vulnerability that allows leads to privilege escalation attack due to a validation check of the token signature/issuer and not the token’s scope.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-89256 | P3 / 38 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89255 | P3 / 38 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89253 | P3 / 38 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89243 | P3 / 38 | WWBN / AVideo | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89010 | P3 / 38 | WAVLINK Technology / WN535M1 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-72710 | P3 / 38 | SPIP / SPIP | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-72709 | P3 / 38 | SPIP / SPIP | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-89262 | WATCH / 30 | moxi624 / MoguBlog | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89260 | WATCH / 30 | moxi624 / MoguBlog | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89251 | WATCH / 30 | WWBN / AVideo | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89250 | WATCH / 30 | WWBN / AVideo | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89245 | WATCH / 30 | WWBN / AVideo | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89146 | WATCH / 30 | libp2p / libp2p-rendezvous | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-71416 | WATCH / 30 | headroomlabs-ai / headroom | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-68497 | WATCH / 30 | FasterXML / jackson-databind | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90456 | WATCH / 28 | CISA / Malcolm | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89259 | WATCH / 28 | gohugoio / hugo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-89258 | WATCH / 28 | gohugoio / hugo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-89254 | WATCH / 28 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-89249 | WATCH / 28 | WWBN / AVideo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-89212 | WATCH / 28 | Perforce / Akana | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-87988 | WATCH / 28 | mistralai / mistral-vibe | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-87987 | WATCH / 28 | mistralai / mistral-vibe | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-87986 | WATCH / 28 | mistralai / mistral-vibe | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-87985 | WATCH / 28 | mistralai / mistral-vibe | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-87984 | WATCH / 28 | mistralai / mistral-vibe | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：26。
- EPSS 未確認：29；Exploitation status 未確認：1。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-12T05:16:44.587798+00:00`；Delta generated at：`2026-09-12T05:16:44.587798+00:00`。

---

## 可驗證資料來源

- **CVE-2026-85706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85706) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-84869** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84869) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84869) · [Vendor / Advisory (connectwise.com)](https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-42018** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42018) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/jfrog-security-advisories) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-42016** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42016) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/jfrog-security-advisories) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-89256** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89256)
- **CVE-2026-89255** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89255)
- **CVE-2026-89253** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89253)
- **CVE-2026-89243** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89243)
- **CVE-2026-89010** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89010)
- **CVE-2026-72710** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-72710)
- **CVE-2026-72709** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-72709)
- **CVE-2026-89262** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89262)
- **CVE-2026-89260** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89260)
- **CVE-2026-89251** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89251)
- **CVE-2026-89250** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89250)
- **CVE-2026-89245** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89245)
- **CVE-2026-89146** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89146)
- **CVE-2026-71416** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71416)
- **CVE-2026-68497** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-68497)
- **CVE-2026-90456** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90456)
- **CVE-2026-89259** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89259)
- **CVE-2026-89258** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89258)
- **CVE-2026-89254** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89254)
- **CVE-2026-89249** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89249)
- **CVE-2026-89212** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89212)
- **CVE-2026-87988** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87988)
- **CVE-2026-87987** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87987)
- **CVE-2026-87986** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87986)
- **CVE-2026-87985** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87985)
- **CVE-2026-87984** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87984)
- **CVE-2026-87983** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87983)
- **CVE-2026-87719** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87719)
- **CVE-2026-84390** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84390)
- **CVE-2026-82617** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82617)
- **CVE-2026-80462** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80462)
- **CVE-2026-79395** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79395)
- **CVE-2026-71644** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71644)
- **CVE-2026-62105** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62105)
- **CVE-2026-62103** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62103)
- **CVE-2026-54072** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54072)
- **CVE-2026-54047** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54047)
- **CVE-2026-53952** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53952)
- **CVE-2026-47839** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47839) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-47839)
- **CVE-2026-3869** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-3869)
- **CVE-2026-38056** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-38056)
- **CVE-2026-14563** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14563) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-14563)
- **CVE-2026-14560** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14560) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-14560)
- **CVE-2026-14559** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14559) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-14559)
- **CVE-2026-89265** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89265)
- **CVE-2026-89264** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89264)
- **CVE-2026-89261** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89261)
- **CVE-2026-89248** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89248)
- **CVE-2026-89246** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89246)
- **CVE-2026-89241** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89241)
- **CVE-2026-89240** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89240)
- **CVE-2026-89148** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89148)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
