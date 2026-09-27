# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**18** 筆符合目前門檻的重要變化；事件統計：EXPLOITATION_CHANGED=1、NEW_CVE=17。
- Intelligence 候選：**30** 筆；P1 **12**、P2 **0**、P3 **0**、WATCH **18**。
- Baseline：state / generated_at=2026-09-26T05:42:30.974498+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-93616、CVE-2026-85706、CVE-2026-85046、CVE-2026-76460、CVE-2026-71362。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **18** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-85542｜IBM / Guardium Data Protection
- **Delta event**：EXPLOITATION_CHANGED (from=active; to=none)
- **Risk**：WATCH / score 20；reasons：CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.02409 / percentile=0.83424
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T14:17:20.193 / 2026-09-27T04:16:36.100
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is affected by a command injection vulnerability in the GIM bundle import functionality. An authenticated attacker can provide a crafted GIM bundle that causes attacker-controlled arguments to be passed to the tar command, resulting in arbitrary command execution with elevated privileges on the Central Manager.

### 2. CVE-2026-97163｜lomart.fr / UP plugin for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T15:16:55.890)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T15:16:55.890 / 2026-09-26T23:16:42.967
- **官方描述（原文）**：Joomla Extension - lomart.fr - Unauthenticated remote code installation in UP plugin extension 5.0.0-5.2.0, 6.0.0-6.0.29

### 3. CVE-2026-97161｜lomart.fr / UP plugin for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T15:16:55.640)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T15:16:55.640 / 2026-09-26T23:16:42.743
- **官方描述（原文）**：Joomla Extension - lomart.fr - Various path traversal / file access vectors in UP plugin extension 5.0.0-5.2.0, 6.0.0-6.0.29

### 4. CVE-2026-97160｜lomart.fr / UP plugin for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T15:16:55.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T15:16:55.520 / 2026-09-26T23:16:42.630
- **官方描述（原文）**：Joomla Extension - lomart.fr - Authenticated, privileged PHP command injection in UP plugin extension 5.0.0-5.2.0, 6.0.0-6.0.29

### 5. CVE-2026-94132｜acymailing.com / AcyMailing Enterprise extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T15:16:55.397)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T15:16:55.397 / 2026-09-26T23:16:39.827
- **官方描述（原文）**：Joomla Extension - acymailing.com - Remote Code Execution vulnerability in mailbox action feature in AcyMailing Enterprise extension < 11.1.0 - MIME parts of incoming emails were saved to media/com_acym/upload/ with no extension check, so anyone who could email the monitored mailbox could write a PHP file into the web root.

### 6. CVE-2026-94130｜joomlaboat.com / YouTube Gallery extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T14:17:00.880)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T14:17:00.880 / 2026-09-26T23:16:39.607
- **官方描述（原文）**：Joomla Extension - joomlaboat.com - Unauthenticated SQL injection in YouTube Gallery extension < 5.7.3 - An SQL injection vulnerability in video search functionality and sorting allowed attackers to inject SQL commands in read queries.

### 7. CVE-2026-85984｜cyberlord92 / miniOrange OTP Login, Verification and SMS Notifications
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T18:16:31.010)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T18:16:31.010 / 2026-09-26T23:16:38.380
- **官方描述（原文）**：The miniOrange OTP Login, Verification and SMS Notifications plugin for WordPress is vulnerable to Authentication Bypass via the mo_wp_login_intent parameter in all versions up to, and including, 5.5.5. This is due to a missing password-intent guard in the skip_pass_fallback-enabled configuration branch of the mo_by_pass_login() function, which treats administrator role membership alone as sufficient authentication whenever the unauthenticated, unverified POST parameter mo_wp_login_intent is submitted with the value otp, causing mo_get_user() to skip wp_authenticate_username_password() and resolve a WP_User purely from a username lookup. This makes it possible for unauthenticated attackers to log in as any existing administrator account by supplying only a known username and an empty password alongside mo_wp_login_intent=otp, with no password or OTP verification required. Exploitation is conditional on a site administrator having simultaneously enabled the following plugin options: WP Login OTP, Login with Only OTP, Allow Users to Login with Username and Password, and Admin OTP Bypass.

### 8. CVE-2026-82901｜themefic / Ultra Addons for Contact Form 7
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T19:16:28.427)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T19:16:28.427 / 2026-09-26T23:16:37.000
- **官方描述（原文）**：The Ultra Addons for Contact Form 7 plugin for WordPress is vulnerable to Arbitrary File Upload due to insufficient file type validation in the 'uacf7_wpcf7_mail_components' function in all versions up to, and including, 3.5.50. This makes it possible for unauthenticated attackers to upload arbitrary files on the affected site's server which may make remote code execution possible. Note: This is only exploitable when the plugin's PDF Generator module is enabled, which is disabled by default.

### 9. CVE-2026-18143｜Addify / Request a Quote for WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T07:17:02.017)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00413 / percentile=0.32983
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T07:17:02.017 / 2026-09-26T23:16:34.427
- **官方描述（原文）**：The Request a Quote for WooCommerce plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 2.9.2 via the `afrfq_submit_quote_via_popup()` function. This is due to missing file extension and MIME type validation in the popup upload handler, which uses the raw attacker-supplied filename directly as the destination for `move_uploaded_file()`. This makes it possible for unauthenticated attackers to upload executable files, such as PHP files, to a web-accessible temporary RFQ upload directory when a public quote rule with the multi-page popup flow is enabled.

### 10. CVE-2026-100835｜edgelesssys / contrast
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-27T02:17:21.640)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-27T02:17:21.640 / 2026-09-27T02:17:21.640
- **官方描述（原文）**：Contrast before 1.16.0 is susceptible to remote attestation relay attacks. Contrast accepted any TEE attestation report that verified correctly and contained the expected firmware patch levels and software measurements, regardless of which machine produced it, so attestation was not bound to specific, physically trusted hardware. An attacker who can both intercept network traffic between the CLI and the Coordinator (or between the Coordinator and an attested component) and forge reports or extract secrets from any single TEE machine under their physical control can relay such a report to impersonate a Contrast Coordinator or a Contrast workload, defeating identity verification in Contrast's attested TLS (aTLS).

### 11. CVE-2026-100721｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-27T02:17:17.547)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-27T02:17:17.547 / 2026-09-27T02:17:18.070
- **官方描述（原文）**：vm2 before 3.12.2 contains an authorization bypass in the NodeVM external-module resolver. When an embedder configures `require.external` with a custom resolver (and `context: 'host'`), `LegacyResolver.customResolve` in lib/resolver-compat.js records the resolved module directory in `this.externals` as `new RegExp('^' + escapeRegExp(resolvedPath))`, without requiring a path separator or end-of-string boundary. Untrusted guest code can therefore require the allowlisted module (e.g. `foo`) and then require the absolute path of a non-allowlisted sibling whose path merely shares the resolved prefix (e.g. `.../node_modules/foo2/index.js`); the sibling passes `isPathAllowedForModule` and is loaded through `hostRequire`, so its top-level code runs in the host process before the exports are wrapped with `vm.readonly`, resulting in a sandbox escape and arbitrary code execution in the host context.

### 12. CVE-2026-100720｜froxlor / froxlor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T14:16:58.230)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T14:16:58.230 / 2026-09-26T23:16:33.660
- **官方描述（原文）**：Froxlor 2.0.0 through 2.3.10 is vulnerable to stored cross-site scripting. When a customer (the lowest-privileged authenticated role) uploads an SSL certificate for one of their own domains, the Certificates API add()/update() methods parse it with openssl_x509_parse() and store the issuer organization (issuer['O']) value verbatim without sanitization. Froxlor's table-listing renderer then emits scalar cells through Twig's `raw` filter, disabling HTML auto-escaping, so when an administrator or reseller opens Domains > SSL certificates the attacker-supplied issuer value executes as script in the privileged user's session. This crosses a privilege boundary from customer to admin and can result in full administrator account takeover; because a Froxlor admin controls webserver, DNS, and PHP configuration applied by a cron job running as root, the issue can be further escalated to command execution as root on the managed server. The issue is fixed in Froxlor 2.3.12.

### 13. CVE-2026-100716｜froxlor / froxlor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T14:16:57.583)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T14:16:57.583 / 2026-09-26T14:16:57.707
- **官方描述（原文）**：Froxlor is a server administration panel. In versions 2.3.10 and earlier, the customer data-export (DataDump) cron fails to validate intermediate path components of the export destination: Froxlor\FileDir::makeCorrectDir() contains an off-by-one in its path-component walk that skips the first segment below the customer home directory, and the guard in ExportCron.php checks only the final component with is_link(). An authenticated customer whose account has the export feature enabled can schedule an export into a genuine subdirectory of their own webspace, then replace an intermediate path component with a symlink before the root-owned cron runs. The cron's `chown -R` then recursively changes ownership of the linked directory tree — for example /etc — to the customer's UID, yielding host root and cross-tenant compromise. Exploitation is deterministic and requires no race. This is an incomplete fix of GHSA-75h4-... The issue is fixed in Froxlor 2.3.12.

### 14. CVE-2026-100714｜froxlor / froxlor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T14:16:57.240)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T14:16:57.240 / 2026-09-26T23:16:33.297
- **官方描述（原文）**：Froxlor before 2.3.12 does not restrict or escape the system.letsencryptchallengepath setting: unlike sibling settings hardened in GHSA-33mp, the field has no string_regexp or required_otp guard, and its value is concatenated unescaped into the acme.sh command line built in lib/Froxlor/Cron/Http/LetsEncrypt/AcmeSh.php and executed by the root cron via FileDir::safe_exec. Because safe_exec only blacklists shell metacharacters such as ; | & > < \ $ ~ ?, spaces and quotes survive and the value is word-split into additional acme.sh arguments. An administrator, or any actor able to write settings (for example through the settings-import API), can therefore inject acme.sh options such as --renew-hook, --pre-hook or --post-hook to obtain arbitrary command execution as root at the next Let's Encrypt cron run, or use --config-home/--cert-home for arbitrary file writes. Versions up to and including 2.3.10 are affected; the issue is fixed in 2.3.12.

### 15. CVE-2026-100706｜kyverno / kyverno
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T14:16:55.843)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T14:16:55.843 / 2026-09-26T23:16:32.810
- **官方描述（原文）**：kyverno before 1.19.1 fails to properly validate URL-encoded path segments in Policy apiCall urlPath, allowing namespace tenants to bypass the per-namespace clamp and create objects in other namespaces as the admission-controller ServiceAccount. Attackers can exploit this by using percent-encoded directory traversal sequences to create MutatingWebhookConfiguration objects cluster-wide or PolicyException objects in the kyverno namespace, enabling privilege escalation to cluster admin.

### 16. CVE-2026-100684｜budibase / server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T14:16:52.720)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T14:16:52.720 / 2026-09-26T14:16:52.720
- **官方描述（原文）**：Budibase versions 3.41.0 before 3.45.0 contain an authentication bypass in the OIDC/SSO login path of @budibase/server. In sso.authenticate, when no existing user matches the incoming SSO subject, the server looks up pending user invites by the IdP-asserted email address alone — without validating an invite code and without an email_verified check (the email_verified gate protects only the existing-account lookup). An attacker who can register at an IdP that the tenant trusts for OIDC and assert a victim's invited email address (even with email_verified=false) claims the pending invite and inherits all of its granted privileges, including builder and admin.global, with no admin exclusion. This results in takeover of the invited principal and, for admin invites, full tenant compromise (access to all apps, datasources including production credentials, and automations); the invite is consumed, denying onboarding to the legitimate invitee.

### 17. CVE-2026-100607｜FlowiseAI / Flowise
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T14:16:40.983)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T14:16:40.983 / 2026-09-26T14:16:41.093
- **官方描述（原文）**：Flowise through 3.1.4 resolves SSO and local-password users solely by email without storing provider or subject identifier bindings, allowing attackers to authenticate as any existing user by claiming their email at any configured SSO provider. Attackers can gain complete account access including chatflows, credentials, and API keys by authenticating through a different SSO provider or local password than the victim's original registration method.

### 18. CVE-2026-100606｜FlowiseAI / Flowise
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-26T14:16:40.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-26T14:16:40.820 / 2026-09-26T14:16:40.933
- **官方描述（原文）**：Flowise through 3.1.4 (Enterprise/platform mode with SSO enabled) contains an authentication bypass in the SSO login path. When an SSO callback arrives with an email matching a user whose status is INVITED, verifyAndLogin (SSOBase.ts:80-94) copies the user record from the database — including the server-stored single-use invitation tempToken — into the data passed to AccountService.register(). The register handler's token lookup, email match, and expiry checks therefore pass trivially against the server's own token instead of a caller-supplied one, and the account and its organization membership are flipped to ACTIVE. As a result, anyone able to authenticate at any configured SSO provider using a pending invitee's email address as the email claim can take over that invitation and obtain the invited user's access to the organization without ever possessing the emailed invitation token, for as long as the invitation is valid (24 hours by default). At the time of the advisory no patched version was available.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-93616｜Check Point / Multiple Products
- **Title**：Check Point Multiple Products Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.19654 / percentile=0.97308
- **CISA KEV**：listed=true / date_added=2026-09-22 / due_date=2026-09-25
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Check Point Security Management Server, Multi-Domain Security Management Server, Log Server, Multi-Domain Log Server, and SmartEvent contain a path traversal vulnerability that allows an unauthenticated attacker to upload and execute arbitrary scripts.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-85706｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.91425 / percentile=0.9981
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contains a path traversal vulnerability that allows an unauthenticated user to read arbitrary files due to an improper path confinement and missing authentication enforcement in the repository commits API.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-85046｜Google / Chromium V8
- **Title**：Google Chromium V8 Type Confusion Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.48881 / percentile=0.9884
- **CISA KEV**：listed=true / date_added=2026-09-04 / due_date=2026-09-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium V8 contains a type confusion vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-76460｜Cisco / Identity Services Engine
- **Title**：Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.14026 / percentile=0.96434
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) contain an incorrect use of privileged APIs vulnerability that could allow an unauthenticated, remote attacker to gain unauthorized access to the affected device by bypassing the web-based management interface.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-71362｜Adobe / Commerce and Magento
- **Title**：Adobe Commerce and Magento Incorrect Authorization Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.87507 / percentile=0.99754
- **CISA KEV**：listed=true / date_added=2026-09-24 / due_date=2026-09-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Adobe Commerce and Magento contains an incorrect authorization vulnerability that could allow an attacker to leverage this vulnerability to gain elevated access to sensitive resources without any user interaction.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2025-57819｜Sangoma / FreePBX
- **Title**：Sangoma FreePBX Authentication Bypass Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.85463 / percentile=0.99716
- **CISA KEV**：listed=true / date_added=2025-08-29 / due_date=2025-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Sangoma FreePBX contains an authentication bypass vulnerability due to insufficiently sanitized user-supplied data allows unauthenticated access to FreePBX Administrator leading to arbitrary database manipulation and remote code execution.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2025-32432｜Craft CMS / Craft CMS
- **Title**：Craft CMS Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.99785 / percentile=0.99955
- **CISA KEV**：listed=true / date_added=2026-03-20 / due_date=2026-04-03
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Craft CMS contains a code injection vulnerability that allows a remote attacker to execute arbitrary code.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2025-30066｜tj-actions / changed-files GitHub Action
- **Title**：tj-actions/changed-files GitHub Action Embedded Malicious Code Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：0.72092 / percentile=0.99415
- **CISA KEV**：listed=true / date_added=2025-03-18 / due_date=2025-04-08
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：tj-actions/changed-files GitHub Action contains an embedded malicious code vulnerability that allows a remote attacker to discover secrets by reading Github Actions Workflow Logs. These secrets may include, but are not limited to, valid AWS access keys, GitHub personal access tokens (PATs), npm tokens, and private RSA keys.
- **CISA Required Action（原文）**：Apply mitigations as set forth in the CISA instructions linked below. Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2025-26633｜Microsoft / Windows
- **Title**：Microsoft Windows Management Console (MMC) Improper Neutralization Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 7.0 (HIGH)
- **EPSS**：0.30391 / percentile=0.98176
- **CISA KEV**：listed=true / date_added=2025-03-11 / due_date=2025-04-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft Windows Management Console (MMC) contains an improper neutralization vulnerability that allows an unauthorized attacker to bypass a security feature locally.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2025-23006｜SonicWall / SMA1000 Appliances
- **Title**：SonicWall SMA1000 Appliances Deserialization Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.23432 / percentile=0.97719
- **CISA KEV**：listed=true / date_added=2025-01-24 / due_date=2025-02-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：SonicWall SMA1000 Appliance Management Console (AMC) and Central Management Console (CMC) contain a deserialization of untrusted data vulnerability, which can enable a remote, unauthenticated attacker to execute arbitrary OS commands.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2025-20352 | P1 / 100 | Cisco / IOS and IOS XE | v3.1 7.7 (HIGH) | 0.39447 / percentile=0.98564 | listed=true / date_added=2025-09-29 / due_date=2025-10-20 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-6558 | P1 / 95 | Google / Chromium | v3.1 8.8 (HIGH) | 0.09585 / percentile=0.95313 | listed=true / date_added=2025-07-22 / due_date=2025-08-12 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-85542 | WATCH / 20 | IBM / Guardium Data Protection | v3.1 8.8 (HIGH) | 0.02409 / percentile=0.83424 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-97163 | WATCH / 28 | lomart.fr / UP plugin for Joomla | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-97161 | WATCH / 28 | lomart.fr / UP plugin for Joomla | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-97160 | WATCH / 28 | lomart.fr / UP plugin for Joomla | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-94132 | WATCH / 28 | acymailing.com / AcyMailing Enterprise extension for Joomla | v4.0 9.5 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-94130 | WATCH / 28 | joomlaboat.com / YouTube Gallery extension for Joomla | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-85984 | WATCH / 28 | cyberlord92 / miniOrange OTP Login, Verification and SMS Notifications | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-82901 | WATCH / 28 | themefic / Ultra Addons for Contact Form 7 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-18143 | WATCH / 28 | Addify / Request a Quote for WooCommerce | v3.1 9.8 (CRITICAL) | 0.00413 / percentile=0.32983 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-100835 | WATCH / 28 | edgelesssys / contrast | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-100721 | WATCH / 28 | patriksimek / vm2 | v4.0 9.5 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-100720 | WATCH / 28 | froxlor / froxlor | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-100716 | WATCH / 28 | froxlor / froxlor | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-100714 | WATCH / 28 | froxlor / froxlor | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-100706 | WATCH / 28 | kyverno / kyverno | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-100684 | WATCH / 28 | budibase / server | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-100607 | WATCH / 28 | FlowiseAI / Flowise | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-100606 | WATCH / 28 | FlowiseAI / Flowise | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：18。
- EPSS 未確認：16；Exploitation status 未確認：6。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-27T06:01:19.516470+00:00`；Delta generated at：`2026-09-27T06:01:19.516470+00:00`。

---

## 可驗證資料來源

- **CVE-2026-93616** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93616) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93616) · [Vendor / Advisory (support.checkpoint.com)](https://support.checkpoint.com/results/sk/sk1000171/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85706) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85706) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85046) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85046) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-76460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76460) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-71362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71362) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-71362) · [Vendor / Advisory (helpx.adobe.com)](https://helpx.adobe.com/security/products/magento/apsb26-92.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85542** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85542) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85542)
- **CVE-2026-97163** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97163)
- **CVE-2026-97161** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97161)
- **CVE-2026-97160** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97160)
- **CVE-2026-94132** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94132)
- **CVE-2026-94130** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94130)
- **CVE-2026-85984** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85984)
- **CVE-2026-82901** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82901)
- **CVE-2026-18143** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18143) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-18143)
- **CVE-2026-100835** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100835)
- **CVE-2026-100721** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100721)
- **CVE-2026-100720** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100720)
- **CVE-2026-100716** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100716)
- **CVE-2026-100714** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100714)
- **CVE-2026-100706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100706)
- **CVE-2026-100684** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100684)
- **CVE-2026-100607** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100607)
- **CVE-2026-100606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100606)
- **CVE-2025-57819** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-57819) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-57819) · [Vendor / Advisory (github.com)](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-m42g-xg4c-5f3h)
- **CVE-2025-32432** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-32432) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-32432) · [Vendor / Advisory (craftcms.com)](https://craftcms.com/knowledge-base/craft-cms-cve-2025-32432) · [Vendor / Advisory (github.com)](https://github.com/craftcms/cms/security/advisories/GHSA-f3gw-9ww9-jmc3)
- **CVE-2025-30066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-30066) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [CISA](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction) · [Vendor / Advisory (github.com)](https://github.com/tj-actions/changed-files/blob/45fb12d7a8bedb4da42342e52fe054c6c2c3fd73/README.md?plain=1#L20-L28)
- **CVE-2025-26633** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-26633) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-26633) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-26633)
- **CVE-2025-23006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-23006) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-23006) · [Vendor / Advisory (psirt.global.sonicwall.com)](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0002)
- **CVE-2025-20352** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-20352) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-20352) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snmp-x4LPhte)
- **CVE-2025-6558** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-6558) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-6558) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2025/07/stable-channel-update-for-desktop_15.html)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
