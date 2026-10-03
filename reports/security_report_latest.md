# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**64** 筆符合目前門檻的重要變化；事件統計：EPSS_INCREASED=2、NEW_CVE=60、NEW_KEV=2。
- Intelligence 候選：**30** 筆；P1 **3**、P2 **0**、P3 **4**、WATCH **23**。
- Baseline：state / generated_at=2026-10-02T06:28:31.003209+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-102490、CVE-2026-102489、CVE-2026-87902。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **64** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-102490｜Zammad GmbH / Zammad
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-02 / due_date=2026-10-05
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-30T17:16:40.707 / 2026-10-03T04:18:00.460
- **官方描述（原文）**：Zammad GmbH Zammad contains an improper privilege management vulnerability that can allow the local zammad user to escalate privileges to root. This vulnerability can be chained with CVE-2026-102489.

### 2. CVE-2026-102489｜Zammad GmbH / Zammad
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-02 / due_date=2026-10-05
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-30T17:16:40.550 / 2026-10-03T04:17:56.693
- **官方描述（原文）**：Zammad GmbH Zammad contains a session fixation vulnerability that can lead to remote code execution as the zammad user. This vulnerability can be chained with CVE-2026-102490.

### 3. CVE-2026-87902｜WordPress / Core
- **Delta event**：EPSS_INCREASED (from=0.19756; to=0.45501)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.45501 / percentile=0.98756
- **CISA KEV**：listed=true / date_added=2026-09-25 / due_date=2026-09-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-22T17:17:28.310 / 2026-09-28T12:20:54.040
- **官方描述（原文）**：WordPress Core contains a remote file inclusion vulnerability which could allow an unauthenticated attacker to make page-template resolution include a chosen readable local `.php` file outside the active theme directories, leading to remote code execution.

### 4. CVE-2023-30804｜Sangfor / Next-Gen Application Firewall (NGAF)
- **Delta event**：EPSS_INCREASED (from=0.12816; to=0.33962)
- **Risk**：P3 / score 48；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.33962 / percentile=0.98354
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2023-10-10T15:15:10.033 / 2026-10-01T15:17:17.093
- **官方描述（原文）**：The Sangfor Next-Gen Application Firewall version NGAF8.0.17 is vulnerable to an authenticated file disclosure vulnerability. A remote and authenticated attacker can read arbitrary system files using the svpn_html/loadfile.php endpoint. This issue is exploitable by a remote and unauthenticated attacker when paired with CVE-2023-30803.

### 5. CVE-2026-104848｜tinylibs / tinypool
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T17:17:03.473)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T17:17:03.473 / 2026-10-02T18:33:20.487
- **官方描述（原文）**：Tinypool is a minimal Node.js worker thread pool implementation. Prior to 2.1.1, Tinypool constructs ThreadPool.options from a normal options object and reads the execArgv and env worker options in dist/index.js, allowing values inherited from a polluted Object.prototype to be copied into own properties and passed to worker_threads.Worker. An attacker who can first pollute either property can cause each newly spawned worker to load attacker-selected JavaScript through command-line preload arguments or NODE_OPTIONS, resulting in code execution with the host process's privileges and possible access to CI secrets, signing material, or build artifacts. This issue is fixed in version 2.1.1.

### 6. CVE-2026-104610｜Tenda / HG7
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T13:17:44.450)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T13:17:44.450 / 2026-10-02T14:17:09.267
- **官方描述（原文）**：A security vulnerability has been detected in Tenda HG7, HG9 and HG10 300001138_en_xpon. This impacts the function boaGetVar of the file /boaform/formLoopBack of the component Boa Web Server. Such manipulation of the argument Ethtype leads to stack-based buffer overflow. The attack can be executed remotely. The exploit has been disclosed publicly and may be used.

### 7. CVE-2026-104467｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:19.373)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:19.373 / 2026-10-02T16:16:46.357
- **官方描述（原文）**：YesWiki before 4.6.7 contains an authorization bypass vulnerability in ApiService::isAuthorized() that allows unauthenticated attackers to call admin-only API routes when public API mode is enabled. Attackers can send requests to endpoints like api/ci/update_config and api/archives to overwrite configuration and list, download, or delete backup archives.

### 8. CVE-2026-51907｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T16:16:50.320)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T16:16:50.320 / 2026-10-02T20:17:02.713
- **官方描述（原文）**：In TaskingAI v0.3.0 in the QR Code Generator plugin save_base64_image function, a path traversal vulnerability allows attackers to write image files to arbitrary locations on the server filesystem by manipulating the project_id parameter.

### 9. CVE-2026-104861｜nodeca / probe-image-size
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T18:17:02.430)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T18:17:02.430 / 2026-10-02T19:16:41.137
- **官方描述（原文）**：probe-image-size gets image dimensions without downloading the entire file. Prior to 7.4.0, lib/parse_sync/svg.js and lib/parse_stream/svg.js use the searching regular expression /<[-_.:a-zA-Z0-9][^>]*>/, which repeatedly scans to the end of input when attacker-controlled data contains many less-than characters without a closing greater-than character. The synchronous parser converts and scans the full supplied buffer without an input cap, while the streaming parser reparses the complete accumulated SVG prefix for every received chunk. The probe.sync(), probe(stream), and probe(url) entry points can therefore block the Node.js event loop at full CPU, and attacker-controlled chunking can amplify the streaming cost. This issue is fixed in version 7.4.0.

### 10. CVE-2026-104472｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:20.197)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:20.197 / 2026-10-02T15:17:08.533
- **官方描述（原文）**：YesWiki before 4.6.7 contains a missing authorization vulnerability in the attachment download handler that allows unauthenticated attackers to bypass page read ACLs. Attackers can request the download handler with a known page tag and file parameter to retrieve confidential attachments from read-restricted pages.

### 11. CVE-2026-104471｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:20.037)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:20.037 / 2026-10-02T14:17:09.137
- **官方描述（原文）**：YesWiki before 4.6.7 contains an unrestricted file upload vulnerability that allows authenticated admins to write remote files into the web-accessible files/ directory via Bazar CSV import preview. Attackers can import a CSV whose file or image field references a remote .php URL, which is saved without extension checks and executed as server-side code.

### 12. CVE-2026-104464｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:18.873)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:18.873 / 2026-10-02T15:17:08.170
- **官方描述（原文）**：YesWiki before 4.6.7 contains a server-side request forgery vulnerability that allows unauthenticated attackers to make server-side GET requests by supplying an unvalidated actor URL to the Bazar abonnements sync action. Attackers can target internal hosts or cloud metadata endpoints and chain attacker-controlled outbox first/next links, with fetched responses stored as readable Bazar entries.

### 13. CVE-2026-104463｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:18.643)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:18.643 / 2026-10-02T14:17:09.010
- **官方描述（原文）**：YesWiki before 4.6.7 contains a server-side request forgery vulnerability that allows unauthenticated attackers to trigger server requests by sending signed Follow activities to the public forms actor inbox route. Attackers sign requests with their own keyId while supplying internal actor URLs in the body, reaching internal hosts or cloud metadata via blind GET and POST requests.

### 14. CVE-2026-104462｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:18.467)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:18.467 / 2026-10-02T15:17:08.050
- **官方描述（原文）**：YesWiki before 4.6.7 contains an SQL injection vulnerability in the Bazar nuagetag action, which concatenates the unescaped tags attribute into a raw SQL IN clause. Attackers with page-write access (unauthenticated on default installs) can embed a nuagetag tag ending in a backslash to break quote parity and inject a UNION subquery, exfiltrating password hashes and arbitrary table data.

### 15. CVE-2026-104460｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:18.140)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:18.140 / 2026-10-02T15:17:07.930
- **官方描述（原文）**：YesWiki before 4.6.7 contains a blind SQL injection vulnerability in the {{newtextsearch}} action because Bazar list option ids are concatenated into SQL REGEXP/LIKE clauses in actions/newtextsearch.php without escaping. Anonymous attackers can plant a malicious option id in an anonymously editable Bazar list and use search requests as a boolean oracle to read arbitrary database data, including admin password hashes from the yeswiki_users table.

### 16. CVE-2026-104458｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:17.813)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:17.813 / 2026-10-02T15:17:07.810
- **官方描述（原文）**：YesWiki before 4.6.7 contains a server-side request forgery vulnerability in validateKeyIdUrl() that allows unauthenticated attackers to bypass the SSRF guard using 6to4, NAT64, or IPv4-compatible IPv6 addresses. Attackers can send a crafted Signature keyId to the public actor inbox route to reach cloud metadata, loopback services, or internal hosts.

### 17. CVE-2026-104456｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:17.490)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:17.490 / 2026-10-02T15:17:07.693
- **官方描述（原文）**：YesWiki before 4.6.7 contains a second-order SQL injection vulnerability in AclService::updateRequestWithACL, where a stored username is concatenated unescaped into a read-ACL LIKE clause. Attackers can self-register an account name containing a double-quote payload, then load non-admin ACL-filtered listings to read database contents and bypass read ACLs.

### 18. CVE-2026-104450｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:16.483)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:16.483 / 2026-10-02T15:17:07.310
- **官方描述（原文）**：YesWiki before 4.6.7 contains a missing authorization flaw in the pointimage action (tools/attach/actions/pointimage.php), which saves content to an attacker-chosen page with write ACL checks bypassed. Unauthenticated attackers can POST pagetag, title, and description fields to any page rendering {{pointimage}} to append raw HTML or JavaScript to any wiki page, including pages whose write ACL restricts editing, causing stored cross-site scripting in viewers' and administrators' browsers.

### 19. CVE-2026-104448｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:16.163)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:16.163 / 2026-10-02T15:17:07.150
- **官方描述（原文）**：YesWiki before 4.6.7 contains a cross-site request forgery vulnerability in the ajaxdeletepage handler, which permanently deletes a page on any GET request carrying a jsonp_callback parameter without checking a CSRF token. Attackers can lure a logged-in administrator or page owner to a crafted link to delete arbitrary pages along with their ACLs, links, triples, comments and referrers.

### 20. CVE-2026-104447｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:15.990)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:15.990 / 2026-10-02T14:17:08.343
- **官方描述（原文）**：YesWiki before 4.6.7 contains a cross-site request forgery vulnerability in the autoupdate UpdateAction that allows attackers to delete installed packages via unprotected GET requests. Attackers can lure a logged-in administrator to a crafted link with action=delete and a package parameter to remove extensions like bazar, breaking core site functionality.

### 21. CVE-2026-104443｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:15.323)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:15.323 / 2026-10-02T14:17:08.213
- **官方描述（原文）**：YesWiki before 4.6.7 contains an empty-filter scope bypass in the triples delete API that allows any authenticated user to delete or forge arbitrary semantic triples regardless of ownership. Attackers can send an empty filter to the triples delete endpoint to remove the admins-group membership triple, emptying the admin group and causing a site-wide authorization lockout.

### 22. CVE-2026-104439｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:14.670)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:14.670 / 2026-10-02T14:17:08.083
- **官方描述（原文）**：YesWiki before 4.6.7 contains a user enumeration vulnerability in LostPasswordAction.php that allows unauthenticated attackers to confirm registered email addresses through differing responses. Attackers can submit emails to the MotDePassePerdu recovery page without rate limiting to identify valid accounts for targeted phishing or password-spraying.

### 23. CVE-2026-104438｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:14.503)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:14.503 / 2026-10-02T16:16:46.120
- **官方描述（原文）**：YesWiki before 4.6.7 contains a missing authorization vulnerability in the listpagestag and includepages actions of the tags tool, which enumerate pages without applying read-ACL filtering. Unauthenticated or unprivileged attackers can embed these actions with a chosen tag or page name to disclose the names and body-derived titles of ACL-restricted pages.

### 24. CVE-2026-104410｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:10.520)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:10.520 / 2026-10-02T18:17:00.790
- **官方描述（原文）**：SiYuan before 3.8.5 contains an information disclosure vulnerability that allows publish readers to read password-protected and publish-disabled database rows via the /api/export/preview endpoint. Attackers can request an export preview of a public document embedding a database view to obtain protected rows' primary-key text and cell values.

### 25. CVE-2026-102626｜LimeSurvey / LimeSurvey
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T18:16:59.433)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T18:16:59.433 / 2026-10-02T19:16:39.097
- **官方描述（原文）**：An authenticated LimeSurvey Community Edition 7.4.0 user with the global Surveys: create permission can store a JavaScript-breaking value in the date_min attribute of a Date/Time question. When another user renders the affected question, LimeSurvey inserts the stored value into a single-quoted inline JavaScript literal without JavaScript-context encoding.

### 26. CVE-2026-97637｜parorrey / JSON API Auth
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T08:17:05.660)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00636 / percentile=0.48656
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T08:17:05.660 / 2026-10-02T13:18:55.613
- **官方描述（原文）**：The JSON API Auth plugin for WordPress is vulnerable to Authentication Bypass via Cached Session Cookie Disclosure in all versions up to, and including, 3.1.2. The vulnerability exists because the required PI-Media/json-api parent plugin caches controller dispatch results in transients keyed solely by URI and query string, ignoring HTTP method and POST body; this causes the `generate_auth_cookie()` endpoint — which embeds a live WordPress `logged_in` cookie produced by `wp_generate_auth_cookie()` directly in its JSON response body — to serve that cached authenticated response to any subsequent unauthenticated GET request to the same URI. This makes it possible for unauthenticated attackers to retrieve a valid Administrator `logged_in` session cookie from the cached response and use it to fully authenticate as the site Administrator, including via the same plugin's `get_currentuserinfo` endpoint and any cookie-authenticated controller action. Exploitation requires the PI-Media/json-api parent plugin to be installed and active with the Auth controller enabled, and a legitimate Administrator must have POSTed to `/api/auth/generate_auth_cookie/` within the preceding 24-hour cache TTL; the nominal HTTPS enforcement gate present in `Auth.php` is trivially bypassed by supplying `insecure=cool` as a request parameter.

### 27. CVE-2026-95102｜Monta / monta.app
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T22:16:56.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T22:16:56.607 / 2026-10-02T22:16:56.607
- **官方描述（原文）**：WebSocket endpoints lack proper authentication mechanisms, enabling attackers to impersonate charging stations. As a result, attackers can exploit this weakness to gain unauthorized access to sensitive data or perform unauthorized actions. Given that no authentication is required, this can lead to privilege escalation and potentially compromise the security of the entire system.

### 28. CVE-2026-94541｜amauric / WPMobile.App – Android and iOS App Builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T10:17:09.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00492 / percentile=0.40089
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T10:17:09.313 / 2026-10-02T18:17:07.870
- **官方描述（原文）**：The WPMobile.App – Android and iOS App Builder plugin for WordPress is vulnerable to authorization bypass in all versions up to, and including, 11.82 This is due to the plugin not properly verifying that a user is authorized to perform an action. This makes it possible for unauthenticated attackers to exfiltrate password-reset URLs for arbitrary users, including administrators, mirrored into the push queue by the mail-to-push feature, and use those URLs to take over the targeted accounts. This exploit chain requires the plugin's mail-to-push feature (wpmobile_auto_mail=1) to be enabled, as that setting is what causes outbound WordPress password-reset emails — including the reset URL and key — to be mirrored into the push row queue where they become accessible to the attacker.

### 29. CVE-2026-93698｜Webpros / cPanel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T07:16:39.027)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.9 (CRITICAL)
- **EPSS**：0.00464 / percentile=0.3794
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T07:16:39.027 / 2026-10-02T19:16:42.917
- **官方描述（原文）**：Insufficient validation allows arbitrary commands to be executed via the Multilang adminbin.

### 30. CVE-2026-93697｜Webpros / cPanel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T07:16:38.893)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.0 (CRITICAL)
- **EPSS**：0.00401 / percentile=0.32005
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T07:16:38.893 / 2026-10-02T19:16:42.790
- **官方描述（原文）**：There is a stored XSS vulnerability allowing arbitrary code execution in the WHM Mass Modify Accounts interface.

### 31. CVE-2026-93029｜Webpros / cPanel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T07:16:38.733)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.0 (CRITICAL)
- **EPSS**：0.00401 / percentile=0.32005
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T07:16:38.733 / 2026-10-02T18:47:49.947
- **官方描述（原文）**：There is a stored XSS vulnerability allowing arbitrary code execution in the WHM Manage SSL Hosts interface.

### 32. CVE-2026-91135｜Apache Software Foundation / Apache Thrift
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T11:17:37.277)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T11:17:37.277 / 2026-10-02T18:17:06.963
- **官方描述（原文）**：Heap-based buffer overflow vulnerability in Apache Thrift C++ THeaderTransport. When an application enables the ZLIB transform for the frames it sends, THeaderTransport::transform() copies the compressed frame into the write buffer without making sure it fits. Data that does not compress, such as content a remote peer supplied, grows under compression, so the copy writes past the end of the heap buffer by an amount that grows with the size of the frame, and for large frames it also reads past the end of the transform buffer. This issue affects Apache Thrift: before 0.25.0. Users are recommended to upgrade to version 0.25.0, which fixes the issue.

### 33. CVE-2026-90970｜GitLab / GitLab AI Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T15:17:12.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T15:17:12.550 / 2026-10-02T18:44:11.270
- **官方描述（原文）**：GitLab has remediated a vulnerability in the GitLab AI Gateway component affecting all versions of the AI Gateway from 18.1.6 before 19.2.4, 19.3 before 19.3.2, and 19.4 before 19.4.1 that, under certain conditions, could have allowed an authenticated user with Duo Agent Platform access to escape the prompt template sandbox via a specially crafted flow configuration, resulting in arbitrary command execution on the AI Gateway.

### 34. CVE-2026-86325｜Moxa / MGate MB3170 Series
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T11:17:36.173)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T11:17:36.173 / 2026-10-02T19:10:09.143
- **官方描述（原文）**：A stack-based buffer overflow vulnerability exists in protocol gateways' account management interface. The vulnerability is caused by insufficient length validation of the `account_name` parameter when processing account management requests. An attacker authenticated as a read-only user to the web management interface could supply a specially crafted account name that exceeds the size of the internal stack buffer, resulting in corruption of program execution flow. Successful exploitation could allow an attacker to read sensitive information from device memory, including credentials, modify arbitrary memory contents, and disrupt device availability.

### 35. CVE-2026-84411｜MikroTik / RouterOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T23:16:58.417)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T23:16:58.417 / 2026-10-02T23:16:58.417
- **官方描述（原文）**：The web management service in affected RouterOS versions contains an integer underflow in its HTTP request body handling that is reachable before authentication. This can be leveraged by an unauthenticated network attacker to achieve arbitrary code execution as root, or to cause a denial of service, using a single crafted request.

### 36. CVE-2026-83632｜Apache Software Foundation / Apache Thrift
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T13:17:58.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T13:17:58.647 / 2026-10-02T17:17:07.603
- **官方描述（原文）**：Allocation of resources without limits or throttling, Integer overflow or wraparound, Heap-based buffer overflow vulnerability in Apache Thrift. This issue affects Apache Thrift: before 0.25.0. Users are recommended to upgrade to version 0.25.0, which fixes the issue.

### 37. CVE-2026-82042｜UTMStack / UTMStack
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T21:16:56.643)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T21:16:56.643 / 2026-10-02T21:16:56.643
- **官方描述（原文）**：UTMStack before 11.2.16 contains an authentication bypass vulnerability that allows remote attackers to gain full administrative API access by presenting a valid Utm-Internal-Key header matching the INTERNAL_KEY environment variable value, which the InternalApiKeyFilter accepts for any endpoint without path restriction, constant-time comparison, rate limiting, or audit logging. Attackers who obtain the key value can authenticate without a user account or JWT to create accounts, manage users, exfiltrate data, and modify security rules.

### 38. CVE-2026-75937｜Digi International / IX Family
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T21:16:56.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T21:16:56.337 / 2026-10-02T21:16:56.337
- **官方描述（原文）**：A specially crafted HTTP POST request to the web administration interface allows an unauthenticated attacker to execute arbitrary operating system commands with root privileges on the affected device. Disable the web server when not configuring the device.

### 39. CVE-2026-63569｜Legion of the Bouncy Castle Inc. / bc-csharp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T07:16:37.430)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00396 / percentile=0.31424
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T07:16:37.430 / 2026-10-02T19:16:41.913
- **官方描述（原文）**：Improper input validation in DHAgreement.CalculateAgreement (MTI/A0 two-pass Diffie-Hellman) in Legion of the Bouncy Castle Inc. bc-csharp before 2.7.0 allows an on-path attacker to make the local party compute an agreed value the attacker already knows, defeating the key authentication MTI/A0 is meant to provide. It also allows a malicious peer to learn the local static private key modulo the small factors of p-1, and to recover it entirely in groups with many such factors. The attack uses a crafted out-of-range or small-order ephemeral value, and works because that value is raised to the static private key without the range and subgroup-membership checks applied to DH public keys. Only applications that call DHAgreement directly are affected.

### 40. CVE-2026-19652｜DiviEngine / Divi Membership
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T14:17:10.483)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T14:17:10.483 / 2026-10-02T17:52:32.600
- **官方描述（原文）**：The Divi Membership plugin for WordPress is vulnerable to Privilege Escalation in versions up to, and including, 2.2.0. This is due to the `dmem_form_submit_handler()` function determining the new user's role by iterating all WordPress roles and calling `password_verify()` against an attacker-controlled bcrypt hash supplied in the `form_id` POST parameter, with no validation or whitelist of allowed roles. This makes it possible for unauthenticated attackers to register a new account with the administrator role by submitting a locally computed bcrypt hash of `administrator` as `form_id`, and when `auto_login=on` is submitted, be immediately authenticated as that administrator in the same request, resulting in full site takeover. Exploitation requires a WordPress nonce, but that nonce is publicly emitted on any page rendering the Divi Membership registration form and is therefore obtainable by any unauthenticated visitor.

### 41. CVE-2026-105080｜C4illin / ConvertX
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-03T01:17:23.650)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-03T01:17:23.650 / 2026-10-03T01:17:23.650
- **官方描述（原文）**：In ConvertX before 0.19.0, converters/calibre.ts does not block recipe files, and instead passes them to the ebook-convert program from Calibre. This affects executable code in a .recipe or .downloaded_recipe file.

### 42. CVE-2026-104849｜tinylibs / tinypool
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T17:17:03.623)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T17:17:03.623 / 2026-10-02T18:33:20.487
- **官方描述（原文）**：Tinypool is a minimal Node.js worker thread pool implementation. Prior to 2.1.2, Tinypool reads filename from a caller-supplied options object in pool.run(task, options) without requiring an own property, so a polluted Object.prototype.filename can replace the intended worker module. Applications are affected only when they pass their own second-argument options object to pool.run(); calls without that argument use the trusted default options object. An attacker who can first pollute the prototype can cause the worker pool to load attacker-selected JavaScript and can read or modify task data with the host process's privileges. This issue is fixed in version 2.1.2.

### 43. CVE-2026-104846｜lxsmnsyc / seroval
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T16:16:47.230)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T16:16:47.230 / 2026-10-02T16:16:47.363
- **官方描述（原文）**：Seroval facilitates JS value stringification, including complex structures beyond JSON.stringify capabilities. From 0.12.0 until 1.6.2, fromJSON deserialization of a fulfilled Promise control node can pass a plugin-produced callable-bearing thenable to a native Promise resolver. ECMAScript thenable assimilation then invokes the callable unexpectedly, allowing attacker-controlled JSON to trigger code in applications using plugin-capable Seroval releases. This path bypasses the Promise resolver type-confusion remediation in version 1.5.3 for CVE-2026-59940 because the unexpected invocation occurs through native Promise settlement after the referenced value is deserialized. This issue is fixed in version 1.6.2.

### 44. CVE-2026-104019｜AWS / sagemaker-distribution
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T20:17:00.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T20:17:00.607 / 2026-10-02T21:16:54.477
- **官方描述（原文）**：OS command injection in the Studio Space startup validation script in Amazon SageMaker Distribution 2.x before 2.14.12, 3.x before 3.9.12, 4.0.x before 4.0.11, 4.1.x before 4.1.11, 4.2.x before 4.2.8, 4.3.x before 4.3.5, and 4.4.x before 4.4.3, as used by Amazon SageMaker Unified Studio, might allow an authenticated remote user with project contributor permissions to execute arbitrary commands in another project member's Studio Space and obtain that member's temporary execution role credentials via a crafted connection resource property that is interpolated into a shell invocation without neutralization. To remediate this issue, users should upgrade to version 2.14.12, 3.9.12, 4.0.11, 4.1.11, 4.2.8, 4.3.5, or 4.4.3, as applicable to the minor line in use. Users on minor lines that have reached end of support must move to a supported minor line, because no patched version will be released for those lines. In Amazon SageMaker Unified Studio, Studio Spaces adopt the latest patch of their minor line on restart once the patched images are deployed, so no version selection is required.

### 45. CVE-2026-103956｜AWS / loom
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T19:16:39.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T19:16:39.750 / 2026-10-02T22:16:53.973
- **官方描述（原文）**：Missing authentication for critical function in the authentication dependency in Loom for AWS before 1.6.1 allowed remote actors to obtain super-admin authority over the agent control plane, including registering tool servers, reading stored integration credentials, and rewriting the IAM role policies attached to managed agent roles, via any request to the application API in a deployment where no identity provider is configured. To remediate this issue, users should upgrade to version 1.6.1 or later.

### 46. CVE-2026-103648｜demsking / image-downloader
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T16:16:44.370)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T16:16:44.370 / 2026-10-02T18:44:11.270
- **官方描述（原文）**：Path traversal in image-downloader 4.3.0 allows an attacker who can control the download URL to cause downloaded response data to be written outside the configured destination directory.

### 47. CVE-2026-103628｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T16:16:43.937)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T16:16:43.937 / 2026-10-03T04:18:01.260
- **官方描述（原文）**：Out of bounds write in WebGL in Google Chrome prior to 154.0.8037.97 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 48. CVE-2023-54405｜H3C / CVM
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T19:16:38.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T19:16:38.897 / 2026-10-02T19:16:38.897
- **官方描述（原文）**：H3C CVM, the Cloud Virtualization Management component of the H3C CAS cloud platform, contains an unauthenticated arbitrary file upload vulnerability in the /cas/fileUpload/upload endpoint that allows remote attackers to write arbitrary files by manipulating the caller-supplied token parameter without restricting path traversal or file type. Attackers can exploit the path traversal in the token parameter to upload a malicious JSP file into a web-accessible directory and then request it to achieve remote code execution as the web-server user. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 49. CVE-2026-51899｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T16:16:49.867)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T16:16:49.867 / 2026-10-02T21:16:55.260
- **官方描述（原文）**：In SuperAGI v0.0.14 and prior, controller endpoints (/api/agents/create, /api/agents/schedule, /api/agents/delete, /api/agents/edit_schedule, /api/agents/stop_schedule) allow authenticated users from one organization to create, schedule, edit, stop, and delete agents belonging to a different organization's project. The endpoints accept a project_id parameter but do not verify that the project belongs to the authenticated user's organization.

### 50. CVE-2026-104638｜onetwothreeneth / HospitalManagementSystem
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T15:17:09.030)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T15:17:09.030 / 2026-10-02T17:52:32.600
- **官方描述（原文）**：A security vulnerability has been detected in onetwothreeneth HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61d. The impacted element is an unknown function of the file php/sessions.php. The manipulation of the argument ID leads to improper authentication. Remote exploitation of the attack is possible. The exploit has been disclosed publicly and may be used. This product follows a rolling release approach for continuous delivery, so version details for affected or updated releases are not provided. The project was informed of the problem early through an issue report but has not responded yet.

### 51. CVE-2026-104470｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:19.870)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:19.870 / 2026-10-02T16:16:46.473
- **官方描述（原文）**：YesWiki before 4.6.7 contains a server-side request forgery vulnerability in the Bazar valeur action that allows page editors to make the server fetch arbitrary URLs. Attackers can supply loopback or internal URLs in the url parameter to probe internal services and inject unescaped remote HTML that executes scripts in viewers' browsers.

### 52. CVE-2026-104468｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:19.540)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:19.540 / 2026-10-02T15:17:08.410
- **官方描述（原文）**：YesWiki before 4.6.7 contains an insufficient session expiration vulnerability that allows attackers to reuse old password reset links because tokens lack expiry timestamps. Attackers who obtain an unused reset URL from mailboxes, logs, backups, or browser history can submit a new password through checkEmailKey() and take over accounts.

### 53. CVE-2026-104466｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:19.217)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:19.217 / 2026-10-02T15:17:08.287
- **官方描述（原文）**：YesWiki before 4.6.7 contains a stored cross-site scripting vulnerability in formatters/wakka.php that allows users who can edit pages or post comments to inject event handlers by placing quotes in markdown image URLs. Attackers can store a crafted markdown image whose src breaks out of the attribute to add an onerror handler, executing JavaScript in viewers' browsers, including administrators.

### 54. CVE-2026-104459｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:17.973)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:17.973 / 2026-10-02T14:17:08.793
- **官方描述（原文）**：YesWiki before 4.6.7 contains a server-side request forgery vulnerability in WebfingerService that allows unauthenticated attackers to trigger HTTPS requests to internal hosts. Attackers can POST a crafted actor_handle with a numeric host and port to the abonnements view to probe internal HTTPS services and ports.

### 55. CVE-2026-104455｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:17.323)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:17.323 / 2026-10-02T14:17:08.610
- **官方描述（原文）**：YesWiki before 4.6.7 contains an access control bypass vulnerability that allows unauthenticated attackers to read restricted page content via the recentchangesrssplus RSS action. Attackers can request the xml method of a page hosting the action to retrieve 500-character body excerpts of every latest page, including read-restricted drafts and notes.

### 56. CVE-2026-104454｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:17.160)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:17.160 / 2026-10-02T15:17:07.570
- **官方描述（原文）**：YesWiki before 4.6.7 contains an algorithmic-complexity denial of service in the wakka.php formatter due to an O(n^2) markdown-link regex. Unauthenticated attackers can submit a small crafted body of bracket characters to the page-edit preview endpoint to pin PHP-FPM workers and saturate the pool.

### 57. CVE-2026-104451｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:16.673)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:16.673 / 2026-10-02T14:17:08.480
- **官方描述（原文）**：YesWiki before 4.6.7 contains a cross-site request forgery vulnerability in RevisionsHandler that allows attackers to restore old page revisions through GET requests lacking CSRF token validation. Attackers can lure write-capable users into a top-level navigation with the restoreRevisionId parameter, silently overwriting current page content with stale or vandalized revisions.

### 58. CVE-2026-104446｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:15.817)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:15.817 / 2026-10-02T15:17:07.013
- **官方描述（原文）**：YesWiki before 4.6.7 contains an authentication bypass in the contact mail AJAX handler that allows unauthenticated attackers to send email through the wiki's SMTP server. Attackers can POST an XMLHttpRequest to the mail handler without field or type parameters, supplying arbitrary recipient, sender, subject and body for spam and phishing.

### 59. CVE-2026-104442｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:15.153)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:15.153 / 2026-10-02T16:16:46.237
- **官方描述（原文）**：YesWiki before 4.6.7 contains an unauthenticated server-side request forgery vulnerability that allows remote attackers to make the server fetch arbitrary URLs by supplying a syndication action through the render handler's content parameter. Attackers can target internal hosts and ports, read back fetched feed content in the rendered page, and cause feed enclosures to be downloaded into the files directory.

### 60. CVE-2026-104440｜YesWiki / yeswiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:14.837)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:14.837 / 2026-10-02T15:17:06.893
- **官方描述（原文）**：YesWiki before 4.6.7 contains a blind server-side request forgery vulnerability that allows unauthenticated attackers to make arbitrary server-side requests via the idtypeannonce parameter of /api/entries/bazarlist. Because isValidURL() always returns true, attackers can supply internal URLs fetched by curl in loadURLContent() to probe internal networks and reach internal services or metadata endpoints.

### 61. CVE-2026-103763｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T12:17:10.277)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T12:17:10.277 / 2026-10-02T16:16:44.620
- **官方描述（原文）**：SiYuan before v3.8.5 contains an information disclosure vulnerability that allows read-only publish readers to learn metadata of publish-excluded documents through the getNotebookInfo endpoint. Attackers, including anonymous visitors when no reader password is set, can query publish-visible notebooks to obtain document count, size and modification timestamps of hidden documents.

### 62. CVE-2026-104614｜CodeAstro / Simple Pharmacy Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T14:17:09.990)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T14:17:09.990 / 2026-10-02T17:52:32.600
- **官方描述（原文）**：A vulnerability was identified in CodeAstro Simple Pharmacy Management System 1.0. This issue affects some unknown processing of the file /SimplePharmacy-PHP/product/delete.php. Such manipulation of the argument ID leads to sql injection. The attack can be launched remotely. The exploit is publicly available and might be used.

### 63. CVE-2026-104613｜CodeAstro / Simple Pharmacy Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T14:17:09.807)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T14:17:09.807 / 2026-10-02T17:52:32.600
- **官方描述（原文）**：A vulnerability was determined in CodeAstro Simple Pharmacy Management System 1.0. This vulnerability affects unknown code of the file /SimplePharmacy-PHP/product/view.php. This manipulation of the argument ID causes sql injection. The attack can be initiated remotely. The exploit has been publicly disclosed and may be utilized.

### 64. CVE-2026-104606｜itsourcecode / Online Admission System Project
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-02T11:17:26.037)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-02T11:17:26.037 / 2026-10-02T18:17:01.430
- **官方描述（原文）**：A security flaw has been discovered in itsourcecode Online Admission System Project 1.0. The impacted element is an unknown function of the file confirm.php. The manipulation of the argument ID results in sql injection. The attack may be launched remotely. The exploit has been released to the public and may be used for attacks.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-102490｜Zammad GmbH / Zammad
- **Title**：Zammad GmbH Zammad Improper Privilege Management Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-02 / due_date=2026-10-05
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Zammad GmbH Zammad contains an improper privilege management vulnerability that can allow the local zammad user to escalate privileges to root. This vulnerability can be chained with CVE-2026-102489.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-102489｜Zammad GmbH / Zammad
- **Title**：Zammad GmbH Zammad Session Fixation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-02 / due_date=2026-10-05
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Zammad GmbH Zammad contains a session fixation vulnerability that can lead to remote code execution as the zammad user. This vulnerability can be chained with CVE-2026-102490.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-87902｜WordPress / Core
- **Title**：WordPress Core Remote File Inclusion Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.45501 / percentile=0.98756
- **CISA KEV**：listed=true / date_added=2026-09-25 / due_date=2026-09-28
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WordPress Core contains a remote file inclusion vulnerability which could allow an unauthenticated attacker to make page-template resolution include a chosen readable local `.php` file outside the active theme directories, leading to remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2023-30804 | P3 / 48 | Sangfor / Next-Gen Application Firewall (NGAF) | v4.0 6.9 (MEDIUM) | 0.33962 / percentile=0.98354 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104848 | P3 / 38 | tinylibs / tinypool | v4.0 9.5 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104610 | P3 / 38 | Tenda / HG7 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104467 | P3 / 38 | YesWiki / yeswiki | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-51907 | WATCH / 30 | 未確認 / 未確認 | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104861 | WATCH / 30 | nodeca / probe-image-size | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104472 | WATCH / 30 | YesWiki / yeswiki | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104471 | WATCH / 30 | YesWiki / yeswiki | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104464 | WATCH / 30 | YesWiki / yeswiki | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104463 | WATCH / 30 | YesWiki / yeswiki | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104462 | WATCH / 30 | YesWiki / yeswiki | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104460 | WATCH / 30 | YesWiki / yeswiki | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104458 | WATCH / 30 | YesWiki / yeswiki | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104456 | WATCH / 30 | YesWiki / yeswiki | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104450 | WATCH / 30 | YesWiki / yeswiki | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104448 | WATCH / 30 | YesWiki / yeswiki | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104447 | WATCH / 30 | YesWiki / yeswiki | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104443 | WATCH / 30 | YesWiki / yeswiki | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104439 | WATCH / 30 | YesWiki / yeswiki | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104438 | WATCH / 30 | YesWiki / yeswiki | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104410 | WATCH / 30 | siyuan-note / siyuan | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102626 | WATCH / 30 | LimeSurvey / LimeSurvey | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97637 | WATCH / 28 | parorrey / JSON API Auth | v3.1 9.8 (CRITICAL) | 0.00636 / percentile=0.48656 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-95102 | WATCH / 28 | Monta / monta.app | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94541 | WATCH / 28 | amauric / WPMobile.App – Android and iOS App Builder | v3.1 9.8 (CRITICAL) | 0.00492 / percentile=0.40089 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93698 | WATCH / 28 | Webpros / cPanel | v3.0 9.9 (CRITICAL) | 0.00464 / percentile=0.3794 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93697 | WATCH / 28 | Webpros / cPanel | v3.0 9.0 (CRITICAL) | 0.00401 / percentile=0.32005 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：1；缺少 Product：1；缺少 Title：27。
- EPSS 未確認：24；Exploitation status 未確認：2。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-03T05:54:47.637906+00:00`；Delta generated at：`2026-10-03T05:54:47.637906+00:00`。

---

## 可驗證資料來源

- **CVE-2026-102490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102490) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (zammad.com)](https://zammad.com/en/product/releases/) · [Vendor / Advisory (community.zammad.org)](https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297/2) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-102489** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102489) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (zammad.com)](https://zammad.com/en/product/releases/) · [Vendor / Advisory (community.zammad.org)](https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297/2) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87902** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87902) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87902) · [Vendor / Advisory (github.com)](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2023-30804** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-30804) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-30804)
- **CVE-2026-104848** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104848)
- **CVE-2026-104610** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104610)
- **CVE-2026-104467** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104467)
- **CVE-2026-51907** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-51907)
- **CVE-2026-104861** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104861)
- **CVE-2026-104472** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104472)
- **CVE-2026-104471** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104471)
- **CVE-2026-104464** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104464)
- **CVE-2026-104463** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104463)
- **CVE-2026-104462** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104462)
- **CVE-2026-104460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104460)
- **CVE-2026-104458** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104458)
- **CVE-2026-104456** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104456)
- **CVE-2026-104450** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104450)
- **CVE-2026-104448** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104448)
- **CVE-2026-104447** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104447)
- **CVE-2026-104443** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104443)
- **CVE-2026-104439** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104439)
- **CVE-2026-104438** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104438)
- **CVE-2026-104410** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104410)
- **CVE-2026-102626** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102626)
- **CVE-2026-97637** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97637) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97637)
- **CVE-2026-95102** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95102)
- **CVE-2026-94541** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94541) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-94541)
- **CVE-2026-93698** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93698) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93698)
- **CVE-2026-93697** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93697) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93697)
- **CVE-2026-93029** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93029) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93029)
- **CVE-2026-91135** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91135)
- **CVE-2026-90970** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90970)
- **CVE-2026-86325** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86325)
- **CVE-2026-84411** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84411)
- **CVE-2026-83632** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83632)
- **CVE-2026-82042** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82042)
- **CVE-2026-75937** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75937)
- **CVE-2026-63569** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63569) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63569)
- **CVE-2026-19652** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19652)
- **CVE-2026-105080** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105080)
- **CVE-2026-104849** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104849)
- **CVE-2026-104846** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104846)
- **CVE-2026-104019** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104019)
- **CVE-2026-103956** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103956)
- **CVE-2026-103648** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103648)
- **CVE-2026-103628** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103628)
- **CVE-2023-54405** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-54405)
- **CVE-2026-51899** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-51899)
- **CVE-2026-104638** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104638)
- **CVE-2026-104470** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104470)
- **CVE-2026-104468** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104468)
- **CVE-2026-104466** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104466)
- **CVE-2026-104459** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104459)
- **CVE-2026-104455** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104455)
- **CVE-2026-104454** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104454)
- **CVE-2026-104451** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104451)
- **CVE-2026-104446** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104446)
- **CVE-2026-104442** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104442)
- **CVE-2026-104440** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104440)
- **CVE-2026-103763** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103763)
- **CVE-2026-104614** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104614)
- **CVE-2026-104613** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104613)
- **CVE-2026-104606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104606)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
