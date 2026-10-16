# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**107** 筆符合目前門檻的重要變化；事件統計：EXPLOITATION_CHANGED=1、NEW_CVE=106、NEW_KEV=1、RANSOMWARE_USE_CHANGED=1。
- Intelligence 候選：**30** 筆；P1 **1**、P2 **0**、P3 **8**、WATCH **21**。
- Baseline：state / generated_at=2026-10-15T05:25:00.357374+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-21589。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **107** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-21589｜Atlassian / Multiple Products
- **Delta event**：NEW_KEV (from=false; to=true)；EXPLOITATION_CHANGED (from=poc; to=known_exploited)；RANSOMWARE_USE_CHANGED (from=未確認; to=Unknown)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)、DELTA_EXPLOIT_ESCALATION(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.02777 / percentile=0.86118
- **CISA KEV**：listed=true / date_added=2026-10-15 / due_date=2026-10-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-05T22:16:58.423 / 2026-10-16T04:18:31.887
- **官方描述（原文）**：Multiple Atlassian products (Bitbucket Data Center ,Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye) contain a files or directories accessible to external parties vulnerability which could allow an unauthenticated attacker to access specific files within the web application root directory in affected versions.

### 2. CVE-2026-57155｜opnsense / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:18:17.300)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:18:17.300 / 2026-10-15T21:08:49.703
- **官方描述（原文）**：OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the Firewall Alias GeoIP importer's process_zip() and process_gzip() paths in src/opnsense/scripts/filter/lib/alias/geoip.py use an unvalidated CSV country_code value to construct output filenames below /usr/local/share/GeoIP/alias. A user with Firewall Alias Edit privilege can configure an attacker-controlled GeoIP source URL and supply an archive whose country code traverses into another existing directory, causing attacker-controlled content to be written as root with an -IPv4 or -IPv6 suffix. A crafted newsyslog fragment and oversized log file can use the default hourly root cron job to execute commands as root, resulting in complete firewall compromise. This issue is fixed in version 26.1.11.

### 3. CVE-2026-19863｜Eclipse Foundation / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T10:17:12.497)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.0054 / percentile=0.44178
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T10:17:12.497 / 2026-10-15T14:41:34.110
- **官方描述（原文）**：An unauthenticated client may access certain protected resources when using EthereumAuthenticator if the request path contains the configured login path. This is caused by the authenticator using an unanchored substring match when identifying the login page. If the login path appears later within a protected request path, the request may be treated as the login page and its authentication or role requirement replaced with ALLOWED. Exploitation requires the protected resource path to contain the configured login path as a later segment. Explicitly FORBIDDEN routes are not affected.

### 4. CVE-2026-110958｜Wavlink / WN530HG4B
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:17:48.467)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:17:48.467 / 2026-10-15T19:56:13.350
- **官方描述（原文）**：A vulnerability was found in Wavlink WN530HG4B M30HG4B_V260724. The impacted element is an unknown function of the file api.cgi. The manipulation results in heap-based buffer overflow. It is possible to launch the attack remotely. The exploit has been made public and could be used. Upgrading to version 2026-09-24-841a51c6d5_tclinux.bin is sufficient to resolve this issue. The affected component should be upgraded. The vendor confirms: "We confirm the finding, and it has already been addressed. In the current firmware the api=info&client=app handler no longer builds a shell command: the login script is now invoked through an argument vector (execvp) instead of system(), and the client address is length-limited and null-checked."

### 5. CVE-2026-105039｜EnergizeLab / station-middleware
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T21:17:04.587)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.587 / 2026-10-15T21:17:04.587
- **官方描述（原文）**：EnergizeLab station-middleware (NestJS) Docker images 1.6.5 through 1.8.2 do not check user roles on administrative APIs. Any authenticated low-privilege user can retrieve AI provider keys and change configuration and object-store contents.

### 6. CVE-2026-105038｜EnergizeLab / FastAPI AI inference server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T21:17:04.467)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.467 / 2026-10-15T21:17:04.467
- **官方描述（原文）**：The EnergizeLab Eilik and EilikO FastAPI AI inference and profiling services expose AI model administration functions without authentication. An unauthenticated remote attacker can change AI model configuration and switch the model in use at runtime.

### 7. CVE-2026-105037｜EnergizeLab / station-middleware
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T21:17:04.350)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.350 / 2026-10-15T21:17:04.350
- **官方描述（原文）**：EnergizeLab station-middleware (NestJS) Docker images 1.6.5 through 1.8.2 allow any registered, low-privilege account to read arbitrary files from the server by supplying an attacker-controlled file path. This exposes middleware files and server secrets.

### 8. CVE-2026-105032｜EnergizeLab / FastAPI AI inference server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T21:17:03.753)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:03.753 / 2026-10-15T21:17:03.753
- **官方描述（原文）**：The EnergizeLab Eilik and EilikO AI skill upload endpoint, served by the FastAPI AI inference and profiling services, does not require authentication and does not constrain uploaded file paths. An unauthenticated remote attacker can use path traversal to write arbitrary files, and thereby tamper with AI skill files used by Eilik and EilikO robots.

### 9. CVE-2026-102946｜authlib / joserfc
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:13.423)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:13.423 / 2026-10-15T20:17:05.407
- **官方描述（原文）**：joserfc is a Python library that provides an implementation of several JSON Object Signing and Encryption (JOSE) standards. Prior to 1.7.4, joserfc.jws.deserialize_json() accepts a JWS General JSON Serialization with an empty signatures array as authenticated. The verify_general_json() loop performs no iterations for the empty array and returns success because no signature check failed, allowing an attacker without a signing key to supply an arbitrary payload that relying applications may treat as authentic. The issue affects the General JSON Serialization path; compact JWS and JWT decoding, Flattened JSON serialization, and JWE JSON processing do not follow this vulnerable path. This issue is fixed in version 1.7.4.

### 10. CVE-2026-77711｜Eclipse Foundation / Eclipse Jetty
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T09:17:18.573)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：0.0032 / percentile=0.23324
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T09:17:18.573 / 2026-10-15T14:41:34.110
- **官方描述（原文）**：When Jetty's `HttpClient` make a request to a server through a forward proxy, the server may reply with a 407 (Proxy Authentication Required). The client mistakenly interprets the 407 as coming from the proxy, so it re-sends the request with the `Proxy-Authentication` header, which arrives to the server, that now has access to the proxy credentials.

### 11. CVE-2026-77470｜LycheeOrg / Lychee
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T17:17:27.997)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T17:17:27.997 / 2026-10-15T21:08:49.703
- **官方描述（原文）**：Lychee is a free, open-source photo-management tool. Prior to 7.7.1, the Supporter or Pro webshop POST /api/v2/Shop/Checkout/Process flow accepts an unrestricted additional_data array and CheckoutService::preparePurchaseParameters() merges it after server-computed purchase parameters. Because later string keys overwrite earlier keys, an unauthenticated buyer can replace amount, currency, returnUrl, cancelUrl, or transactionId before CheckoutService::processPayment() passes the parameters to a non-PayPal Omnipay gateway. An attacker can therefore make a gateway accept a successful payment for an attacker-selected amount and obtain auto-fulfilled goods while underpaying the merchant. The issue requires an enabled webshop, a purchasable item, and an affected Omnipay gateway. This issue is fixed in version 7.7.1.

### 12. CVE-2026-77466｜LycheeOrg / Lychee
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T17:17:27.580)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T17:17:27.580 / 2026-10-15T21:08:49.703
- **官方描述（原文）**：Lychee is a free, open-source photo-management tool. Prior to 7.7.0, Lychee hides the Omnipay Dummy test provider from the checkout options in production through OmnipayFactory::get_supported_providers(), but CreateSessionRequest validates only that the submitted provider is an OmnipayProviderType and does not enforce OmnipayProviderType::isAllowed(). A buyer, including a guest when webshop_allow_guest_checkout is enabled, can submit Dummy directly and complete the test gateway flow without a real payment. When webshop_auto_fulfill_enabled is enabled, OrderCompletedListener::fullfillOrder() can then release the purchasable item. The issue requires access to the Supporter or Pro webshop and an enabled purchasable item. Testing bypassed the closed-source license middleware, so whether the real license layer performs additional payment-provider validation remains unverified. The payment finalize status check itself is not the root cause. This issue is fixed in version 7.7.0.

### 13. CVE-2026-76184｜Eclipse Foundation / Eclipse Jetty
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T09:17:18.443)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：0.00278 / percentile=0.18899
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T09:17:18.443 / 2026-10-15T14:41:34.110
- **官方描述（原文）**：In Eclipse Jetty, HttpClient may receive a redirect of the form: ``` /secure/../evil ``` If an attacker is able to control the redirects, then HttpClient matches authentication credentials against `/secure` rather than normalizing the path to `/evil`, and will therefore follow the redirect sending the `Authorization` header for `/secure` to `/evil`. This also mean that the attacker must have an evil application deployed on the same domain as the target.

### 14. CVE-2026-71490｜opnsense / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:18:19.723)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:18:19.723 / 2026-10-15T21:08:49.703
- **官方描述（原文）**：OPNsense is a FreeBSD based firewall and routing platform. Prior to 26.1.11, OPNsense\Core\ACL::hasPrivilege() appends a directly assigned comma-separated <priv> value as one string and then uses an exact comparison when checking user-config-readonly. A user directly assigned both a component write privilege and user-config-readonly can therefore be treated as lacking the read-only restriction, and MVC APIs protected by throwReadOnly() can persist configuration changes for that component. Group privileges are not affected by the same parser flaw because the group path already splits comma-separated values. This issue is fixed in version 26.1.11.

### 15. CVE-2026-61838｜LycheeOrg / Lychee
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T17:17:26.677)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T17:17:26.677 / 2026-10-15T21:08:49.703
- **官方描述（原文）**：Lychee is a free, open-source photo-management tool. Prior to 7.6.3, GET /api/v2/Zip authorizes album and photo archives through AlbumPolicy::canDownload() and PhotoPolicy::canDownload() without first enforcing AlbumPolicy::canAccess(). For a public, password-protected album with grants_download enabled, an unauthenticated attacker who knows the shared album identifier can download a ZIP archive without supplying the password or unlocking the album, even though browsing endpoints deny access. The archive exposes the album's photos and can include full-resolution originals and associated metadata when grants_full_photo_access is enabled. This issue is fixed in version 7.6.3.

### 16. CVE-2026-55246｜Tatsh / bincookie
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T18:17:27.317)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T18:17:27.317 / 2026-10-15T19:17:40.430
- **官方描述（原文）**：bincookie is a header-only binarycookies parser. Prior to 0.1.9, bincookie_init_file() in bincookie.h allocates a buffer using the actual .binarycookies file length but trusts the file-controlled num_pages field as the loop bound for byte-swapping page_sizes entries. A crafted file can make the loop read and write beyond the heap allocation, and related unvalidated page sizes and cookie_offsets can drive additional out-of-bounds accesses in page and cookie iteration. Applications that parse an attacker-supplied binarycookies file may crash or suffer heap corruption that can potentially enable code execution. This issue is fixed in version 0.1.9.

### 17. CVE-2026-18661｜Eclipse Foundation / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T09:17:17.270)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：0.00335 / percentile=0.25293
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T09:17:17.270 / 2026-10-15T14:41:34.110
- **官方描述（原文）**：In Eclipse Jetty, across various versions of `jetty-annotations`, and `jetty-eeN-annotations`, the Jakarta Spec authoritative url-pattern rules for mixed `@ServletSecurity` annotation, and `web.xml` defined `security-constraint` on the same `url-pattern` were not being applied if the `web.xml` had more than 1 `url-pattern` for a servlet, and had a `security-constraint` applying to only some of those `url-pattern` definitions.

### 18. CVE-2026-18660｜Eclipse Foundation / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T10:17:12.097)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：0.00421 / percentile=0.34936
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T10:17:12.097 / 2026-10-15T14:41:34.110
- **官方描述（原文）**：In Eclipse Jetty, across various versions of `jetty-server`, and `jetty-proxy`, the host whitelist/blacklist is case-sensitive, and would allow hosts through that only differ by case.

### 19. CVE-2026-111220｜Netgate / pfSense CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:34.500)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:34.500 / 2026-10-15T21:05:32.823
- **官方描述（原文）**：pfSense CE through 2.9.0 contains a crontab injection vulnerability in interfaces_ppps_edit.php that allows authenticated users to execute commands as root by injecting newlines into the ptpid or reset hour/minute fields. Attackers holding the 'WebCfg - Interfaces: PPPs: Edit' privilege can submit crafted POST values that configure_cron() writes unescaped into /etc/crontab, running arbitrary root commands on schedule.

### 20. CVE-2026-111218｜Netgate / pfSense CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:34.210)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:34.210 / 2026-10-15T21:05:32.823
- **官方描述（原文）**：Netgate pfSense CE 2.7.0 through 2.9.0 contains an OS command injection vulnerability that allows authenticated users with Traffic Shaper Limiters privileges to execute root commands by tampering with the limiter number field. Attackers can submit a malicious hidden 'number' value when editing a limiter, then delete it so delete_queue() passes the unquoted value to dnctl via /bin/sh as root.

### 21. CVE-2026-111215｜Netgate / pfSense CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:33.757)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:33.757 / 2026-10-15T21:05:32.823
- **官方描述（原文）**：Netgate pfSense CE through 2.9.0 contains an OS command injection vulnerability that allows authenticated users to execute commands as root by supplying a crafted wireless parent interface name. Attackers with limited Wireless Edit or Interface Assignments privileges can submit values like ath0;<cmd> via interfaces_wireless_edit.php or interfaces_assign.php, which interface_wireless_clone() interpolates unescaped into an ifconfig shell command.

### 22. CVE-2026-110746｜TotalSecurity / TotalAV
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T15:17:28.487)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T15:17:28.487 / 2026-10-15T16:17:46.450
- **官方描述（原文）**：A local privilege escalation vulnerability in TotalAV allows an unprivileged local user to forge the gRPC IPC authentication token, through loading IPC.dll and abuse the SYSTEM service's within TotalAV to execute arbitrary code as NT AUTHORITY\SYSTEM.

### 23. CVE-2026-105040｜EnergizeLab / NestJS auth service
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T21:17:04.703)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.703 / 2026-10-15T21:17:04.703
- **官方描述（原文）**：The EnergizeLab Eilik NestJS auth service accepts a user-controlled user ID in account update requests (mass assignment). A registered user can set another account's identifier and take over that account.

### 24. CVE-2026-105036｜EnergizeLab / Robot firmware (mode 104000)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T21:17:04.230)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.230 / 2026-10-15T21:17:04.230
- **官方描述（原文）**：EnergizeLab AI Station firmware, EilikO Linux robot firmware v2.1_20260617182218_release, and the EnergizeLab Windows desktop app 3.1.2 download firmware updates over plain HTTP and do not verify their integrity or authenticity. An attacker able to intercept or modify the traffic can substitute a malicious update.

### 25. CVE-2026-105035｜EnergizeLab / FirmwareUpdater
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T21:17:04.113)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:04.113 / 2026-10-15T21:17:04.113
- **官方描述（原文）**：The EnergizeLab FirmwareUpdater (AArch64 ELF, distributed in the CDN bin.zip) uses a single hard-coded AES key shared by all installations. An attacker who recovers the key from the updater can decrypt and forge firmware packages for any device that trusts it.

### 26. CVE-2026-105034｜EnergizeLab / NestJS auth service
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T21:17:03.997)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:03.997 / 2026-10-15T21:17:03.997
- **官方描述（原文）**：The EnergizeLab Eilik NestJS auth service issues device tokens for arbitrary robot serial numbers without authentication. An unauthenticated remote attacker can obtain a valid device token for any serial number and act as that device against the cloud services.

### 27. CVE-2026-105033｜EnergizeLab / AI Station firmware (RK3562)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T21:17:03.883)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:03.883 / 2026-10-15T21:17:03.883
- **官方描述（原文）**：The EnergizeLab AI Station (RK3562) firmware image ships with default root credentials and SSH enabled. An attacker with network access to the device can log in as root and take full control of it.

### 28. CVE-2026-100354｜getkin / kin-openapi
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T17:17:07.780)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T17:17:07.780 / 2026-10-15T19:17:12.943
- **官方描述（原文）**：kin-openapi is a Go project for handling OpenAPI files. Prior to 0.149.0, runtime request, response, and direct schema validation lacks cycle detection when an allOf, anyOf, or oneOf chain refers back to an ancestor schema, even though loading and document validation accept the circular reference. A request or response that reaches the affected schema causes unbounded recursion in Schema.visitJSON or openapi3filter.decodeValue and exhausts the Go goroutine stack. The resulting fatal stack overflow cannot be caught with recover and terminates the entire process, including unrelated requests. This issue is fixed in version 0.149.0.

### 29. CVE-2026-100351｜getkin / kin-openapi
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:17:31.110)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:17:31.110 / 2026-10-15T17:17:07.520
- **官方描述（原文）**：kin-openapi is a Go project for handling OpenAPI files. From 0.144.0 until 0.147.0, openapi3filter.ValidationHandler validates an operation selected from decoded URL.Path while a downstream gorilla/mux router configured with UseEncodedPath can dispatch a different operation selected from URL.RawPath. When a public exact route and a protected parameterized route use the same method and overlap after decoding, an unauthenticated remote request containing an encoded path separator can be validated as public and then dispatched to the protected handler without invoking the configured AuthenticationFunc. The reachable path parameter is constrained to an encoded representation that decodes to the public literal route, and proxies that canonicalize the URI before forwarding prevent this specific mismatch. This issue is fixed in version 0.147.0.

### 30. CVE-2026-99999｜Linux / Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T13:17:14.137)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T13:17:14.137 / 2026-10-15T23:19:38.590
- **官方描述（原文）**：In the Linux kernel, the following vulnerability has been resolved: ipv4: validate checksum_start before completing checksum If a packet with bad checksum metadata gets into the ipv4 stack, skb_checksum_help can corrupt the network header and cause a bunch of mischief. This was discovered and reported by Paulos, and has been reporoduced by others independently since. We really shouldn't allow such packets in, but as a defence in depth measure, let's also check before we complete the checksum. A more complete validation at input is forthcoming, but needs more work.

### 31. CVE-2026-84731｜Nutanix / Acropolis Operating System (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T18:17:29.960)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T18:17:29.960 / 2026-10-15T20:17:15.097
- **官方描述（原文）**：An unauthenticated remote attacker can bypass authentication and gain full access to administrative API endpoints in Nutanix Prism Element by including a crafted internal management HTTP header. The vulnerability is caused by a misconfiguration in the application's authentication filters. Consequently, the server responds with a Set-Cookie header containing a valid JSESSIONID. This session cookie decodes to a JSON Web Token (JWT) granting maximum cluster administrative privileges. Successful exploitation allows the attacker to execute root-level commands on all Controller VMs (CVMs) in the cluster, leading to complete cluster destruction and unauthorized access to VM memory and virtual disks.

### 32. CVE-2026-57496｜Labs64 / NetLicensing-MCP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:41.733)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:41.733 / 2026-10-15T19:17:41.733
- **官方描述（原文）**：NetLicensing MCP Server is a natural-language interface that enables agentic applications to manage the software-licensing lifecycle in Labs64 NetLicensing. Prior to 0.1.8, netlicensing_get_product passes the caller-controlled product_number to src/netlicensing_mcp/tools/products.py, which interpolates it into a REST path consumed by nl_get() in src/netlicensing_mcp/client.py without path-segment validation. A traversal segment can be normalized from the intended product path to the /token endpoint, after which the response is serialized through _wrap_json instead of _wrap_json_token_read, bypassing redact_token_read() protections for APIKEY number and SHOP shopURL fields. An authenticated MCP client with a non-administrative API key can retrieve plaintext token values, and a recovered administrative token can provide broad read, write, and delete access to the NetLicensing account. This issue is fixed in version 0.1.8.

### 33. CVE-2026-55240｜msgbyte / tianji
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:40.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:40.290 / 2026-10-15T19:17:40.290
- **官方描述（原文）**：Tianji is an open source analytics, uptime monitoring, and server status platform. Prior to 1.31.29, formatString() in src/server/utils/template.ts passes survey feedTemplate and monitor notification templates to lodash template(), while the default evaluate pattern remains enabled. A workspace administrator can store an evaluate block using the <% code %> form, and the public survey.submit endpoint renders a survey template when an unauthenticated user submits a response. The compiled template executes server-side JavaScript in the Tianji Node.js process, allowing command execution, secret disclosure, data modification, or service disruption. This issue is fixed in version 1.31.29.

### 34. CVE-2026-50619｜QNAP Systems Inc. / Qsirch
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T10:17:15.220)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00614 / percentile=0.48287
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T10:17:15.220 / 2026-10-15T16:32:39.893
- **官方描述（原文）**：A path traversal vulnerability has been reported to affect Qsirch. If exploited, the vulnerability could allow remote attackers to read the contents of unexpected files or system data. We have already fixed the vulnerability in the following version: Qsirch 7.0.3.0 and later

### 35. CVE-2026-50612｜QNAP Systems Inc. / QuMagie
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T10:17:15.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00488 / percentile=0.40518
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T10:17:15.090 / 2026-10-15T16:32:39.893
- **官方描述（原文）**：An unix symbolic link (symlink) following vulnerability has been reported to affect QuMagie. If a remote attacker gains a user account, they can then exploit the vulnerability to compromise the security of the system. We have already fixed the vulnerability in the following version: QuMagie 2.9.2 and later

### 36. CVE-2026-47786｜QNAP Systems Inc. / HybridDesk Station
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T10:17:14.720)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.01413 / percentile=0.72214
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T10:17:14.720 / 2026-10-15T16:32:39.893
- **官方描述（原文）**：An OS command injection vulnerability has been reported to affect HybridDesk Station. If exploited, the vulnerability could allow remote attackers to execute arbitrary commands. We have already fixed the vulnerability in the following version: HybridDesk Station 4.2.23 and later HybridDesk Station 4.3.4 and later

### 37. CVE-2026-47218｜containerd / runwasi
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:39.257)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:39.257 / 2026-10-15T20:17:13.510
- **官方描述（原文）**：runwasi facilitates running Wasm and WASI workloads managed by containerd. Prior to 0.6.1, containerd-shim-wasmtime-v1 can treat Wasmtime precompiled bytes supplied directly in an OCI image layer as a trusted artifact from the precompile-cache path and deserialize them as native code. An attacker who causes a victim to run a crafted image can bypass WebAssembly validation and execute native code in the shim zygote process, gaining the filesystem, environment, credentials, networking, and Linux syscall access available to the workload container. Downstream shims built with runwasi's containerd-shim-wasm precompile-cache API are also affected if they implement Compiler and trust executable precompiled artifacts from OCI image layers; the 0.6.1 boundary applies specifically to containerd-shim-wasmtime and does not independently certify downstream product releases. The flaw escapes the WASI sandbox to the workload container boundary, but it does not by itself bypass container isolation or provide direct host code execution. This issue is fixed in version 0.6.1.

### 38. CVE-2026-47168｜espocrm / espocrm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T15:17:34.917)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T15:17:34.917 / 2026-10-15T15:17:35.037
- **官方描述（原文）**：EspoCRM is an open source customer relationship management application. Prior to 9.3.7, an authenticated administrator can supply crafted serialized PHP object data that is stored in background MassAction or Export parameters and later deserialized by the application. The deserialization paths do not restrict allowed classes, allowing attacker-controlled object instantiation and arbitrary code execution on the server. This issue is fixed in version 9.3.7.

### 39. CVE-2026-34006｜QNAP Systems Inc. / sMedio DTCP MOVE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T10:17:13.187)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00534 / percentile=0.43786
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T10:17:13.187 / 2026-10-15T16:32:39.893
- **官方描述（原文）**：A missing authentication for critical function vulnerability has been reported to affect sMedio DTCP MOVE. If exploited, the vulnerability could allow remote attackers to gain access to the system. We have already fixed the vulnerability in the following version: sMedio DTCP MOVE 1.4.5 and later

### 40. CVE-2026-16438｜Mitsubishi Electric Corporation / GENESIS64
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T09:17:17.087)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00238 / percentile=0.13797
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T09:17:17.087 / 2026-10-15T20:38:04.303
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in Mitsubishi Electric GENESIS64 versions 10.97.3 and prior, ICONICS Suite versions 10.97.3 and prior, Hyper Historian versions 10.97.3 and prior, AnalytiX versions 10.97.3 and prior, MobileHMI 10.97.3 and prior, MC Works64 all versions, Mitsubishi Electric Iconics Digital Solutions GENESIS64 versions 10.97.3 and prior, ICONICS Suite versions 10.97.3 and prior, Hyper Historian versions 10.97.3 and prior, AnalytiX versions 10.97.3 and prior, and MobileHMI 10.97.3 and prior allows an attacker who can log in using the same administrator account for the affected products to launch and operate DCOM objects locally or remotely. During installation, the installers of the affected products unnecessarily grant default DCOM permissions to the administrator account of the affected products. Users with that administrator accounts can locally or remotely launch and operate DCOM objects that should require UAC elevation. As a result, the attacker may disclose, tamper with, destroy, or delete internal information, or cause the affected system to enter a denial-of-service (DoS) condition.

### 41. CVE-2026-16436｜Mitsubishi Electric Corporation / GENESIS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T09:17:16.717)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00303 / percentile=0.21505
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T09:17:16.717 / 2026-10-15T20:38:04.303
- **官方描述（原文）**：Weak Password Recovery Mechanism for Forgotten Password vulnerability in Mitsubishi Electric GENESIS versions 11.03 and prior, GENESIS64 versions 10.97.3 and prior, ICONICS Suite versions 10.97.3 and prior, Hyper Historian versions 10.97.3 and prior, AnalytiX versions 10.97.3 and prior, MobileHMI 10.97.3 and prior, IoTWorX 10.97.3 and prior, MC Works64 all versions, GENESIS32 all versions, BizViz all versions, Mitsubishi Electric Iconics Digital Solutions GENESIS versions 11.03 and prior, GENESIS64 versions 10.97.3 and prior, ICONICS Suite versions 10.97.3 and prior, Hyper Historian versions 10.97.3 and prior, AnalytiX versions 10.97.3 and prior, MobileHMI 10.97.3 and prior, IoTWorX 10.97.3 and prior, GENESIS32 all versions, and BizViz all versions allows a remote attacker to unlock the system by obtaining the challenge response by some means. The challenge response used to unlock the system is common to all users and fixed. As a result, the attacker may disclose, tamper with, destroy, or delete internal information, or cause the affected system to enter a denial-of-service (DoS) condition.

### 42. CVE-2026-111444｜Wheels / Wheels
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T04:18:30.353)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T04:18:30.353 / 2026-10-16T04:18:30.353
- **官方描述（原文）**：Wheels through 4.1.2 allows SQL injection on MySQL/MariaDB with backslash escaping enabled (NO_BACKSLASH_ESCAPES absent) when an application supplies request data to inline-literal paths. These include opt-in parameterize=false queries and IN lists, and positions in developer-written where strings that the parser does not bind, such as BETWEEN bounds, function arguments and LIKE ESCAPE literals. Doubling single quotes without accounting for backslash escapes allows a value to alter the query. Bound paths are not affected; whereBetween() is bound from 4.1.2. This is fixed in 4.2.0.

### 43. CVE-2026-111356｜magicblack / MacCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T22:19:33.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T22:19:33.647 / 2026-10-15T22:19:33.647
- **官方描述（原文）**：MacCMS v10 through 2026.1000.4056 does not limit attempts on the six-digit password recovery code, allowing unauthenticated attackers to take over member accounts. Attackers knowing a victim's email or phone can request a code and brute-force findpass_reset to overwrite the member's password.

### 44. CVE-2026-111329｜juggleim / JuggleIM
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T22:19:31.063)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T22:19:31.063 / 2026-10-15T22:19:31.063
- **官方描述（原文）**：JuggleIM im-server through 1.8.16 ships default administrator credentials admin/123456 that allow unauthenticated remote attackers to access the admin console on port 8090. Attackers can log in as administrator, even after account deletion since CheckLogin recreates it, to control tenant applications and app secrets.

### 45. CVE-2026-111322｜coleam00 / Archon
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T22:19:30.633)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T22:19:30.633 / 2026-10-15T22:19:30.633
- **官方描述（原文）**：Archon 0.2.13 through 0.11.1 contains a missing authentication vulnerability that allows unauthenticated attackers to access the /api/* control API, which binds to 0.0.0.0 by default. Attackers with network access can send messages to the AI coding agent, which runs with bypassPermissions, to execute commands on the host as the Archon user.

### 46. CVE-2026-111312｜OpenHealthForAll / OpenHealth
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T22:19:30.053)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T22:19:30.053 / 2026-10-15T22:19:30.053
- **官方描述（原文）**：OpenHealth through 0.2.0 contains a missing authentication and authorization vulnerability in the /api/health-data/[id] GET, PATCH and DELETE handlers that query records by id without session or authorId checks. Unauthenticated attackers who know a HealthData record id can read another user's medical record data and file metadata, overwrite it with arbitrary JSON, or delete it.

### 47. CVE-2026-111283｜BMC Helix / BMC Helix Network Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T22:19:29.747)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T22:19:29.747 / 2026-10-15T22:19:29.747
- **官方描述（原文）**：BMC Helix Network Management on-prem before 26.3.01 contains an authentication bypass vulnerability that allows unauthenticated attackers to log in as the local administrator with any password when SAML single sign-on is configured. Attackers can submit the administrator username with an arbitrary password on the web login page to obtain a SuperAdmin session, modify device credentials, run device commands, and alter audit records.

### 48. CVE-2026-111281｜Jooan / JA-A12
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T22:19:29.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T22:19:29.457 / 2026-10-15T22:19:29.457
- **官方描述（原文）**：Jooan JA-A12 IP cameras with firmware 009_20171107 and 05.02.31.105 contain a remote code execution vulnerability that allows unauthenticated attackers to run root commands via hard-coded credentials. Attackers send singleCMD=SetDiagMode to /goform/SingleHandlebyCommand with an attacker-chosen authserverip and authcode, making the jooandiag daemon execute their commands through /bin/sh, giving full device control.

### 49. CVE-2026-111235｜The OpenNMS Group / Meridian
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:36.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:36.693 / 2026-10-15T19:17:36.693
- **官方描述（原文）**：An authorization bypass vulnerability exists in the REST API of multiple versions of OpenNMS Meridian and Horizon. The /rest/** Spring Security filter chains authorize requests with intercept-url rules that name the HTTP method as an uppercase token, compare the method case-sensitively, and have no terminal deny rule. A request that uses a non-canonical (for example lowercase) method token matches no rule and is processed without authentication. A remote, unauthenticated attacker can read the monitored inventory and can create, modify, or delete resources through the REST API, which includes injecting events to fabricate or suppress alarms. The /rest/alarms chain has the same missing deny rule and discloses whether an alarm exists through a difference in the response. The fix adds a terminal deny rule to each REST filter chain. The solution is to upgrade to Meridian 2024.3.14, 2025.0.11, 2026.0.1 and Horizon 36.0.5 or newer. Meridian and Horizon installation instructions state that they are intended for installation within an organization's private networks and should not be directly accessible from the Internet.

### 50. CVE-2026-110957｜Wavlink / WL-WN530BE2-A
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T15:17:30.640)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T15:17:30.640 / 2026-10-15T19:56:13.350
- **官方描述（原文）**：A vulnerability has been found in Wavlink WL-WN530BE2-A up to M30BE2_V250604. The affected element is the function sub_12580 of the file api.cgi of the component Login Processing. The manipulation of the argument REMOTE_ADDR leads to os command injection. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. Upgrading to version 2026-09-24-841a51c6d5_tclinux.bin is sufficient to fix this issue. You should upgrade the affected component. The vendor confirms: "We confirm the finding, and it has already been addressed. In the current firmware the api=info&client=app handler no longer builds a shell command: the login script is now invoked through an argument vector (execvp) instead of system(), and the client address is length-limited and null-checked."

### 51. CVE-2026-110812｜AWS / Amazon Neptune Engine
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T17:17:16.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T17:17:16.110 / 2026-10-15T19:17:23.697
- **官方描述（原文）**：Deserialization of untrusted data in the Gremlin graph data import component in Amazon Neptune engine might allow an authenticated remote actor with standard database permissions to execute arbitrary code and access internal service credentials. To remediate this issue, users not enrolled in auto-update should upgrade to Amazon Neptune engine version 1.5.0.0.(Backports to 1.4.8.1 and 1.4.7.1)

### 52. CVE-2026-109892｜Shabti Kaplan / Frontend Admin by DynamiApps
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T13:17:12.697)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T13:17:12.697 / 2026-10-15T14:45:38.353
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in Shabti Kaplan Frontend Admin by DynamiApps acf-frontend-form-element allows Privilege Escalation.This issue affects Frontend Admin by DynamiApps: from n/a through 3.29.13.

### 53. CVE-2026-109698｜Kitae Park / Mang Board WP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T13:17:12.317)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T13:17:12.317 / 2026-10-15T14:45:38.353
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Kitae Park Mang Board WP mangboard allows SQL Injection.This issue affects Mang Board WP: from n/a through 2.4.4.

### 54. CVE-2026-109694｜WP ManageNinja LLC / Fluent CRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T11:17:24.537)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T11:17:24.537 / 2026-10-15T15:17:27.977
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in WP ManageNinja LLC Fluent CRM fluent-crm allows Privilege Escalation.This issue affects Fluent CRM: from n/a through 3.2.5.

### 55. CVE-2026-109688｜Link Whisper INC / Link Whisper Free
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T13:17:11.917)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T13:17:11.917 / 2026-10-15T15:17:27.873
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Link Whisper INC Link Whisper Free link-whisper allows Blind SQL Injection.This issue affects Link Whisper Free: from n/a through 0.9.7.

### 56. CVE-2026-109686｜Link Whisper INC / Link Whisper Free
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T13:17:11.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T13:17:11.540 / 2026-10-15T16:17:44.390
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Link Whisper INC Link Whisper Free link-whisper allows Object Injection.This issue affects Link Whisper Free: from n/a through 0.9.7.

### 57. CVE-2026-109515｜properfraction / MailOptin – Popup, Optin Forms & Email Newsletters for Mailchimp, HubSpot, AWeber Etc.
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T05:17:29.597)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T05:17:29.597 / 2026-10-16T05:17:29.597
- **官方描述（原文）**：The MailOptin – Popup, Optin Forms & Email Newsletters for Mailchimp, HubSpot, AWeber Etc. plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 1.2.78.6 This is due to the `subscribe_to_email_list` endpoint accepting an attacker-supplied `optin_data[form_custom_field_mappings]` parameter without any allow-list validation on destination keys, allowing the attacker-controlled mapping to override the administrator's saved mapping and pass arbitrary `wp_users` column names — including `ID` and `user_pass` — directly into `wp_insert_user()` via the `subscribe()` function. This makes it possible for unauthenticated attackers to force `wp_insert_user()` into UPDATE mode on any existing account by supplying a target user's numeric `ID`, overwrite that account's password with a pre-hashed value of their choosing, and thereby take over any WordPress user account — including administrators — leading to full site compromise. Exploitation requires that a WordPress User Registration opt-in form is published somewhere on the site, though the form's UUID is visible in page source and no authentication, nonce, or capability check is required to reach the vulnerable endpoint.

### 58. CVE-2026-109219｜kitae-park / Mang Board
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T05:17:29.100)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T05:17:29.100 / 2026-10-16T05:17:29.100
- **官方描述（原文）**：The Mang Board plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 2.4.4 via the mbw_file_upload function. This is due to missing file extension validation on the attacker-supplied image_path parameter, whose basename-derived file name bypasses the extension allowlist applied only to the separate file_name parameter. This makes it possible for unauthenticated attackers to upload files that may be executable, which makes remote code execution possible. Exploitation requires the board to be configured to allow guest posts, which is the plugin's default mode; the required nonce is printed on every public board page, making it readable by any unauthenticated visitor without a WordPress login.

### 59. CVE-2026-109145｜Unknown / User Rights Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T07:17:58.617)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00136 / percentile=0.02706
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T07:17:58.617 / 2026-10-15T14:47:05.720
- **官方描述（原文）**：The User Rights Access Manager WordPress plugin through 1.1.3 does not restrict access to one of its AJAX account-registration handlers and assigns newly registered accounts a role that was created as a copy of the administrator role, allowing unauthenticated attackers to register an administrator-equivalent account and take over the site.

### 60. CVE-2026-108497｜TMS / Amelia
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T11:17:19.823)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T11:17:19.823 / 2026-10-15T14:45:38.353
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in TMS Amelia ameliabooking allows SQL Injection.This issue affects Amelia: from n/a through 2.4.10.

### 61. CVE-2026-105474｜WebPros / SolusVM 2
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:17:34.373)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:17:34.373 / 2026-10-15T17:17:12.287
- **官方描述（原文）**：A server-side template injection exists in SolusVM 2 up to version 2.0.0-44576 that allows remote authenticated users to execute arbitrary code as root.

### 62. CVE-2026-104798｜joedolson / My Calendar – Accessible Event Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-16T05:17:28.580)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-16T05:17:28.580 / 2026-10-16T05:17:28.580
- **官方描述（原文）**：The My Calendar – Accessible Event Manager plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 3.8.7. The public `mcs` GET parameter is reflected into post content unsanitized before WordPress core's `do_shortcode` filter runs, allowing an unauthenticated attacker to inject a nested `[my_calendar above=...]` shortcode; `mc_generate_calendar_nav()` then splits the `above` attribute on commas and dispatches each element via `call_user_func()` with no authentication, authorization, or callable allowlist check. This makes it possible for unauthenticated attackers to invoke arbitrary loaded PHP functions, enabling a call chain in which the shortcode `$params` array is passed to `edit_user()` — which PHP coerces to integer `1` as the `$user_id` argument — overwriting the credentials of the initial Administrator account (user ID 1) and granting the attacker full wp-admin access. Exploitation is trivially reachable via the plugin's auto-generated `/my-calendar/` page, which is publicly accessible by default upon plugin activation.

### 63. CVE-2026-102764｜BeyondTrust / Remote Support
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T21:17:00.117)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T21:17:00.117 / 2026-10-15T21:17:00.117
- **官方描述（原文）**：The vulnerability exists within internal components of BeyondTrust’s Remote Support product. The components did not adequately validate the origin of the messages it received. Under the right conditions, this could allow an attacker to perform file operations on the appliance.

### 64. CVE-2026-102469｜Eclipse Foundation / Eclipse Vert.x
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T09:17:15.573)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00413 / percentile=0.34029
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T09:17:15.573 / 2026-10-15T15:17:19.537
- **官方描述（原文）**：In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the Vert.x DB2 client (vertx-db2-client) contains DRDA protocol handling code that deserializes User Defined Type (UDT) column data using a bare ObjectInputStream.readObject() call with no ObjectInputFilter or class allowlist. This code path is triggered when a DRDA server sends a result set with a column tagged as UDT (FDOCA protocol LID 0x50). However, DB2 does not support this type of UDT. The FDOCA 0x50 type is never sent by a legitimate DB2 server. Nevertheless, a malicious or man-in-the-middle DRDA server could craft a response with a 0x50-tagged column, causing the client to deserialize arbitrary attacker-controlled bytes on the Vert.x event loop before any application code can inspect or reject the data. If a Java deserialization gadget chain is present on the application's classpath, this enables remote code execution. Without a gadget chain, denial of service is possible via crafted object graphs. TLS is disabled by default, making man-in-the-middle exploitation feasible. The impacted component is io.vertx:vertx-db2-client.

### 65. CVE-2026-101287｜Diaple / Stela
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T09:17:14.367)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00398 / percentile=0.32347
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T09:17:14.367 / 2026-10-15T16:33:47.027
- **官方描述（原文）**：Authentication bypass vulnerability in Stela, versions prior to 1.60.1, due to the use of a cookie named “authProcess” without validating its integrity. The application stores the user identifier (userId) and the status of the authentication process (validSteps) in this cookie and relies on these values—which can be modified by the client—to complete the login process. A remote attacker, without valid credentials or interaction from other users, could manipulate the cookie to bypass authentication checks and impersonate any account, including one with SUPER_ADMIN privileges. This would allow the attacker to obtain a valid JWT token with administrative privileges and compromise the confidentiality and integrity of the application.

### 66. CVE-2026-78851｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T17:17:28.640)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T17:17:28.640 / 2026-10-15T19:17:43.850
- **官方描述（原文）**：Directory Traversal vulnerability in Grav CMS 2.0.3 through 2.0.6 allows a remote attacker to obtain sensitive information via the GravExtension.php and the mediaDirFunc method.

### 67. CVE-2026-78850｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T17:17:28.513)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.0 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T17:17:28.513 / 2026-10-15T18:17:29.350
- **官方描述（原文）**：An issue in Matomo v.5.11.2 allows a remote attacker to obtain sensitive information via the SiteContentDetector / SitesManager component

### 68. CVE-2026-76182｜Eclipse Foundation / Eclipse Jetty
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T09:17:18.300)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.00272 / percentile=0.18285
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T09:17:18.300 / 2026-10-15T14:41:34.110
- **官方描述（原文）**：In Eclipse Jetty, `TryPathsHandler` and `TryFilesFilter` can be configured to forward requests to template URIs such as `index?p=$path`, where `$path` is the request path in context. However, URI paths may contain characters that are reserved in URI queries so that a path of `/s&a=1` when applied to the template becomes `index?p=/s&a=1`, which is interpreted as 2 query parameters: `p=/s` and `a=1`, rather than just one query parameter `p` whose value is `/s&a=1`.

### 69. CVE-2026-63430｜rust-ammonia / ammonia
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:42.367)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:42.367 / 2026-10-15T21:17:14.177
- **官方描述（原文）**：ammonia is a Rust library for repairing and securing untrusted HTML. Prior to 3.3.2, 4.0.2, and 4.1.3, applications that explicitly allow the math tag, annotation-xml, and at least one raw-text HTML element while disallowing the encoding attribute can permit mutation cross-site scripting. ammonia does not correctly implement annotation-xml's encoding-dependent MathML integration-point behavior after attribute filtering removes encoding, so the sanitizer validates a descendant under one namespace interpretation while the browser reparses the output under another. An attacker can use that namespace transition and an allowed raw-text HTML element to execute JavaScript when a user renders the sanitized output. The required tags are not enabled by default, so applications that do not explicitly allow them are not affected. This issue is fixed in versions 3.3.2, 4.0.2, and 4.1.3.

### 70. CVE-2026-58395｜opnsense / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:18:18.583)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:18:18.583 / 2026-10-15T21:08:49.703
- **官方描述（原文）**：OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the safe-delete path reached through ApiMutableModelControllerBase::delBase() interpolates an unvalidated safe-delete token from the request URL into an XPath expression over config.xml before confirming that the token is a valid identifier. A user holding any one affected module privilege can send a crafted token to one of 21 affected delete endpoints covering Traffic Shaper, DHCP relay, Dnsmasq, Firewall Category, or Kea DHCP, causing the XPath to match configuration data across modules. The resulting error response exposes configuration item names, descriptions, reference paths, and UUIDs and provides an XPath substring-presence oracle, including for modules the user cannot otherwise access. The request does not modify configuration or perform a deletion. This issue is fixed in version 26.1.11.

### 71. CVE-2026-58394｜opnsense / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:18:18.447)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.2 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:18:18.447 / 2026-10-15T21:08:49.703
- **官方描述（原文）**：OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, src/www/system_advanced_admin.php reads certificate records into $a_cert but omits that array from legacy_html_escape_form_data() before rendering each certificate descr value in the SSL Certificate selector. The certificate description accepts HTML metacharacters, allowing a user with the page-system-certmanager privilege to store markup that executes when another user opens System Settings Administration. This issue is fixed in version 26.1.11.

### 72. CVE-2026-58393｜opnsense / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:18:18.310)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:18:18.310 / 2026-10-15T21:08:49.703
- **官方描述（原文）**：OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the OpenVPN Client Specific Override common_name field accepts path traversal sequences and openvpn_csc_conf_write() concatenates the value into /var/etc/openvpn-csc/<vpnid>/<common_name> without normalization or a basename check. The affected event handlers are client_connect.php and user_pass_verify.php. An authenticated user with Client Specific Override privileges can store the traversal value, and a matching OpenVPN client-connect or authentication event causes a generated CSO file to be written outside the intended directory. The file content is generated OpenVPN configuration rather than arbitrary bytes, and practical exploitation requires the attacker to cause a matching common name or username to be processed. This issue is fixed in version 26.1.11.

### 73. CVE-2026-58392｜opnsense / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:18:18.167)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:18:18.167 / 2026-10-15T21:08:49.703
- **官方描述（原文）**：OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.11, the NTP GPS page stores the operator-supplied initcmd value in base64 form, applies legacy_html_escape_form_data() to the encoded string, and then uses base64_decode() to decode the value directly into the GPS initialization-command textarea in src/www/services_ntpd_gps.php. Because decoding occurs after escaping, stored HTML remains unescaped at the output sink. A user with page-services-ntp-gps privilege can store a value that closes the textarea, and script executes in the session of any user who later opens the GPS page. The script can read CSRF material and perform authenticated actions, including actions available to an administrator. This issue is fixed in version 26.1.11.

### 74. CVE-2026-55875｜HeliumEdu / platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T18:17:28.130)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T18:17:28.130 / 2026-10-15T18:17:28.130
- **官方描述（原文）**：Helium is a free online student planner for classes, homework, grades, and notes. Prior to 2.2.60, any authenticated user can submit an arbitrary URL to POST /feed/externalcalendars/, where helium/feed/services/icalexternalcalendarservice.py uses validate_url to check only URL syntax before passing the value to urllib.request.urlopen, and fetch_ical_conditional periodically refetches the stored URL. The server can therefore issue requests to attacker-selected external or internal hosts, while distinct responses, including an uncaught http.client.RemoteDisconnected condition for non-HTTP services, reveal internal host and port reachability. The supported impact is forced outbound requests and internal service reconnaissance; the advisory does not demonstrate secret retrieval because the relevant ECS credentials path is task-specific and unpredictable. This issue is fixed in version 2.2.60.

### 75. CVE-2026-55871｜mayerbalintdev / GYM-One
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:41.150)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:41.150 / 2026-10-15T20:17:13.787
- **官方描述（原文）**：GYM One is open-source gym management software for fitness centers, personal trainers, and sports clubs. Prior to 1.4.1, GYM One's admin/users/index.php concatenates the search_name and search_email GET parameters into both the user-list query and the COUNT query used for pagination without prepared statements. An authenticated administrator can inject SQL through either search field to read data from arbitrary tables, including user information and password hashes. Depending on database permissions, the same injection may also permit filesystem writes. This issue is fixed in version 1.4.1.

### 76. CVE-2026-55840｜Erudika / scoold
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:40.823)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:40.823 / 2026-10-15T21:17:13.573
- **官方描述（原文）**：Scoold is a Q&A and a knowledge sharing platform for teams. Prior to 1.69.1, the getBackToUrl() method in src/main/java/com/erudika/scoold/utils/HttpUtils.java validates the backto and returnto parameters with Strings.CI.startsWith against the configured server URL. An attacker can supply an absolute URL whose hostname begins with the legitimate hostname, causing URI.resolve() to retain the attacker URL and the prefix check to accept it. A victim who follows the crafted sign-in link can be redirected to an attacker-controlled domain after authentication, enabling phishing and possible credential or token theft. This issue is fixed in version 1.69.1.

### 77. CVE-2026-55414｜nl-portal / nl-portal-backend-libraries
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T18:17:27.503)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T18:17:27.503 / 2026-10-15T19:17:40.533
- **官方描述（原文）**：NL Portal Backend Libraries provide backend components for Dutch government portals that interact with residents, customers, suppliers, and partner organizations. From 1.1.0 until 3.0.4, and in 3.1.0, the public getFormDefinitionByObjectenApiUrl and deprecated getFormDefinitionById GraphQL resolvers are reachable without CommonGroundAuthentication and forward a caller-influenced URL through ObjectenApiService.getObjectByUrl to ObjectsApiClient.getObjectByUrl, which attaches the privileged Objecten-API token. The host-equality check restricts requests to the configured Objecten-API host but does not constrain the scheme, port, or path, allowing an unauthenticated caller to induce a token-bearing request to a chosen endpoint on that host. Standard deployments are not exposed to cross-host SSRF, token capture requires attacker-controlled routing on the configured host, and typed deserialization limits returned data to objects shaped like form definitions. The 3.0 release line is fixed in version 3.0.4. The advisory does not identify a fixed 3.1 release.

### 78. CVE-2026-18662｜Eclipse Foundation / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T10:17:12.357)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.00403 / percentile=0.32988
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T10:17:12.357 / 2026-10-15T14:41:34.110
- **官方描述（原文）**：In Eclipse Jetty, across various versions of `jetty-security`, and `jetty-eeN-security`, two or more security constraints with the same http-method-omission set, and no url-patterns, are not combined properly per Jakarta Servlet Spec. Resulting in later http-method-omission sets overriding previous constraints with the same http-method-omission set.

### 79. CVE-2026-18659｜Eclipse Foundation / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T10:17:11.943)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.00428 / percentile=0.35559
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T10:17:11.943 / 2026-10-15T14:41:34.110
- **官方描述（原文）**：In Eclipse Jetty, across various versions of `jetty-security`, and `jetty-eeN-security`, and `jetty-eeN-servlet`, the Jakarta Spec constraints defined as `http-method-omission` can be bypassed by using substrings of the defined HTTP Methods.

### 80. CVE-2026-111228｜Netgate / pfSense CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:35.670)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:35.670 / 2026-10-15T21:05:32.823
- **官方描述（原文）**：Netgate pfSense CE from 2.7.1 through 2.9.0 contains a CRLF injection vulnerability in services_unbound_advanced.php that allows authenticated users with DNS Resolver: Advanced privilege to inject Unbound directives. Attackers can embed CR/LF characters in the unvalidated sock_queue_timeout parameter, which is written raw into unbound.conf, to override local records and forwarding for all clients.

### 81. CVE-2026-111171｜ethereum / web3.py
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:33.300)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:33.300 / 2026-10-15T20:17:12.173
- **官方描述（原文）**：Web3.py 7.15.0 through 7.16.0 and 8.0.0b2 through 8.0.0 contains a server-side request forgery vulnerability because _check_ip_blocked() does not unwrap IPv4-mapped IPv6 addresses in CCIP Read URL validation. Malicious contracts can return OffchainLookup URLs with IPv4-mapped IPv6 hosts or AAAA records, making clients with CCIP Read enabled send requests to loopback, private, or link-local services.

### 82. CVE-2026-111166｜sezero / libmikmod
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:32.450)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:32.450 / 2026-10-15T20:17:11.937
- **官方描述（原文）**：libmikmod through 3.3.15 contains a heap out-of-bounds read vulnerability in the IMF_Load() loader that allows attackers to read beyond allocated memory by supplying a crafted IMF module. Attackers can enable the linear-period header flag and map notes to out-of-range samples, causing noteindex indexing far past the heap allocation and crashing applications that load the file.

### 83. CVE-2026-111163｜Mindwerks / WildMIDI
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:31.550)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:31.550 / 2026-10-15T20:17:11.820
- **官方描述（原文）**：WildMIDI through 0.5.0 contains a heap out-of-bounds read vulnerability in _WM_ParseNewHmi() in src/f_hmi.c that reads past buffers when handling 0xfe sub-events. Attackers can supply a crafted HMI file placing a 0xfe 0x10 sub-event near the buffer end to read up to four bytes past the allocation, crashing the decoding application.

### 84. CVE-2026-111161｜Wohlstand / libADLMIDI
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:31.260)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:31.260 / 2026-10-15T20:17:11.703
- **官方描述（原文）**：libADLMIDI 1.6.2 through 1.6.2.1 contains an off-by-one stack out-of-bounds write vulnerability in BW_MidiSequencer that allows attackers to corrupt stack memory via crafted MIDI files. Attackers can supply a MIDI file with a note-on using status 0x9F and note 0x7F through adl_openFile() or adl_openData() to crash the hosting media player or game engine.

### 85. CVE-2026-111158｜EarthScope / libmseed
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:30.810)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:30.810 / 2026-10-15T20:17:11.590
- **官方描述（原文）**：EarthScope libmseed through 3.5.4 contains a heap out-of-bounds read vulnerability in ms3_detect() in parseutils.c that reads past truncated miniSEED 2 record buffers. Attackers can supply a 40 to 47 byte buffer passing MS2_ISVALIDHEADER to msr3_parse() or ms3_detect(), over-reading up to 8 bytes and potentially crashing the process.

### 86. CVE-2026-111156｜sezero / libtimidity
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:30.527)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:30.527 / 2026-10-15T20:17:11.470
- **官方描述（原文）**：libTiMidity through 0.2.8 contains an out-of-bounds access vulnerability in init_soundfont() in src/sndfont.c that allows attackers to corrupt memory by supplying unvalidated SF2 preset header bank and preset values. Attackers can craft a .sf2 file whose bank or preset indexes past the 128-entry tonebank or drumset arrays, causing heap memory reads, writes, and application crashes.

### 87. CVE-2026-111153｜libgme / game-music-emu
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:30.103)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:30.103 / 2026-10-15T20:17:11.350
- **官方描述（原文）**：Game Music Emu (libgme) through 0.6.5 contains a global out-of-bounds read vulnerability in Classic_Emu::mute_voices_ that allows attackers to crash applications by supplying NSF files whose voice count exceeds the 16-entry voice-type table. Attackers can craft an NSF header with chip_flags 0x3F, opened through gme_open_data or gme_open_file, to read past the static array during loading and cause denial of service.

### 88. CVE-2026-111151｜aous72 / OpenJPH
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:29.800)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:29.800 / 2026-10-15T20:17:11.237
- **官方描述（原文）**：OpenJPH through 0.32.0 contains a heap out-of-bounds write vulnerability in the HTJ2K cleanup-pass decoder that allows attackers to corrupt memory via one-row codeblocks. Attackers can supply a crafted .j2c or .jph codestream with small precinct sizes, causing the decoder to write a second row past the codeblock buffer, resulting in memory corruption and crashes.

### 89. CVE-2026-111148｜libsidplayfp / libsidplayfp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:29.353)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:29.353 / 2026-10-15T20:17:11.123
- **官方描述（原文）**：libsidplayfp through 3.1.1 contains a heap out-of-bounds read vulnerability that allows attackers to crash applications by supplying a PSID/RSID file with an unchecked data offset. Attackers can set the header data offset beyond the file size, wrapping the length calculation so resolveAddrs() reads up to 64 KiB past the heap buffer.

### 90. CVE-2026-111146｜Yeraze / ytnef
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:29.040)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:29.040 / 2026-10-15T20:17:11.010
- **官方描述（原文）**：ytnef through 2.1.2 contains a heap out-of-bounds read vulnerability in MAPIPrint() that allows attackers to read past heap allocations by supplying compressed RTF properties. Attackers can deliver a crafted winmail.dat whose decompressed RTF lacks a NUL terminator, causing printf to over-read, crashing ytnefprint and leaking adjacent heap bytes.

### 91. CVE-2026-111143｜ansilove / libansilove
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:28.563)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:28.563 / 2026-10-15T20:17:10.890
- **官方描述（原文）**：Ansilove libansilove through 1.4.2 contains an out-of-bounds read vulnerability in ansilove_xbin() in src/loaders/xbin.c that lacks bounds checks for compressed run-length records. Attackers can supply a crafted compressed XBIN file ending in a control byte such as 0x7F to read past the input buffer, crashing applications that render untrusted XBIN art.

### 92. CVE-2026-111141｜gdraheim / zziplib
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:28.267)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.7 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:28.267 / 2026-10-15T20:17:10.780
- **官方描述（原文）**：zziplib through 0.13.80 contains an out-of-bounds read vulnerability in __zzip_parse_root_directory() in zzip/zip.c that allows attackers to read past the mapped central directory in mmap builds due to an ineffective bounds check. Attackers can supply a crafted ZIP whose entry name ends at the central directory end, triggering 28-byte ZIP64 extra field over-reads via zzip_dir_open() that crash the process.

### 93. CVE-2026-111138｜NetSurf / libnsbmp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:27.840)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:27.840 / 2026-10-15T20:17:10.660
- **官方描述（原文）**：NetSurf libnsbmp through 0.1.7 contains an out-of-bounds read vulnerability in bmp_decode_rle8() and bmp_decode_rle4() because absolute-run bound checks omit the word-alignment pad byte. Attackers can supply a crafted RLE8 or RLE4 BMP ending on an odd-length absolute run to cause a one-byte heap over-read, crashing applications decoding untrusted images.

### 94. CVE-2026-111136｜swami / libinstpatch
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:27.490)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:27.490 / 2026-10-15T20:17:10.543
- **官方描述（原文）**：libInstPatch through 1.1.7 contains a heap out-of-bounds write vulnerability in the SoundFont 2 loader because ipatch_sf2_gen_is_valid() does not range-check generator IDs before the validity mask test. Attackers can supply crafted SF2 files with out-of-range pgen or igen generator IDs to write attacker-chosen values past the zone genarray, corrupting heap memory and crashing Swami or other consumers.

### 95. CVE-2026-111133｜libyal / libfsapfs
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:26.957)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:26.957 / 2026-10-15T20:17:10.427
- **官方描述（原文）**：libfsapfs through 20260921 contains an integer underflow in libfsapfs_key_encrypted_key_read_data() that allows attackers to trigger heap out-of-bounds reads via crafted KEK attributes. Attackers can supply a crafted encrypted APFS image with malformed HMAC or wrapped KEK attribute lengths to crash fsapfsinfo, pyfsapfs, dfVFS or plaso and read adjacent heap memory before password checks.

### 96. CVE-2026-111131｜libxmp / libxmp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:26.660)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:26.660 / 2026-10-15T20:17:10.310
- **官方描述（原文）**：libxmp through 4.7.4 contains an off-by-one stack out-of-bounds read vulnerability in the prowizard P61A depacker depack_p61a() in src/loaders/prowizard/p61a.c. Attackers can supply a crafted headerless P61A module with 31 samples and a 0xffe0 back-reference size word to leak stack memory into sample metadata or disrupt loading.

### 97. CVE-2026-111128｜assimp / assimp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:26.213)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:26.213 / 2026-10-15T20:17:10.190
- **官方描述（原文）**：Assimp through 6.0.5 contains a NULL pointer dereference vulnerability in the Ogre3D importer that allows attackers to crash applications via unvalidated bone indices in OgreStructs.cpp. Attackers can supply a crafted .mesh and .skeleton file referencing a missing bone, causing BoneById() to return null and crash the host process.

### 98. CVE-2026-111126｜catdoc / catdoc
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:25.923)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:25.923 / 2026-10-15T20:17:10.070
- **官方描述（原文）**：catdoc through 0.95 contains an out-of-bounds read vulnerability in the MULRK record handler of process_item() in src/xlsparse.c that allows attackers to read past the static rec buffer via a crafted end column. Attackers can supply a crafted .xls workbook or BIFF stream with a large endcol to xls2csv to disclose adjacent process memory as CSV cells or crash the process.

### 99. CVE-2026-111123｜FluidSynth / fluidsynth
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:25.460)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:25.460 / 2026-10-15T20:17:09.930
- **官方描述（原文）**：FluidSynth through 2.6.1 contains an out-of-bounds write vulnerability that allows attackers to corrupt heap and stack memory by supplying unvalidated SoundFont modulator destination values. Attackers can craft an SF2 file with PMOD/IMOD destinations of 63 to 255 that, when loaded and played, write past the voice generator array and updated_gen_bit, causing memory corruption and crashes.

### 100. CVE-2026-110877｜adplug / adplug
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:24.823)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:24.823 / 2026-10-15T20:17:09.247
- **官方描述（原文）**：AdPlug through 2.4 contains a heap out-of-bounds read vulnerability in CdmoLoader::load() in src/dmo.cpp that allows attackers to read past a heap allocation by supplying a truncated TwinTeam DMO file. Attackers can supply a 12- or 13-byte file passing dmo_unpacker::decrypt(), opened via CAdPlug::factory, to read bytes beyond packed_module and potentially crash the application.

### 101. CVE-2026-104198｜ZoneMinder / zoneminder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T20:17:06.127)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T20:17:06.127 / 2026-10-15T21:17:02.680
- **官方描述（原文）**：ZoneMinder is a free, open source closed-circuit television software application. In versions 1.34.0 through 1.36.38, the web interface mishandles failed token authentication in web/includes/auth.php. validateToken() returns false when a token is malformed or has an invalid signature, but the caller assigns that value to the global $user variable; because web/index.php tests isset($user), boolean false is treated as a present user and the normal login redirect is skipped. This can dispatch views that rely on the outer authentication gate, including the zones view, which accepts an attacker-selected monitor ID and discloses monitor and zone metadata without an independent permission check. Permission helpers receive the false user value and deny privileged operations, so unauthorized state changes have not been established. This vulnerability is fixed in version 1.36.63, where conversion to ZM\User objects causes invalid token state to fail before view dispatch. Later defense-in-depth changes explicitly leave $user unset after failed token validation and reject non-ZM\User values at the web authentication gate.

### 102. CVE-2026-100350｜getkin / kin-openapi
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:17:30.793)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:17:30.793 / 2026-10-15T19:17:12.833
- **官方描述（原文）**：kin-openapi is a Go project for handling OpenAPI files. From 0.145.0 until 0.146.0, openapi3filter repeatedly calls regexp.MustCompile for the same parameter-name regular expression inside the per-query-key loop in urlValuesDecoder.DecodeObject used to decode a deepObject query parameter. An unauthenticated remote client can send an affected endpoint a request containing many unrelated query keys, causing ValidateRequest to perform work and allocations proportional to the attacker-controlled key count for every deepObject parameter. The expression itself is fixed and this is not regular expression denial of service; the resource consumption comes from loop-invariant recompilation. This issue is fixed in version 0.146.0.

### 103. CVE-2026-100347｜getkin / kin-openapi
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T16:17:30.287)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T16:17:30.287 / 2026-10-15T17:17:07.413
- **官方描述（原文）**：kin-openapi is a Go project for handling OpenAPI files. Prior to 0.145.0, openapi3filter.ValidationHandler uses the routers/legacy router, which passes an unsupported or non-canonical HTTP method for an existing static path to openapi3.PathItem.GetOperation. The default branch of GetOperation panics before authentication runs, so an unauthenticated remote client can repeatedly send methods such as PROPFIND or lowercase get to abort connections and generate stack-trace log growth. The specific panic requires an exact static path; a concrete path matched only by a templated route does not reach the same sink. This issue is fixed in version 0.145.0.

### 104. CVE-2026-57569｜LycheeOrg / Lychee
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T17:17:24.033)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T17:17:24.033 / 2026-10-15T21:08:49.703
- **官方描述（原文）**：Lychee is a free, open-source photo-management tool. Prior to 7.6.0, the POST /api/v2/Photo::fromUrl flow validates a hostname and its resolved addresses in app/Rules/PhotoUrlRule.php but later passes the original hostname through app/Actions/Import/FromUrl.php to app/Image/Files/DownloadedFile.php for a separate fopen connection. An authenticated attacker who controls DNS responses can cause validation to observe a public address and the subsequent fetch to resolve the same hostname to a private or otherwise forbidden address. This DNS rebinding time-of-check to time-of-use mismatch bypasses the intended server-side request forgery protections and can reach services available from the Lychee server, subject to deployment and TLS behavior. This issue is fixed in version 7.6.0.

### 105. CVE-2026-55467｜OpenPrinting / cups
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T18:17:27.833)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 2.5 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T18:17:27.833 / 2026-10-15T18:17:27.833
- **官方描述（原文）**：OpenPrinting CUPS is an open source printing system for Linux and other Unix-like operating systems. Prior to 2.4.20, the cupsdCreateJob option-string builder in scheduler/job.c maps attacker-controlled destination-uri and pre-dial-string values from a configured fax queue to the phone and faxPrefix options. Unlike ordinary IPP job attributes, these mapped fax values bypass the control-character sanitizer and are copied directly into the filter options argument. A user permitted to submit a job can therefore inject control characters into the downstream option stream. The reporter states that a downstream fax filter passing these values to a shell or modem command could execute code as lp, while the maintainer states that CUPS has no confidentiality or integrity impact because the only known code-executing filter is optional Foomatic and addressed separately, leaving possible disruption of the affected queue. This issue is fixed in version 2.4.20.

### 106. CVE-2026-111233｜Netgate / pfSense CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:36.397)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:36.397 / 2026-10-15T21:05:32.823
- **官方描述（原文）**：Netgate pfSense CE 2.7.1 through 2.9.0 contains a reflected cross-site scripting vulnerability in firewall_rules.php that allows remote attackers to inject script via the unencoded if parameter. When the non-default Require Firewall Interface option is enabled, attackers can lure users with firewall rules privileges into opening a crafted GET link to execute script in the WebGUI with their privileges.

### 107. CVE-2026-111225｜Netgate / pfSense CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T19:17:35.230)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T19:17:35.230 / 2026-10-15T21:05:32.823
- **官方描述（原文）**：Netgate pfSense CE 2.5.0 through 2.9.0 contains an OS command injection vulnerability in openvpn.learn-address.sh that allows authenticated VPN clients to execute commands as the unbound user. Attackers can embed shell metacharacters in the certificate common name or username, which is interpolated unquoted into su -c strings, when DNS Resolver client registration is enabled.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-21589｜Atlassian / Multiple Products
- **Title**：Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)、DELTA_EXPLOIT_ESCALATION(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.02777 / percentile=0.86118
- **CISA KEV**：listed=true / date_added=2026-10-15 / due_date=2026-10-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Multiple Atlassian products (Bitbucket Data Center ,Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye) contain a files or directories accessible to external parties vulnerability which could allow an unauthenticated attacker to access specific files within the web application root directory in affected versions.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-57155 | P3 / 38 | opnsense / core | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-19863 | P3 / 38 | Eclipse Foundation / 未確認 | v4.0 9.3 (CRITICAL) | 0.0054 / percentile=0.44178 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110958 | P3 / 38 | Wavlink / WN530HG4B | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105039 | P3 / 38 | EnergizeLab / station-middleware | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105038 | P3 / 38 | EnergizeLab / FastAPI AI inference server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105037 | P3 / 38 | EnergizeLab / station-middleware | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105032 | P3 / 38 | EnergizeLab / FastAPI AI inference server | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102946 | P3 / 38 | authlib / joserfc | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-77711 | WATCH / 30 | Eclipse Foundation / Eclipse Jetty | v4.0 8.2 (HIGH) | 0.0032 / percentile=0.23324 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77470 | WATCH / 30 | LycheeOrg / Lychee | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77466 | WATCH / 30 | LycheeOrg / Lychee | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-76184 | WATCH / 30 | Eclipse Foundation / Eclipse Jetty | v4.0 8.2 (HIGH) | 0.00278 / percentile=0.18899 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-71490 | WATCH / 30 | opnsense / core | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-61838 | WATCH / 30 | LycheeOrg / Lychee | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55246 | WATCH / 30 | Tatsh / bincookie | v3.1 7.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-18661 | WATCH / 30 | Eclipse Foundation / 未確認 | v4.0 8.8 (HIGH) | 0.00335 / percentile=0.25293 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-18660 | WATCH / 30 | Eclipse Foundation / 未確認 | v4.0 8.8 (HIGH) | 0.00421 / percentile=0.34936 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111220 | WATCH / 30 | Netgate / pfSense CE | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111218 | WATCH / 30 | Netgate / pfSense CE | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111215 | WATCH / 30 | Netgate / pfSense CE | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110746 | WATCH / 30 | TotalSecurity / TotalAV | v3.1 7.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105040 | WATCH / 30 | EnergizeLab / NestJS auth service | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105036 | WATCH / 30 | EnergizeLab / Robot firmware (mode 104000) | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105035 | WATCH / 30 | EnergizeLab / FirmwareUpdater | v3.1 7.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105034 | WATCH / 30 | EnergizeLab / NestJS auth service | v3.1 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105033 | WATCH / 30 | EnergizeLab / AI Station firmware (RK3562) | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-100354 | WATCH / 30 | getkin / kin-openapi | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-100351 | WATCH / 30 | getkin / kin-openapi | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-99999 | WATCH / 28 | Linux / Linux | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：3；缺少 Title：29。
- EPSS 未確認：24；Exploitation status 未確認：1。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-16T05:17:55.211747+00:00`；Delta generated at：`2026-10-16T05:17:55.211747+00:00`。

---

## 可驗證資料來源

- **CVE-2026-21589** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21589) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-21589) · [Vendor / Advisory (confluence.atlassian.com)](https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html?ref=labs.watchtowr.com) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-57155** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57155)
- **CVE-2026-19863** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19863) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-19863)
- **CVE-2026-110958** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110958)
- **CVE-2026-105039** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105039)
- **CVE-2026-105038** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105038)
- **CVE-2026-105037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105037)
- **CVE-2026-105032** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105032)
- **CVE-2026-102946** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102946)
- **CVE-2026-77711** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77711) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77711)
- **CVE-2026-77470** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77470)
- **CVE-2026-77466** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77466)
- **CVE-2026-76184** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76184) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76184)
- **CVE-2026-71490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71490)
- **CVE-2026-61838** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61838)
- **CVE-2026-55246** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55246)
- **CVE-2026-18661** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18661) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-18661)
- **CVE-2026-18660** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18660) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-18660)
- **CVE-2026-111220** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111220)
- **CVE-2026-111218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111218)
- **CVE-2026-111215** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111215)
- **CVE-2026-110746** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110746)
- **CVE-2026-105040** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105040)
- **CVE-2026-105036** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105036)
- **CVE-2026-105035** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105035)
- **CVE-2026-105034** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105034)
- **CVE-2026-105033** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105033)
- **CVE-2026-100354** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100354)
- **CVE-2026-100351** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100351)
- **CVE-2026-99999** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-99999)
- **CVE-2026-84731** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84731)
- **CVE-2026-57496** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57496)
- **CVE-2026-55240** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55240)
- **CVE-2026-50619** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-50619) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-50619)
- **CVE-2026-50612** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-50612) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-50612)
- **CVE-2026-47786** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47786) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-47786)
- **CVE-2026-47218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47218)
- **CVE-2026-47168** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-47168)
- **CVE-2026-34006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-34006) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-34006)
- **CVE-2026-16438** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16438) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-16438)
- **CVE-2026-16436** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16436) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-16436)
- **CVE-2026-111444** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111444)
- **CVE-2026-111356** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111356)
- **CVE-2026-111329** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111329)
- **CVE-2026-111322** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111322)
- **CVE-2026-111312** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111312)
- **CVE-2026-111283** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111283)
- **CVE-2026-111281** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111281)
- **CVE-2026-111235** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111235)
- **CVE-2026-110957** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110957)
- **CVE-2026-110812** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110812)
- **CVE-2026-109892** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109892)
- **CVE-2026-109698** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109698)
- **CVE-2026-109694** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109694)
- **CVE-2026-109688** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109688)
- **CVE-2026-109686** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109686)
- **CVE-2026-109515** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109515)
- **CVE-2026-109219** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109219)
- **CVE-2026-109145** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109145) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109145)
- **CVE-2026-108497** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108497)
- **CVE-2026-105474** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105474)
- **CVE-2026-104798** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104798)
- **CVE-2026-102764** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102764)
- **CVE-2026-102469** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102469) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-102469)
- **CVE-2026-101287** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101287) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-101287)
- **CVE-2026-78851** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78851)
- **CVE-2026-78850** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78850)
- **CVE-2026-76182** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76182) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76182)
- **CVE-2026-63430** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63430)
- **CVE-2026-58395** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58395)
- **CVE-2026-58394** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58394)
- **CVE-2026-58393** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58393)
- **CVE-2026-58392** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58392)
- **CVE-2026-55875** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55875)
- **CVE-2026-55871** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55871)
- **CVE-2026-55840** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55840)
- **CVE-2026-55414** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55414)
- **CVE-2026-18662** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18662) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-18662)
- **CVE-2026-18659** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18659) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-18659)
- **CVE-2026-111228** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111228)
- **CVE-2026-111171** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111171)
- **CVE-2026-111166** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111166)
- **CVE-2026-111163** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111163)
- **CVE-2026-111161** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111161)
- **CVE-2026-111158** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111158)
- **CVE-2026-111156** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111156)
- **CVE-2026-111153** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111153)
- **CVE-2026-111151** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111151)
- **CVE-2026-111148** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111148)
- **CVE-2026-111146** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111146)
- **CVE-2026-111143** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111143)
- **CVE-2026-111141** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111141)
- **CVE-2026-111138** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111138)
- **CVE-2026-111136** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111136)
- **CVE-2026-111133** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111133)
- **CVE-2026-111131** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111131)
- **CVE-2026-111128** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111128)
- **CVE-2026-111126** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111126)
- **CVE-2026-111123** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111123)
- **CVE-2026-110877** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110877)
- **CVE-2026-104198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104198)
- **CVE-2026-100350** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100350)
- **CVE-2026-100347** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100347)
- **CVE-2026-57569** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57569)
- **CVE-2026-55467** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55467)
- **CVE-2026-111233** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111233)
- **CVE-2026-111225** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111225)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
