# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**34** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=34。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **0**、WATCH **30**。
- Baseline：state / generated_at=2026-11-02T06:59:28.559925+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **34** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-29508｜ReadyMedia / ReadyMedia (MiniDLNA)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T21:17:31.087)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T21:17:31.087 / 2026-11-02T21:17:31.087
- **官方描述（原文）**：ReadyMedia (formerly MiniDLNA) versions 1.3.0 through 1.3.3 contain a stack-based buffer overflow vulnerability that allows remote attackers to corrupt stack memory by crafting a malicious DFF audio file with an oversized PROP chunk size value that is used unvalidated to allocate a variable-length stack array and read file data into it. Attackers can place a crafted DFF file in a directory monitored by ReadyMedia to trigger automatic parsing via inotify, achieving remote code execution on unprotected builds or denial of service on hardened builds with stack protections.

### 2. CVE-2026-120448｜doramart / DoraCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:27.737)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:27.737 / 2026-11-02T19:35:33.347
- **官方描述（原文）**：DoraCMS through 3.1.0 contains a mass assignment vulnerability in the PUT /api/v1/user/api-keys/:id endpoint that allows authenticated low-privileged users to rebind their API key to another user's account. Attackers can set the userId field on their own key to a victim's id, then act as that victim to modify profiles and publish or delete content.

### 3. CVE-2026-120444｜sea-team / GoFound
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:26.917)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:26.917 / 2026-11-02T19:35:33.347
- **官方描述（原文）**：GoFound through 1.4.1 contains a path traversal vulnerability that allows unauthenticated attackers to delete arbitrary directories by supplying ../ sequences in the database parameter. Attackers can send GET requests to /api/db/create and /api/db/drop, directly or via a victim's browser, triggering os.RemoveAll on directories outside the data directory.

### 4. CVE-2026-120425｜munafio / Chatify
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:23.407)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:23.407 / 2026-11-02T19:35:33.347
- **官方描述（原文）**：Chatify before 1.6.4 contains an authorization bypass vulnerability in the Pusher channel authorization endpoint that allows authenticated users to subscribe to other users' private channels by supplying arbitrary channel names. Attackers can request a signature for private-chatify.<victim id> via POST /chat/auth to receive the victim's incoming private messages and attachments in real time.

### 5. CVE-2026-119737｜Nexbox / A95X
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T20:17:38.143)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T20:17:38.143 / 2026-11-02T21:17:29.267
- **官方描述（原文）**：The pppoe_wrapper vendor daemon from the Amlogic Android SDK, as shipped on Nexbox A95X (Amlogic S905/S905X) TV boxes, contains a command injection vulnerability that allows local attackers to execute arbitrary commands as root by sending crafted messages to a world-writable AF_UNIX datagram socket at /dev/socket/pppoe_wrapper. Attackers can send a message beginning with 'pppd pty' followed by shell metacharacters and arbitrary commands, which are passed unfiltered to system(3) and executed by /system/bin/sh -c as root, resulting in full privilege escalation.

### 6. CVE-2026-119733｜Petpooja / Munshi
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T19:18:02.037)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T19:18:02.037 / 2026-11-02T20:17:37.993
- **官方描述（原文）**：Munshi (by Petpooja) before 2026-07-07 contained a missing authorization vulnerability in its company deletion workflow at DELETE /api/companies/{company_id}, where the application fails to enforce the dedicated company_delete permission or verify company ownership. An authenticated invited sub-user with mere access to a company can exploit this flaw to perform a hard delete of the company record, causing irreversible loss of associated business data including invoices, configurations, and chat sessions.

### 7. CVE-2026-106808｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T18:18:34.120)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T18:18:34.120 / 2026-11-02T19:35:33.347
- **官方描述（原文）**：OpenAirInterface Core Network v2.2.1 has a stack-based buffer overflow vulnerability in the OAI CN5G UDM Nudm_UEAU Generate Authentication Data endpoint. The UDM passes attacker-controlled resynchronizationInfo.rand and auts values to conv::hex_str_to_uint8(), which converts arbitrary-length hex strings into fixed-size stack buffers without validating the destination size. An unauthenticated attacker with access to the SBI interface and a valid SUPI can submit an oversized value to overwrite adjacent stack memory, corrupt the stack canary, and terminate the UDM process.

### 8. CVE-2026-106804｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T17:17:33.453)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T17:17:33.453 / 2026-11-02T19:34:23.993
- **官方描述（原文）**：A stack-based buffer overflow exists in Kamailio v6.1.3 and v6.1.4 in the ims_qos_npn module. The w_rx_aar_register() function copies the attacker-controlled host field from the SIP `Via` header into a fixed 46-byte stack buffer without validating its length. An unauthenticated remote attacker can trigger the vulnerability with a crafted SIP `REGISTER` request, causing stack corruption and termination of the affected Kamailio instance, resulting in denial of service.

### 9. CVE-2026-97718｜Absolute Security / Secure Access
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T20:18:05.253)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T20:18:05.253 / 2026-11-02T20:18:05.253
- **官方描述（原文）**：CVE-2026-97718 Is a cross-site request forgery vulnerability in version 14.60 of the Secure Access server. Because of a bypassed security control, an attacker can cause an admin to create an account under their control.

### 10. CVE-2026-94290｜SUSE / Rancher
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T16:17:45.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T16:17:45.190 / 2026-11-03T05:18:55.230
- **官方描述（原文）**：SUSE Rancher Fleet clusters reference a kubeconfig secret that the controller uses to install and manage a Fleet agent on the target cluster. The controller did not sufficiently restrict which kubeconfig secrets a Fleet Cluster object was allowed to reference. As a result, a Fleet cluster defined in a namespace an ordinary user controls could be associated with administrative credentials for the management cluster itself, causing the controller to manage the management cluster on that user's behalf and to run that user's Fleet content there with elevated privileges. This affects SUSE Rancher Fleet 0.16.0 up to 0.16.3, 0.15.0 up to 0.15.8, 0.14.0 up to 0.14.12, 0.13.0 up to 0.13.17 and possible older versions.

### 11. CVE-2026-88811｜SUSE / Rancher
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T17:17:45.793)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T17:17:45.793 / 2026-11-03T05:18:53.400
- **官方描述（原文）**：Missing filtering in the SUSE Rancher Manager meta proxy could cause passed in rancher credentials to be leaked to cloud providers. This affects SUSE Rancher 2.15.0 up to 2.15.3, 2.14.0 up to 2.14.7, 2.13.0 up to 2.13.11,

### 12. CVE-2026-86596｜clavaque / s2Member – Excellent for All Kinds of Memberships, Content Restriction Paywalls & Member Access Subscriptions
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T22:17:23.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T22:17:23.490 / 2026-11-02T22:17:23.633
- **官方描述（原文）**：The s2Member plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, <= 260927 via the 'item_name' parameter parameter. This is due to insufficient sanitization in strip_php_tags_deep(), which only strips literal '<?' sequences, combined with a post-interpolation placeholder cleanup that reassembles a valid '<?php' opener after the attacker-controlled value has already been embedded in the email template. This makes it possible for authenticated attackers, with custom-level access and above, to execute code on the server.

### 13. CVE-2026-77876｜Control Web Panel / Control Web Panel
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T16:17:43.293)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T16:17:43.293 / 2026-11-02T19:35:33.347
- **官方描述（原文）**：Control Web Panel (CWP) before webpanel_version 1.16 contains an OS command injection vulnerability in the protected_directory user panel module that allows attackers to execute arbitrary commands by submitting unescaped input through the file POST parameter in the acc=deletedp action. Attackers can exploit this flaw, which passes attacker-controlled input directly into a shell_exec call, to achieve code execution in the user panel context.

### 14. CVE-2026-73696｜Control Web Panel / Control Web Panel
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:37.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:37.480 / 2026-11-02T19:35:33.347
- **官方描述（原文）**：Control Web Panel (CWP) before webpanel_version 1.12 contains an execution after redirect vulnerability in the user panel authentication flow (CWPUserIndex) that allows unauthenticated attackers to bypass authentication by exploiting a missing exit() call after a header('Location: ...') redirect. Attackers can send unauthenticated requests to continue PHP execution past the redirect, reaching user panel functionality that should require authentication.

### 15. CVE-2026-120534｜ACF Extended / Advanced Custom Fields: Extended PRO
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T05:18:31.987)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T05:18:31.987 / 2026-11-03T05:18:32.140
- **官方描述（原文）**：The Advanced Custom Fields: Extended PRO plugin for WordPress is vulnerable to Limited Code Injection in all versions up to, and including, 0.9.2.6 via the render_field function. This is due to insufficient validation of form configuration parameters before merging into field settings and passing to call_user_func_array in the render_field method. This makes it possible for unauthenticated attackers to call arbitrary WordPress functions with controlled arguments. Method 1 requires the administrator to enable the non-default 'shortcode_preview' setting for the target form, while Method 2 requires the server environment to lack OpenSSL functions, causing ACF Pro's acf_decrypt to fall back to unverified base64 decoding.

### 16. CVE-2026-120518｜kalengi / BuddyPress XProfile Custom Image Field
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-03T05:18:31.380)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-03T05:18:31.380 / 2026-11-03T05:18:31.657
- **官方描述（原文）**：The BuddyPress XProfile Image Field plugin for WordPress is vulnerable to arbitrary file deletion in all versions up to, and including, 3.1.0. This is due to bpxp_image_field_update_on_user_activation() calling unlink() on a path built from visitor-supplied signup metadata with no realpath() resolution, no containment check against the profile-image directory and no extension allow-list. Submitting a zero-byte file with the 'field_N_hidden' parameter during registration makes the plugin store the raw value, which is then resolved against the document root when the pending signup is activated. This makes it possible for unauthenticated attackers to delete arbitrary files on the server, which can easily lead to remote code execution when the right file (such as wp-config.php) is deleted. Requires open registration and an image-type profile field on the signup form.

### 17. CVE-2026-120459｜mpdavis / python-jose
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:29.867)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:29.867 / 2026-11-02T19:14:53.030
- **官方描述（原文）**：python-jose through 3.5.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge JWTs because HMACKey and CryptographyHMACKey accept zero-length HMAC secrets. When an application's HS256/HS384/HS512 verification key resolves to empty, such as an oct JWK with empty k, attackers can forge tokens with arbitrary claims that jwt.decode accepts.

### 18. CVE-2026-120447｜bufanyun / HotGo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:27.523)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:27.523 / 2026-11-03T00:17:18.797
- **官方描述（原文）**：HotGo 2.8.4 through 2.15.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to choose the SMS login verification code by supplying the Code field to /admin/sms/send. Attackers who know a user's mobile number can set a known code and sign in through /admin/site/mobileLogin to take over accounts, including administrators.

### 19. CVE-2026-120442｜xianhc / ape-volo-admin
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:26.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:26.490 / 2026-11-02T19:35:33.347
- **官方描述（原文）**：ape-volo-admin before 3.6.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge administrator tokens using a hardcoded JWT signing key in appsettings.json. Attackers can sign tokens offline with the jti claim set to the seeded administrator id to gain full API control over users, roles, permissions and data.

### 20. CVE-2026-120213｜@fastify/http-proxy / @fastify/http-proxy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T11:17:31.137)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T11:17:31.137 / 2026-11-02T17:17:39.467
- **官方描述（原文）**：@fastify/http-proxy is a Fastify plugin that proxies HTTP requests to an upstream server under a configured prefix. In versions 9.0.0 through 11.6.5, when an application uses parameterized prefix and rewritePrefix options to pin clients to a fixed upstream path, the plugin substitutes URL-decoded route parameters into rewritePrefix without re-encoding them. A parameter value that encodes a path separator together with a fragment or query delimiter therefore decodes into real separators and delimiters that inject extra upstream path segments and strip the mandatory suffix the rewritePrefix was meant to enforce, without using any dot-dot traversal. An unauthenticated remote attacker can use this to reach upstream locations outside the intended prefix, leading to path-restriction bypass and, depending on the upstream, server-side request forgery or authorization bypass in the proxied service. The issue is fixed in @fastify/http-proxy 11.6.6, and users should upgrade to 11.6.6 or later. There is no workaround other than upgrading.

### 21. CVE-2026-119085｜AWS / virtual-engineering-workbench
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T18:18:44.283)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T18:18:44.283 / 2026-11-02T19:34:23.993
- **官方描述（原文）**：Improper neutralization of special elements used in a template engine in the publishing component of Amazon Virtual Engineering Workbench (VEW) could allow a remote authenticated third party to run arbitrary code with the permissions of the publishing Lambda's IAM role. This could allow access to data and resources across all tenant projects. The code is reachable through a crafted CloudFormation template body containing template engine directives submitted through the product versioning API. To remediate this issue, users should redeploy from the latest version of awslabs/virtual-engineering-workbench.

### 22. CVE-2026-116769｜Absolute Security / Secure Access
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T20:17:33.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T20:17:33.527 / 2026-11-02T20:17:33.527
- **官方描述（原文）**：CVE-2026-116769 is an authentication bypass vulnerability in Secure Access servers starting with version 13.0 and prior to 14.61. Attackers can modify security settings of a client via the server.

### 23. CVE-2026-116606｜Barracuda Networks / Barracuda Email Security Gateway (ESG)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T13:17:37.017)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T13:17:37.017 / 2026-11-03T05:18:31.200
- **官方描述（原文）**：An authentication bypass in Barracuda Email Security Gateway versions earlier than 9.4.0.030 allows an unauthenticated remote attacker to invoke a configuration-import function and restore a crafted, compatible backup archive, resulting in unauthorized modification of the appliance’s global configuration.

### 24. CVE-2026-105769｜chainguard / kaniko
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T17:17:32.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T17:17:32.670 / 2026-11-02T19:34:23.993
- **官方描述（原文）**：kaniko before 1.25.20 can send a Microsoft Entra ID (Azure AD) access token for Azure Resource Manager to an attacker-controlled registry host. kaniko uses the Azure Container Registry credential helper github.com/chrismellard/docker-credential-acr-env, which decides whether a host is an ACR registry with an unanchored regular expression, so any hostname containing .azurecr.io, .azurecr.cn, .azurecr.de or .azurecr.us is accepted. kaniko consults this helper for any registry that has no credentials in the Docker config and is not a Google or Amazon ECR registry, before contacting the registry. A Dockerfile that references an image on a lookalike host, such as FROM x.azurecr.io.attacker.com/img or COPY --from=<image>, causes the helper to obtain a token from the build's Azure identity (service principal environment variables, federated workload identity token, or managed identity) and POST it to https://<host>/oauth2/exchange. The attacker can use the token against Azure Resource Manager with the identity's role assignments until it expires, and can exchange it for credentials to any ACR registry the identity can access. No RUN instruction or push is required. This issue is fixed in 1.25.20.

### 25. CVE-2026-105606｜joomlaboat.com / Custom Tables extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T19:17:50.330)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T19:17:50.330 / 2026-11-02T20:17:27.253
- **官方描述（原文）**：Joomla Extension - joomlaboat.com - Unauthenticated arbitrary file upload in Custom Tables < 3.7.8 - An unauthenticated attacker can upload a polyglot file with an attacker-controlled extension to the web-accessible tmp directory of any Joomla site that exposes a public Custom Tables submission form, and the stored path is disclosed in the response. By default the uploaded file is served as static content, so the primary impact is an unauthenticated arbitrary file write to a web-accessible directory, which allows hosting of attacker-controlled content (for example phishing or malware pages) under the victim's domain.

### 26. CVE-2026-105604｜dj-extensions.com / DJ-Classifieds extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T19:17:49.997)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T19:17:49.997 / 2026-11-02T19:35:33.347
- **官方描述（原文）**：Joomla Extension - dj-extensions.com - Unauthenticated SQL injection in DJ-Classifieds < 3.11.3 - The Joomla extension DJ-Classifieds is vulnerable to an unauthenticated SQL injection vector in the frontend search.

### 27. CVE-2026-105603｜dj-extensions.com / DJ-Classifieds extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T19:17:49.823)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T19:17:49.823 / 2026-11-02T19:35:33.347
- **官方描述（原文）**：Joomla Extension - dj-extensions.com - Authenticated arbitrary file upload in DJ-Classifieds < 3.11.3 - The Joomla extension DJ-Classifieds is vulnerable to an unprivileged file upload, leading to full RCE.

### 28. CVE-2026-102435｜themefic / Ultra Addons for Contact Form 7
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T20:17:26.287)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T20:17:26.287 / 2026-11-02T20:17:26.440
- **官方描述（原文）**：The Ultra Addons for Contact Form 7 plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient file path validation in the _getObjAttr function in all versions up to, and including, 3.5.54. This makes it possible for unauthenticated attackers to delete arbitrary files on the server, which can easily lead to remote code execution when the right file is deleted (such as wp-config.php). This requires the PDF Generator add-on to be active and a Contact Form 7 form to be configured for PDF generation, as the WPCF7_Submission POP gadget chain relies on CF7 being present to complete the file deletion via __destruct(). Note: This vulnerability can only be exploited when the PDF generator feature is enabled.

### 29. CVE-2026-120497｜AWS / aidlc-traceability
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T19:18:04.277)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 4.6 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T19:18:04.277 / 2026-11-02T20:17:40.867
- **官方描述（原文）**：Stored cross-site scripting (XSS) in the HTML report generator in the aidlc-traceability CLI in AWS AI-DLC Workflows before 2026-07-03 might allow an actor who can modify a project's AI-DLC artifact files to execute arbitrary script in the browser of a user who opens a generated HTML traceability report via crafted artifact titles or descriptions. To remediate this issue, users should remove any local copy of the aidlc-traceability CLI obtained before 2026-07-03, or update it to commit 96cf0ea or later. The CLI was removed from the repository on 2026-07-16.

### 30. CVE-2026-120457｜Deutsches Klimarechenzentrum / libaec
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:29.507)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:29.507 / 2026-11-02T19:34:23.993
- **官方描述（原文）**：libaec through 1.1.7 contains an out-of-bounds read vulnerability in m_se_decode() in src/decode.c that allows attackers to bypass a signed bounds check via an overlong fundamental sequence. Attackers can supply a crafted CCSDS 121.0/SZIP stream with 2^31 or more zero bits to crash the decoder or leak adjacent memory into decoded samples.

### 31. CVE-2026-120453｜The Sleuth Kit / The Sleuth Kit
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:28.750)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 4.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:28.750 / 2026-11-02T19:34:23.993
- **官方描述（原文）**：The Sleuth Kit through 4.15.0 contains a heap out-of-bounds read vulnerability in hfs_load_extended_attrs() in tsk/fs/hfs.c that reads the decmpfs header without checking attribute length. Attackers can supply a crafted HFS+ image with a com.apple.decmpfs attr_size of 1 to 15 to read past the allocation and crash analysis tools like istat or icat.

### 32. CVE-2026-120449｜Outline / Outline
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:27.937)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:27.937 / 2026-11-02T19:34:23.993
- **官方描述（原文）**：Outline before 1.12.0 contains an improper access control vulnerability that allows unauthenticated users to read unpublished documents because the share loader ignores unpublished status. Attackers holding an existing share link can query shares.info, documents.info, or the /s/ share routes to read withdrawn content, while shares.revoke returns 404 and blocks revocation.

### 33. CVE-2026-120428｜Chaitin / PandaWiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T15:17:24.010)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T15:17:24.010 / 2026-11-02T19:35:33.347
- **官方描述（原文）**：PandaWiki 3.65.0 through 3.87.5 contains a stored cross-site scripting vulnerability that allows unauthenticated attackers to upload HTML files with image extensions via /share/v1/common/file/upload. Attackers can lure administrators to /static-file/<key>?a=.pdf, bypassing the nginx attachment header to serve HTML inline and steal the panda_wiki_token JWT for session takeover.

### 34. CVE-2026-120349｜dayrui / XunRuiCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T07:18:03.843)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T07:18:03.843 / 2026-11-02T16:19:19.997
- **官方描述（原文）**：A security flaw has been discovered in dayrui XunRuiCMS up to 4.7.4. Affected by this issue is the function str_replace of the file /var/www/html/zzmob/index.php of the component Mobile Site Directory. The manipulation of the argument dirname results in code injection. The attack can be launched remotely. The exploit has been released to the public and may be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-29508 | WATCH / 30 | ReadyMedia / ReadyMedia (MiniDLNA) | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-120448 | WATCH / 30 | doramart / DoraCMS | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-120444 | WATCH / 30 | sea-team / GoFound | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-120425 | WATCH / 30 | munafio / Chatify | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-119737 | WATCH / 30 | Nexbox / A95X | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-119733 | WATCH / 30 | Petpooja / Munshi | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-106808 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-106804 | WATCH / 30 | 未確認 / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97718 | WATCH / 28 | Absolute Security / Secure Access | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94290 | WATCH / 28 | SUSE / Rancher | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-88811 | WATCH / 28 | SUSE / Rancher | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-86596 | WATCH / 28 | clavaque / s2Member – Excellent for All Kinds of Memberships, Content Restriction Paywalls & Member Access Subscriptions | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-77876 | WATCH / 28 | Control Web Panel / Control Web Panel | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-73696 | WATCH / 28 | Control Web Panel / Control Web Panel | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-120534 | WATCH / 28 | ACF Extended / Advanced Custom Fields: Extended PRO | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120518 | WATCH / 28 | kalengi / BuddyPress XProfile Custom Image Field | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120459 | WATCH / 28 | mpdavis / python-jose | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120447 | WATCH / 28 | bufanyun / HotGo | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120442 | WATCH / 28 | xianhc / ape-volo-admin | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120213 | WATCH / 28 | @fastify/http-proxy / @fastify/http-proxy | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-119085 | WATCH / 28 | AWS / virtual-engineering-workbench | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-116769 | WATCH / 28 | Absolute Security / Secure Access | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-116606 | WATCH / 28 | Barracuda Networks / Barracuda Email Security Gateway (ESG) | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105769 | WATCH / 28 | chainguard / kaniko | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105606 | WATCH / 28 | joomlaboat.com / Custom Tables extension for Joomla | v4.0 9.5 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105604 | WATCH / 28 | dj-extensions.com / DJ-Classifieds extension for Joomla | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-105603 | WATCH / 28 | dj-extensions.com / DJ-Classifieds extension for Joomla | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-102435 | WATCH / 28 | themefic / Ultra Addons for Contact Form 7 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120497 | WATCH / 22 | AWS / aidlc-traceability | v4.0 4.6 (MEDIUM) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-120457 | WATCH / 22 | Deutsches Klimarechenzentrum / libaec | v4.0 5.8 (MEDIUM) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：2；缺少 Product：2；缺少 Title：30。
- EPSS 未確認：30；Exploitation status 未確認：10。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-03T07:24:28.430596+00:00`；Delta generated at：`2026-11-03T07:24:28.430596+00:00`。

---

## 可驗證資料來源

- **CVE-2026-29508** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-29508)
- **CVE-2026-120448** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120448)
- **CVE-2026-120444** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120444)
- **CVE-2026-120425** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120425)
- **CVE-2026-119737** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119737)
- **CVE-2026-119733** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119733)
- **CVE-2026-106808** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-106808)
- **CVE-2026-106804** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-106804)
- **CVE-2026-97718** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97718)
- **CVE-2026-94290** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94290)
- **CVE-2026-88811** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88811)
- **CVE-2026-86596** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86596)
- **CVE-2026-77876** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77876)
- **CVE-2026-73696** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73696)
- **CVE-2026-120534** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120534)
- **CVE-2026-120518** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120518)
- **CVE-2026-120459** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120459)
- **CVE-2026-120447** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120447)
- **CVE-2026-120442** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120442)
- **CVE-2026-120213** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120213)
- **CVE-2026-119085** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119085)
- **CVE-2026-116769** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116769)
- **CVE-2026-116606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116606)
- **CVE-2026-105769** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105769)
- **CVE-2026-105606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105606)
- **CVE-2026-105604** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105604)
- **CVE-2026-105603** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105603)
- **CVE-2026-102435** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102435)
- **CVE-2026-120497** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120497)
- **CVE-2026-120457** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120457)
- **CVE-2026-120453** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120453)
- **CVE-2026-120449** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120449)
- **CVE-2026-120428** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120428)
- **CVE-2026-120349** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120349)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
