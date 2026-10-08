# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**68** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=5、NEW_CVE=63。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **4**、WATCH **26**。
- Baseline：state / generated_at=2026-10-07T06:42:35.310142+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **68** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-62252｜sipcapture / homer
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:16:56.467)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:16:56.467 / 2026-10-07T18:17:21.033
- **官方描述（原文）**：Homer is open source telecom observability software. Prior to version 11.0.283, on every fresh Homer deployment using internal authentication, the bootstrap process automatically creates an `admin` account with the password `sipcapture` (stored as a legacy SHA-256 hex hash). There is no first-login forced-change mechanism. Any attacker who reaches the login endpoint immediately gains full administrative access. Version 11.0.283 patches the issue.

### 2. CVE-2026-62176｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:16:56.007)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:16:56.007 / 2026-10-07T17:16:56.153
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to version 4.6.78, the `deploy/api.py` module generates Python server code by directly interpolating the `agents_file` parameter into an f-string that is then written to a file and executed via `subprocess.Popen()`. An attacker who controls the `agents_file` value (via CLI argument, configuration, or upstream API) can inject arbitrary Python code. Version 4.6.78 patches the issue.

### 3. CVE-2026-107204｜LMCache / LMCache
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T16:17:45.113)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T16:17:45.113 / 2026-10-07T17:16:53.657
- **官方描述（原文）**：LMCache through 0.5.5 contains an unauthenticated remote code execution vulnerability that allows remote attackers to execute Python code by posting scripts to the /run_script endpoint. Attackers can recover real builtins through the injected FastAPI app object, bypassing the guarded __import__, to import os and run operating system commands as the LMCache process.

### 4. CVE-2025-70518｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T15:16:53.183)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T15:16:53.183 / 2026-10-07T17:16:44.960
- **官方描述（原文）**：The management portal's diagnostic ping tool of Fanvil x7a firmware version 2.6.0.1182 does not handle user supplied input securely. The lack of secure user input handling allows any unauthenticated attacker to inject commands and run code in the underlying Android operating system.

### 5. CVE-2026-46434｜wger-project / wger
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T14:17:10.277)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T14:17:10.277 / 2026-10-07T15:17:20.877
- **官方描述（原文）**：wger is a free, open-source workout and fitness manager. Prior to version 2.6, a user with only the `gym_trainer` permission can deactivate any account in the same gym, including `gym_manager` and `general_gym_manager` accounts. The `UserDeactivateView` grants access to anyone holding any one of `gym.manage_gym`, `gym.manage_gyms`, or `gym.gym_trainer` (OR logic via `WgerMultiplePermissionRequiredMixin`), and performs no privilege-hierarchy check to prevent a lower-privileged role from disabling a higher-privileged one. Version 2.6 fixes the issue.

### 6. CVE-2026-43976｜wger-project / wger
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T14:17:09.887)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T14:17:09.887 / 2026-10-07T18:17:20.770
- **官方描述（原文）**：wger is a free, open-source workout and fitness manager. Prior to version 2.6, five gym management views in wger apply a flawed gym-scope guard (`gym_a != gym_b`) that silently passes when both operands are `None`. A trainer with `gym.gym_trainer` and `gym.add_adminusernote` permissions and no gym assignment (`gym=None`) can read private admin notes, uploaded documents, gym contracts, user configuration, and user permission data for **any other unaffiliated user** on the instance. The subsequent querysets filter only on the attacker-supplied `member_id` with no secondary gym-scoped validation, so all records are disclosed. Version 2.6 fixes the issue.

### 7. CVE-2026-107270｜gophish / gophish
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T16:17:46.490)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T16:17:46.490 / 2026-10-07T17:16:54.063
- **官方描述（原文）**：Gophish through 0.12.1 contains an insecure direct object reference vulnerability that allows authenticated users to take over other users' groups, templates, landing pages and sending profiles. Attackers can supply another user's sequential id in POST requests to /api/groups/, /api/templates/, /api/pages/ or /api/smtp/ to overwrite and reassign objects, locking out owners and exposing victims' recipient lists.

### 8. CVE-2026-107214｜qax-os / excelize
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T18:17:19.040)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T18:17:19.040 / 2026-10-07T20:17:11.320
- **官方描述（原文）**：Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.3.1 to 2.11.0, the decryption dispatch performs insufficient structural and parameter validation before standard and agile decryptors slice, index, allocate, and divide using attacker-controlled values. Decrypt passes attacker-controlled EncryptionInfo and EncryptedPackage data into standardDecrypt or agileDecrypt before validating the structures used by those routines. When a malformed OLE compound file with a version-valid EncryptionInfo stream is opened or passed to Decrypt, nine malformed-input classes reach unrecovered Go runtime panics instead of the documented error path, allowing an attacker to terminate the calling process. No fixed version is available as of this review.

### 9. CVE-2026-107212｜qax-os / excelize
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T18:17:18.670)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T18:17:18.670 / 2026-10-07T18:17:18.670
- **官方描述（原文）**：Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.1.0 to 2.11.0, Rows.Columns accepts a look-ahead row number above TotalRows without applying the limit enforced by Rows.Next. File.GetRows relies on Rows.Next and Rows.Columns, but Rows.Columns consumes the row r attribute without the limit check in Rows.Next. When a crafted worksheet places an oversized row number after an ordinary valid row and the application calls GetRows or iterates Rows, the iterator advances through every missing row number instead of rejecting the workbook, allowing an attacker to consume a CPU core for an attacker-controlled duration. No fixed version is available as of this review.

### 10. CVE-2026-107206｜LMCache / LMCache
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T16:17:45.447)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T16:17:45.447 / 2026-10-07T17:16:53.927
- **官方描述（原文）**：LMCache through 0.5.5 contains a missing authentication vulnerability in the multiprocess mode HTTP server that allows remote unauthenticated attackers to access management endpoints listening on all interfaces by default. Attackers can read environment credentials via GET /env and configuration via GET /config, clear caches, delete cache objects, and modify tenant quotas to evict other tenants' cached data.

### 11. CVE-2026-107181｜Telegram / Telegram Desktop
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T14:17:08.807)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T14:17:08.807 / 2026-10-07T17:16:53.520
- **官方描述（原文）**：Telegram Desktop before 7.2.9 contains an IPC record-separator injection vulnerability in Core::Sandbox that allows remote attackers to inject OPEN: records via crafted tg:// links containing unescaped semicolons. Attackers can reach the interpret: scheme handler to upload local files, including tdata session keys, to an attacker channel, enabling account takeover.

### 12. CVE-2026-107177｜ExpressGateway / express-gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T13:17:20.827)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T13:17:20.827 / 2026-10-07T18:17:18.150
- **官方描述（原文）**：Express Gateway through 1.16.11 contains a hardcoded cryptographic key vulnerability that allows attackers with datastore access to decrypt stored OAuth 2.0 token secrets via the default crypto.cipherKey 'sensitiveKey'. Attackers who can read Redis can decrypt tokenEncrypted values and combine them with stored token IDs to obtain valid bearer tokens for any user.

### 13. CVE-2026-106058｜gitahead / gitahead
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T12:17:08.920)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T12:17:08.920 / 2026-10-07T21:17:12.053
- **官方描述（原文）**：GitAhead through 2.7.1 contains an OS command injection vulnerability in src/git/Filter.cpp that allows malicious repositories to execute commands by substituting crafted filenames into clean/smudge filter commands. Attackers can ship files named with $(command) selected via .gitattributes so checkout or staging runs the command through bash -c as the victim.

### 14. CVE-2026-97720｜Apache Software Foundation / Apache Impala
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T09:17:06.333)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00196 / percentile=0.08526
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T09:17:06.333 / 2026-10-07T19:17:45.470
- **官方描述（原文）**：Incorrect implementation of JWT/OAuth authentication in Impala executors in Apache Impala versions up to and including 4.5.2 which allows attacked to access resources served by the executor's webserver when that webserver is configured to accept JWT/OAuth tokens. Bearer token (JWT) signatures are not validated resulting in the webserver accepting any valid JWT. Users are recommended to either disable JWT/OAuth auth for Impala executors or upgrade to version 4.5.3, which fixes this issue.

### 15. CVE-2026-96408｜Six Apart Ltd. / Movable Type Cloud Edition
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T11:17:20.620)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T11:17:20.620 / 2026-10-07T18:17:32.210
- **官方描述（原文）**：A code injection vulnerability exists in the upgrade script of Movable Type, which may allow an unauthenticated attacker to execute an arbitrary Perl script or an SQL query on the affected product.

### 16. CVE-2026-95606｜Liquid Web / StellarWP / The Events Calendar
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:04.213)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:04.213 / 2026-10-07T18:17:31.910
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Liquid Web / StellarWP The Events Calendar allows Object Injection. This issue affects The Events Calendar: from n/a through 6.17.4.

### 17. CVE-2026-95605｜Passionate Programmer Peter / WP Data Access
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:04.063)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:04.063 / 2026-10-07T19:17:45.353
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Passionate Programmer Peter WP Data Access allows Blind SQL Injection. This issue affects WP Data Access: from n/a through 5.5.82.

### 18. CVE-2026-92414｜Apache Software Foundation / Apache Jackrabbit
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T16:19:12.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T16:19:12.900 / 2026-10-07T21:17:21.360
- **官方描述（原文）**：: Session Fixation / Session Reuse across Users vulnerability in Apache Jackrabbit. Jackrabbit WebDAV server attaches a cached authenticated session on any Lock-Token/TransactionId/SubscriptionId/If-header field token match with no credential check. This issue affects Apache Jackrabbit: from 2.23.0 through 2.23.5, from 2.22.0 through 2.22.4, from 2.20.0 through 2.20.17. Users are recommended to upgrade to versions 2.23.6, 2.22.5, or 2.20.18 which fix the issue.

### 19. CVE-2026-76501｜Cisco / Cisco NX-OS Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:02.113)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:02.113 / 2026-10-08T04:17:35.760
- **官方描述（原文）**：A vulnerability in the Segment Routing over IPv6 (SRv6) Operation, Administration, and Maintenance (OAM) feature of Cisco NX-OS Software, known as NGOAM, could allow an unauthenticated, remote attacker to execute arbitrary code with root privileges or cause a denial of service (DoS) on an affected device. This vulnerability is due to improper input validation of IP traffic when the NGOAM and SRv6 features are enabled. An attacker could exploit this vulnerability by sending crafted packets to an IP interface on an affected device. A successful exploit could allow the attacker to execute arbitrary code with root privileges and could cause process crashes resulting in a reload and DoS condition.

### 20. CVE-2026-76500｜Cisco / Cisco Application Policy Infrastructure Controller (APIC)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:01.963)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:01.963 / 2026-10-07T17:17:01.963
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Application Policy Infrastructure Controller (APIC) engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. &nbsp; The vulnerabilities tracked by CVE-2026-76500 are related to issues with improper control of a resource through its lifetime that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-664.

### 21. CVE-2026-76499｜Cisco / Cisco Application Policy Infrastructure Controller (APIC)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:01.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:01.820 / 2026-10-07T18:17:30.330
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Application Policy Infrastructure Controller (APIC) engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76499 are related to improper neutralization issues that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-707. &nbsp;

### 22. CVE-2026-76498｜Cisco / Cisco Application Policy Infrastructure Controller (APIC)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:01.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:01.670 / 2026-10-07T19:17:41.153
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Application Policy Infrastructure Controller (APIC) engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76498 are related to improper access control issues that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-284.

### 23. CVE-2026-76486｜Cisco / Cisco NX-OS Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:01.350)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:01.350 / 2026-10-08T04:17:35.460
- **官方描述（原文）**：A vulnerability in the VXLAN Operation, Administration, and Maintenance (OAM) feature of Cisco NX-OS Software, known as NGOAM, could allow an unauthenticated, remote attacker to execute arbitrary code with root privileges or cause a Denial-of-Service (DoS) on an affected device. This vulnerability is due to improper input validation of IP traffic when the NGOAM feature is enabled. An attacker could exploit this vulnerability by sending crafted packets to an IP interface on an affected device. A successful exploit could allow the attacker to execute arbitrary code with root privileges and could cause process crashes resulting in a reload and DoS condition.

### 24. CVE-2026-76485｜Cisco / Cisco NX-OS Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:01.183)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:01.183 / 2026-10-08T04:17:35.310
- **官方描述（原文）**：A vulnerability in the VXLAN Operation, Administration, and Maintenance (OAM) feature of Cisco NX-OS Software, known as NGOAM, could allow an unauthenticated, remote attacker to execute arbitrary code with root privileges or cause a Denial-of-Service (DoS) on an affected device. This vulnerability is due to improper input validation of IP traffic when the NGOAM feature is enabled. An attacker could exploit this vulnerability by sending crafted packets to an IP interface on an affected device. A successful exploit could allow the attacker to execute arbitrary code with root privileges and could cause process crashes resulting in a reload and DoS condition.

### 25. CVE-2026-76483｜Cisco / Cisco License On-Prem
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:00.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:00.910 / 2026-10-08T04:17:35.010
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the engineering team for Cisco License On-Prem, formerly Cisco Smart Software Manager On-Prem (SSM On-Prem), has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. &nbsp; The vulnerabilities tracked by CVE-2026-76483 are related to issues with insufficiently protected credentials that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-522.

### 26. CVE-2026-76482｜Cisco / Cisco License On-Prem
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:00.773)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:00.773 / 2026-10-08T04:17:34.870
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the engineering team for Cisco License On-Prem, formerly Cisco Smart Software Manager On-Prem (SSM On-Prem), has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76482 are related to issues with improper input verification that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-347.

### 27. CVE-2026-76480｜Cisco / Cisco License On-Prem
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:00.620)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:00.620 / 2026-10-08T04:17:34.733
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the engineering team for Cisco License On-Prem, formerly Cisco Smart Software Manager On-Prem (SSM On-Prem), has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76480 are related to issues with improper authentication that are grouped under the Common Weakness Enumeration (CWE) Pillar CWE-306.

### 28. CVE-2026-76471｜Cisco / Cisco NX-OS Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:17:00.230)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:17:00.230 / 2026-10-08T04:17:34.533
- **官方描述（原文）**：A vulnerability in the NX-API feature of Cisco NX-OS Software could allow an unauthenticated, remote attacker to execute arbitrary code with root privileges or cause a denial of service (DoS) condition on an affected device.&nbsp; The vulnerability is due to insufficient input validation of data that is sent to the NX-API. An attacker could exploit this vulnerability by sending a crafted HTTP request to the NX-API of an affected device. A successful exploit could allow the attacker to execute arbitrary code with root privileges and could cause process crashes, which could result in a reload of the device and a DoS condition.

### 29. CVE-2026-76465｜Cisco / Cisco NX-OS Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:16:59.350)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:16:59.350 / 2026-10-08T04:17:34.377
- **官方描述（原文）**：A vulnerability in the MPLS Operation, Administration, and Maintenance (OAM) feature of Cisco NX-OS Software for Cisco Nexus 3000 Series Switches and Cisco Nexus 9000 Series Switches could allow an unauthenticated, remote attacker to execute arbitrary code with&nbsp;root privileges or cause a denial of service (DoS) condition on an affected device. This vulnerability is due to improper validation when an affected device is processing an MPLS echo-request packet. An attacker could exploit this vulnerability by sending a crafted MPLS echo-request to an IP address on an affected device. A successful exploit could allow the attacker to execute arbitrary code with&nbsp;root privileges and could cause process crashes, which could result in a device reload and a DoS condition.

### 30. CVE-2026-76464｜Cisco / Cisco Campus Gateway Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:16:59.053)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:16:59.053 / 2026-10-07T19:17:40.650
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco networking engineering team has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by this CVE-2026-76464 are related to buffer management issues that are grouped under the Common Weakness Enumeration (CWE) CWE-119.

### 31. CVE-2026-76455｜Cisco / Cisco NX-OS Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:16:57.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:16:57.520 / 2026-10-08T04:17:32.710
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco NX-OS engineering team has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76455 are related to improper access control issues that are grouped under the Common Weakness Enumeration (CWE) CWE-284.

### 32. CVE-2026-76454｜Cisco / Cisco License On-Prem
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:16:57.363)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:16:57.363 / 2026-10-07T17:16:57.363
- **官方描述（原文）**：A vulnerability in the Cisco Smart Licensing Utility API of Cisco License On-Prem, formerly Cisco Smart Software Manager On-Prem (SSM On-Prem), could allow an unauthenticated, remote attacker to write arbitrary files to the system or cause a DoS condition on an affected application. This vulnerability is due to improper input validation and a lack of authentication in the management API. An attacker could exploit this vulnerability by sending a crafted request to the affected API. A successful exploit could allow the attacker to modify system files or cause a DoS condition.

### 33. CVE-2026-76268｜Splunk / Splunk Enterprise
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T21:17:17.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T21:17:17.607 / 2026-10-07T21:17:17.607
- **官方描述（原文）**：In Splunk Enterprise versions below 10.4.3 and 10.2.7, an unauthenticated user with network access to the Patroni Representational State Transfer (REST) Application Programming Interface (API) on a search head cluster member could execute attacker-controlled operating-system commands. The vulnerability is possible because this interface does not require authentication for critical configuration operations. For more information see Sidecar configuration settings (https://help.splunk.com/en/data-management/splunk-enterprise-admin-manual/10.2/splunk-sidecars/sidecar-configuration-settings) in the Splunk documentation. Splunk Enterprise versions 10.0.x and 9.4.x are not affected.

### 34. CVE-2026-62253｜sipcapture / homer
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:16:56.627)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:16:56.627 / 2026-10-07T17:16:56.627
- **官方描述（原文）**：Homer is open source telecom observability software. Prior to version 11.0.283, both JWT middleware functions (`JWTMiddleware` and `JWTMiddlewareV4`) immediately return `next(c)` when `jwtSecret == ""`. The JWT secret defaults to an empty string. On a default installation, all protected API endpoints under `/api/v1`, `/api/v3`, and `/api/v4` are completely unauthenticated. Version 11.0.283 patches the issue.

### 35. CVE-2026-20328｜Cisco / Cisco License On-Prem
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T17:16:55.157)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T17:16:55.157 / 2026-10-08T04:17:23.697
- **官方描述（原文）**：A vulnerability in the web-based management interface of Cisco License On-Prem, formerly Cisco Smart Software Manager On-Prem (SSM On-Prem), could allow an unauthenticated, remote attacker to gain unauthorized access to an affected application. This vulnerability is due to improper checks during the password reset process. An attacker could exploit this vulnerability by sending a malicious request to the web-based management interface. A successful exploit could allow the attacker to reset the password of an arbitrary account, including high-privileged administrative user accounts, possibly allowing the attacker to gain unauthorized access to the application as any user.

### 36. CVE-2026-17609｜WebRehab / Super Forms – Drag & Drop Form Builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T05:17:04.793)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T05:17:04.793 / 2026-10-08T05:17:04.793
- **官方描述（原文）**：The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Arbitrary Directory Deletion in all versions up to, and including, 6.3.316 via the submit_form function. This is due to insufficient validation of attacker-controlled JSON field declarations against the actual form schema, combined with a non-effective ABSPATH guard that dirname() trivially bypasses by stripping the trailing slash. This makes it possible for unauthenticated attackers to recursively delete arbitrary directories on the server, including the WordPress root directory. Exploitation requires that an administrator has enabled the 'Delete files from server after form submissions' setting, though this is a documented and commonly-enabled feature.

### 37. CVE-2026-107459｜Openfind / SecuShare Pro
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-08T06:16:42.000)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T06:16:42.000 / 2026-10-08T06:16:42.000
- **官方描述（原文）**：The SecuShare Pro developed by Openfind has an OS Command Injection vulnerability. Unauthenticated remote attackers can inject arbitrary OS commands and execute them on the server.

### 38. CVE-2026-107282｜AsyncHttpClient / async-http-client
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T22:17:04.167)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T22:17:04.167 / 2026-10-07T22:17:04.167
- **官方描述（原文）**：The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process HTTP responses. Prior to 3.0.13 and 2.16.1, cross-host request replay updates the current request but leaves the target request and related proxy context pointing at the original origin. Connection-pool selection, CONNECT handling, realm selection, and TLS setup can consequently send the original host's path, Host header, Authorization credentials, or plaintext request to the replay destination. Documented ResponseFilter failover and retry paths can trigger the replay. This issue is fixed in versions 3.0.13 and 2.16.1.

### 39. CVE-2026-107202｜jonssonyan / h-ui
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T15:17:20.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T15:17:20.090 / 2026-10-07T21:17:13.977
- **官方描述（原文）**：A command injection vulnerability exists in the h-ui (version v0.0.25 and below) administrative API due to improper validation of the listen configuration field. When an authenticated administrator submits a value containing shell metacharacters, the application constructs nftables/iptables rule strings using fmt.Sprintf and executes them via bash -c as root. Because the listen field lacks port or format validation, arbitrary OS commands can be injected and executed with root privileges.

### 40. CVE-2026-107194｜Sungrow / iSolarCloud
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T14:17:09.203)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T14:17:09.203 / 2026-10-07T14:47:21.140
- **官方描述（原文）**：Sungrow iSolarCloud before 2026 allows authentication bypass and account takeover via "login_type":"5" in a login request, potentially leading to "local blackouts on the whole continent" in Europe. An email address for the user_account property is required; however, a user can view the email address associated with their parent organization.

### 41. CVE-2026-107183｜ggml-org / llama.cpp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T14:17:09.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T14:17:09.003 / 2026-10-07T15:57:20.793
- **官方描述（原文）**：llama.cpp before b11393 contains a use-after-free and double free vulnerability in common_chat_peg_mapper::map that allows unauthenticated remote attackers to corrupt heap memory via a dangling current_tool pointer. Attackers can submit a chat_parser in a POST /completion request emitting a tool-id after a tool-close tag to crash llama-server and shape a heap write primitive.

### 42. CVE-2026-107104｜Manacle Technologies / Multi-tenant ERP System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T09:17:05.037)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00423 / percentile=0.34559
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T09:17:05.037 / 2026-10-07T19:17:33.483
- **官方描述（原文）**：This vulnerability exists in the ERP system due to unsafe deserialization of user controlled data in the affected functionality. An unauthenticated remote attacker could exploit this vulnerability by supplying specially crafted data to the vulnerable functionality of the targeted system. Successful exploitation of this vulnerability could allow the attacker to execute arbitrary code, manipulate application data or perform other unintended actions on the targeted system.

### 43. CVE-2026-107103｜Manacle Technologies / Multi-tenant ERP System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T09:17:04.913)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00325 / percentile=0.23589
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T09:17:04.913 / 2026-10-07T19:17:33.313
- **官方描述（原文）**：This vulnerability exists in the ERP system due to insufficient validation and parameterization of user supplied input in an API endpoint. An unauthenticated remote attacker could exploit this vulnerability by supplying specially crafted input to the vulnerable endpoint. Successful exploitation of this vulnerability could allow the attacker to perform SQL injection attacks on the targeted system.

### 44. CVE-2026-107102｜Manacle Technologies / Multi-tenant ERP System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T09:17:04.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00255 / percentile=0.15702
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T09:17:04.780 / 2026-10-07T19:17:33.177
- **官方描述（原文）**：This vulnerability exists in the ERP system due to improper validation of payment callback parameters and inadequate authentication controls in API endpoint. An unauthenticated remote attacker could exploit this vulnerability by manipulating the parameter to cause the application to establish an authenticated session for an arbitrary user without valid payment verification. Successful exploitation of this vulnerability could allow the attacker to bypass authentication and gain unauthorized access to other user accounts on the targeted system.

### 45. CVE-2026-105192｜LMCache / LMCache
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T10:17:32.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00671 / percentile=0.50454
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T10:17:32.647 / 2026-10-07T18:17:15.427
- **官方描述（原文）**：LMCache multiprocess mode, also called distributed mode, opens an unauthenticated ZeroMQ ROUTER so worker processes can register and share KV cache blocks. Messages on that socket are msgpack. Extension code 1 is passed to DeviceIPCWrapper.Deserialize, which calls pickle.loads, while the server is still decoding request arguments and before the handler runs. A single unauthenticated ZMQ DEALER message to the transport port (default 5555) therefore executes code as the user the LMCache process runs as. Official container images run that process as root. The transport binds to localhost unless the operator sets a routable address with --host, which is how multi-node deployments let peers connect.

### 46. CVE-2026-103416｜Eclipse Foundation / Eclipse ThreadX - NetX Duo
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T09:17:04.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00209 / percentile=0.10205
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T09:17:04.647 / 2026-10-07T19:17:31.577
- **官方描述（原文）**：Out-of-bounds write via the TLS 1.3 handshake message cache in NetX Duo in Eclipse ThreadX NetX Duo 6.5.1.202602 allows a handshake message larger than the cache writes past it and on into the rest of the session control block, which holds pointers. A malicious or compromised server can make a TLS 1.3 client produce such a message before certificate authentication completes, so no server certificate is needed to reach it.

### 47. CVE-2026-102782｜ordasoft.com / OrdaSoft Simple Membership extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T09:17:04.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00277 / percentile=0.18456
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T09:17:04.527 / 2026-10-07T19:17:31.313
- **官方描述（原文）**：Joomla Extension - ordasoft.com - Unauthenticated SQL injection in OrdaSoft Simple Membership < 7.4.0 - site/simplemembership.php dispatches task=checkLoginPass with no authentication or access control check of any kind. The handler reads a login request parameter through Joomla’s generic, non-sanitizing input filter, which strips HTML/script tags but never touches quotes or SQL syntax, and concatenates it directly into a query string with no escaping or parameterization:

### 48. CVE-2026-102255｜SonicWall / SMA1000
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T13:17:16.387)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T13:17:16.387 / 2026-10-07T16:17:32.440
- **官方描述（原文）**：A Pre-authentication SSRF vulnerability exists in the SMA1000 Appliance Work Place interface due to an unintended alternate access path. By abusing this path, a remote unauthenticated attacker could potentially exploit this vulnerability to direct the appliance to issue requests on their behalf and reach internal functionality and perform unauthorized operations.

### 49. CVE-2025-70521｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T15:16:55.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T15:16:55.003 / 2026-10-07T21:17:06.540
- **官方描述（原文）**：The management portal's diagnostic ping tool of Fanvil x7a firmware version 2.6.0.1182 does not handle user supplied input securely. The lack of secure user input handling allows any unauthenticated attacker to inject commands and run code in the underlying Android operating system.

### 50. CVE-2025-70516｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T15:16:52.310)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T15:16:52.310 / 2026-10-07T21:17:06.343
- **官方描述（原文）**：The websocket handler of Fanvil x7a firmware version 2.6.0.1182 does not enforce proper authentication restrictions against sessionless users. The lack of restrictions grants anyone the ability to view any device resources such as operational logs or perform diagnostic requests.

### 51. CVE-2025-64393｜Veeam / Backup and Replication
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T09:17:04.273)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.0036 / percentile=0.27681
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T09:17:04.273 / 2026-10-08T04:16:55.397
- **官方描述（原文）**：This vulnerability in Veeam Backup & Replication allows a Backup Viewer to execute arbitrary code as SYSTEM on the backup server.

### 52. CVE-2026-46438｜wger-project / wger
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T14:17:10.650)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T14:17:10.650 / 2026-10-07T19:17:37.280
- **官方描述（原文）**：wger is a free, open-source workout and fitness manager. Prior to version 2.6, an authenticated attacker can inject arbitrary workout log entries into any other user's `SlotEntry` by supplying the victim's `slot_entry` ID in a `POST /api/v2/workoutlog/` request. The `slot_entry` foreign key is not included in the ownership verification performed by `WorkoutLogViewSet.get_owner_objects()`, so the server accepts and persists the cross-user reference without error. Because `SlotEntry.get_config_data()` retrieves associated logs via `self.workoutlog_set.all()` with no user filter, the attacker's injected data is silently folded into the victim's progressive-overload calculations, corrupting their auto-generated weight and repetition targets. Version 2.6 contains a patch.

### 53. CVE-2026-107363｜OpenStack / Zaqar
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T21:17:15.690)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T21:17:15.690 / 2026-10-08T00:16:34.973
- **官方描述（原文）**：In OpenStack Zaqar before 23.0.1, the WebSocket transport fails to bind the project identifier in subsequent requests to the project authenticated by the Keystone token. An authenticated user with a valid token for one project may substitute another project's UUID to enumerate, inspect, create, or delete queues belonging to that project, resulting in unauthorized disclosure, modification, or loss of queue data. Only deployments using the WebSocket transport with Keystone authentication are affected.

### 54. CVE-2026-107313｜pgjdbc / pgjdbc
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T19:17:35.513)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.2 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T19:17:35.513 / 2026-10-07T21:17:15.230
- **官方描述（原文）**：pgjdbc, the PostgreSQL JDBC Driver, versions 42.7.4 and 42.7.5 can send the previous contents of the GSS send buffer in place of the first part of a value on a connection with GSS encryption (gssEncMode=prefer or require), and the server stores the value without an error. The buffer is 16320 bytes with MIT Kerberos. The stored value then holds bytes of the messages the driver sent just before it on the same connection, such as the statement's SQL text, its other parameters, and earlier rows of the same batch, instead of the bytes the application supplied. Values at least as long as the buffer are affected when the driver writes them from a byte array: bind parameters set with setString, setBytes, or a ByteStreamWriter, CopyIn.writeToCopy, and LargeObject.write. Most such writes fail with an ArrayIndexOutOfBoundsException instead. The default, gssEncMode=allow, does not start GSS encryption, and connections without GSS encryption are not affected. Versions 42.7.3 and earlier are not affected, and 42.7.6 fixes the problem.

### 55. CVE-2026-107273｜gophish / gophish
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T16:17:47.033)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T16:17:47.033 / 2026-10-07T21:17:14.777
- **官方描述（原文）**：Gophish 0.11.0 through 0.12.1 contains a server-side request forgery vulnerability that allows authenticated low-privileged users to reach loopback and private hosts via POST /api/import/site. Attackers can submit internal URLs, which the default dialer deny list does not block, to read service responses and enumerate internal hosts and ports through error messages.

### 56. CVE-2026-107271｜gophish / gophish
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T16:17:46.667)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T16:17:46.667 / 2026-10-07T23:17:00.203
- **官方描述（原文）**：Gophish through 0.12.1 contains a rate limit bypass vulnerability that allows unauthenticated attackers to evade /login throttling by spoofing X-Forwarded-For or X-Real-IP headers. Attackers can send a different forwarded address per request so the limiter keyed on rewritten RemoteAddr never triggers, enabling unlimited password guessing and credential stuffing.

### 57. CVE-2026-107224｜qax-os / excelize
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T19:17:35.140)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T19:17:35.140 / 2026-10-07T20:17:11.713
- **官方描述（原文）**：Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.1.0 to 2.11.0, a Zip64 uncompressed size with the high bit set is converted from uint64 to a negative int64 before signed size-limit checks and allocation. ReadZipReader obtains UncompressedSize64 through FileInfo.Size and passes the wrapped negative value to readFile. When a crafted Zip64 entry declares an uncompressed size from 2^63 through 2^64-1 and the workbook is opened, the negative size bypasses unzip limits and reaches make as a negative capacity, allowing an attacker to panic during workbook opening. No fixed version is available as of this review.

### 58. CVE-2026-107221｜qax-os / excelize
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T19:17:34.620)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T19:17:34.620 / 2026-10-07T20:17:11.580
- **官方描述（原文）**：Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.0.0 to 2.11.0, checkRow sizes its target cell slice from the last cell in XML document order and then re-scatters every cell by its explicit column reference. GetCellValue reaches workSheetReader and checkRow, where targetList is too short for an earlier out-of-order cell. When a crafted row places a higher-column cell before a lower-column final cell and a non-streaming worksheet API reads the sheet, the earlier cell's column index exceeds the slice length derived from the final cell, allowing an attacker to cause an unrecovered panic and terminate the process. No fixed version is available as of this review.

### 59. CVE-2026-107207｜LMCache / LMCache
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T16:17:45.617)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T16:17:45.617 / 2026-10-07T21:17:14.147
- **官方描述（原文）**：LMCache through 0.5.5 contains a server-side request forgery vulnerability in its frontend monitoring service that allows unauthenticated attackers to bypass the proxy allowlist by registering arbitrary hosts. Attackers can add entries via POST /api/proxies and then use /proxy or /proxy2 to reach internal hosts, read responses, and tamper with nodes or stop the heartbeat.

### 60. CVE-2026-107166｜未確認 / Open5GS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T16:17:44.870)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T16:17:44.870 / 2026-10-07T23:16:59.560
- **官方描述（原文）**：A weakness has been identified in Open5GS up to 2.7.7. This vulnerability affects the function ogs_pfcp_xact_local_create of the file src/upf/gtp-path.c of the component GTP-U Receive Path. This manipulation causes allocation of resources. The attack is possible to be carried out remotely. The exploit has been made available to the public and could be used for attacks. Patch name: 9ffc252482d9b03ac01abcedbe95497ff4f95dd0. It is recommended to apply a patch to fix this issue.

### 61. CVE-2025-70519｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T15:16:53.903)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T15:16:53.903 / 2026-10-07T19:17:30.810
- **官方描述（原文）**：The device log component of Fanvil x7a firmware version 2.6.0.1182 does not properly sanitize or encode reflected user supplied data. The lack of sanitization allows for the injection of HTML which can be used to execute malicious JavaScript code on any target browser which renders the device log component.

### 62. CVE-2026-107272｜gophish / gophish
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T16:17:46.853)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T16:17:46.853 / 2026-10-07T17:16:54.210
- **官方描述（原文）**：Gophish through 0.12.1 contains stored and reflected cross-site scripting vulnerabilities that allow attackers to inject script by returning malicious SMTP server error messages. Attackers controlling or intercepting a sending profile's SMTP server can execute script when administrators view campaign results or send test emails, stealing API keys.

### 63. CVE-2026-107125｜XnView / Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-07T15:17:18.440)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-07T15:17:18.440 / 2026-10-07T18:17:17.677
- **官方描述（原文）**：A flaw has been found in XnView Classic 2.52.5. Impacted is an unknown function of the component FLI File Parser. This manipulation of the argument starting_line causes heap-based buffer overflow. Remote exploitation of the attack is possible. Upgrading to version 2.52.6 is recommended to address this issue. Upgrading the affected component is advised.

### 64. CVE-2026-102266｜jpadilla / pyjwt
- **Delta event**：CVSS_CHANGED (from=7.4; to=9.1)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00175 / percentile=0.06317
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T21:17:14.257 / 2026-10-07T20:55:07.653
- **官方描述（原文）**：PyJWT is a Python implementation of JSON Web Token standards. From 2.13.0 until 2.14.0, HMACAlgorithm.from_jwk is affected because PyJWK verification path used the decoded key without applying prepare_key validation. This occurs when a trusted JWK Set contains an oct entry with an empty k value. As a result, an attacker signs an HMAC token with the same zero-length key accepted by PyJWT. Consequently, forged token can carry arbitrary authenticated claims. This issue is fixed in version 2.14.0.

### 65. CVE-2026-96419｜Wireshark Foundation / Wireshark
- **Delta event**：CVSS_CHANGED (from=5.5; to=7.8)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.00187 / percentile=0.07577
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:16.640 / 2026-10-08T01:01:35.387
- **官方描述（原文）**：Profile import crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service and possible code execution

### 66. CVE-2026-95387｜Wireshark Foundation / Wireshark
- **Delta event**：CVSS_CHANGED (from=8.1; to=8.8)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00364 / percentile=0.28192
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:14.713 / 2026-10-08T01:33:55.930
- **官方描述（原文）**：SPDY protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 67. CVE-2026-105744｜docling-project / docling
- **Delta event**：CVSS_CHANGED (from=7.5; to=8.8)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00304 / percentile=0.2127
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T22:16:57.177 / 2026-10-07T19:33:16.747
- **官方描述（原文）**：Docling simplifies document processing by parsing diverse formats and providing integrations with the generative AI ecosystem. From 2.94.0 until 2.132.0, callers that opt into LatexBackendOptions(tikz_engine="tectonic") invoke docling/backend/latex/engines/tectonic.py to compile an untrusted TikZ body and document preamble without restricting TeX file primitives including \openin and \openout. Crafted input can read files available to the converter and create or overwrite writable files, and enabling the tikz_engine_allow_shell_escape option additionally permits shell commands through TeX. The default configuration, which does not enable Tectonic rendering, is not affected. This vulnerability is fixed in 2.132.0.

### 68. CVE-2026-105742｜docling-project / docling
- **Delta event**：CVSS_CHANGED (from=3.7; to=5.3)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00218 / percentile=0.1124
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T22:16:56.867 / 2026-10-07T19:52:37.513
- **官方描述（原文）**：Docling simplifies document processing by parsing diverse formats and providing integrations with the generative AI ecosystem. From 2.95.0 until 2.132.0, the HTML image resource loader in docling/backend/utils/image_resource_loader.py forwards headers configured through the HTMLBackendOptions.headers setting to every remote image URL named by an untrusted document when enable_remote_fetch=True and fetch_images=True. The loader does not restrict those credentials to the source document's origin, allowing requests that carry custom headers such as API keys and cookies to follow cross-origin redirects and expose the caller's configured credentials to a document author. The default configuration is not affected because remote fetching and configured headers are required. This issue is fixed in 2.132.0.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-62252 | P3 / 38 | sipcapture / homer | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-62176 | P3 / 38 | MervinPraison / PraisonAI | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107204 | P3 / 38 | LMCache / LMCache | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2025-70518 | P3 / 38 | 未確認 / 未確認 | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-46434 | WATCH / 30 | wger-project / wger | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-43976 | WATCH / 30 | wger-project / wger | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107270 | WATCH / 30 | gophish / gophish | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107214 | WATCH / 30 | qax-os / excelize | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107212 | WATCH / 30 | qax-os / excelize | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107206 | WATCH / 30 | LMCache / LMCache | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107181 | WATCH / 30 | Telegram / Telegram Desktop | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107177 | WATCH / 30 | ExpressGateway / express-gateway | v4.0 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-106058 | WATCH / 30 | gitahead / gitahead | v4.0 7.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97720 | WATCH / 28 | Apache Software Foundation / Apache Impala | v3.1 9.1 (CRITICAL) | 0.00196 / percentile=0.08526 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96408 | WATCH / 28 | Six Apart Ltd. / Movable Type Cloud Edition | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95606 | WATCH / 28 | Liquid Web / StellarWP / The Events Calendar | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95605 | WATCH / 28 | Passionate Programmer Peter / WP Data Access | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-92414 | WATCH / 28 | Apache Software Foundation / Apache Jackrabbit | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76501 | WATCH / 28 | Cisco / Cisco NX-OS Software | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76500 | WATCH / 28 | Cisco / Cisco Application Policy Infrastructure Controller (APIC) | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76499 | WATCH / 28 | Cisco / Cisco Application Policy Infrastructure Controller (APIC) | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76498 | WATCH / 28 | Cisco / Cisco Application Policy Infrastructure Controller (APIC) | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76486 | WATCH / 28 | Cisco / Cisco NX-OS Software | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76485 | WATCH / 28 | Cisco / Cisco NX-OS Software | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76483 | WATCH / 28 | Cisco / Cisco License On-Prem | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76482 | WATCH / 28 | Cisco / Cisco License On-Prem | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76480 | WATCH / 28 | Cisco / Cisco License On-Prem | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76471 | WATCH / 28 | Cisco / Cisco NX-OS Software | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76465 | WATCH / 28 | Cisco / Cisco NX-OS Software | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-76464 | WATCH / 28 | Cisco / Cisco Campus Gateway Software | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：1；缺少 Product：1；缺少 Title：30。
- EPSS 未確認：29；Exploitation status 未確認：1。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-08T06:51:07.715417+00:00`；Delta generated at：`2026-10-08T06:51:07.715417+00:00`。

---

## 可驗證資料來源

- **CVE-2026-62252** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62252)
- **CVE-2026-62176** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62176)
- **CVE-2026-107204** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107204)
- **CVE-2025-70518** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-70518)
- **CVE-2026-46434** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46434)
- **CVE-2026-43976** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-43976)
- **CVE-2026-107270** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107270)
- **CVE-2026-107214** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107214)
- **CVE-2026-107212** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107212)
- **CVE-2026-107206** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107206)
- **CVE-2026-107181** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107181)
- **CVE-2026-107177** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107177)
- **CVE-2026-106058** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-106058)
- **CVE-2026-97720** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97720) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97720)
- **CVE-2026-96408** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96408)
- **CVE-2026-95606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95606)
- **CVE-2026-95605** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95605)
- **CVE-2026-92414** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92414)
- **CVE-2026-76501** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76501)
- **CVE-2026-76500** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76500)
- **CVE-2026-76499** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76499)
- **CVE-2026-76498** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76498)
- **CVE-2026-76486** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76486)
- **CVE-2026-76485** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76485)
- **CVE-2026-76483** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76483)
- **CVE-2026-76482** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76482)
- **CVE-2026-76480** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76480)
- **CVE-2026-76471** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76471)
- **CVE-2026-76465** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76465)
- **CVE-2026-76464** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76464)
- **CVE-2026-76455** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76455)
- **CVE-2026-76454** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76454)
- **CVE-2026-76268** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76268)
- **CVE-2026-62253** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62253)
- **CVE-2026-20328** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20328)
- **CVE-2026-17609** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17609)
- **CVE-2026-107459** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107459)
- **CVE-2026-107282** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107282)
- **CVE-2026-107202** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107202)
- **CVE-2026-107194** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107194)
- **CVE-2026-107183** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107183)
- **CVE-2026-107104** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107104) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107104)
- **CVE-2026-107103** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107103) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107103)
- **CVE-2026-107102** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107102) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107102)
- **CVE-2026-105192** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105192) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105192)
- **CVE-2026-103416** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103416) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-103416)
- **CVE-2026-102782** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102782) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-102782)
- **CVE-2026-102255** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102255)
- **CVE-2025-70521** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-70521)
- **CVE-2025-70516** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-70516)
- **CVE-2025-64393** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-64393) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-64393)
- **CVE-2026-46438** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46438)
- **CVE-2026-107363** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107363)
- **CVE-2026-107313** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107313)
- **CVE-2026-107273** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107273)
- **CVE-2026-107271** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107271)
- **CVE-2026-107224** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107224)
- **CVE-2026-107221** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107221)
- **CVE-2026-107207** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107207)
- **CVE-2026-107166** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107166)
- **CVE-2025-70519** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-70519)
- **CVE-2026-107272** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107272)
- **CVE-2026-107125** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107125)
- **CVE-2026-102266** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102266) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-102266)
- **CVE-2026-96419** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96419) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96419)
- **CVE-2026-95387** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95387) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95387)
- **CVE-2026-105744** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105744) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105744)
- **CVE-2026-105742** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105742) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105742)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
