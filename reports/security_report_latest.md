# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**89** 筆符合目前門檻的重要變化；事件統計：EXPLOITATION_CHANGED=9、NEW_CVE=78、NEW_KEV=2。
- Intelligence 候選：**30** 筆；P1 **2**、P2 **0**、P3 **6**、WATCH **22**。
- Baseline：state / generated_at=2026-10-16T05:17:55.211747+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-102764、CVE-2025-61624。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **89** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-102764｜BeyondTrust / Remote Support
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00601 / percentile=0.47647
- **CISA KEV**：listed=true / date_added=2026-10-16 / due_date=2026-10-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-15T21:17:00.117 / 2026-10-17T04:16:47.117
- **官方描述（原文）**：BeyondTrust Remote Support contains an authentication bypass by spoofing vulnerability that could allow a remote attacker to perform file operations on the appliance.

### 2. CVE-2025-61624｜Fortinet / Multiple Products
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：0.0058 / percentile=0.46551
- **CISA KEV**：listed=true / date_added=2026-10-16 / due_date=2026-10-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-04-14T16:16:31.300 / 2026-10-17T04:16:43.363
- **官方描述（原文）**：FortiOS, FortiPAM, FortiProxy, and FortiSwitchManager contain a path traversal vulnerability that may allow an authenticated attacker with admin profile and at least read-write permissions to write or delete arbitrary files via specific CLI commands.

### 3. CVE-2026-105039｜EnergizeLab / station-middleware
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00293 / percentile=0.20447
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.587 / 2026-10-16T20:17:18.590
- **官方描述（原文）**：EnergizeLab station-middleware (NestJS) Docker images 1.6.5 through 1.8.2 do not check user roles on administrative APIs. Any authenticated low-privilege user can retrieve AI provider keys and change configuration and object-store contents.

### 4. CVE-2026-105038｜EnergizeLab / FastAPI AI inference server
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00646 / percentile=0.49909
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.467 / 2026-10-16T20:17:18.490
- **官方描述（原文）**：The EnergizeLab Eilik and EilikO FastAPI AI inference and profiling services expose AI model administration functions without authentication. An unauthenticated remote attacker can change AI model configuration and switch the model in use at runtime.

### 5. CVE-2026-105037｜EnergizeLab / station-middleware
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.004 / percentile=0.32638
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.350 / 2026-10-16T20:17:18.330
- **官方描述（原文）**：EnergizeLab station-middleware (NestJS) Docker images 1.6.5 through 1.8.2 allow any registered, low-privilege account to read arbitrary files from the server by supplying an attacker-controlled file path. This exposes middleware files and server secrets.

### 6. CVE-2026-105032｜EnergizeLab / FastAPI AI inference server
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00902 / percentile=0.58994
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:03.753 / 2026-10-16T20:17:17.703
- **官方描述（原文）**：The EnergizeLab Eilik and EilikO AI skill upload endpoint, served by the FastAPI AI inference and profiling services, does not require authentication and does not constrain uploaded file paths. An unauthenticated remote attacker can use path traversal to write arbitrary files, and thereby tamper with AI skill files used by Eilik and EilikO robots.

### 7. CVE-2026-105040｜EnergizeLab / NestJS auth service
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 20；reasons：CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00348 / percentile=0.26802
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.703 / 2026-10-16T20:17:18.690
- **官方描述（原文）**：The EnergizeLab Eilik NestJS auth service accepts a user-controlled user ID in account update requests (mass assignment). A registered user can set another account's identifier and take over that account.

### 8. CVE-2026-105036｜EnergizeLab / Robot firmware (mode 104000)
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 20；reasons：CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00235 / percentile=0.13465
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.230 / 2026-10-16T20:17:18.217
- **官方描述（原文）**：EnergizeLab AI Station firmware, EilikO Linux robot firmware v2.1_20260617182218_release, and the EnergizeLab Windows desktop app 3.1.2 download firmware updates over plain HTTP and do not verify their integrity or authenticity. An attacker able to intercept or modify the traffic can substitute a malicious update.

### 9. CVE-2026-105035｜EnergizeLab / FirmwareUpdater
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 20；reasons：CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.00199 / percentile=0.09118
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.113 / 2026-10-16T20:17:18.030
- **官方描述（原文）**：The EnergizeLab FirmwareUpdater (AArch64 ELF, distributed in the CDN bin.zip) uses a single hard-coded AES key shared by all installations. An attacker who recovers the key from the updater can decrypt and forge firmware packages for any device that trusts it.

### 10. CVE-2026-105034｜EnergizeLab / NestJS auth service
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 20；reasons：CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：0.00558 / percentile=0.4527
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:03.997 / 2026-10-16T20:17:17.917
- **官方描述（原文）**：The EnergizeLab Eilik NestJS auth service issues device tokens for arbitrary robot serial numbers without authentication. An unauthenticated remote attacker can obtain a valid device token for any serial number and act as that device against the cloud services.

### 11. CVE-2026-105033｜EnergizeLab / AI Station firmware (RK3562)
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 20；reasons：CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00354 / percentile=0.27501
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:03.883 / 2026-10-16T20:17:17.817
- **官方描述（原文）**：The EnergizeLab AI Station (RK3562) firmware image ships with default root credentials and SSH enabled. An attacker with network access to the device can log in as root and take full control of it.

### 12. CVE-2026-95182｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T15:17:36.940)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T15:17:36.940 / 2026-10-16T19:56:15.773
- **官方描述（原文）**：An untrusted search path in DeepSeek Harness (dsh) commit c291e796 allows attackers to execute arbitrary code via supplying and opening crafted executable files in place of legitimate content.

### 13. CVE-2026-111708｜canove / whaticket-community
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:54.933)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:54.933 / 2026-10-16T20:17:22.847
- **官方描述（原文）**：WhaTicket Community through commit cf04795 contains an authentication bypass vulnerability that allows unauthenticated attackers to self-register as administrators via POST /auth/signup. Attackers can omit the profile field or set it to admin, gaining user management, settings, and access to all tickets, contacts, messages, and WhatsApp connections.

### 14. CVE-2026-111692｜databufflabs / databuff
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:52.633)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:52.633 / 2026-10-16T20:17:22.490
- **官方描述（原文）**：DataBuff ai-apm-web through 0.1.10 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge admin session tokens by using the hardcoded HMAC secret in JwtTokenService. Attackers can sign a payload of admin and a future expiry with the default dev-secret to gain full administrative access to protected /webapi routes, including the Doris SQL query API.

### 15. CVE-2026-111687｜rachelos / we-mp-rss
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:51.920)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:51.920 / 2026-10-16T20:17:22.260
- **官方描述（原文）**：WeRSS (we-mp-rss) through 1.5.3 contains a remote code execution vulnerability that allows unauthenticated attackers to run code via the template parameter of the public GET /rss/{feed_id} endpoint. Attackers can supply a non-built-in ext value and a {{=expression}} template whose object-subclass traversal bypasses the eval denylist to run OS commands as the service account.

### 16. CVE-2026-111673｜Thecosy / IceCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:49.920)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:49.920 / 2026-10-16T20:17:22.020
- **官方描述（原文）**：IceCMS through 4.1.5 contains a missing authentication vulnerability that allows unauthenticated attackers to modify, delete, or disable any account because /User/** is excluded from the Shiro jwt filter. Attackers can send PUT requests to /User/updateUser to set a new password and role on any userId, including administrators, enabling full account takeover.

### 17. CVE-2026-111391｜sgl-project / sglang
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T12:16:33.197)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T12:16:33.197 / 2026-10-16T14:17:23.290
- **官方描述（原文）**：SGLang 0.5.10 through 0.5.22 contains a code injection vulnerability in _evaluate_filter() that allows remote attackers to execute Python code by escaping the eval() sandbox through re.search __globals__. Attackers can send a crafted filter expression to the unauthenticated /dumper/configure endpoint when DUMPER_SERVER_PORT is set, running code in the scheduler process on the next forward pass.

### 18. CVE-2026-88755｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T15:17:33.537)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T15:17:33.537 / 2026-10-16T20:18:12.557
- **官方描述（原文）**：Z.ai ZCode v3.11.2.6792 was discovered to automatically establish connections with MCP servers declared inside a repository's workspace configuration, possibly allowing attackers to execute arbitrary code via opening a crafted repository.

### 19. CVE-2026-57488｜pupnp / pupnp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T16:18:44.823)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T16:18:44.823 / 2026-10-16T20:17:23.460
- **官方描述（原文）**：pupnp is an SDK for development of UPnP device and control point applications. Prior to 2.0.2, raw_to_int in upnp/src/genlib/net/http/httpparser.c parses Content-Length with strtol and casts the resulting long to a 32-bit int before the caller stores it as unsigned int. On LP64 systems, values greater than INT_MAX can truncate or wrap, so the HTTP parser can accept a body length different from the declared value. A remote adjacent-network peer can use the resulting parser disagreement to leave bytes to be interpreted as another request in persistent or proxied contexts, or can make a worker wait for an extremely large body and cause denial of service. This issue is fixed in 2.0.2.

### 20. CVE-2026-57486｜pupnp / pupnp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T16:18:44.510)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T16:18:44.510 / 2026-10-16T18:09:59.750
- **官方描述（原文）**：pupnp is an SDK for development of UPnP device and control point applications. Prior to 2.0.2, ixmlNode_compare in ixml/src/node.c passes the nullable nodeValue, namespaceURI, prefix, and localName fields directly to strcmp. Non-namespaced attributes created by ixmlDocument_createAttribute legitimately leave those fields NULL. When ixmlElement_removeAttributeNode compares two distinct attribute objects with the same nodeName through find_condition_node, the pointer-identity shortcut does not apply and the comparison dereferences NULL, causing a process crash when application handling of attacker-controlled XML reaches this path. This issue is fixed in 2.0.2.

### 21. CVE-2026-48503｜mz-automation / libiec61850
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T16:18:11.793)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T16:18:11.793 / 2026-10-16T20:04:29.760
- **官方描述（原文）**：libIEC61850 is an open-source implementation of IEC 61850 client and server protocols including MMS, GOOSE, Sampled Values, and R-Session. Prior to 1.6.2, the MMS file service in src/mms/iso_mms/server/mms_file_service.c accepts an out-of-range initialPosition in fileOpen and stores it in the file-read state. The fileRead path then subtracts the larger read position from the file size using unsigned arithmetic and fails to limit the response to the actual FileSystem_readFile return value. The oversized response can include stale bytes from the reused connection buffer after the requested file contents, disclosing prior response data and protocol fragments to an unauthenticated remote client when the file service is enabled. This issue is fixed in version 1.6.2.

### 22. CVE-2026-42270｜Countly / countly-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T16:17:23.940)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T16:17:23.940 / 2026-10-16T20:02:37.630
- **官方描述（原文）**：countly-server is the server-side part of Countly, a product analytics solution. Prior to 24.05.50 and 25.03.44, star-rating/images/ and dashboards/images/screenshots/ are among public image and screenshot routes using the local fs storage backend that call getStream and pipe filesystem streams to HTTP responses without an error listener. An unauthenticated request containing a URL-encoded dot can make createReadStream open a directory, emit an asynchronous EISDIR error, and terminate the Node.js process as an unhandled exception, allowing repeated requests to keep the analytics API unavailable. The affected routes also include /appimages/*, /memberimages/*, and */screenshots/*. This issue is fixed in versions 24.05.50 and 25.03.44.

### 23. CVE-2026-30971｜ZoneMinder / zoneminder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T20:17:23.190)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T20:17:23.190 / 2026-10-16T20:17:23.320
- **官方描述（原文）**：ZoneMinder is a free, open source closed-circuit television software application. Prior to 1.39.2, 1.38.2, and 1.36.40, ZoneMinder interpolates an unvalidated monitor Device field into shell commands in PHP and Perl control paths when an authenticated user with monitor-create or monitor-edit permission saves a Local monitor whose Device Path contains shell metacharacters and the monitor control or startup path runs. In this attack mechanism, the stored Device value reaches Perl qx() and backtick execution before zmdc.pl argument detainting, while separate PHP command paths use bypassable escapeshellcmd defenses. The attacker can execute arbitrary commands as the web server user. This vulnerability is fixed in 1.39.2, 1.38.2, and 1.36.40.

### 24. CVE-2026-111722｜LingGuoAI / LingGuo-Drama
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:56.823)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:56.823 / 2026-10-16T19:17:05.570
- **官方描述（原文）**：LingGuo-Drama through commit 8a6924a contains an insecure direct object reference vulnerability that allows registered users to access other users' projects because projects.Get lacks an owner check. Self-registered attackers can iterate numeric IDs via GET, PUT and DELETE /admin/v1/projects/:id to read, overwrite, reassign or delete any user's short-drama projects.

### 25. CVE-2026-111718｜kuafuai / aipexbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:56.257)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:56.257 / 2026-10-16T20:17:22.960
- **官方描述（原文）**：AipexBase through commit 690adb9 contains a sql injection vulnerability that allows attackers to inject SQL through the order_by and group_by fields of the /api/data/invoke endpoint. Attackers can supply subqueries or EXTRACTVALUE and UPDATEXML functions that bypass the SqlGuard denylist and row-level security, reading other users' rows and tables.

### 26. CVE-2026-111702｜sugarforever / chat-ollama
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:54.080)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:54.080 / 2026-10-16T19:17:05.120
- **官方描述（原文）**：ChatOllama through commit 96c3ce5 contains an insecure direct object reference vulnerability that allows remote attackers to access other users' private knowledge bases by supplying sequential ids. Attackers can enumerate ids via GET /api/knowledgebases/{id} or the knowledgebaseId parameter of POST /api/models/chat to read metadata and retrieved document content.

### 27. CVE-2026-111698｜roinli / HUIZHI-ChargeOS-cloud
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:53.490)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:53.490 / 2026-10-16T20:17:22.610
- **官方描述（原文）**：HUIZHI ChargeOS cloud through 3.0.9 contains a missing authorization vulnerability in the hcp-mp PayController.xcxRecharge endpoint that allows attackers to modify any member's wallet balance without payment. Attackers can send requests with arbitrary amount and userId parameters to credit or reduce balances and consume charging services for free.

### 28. CVE-2026-111697｜roinli / HUIZHI-ChargeOS-cloud
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:53.350)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:53.350 / 2026-10-16T19:17:05.007
- **官方描述（原文）**：HUIZHI ChargeOS cloud through 3.0.9 contains an insecure direct object reference vulnerability in the hcp-mp MeController and OrderController that trusts client-supplied userId, openId and orderNumber parameters. Attackers can enumerate sequential member ids against endpoints like /me/getMemberBalanceByUserId and /order/orderDetail to read any member's wallet, credit, profile and charging orders.

### 29. CVE-2026-111682｜smartloli / EFAK
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:51.213)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:51.213 / 2026-10-16T20:17:22.140
- **官方描述（原文）**：EFAK 5.0.0 through 5.1.0 contains a missing authorization vulnerability that allows authenticated low-privilege users to read LLM provider API keys through the /api/model-config REST API. Attackers with any ROLE_USER account can query /api/model-config/page or /api/model-config/{id} to retrieve unmasked keys, enabling provider account access and incurred costs.

### 30. CVE-2026-111642｜fastapiadmin / FastapiAdmin
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:44.877)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:44.877 / 2026-10-16T20:17:21.400
- **官方描述（原文）**：FastapiAdmin through 3.0 contains a hard-coded JWT signing secret in backend/app/config/setting.py that allows low-privileged users to forge tokens impersonating the superuser. Attackers can register via the unauthenticated /api/v1/system/user/register endpoint, log in, and forge an HS256 token keeping their session_id but naming the superuser in user_name to gain superuser privileges.

### 31. CVE-2026-111627｜hestiacp / hestiacp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:42.760)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:42.760 / 2026-10-16T20:17:20.960
- **官方描述（原文）**：HestiaCP before 1.10.5 contains an authorization bypass vulnerability that allows non-ROOT_USER administrators to perform write actions while impersonating the protected ROOT_USER account. Attackers can log in via the loginas parameter and POST to /add/cron/, because the read-only flag is never checked, causing crond to run their commands as the protected administrator's system account.

### 32. CVE-2026-111622｜a466350665 / smart-sso
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:41.980)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:41.980 / 2026-10-16T20:17:20.827
- **官方描述（原文）**：smart-sso through 2.1.1 contains an open redirect vulnerability in the /login handler that allows unauthenticated attackers to steal OAuth2 authorization codes by supplying an unvalidated redirectUri parameter. Attackers can send crafted /login links to users with active SSO sessions, then redeem stolen codes at /oauth2/access_token with any valid client credentials to obtain victims' access tokens.

### 33. CVE-2026-111612｜qaiu / netdisk-fast-download
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:40.533)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:40.533 / 2026-10-16T20:17:20.597
- **官方描述（原文）**：netdisk-fast-download through 0.4.8 contains an information disclosure vulnerability that allows unauthenticated attackers to retrieve donated netdisk credentials via the /v2/randomAuth endpoint in ParserApi. Attackers can repeatedly call the endpoint and decrypt the encryptedAuth blob using the hard-coded AES key nfd_auth_key2026 to recover other users' cloud-drive cookies, tokens, or passwords.

### 34. CVE-2026-111607｜jeequan / jeepay
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:39.813)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:39.813 / 2026-10-16T20:17:20.483
- **官方描述（原文）**：Jeepay through 3.2.9 contains an insecure direct object reference vulnerability that allows authenticated merchant users to overwrite another merchant application's payment channel configuration by supplying a victim infoId to MchPayInterfaceConfigController.saveOrUpdate. Attackers holding the default ENT_MCH_PAY_CONFIG_ADD permission can replace signing keys, certificates, and fee rates to break or redirect the victim merchant's payment processing.

### 35. CVE-2026-96620｜anthropics / claude-agent-sdk-python
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T20:18:28.293)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T20:18:28.293 / 2026-10-16T20:18:28.293
- **官方描述（原文）**：Claude Agent SDK is a Python SDK for Claude Code. Prior to 0.2.121, the resume option is passed to the Claude CLI as a separate token without validation, so a dash-leading value is parsed as an independent CLI flag. An attacker can inject the --mcp-config flag to define a stdio MCP server, causing arbitrary command execution at CLI startup outside the SDK permission controls. The issue is exploitable when an application passes untrusted input as the session ID to resume. This issue is fixed in version 0.2.121.

### 36. CVE-2026-94388｜halfdata / Green Popups
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T07:17:14.430)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.00236 / percentile=0.13606
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T07:17:14.430 / 2026-10-16T15:19:36.177
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in halfdata Green Popups halfdata-green-popups allows Blind SQL Injection.This issue affects Green Popups: from n/a before 7.6.3.

### 37. CVE-2026-94169｜Theme-one / The Grid
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T07:17:14.297)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00985 / percentile=0.61672
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T07:17:14.297 / 2026-10-16T15:19:36.177
- **官方描述（原文）**：Improper Control of Generation of Code ('Code Injection') vulnerability in Theme-one The Grid the-grid allows Command Injection.This issue affects The Grid: from n/a through 2.8.1.

### 38. CVE-2026-92262｜MariaDB / server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T17:17:52.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T17:17:52.710 / 2026-10-16T18:09:12.750
- **官方描述（原文）**：MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3.3, and 13.0.2, the #mysql50# bypass prefix is affected because it allows the #mysql50# prefix to bypass normal table-name filesystem encoding. An attacker can trigger the issue with a table name using the #mysql50# prefix, then use a #mysql50# table name to access files under their legacy unencoded name and cause crashes, data corruption, data exfiltration, or remote code execution. This issue is fixed in versions 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3.3, and 13.0.2.

### 39. CVE-2026-89079｜jfarthing84 / Theme My Login
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T06:17:12.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00294 / percentile=0.2053
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T06:17:12.410 / 2026-10-16T18:19:42.210
- **官方描述（原文）**：The Theme My Login plugin for WordPress is vulnerable to privilege escalation via account takeover in versions up to, and including, 7.2.1. This is due to the plugin not properly validating a user's identity prior to updating their password. This makes it possible for unauthenticated attackers to change arbitrary user's passwords on multi-site setups in certain configurations.

### 40. CVE-2026-85748｜MariaDB / server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T17:17:51.303)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T17:17:51.303 / 2026-10-16T18:09:12.750
- **官方描述（原文）**：MariaDB server is a community developed fork of MySQL server. From 12.3.1 until 12.3.3 and 13.0.2, SYS_REFCURSOR handling is affected because cursor-array reallocation can leave stale references in routine contexts. A low-privileged attacker can open a large number of SYS_REFCURSORs and then fetch one to trigger a use-after-free that can enable remote code execution when combined with another vulnerability. This issue is fixed in versions 12.3.3 and 13.0.2.

### 41. CVE-2026-85746｜MariaDB / server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T17:17:51.167)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T17:17:51.167 / 2026-10-16T18:19:16.007
- **官方描述（原文）**：MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3.3, and 13.0.2, ST_AsText can write beyond an allocated output buffer when converting deeply nested GeometryCollections because recursive WKT serialization does not account for bytes consumed or reserve sufficient space. A low-privileged remote attacker can submit a specially crafted GIS object to corrupt memory and potentially achieve code execution when combined with another vulnerability. This issue is fixed in versions 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3.3, and 13.0.2.

### 42. CVE-2026-57169｜Finsys / dockhand
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T17:17:35.113)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T17:17:35.113 / 2026-10-16T20:04:29.760
- **官方描述（原文）**：Dockhand is a Docker management application. Prior to 1.0.34, the in-browser container terminal endpoint /api/containers/<id>/exec does not enforce authentication on the WebSocket upgrade request. When an unauthenticated attacker has network reach to Dockhand, knows a target container ID, and targets a container with an interactive shell, the attacker can open a raw WebSocket terminal session and execute commands inside a known target container. This allows unauthenticated command execution inside the container, with possible host compromise when the container has sensitive mounts or privileged execution. This issue is fixed in version 1.0.34.

### 43. CVE-2026-49868｜RIOT-OS / RIOT
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T17:17:34.963)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T17:17:34.963 / 2026-10-16T20:04:29.760
- **官方描述（原文）**：RIOT is an open-source microcontroller operating system designed for Internet of Things devices and other embedded systems. Prior to 2026.07, _parse_reply() in sys/net/application_layer/dhcpv6/client.c omits minimum-length validation before passing IA_PD and IA_NA option bodies to sub-option parsers. A malicious or compromised DHCPv6 server can send a REPLY with an option length smaller than the required structure while MODULE_DHCPV6_CLIENT_IA_PD is enabled, causing _parse_ia_pd_option to read past the option body, size_t underflow, and unbounded out-of-bounds heap reads that can crash the device and may expose or corrupt memory. This issue is fixed in version 2026.07.

### 44. CVE-2026-44977｜Countly / countly-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T16:17:44.483)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T16:17:44.483 / 2026-10-16T20:02:37.630
- **官方描述（原文）**：countly-server is the server-side part of Countly, a product analytics solution. Prior to 24.05.50 and 25.03.44, plugins/star-rating/api/api.js allows a non-global application administrator to use uploadFeedbackFile to store attacker-controlled active content while trusting the supplied MIME type. plugins/star-rating/frontend/app.js publicly serves the stored content from feedback/preview/ with the attacker-influenced Content-Type, so a global administrator who opens the preview executes the payload in the Countly origin and exposes authenticated session capabilities, including auth_token and csrf_token values. This issue is fixed in versions 24.05.50 and 25.03.44.

### 45. CVE-2026-18516｜Arcadia Technology, LLC / Crafty Controller
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T14:17:24.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T14:17:24.710 / 2026-10-16T20:04:29.760
- **官方描述（原文）**：An output escaping vulnerability in the Audit Logs component of Crafty Controller allows a remote, unauthenticated attacker to perform stored cross-site scripting via HTTP header injection

### 46. CVE-2026-111823｜Mage / mage-ai
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-17T02:17:18.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-17T02:17:18.470 / 2026-10-17T02:17:18.470
- **官方描述（原文）**：Mage OSS through 0.9.80 before 76c4f46 can proceed with session creation upon encountering an unknown OAuth provider.

### 47. CVE-2026-111711｜Netcore / NR256CN
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:55.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:55.337 / 2026-10-16T22:17:23.053
- **官方描述（原文）**：Netcore NR256CN through 1.5.140116 contains a pre-authentication stack overflow vulnerability in the Boa web server's user_ok() function, which copies Basic-auth usernames with unbounded strcpy() calls into 64-byte stack buffers. Unauthenticated attackers can send a username longer than 63 bytes to any protected /router/*.cgi route to crash the main Boa process or potentially execute code.

### 48. CVE-2026-111704｜LangChat / langchat
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:54.370)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:54.370 / 2026-10-16T19:03:18.127
- **官方描述（原文）**：LangChat through commit 2a6285a contains a missing authentication vulnerability that allows unauthenticated remote attackers to access REST controllers because no Sa-Token interceptor is registered. Attackers can query /api/v1/auth/users to read plaintext passwords, retrieve LLM provider API keys, create super-admin accounts, and modify or delete data.

### 49. CVE-2026-111693｜databufflabs / databuff
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:52.773)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:52.773 / 2026-10-16T19:03:18.127
- **官方描述（原文）**：DataBuff ai-apm-web through 0.1.10 contains a hard-coded default credentials vulnerability that allows unauthenticated attackers to gain administrator access using the built-in admin/Databuff@123 account. Attackers can POST these credentials to /webapi/api/v1/auth/login to obtain an administrator token and access all protected /webapi routes.

### 50. CVE-2026-111691｜wimoor-erp / wimoor
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:52.493)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:52.493 / 2026-10-16T22:17:22.613
- **官方描述（原文）**：WIMOOR through commit ec86736 contains an authentication bypass vulnerability that allows attackers to impersonate any tenant and privilege level by sending an unsigned X-USERINFO header. Attackers reaching backend service ports directly, bypassing the gateway, can forge companyid and manager or admin usertype values to read and modify other tenants' orders, finance data, and Amazon seller authorizations.

### 51. CVE-2026-111690｜suyuan32 / simple-admin-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:52.350)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:52.350 / 2026-10-16T19:03:18.127
- **官方描述（原文）**：Simple Admin Core through 1.8.7 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge super administrator tokens by using the hard-coded Auth.AccessSecret in api/etc/core.yaml. Attackers can sign a JWT with the public secret and roleId claim 001 to gain full administrative control over users, roles, menus, API authorities, configuration and tokens.

### 52. CVE-2026-111675｜xiaochong0302 / course-tencent-cloud
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:50.197)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:50.197 / 2026-10-16T19:03:18.127
- **官方描述（原文）**：Course-tencent-cloud through 2.0.1 contains an improper restriction of authentication attempts vulnerability that allows unauthenticated attackers to brute force 6-digit SMS/email verification codes, which are never invalidated or attempt-limited. Attackers who know a victim's phone or email can trigger a code and rotate source IPs against the password reset and verify login endpoints to take over accounts.

### 53. CVE-2026-111663｜chaskiq / chaskiq
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:48.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:48.077 / 2026-10-16T19:03:18.127
- **官方描述（原文）**：Chaskiq through 2.0.3 contains a server-side request forgery vulnerability that allows unauthenticated attackers to fetch arbitrary URLs via the createUrlUpload GraphQL mutation. Attackers can submit internal URLs, including cloud instance metadata endpoints, through POST /graphql and retrieve the full response via the returned ActiveStorage blob URL.

### 54. CVE-2026-111643｜l429609201 / misaka_danmu_server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:45.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:45.013 / 2026-10-16T19:03:18.127
- **官方描述（原文）**：Misaka Danmu Server through 2.8.9 contains an authentication bypass vulnerability that allows unauthenticated attackers to write arbitrary configuration keys via the unprotected POST /api/ui/config-history/rollback endpoint. Attackers can set the ipWhitelist key to their own /32 address, or alter trustedProxies and webhookApiKey, to access every protected endpoint as the administrator.

### 55. CVE-2026-111641｜fastapiadmin / FastapiAdmin
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:44.730)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:44.730 / 2026-10-16T22:17:21.500
- **官方描述（原文）**：FastapiAdmin through 3.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to obtain sessions for any user by abusing unprotected auto-login endpoints. Attackers can list users via /api/v1/auth/auto-login/users, mint a superuser auto-login token, and exchange it for a JWT session to gain full administrative control.

### 56. CVE-2026-111636｜OpenBMB / StaffDeck
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:44.010)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:44.010 / 2026-10-16T22:17:21.390
- **官方描述（原文）**：OpenBMB StaffDeck through 0.5.6 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge administrator session tokens using the hard-coded default app_secret. Attackers can sign an HMAC-SHA256 token for the seeded 'admin' user in 'tenant_demo' to gain full tenant administration, including stored model and channel credentials.

### 57. CVE-2026-111626｜Webreaper / Damselfly
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:42.583)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:42.583 / 2026-10-16T22:17:21.177
- **官方描述（原文）**：Webreaper Damselfly through 4.5.3 contains an authentication bypass vulnerability that allows unauthenticated attackers to access all /api/* routes because controller authorization attributes are commented out. Attackers can send PUT /api/users with Admin roles to create administrator accounts, or POST /api/users to reset any user's password, gaining full control.

### 58. CVE-2026-111472｜TSG / Profleet
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T09:17:04.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00228 / percentile=0.12587
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T09:17:04.410 / 2026-10-16T15:19:36.177
- **官方描述（原文）**：An SQL injection vulnerability has been discovered in TSG Profleet. The vulnerability could allow an attacker to retrieve, create, update and delete data from the database by sending a GET request using the ‘Identificación’ parameter of the ‘/cgi-bin/index.php’ endpoint.

### 59. CVE-2026-110653｜latepoint / Appointment Booking Plugin – LatePoint | Calendar & Scheduling for WordPress
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-17T03:16:28.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-17T03:16:28.480 / 2026-10-17T03:16:28.480
- **官方描述（原文）**：The Appointment Booking Plugin – LatePoint | Calendar & Scheduling for WordPress plugin for WordPress is vulnerable to Authentication Bypass via Race Condition in all versions up to, and including, 5.7.4. This is due to a non-atomic read-modify-write on the OTP verification attempts counter in the `verifyOTP` function: the counter is incremented using a stale in-memory value with no conditional `WHERE attempts < 10` guard on the `UPDATE` and no `SELECT ... FOR UPDATE` row lock, creating a TOCTOU window that allows concurrent requests to bypass the 10-attempt lockout. This makes it possible for unauthenticated attackers — who know a target customer's registered email address or phone number — to fire concurrent requests to the `auth__verify_otp` endpoint, defeat the lockout cap, brute-force the 6-digit OTP code, and authenticate as the targeted LatePoint customer, gaining full access to their account, bookings, and personal data. The nonce check present on the endpoint (`otp_verify_otp_nonce`) does not mitigate this issue, as the nonce is publicly emitted by the unauthenticated `request_otp` and `resend_otp` endpoints and is trivially obtainable by any unauthenticated attacker prior to launching the race.

### 60. CVE-2026-109588｜FreeRTOS / FreeRTOS-Kernel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:31.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:31.457 / 2026-10-16T20:02:37.630
- **官方描述（原文）**：Numeric truncation of the buffer length in the MPU buffer authorization check in FreeRTOS-Kernel V11.3.0 and V11.3.1 on the Arm Cortex-R82 (Armv8-R AArch64) MPU port might allow, under certain conditions, an unprivileged task on MPU-enabled builds to read or write privileged kernel memory beyond the validated buffer window, via a stream buffer system call. To remediate this issue, users should upgrade to version V11.3.2 or later.

### 61. CVE-2026-109587｜FreeRTOS / FreeRTOS-Kernel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:31.330)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:31.330 / 2026-10-16T20:02:37.630
- **官方描述（原文）**：Incorrect authorization in the Arm Cortex-R82 (Armv8-R AArch64) MPU port in FreeRTOS-Kernel V11.3.0 and V11.3.1 might allow an unprivileged task on MPU-enabled builds to read and write privileged kernel memory outside the regions assigned to it, via a buffer argument passed to an MPU system call. To remediate this issue, users should upgrade to version V11.3.2 or later.

### 62. CVE-2026-107617｜Guangzhou Juan IoT Technology Co., Ltd. / EseeCloud App
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T14:17:16.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T14:17:16.510 / 2026-10-16T20:04:29.760
- **官方描述（原文）**：An attacker can use a hard-coded credential to log in to EseeCloud devices.

### 63. CVE-2026-105279｜J4Care / dcm4chee-arc-light
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T15:17:04.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T15:17:04.130 / 2026-10-16T20:04:29.760
- **官方描述（原文）**：In the default configuration, the archive accepts DICOM associations from an unregistered calling AE. A remote peer can use C-FIND and C-GET to enumerate and retrieve patient information and medical images. It can also use C-STORE to file fabricated study content under an existing patient identity.

### 64. CVE-2026-104736｜thimpress / LearnPress – WordPress LMS Plugin for Create and Sell Online Courses
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-17T04:16:47.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-17T04:16:47.780 / 2026-10-17T04:16:47.780
- **官方描述（原文）**：The LearnPress plugin for WordPress is vulnerable to PHP Object Injection in versions up to, and including, 4.4.10 via deserialization of untrusted input from the 'checkout-email' request parameter during the checkout AJAX action. The value is passed through sanitize_text_field(), which does not strip serialized object syntax, then stored in the LearnPress session table and later fed to LP_Helper::maybe_unserialize() → unserialize() (without an allowed_classes restriction) by LP_Session_Handler::get() on subsequent requests. This makes it possible for unauthenticated attackers to inject a PHP Object.

### 65. CVE-2026-104730｜sunshinephotocart / Sunshine Photo Cart – Client Photo Gallery & Photo Proofing for Photographers
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T07:17:08.267)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00512 / percentile=0.42323
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T07:17:08.267 / 2026-10-16T15:17:03.460
- **官方描述（原文）**：The Sunshine Photo Cart – Client Photo Gallery & Photo Proofing for Photographers plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 3.7.4 via deserialization of untrusted input . This makes it possible for unauthenticated attackers to inject a PHP Object. No known POP chain is present in the vulnerable software, which means this vulnerability has no impact unless another plugin or theme containing a POP chain is installed on the site. If a POP chain is present via an additional plugin or theme installed on the target system, it may allow the attacker to perform actions like delete arbitrary files, retrieve sensitive data, or execute code depending on the POP chain present. If a POP chain is present via an additional plugin or theme installed on the target system, the attacker can store the malicious payload unauthenticated via the public favorites page and trigger deserialization by viewing any image in a non-viewable or private gallery.

### 66. CVE-2026-103768｜elextensions / ELEX WordPress HelpDesk & Customer Ticketing System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T06:17:03.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00578 / percentile=0.46405
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T06:17:03.060 / 2026-10-16T15:17:02.553
- **官方描述（原文）**：The ELEX WordPress HelpDesk & Customer Ticketing System plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 3.3.7 via the initMailPart function. This is due to insufficient file type validation when saving IMAP email attachments. This makes it possible for unauthenticated attackers to upload files that may be executable, which makes remote code execution possible.

### 67. CVE-2026-102693｜RIOT-OS / RIOT
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T17:17:17.173)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T17:17:17.173 / 2026-10-16T20:17:17.397
- **官方描述（原文）**：RIOT is an open-source microcontroller operating system designed for Internet of Things devices and other embedded systems. Prior to 2026.04, the ATWINC15x0 driver's _atwinc15x0_sta_set_current_ssid function uses strcpy to copy an SSID without checking the destination size. When MODULE_ATWINC15X0_DYNAMIC_CONNECT is enabled, a nearby attacker can advertise a malformed or oversized SSID that is processed during Wi-Fi scanning, causing memory corruption and potentially a hard fault, denial of service, or code execution. This issue is fixed in version 2026.04.

### 68. CVE-2026-102692｜RIOT-OS / RIOT
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T17:17:16.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T17:17:16.980 / 2026-10-16T22:17:08.800
- **官方描述（原文）**：RIOT is an open-source microcontroller operating system designed for Internet of Things devices and other embedded systems. Prior to 2026.07, nanocoap accepts oversized CoAP Block2 option values without enforcing the 20-bit maximum block number, allowing block offset multiplication to overflow on 32-bit targets. The affected master baseline is commit aeeae69e; the verified fix is later on master and remains unreleased. The oversized value passes from coap_get_blockopt() to coap_block_slicer_init(). A remote CoAP client can send a malformed Block2 option that produces an invalid slice range and can cause out-of-bounds memory access, denial of service, or memory corruption. This vulnerability is fixed in 2026.07.

### 69. CVE-2026-102608｜ZoneMinder / zoneminder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T20:17:17.253)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T20:17:17.253 / 2026-10-16T20:17:17.363
- **官方描述（原文）**：ZoneMinder is a free, open source closed-circuit television software application. Prior to 1.38.3, downloadEvents() manually wraps a monitor Name value in single quotes instead of using escapeshellarg() before placing it in shell commands when a user with monitor-create or monitor-edit permission stores a monitor Name containing shell metacharacters and a user with Events View permission exports that monitor's events. In this attack mechanism, the stored monitor Name reaches both the ffmpeg concatenation command and the tar or zip archive command and breaks out of manual quoting. Arbitrary commands execute as the web server user. This issue is fixed in version 1.38.3.

### 70. CVE-2026-102551｜FreeRTOS / FreeRTOS-Plus-TCP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:14.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:14.750 / 2026-10-16T20:02:37.630
- **官方描述（原文）**：Improper verification of the source of a communication channel in the IPv6 Router Advertisement handler in Amazon FreeRTOS-Plus-TCP before V4.4.2 might allow a remote third-party to influence an endpoint's IPv6 default gateway, on-link prefix, and address configuration via a crafted Router Advertisement. To remediate this issue, users should upgrade to version V4.4.2.

### 71. CVE-2026-68908｜mz-automation / libiec61850
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T16:20:01.140)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T16:20:01.140 / 2026-10-16T20:04:29.760
- **官方描述（原文）**：libIEC61850 is an open-source implementation of IEC 61850 client and server protocols including MMS, GOOSE, Sampled Values, and R-Session. Prior to 1.6.2, Reporting_RCBWriteAccessHandler accepts an RptID longer than 129 bytes in the report-control-block write path. When GI later causes sendNextReportEntrySegment to serialize the report, the function wraps rptIdBuf[130] as a temporary MmsValue and passes it to MmsValue_setVisibleString. The setter's resize path frees the stack-backed buffer, allowing a remote client to trigger an invalid free and server crash by writing the oversized RptID and then generating a report. This issue is fixed in version 1.6.2.

### 72. CVE-2026-59966｜TandoorRecipes / recipes
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T20:17:23.700)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.7 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T20:17:23.700 / 2026-10-16T20:17:23.700
- **官方描述（原文）**：Tandoor Recipes is an application for managing recipes, planning meals, and building shopping lists. Prior to 2.6.10, executes user-controlled Automation regular-expression patterns with Python re.sub() without complexity validation or an execution timeout when an authenticated user stores a catastrophic-backtracking regex and any user in the same Space imports a matching recipe. Request processing uses Automation.param_2, apply_regex_replace_automation, sub, api/recipe-from-source/. The attack works because the shared-Space automation engine evaluates the malicious pattern during recipe import and can occupy a Gunicorn worker until its request timeout. This can exhaust application worker slots and make the service unavailable to users. This issue is fixed in version 2.6.10.

### 73. CVE-2026-55862｜pupnp / pupnp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T16:18:44.060)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T16:18:44.060 / 2026-10-16T20:17:23.363
- **官方描述（原文）**：pupnp is an SDK for development of UPnP device and control point applications. Prior to 2.0.0, multiple ixml DOM traversal functions process deeply nested XML with unbounded recursion. The iterative XML parser accepts the document, but ixmlPrintDomTreeRecursive in ixml/src/ixml.c and ixmlNode_getElementsByTagNameRecursive, ixmlNode_getElementsByTagNameNSRecursive, ixmlNode_cloneNodeTreeRecursive, and ixmlNode_isAncestor in ixml/src/node.c recurse over firstChild and nextSibling links. An unauthenticated peer on the local network can supply deeply nested XML through a SOAP request, exhaust a service thread's stack, and crash the UPnP service. This is an incomplete-fix case for CVE-2021-28302 because its remediation converted ixmlNode_free but left these traversal paths recursive. This issue is fixed in 2.0.0.

### 74. CVE-2026-55836｜open-zaak / open-zaak
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T16:18:43.897)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T16:18:43.897 / 2026-10-16T20:04:29.760
- **官方描述（原文）**：Open Zaak is an open-source data and services layer for Dutch case-oriented working. From 1.13.0 until 1.27.2, 1.28.2, and 1.29.0, _import_document_row in src/openzaak/components/documenten/tasks.py uses the attacker-controlled bestandspad CSV field without ensuring that the resolved path remains under IMPORT_DOCUMENTEN_BASE_DIR. A client with an all-authorizations application token can supply an absolute or parent-traversal path to a file readable by the Celery service account. The worker copies that file into document storage, allowing its contents to be retrieved through the normal document download API and exposing server secrets or other private files. This issue is fixed in versions 1.27.2, 1.28.2, and 1.29.0.

### 75. CVE-2026-111717｜nduckmink / arkon
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:56.130)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:56.130 / 2026-10-16T19:17:05.457
- **官方描述（原文）**：Arkon through 0.9.2 contains a missing authorization vulnerability in list_skill_versions that allows authenticated employees to read other departments' skill version metadata by bypassing the can_access_skill check. Attackers holding the default skill:read permission can request GET /api/skills/{slug}/versions for another department's skill to obtain version numbers, hashes, storage paths and changelogs.

### 76. CVE-2026-111707｜vastxie / 99AI
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:54.803)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:54.803 / 2026-10-16T19:17:05.233
- **官方描述（原文）**：99AI through 4.3.0 contains an insecure direct object reference vulnerability that allows unauthenticated attackers to read other users' chat messages because querySingleChat lacks an owner check. Attackers can send a fingerprint header to obtain a visitor JWT and iterate sequential chatId values to retrieve other users' message content and task data.

### 77. CVE-2026-111703｜guchengwuyue / yshop-crm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:54.213)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:54.213 / 2026-10-16T20:17:22.730
- **官方描述（原文）**：yshop-crm through 2.1.3 contains an insecure direct object reference vulnerability that allows authenticated sales users to access other users' customer records by supplying arbitrary ids. Attackers can enumerate ids against the get, update, delete and do-open endpoints to read contact details, overwrite or delete customers, or release them into the public pool.

### 78. CVE-2026-111688｜Exrick / xboot
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:52.063)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:52.063 / 2026-10-16T21:17:24.157
- **官方描述（原文）**：Exrick XBoot through 3.3.4 contains an authorization bypass vulnerability that allows authenticated users to evade role data-scope restrictions by sending openDataFilter=false. Attackers can append this parameter to the department getByParentId or search endpoints to retrieve the entire organization's department tree and names outside their assigned scope.

### 79. CVE-2026-111677｜Adri van Os / antiword
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:50.477)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:50.477 / 2026-10-16T19:17:04.880
- **官方描述（原文）**：Antiword through 0.37 contains a heap out-of-bounds read vulnerability in vGet8LstInfo in prop8.c caused by an inverted bounds check on the PlcfLst record count. Attackers can supply a crafted Word 8 .doc file claiming up to 0xffff LSTF records in a tiny buffer, causing reads past the heap allocation that crash the process.

### 80. CVE-2026-111672｜data-infra / cube-studio
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:49.790)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:49.790 / 2026-10-16T19:17:04.760
- **官方描述（原文）**：Cube-studio through 2026.09.01 contains a missing authorization vulnerability in myapp/views/view_pipeline.py that allows authenticated users to view or copy other project groups' pipelines by id. Attackers can enumerate sequential pipeline ids via the web, log, monitoring, pod, and copy_pipeline endpoints to expose DAGs, cluster names, namespaces, Argo workflow ids, and pod names, or clone pipelines.

### 81. CVE-2026-111667｜getrebuild / rebuild
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:48.660)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:48.660 / 2026-10-16T19:17:04.653
- **官方描述（原文）**：REBUILD through 4.5.0 contains a missing authorization vulnerability in TaskCommentController.commentList that allows authenticated low-privileged users to read task comments without project membership checks. Attackers can supply the id of a task in a private project to the /project/comments/list endpoint to retrieve its comment content and attachment references.

### 82. CVE-2026-111662｜chaskiq / chaskiq
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:47.900)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:47.900 / 2026-10-16T20:17:21.893
- **官方描述（原文）**：Chaskiq through 2.0.3 contains a server-side request forgery vulnerability that allows unauthenticated attackers to make the server fetch arbitrary URLs via the url parameter of the /oembed endpoint. Attackers can target loopback, private, or cloud-metadata addresses through FetchLinkCardService, which follows redirects and skips TLS verification, to read internal page titles and descriptions.

### 83. CVE-2026-111657｜beikeshop / beikeshop
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:47.083)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:47.083 / 2026-10-16T20:17:21.773
- **官方描述（原文）**：BeikeShop through 2.0.0.31 contains an insecure direct object reference vulnerability in the markAsShipped handler of RmaController that allows authenticated customers to modify other customers' returns. Attackers can submit sequential RMA ids to the account/rmas/{id}/mark_as_shipped endpoint to overwrite courier names and tracking numbers and mark approved returns as shipped.

### 84. CVE-2026-111652｜3xxx / engineercms
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:46.360)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:46.360 / 2026-10-16T20:17:21.647
- **官方描述（原文）**：Engineercms through 2.0.5 contains a missing authorization vulnerability in AttachController.Attachment that allows unauthenticated attackers to download project image and video attachments. Attackers can request known or derived /attachment/* paths for .jpg, .png, .bmp, or .mp4 files, which are served before casbin, owner, or admin checks.

### 85. CVE-2026-111647｜PickMall / lilishop
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:45.597)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:45.597 / 2026-10-16T20:17:21.523
- **官方描述（原文）**：PickMall lilishop through 5.0.0 contains an insecure direct object reference vulnerability that allows authenticated buyers to read other buyers' invoice records because ReceiptServiceImpl.getDetail performs no ownership check. Attackers can supply another buyer's receipt id to GET /buyer/trade/receipt/{id} to obtain invoice titles, taxpayer identification numbers, order numbers, member ids and member names.

### 86. CVE-2026-111637｜Blair2004 / NexoPOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:44.157)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:44.157 / 2026-10-16T20:17:21.290
- **官方描述（原文）**：NexoPOS through 6.2.4 contains a missing authentication vulnerability that allows unauthenticated attackers to read accounting transaction records via GET /api/fields/{resource}/{identifier}. Attackers can request transaction field classes like ns.entity-transaction with sequential ids to retrieve names, values, account ids, and descriptions without nexopos.read.transactions permission.

### 87. CVE-2026-111632｜aureuserp / aureuserp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:43.470)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:43.470 / 2026-10-16T20:17:21.170
- **官方描述（原文）**：Aureus ERP through 1.6.0 contains an authorization bypass vulnerability that allows authenticated API users to create or move records into disallowed companies by supplying a foreign company_id. Attackers can submit create or update requests to plugin REST API endpoints such as partners, sales, or inventories to break multi-company data segregation.

### 88. CVE-2026-111617｜MGdaasLab / WHartTest
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:41.250)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:41.250 / 2026-10-16T20:17:20.710
- **官方描述（原文）**：WHartTest through 2.8.1 contains a missing authentication vulnerability that allows unauthenticated attackers to connect to the /ws/ui/web/ and /ws/ui/actuator/ WebSocket endpoints because UiAutomationConsumer accepts every connection. Attackers can register an actuator with a client-supplied id to intercept other users' test-case payloads, receive broadcast step results, and spoof results and screen frames into victim sessions.

### 89. CVE-2026-111392｜sgl-project / sglang
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T18:17:38.950)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T18:17:38.950 / 2026-10-16T20:17:20.370
- **官方描述（原文）**：SGLang through 0.5.21 trusts caller-supplied mm_hashes values as the multimodal prefix-cache key, allowing remote attackers to poison cached KV entries across requests. Attackers can send a different image under a known or predicted hash via /generate to disclose another request's image content or corrupt victims' responses.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-102764｜BeyondTrust / Remote Support
- **Title**：BeyondTrust Remote Support Authentication Bypass by Spoofing Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00601 / percentile=0.47647
- **CISA KEV**：listed=true / date_added=2026-10-16 / due_date=2026-10-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：BeyondTrust Remote Support contains an authentication bypass by spoofing vulnerability that could allow a remote attacker to perform file operations on the appliance.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2025-61624｜Fortinet / Multiple Products
- **Title**：Fortinet Multiple Products Path Traversal Vulnerability
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：0.0058 / percentile=0.46551
- **CISA KEV**：listed=true / date_added=2026-10-16 / due_date=2026-10-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：FortiOS, FortiPAM, FortiProxy, and FortiSwitchManager contain a path traversal vulnerability that may allow an authenticated attacker with admin profile and at least read-write permissions to write or delete arbitrary files via specific CLI commands.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-95182 | P3 / 38 | 未確認 / 未確認 | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111708 | P3 / 38 | canove / whaticket-community | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111692 | P3 / 38 | databufflabs / databuff | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111687 | P3 / 38 | rachelos / we-mp-rss | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111673 | P3 / 38 | Thecosy / IceCMS | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111391 | P3 / 38 | sgl-project / sglang | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-105039 | WATCH / 28 | EnergizeLab / station-middleware | v3.1 9.6 (CRITICAL) | 0.00293 / percentile=0.20447 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105038 | WATCH / 28 | EnergizeLab / FastAPI AI inference server | v3.1 9.8 (CRITICAL) | 0.00646 / percentile=0.49909 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105037 | WATCH / 28 | EnergizeLab / station-middleware | v3.1 9.9 (CRITICAL) | 0.004 / percentile=0.32638 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105032 | WATCH / 28 | EnergizeLab / FastAPI AI inference server | v3.1 9.1 (CRITICAL) | 0.00902 / percentile=0.58994 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105040 | WATCH / 20 | EnergizeLab / NestJS auth service | v3.1 8.8 (HIGH) | 0.00348 / percentile=0.26802 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105036 | WATCH / 20 | EnergizeLab / Robot firmware (mode 104000) | v3.1 7.5 (HIGH) | 0.00235 / percentile=0.13465 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105035 | WATCH / 20 | EnergizeLab / FirmwareUpdater | v3.1 7.8 (HIGH) | 0.00199 / percentile=0.09118 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105034 | WATCH / 20 | EnergizeLab / NestJS auth service | v3.1 8.2 (HIGH) | 0.00558 / percentile=0.4527 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105033 | WATCH / 20 | EnergizeLab / AI Station firmware (RK3562) | v3.1 8.8 (HIGH) | 0.00354 / percentile=0.27501 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-88755 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57488 | WATCH / 30 | pupnp / pupnp | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-57486 | WATCH / 30 | pupnp / pupnp | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-48503 | WATCH / 30 | mz-automation / libiec61850 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-42270 | WATCH / 30 | Countly / countly-server | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-30971 | WATCH / 30 | ZoneMinder / zoneminder | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111722 | WATCH / 30 | LingGuoAI / LingGuo-Drama | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111718 | WATCH / 30 | kuafuai / aipexbase | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111702 | WATCH / 30 | sugarforever / chat-ollama | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111698 | WATCH / 30 | roinli / HUIZHI-ChargeOS-cloud | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111697 | WATCH / 30 | roinli / HUIZHI-ChargeOS-cloud | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111682 | WATCH / 30 | smartloli / EFAK | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111642 | WATCH / 30 | fastapiadmin / FastapiAdmin | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：2；缺少 Product：2；缺少 Title：28。
- EPSS 未確認：19；Exploitation status 未確認：0。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-17T05:12:16.673028+00:00`；Delta generated at：`2026-10-17T05:12:16.673028+00:00`。

---

## 可驗證資料來源

- **CVE-2026-102764** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102764) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-102764) · [Vendor / Advisory (beyondtrust.com)](https://www.beyondtrust.com/trust-center/security-advisories/bt26-05) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-61624** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-61624) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-61624) · [Vendor / Advisory (fortiguard.fortinet.com)](https://fortiguard.fortinet.com/psirt/FG-IR-26-122) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-105039** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105039) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105039)
- **CVE-2026-105038** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105038) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105038)
- **CVE-2026-105037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105037) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105037)
- **CVE-2026-105032** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105032) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105032)
- **CVE-2026-105040** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105040) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105040)
- **CVE-2026-105036** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105036) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105036)
- **CVE-2026-105035** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105035) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105035)
- **CVE-2026-105034** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105034) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105034)
- **CVE-2026-105033** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105033) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105033)
- **CVE-2026-95182** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95182)
- **CVE-2026-111708** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111708)
- **CVE-2026-111692** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111692)
- **CVE-2026-111687** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111687)
- **CVE-2026-111673** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111673)
- **CVE-2026-111391** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111391)
- **CVE-2026-88755** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88755)
- **CVE-2026-57488** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57488)
- **CVE-2026-57486** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57486)
- **CVE-2026-48503** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48503)
- **CVE-2026-42270** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42270)
- **CVE-2026-30971** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-30971)
- **CVE-2026-111722** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111722)
- **CVE-2026-111718** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111718)
- **CVE-2026-111702** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111702)
- **CVE-2026-111698** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111698)
- **CVE-2026-111697** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111697)
- **CVE-2026-111682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111682)
- **CVE-2026-111642** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111642)
- **CVE-2026-111627** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111627)
- **CVE-2026-111622** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111622)
- **CVE-2026-111612** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111612)
- **CVE-2026-111607** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111607)
- **CVE-2026-96620** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96620)
- **CVE-2026-94388** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94388) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-94388)
- **CVE-2026-94169** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94169) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-94169)
- **CVE-2026-92262** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92262)
- **CVE-2026-89079** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89079) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89079)
- **CVE-2026-85748** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85748)
- **CVE-2026-85746** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85746)
- **CVE-2026-57169** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57169)
- **CVE-2026-49868** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-49868)
- **CVE-2026-44977** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-44977)
- **CVE-2026-18516** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18516)
- **CVE-2026-111823** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111823)
- **CVE-2026-111711** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111711)
- **CVE-2026-111704** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111704)
- **CVE-2026-111693** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111693)
- **CVE-2026-111691** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111691)
- **CVE-2026-111690** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111690)
- **CVE-2026-111675** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111675)
- **CVE-2026-111663** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111663)
- **CVE-2026-111643** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111643)
- **CVE-2026-111641** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111641)
- **CVE-2026-111636** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111636)
- **CVE-2026-111626** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111626)
- **CVE-2026-111472** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111472) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111472)
- **CVE-2026-110653** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110653)
- **CVE-2026-109588** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109588)
- **CVE-2026-109587** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109587)
- **CVE-2026-107617** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107617)
- **CVE-2026-105279** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105279)
- **CVE-2026-104736** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104736)
- **CVE-2026-104730** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104730) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-104730)
- **CVE-2026-103768** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103768) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-103768)
- **CVE-2026-102693** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102693)
- **CVE-2026-102692** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102692)
- **CVE-2026-102608** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102608)
- **CVE-2026-102551** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102551)
- **CVE-2026-68908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-68908)
- **CVE-2026-59966** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59966)
- **CVE-2026-55862** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55862)
- **CVE-2026-55836** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55836)
- **CVE-2026-111717** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111717)
- **CVE-2026-111707** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111707)
- **CVE-2026-111703** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111703)
- **CVE-2026-111688** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111688)
- **CVE-2026-111677** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111677)
- **CVE-2026-111672** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111672)
- **CVE-2026-111667** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111667)
- **CVE-2026-111662** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111662)
- **CVE-2026-111657** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111657)
- **CVE-2026-111652** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111652)
- **CVE-2026-111647** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111647)
- **CVE-2026-111637** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111637)
- **CVE-2026-111632** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111632)
- **CVE-2026-111617** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111617)
- **CVE-2026-111392** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111392)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
