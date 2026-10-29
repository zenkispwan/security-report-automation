# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**34** 筆符合目前門檻的重要變化；事件統計：EPSS_INCREASED=2、NEW_CVE=30、NEW_KEV=2。
- Intelligence 候選：**30** 筆；P1 **4**、P2 **0**、P3 **0**、WATCH **26**。
- Baseline：state / generated_at=2026-10-28T06:27:38.037172+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-46300、CVE-2026-41709、CVE-2026-48356、CVE-2026-111497。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **34** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-46300｜Linux / Kernel
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.10192 / percentile=0.95651
- **CISA KEV**：listed=true / date_added=2026-10-28 / due_date=2026-10-31
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-05-23T12:17:02.660 / 2026-10-29T04:18:37.173
- **官方描述（原文）**：Linux Kernel contains a missing initialization of a variable vulnerability that could allow for unintended modification of page-cache-backed data via failure to preserve the shared-fragment marker during socket buffer coalescing, causing ESP input processing to decrypt shared fragments in place. This vulnerability can be chained with CVE-2026-109618 and CVE-2026-109619 to implant PHP webshells and run commands as root.

### 2. CVE-2026-41709｜Broadcom / VMware ESX
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 85；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 2.7 (LOW)
- **EPSS**：0.00297 / percentile=0.22291
- **CISA KEV**：listed=true / date_added=2026-10-28 / due_date=2026-11-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-07-30T14:16:57.420 / 2026-10-29T04:18:36.507
- **官方描述（原文）**：Broadcom VMWare ESX contains an insufficient logging vulnerability that could allow a malicious actor with admin access to perform certain operations without being logged.

### 3. CVE-2026-48356｜Adobe / Commerce and Magento
- **Delta event**：EPSS_INCREASED (from=0.30582; to=0.59078)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.59078 / percentile=0.9911
- **CISA KEV**：listed=true / date_added=2026-10-27 / due_date=2026-11-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-07-14T20:17:08.437 / 2026-10-28T13:34:50.330
- **官方描述（原文）**：Adobe Commerce and Magento contain an unrestricted upload of file with dangerous type vulnerability that could result in arbitrary code execution in the context of the current user, potentially gaining elevated access or control over the victim's account or session.

### 4. CVE-2026-111497｜Google / Brotli
- **Delta event**：EPSS_INCREASED (from=0.55483; to=0.87988)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.87988 / percentile=0.99763
- **CISA KEV**：listed=true / date_added=2026-10-27 / due_date=2026-11-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-22T14:17:37.190 / 2026-10-28T17:47:31.370
- **官方描述（原文）**：Google Brotli contains an unchecked return value vulnerability that allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.

### 5. CVE-2026-90717｜Dell / PowerProtect Data Domain Management Center
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T09:17:08.297)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00233 / percentile=0.14146
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T09:17:08.297 / 2026-10-28T16:17:09.697
- **官方描述（原文）**：Dell PowerProtect Data Domain Management Center, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7.13.1.80, LTS2025 release versions 8.3.1.0 through 8.3.1.40, LTS2026 release versions 8.6.1.0 through 8.6.1.20, contain an Authentication Bypass by Spoofing vulnerability. A low privileged attacker with remote access could potentially exploit this vulnerability, leading to Elevation of privileges. This vulnerability could impact other managed Data Domain systems.

### 6. CVE-2026-86400｜Dell / PowerProtect Data Domain
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T09:17:08.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00896 / percentile=0.59431
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T09:17:08.040 / 2026-10-28T14:07:11.677
- **官方描述（原文）**：Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7.13.1.80, LTS2025 release versions 8.3.1.0 through 8.3.1.40, LTS2026 release versions 8.6.1.0 through 8.6.1.20, contain an Improper Authentication vulnerability. An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to arbitrary command execution with root privileges. This is a critical severity vulnerability as it allows an attacker to take complete control of the system. Dell recommends customers to upgrade at the earliest opportunity.

### 7. CVE-2026-86397｜Dell / PowerProtect Data Domain
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T09:17:07.663)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00336 / percentile=0.26963
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T09:17:07.663 / 2026-10-28T14:07:11.677
- **官方描述（原文）**：Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7.13.1.80, LTS2025 release versions 8.3.1.0 through 8.3.1.40, LTS2026 release versions 8.6.1.0 through 8.6.1.20, contain an Improper Authentication vulnerability. An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to privileged account creation. This is a critical severity vulnerability as it allows an attacker to take complete control of the system. Dell recommends customers to upgrade at the earliest opportunity.

### 8. CVE-2026-86384｜Dell / PowerProtect Data Domain
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T10:17:09.433)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00498 / percentile=0.42569
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T10:17:09.433 / 2026-10-29T04:18:42.203
- **官方描述（原文）**：Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7.13.1.80, LTS2025 release versions 8.3.1.0 through 8.3.1.40, LTS2026 release versions 8.6.1.0 through 8.6.1.20, contain an Use of Hard-coded Cryptographic Key vulnerability. An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to credential exposure. The credentials may be used to access the system with privileges of the compromised user.

### 9. CVE-2026-67074｜HCL Software / BigFix AEX
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T13:17:08.463)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T13:17:08.463 / 2026-10-28T14:05:59.757
- **官方描述（原文）**：HCL BigFix AEX is affected by a Remote Code Execution Vulnerability . It may allow attackers to execute code with the privileges of the affected application or service, potentially leading to unauthorized access, data exposure, or system compromise.

### 10. CVE-2026-66088｜Apereo Foundation / openEQUELLA
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T02:16:52.523)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T02:16:52.523 / 2026-10-29T04:18:39.647
- **官方描述（原文）**：In openEQUELLA before 2026.1, the system.execute() function available to the scripting engine runs supplied operating system commands without validation or an allow-list of permitted executables. A user able to create or edit scripts can use it to execute arbitrary commands with the privileges of the openEQUELLA service account.

### 11. CVE-2026-63190｜fearlessgeekmedia / FearlessCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T20:18:37.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T20:18:37.470 / 2026-10-28T20:18:37.470
- **官方描述（原文）**：FearlessCMS is a flat-file `content` management system centered on simplicity and open source. Prior to version 0.1.4, five debug/test PHP scripts under `admin/` perform privileged operations without `isLoggedIn()` authentication checks, CSRF protection or adequate `path` validation. On PHP's built-in development server, including the default Docker deployment, `router.php` checks an unnormalized admin URI prefix while the filesystem resolves dot segments, so `/./admin/` bypasses the admin login gate and executes those scripts directly. In `admin/debug_save_flow.php`, attacker-controlled `path` and `content` reach `file_put_contents` for arbitrary `.md` writes under `content`/ or outside it through `path` traversal, enabling site defacement and stored JavaScript in public pages; `print_r($_POST)` output without `htmlspecialchars` escaping also causes reflected cross-site scripting. The `admin/debug_content.php` `path` parameter reaches `scandir()`, `file_get_contents()` and `posix_getpwuid()`, permitting arbitrary directory enumeration and `.md` file reads that expose absolute paths, ownership, permissions, hashes and `content` previews. The `admin/preview-handler.php` endpoint accepts JSON `content` and `title` and writes enumerable files under `content/_preview/`, enabling stored cross-site scripting and disk exhaustion. The `admin/testdebug.php` endpoint appends to `admin/testdebug.log` without authentication, also enabling disk exhaustion. The `admin/test_redirect.php` script exposes a test artifact but escapes its inputs and is not itself an XSS sink. Stored script execution can steal sessions and compromise administrators when they view affected `content`. Reads and writes execute with PHP's privileges; the tested deployment runs PHP as root, amplifying filesystem impact. This issue is fixed in version 0.1.4.

### 12. CVE-2026-61567｜WWBN / AVideo-Encoder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T22:17:15.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T22:17:15.900 / 2026-10-28T22:17:15.900
- **官方描述（原文）**：AVideo is a video-sharing Platform. Prior to 8.1.0, the live-streaming endpoint `view/videosListToLive.php` accepts an attacker-named streamer in `webSiteRootURL`, calls `Login::run` in `objects/Login.php`, and trusts the returned JSON as session state. An unauthenticated remote attacker who can host an HTTP service reachable by the encoder can self-grant `isLogged` and `canStream` without legitimate credentials. The endpoint requires only nonempty `playlists_id` and `APISecret` values; `APISecret` is forwarded rather than checked against a stored secret. This path never calls `Streamer::isURLAllowed` and therefore works regardless of the operator's streamer allowlist. It fetches a second attacker-controlled video-list response and interpolates `videos[].path` without shell argument escaping into `ffprobe` and `ffmpeg` commands passed to `exec`; `isAudio` calls `isVideo` to reach the `ffprobe` command. Paths containing shell delimiters execute arbitrary operating-system commands as the web-server user. The request filter does not inspect the video-list JSON. This can disclose database and stored streamer credentials, compromise the upstream platform using those credentials, modify files owned by the web-server user, establish persistence, and deny encoder service. This issue is fixed in version 8.1.0.

### 13. CVE-2026-61564｜WWBN / AVideo-Encoder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T22:17:15.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T22:17:15.750 / 2026-10-28T22:17:15.750
- **官方描述（原文）**：AVideo is a video-sharing Platform. Prior to 8.1.0, the unauthenticated installer endpoint `install/checkConfiguration.php` assembles `videos/configuration.php` by interpolating request parameters, including `webSiteRootURL`, into single-quoted PHP string literals without escaping. An attacker can terminate a literal and inject PHP that executes as the web-server user when the generated, directly requestable file is loaded. Exploitation requires `videos/configuration.php` to be absent, as on every fresh deployment or after the file is removed or moved; an existing file blocks this endpoint. The supplied `systemRootPath` must contain index.php and a connection using `databaseHost`, `databaseUser`, and `databasePass` must succeed, but the attacker can point those parameters to their own database server and needs no target credentials. The write location is also derived from `systemRootPath` without a base-directory constraint. This permits arbitrary command execution, reading and overwriting files owned by the web-server user, persistent PHP code, and control over stored database connection settings. The endpoint additionally interpolates request values into streamer and configuration INSERT statements, creating a secondary SQL-injection sink. This issue is fixed in version 8.1.0.

### 14. CVE-2026-44179｜xwikisas / xwiki-pro-macros
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T16:17:07.400)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T16:17:07.400 / 2026-10-28T16:17:07.400
- **官方描述（原文）**：XWiki Remote Macros provides XWiki rendering macros that are useful when migrating content from Confluence. From 1.13 until 1.14.5, the `excerpt-include` macro does not properly escape the included page's title and executes `excerpt` content with the macro's rights. The title handling in `xwiki-pro-macros-ui/src/main/resources/Confluence/Macros/ExcerptInclude.xml` and the rendering of `excerpt` content into XWiki syntax both allow syntax injection. Any user able to edit a page, even without script or programming rights, can supply executable macro syntax in the title or `excerpt` and cause remote code execution when the page is included. This affects confidentiality, integrity and availability of the whole XWiki installation. This issue is fixed in version 1.14.5.

### 15. CVE-2026-42922｜frangoteam / Frangoteam
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T04:18:36.777)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T04:18:36.777 / 2026-10-29T04:18:36.777
- **官方描述（原文）**：A authorization bypass vulnerability exists in the /nodered functionality of FUXA (version(s): 1.3.2-2809). A specially crafted HTTP request can lead to a arbitrary code execution. An attacker can make an unauthenticated HTTP request to trigger this vulnerability.

### 16. CVE-2026-14571｜Futurum Software / Futurum Software User Authentication Module
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T10:17:08.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T10:17:08.780 / 2026-10-28T14:43:13.110
- **官方描述（原文）**：A Blind SQL Injection vulnerability in Futurum Software’s management software, caused by a lack of adequate validation and sanitisation of user-provided inputs in queries to the private area’s database, as well as by an incorrect WAF configuration. This weakness allows the protection mechanisms to be bypassed solely by sending manipulated HTTP requests. Successful exploitation of the vulnerability could allow an unauthenticated attacker to execute arbitrary queries against the database, extract its complete structure and gain access to sensitive customer information, including personally identifiable information (PII).

### 17. CVE-2026-118690｜SignalK / signalk-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T22:17:13.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T22:17:13.070 / 2026-10-28T22:17:13.070
- **官方描述（原文）**：Signal K Server before 2.33.0 contains a missing authentication vulnerability that allows unauthenticated remote attackers to download log archives via the /skServer/ziplogs endpoint. Attackers can extract the JWT secretKey from security.json in the ZIP, forge administrator tokens, and create persistent admin accounts for full server control.

### 18. CVE-2026-118633｜Sophos / SG UTM
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T19:17:31.537)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T19:17:31.537 / 2026-10-28T19:17:31.537
- **官方描述（原文）**：A path traversal vulnerability allows a remote unauthenticated attacker to execute arbitrary code as root in Sophos UTM (all versions) after winning a race condition by sustaining repeated attacks for a few minutes when the email proxy is used with scanning enabled. Sophos UTM is end-of-life and the patch must be installed manually.

### 19. CVE-2026-118264｜labstack / echo
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T19:17:31.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T19:17:31.237 / 2026-10-28T19:17:31.237
- **官方描述（原文）**：Echo is a Go web framework. From 4.0.0 until 4.16.1 and 5.4.1, Echo's Proxy middleware selects a raw tunnel from a client WebSocket upgrade request before verifying that the configured upstream accepted the upgrade. If the upstream rejects the upgrade with an ordinary keep-alive response, later HTTP requests on the connection are sent directly to that upstream without passing through Echo's router or route-specific middleware. This can bypass authentication or authorization enforced only by Echo routes, but requires an accessible proxy route, a cooperating rejected-upgrade response, and a target without independent upstream authorization. This issue is fixed in 4.16.1 and 5.4.1.

### 20. CVE-2026-117574｜Red Hat / Red Hat OpenShift AI (RHOAI)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T20:17:21.417)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T20:17:21.417 / 2026-10-28T20:17:21.540
- **官方描述（原文）**：A flaw was found in ai-gateway-payload-processing. An authenticated remote attacker can exploit this vulnerability by submitting a request specifying another tenant's model identifier in the request body or header. Because the service does not verify authorization before retrieving credentials from the shared store, it injects the target tenant's application programming interface (API) keys into the request. This flaw allows an attacker to perform unauthorized requests and consume another tenant's large language model (LLM) resources and quotas.

### 21. CVE-2026-115968｜Ultimate Member / Ultimate Member
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T14:16:58.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T14:16:58.013 / 2026-10-28T16:17:06.427
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Ultimate Member Ultimate Member ultimate-member allows Object Injection.This issue affects Ultimate Member: from n/a through 2.13.1.

### 22. CVE-2026-115904｜topluyo / App
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T13:17:05.400)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T13:17:05.400 / 2026-10-28T15:24:56.033
- **官方描述（原文）**：Topluyo is a social networking platform. A vulnerability exists in Topluyo Desktop for Linux prior to version 2026.9.2410 where user-controlled URLs are unsafely processed, leading to OS Command Injection via the `openExternalLinks()` routine in `utils.js`. An attacker who controls a target URL can execute arbitrary operating system commands with the privileges of the user running the application upon opening the link. Version 2026.9.2410 patches the issue.

### 23. CVE-2026-115607｜Crowd Favorite / DXP ToolKit
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T13:17:04.993)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T13:17:04.993 / 2026-10-28T13:46:33.207
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Crowd Favorite DXP ToolKit dxp-toolkit allows SQL Injection.This issue affects DXP ToolKit: from n/a through 2.0.1.

### 24. CVE-2026-114278｜Eclipse Foundation / Eclipse Che
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T12:17:39.773)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T12:17:39.773 / 2026-10-28T15:24:56.033
- **官方描述（原文）**：The che-machine-exec service constructs a shell command by concatenating user-controlled input (the username and namespace fields from the /exec/init and /exec/config JSON endpoints) into a double-quoted sh -c "echo "..." > ..." invocation without any escaping. When che-machine-exec is run with authentication disabled (its default), any network-reachable attacker can achieve remote code execution in containers che-machine-exec is configured to access, via shell command substitution ($(...) or backticks).

### 25. CVE-2026-112197｜Tactis / NoviGest Desktop App
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T11:17:15.073)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T11:17:15.073 / 2026-10-28T14:43:13.110
- **官方描述（原文）**：Vulnerability due to a lack of authentication in critical functions of the NoviGest Desktop App's Java RMI service. An attacker with network access to the service can invoke remote methods without authentication, obtain sensitive credentials, and execute arbitrary SQL queries on PostgreSQL. The elevated privileges of the database account allow these capabilities to be chained together to execute operating system commands on the server, compromising its confidentiality, integrity, and availability.

### 26. CVE-2026-111411｜Aman / FunnelKit Automations
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T13:17:04.167)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T13:17:04.167 / 2026-10-28T16:17:01.400
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Aman FunnelKit Automations wp-marketing-automations allows Blind SQL Injection.This issue affects FunnelKit Automations: from n/a through 3.8.5.2.

### 27. CVE-2026-109516｜guruteam / Bot for Telegram on WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-29T04:18:22.763)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T04:18:22.763 / 2026-10-29T04:18:22.763
- **官方描述（原文）**：The Bot for Telegram on WooCommerce plugin for WordPress is vulnerable to Authentication Bypass leading to Account Takeover in all versions up to, and including, 1.3.0. The `/wp-json/woo-telegram/v1/main/` REST endpoint is registered with `permission_callback => '__return_true'` and performs no Telegram webhook signature verification, allowing an unauthenticated attacker to POST a forged bot update with a `message.chat.id` set to any WordPress login name; `bftow_get_user_system_id()` resolves this attacker-supplied value to the targeted account via `get_user_by('login', $tgId)` with no ownership proof, and writes a login token computed as `md5($_SERVER['HTTP_USER_AGENT'] . time())` — both inputs are fully attacker-controlled or bounded within seconds using the response's own `Date` header. The resulting token is redeemable at the unauthenticated, capability-check-free, and nonce-less `?action=bftow_create_order&bftow_token=` endpoint, which calls `wp_set_auth_cookie()` unconditionally via `login_user_by_id`, issuing a persistent authenticated session cookie for the targeted account to the attacker. This makes it possible for unauthenticated attackers to log in as any WordPress user, including administrators, given only that user's username.

### 28. CVE-2026-109218｜kleor / Contact Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T07:16:44.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00643 / percentile=0.50699
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T07:16:44.120 / 2026-10-29T02:16:46.770
- **官方描述（原文）**：The Contact Manager plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 9.1.2 via the add_message function. This is due to an incomplete extension blacklist that fails to detect dangerous extensions when a trailing dot causes the extension-derivation routine to return an empty string, which sanitize_file_name() then silently removes before the file is written to disk. This makes it possible for unauthenticated attackers to upload files that may be executable, which makes remote code execution possible. Successful code execution additionally requires the server to use Apache with libapache2-mod-php (which maps .phar to PHP by default) and the attacker to retrieve the uploaded file within the brief window before it is removed by unlink() at end of request.

### 29. CVE-2026-105420｜Wing Soft Technology / Wing FTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T14:16:56.230)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T14:16:56.230 / 2026-10-28T15:24:56.033
- **官方描述（原文）**：Wing FTP Server does not verify user's base folder. An attacker with admin privileges can add user directories via scripts, allowing the added directories to escape the base folder. This allows the attacker to write files on the system and can lead to remote code execution with process owner privileges.Critically, since the installation guide mentions running the command with `sudo`, the files are created as “root.” This issue was fixed in version 8.2.6.

### 30. CVE-2026-103799｜Dell / PowerProtect Data Domain Management Center
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T11:17:14.390)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T11:17:14.390 / 2026-10-28T14:13:52.740
- **官方描述（原文）**：Dell PowerProtect Data Domain Management Center, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7.13.1.80, LTS2025 release versions 8.3.1.0 through 8.3.1.40, LTS2026 release versions 8.6.1.0 through 8.6.1.20, contain a Missing Authorization vulnerability. A low privileged attacker with remote access could potentially exploit this vulnerability, leading to unauthorized system operation on managed systems.

### 31. CVE-2026-103792｜Dell / PowerProtect Data Domain Management Center
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T11:17:14.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T11:17:14.250 / 2026-10-29T04:18:22.133
- **官方描述（原文）**：Dell PowerProtect Data Domain Management Center, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7.13.1.80, LTS2025 release versions 8.3.1.0 through 8.3.1.40, LTS2026 release versions 8.6.1.0 through 8.6.1.20, contain an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability. A low privileged attacker with remote access could potentially exploit this vulnerability, leading to Unauthorized access to managed systems.

### 32. CVE-2026-103780｜Dell / PowerProtect Data Domain
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T11:17:14.113)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T11:17:14.113 / 2026-10-29T04:18:21.977
- **官方描述（原文）**：Dell PowerProtect Data Domain, Feature Release versions 7.7.1.0 through 8.8, LTS2024 release versions 7.13.1.0 through 7.13.1.80, LTS2025 release versions 8.3.1.0 through 8.3.1.40, LTS2026 release versions 8.6.1.0 through 8.6.1.20, contain a Stack-based Buffer Overflow vulnerability. An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to command execution.

### 33. CVE-2026-103409｜Juniper Networks / Session Smart Router
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T17:17:27.840)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T17:17:27.840 / 2026-10-28T17:17:28.083
- **官方描述（原文）**：A Missing authentication for critical function vulnerability in Juniper Networks Session Smart Router allows an unauthenticated network-based attacker to obtain administrative privileges by passing crafted URL parameters to an insecure endpoint running as root. Note that this vulnerability can only be exploited prior to the device being onboarded to Mist/Conductor. The issue can no longer be exploited once a device is onboarded to Mist/Conductor.

### 34. CVE-2026-103406｜Juniper Networks / Session Smart Conductor
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-28T17:17:25.830)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-28T17:17:25.830 / 2026-10-28T17:17:26.133
- **官方描述（原文）**：An Improper Neutralization of Special Elements used in an OS Command vulnerability in the AutomatedProvisioner in Juniper Networks Session Smart Conductor allows a remote attacker to execute arbitrary commands as root via a specially crafted salt minion ID.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-46300｜Linux / Kernel
- **Title**：Linux Kernel Missing Initialization of a Variable Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.10192 / percentile=0.95651
- **CISA KEV**：listed=true / date_added=2026-10-28 / due_date=2026-10-31
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Linux Kernel contains a missing initialization of a variable vulnerability that could allow for unintended modification of page-cache-backed data via failure to preserve the shared-fragment marker during socket buffer coalescing, causing ESP input processing to decrypt shared fragments in place. This vulnerability can be chained with CVE-2026-109618 and CVE-2026-109619 to implant PHP webshells and run commands as root.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-41709｜Broadcom / VMware ESX
- **Title**：Broadcom VMWare ESX Insufficient Logging Vulnerability
- **Risk**：P1 / score 85；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 2.7 (LOW)
- **EPSS**：0.00297 / percentile=0.22291
- **CISA KEV**：listed=true / date_added=2026-10-28 / due_date=2026-11-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Broadcom VMWare ESX contains an insufficient logging vulnerability that could allow a malicious actor with admin access to perform certain operations without being logged.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-48356｜Adobe / Commerce and Magento
- **Title**：Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.59078 / percentile=0.9911
- **CISA KEV**：listed=true / date_added=2026-10-27 / due_date=2026-11-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Adobe Commerce and Magento contain an unrestricted upload of file with dangerous type vulnerability that could result in arbitrary code execution in the context of the current user, potentially gaining elevated access or control over the victim's account or session.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-111497｜Google / Brotli
- **Title**：Google Brotli Unchecked Return Value Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.87988 / percentile=0.99763
- **CISA KEV**：listed=true / date_added=2026-10-27 / due_date=2026-11-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Brotli contains an unchecked return value vulnerability that allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-90717 | WATCH / 28 | Dell / PowerProtect Data Domain Management Center | v3.1 9.1 (CRITICAL) | 0.00233 / percentile=0.14146 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-86400 | WATCH / 28 | Dell / PowerProtect Data Domain | v3.1 9.8 (CRITICAL) | 0.00896 / percentile=0.59431 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-86397 | WATCH / 28 | Dell / PowerProtect Data Domain | v3.1 9.8 (CRITICAL) | 0.00336 / percentile=0.26963 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-86384 | WATCH / 28 | Dell / PowerProtect Data Domain | v3.1 9.8 (CRITICAL) | 0.00498 / percentile=0.42569 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-67074 | WATCH / 28 | HCL Software / BigFix AEX | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-66088 | WATCH / 28 | Apereo Foundation / openEQUELLA | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-63190 | WATCH / 28 | fearlessgeekmedia / FearlessCMS | v3.1 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-61567 | WATCH / 28 | WWBN / AVideo-Encoder | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-61564 | WATCH / 28 | WWBN / AVideo-Encoder | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-44179 | WATCH / 28 | xwikisas / xwiki-pro-macros | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-42922 | WATCH / 28 | frangoteam / Frangoteam | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-14571 | WATCH / 28 | Futurum Software / Futurum Software User Authentication Module | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-118690 | WATCH / 28 | SignalK / signalk-server | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-118633 | WATCH / 28 | Sophos / SG UTM | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-118264 | WATCH / 28 | labstack / echo | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-117574 | WATCH / 28 | Red Hat / Red Hat OpenShift AI (RHOAI) | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115968 | WATCH / 28 | Ultimate Member / Ultimate Member | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-115904 | WATCH / 28 | topluyo / App | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115607 | WATCH / 28 | Crowd Favorite / DXP ToolKit | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-114278 | WATCH / 28 | Eclipse Foundation / Eclipse Che | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-112197 | WATCH / 28 | Tactis / NoviGest Desktop App | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-111411 | WATCH / 28 | Aman / FunnelKit Automations | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-109516 | WATCH / 28 | guruteam / Bot for Telegram on WooCommerce | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-109218 | WATCH / 28 | kleor / Contact Manager | v3.1 9.8 (CRITICAL) | 0.00643 / percentile=0.50699 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105420 | WATCH / 28 | Wing Soft Technology / Wing FTP Server | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-103799 | WATCH / 28 | Dell / PowerProtect Data Domain Management Center | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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
- EPSS 未確認：21；Exploitation status 未確認：20。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-29T06:38:47.695264+00:00`；Delta generated at：`2026-10-29T06:38:47.695264+00:00`。

---

## 可驗證資料來源

- **CVE-2026-46300** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46300) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-46300) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/3599e6b3cc1ada96883d496a50a210d3afbb6987) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/2f2b16022a2e10ca7bccfb98db5ed2ec0f72641c) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/9d3e5fd19fe1063bf607219e8562fbd567b8e8d5) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/78bf6b6bb19541d19fbda6242e7cfe2c682763c0) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/760e1addc27ba1a7beb4a0a7e8b3e9ec49e7a34e) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/3bd9e113d50034db99d7ef69fd8e5242d15e414a) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/3884358a9286b17f389a72b1426fc4547c23c111) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/f84eca5817390257cef78013d0112481c503b4a3) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-41709** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-41709) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-41709) · [Vendor / Advisory (support.broadcom.com)](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48356** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48356) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48356) · [Vendor / Advisory (adobe.com)](https://www.adobe.com/trust/security/products/commerce/apsb26-73.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-111497** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111497) · [Vendor / Advisory (github.com)](https://github.com/google/brotli/releases/tag/v1.2.1) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-90717** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90717) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-90717)
- **CVE-2026-86400** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86400) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86400)
- **CVE-2026-86397** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86397) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86397)
- **CVE-2026-86384** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86384) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86384)
- **CVE-2026-67074** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67074)
- **CVE-2026-66088** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66088)
- **CVE-2026-63190** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63190)
- **CVE-2026-61567** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61567)
- **CVE-2026-61564** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61564)
- **CVE-2026-44179** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-44179)
- **CVE-2026-42922** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42922)
- **CVE-2026-14571** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14571)
- **CVE-2026-118690** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118690)
- **CVE-2026-118633** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118633)
- **CVE-2026-118264** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118264)
- **CVE-2026-117574** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-117574)
- **CVE-2026-115968** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115968)
- **CVE-2026-115904** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115904)
- **CVE-2026-115607** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115607)
- **CVE-2026-114278** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114278)
- **CVE-2026-112197** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112197)
- **CVE-2026-111411** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111411)
- **CVE-2026-109516** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109516)
- **CVE-2026-109218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109218) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109218)
- **CVE-2026-105420** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105420)
- **CVE-2026-103799** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103799)
- **CVE-2026-103792** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103792)
- **CVE-2026-103780** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103780)
- **CVE-2026-103409** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103409)
- **CVE-2026-103406** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103406)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
