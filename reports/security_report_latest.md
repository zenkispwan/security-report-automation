# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**52** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=52、NEW_KEV=1。
- Intelligence 候選：**30** 筆；P1 **1**、P2 **0**、P3 **2**、WATCH **27**。
- Baseline：state / generated_at=2026-10-01T06:42:01.194668+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-104286。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **52** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-104286｜Fortinet / FortiMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T20:17:24.010)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-01 / due_date=2026-10-04
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-01T20:17:24.010 / 2026-10-02T04:18:04.950
- **官方描述（原文）**：Fortinet FortiMail contains a path traversal and an improper neutralization of NULL byte or NULL character vulnerability that may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests.

### 2. CVE-2026-56660｜GetSimpleCMS-CE / GetSimpleCMS-CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T20:17:26.643)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T20:17:26.643 / 2026-10-01T20:23:46.493
- **官方描述（原文）**：GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. Prior to version 1.5, the update handler in UpdateCE.php downloads a ZIP archive and extracts its contents into the web root without validating file types or extraction paths. Because PHP files are written into a web-accessible directory, an attacker who can cause a malicious archive to be processed achieves remote code execution as the web-server user. Entry names are also used unsafely, allowing directory traversal (../) to write files outside the intended extraction directory. This issue has been patched in version 1.5.

### 3. CVE-2026-103244｜sgoudelis / ground-station
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T11:17:17.503)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T11:17:17.503 / 2026-10-01T15:09:04.013
- **官方描述（原文）**：ground-station versions before 0.8.0 contain an authentication bypass vulnerability in the setup.restore command that allows unauthenticated attackers to execute arbitrary SQL during first-run setup mode. Attackers can invoke setup.restore via Socket.IO to plant admin users and forged session tokens, then authenticate as administrator without credentials for complete application takeover.

### 4. CVE-2026-73976｜4TUResearchData / djehuty
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T18:17:27.550)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T18:17:27.550 / 2026-10-01T18:17:27.550
- **官方描述（原文）**：djehuty is a research data repository system developed by 4TU.ResearchData. Prior to version 26.3.2, An unauthenticated attacker can inject SPARQL into the search/listing queries through three separate parameters. Because the affected queries are read (SELECT) queries, this does not write to the store, but it allows: Cross-graph data exfiltration — e.g. UNION-ing in triples from graphs the request was never scoped to (drafts/private/internal data held in the RDF store); denial of service — expensive or malformed queries that tie up the SPARQL backend / web workers. No account or user interaction is required. This issue has been patched in version 26.3.2.

### 5. CVE-2026-71542｜GetSimpleCMS-CE / GetSimpleCMS-CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T20:17:29.430)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T20:17:29.430 / 2026-10-01T20:23:46.493
- **官方描述（原文）**：GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. In versions 3.3.22 and prior, GetSimpleCMS-CE is vulnerable to stored Cross-Site Scripting (XSS) in the "Theme to Components" functionality (admin/components.php) via the title parameter. The stored title is rendered inside a double-quoted HTML attribute in the administrative interface through an output path that HTML-entity-decodes the value before printing it, without re-encoding for the attribute context. This allows persistent execution of arbitrary JavaScript in the admin panel. At time of publication, there are no publicly available patches.

### 6. CVE-2026-71426｜GetSimpleCMS-CE / GetSimpleCMS-CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T20:17:29.260)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T20:17:29.260 / 2026-10-01T20:23:46.493
- **官方描述（原文）**：GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. In versions 3.3.22 and prior, an authenticated user with page-editing rights can store an arbitrary filesystem path in a page's template attribute. On the public front-end, this value is passed unsanitized to a PHP include() when the page is rendered. Because the include path is never confined, this allows directory-traversal Local File Inclusion: arbitrary local files are included (and, if they contain PHP, executed) when any visitor requests the page. At time of publication, there are no publicly available patches.

### 7. CVE-2026-68496｜FasterXML / jackson-dataformats-binary
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T18:17:27.360)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T18:17:27.360 / 2026-10-01T19:17:24.467
- **官方描述（原文）**：The Smile parser in FasterXML jackson-dataformats-binary never invokes StreamReadConstraints.validateNameLength() when decoding JSON object property names, so the maxNameLength limit is not enforced for this format. SmileParser._handleLongFieldName() grows its internal name buffer through an unconstrained _growArrayTo() call and performs no length validation. An attacker who can have a Smile document parsed may therefore embed a single property name of unbounded length; the parser buffers the whole name in memory before returning it, whatever maxNameLength is configured to. Because StreamReadConstraints.maxDocumentLength is also disabled by default, nothing else bounds the name under default settings, so the only limits are the attacker's upload capacity and available heap, leading to memory exhaustion and denial of service. No privileges beyond the ability to submit data to a parsing endpoint are required, and exploitation needs only that the bytes reach SmileFactory parsing, directly or through an ObjectMapper configured with the Smile module. jackson-core's own JSON parsers enforce maxNameLength incrementally during name decoding; this gap is specific to the binary formats. maxNameLength and validateNameLength were introduced in jackson-core 2.16.0, so releases before 2.16.0 do not contain the constraint that is left unenforced. This issue is tracked together with the CBOR parser defect in the same vendor advisory, GHSA-3v8f-v6vx-fmrm, which covers both binary formats. The Smile parser defect (jackson-dataformats-binary issue #726) is CVE-2026-68496; the CBOR parser defect (issue #725) is assigned CVE-2026-68495.

### 8. CVE-2026-68495｜FasterXML / jackson-dataformats-binary
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T18:17:27.167)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T18:17:27.167 / 2026-10-01T19:17:24.277
- **官方描述（原文）**：The CBOR parser in FasterXML jackson-dataformats-binary never invokes StreamReadConstraints.validateNameLength() when decoding JSON object property names, so the maxNameLength limit is not enforced for this format. CBORParser._decodeLongerName() decodes a definite-length property name with no length check, and CBORParser._decodeChunkedName() delegates to the value-oriented _finishChunkedText() routine, which validates maxStringLength rather than maxNameLength. An attacker who can have a CBOR document parsed may therefore embed a single property name of unbounded length; the parser buffers the whole name in memory before returning it, whatever maxNameLength is configured to. Because StreamReadConstraints.maxDocumentLength is also disabled by default, nothing else bounds the name under default settings, so the only limits are the attacker's upload capacity and available heap, leading to memory exhaustion and denial of service. No privileges beyond the ability to submit data to a parsing endpoint are required, and exploitation needs only that the bytes reach CBORFactory parsing, directly or through an ObjectMapper configured with the CBOR module. jackson-core's own JSON parsers enforce maxNameLength incrementally during name decoding; this gap is specific to the binary formats. maxNameLength and validateNameLength were introduced in jackson-core 2.16.0, so releases before 2.16.0 do not contain the constraint that is left unenforced. This issue is tracked together with the Smile parser defect in the same vendor advisory, GHSA-3v8f-v6vx-fmrm, which covers both binary formats. The CBOR parser defect (jackson-dataformats-binary issue #725) is CVE-2026-68495; the Smile parser defect (issue #726) is assigned CVE-2026-68496.

### 9. CVE-2026-56661｜GetSimpleCMS-CE / GetSimpleCMS-CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T20:17:26.793)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T20:17:26.793 / 2026-10-01T20:23:46.493
- **官方描述（原文）**：GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. Prior to version 1.5, the update handler fetches a user-supplied URL with file_get_contents() after only format validation (FILTER_VALIDATE_URL) — there is no validation of the request destination. An attacker who can submit the form can make the server issue requests to arbitrary destinations, including internal-only services and cloud metadata endpoints (169.254.169.254). The fetched response body is written to a web-accessible file (/Tmpfile.zip) and is not deleted when the content is not a valid ZIP, turning this into a full-read SSRF: the attacker can retrieve the response of the internal request directly. This issue has been patched in version 1.5.

### 10. CVE-2026-55231｜givanz / Vvveb
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T19:17:21.680)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T19:17:21.680 / 2026-10-01T20:17:25.847
- **官方描述（原文）**：Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to version 1.0.8.6, a flawed central path sanitizer lets an authenticated admin-panel user who holds backup access (default role site_admin or higher) read and delete arbitrary files on a server. An attacker can recover database credentials from config/db.php, read host files such as /etc/passwd, and delete config/db.php to push a site back into install mode for a full takeover. This issue has been patched in version 1.0.8.6.

### 11. CVE-2026-55230｜givanz / Vvveb
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T19:17:21.503)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T19:17:21.503 / 2026-10-01T20:17:25.737
- **官方描述（原文）**：Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to version 1.0.8.6, Vvveb's HTML sanitizer fails to strip event-handler attributes when a tag carries a greater-than character inside a quoted attribute value. A low-privilege content author (default role author or contributor) can store a payload in post or product content that runs JavaScript in a browser of every visitor and of any administrator who views or previews that content, which opens a path to admin account takeover. This issue has been patched in version 1.0.8.6.

### 12. CVE-2026-103757｜Budibase / budibase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T11:17:26.177)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T11:17:26.177 / 2026-10-01T14:17:28.720
- **官方描述（原文）**：Budibase through 3.41.0 contains a server-side request forgery vulnerability in AI table generation because the uploadUrl function in packages/server/src/utilities/fileUtils.ts uses raw node-fetch instead of fetchWithBlacklist. Authenticated builder users can send a prompt to POST /api/ai/tables that places an internal URL in an attachment column, causing the server to fetch it and return a presigned object-storage URL containing the response, such as cloud metadata credentials.

### 13. CVE-2026-103263｜tornadoweb / tornado
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T11:17:21.233)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T11:17:21.233 / 2026-10-01T20:17:23.097
- **官方描述（原文）**：Tornado before 6.5.9 contains a path traversal vulnerability in StaticFileHandler that follows symbolic links inside the static root without confirming the resolved target stays within it. When a symlink pointing outside the static directory exists inside it, unauthenticated attackers can request it to read files such as configuration files, private keys, and application secrets accessible to the process user.

### 14. CVE-2026-96659｜Red Hat / Red Hat Satellite 6.16 for RHEL 8
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T17:17:35.590)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T17:17:35.590 / 2026-10-02T00:17:04.627
- **官方描述（原文）**：A flaw was found in Foreman. This vulnerability allows an authenticated user with low-level Viewer permissions to cause unauthorized information disclosure by submitting requests to template preview endpoints. By exploiting this issue, the user can access sensitive data, such as host root passwords. Furthermore, under insecure system configurations where Safemode protections are disabled, the flaw may allow the user to execute arbitrary commands as the Foreman system account.

### 15. CVE-2026-96658｜Red Hat / Red Hat Satellite 6.16 for RHEL 8
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T17:17:34.500)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T17:17:34.500 / 2026-10-02T04:18:09.757
- **官方描述（原文）**：A flaw was found in Foreman. An authenticated attacker with low-level permissions can achieve remote code execution (RCE) by bypassing the safemode sandbox within the templating engine. Due to improper handling of delegated methods, an attacker can append unauthorized functions to the allowed execution list, enabling them to run arbitrary commands on the hosting server.

### 16. CVE-2026-94620｜foundation50 / classroom50
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T16:18:08.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T16:18:08.550 / 2026-10-01T17:17:33.557
- **官方描述（原文）**：Classroom 50 is a free and open-source tool for managing and grading programming assignments via GitHub. Prior to version 1.11.0, `gh teacher download` clones each student's assignment repository and then writes autograde artifacts (`result.json` and `results.json`) into the just-cloned working tree. The write followed symlinks, so a student who committed `result.json` or `results.json` as a **symlink** (materialized verbatim by `git clone`) could redirect the teacher's write to an arbitrary path — e.g. `~/.zshrc`, `~/.ssh/authorized_keys`, a cron file, or an in-clone `.git/hooks/*` file that git subsequently executes. The written bytes are attacker-controlled (the student's uploaded release asset for `result.json`; student-chosen submit-tag names for `results.json`). This is an arbitrary file write leading to code execution as the teacher, whose `gh` token carries `admin:org`, `repo`, and `workflow` across the entire classroom organization. Version 1.11.0 contains a patch. Some workarounds are available. Avoid running `gh teacher download` against untrusted student repositories, or run it inside a disposable sandbox / container with no access to sensitive host files or credentials. Inspect cloned trees for symlinked, hardlinked, or special (`result.json`/`results.json`) entries before allowing the artifact-refresh step to run.

### 17. CVE-2026-86345｜Red Hat / Red Hat Directory Server 11
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T00:17:04.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T00:17:04.180 / 2026-10-02T00:17:04.180
- **官方描述（原文）**：A flaw was found in 389-ds-base. The server does not discard plaintext bytes already buffered from a client connection when negotiating StartTLS, allowing an on-path attacker to inject a crafted LDAP message that is processed after the TLS upgrade and whose response is delivered to the client in place of the client's own pending operation's response, due to messageID collision. This can cause a client application to treat a failed authentication (bind) attempt as successful.

### 18. CVE-2026-79901｜Fortra / BoKS Manager boks-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T14:17:30.883)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T14:17:30.883 / 2026-10-01T15:17:32.163
- **官方描述（原文）**：In deployments using BoKS keytab management, affected versions of boks_keytabmd generate Active Directory service-account passwords from a predictable pseudo-random sequence seeded with the current Unix timestamp. An attacker who knows the service principal and can estimate the password-change time can reproduce a limited candidate set and verify candidates offline.

### 19. CVE-2026-79898｜Fortra / BoKS Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T15:17:31.623)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T15:17:31.623 / 2026-10-01T20:34:26.287
- **官方描述（原文）**：Fortra BoKS Manager contains a command injection vulnerability in crlserver. An authenticated user authorized to add CRL URLs through BCC, the WSI REST or SOAP API, or the cacrl command-line interface could cause shell command substitution to be processed by crlserver as root on the BoKS Master. BCC and WSI provide network-accessible administration paths and do not require a local sudo or suexec rule; non-root use of cacrl requires such a rule.

### 20. CVE-2026-75957｜superdav42 / Ultimate Multisite – WordPress Multisite SaaS & WaaS Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T08:16:52.763)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T08:16:52.763 / 2026-10-01T14:17:30.497
- **官方描述（原文）**：The Ultimate Multisite – WordPress Multisite SaaS & WaaS Platform plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 2.15.0 via the `checkout_form` parameter of the `login_customer_after_checkout` function. This is due to the publicly accessible `wu_ajax_nopriv_wu_validate_form` AJAX handler accepting a freely obtainable checkout nonce, and the `checkout_form=wu-finish-checkout` parameter causing `get_validation_rules()` to discard all validation rules while `finish_checkout_form_fields()` returns an empty step list — forcing `is_last_step()` to return true and routing the request directly into full order processing — after which `maybe_create_customer()` resolves the attacker-supplied `email_address` to an existing WordPress user ID without any authentication or ownership verification, and `login_customer_after_checkout()` calls `wp_set_auth_cookie()` for that user ID via a passwordless code path. This makes it possible for unauthenticated attackers to log in as any existing WordPress user — including a Network Super Admin — simply by knowing their email address. Exploitation requires that the targeted user account has no pre-existing Ultimate Multisite customer record; accounts such as a Network Super Admin on a fresh Multisite install, or any administrator or editor added before Ultimate Multisite was configured, satisfy this condition and are therefore exploitable.

### 21. CVE-2026-71449｜Johnson Controls / EasyIO FS32
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T22:17:04.903)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T22:17:04.903 / 2026-10-01T22:17:04.903
- **官方描述（原文）**：: Use of Hard-coded Cryptographic Key vulnerability in Johnson Controls EasyIO FS32 allows : Retrieve Embedded Sensitive Data. This issue affects EasyIO FS32: before 3.0b63.

### 22. CVE-2026-62071｜nickboss / WordPress File Upload
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T15:17:30.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T15:17:30.647 / 2026-10-01T20:31:55.537
- **官方描述（原文）**：Unauthenticated SQL Injection in WordPress File Upload <= 5.1.10 versions.

### 23. CVE-2026-59797｜Apache Software Foundation / Apache HTTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T17:17:29.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T17:17:29.527 / 2026-10-01T21:17:23.263
- **官方描述（原文）**：Improper Privilege Management vulnerability in Apache HTTP Server's mod_ssl via SSLRequire and file-related expressions. This issue affects Apache HTTP Server: from 2.4.0 through 2.4.68.

### 24. CVE-2026-57941｜Apache Software Foundation / Apache HTTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T17:17:27.457)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T17:17:27.457 / 2026-10-01T21:17:22.607
- **官方描述（原文）**：Use After Free vulnerability in Apache HTTP Server's mod_http2 via shared session->bbtmp re-entrancy This issue affects Apache HTTP Server: from 2.4.0 through 2.4.68.

### 25. CVE-2026-56662｜GetSimpleCMS-CE / GetSimpleCMS-CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T20:17:26.950)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T20:17:26.950 / 2026-10-01T20:23:46.493
- **官方描述（原文）**：GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. Prior to version 1.5, the UpdateCE update form contained no anti-CSRF token, and the POST handler performed no token or request-origin verification. A remote attacker can host a page that auto-submits a forged POST to the update endpoint; when an authenticated administrator visits it, the server performs an attacker-directed download-and-deploy operation in the administrator's session — with no further interaction. Because the deployed content is executed (see the related ZIP-extraction advisory), this yields remote code execution. The url field is additionally written into the form unescaped, providing a secondary HTML-injection sink via a malicious upgrade.json. This issue has been patched in version 1.5.

### 26. CVE-2026-56154｜Apache Software Foundation / Apache HTTP Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T17:17:26.610)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T17:17:26.610 / 2026-10-01T21:17:22.267
- **官方描述（原文）**：Use After Free vulnerability in Apache HTTP Server's mod_rewrite when using lookahead (%{LA-U:HTTP:...}) This issue affects Apache HTTP Server: from 2.4.0 through 2.4.68.

### 27. CVE-2026-55395｜Teledyne FLIR / Aware2
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T21:17:21.830)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T21:17:21.830 / 2026-10-01T21:17:21.830
- **官方描述（原文）**：Hardcoded passwords in the access control in Teledyne FLIR Aware2 versions through 6.9.0.2 (PackBot) and 1.7.9 (FirstLook) allows remote unauthenticated attackers to access and reconfigure Teledyne FLIR PackBot and FirstLook robots running this software via reading the passwords from the firmware or documentation.

### 28. CVE-2026-55393｜Teledyne FLIR / Aware2
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T21:17:21.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T21:17:21.540 / 2026-10-01T21:17:21.540
- **官方描述（原文）**：Unvalidated pathnames in the web interface in Teledyne FLIR Aware2 versions through 6.9.0.2 (PackBot) and 1.7.9 (FirstLook) allows remote unauthenticated attackers to read configuration and security parameters on Teledyne FLIR PackBot and FirstLook robots running this software via path traversal.

### 29. CVE-2026-55083｜dhis2 / dhis2-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T19:17:21.330)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T19:17:21.330 / 2026-10-01T19:17:21.330
- **官方描述（原文）**：DHIS2 is a flexible information system for data capture, management, validation, analytics and visualization. From versions 2.42.0 to before 2.42.5.1, and from versions 2.43.0 to before 2.43.0.1, DHIS2 is vulnerable to remote code execution (RCE) via unsafe Java deserialization. This issue has been patched in versions 2.42.5.1, 2.43.0.1, and 2.44.

### 30. CVE-2026-53953｜GetSimpleCMS-CE / GetSimpleCMS-CE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T20:17:25.283)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T20:17:25.283 / 2026-10-01T20:25:35.640
- **官方描述（原文）**：GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. In version 3.3.22, the password reset endpoint can be accessed without authentication. When a reset request is submitted for an existing user, the application generates a new temporary password and immediately stores its hash as the user's new password. The temporary password is generated using PHP rand() seeded with microtime(). Because this seed is time-based and has a limited effective search space, an attacker can generate possible reset password candidates. Since the admin login endpoint does not enforce rate limiting or account lockout, these candidates can be tested online until the correct password is found. Successful exploitation may lead to administrator account takeover. At time of publication, there are no publicly available patches.

### 31. CVE-2026-19660｜DiviEngine / Divi Membership
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T05:16:38.430)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T05:16:38.430 / 2026-10-02T05:16:38.430
- **官方描述（原文）**：The Divi Membership plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 2.3.0. The `process_paypal_callback` function, hooked to the `init` action, accepts a base64-encoded `paypal_param` GET parameter with no IPN validation, no cryptographic signature check, no ownership verification, and no nonce, allowing it to trust an entirely attacker-controlled user ID value that is passed directly to `wp_set_current_user()` and `wp_set_auth_cookie()`. This makes it possible for unauthenticated attackers to log in as any existing WordPress user — including administrators — by supplying an arbitrary user ID in the `paypal_param` GET parameter, resulting in full site takeover. The vulnerability is further compounded by the fact that the PayPal gateway class is instantiated unconditionally regardless of whether PayPal is enabled or configured, ensuring the vulnerable hook is always registered on every front-end request.

### 32. CVE-2026-18397｜Thales / SConnect
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T22:17:01.220)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T22:17:01.220 / 2026-10-01T22:17:01.220
- **官方描述（原文）**：This vulnerability enables unauthenticated remote code execution (RCE) on a victim's machine by exploiting a combination of cryptographic weaknesses and memory management issues in the SConnect native host component. The attack leverages an unrestricted messaging interface between an attacker-controlled web page and the native host, allowing malicious input to bypass security checks.

### 33. CVE-2026-15989｜WebRehab / Super Forms – Drag & Drop Form Builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T08:16:51.233)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T08:16:51.233 / 2026-10-01T14:17:28.893
- **官方描述（原文）**：The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 6.3.316. This is due to the Register & Login add-on's before_email_success_msg() function whitelisting the client-submitted 'role' key and copying it into the user-data array that is passed directly to wp_insert_user(), without validating the submitted role against the administrator-configured register_user_role, without an allow-list, and without any current_user_can() capability check. This makes it possible for unauthenticated attackers to register a new account with the Administrator role by injecting role=administrator into the data submitted to any published Super Forms registration form (register_login_action='register').

### 34. CVE-2026-15896｜WebRehab / Super Forms – Drag & Drop Form Builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T06:16:40.773)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T06:16:40.773 / 2026-10-02T06:16:40.773
- **官方描述（原文）**：The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Directory Traversal in all versions up to, and including, 6.3.316 via the parse_request function. This makes it possible for unauthenticated attackers to read the contents of arbitrary files on the server, which can contain sensitive information. The optional 'file_upload_auth' setting defaults to empty, meaning no authentication is required in the default configuration; enabling this setting mitigates unauthenticated exploitation but does not remediate the path traversal itself. Exploitation on Linux requires a real 13-digit timestamp directory to exist, whereas on Windows the traversal works with any hardcoded 13-digit prefix. However, the plugin's file upload response returns the name of the created directory, which means the vulnerability is exploitable as long as file upload is enabled on the form.

### 35. CVE-2026-14984｜Teledyne FLIR / Aware2
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T20:17:24.297)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T20:17:24.297 / 2026-10-01T21:17:20.093
- **官方描述（原文）**：Cleartext transmission in the primary control endpoints of Teledyne FLIR Aware2 versions through 6.9.0.2 allows remote unauthenticated attackers to intercept, hijack, or modify session traffic against Teledyne FLIR PackBot robots running this software via sniffing or hijacking network traffic.

### 36. CVE-2026-14378｜dplugins / DevKit Pro
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T04:18:06.277)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T04:18:06.277 / 2026-10-02T04:18:06.277
- **官方描述（原文）**：The DevKit Pro plugin for WordPress is vulnerable to Authentication Bypass Leading to Administrator Account Takeover in all versions up to, and including, 2.3.0 This is due to the `revert_switch` handler trusting the attacker-controlled `original_user_id` cookie as the privileged identity: `verify_nonce_and_capability()` incorrectly checks the `manage_options` capability on the user identified by the cookie rather than on the actual requester via `current_user_can()`, while the switch-back form and a valid session-bound nonce are emitted publicly via `wp_footer` to any visitor — including unauthenticated users — whenever that cookie is present. This makes it possible for unauthenticated attackers to set the `original_user_id` cookie to any administrator's user ID, collect the rendered nonce, and POST it back to the `revert_switch` handler, causing `wp_set_auth_cookie()` to be called with the administrator's ID and granting the attacker a full administrator-level authenticated session and complete site takeover.

### 37. CVE-2026-13043｜WatchGuard / Endpoint Security
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T17:17:21.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T17:17:21.290 / 2026-10-01T17:17:21.290
- **官方描述（原文）**：A missing authentication vulnerability in the Kernel Memory Access Driver (PSKMAD) used by WatchGuard endpoint security products allows a local, authenticated attacker to bypass the driver's access-control handshake and issue arbitrary privileged commands to the driver, resulting in disclosure of kernel and process memory.

### 38. CVE-2026-12627｜Fortra / Fortra's Core Privileged Access Manager (BoKS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T16:17:40.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T16:17:40.480 / 2026-10-01T20:34:26.287
- **官方描述（原文）**：Fortra's Core Privileged Access Manager (BoKS) contains a stack-based buffer overflow vulnerability in boks_autoregisterd. A remote attacker with network access to the autoregistration service may be able to trigger memory corruption during client response processing.

### 39. CVE-2026-104480｜Discord / libdave
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T02:17:02.007)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T02:17:02.007 / 2026-10-02T02:17:02.007
- **官方描述（原文）**：Discord libdave before 1.2.0 did not reject an MLS Welcome message when the resulting group roster contained an unrecognized participant. An attacker in control of the DAVE signaling path (the voice gateway, or an equivalent position able to add, alter, or withhold signaling messages to a client) could cause affected clients to accept an unauthorized member into the end-to-end encrypted media session, compromising the confidentiality and integrity of audio and video.

### 40. CVE-2026-103922｜ionic-team / capacitor
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T18:17:12.840)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T18:17:12.840 / 2026-10-01T19:17:18.760
- **官方描述（原文）**：Capacitor is a cross-platform native runtime for web applications. From 6.0.0 until 6.2.2, 7.6.9, 8.3.5, 8.4.3, and 8.5.1, the Android and iOS WebView navigation guard validates a target URL's host and scheme but not its path, allowing a victim who activates an untrusted link to navigate a frame to /_capacitor_http_interceptor_. The native proxy can fetch an attacker-selected URL and return the response as a document at the application's own origin, allowing script in that response to access same-origin storage, cookies, and registered Capacitor plugin capabilities. Applications remain affected when CapacitorHttp is disabled because affected releases serve the proxy path regardless of that setting. This issue is fixed in versions 6.2.2, 7.6.9, 8.3.5, 8.4.3, and 8.5.1.

### 41. CVE-2026-103764｜kvcache-ai / Mooncake
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T00:16:59.253)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T00:16:59.253 / 2026-10-02T00:16:59.253
- **官方描述（原文）**：Mooncake transfer engine before 0.3.13 contains an untrusted pointer dereference in ServerSession::readHeader that allows unauthenticated attackers to read and write arbitrary process memory via the TCP transport data port. Attackers can send a crafted SessionHeader with arbitrary addr and size values using READ or WRITE opcodes to disclose KV cache contents, prompts and secrets or corrupt memory toward code execution.

### 42. CVE-2026-103752｜Paul Ryan / Authorizer
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T15:17:29.270)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T15:17:29.270 / 2026-10-01T20:31:55.537
- **官方描述（原文）**：Unauthenticated Privilege Escalation in Authorizer <= 3.15.3 versions.

### 43. CVE-2026-103655｜MISP / MISP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T09:17:07.867)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T09:17:07.867 / 2026-10-01T16:17:37.487
- **官方描述（原文）**：MISP contains a vulnerability in its two-factor authentication (TOTP) verification process that permits a valid one-time code to be accepted more than once within its time-based validity window. The issue exists in the user login flow where a TOTP code is verified as a second authentication factor. Because the system did not record whether a given TOTP period had already been consumed, the same code remained valid for its entire time window (typically 30 seconds). An attacker who captures a legitimate code during a user's login could replay it to authenticate a second session as that user. Preconditions: - The target user has TOTP-based two-factor authentication enabled. - The attacker is in a position to observe or intercept the TOTP code during a legitimate login (e.g., network-level interception, shoulder surfing, or a compromised client). - The replay must occur within the TOTP validity period. Security impact: - Unauthorized account access by replaying a captured one-time code. - Potential compromise of threat-intelligence data and administrative functions accessible to the targeted user. Affected versions: <v2.5.48.

### 44. CVE-2026-103264｜fleetdm / fleet
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T11:17:21.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T11:17:21.410 / 2026-10-01T15:09:04.013
- **官方描述（原文）**：Fleet versions before 4.87.0 contain an authentication bypass vulnerability in the device API that accepts hostnames and hardware serials as authentication tokens in addition to device UUIDs. Unauthenticated attackers who know or guess these non-secret identifiers can authenticate as iOS/iPadOS hosts to read device data and trigger device-scoped actions including software installation and MDM migration.

### 45. CVE-2026-102667｜Joyland / Joyland.ai
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T20:17:21.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T20:17:21.750 / 2026-10-01T20:31:38.333
- **官方描述（原文）**：Joyland AI app allows an attacker with shared network access to inject JavaScript into content loaded in WebView. Without user-granted permissions, an attacker could access the clipboard, make arbitrary HTTP requests via the Weex 'stream' module, or access app-internal storage. If the installed app has been granted permissions previously, the attacker can access the entire file system, camera, microphone, and GPS tracking.

### 46. CVE-2026-102628｜Eummena / Cadmos LTI
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T20:17:21.447)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T20:17:21.447 / 2026-10-01T20:37:52.400
- **官方描述（原文）**：The Cadmos LTI application hosted at cadmos.eummena.io had Laravel debug mode enabled (APP_DEBUG=true, APP_ENV=local) in a publicly accessible environment. An unauthenticated attacker could send a GET request and trigger an unhandled exception, causing Laravel to expose the entire server environment, including all .env configuration variables, in plaintext. Fixed on or before 2026-09-02.

### 47. CVE-2025-41753｜WAGO / 0751-9x01
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T07:16:32.473)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T07:16:32.473 / 2026-10-01T20:17:20.530
- **官方描述（原文）**：The object name of a dynamically created BACnet File Object is interpreted as a file path without sufficient validation. Because relative paths are not limited to the intended directory, an unauthenticated remote attacker can traverse outside of it and read or overwrite arbitrary files on the device, which may lead to full system compromise.

### 48. CVE-2026-77387｜geopy / geopy
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T17:17:31.733)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.0 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T17:17:31.733 / 2026-10-01T18:17:27.723
- **官方描述（原文）**：geopy is a geocoding library for Python. Prior to 2.5.0, geopy.Point and Point.from_string() can spend excessive CPU time due to inefficient regular-expression behavior when an application passes a long malformed coordinate string without the 256-character input limit used by the fix. Geocoder reverse methods also reach the vulnerable parsing path when called with string inputs. Repeated attacker-controlled requests can cause a denial of service, while the numeric Point constructor is unaffected. This issue is fixed in version 2.5.0.

### 49. CVE-2026-104183｜uhop / stream-json
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T21:17:19.197)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T21:17:19.197 / 2026-10-01T21:17:19.197
- **官方描述（原文）**：stream-json is a micro-library of stream components for processing JSON and JSONC with a minimal memory footprint. Prior to 3.6.0, Assembler materializes object properties with plain assignment, so an input key named __proto__ invokes the inherited setter and causes parsed object prototype replacement instead of creating an own data property. Applications that make authorization or feature decisions from inherited values can therefore consume attacker-controlled properties, and a null prototype can disrupt code that expects Object.prototype methods. The researcher treats parsing untrusted JSON as part of the project contract, while the maintainer states that documented inputs are locally owned dumps, exports, or logs and characterizes the attack vector as local. The global Object.prototype is not polluted. This issue is fixed in version 3.6.0.

### 50. CVE-2026-103687｜rhukster / dom-sanitizer
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T15:17:29.073)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T15:17:29.073 / 2026-10-01T20:31:55.537
- **官方描述（原文）**：A vulnerability has been found in rhukster dom-sanitizer up to 1.0.15. The affected element is the function url of the file src/DOMSanitizer.php of the component SVG Sanitization. Such manipulation leads to incomplete blacklist. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. Upgrading to version 1.0.16 is sufficient to fix this issue. The name of the patch is 139c46c3d7c9bc81542b7b5a58d5cde5d0e0195a. Upgrading the affected component is recommended.

### 51. CVE-2026-103690｜itsourcecode / Leave Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T16:17:40.090)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T16:17:40.090 / 2026-10-01T20:31:55.537
- **官方描述（原文）**：A flaw has been found in itsourcecode Leave Management System 1.0. This vulnerability affects unknown code of the file /module/leave/controller.php. Executing a manipulation of the argument LEAVEID can lead to sql injection. The attack may be performed from remote. The exploit has been published and may be used.

### 52. CVE-2026-103544｜datadrivenconstruction / OpenConstructionERP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-01T07:16:33.900)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-01T07:16:33.900 / 2026-10-01T15:17:28.433
- **官方描述（原文）**：A vulnerability was found in datadrivenconstruction OpenConstructionERP up to 14.8.1. The impacted element is an unknown function of the file backend/app/modules/ai/ai_client.py of the component Al Provider Configuration Handler. Performing a manipulation results in exposure of data element to wrong session. The attack may be initiated remotely. The exploit has been made public and could be used. Upgrading to version 15.0.0 is sufficient to resolve this issue. It is suggested to upgrade the affected component.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-104286｜Fortinet / FortiMail
- **Title**：Fortinet FortiMail Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-01 / due_date=2026-10-04
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Fortinet FortiMail contains a path traversal and an improper neutralization of NULL byte or NULL character vulnerability that may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-56660 | P3 / 38 | GetSimpleCMS-CE / GetSimpleCMS-CE | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-103244 | P3 / 38 | sgoudelis / ground-station | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-73976 | WATCH / 30 | 4TUResearchData / djehuty | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-71542 | WATCH / 30 | GetSimpleCMS-CE / GetSimpleCMS-CE | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-71426 | WATCH / 30 | GetSimpleCMS-CE / GetSimpleCMS-CE | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-68496 | WATCH / 30 | FasterXML / jackson-dataformats-binary | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-68495 | WATCH / 30 | FasterXML / jackson-dataformats-binary | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-56661 | WATCH / 30 | GetSimpleCMS-CE / GetSimpleCMS-CE | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55231 | WATCH / 30 | givanz / Vvveb | v3.1 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55230 | WATCH / 30 | givanz / Vvveb | v3.1 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-103757 | WATCH / 30 | Budibase / budibase | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-103263 | WATCH / 30 | tornadoweb / tornado | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-96659 | WATCH / 28 | Red Hat / Red Hat Satellite 6.16 for RHEL 8 | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-96658 | WATCH / 28 | Red Hat / Red Hat Satellite 6.16 for RHEL 8 | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-94620 | WATCH / 28 | foundation50 / classroom50 | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-86345 | WATCH / 28 | Red Hat / Red Hat Directory Server 11 | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79901 | WATCH / 28 | Fortra / BoKS Manager boks-server | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-79898 | WATCH / 28 | Fortra / BoKS Manager | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-75957 | WATCH / 28 | superdav42 / Ultimate Multisite – WordPress Multisite SaaS & WaaS Platform | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-71449 | WATCH / 28 | Johnson Controls / EasyIO FS32 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-62071 | WATCH / 28 | nickboss / WordPress File Upload | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-59797 | WATCH / 28 | Apache Software Foundation / Apache HTTP Server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-57941 | WATCH / 28 | Apache Software Foundation / Apache HTTP Server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-56662 | WATCH / 28 | GetSimpleCMS-CE / GetSimpleCMS-CE | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-56154 | WATCH / 28 | Apache Software Foundation / Apache HTTP Server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-55395 | WATCH / 28 | Teledyne FLIR / Aware2 | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-55393 | WATCH / 28 | Teledyne FLIR / Aware2 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-55083 | WATCH / 28 | dhis2 / dhis2-core | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-53953 | WATCH / 28 | GetSimpleCMS-CE / GetSimpleCMS-CE | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：29。
- EPSS 未確認：30；Exploitation status 未確認：5。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-02T06:28:31.003209+00:00`；Delta generated at：`2026-10-02T06:28:31.003209+00:00`。

---

## 可驗證資料來源

- **CVE-2026-104286** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104286) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (fortiguard.fortinet.com)](https://fortiguard.fortinet.com/psirt/FG-IR-26-175) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-56660** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56660)
- **CVE-2026-103244** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103244)
- **CVE-2026-73976** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73976)
- **CVE-2026-71542** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71542)
- **CVE-2026-71426** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71426)
- **CVE-2026-68496** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-68496)
- **CVE-2026-68495** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-68495)
- **CVE-2026-56661** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56661)
- **CVE-2026-55231** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55231)
- **CVE-2026-55230** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55230)
- **CVE-2026-103757** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103757)
- **CVE-2026-103263** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103263)
- **CVE-2026-96659** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96659)
- **CVE-2026-96658** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96658)
- **CVE-2026-94620** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94620)
- **CVE-2026-86345** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86345)
- **CVE-2026-79901** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79901)
- **CVE-2026-79898** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79898)
- **CVE-2026-75957** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75957)
- **CVE-2026-71449** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71449)
- **CVE-2026-62071** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62071)
- **CVE-2026-59797** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59797)
- **CVE-2026-57941** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57941)
- **CVE-2026-56662** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56662)
- **CVE-2026-56154** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56154)
- **CVE-2026-55395** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55395)
- **CVE-2026-55393** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55393)
- **CVE-2026-55083** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55083)
- **CVE-2026-53953** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53953)
- **CVE-2026-19660** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19660)
- **CVE-2026-18397** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18397)
- **CVE-2026-15989** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15989)
- **CVE-2026-15896** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15896)
- **CVE-2026-14984** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14984)
- **CVE-2026-14378** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14378)
- **CVE-2026-13043** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13043)
- **CVE-2026-12627** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12627)
- **CVE-2026-104480** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104480)
- **CVE-2026-103922** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103922)
- **CVE-2026-103764** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103764)
- **CVE-2026-103752** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103752)
- **CVE-2026-103655** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103655)
- **CVE-2026-103264** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103264)
- **CVE-2026-102667** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102667)
- **CVE-2026-102628** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102628)
- **CVE-2025-41753** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-41753)
- **CVE-2026-77387** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77387)
- **CVE-2026-104183** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104183)
- **CVE-2026-103687** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103687)
- **CVE-2026-103690** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103690)
- **CVE-2026-103544** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103544)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
