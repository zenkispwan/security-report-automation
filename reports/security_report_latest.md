# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**135** 筆符合目前門檻的重要變化；事件統計：EXPLOITATION_CHANGED=6、NEW_CVE=127、NEW_KEV=4。
- Intelligence 候選：**30** 筆；P1 **4**、P2 **0**、P3 **6**、WATCH **20**。
- Baseline：state / generated_at=2026-10-14T05:38:44.265442+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-76519、CVE-2026-105134、CVE-2026-0322、CVE-2026-105133。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **135** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-76519｜Cisco / Secure Email Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:19:10.747)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-14T17:19:10.747 / 2026-10-15T04:18:26.410
- **官方描述（原文）**：Cisco Secure Email Gateway contains a relative path traversal vulnerability that could allow an unauthenticated, remote attacker to write arbitrary files on the underlying operating system.

### 2. CVE-2026-105134｜Ahsay / AhsayCBS
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.01843 / percentile=0.78594
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-04T07:16:33.480 / 2026-10-15T04:18:15.337
- **官方描述（原文）**：Ahsay AhsayCBS contains a command injection vulnerability that could allow a remote attacker to execute operating system commands via manipulation of the random parameter in the Replication Receiver component’s /rps/api/json/UpdateReceivers.do endpoint. This vulnerability can be chained with CVE-2026-105133.

### 3. CVE-2026-0322｜Palo Alto Networks / PAN-OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:17:07.743)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-14T18:17:07.743 / 2026-10-15T04:18:03.657
- **官方描述（原文）**：Palo Alto Networks PAN-OS contains a code injection vulnerability that could allow an authenticated attacker with network access to execute arbitrary code with root privileges on the firewall.

### 4. CVE-2026-105133｜Ahsay / AhsayCBS
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00383 / percentile=0.30672
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-04T07:16:33.087 / 2026-10-15T04:18:14.760
- **官方描述（原文）**：Ahsay AhsayCBS contains an improper authentication vulnerability that could allow a remote attacker to bypass authentication via manipulation of the random parameter in the API component’s checkSysPwd function. This vulnerability can be chained with CVE-2026-105134.

### 5. CVE-2026-65198｜Huawei / openUBMC
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 20；reasons：CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：0.00189 / percentile=0.07967
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T15:17:46.823 / 2026-10-14T20:17:58.190
- **官方描述（原文）**：Huawei's openUBMC ships a default SNMPv3 USM key that uses one value for both authentication and privacy. An attacker who holds the key (recoverable from the open-source build) can authenticate SNMPv3 to, and decrypt SNMPv3 traffic from, any unit that still carries the shipped key. The build customization `manifest/build/customization/default_password.lua` sets `AuthenticationKey == EncryptionKey == 7df2f29369e3ac3245b2c9d46b67a0ecd055197e41808a34ef325db2f6422581` for the iBMC product build, and the community seed `account/manufacture/default_password.lua` sets both to `7a2f5b86f20233ec7b7bef49643fbf34d86d0cbf6f1f8f5c52d4f30d4536938b`. These are shipped constants, not per-unit values, and they are not rotated by the Administrator password reset, so they survive account provisioning. This is especially dangerous considering that SNMP access is mapped to full device administration privileges, including system reset and firmware upgrades.

### 6. CVE-2026-93748｜kornelski / http-cache-semantics
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 12；reasons：CVSS_HIGH(+12)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.00569 / percentile=0.45808
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:18:33.330 / 2026-10-14T23:19:08.810
- **官方描述（原文）**：http-cache-semantics through 4.2.0 fails to properly validate security-zeroed cache entries when processing client max-stale directives, allowing unauthenticated attackers to retrieve cached responses belonging to other users. Attackers can request the same URL with a large max-stale value to obtain another user's Set-Cookie session credentials from shared-cache entries that were deliberately zeroed for security reasons.

### 7. CVE-2026-93687｜micromatch / braces
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 12；reasons：CVSS_HIGH(+12)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.00757 / percentile=0.54161
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:15.507 / 2026-10-14T23:19:08.670
- **官方描述（原文）**：braces through 3.0.3 contains a stack overflow vulnerability in the recursive AST walkers that lack depth guards. Attackers can supply deeply nested brace patterns under the character limit to exhaust the call stack and terminate the Node.js process with an uncaught RangeError.

### 8. CVE-2026-65199｜Huawei / openBMC
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 12；reasons：CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：0.0015 / percentile=0.03774
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T15:17:46.947 / 2026-10-14T19:17:18.883
- **官方描述（原文）**：openUBMC assigns the full privilege set to pseudo-identities representing SNMP callers. An authenticated, but low-privilege, SNMP user can therefore invoke mapped backend operations as an administrative identity. In `route_mapper/account.lua`, `get_user_privilege` returns the complete nine-privilege set for a `special_users` group that includes the `SNMPv1_v2c` pseudo-user.

### 9. CVE-2026-65200｜Huawei / openBMC
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 8；reasons：RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.5 (LOW)
- **EPSS**：0.00143 / percentile=0.0317
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T15:17:47.077 / 2026-10-14T19:17:19.040
- **官方描述（原文）**：The openUBMC device-management process parses PLDM-over-MCTP and NCSI-over-MCTP responses from on-bus devices, and three response parsers in the shared transport libraries subtract a fixed header or reserved-field size from a device-supplied response length without a lower-bound check. An undersized response wraps the unsigned length difference to a very large value, and the parser then reads far past the response buffer. The affected code sits in the base (non-vendor) PLDM control class and the Huawei NCSI driver, so it is reachable for any PLDM endpoint or Huawei NIC on the internal management bus, unlike the vendor-specific wangxun parser tracked separately.

### 10. CVE-2026-65197｜H3C / HDM Family-A G5
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)
- **Risk**：WATCH / score 8；reasons：RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.1 (LOW)
- **EPSS**：0.00098 / percentile=0.00739
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T15:17:46.690 / 2026-10-14T19:17:18.740
- **官方描述（原文）**：H3C HDM Family-A verifies the RSA signature of a firmware image against a public key it reads from the mutable file `/conf/public.pem`. That file is writable by an authenticated Redfish client through the `UpdateService.UploadSignKey` action, which stores the uploaded body verbatim after validating only that the multipart filename ends in `.pem`. An administrator, or any account with `firmware-update` privilege, can therefore replace the trust anchor with their own key, sign a malicious image with the matching private key, and have it pass verification. Family-A has no hardware root-of-trust (no PFR) to catch the substituted key. This was observed on H3C HDM Family-A G5 HDM 6.14.01. H3C HDM Family-A G3/G5 builds carrying the Redfish/DRE update tree appear to be affected. HDM2 uses a different update path and is not covered by this finding.

### 11. CVE-2026-77371｜getredash / redash
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:18:18.570)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:18:18.570 / 2026-10-14T20:17:59.113
- **官方描述（原文）**：Redash is a package for data visualization and sharing. From 26.0.0 until 26.9.0, the DuckDB query runner's _connect() path in redash/query_runner/duckdb.py created connections with enable_external_access left at its default value of true. A user with query access to an administrator-created DuckDB data source could use native file-reading functions to retrieve files readable by the Redash process or use COPY TO to write files with that process's privileges. Reading application secrets such as REDASH_COOKIE_SECRET or REDASH_SECRET_KEY could also enable forged sessions and authentication bypass. This issue is fixed in version 26.9.0.

### 12. CVE-2026-110650｜anshulkharb / thumbnail
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:18.793)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:18.793 / 2026-10-14T21:17:35.953
- **官方描述（原文）**：The thumbnail Python package through 1.5 contains an OS command injection vulnerability in generate_thumbnail() that allows attackers to execute commands by supplying shell metacharacters in file paths. Attackers who control a file name passed to generate_thumbnail, such as an uploaded file, can inject commands into os.system() calls running ffmpeg, convert or unoconv with the Python process privileges.

### 13. CVE-2026-110645｜ArsalanDotMe / video-stitch
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:18.090)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:18.090 / 2026-10-14T21:17:35.830
- **官方描述（原文）**：Video-stitch before 2.0.0-beta.1 contains an OS command injection vulnerability that allows attackers to execute commands by supplying file names interpolated unquoted into shell-executed ffmpeg command lines. Attackers who influence file names passed to concat(), cut(), or merge() can inject shell metacharacters to run commands with the Node.js process privileges.

### 14. CVE-2026-110632｜Report One / MyReport Updater
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:16.143)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:16.143 / 2026-10-14T19:17:10.787
- **官方描述（原文）**：Report One MyReport Updater through 2.1.1 exposes an unauthenticated gRPC service on TCP port 9095 that allows remote attackers to redirect the SYSTEM updater by invoking the UpdateConfigReferent method. Attackers can point the updater to a malicious reference server serving modified module archives with matching MD5 digests to write files and execute code as SYSTEM.

### 15. CVE-2026-110612｜wwwlike / vlife
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:13.187)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:13.187 / 2026-10-14T18:17:34.803
- **官方描述（原文）**：vlife through 2.0.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge JWTs using the hardcoded HS256 signing key in TokenUtil. Attackers can sign a token with superUser=true and arbitrary groupIds claims to gain super administrator access to any URL on vlife instances.

### 16. CVE-2026-108390｜hestiacp / hestiacp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:17:27.180)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:17:27.180 / 2026-10-14T18:17:27.180
- **官方描述（原文）**：Hestia Control Panel is a lightweight and powerful control panel for the modern web. From version 1.9.7 through 1.10.4, update_object_value() in func/main.sh does not escape single quotes when writing a custom document-root value to a user's web.conf file, allowing a low-privileged authenticated panel user with a web domain to inject an additional PATH field. When the user invokes the ordinary Search feature, the root-privileged v-search-user-object script loads the forged field through parse_object_kv_list_non_eval(), which permits reserved shell-variable names and globally replaces PATH before invoking column without an absolute path. By placing a malicious column executable in the injected search path, the user can execute arbitrary code as root. This residual vulnerability was introduced when version 1.9.7 replaced the raw eval sink addressed by CVE-2026-84984 with parse_object_kv_list_non_eval(), and it is fixed in version 1.10.5.

### 17. CVE-2026-73252｜cesanta / mongoose
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:19.667)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:19.667 / 2026-10-14T20:17:58.753
- **官方描述（原文）**：Mongoose is an embedded web server and network library. Prior to 7.23, the built-in TLS stack selected by MG_TLS_BUILTIN in src/tls_builtin.c accepts a TLS 1.3 record whose decrypted size is exactly the 16-byte authentication tag with no plaintext or ContentType byte. In mg_tls_recv_record(), the msgsz length check permits that record and the recv_len calculation underflows to SIZE_MAX, so a later handshake step treats stale buffer contents as a trusted message with an effectively unbounded length. An unauthenticated malicious TLS peer can trigger a heap out-of-bounds read before certificate or Finished validation, causing a remote denial of service. This issue is fixed in version 7.23.

### 18. CVE-2026-55386｜InvoiceShelf / InvoiceShelf
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T20:17:48.773)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T20:17:48.773 / 2026-10-14T20:17:48.773
- **官方描述（原文）**：InvoiceShelf is an open-source web & mobile app that helps track expenses, payments and create professional invoices and estimates. Prior to version 2.4.0, InvoiceShelf passes the authenticated user's orderByField query parameter into Laravel orderBy calls in Invoice::scopeApplyFilters without restricting the value to column identifiers. A crafted SQL expression can therefore enter the ORDER BY clause across invoice and other list endpoints, enabling boolean-based blind extraction of database information. This issue is fixed in version 2.4.0.

### 19. CVE-2026-55383｜InvoiceShelf / InvoiceShelf
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T20:17:48.350)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T20:17:48.350 / 2026-10-14T20:17:48.350
- **官方描述（原文）**：InvoiceShelf is an open-source web & mobile app that helps track expenses, payments and create professional invoices and estimates. Prior to version 2.4.0, InvoiceShelf public customer invoice, estimate, and payment routes use an EmailLog token's numeric mailable_id without verifying mailable_type, and the JSON handlers do not enforce EmailLog::isExpired. A token issued for one document type can therefore disclose a different company's document when numeric identifiers collide, and an expired token can remain usable on the JSON routes GET /customer/invoices/{email_log:token}, GET /customer/estimates/{email_log:token}, and GET /customer/payments/{email_log:token}. View handlers can also mark a mismatched invoice or estimate as viewed and send a notification. This issue is fixed in version 2.4.0.

### 20. CVE-2026-54566｜shd101wyy / vscode-markdown-preview-enhanced
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T20:17:47.403)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T20:17:47.403 / 2026-10-14T20:17:47.403
- **官方描述（原文）**：Markdown Preview Enhanced is a Markdown preview extension for Visual Studio Code. Prior to 0.8.29, Markdown Preview Enhanced evaluates repository-controlled .crossnote/config.js and .crossnote/parser.js files with vm.runInNewContext, which does not provide a security boundary from the Node.js host realm. Opening a Markdown file in a malicious repository automatically loads these files, and prototype-chain traversal can reach the host Function constructor and process object, allowing operating-system commands to execute as the victim account without further interaction. Both configuration evaluation and parser-hook evaluation are affected, and the attack does not depend on module-scoped require being available. This issue is fixed in version 0.8.29.

### 21. CVE-2026-53999｜radius-project / radius
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:17.340)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:17.340 / 2026-10-14T20:17:47.277
- **官方描述（原文）**：Radius is a cloud-native, portable application platform that makes app development easier for teams building cloud-native apps. Prior to 0.58.0, the Kubernetes controller deserializes the user-controlled radapp.io/status annotation on a Deployment and uses its container resource identifier for deletion without confirming ownership by that Deployment. An attacker with permission to modify Deployment annotations and knowledge of a target Radius resource ID can forge radapp.io/status and set radapp.io/enabled to false, causing reconciliation to enter the privileged deletion path for another tenant's Radius-managed container resource. In a multi-tenant installation this confused-deputy condition can delete another team's recoverable container resource and disrupt service; in a single-tenant installation the impact is limited to self denial of service. The multi-tenant Radius controller reads the annotations in pkg/controller/reconciler/annotations.go and reaches the privileged delete in pkg/controller/reconciler/deployment_reconciler.go. The issue does not disclose data, grant privileges, or provide persistence. This issue is fixed in version 0.58.0.

### 22. CVE-2026-53612｜util-linux / util-linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:20.260)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.0 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:20.260 / 2026-10-14T19:17:17.210
- **官方描述（原文）**：util-linux is a random collection of Linux utilities. In util-linux 2.39 through 2.41.4 and 2.42 through 2.42.1, the SUID `mount` utility's `hook_owner.c` post-mount hook performs path-based `chmod()` and `lchown()` operations on a previously validated mount target. A local low-privileged user authorized by an `/etc/fstab` entry with `user` or `users` and an `X-mount.mode`, `X-mount.owner`, or `X-mount.group` option can use `renameat2(RENAME_EXCHANGE)` to race a writable ancestor of the target and redirect the privileged ownership or mode change to a root-owned path, potentially gaining root privileges. This issue is fixed in 2.41.5 and 2.42.2.

### 23. CVE-2026-42093｜getredash / redash
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:17:36.980)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:17:36.980 / 2026-10-14T20:17:44.173
- **官方描述（原文）**：Redash is a package for data visualization and sharing. From versions after 8.0.0 until 26.9.0, the Query Results query runner in redash/query_runner/query_results.py accepts param_query_N_{key=value} parameters and passed attacker-controlled values to replace_query_parameters() for raw substitution into a referenced query's SQL. This path bypassed the ParameterizedQuery schema validation used by normal query execution and omitted the is_safe permission check. An authenticated user with at least view-only access to both the Query Results data source and the referenced data source could therefore inject SQL through text parameters and execute it with the referenced data source's privileges. This issue is fixed in version 26.9.0.

### 24. CVE-2026-110718｜TurboDocx / html-to-docx
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:44.047)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:44.047 / 2026-10-14T21:17:36.797
- **官方描述（原文）**：TurboDocx html-to-docx through 1.23.1 contains a server-side request forgery vulnerability that allows attackers supplying HTML to make the server fetch internal URLs via img src attributes. Attackers can reference loopback, private, or cloud metadata addresses that bypass the loose isValidUrl() check, and read responses embedded in the generated DOCX word/media folder.

### 25. CVE-2026-110713｜sahlberg / libsmb2
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:43.337)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:43.337 / 2026-10-14T20:17:31.393
- **官方描述（原文）**：libsmb2 through 6.2 contains a heap out-of-bounds read vulnerability in smb2_decode_file_fs_volume_info and smb2_decode_file_fs_attribute_info that allows malicious SMB servers to read past reply buffers. Attackers controlling a server or intercepting unsigned sessions can send crafted QUERY_INFO replies with missing or oversized name lengths to crash the client.

### 26. CVE-2026-110712｜sahlberg / libsmb2
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:43.193)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:43.193 / 2026-10-14T18:17:36.103
- **官方描述（原文）**：libsmb2 through 6.2 contains a heap out-of-bounds read vulnerability in smb2_decode_file_all_info that allows malicious SMB servers to crash clients by sending an unchecked FileNameLength. Attackers controlling the server or performing man-in-the-middle on unsigned sessions can return crafted FileAllInformation replies to smb2_stat or smb2_fstat calls, crashing the client.

### 27. CVE-2026-110614｜Yiuman / citrus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:13.463)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:13.463 / 2026-10-14T17:18:25.803
- **官方描述（原文）**：Yiuman citrus through 0.15.0 contains an ORDER BY sql injection vulnerability in the citrus-support generic query framework that allows users to inject SQL via the sortBy request parameter. Attackers can reach any generic list route of controllers extending BaseQueryController or BaseQueryRestful to append unvalidated SQL to the ORDER BY clause and extract database contents using boolean- or time-based blind techniques.

### 28. CVE-2026-110609｜dromara / skyeye
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:12.760)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:12.760 / 2026-10-14T17:18:25.683
- **官方描述（原文）**：Dromara Skyeye through commit 65d3ddcede70 contains an sql injection vulnerability that allows authenticated low-privileged users to inject SQL via the keyword parameter in the queryErpOrderItem MyBatis statement using raw ${} substitution. Attackers can send crafted keyword values to the queryWarehousingDetails or queryOutgoingDetails endpoints to extract database data, including other tenants' data, using boolean, UNION, error or time-based techniques.

### 29. CVE-2026-110607｜BizSpring / BizSpring Shop
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:12.457)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:12.457 / 2026-10-14T18:17:34.667
- **官方描述（原文）**：BizSpring Shop through commit cf22d39daaf1 contains a payment verification bypass vulnerability that allows authenticated buyers to mark orders paid by calling the PaymentController.testPostPay handler. Attackers can generate a payment log via /member/payment/load and request /member/payment/test_post_pay_{paymentLogSn} to obtain goods without paying or settle other members' orders.

### 30. CVE-2026-105106｜Koha Community / Koha
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T08:17:03.587)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.01613 / percentile=0.75485
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T08:17:03.587 / 2026-10-14T18:17:23.040
- **官方描述（原文）**：Koha is vulnerable to OS command injection in the Task Scheduler deletion path. The tools/scheduler.pl handler accepts the jobid request parameter for op=cud-delete and passes it to C4::Scheduler::remove_at_job without validating it. Schedule::At::remove substitutes the supplied job ID into an atrm command string without quoting or escaping it and executes the command through a single-argument system() call, which invokes the shell. An authenticated staff user with the tools => schedule_tasks permission can therefore execute arbitrary operating-system commands as the Koha web/application user by supplying shell metacharacters in jobid. The issue is fixed in Koha 24.11.20, 25.05.15, 25.11.09, and 26.05.04, and in the 26.11 development branch.

### 31. CVE-2026-101895｜angular / angular
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:03.370)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:03.370 / 2026-10-14T18:17:10.800
- **官方描述（原文）**：Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.31, 21.2.23, and 22.1.6, the @angular/platform-server DOM emulation parser can enter an infinite synchronous loop when Angular server-side rendering processes attacker-controlled HTML containing an incomplete DOCTYPE that ends with whitespace at end of input. In Domino lib/HTMLParser.js, after_doctype_name_state emits doctype and EOF tokens without advancing nextchar or leaving the fixed-lookahead state, so the scanner repeatedly handles the same EOF marker. A remote unauthenticated attacker can use this condition through server-side HTML parsing paths such as innerHTML binding to consume a Node.js SSR worker at full CPU, starve the event loop, and stop concurrent and subsequent requests. This issue is fixed in versions 20.3.31, 21.2.23, and 22.1.6.

### 32. CVE-2025-71433｜usekaneo / kaneo
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:00.837)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:00.837 / 2026-10-14T18:17:07.607
- **官方描述（原文）**：Kaneo before 2.1.6 contains a missing authorization vulnerability that allows authenticated users to access other workspaces by supplying project, task, label or workspace identifiers to API routes lacking membership checks. Attackers who obtain identifiers, for example from shared project links, can read projects and tasks, modify or delete tasks, labels and comments, and search workspace contents.

### 33. CVE-2026-97205｜F5 / NGINX Plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:28.200)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:28.200 / 2026-10-15T04:18:31.167
- **官方描述（原文）**：NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_core_module module. When asynchronous file I/O (AIO) is enabled in certain configurations, processing a Server Side Includes (SSI) page containing “include virtual” commands may trigger a Use-After-Free (UAF) in the NGINX worker process. This may cause memory corruption or a worker process crash. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. Impact: This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system, corrupt its memory, or possibly trigger code execution. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 34. CVE-2026-93483｜Znuny / Znuny
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T04:18:30.153)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T04:18:30.153 / 2026-10-15T04:18:30.153
- **官方描述（原文）**：In Znuny through 7.3.6, an attacker can bypass specific standard login procedures and gain unauthorized access to sensitive system functions by manipulating a specific HTTP request header. Because the application incorrectly trusts this header, an attacker can impersonate any user, including administrators, without requiring a password. This grants full access to confidential data and system controls. More specifically, the HTTPBasicAuth modules for the agent (Kernel::System::Auth::HTTPBasicAuth) and customer (Kernel::System::CustomerAuth::HTTPBasicAuth) interfaces read the username to log in not only from $ENV{REMOTE_USER} (set by the web server after successful authentication), but also, as a fallback, from $ENV{HTTP_REMOTE_USER}, which is populated directly from an attacker-controllable "Remote-User" request header. On systems where HTTPBasicAuth was configured as the authentication backend, this allowed an attacker to log in as any existing user by sending a request with a forged Remote-User header, without providing any credentials.

### 35. CVE-2026-93479｜F5 / NGINX Plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:26.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:26.810 / 2026-10-15T04:18:29.960
- **官方描述（原文）**：A vulnerability exists in NGINX Plus and NGINX Open Source when a map directive uses regex matching and the root directive or access log format references the map's regex capture variables before referencing the map output variable. Alternatively, the same result could be achieved by using a non-cacheable variable in a string expression under certain conditions. An unauthenticated attacker along with conditions beyond their control can exploit this vulnerability by sending crafted HTTP requests. This may cause a heap buffer overflow in the NGINX worker process leading to a restart. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. Impact: This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or to possibly trigger a code execution. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 36. CVE-2026-92152｜nasa / fprime
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:19:34.497)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:19:34.497 / 2026-10-14T18:19:34.497
- **官方描述（原文）**：F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applications. From 4.1.0 until 4.2.0, Svc::GenericHub output-port dispatch is vulnerable because the deserialized port field is passed to serialOut_out, bufferOut_out, eventOut_out, or tlmOut_out without an explicit range check. When a remote hub packet supplies a port index outside the configured output-port array, assert-enabled builds abort, while builds without assertions can access an output-port array out of bounds, corrupt heap memory, and potentially allow remote code execution. This issue is fixed in version 4.2.0.

### 37. CVE-2026-91881｜Dell / Terraform Provider for Redfish
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:56.767)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:56.767 / 2026-10-14T16:17:56.767
- **官方描述（原文）**：Dell Terraform Provider for Redfish, versions prior to 1.6.2, contains an Improper Certificate Validation vulnerability in the HTTP transport component. An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to information exposure and unauthorized access. This is a Critical severity vulnerability as it allows an unauthenticated attacker to intercept all Redfish BMC traffic including credentials by performing a man-in-the-middle attack, since TLS certificate verification is unconditionally disabled in the base HTTP transport. Dell recommends customers to upgrade at the earliest opportunity.

### 38. CVE-2026-89310｜JTL SW GmbH / JTL-WMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T07:17:04.650)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00467 / percentile=0.38891
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T07:17:04.650 / 2026-10-14T16:17:56.193
- **官方描述（原文）**：A parameter taken from the request body is inserted into a T-SQL statement without parameterization or escaping, allowing a remote attacker to execute arbitrary SQL statements in the context of the application's database account.

### 39. CVE-2026-86002｜dokku / dokku
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:54.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:54.470 / 2026-10-14T18:19:17.510
- **官方描述（原文）**：Dokku is a docker-powered platform as a service. In Dokku versions before 0.38.25, a user with app-level Dokku access and remote SSH access to execute docker-options commands can store arbitrary strings through the docker-options plugin, and those strings are later concatenated into DOCKER_ARGS and processed by Bash eval during build, deploy, or run operations. Shell command substitutions in the stored values are interpreted on the host, allowing arbitrary command execution with the privileges of the dokku operating-system user. This issue is fixed in version 0.38.25.

### 40. CVE-2026-85714｜Stirling-Tools / Stirling-PDF
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:22.050)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:22.050 / 2026-10-14T19:17:22.050
- **官方描述（原文）**：Stirling-PDF is a locally hosted web application that facilitates various operations on PDF files. Prior to 2.13.2, an authenticated administrator using the default H2 database and security mode can upload a crafted SQL file to POST /api/v1/database/import-database. DatabaseService.validateSqlContent() splits normalized input on semicolons and accepts a statement when it contains any allowed keyword, allowing dangerous H2 functions such as FILE_READ and CSVWRITE, plus CREATE ALIAS, to bypass the insufficient whitelist and execute side effects when RUNSCRIPT processes the file. This permits arbitrary file access. The demonstrated operating-system command execution chain writes attacker-controlled startup files to a user-site location and then triggers an application Python interpreter configured to load those startup files, resulting in command execution as the JVM service account. This issue is fixed in version 2.13.2.

### 41. CVE-2026-77524｜kedacore / keda
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:19:11.147)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:19:11.147 / 2026-10-14T17:19:11.147
- **官方描述（原文）**：KEDA is a Kubernetes-based Event Driven Autoscaling component. In version 2.20.2 and earlier, a namespace administrator who can create TriggerAuthentication and ScaledObject resources can set hashiCorpVault.address to a tenant-controlled endpoint and select Kubernetes authentication without an explicit credential. KEDA then uses the operator pod's projected ServiceAccount token and sends it to that endpoint as a Vault login credential. The JWT-shape filter from the prior CVE-2025-68476 remediation accepts the operator token because its subject is a Kubernetes ServiceAccount, so the attacker can obtain the operator's cluster-wide permissions, including broad Secret reads and workload or admission-related operations. This vulnerability is fixed in 2.21.0.

### 42. CVE-2026-59774｜Gitea / Gitea
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:20.677)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:20.677 / 2026-10-15T04:18:24.663
- **官方描述（原文）**：Gitea's Org-mode markup renderer processes INCLUDE directives supplied to the repository markup endpoint without preventing access to server-side files. An unauthenticated attacker can use a suitable public repository to read files accessible to the Gitea service account. If the disclosed files include app.ini and its INTERNAL_TOKEN, the attacker can chain the disclosure with internal logger access to modify a Git hook and execute commands as the Gitea service account.

### 43. CVE-2026-55684｜LabRedesCefetRJ / WeGIA
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T20:17:50.783)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T20:17:50.783 / 2026-10-14T20:17:50.897
- **官方描述（原文）**：WeGIA is a web manager for charitable institutions. Prior to 3.8.6, the unauthenticated web/html/socio/sistema/cadastro_cobrancas_geracao.php endpoint accepts form-encoded POST data through extract($_REQUEST) and interpolates codigo, descricao, data_emissao, data_vencimento, data_pagamento, valor, valor_pago, status, link_cobranca, link_boleto, linha_digitavel, and id_socio into a raw INSERT statement. Numeric parameters are unquoted and unvalidated, while string parameters can break out of their single-quoted SQL context. A remote attacker can execute arbitrary SQL to read or modify billing, member, employee, permission, and credential data or to delete database tables. This issue is fixed in version 3.8.6.

### 44. CVE-2026-55683｜LabRedesCefetRJ / WeGIA
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T20:17:50.640)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T20:17:50.640 / 2026-10-14T20:17:50.750
- **官方描述（原文）**：WeGIA is a web manager for charitable institutions. Prior to 3.8.6, the unauthenticated web/html/socio/sistema/cadastro_cobranca.php endpoint accepts POST input through extract($_REQUEST) and directly incorporates valor, valor_pago, id_pessoa, id_socio, and id_sociotipo into UPDATE, INSERT, and SELECT statements without prepared statements. A remote attacker can use the affected parameters to execute arbitrary SQL that reads or modifies WeGIA database content, including billing records and credential data. The same SQL access can delete or truncate tables, causing loss of application data. This issue is fixed in version 3.8.6.

### 45. CVE-2026-55680｜LabRedesCefetRJ / WeGIA
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T20:17:50.193)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T20:17:50.193 / 2026-10-14T20:17:50.310
- **官方描述（原文）**：WeGIA is a web manager for charitable institutions. Prior to 3.8.6, unauthenticated POST requests to web/html/socio/sistema/cadastro_cobranca.php can place a quoted SQL expression in the codigo parameter, which extract($_REQUEST) passes into the WHERE codigo= clause of an UPDATE statement without validation or parameter binding. Quoting the value bypasses MariaDB type conversion for the VARCHAR column and permits arbitrary SQL execution without a session. An attacker can read or modify database content, including user credential hashes and billing records in the cobrancas table. This issue is fixed in version 3.8.6.

### 46. CVE-2026-55573｜e107inc / e107
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:17:38.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:17:38.013 / 2026-10-14T18:17:38.013
- **官方描述（原文）**：e107 is a content management system (CMS). Prior to 2.3.7, install.php decodes the attacker-controlled previous_steps POST parameter and passes it to unserialize() at file scope and again in the e_install constructor without restricting allowed classes. The installer remains accessible after a normal installation, and a crafted object graph using the bundled GuzzleHttp\Psr7\PumpStream class can flow through paths.hash into site_path, where string coercion invokes an attacker-controlled callable. An unauthenticated attacker who can reach install.php can therefore execute arbitrary PHP functions with the web server process's privileges, leading to full server compromise. This issue is fixed in version 2.3.7.

### 47. CVE-2026-55572｜e107inc / e107
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:17:37.863)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:17:37.863 / 2026-10-14T18:17:37.863
- **官方描述（原文）**：e107 is a content management system (CMS). Prior to 2.3.7, the bundled alt_auth plugin's otherdb and e107db authentication backends interpolate the submitted login username directly into SQL in e107_plugins/alt_auth/otherdb_auth.php and e107_plugins/alt_auth/e107db_auth.php. The login() methods execute those strings with PDO::query() before effective sanitization, so an unauthenticated user can inject SQL when alt_auth is installed and either backend is configured with a live external database connection. The injection can expose or modify data available to the configured database account, and query failures can additionally disclose the generated query through the debug-message path. This issue is fixed in version 2.3.7.

### 48. CVE-2026-33796｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:28.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:28.320 / 2026-10-15T04:18:23.750
- **官方描述（原文）**：A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evolved allows a configured external BGP neighbor to execute arbitrary commands with root privileges via BMP route monitoring.

### 49. CVE-2026-33792｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:27.933)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:27.933 / 2026-10-15T04:18:23.583
- **官方描述（原文）**：A Stack-based Buffer Overflow vulnerability in the srxpfe process of Juniper Networks Junos OS on SRX Series allows an unauthenticated network attacker to execute code as root or cause a denial of service via a crafted packet received on a configured GRE tunnel.

### 50. CVE-2026-33789｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:27.763)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:27.763 / 2026-10-15T04:18:23.400
- **官方描述（原文）**：A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evolved allows an unauthenticated BGP peer to cause a denial of service and potential root-level command execution via crafted BGP route updates when the BGP Monitoring Protocol (BMP) is enabled.

### 51. CVE-2026-16741｜TR7 Cyber ​​Defense Inc. / TR7 ASP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T13:17:28.103)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T13:17:28.103 / 2026-10-14T14:17:44.627
- **官方描述（原文）**：Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in TR7 Cyber ​​Defense Inc. TR7 ASP on virtual appliance and TR7 Cyber ​​Defense Inc. TR7 ASP on physical appliance allows OS Command Injection. This issue affects TR7 ASP: from 1.0.40.236 before 1.0.1554.2331; TR7 ASP: from 1.6.42.239 before 1.6.1554.2331.

### 52. CVE-2026-16740｜TR7 Cyber ​​Defense Inc. / TR7 ASP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T13:17:27.977)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T13:17:27.977 / 2026-10-14T14:17:44.427
- **官方描述（原文）**：Missing authentication for critical function vulnerability in TR7 Cyber ​​Defense Inc. TR7 ASP on virtual appliance and TR7 Cyber ​​Defense Inc. TR7 ASP on physical appliance allows OS Command Injection. This issue affects TR7 ASP: from 1.0.40.236 before 1.0.1554.2331; TR7 ASP: from 1.6.42.239 before 1.6.1554.2331.

### 53. CVE-2026-15176｜F5 / NGINX Plus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:19.140)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:19.140 / 2026-10-15T04:18:23.203
- **官方描述（原文）**：A vulnerability exists in NGINX Plus and NGINX Open Source when a location is configured that uses the alias directive together with rewrite and a set or return directive referencing the $request_filename variable. Alternatively, the same result could be achieved when the $request_filename variable is used in an access log format directive. An unauthenticated attacker along with conditions beyond their control can exploit this vulnerability by sending crafted HTTP requests. This may cause a heap buffer overflow in the NGINX worker process leading to a restart. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. Impact: This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or to possibly trigger a code execution. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

### 54. CVE-2026-14851｜Copart / Copart’s online billing service
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T09:17:22.437)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00332 / percentile=0.24767
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T09:17:22.437 / 2026-10-14T15:17:18.930
- **官方描述（原文）**：A vulnerability relating to the exposure of confidential information in the customer invoicing web application, which exposes personally identifiable information (PII) and financial data – including customer names, addresses, invoice numbers, payment details and tax information – to unauthorised individuals. The issue is caused by a lack of authorisation checks at the endpoint responsible for serving PDF invoice files. Furthermore, some URLs for invoicing documents appear to be publicly accessible via search engines, exposing paths to confidential files. Successful exploitation of this vulnerability could allow an attacker to access data to which they should not have access, as well as to predict identifiers in order to access even more confidential information.

### 55. CVE-2026-110911｜Wheels / Wheels
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T04:18:22.813)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T04:18:22.813 / 2026-10-15T04:18:22.813
- **官方描述（原文）**：Wheels 1.1.8 through 4.1.1 allows SQL injection when caller-supplied quoted values are parsed again as SQL by dynamic finders (such as findOneByEmail), the query builder's where(property, value) and where(property, operator, value), string/UUID-key lookup paths (findByKey, updateByKey, deleteByKey and findOrCreateBy...), and validatesUniquenessOf. The parser incorrectly treats a doubled single quote as the end of a literal. Applications passing request data to these APIs can expose authentication, password-reset or token lookups, and data to unauthorized access; numeric-column values are not affected. There is a similar concern for query-builder whereBetween() in 4.0.0 through 4.1.1: string/date bounds can alter SQL on MySQL/MariaDB with backslash escaping enabled. This is fixed in 4.1.2.

### 56. CVE-2026-110867｜renovatebot / renovate
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T23:17:28.397)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T23:17:28.397 / 2026-10-14T23:17:28.397
- **官方描述（原文）**：Renovate before 44.60.1 contains an allowlist bypass vulnerability that allows repositories to set restricted environment variables by placing env inside a shared preset. Attackers controlling an externally sourced preset can override variables like PATH, LD_PRELOAD, NODE_OPTIONS, or GIT_SSL_CAINFO in child processes on self-hosted instances.

### 57. CVE-2026-110864｜better-auth / better-auth
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T23:17:27.970)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T23:17:27.970 / 2026-10-14T23:17:27.970
- **官方描述（原文）**：Better Auth from 1.5.0-beta.12 before 1.7.7 contains an authentication bypass vulnerability in the OAuth Proxy plugin that allows unauthenticated attackers to sign in as other users by forging encrypted profiles. When the proxy shares the global secret and cookie-stored state is used, attackers can obtain encrypted state for a fake profile with a victim's verified email to take over the account via implicit linking.

### 58. CVE-2026-110862｜better-auth / better-auth
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T23:17:27.673)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T23:17:27.673 / 2026-10-14T23:17:27.673
- **官方描述（原文）**：Better Auth from 1.4.0-beta.18 before 1.7.7 contains an authentication bypass vulnerability that allows unauthenticated attackers to sign in as other users by reusing OAuth state values as Magic Link tokens. Attackers can start an OAuth sign-in with a victim's email and submit the returned state to Magic Link verification, gaining sessions or creating falsely email-verified accounts.

### 59. CVE-2026-110858｜gitpython-developers / GitPython
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T23:17:27.043)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T23:17:27.043 / 2026-10-14T23:17:27.043
- **官方描述（原文）**：GitPython from 3.1.30 before 3.2.0 contains a remote code execution vulnerability in Remote.pull() whose unsafe-option guard inspects only keyword arguments, not the positional refspec. Attackers controlling the refspec can supply --upload-pack=<command> to execute OS commands as the calling process over local-path or SSH transports.

### 60. CVE-2026-110770｜databasus / databasus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:13.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:13.077 / 2026-10-14T19:17:13.077
- **官方描述（原文）**：Databasus 3.7.0 through 3.61.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to brute-force password reset codes via POST /api/v1/users/reset-password. Attackers can request a six-digit code for a known email, then guess it without rate limiting, lockout, or invalidation to take over accounts, including administrators.

### 61. CVE-2026-110649｜shahkashani / stills
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:18.650)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:18.650 / 2026-10-14T18:17:35.793
- **官方描述（原文）**：Stills before 25.24.2 contains an OS command injection vulnerability that allows attackers to execute shell commands by supplying crafted media file paths. Attackers can name a media file with $(...) or backticks to execute operating system commands with Node.js process privileges when ffmpeg, ffprobe, gifsicle, or convert runs.

### 62. CVE-2026-110646｜beganovich / snappdf
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:18.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:18.237 / 2026-10-14T15:17:18.237
- **官方描述（原文）**：Beganovich snappdf from 1.1.0 before 6.1.0 contains an OS command injection vulnerability on Windows that allows attackers to run commands by influencing the rendered URL. Attackers can supply cmd.exe metacharacters such as & in the setUrl() value, which executeOnWindows() passes unescaped to PHP exec(), executing commands as the PHP process.

### 63. CVE-2026-110644｜ChetanXpro / nodejs-whisper
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:17.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:17.940 / 2026-10-14T18:17:35.667
- **官方描述（原文）**：nodejs-whisper through 0.3.1 contains an OS command injection vulnerability in convertToWavType() that allows attackers to execute commands by supplying crafted audio file paths. Attackers can provide file names containing $() command substitution or closing quotes, which are interpolated into an ffmpeg command run via shelljs exec(), executing OS commands with Node.js process privileges.

### 64. CVE-2026-110643｜kky-ykk / transcribe2texts
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:17.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:17.790 / 2026-10-14T15:17:17.790
- **官方描述（原文）**：transcribe2texts through 1.0.6 contains an OS command injection vulnerability that allows attackers to execute commands by supplying crafted audioPath values to transcribeAudio(). Attackers can inject $() or backtick substitution or a closing quote into the unescaped path passed to child_process.exec() to run commands with Node.js process privileges.

### 65. CVE-2026-110640｜ariym / whisper-node
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:17.277)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:17.277 / 2026-10-14T15:17:17.277
- **官方描述（原文）**：Whisper-node through 1.1.1 contains an OS command injection vulnerability that allows attackers to execute commands by supplying crafted filePath or whisperOptions.language values to whisper(). Attackers can inject shell metacharacters or $() substitution into the command string built by createCppCommand() and run via shelljs exec() to execute commands with Node.js process privileges.

### 66. CVE-2026-110639｜mborne / @mborne/extract
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:17.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:17.130 / 2026-10-14T18:17:35.547
- **官方描述（原文）**：@mborne/extract before 0.2.1 contains an OS command injection vulnerability that allows attackers to execute commands by supplying shell metacharacters in archivePath or targetDir options. Attackers controlling these values passed to extract() can inject commands into unquoted shelljs exec() strings in the unzip, 7z, tar-bz2 and gz extractors, running them with Node.js process privileges.

### 67. CVE-2026-110638｜zepspaiva / doc-recog
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:16.997)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:16.997 / 2026-10-14T15:17:16.997
- **官方描述（原文）**：doc-recog through 1.1.6 contains an OS command injection vulnerability that allows attackers to execute commands by supplying crafted document paths to recog() or tag(). Attackers can embed $(...) or backtick command substitution in the file path, which DocData._readPDF passes to a shell-based pdftotext exec call, running commands with Node.js process privileges.

### 68. CVE-2026-110636｜revolunet / pypdftk
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:16.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:16.710 / 2026-10-14T15:17:16.710
- **官方描述（原文）**：pypdftk through 0.5 contains an OS command injection vulnerability in fill_form(), dump_data_fields(), and pdftk_cmd_util() that builds shell commands from caller-supplied paths. Attackers controlling pdf_path or out_file can inject shell metacharacters interpreted by subprocess.Popen with shell=True to execute OS commands as the Python process.

### 69. CVE-2026-110635｜scionoftech / webp-converter
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:16.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:16.560 / 2026-10-14T15:17:16.560
- **官方描述（原文）**：webp-converter before 3.0.0 contains an OS command injection vulnerability in src/webpconverter.js helpers that run libwebp binaries via execFile with shell enabled. Attackers controlling file names or option strings passed to cwebp, dwebp, gwebp, or webpmux functions can inject shell metacharacters to execute OS commands as the Node.js process.

### 70. CVE-2026-110634｜danday74 / git-diff
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:16.417)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:16.417 / 2026-10-14T18:17:35.423
- **官方描述（原文）**：git-diff before 2.0.7 contains an OS command injection vulnerability that allows attackers to execute shell commands by supplying crafted strings to the gitDiff API. Attackers who control a diffed document string can embed $(cmd) or backtick substitutions that shelljs.exec evaluates, running commands with Node.js process privileges.

### 71. CVE-2026-110631｜moghtech / komodo
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:15.983)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:15.983 / 2026-10-14T16:17:41.960
- **官方描述（原文）**：Komodo through 2.3.3 contains an authentication bypass vulnerability in the Periphery agent that allows unauthenticated attackers to connect as a trusted Core because empty core_public_keys and passkeys lists fail open by default. Attackers reaching port 8120 can present any generated keypair to issue Periphery API requests, including terminal sessions and container operations, executing commands on managed hosts typically as root.

### 72. CVE-2026-110628｜kanbn / kan
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:15.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:15.540 / 2026-10-14T15:17:15.653
- **官方描述（原文）**：Kan 0.5.5 through 0.6.0 contains an unauthenticated server-side request forgery vulnerability in the /api/download/attatchment route due to an incomplete fix for CVE-2026-32255. When S3_ENDPOINT is unset, attackers can pass arbitrary url query parameters to fetch() to read internal services, localhost ports, and cloud instance metadata.

### 73. CVE-2026-110616｜nullclaw / NullHub
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:13.767)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:13.767 / 2026-10-14T15:17:13.767
- **官方描述（原文）**：NullHub through 2026.5.29 contains a missing authentication vulnerability that allows unauthenticated attackers to access the /api/* management API because the auth_token field defaults to null and is never assigned. Attackers sending requests without Authorization or Origin headers to non-loopback listeners can control agent instances, rewrite configurations including provider credentials, and manage cron jobs and MCP servers.

### 74. CVE-2026-110536｜D-Link / DIR-868L
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:10.610)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:10.610 / 2026-10-14T19:17:10.610
- **官方描述（原文）**：A vulnerability was determined in D-Link DIR-868L 2.01b05. This impacts the function system of the file /htdocs/cgibin of the component HNAP CGI Handler. Executing a manipulation of the argument SOAPACTION can lead to os command injection. The attack may be launched remotely. The exploit has been publicly disclosed and may be utilized.

### 75. CVE-2026-109439｜LANTRONIX / XPress-DR
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:23.253)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:23.253 / 2026-10-14T17:18:23.253
- **官方描述（原文）**：Lantronix XPress-DR and XPress-DR-I (CoBos-family) firmware through 8.1.0.0 contains a missing authentication vulnerability that allows remote attackers to read and persistently overwrite device configuration by sending crafted frames to the unauthenticated UDP configuration protocol on port 30718. Attackers can send a type 0xF8 query to read live configuration data and a type 0xFD frame with exactly 0x78 body bytes to rewrite the device IP address and serial-channel forwarding records, causing changes to commit to EEPROM and persist across reboots. The XPress-DR product series reached end-of-life/end-of-support in February 2025.

### 76. CVE-2026-108587｜10web / 10Web Booster – Website speed optimization, Cache & Page Speed optimizer
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-15T05:17:02.637)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-15T05:17:02.637 / 2026-10-15T05:17:02.637
- **官方描述（原文）**：The 10Web Booster – Website speed optimization, Cache & Page Speed optimizer plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 2.34.10 via the compressCustom function. This is due to missing file type validation and extension filtering on the page_id parameter, combined with a world-readable leaked nonce that bypasses authentication checks. This makes it possible for unauthenticated attackers to upload files that may be executable, which makes remote code execution possible. This exploit chain requires obtaining the plugin's REST nonce (tenwebio_rest), which is automatically serialized to a world-readable file under wp-content/uploads/ whenever a bulk optimisation batch pauses; because the nonce is generated in a cron/loopback context with a user ID of 0, it is valid for unauthenticated visitors.

### 77. CVE-2026-108336｜Hitachi Vantara / Remot Ops Agent
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T22:17:22.433)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T22:17:22.433 / 2026-10-14T22:17:22.433
- **官方描述（原文）**：When the default self-signed certificate is used, an attacker could gain administrative access to the application. The SSL certificate for the web interface is used to sign JWT access tokens that are used to validate that the user is logged in. When the default SSL certificate is used, an attacker could have the capability to sign JWT access tokens and bypass login. An attacker could gain administrative access to the application and perform actions like configuring the service or requesting log collection. Device credentials and customer data cannot be accessed with this vulnerability.

### 78. CVE-2026-108335｜Hitachi Vantara / Remote Ops Agent
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T22:17:22.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T22:17:22.290 / 2026-10-14T22:17:22.290
- **官方描述（原文）**：When the password reset functionality is enabled, and email is configured, an attacker could take over any account using a brute-force attack. There is no rate limiting on the attempts to enter the reset code, leading to the possibility of a brute force solution to the password reset challenge. An attacker could gain administrative access to the application and perform actions like configuring the service or requesting log collection. Device credentials and customer data cannot be accessed with this vulnerability.

### 79. CVE-2026-108291｜itthinx / Affiliates
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T13:17:24.633)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T13:17:24.633 / 2026-10-14T14:26:59.367
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in itthinx Affiliates affiliates allows Object Injection.This issue affects Affiliates: from n/a through 7.0.1.

### 80. CVE-2026-108065｜Channel Software / WebAlliance eCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T14:17:33.813)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T14:17:33.813 / 2026-10-14T14:17:33.813
- **官方描述（原文）**：SQL Injection (CWE-89) in the SOAP GetUser method of the /preapproval.asmx endpoint in Channel Software WebAlliance eCommerce [VERSION — missing] allows an unauthenticated remote attacker to read, write, and potentially execute commands on the backend Microsoft SQL Server via a crafted sUserID parameter value containing a single quote and stacked SQL query.

### 81. CVE-2026-107594｜Unknown / File Upload to Order
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T07:17:02.090)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.0019 / percentile=0.08099
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T07:17:02.090 / 2026-10-14T16:14:02.800
- **官方描述（原文）**：The File Upload to Order WordPress plugin before 1.1.4 does not validate or confine a file path taken from attacker-controlled session data before deleting the file, and the action that performs the deletion is reachable by unauthenticated users, allowing them to delete arbitrary files on the server, including files whose removal leads to full site compromise.

### 82. CVE-2026-107424｜M A Vinoth Kumar / Frontend Dashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T13:17:23.453)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T13:17:23.453 / 2026-10-14T14:26:59.367
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in M A Vinoth Kumar Frontend Dashboard frontend-dashboard allows Privilege Escalation.This issue affects Frontend Dashboard: from n/a through 3.0.7.

### 83. CVE-2026-104748｜wpazleen / SimpleForm – Form Maker to Chat Apps with Quiz, Poll and Multi Lead Notifications
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T08:17:02.997)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00646 / percentile=0.49779
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T08:17:02.997 / 2026-10-14T14:26:59.367
- **官方描述（原文）**：The SimpleForm – Form Maker to Chat Apps with Quiz, Poll and Multi Lead Notifications plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 3.10.0 This is due to the `wp_ajax_nopriv_simpleform_wp_register` AJAX action lacking any capability check for role assignment and the `save_custom_fields_to_user_meta()` function using an exclusion list that omits `wp_capabilities`, combined with `get_form_settings()` returning a hard-coded defaults array that unconditionally enables meta writing regardless of the supplied `form_id`. This makes it possible for unauthenticated attackers to create a new Administrator-level WordPress account by supplying `wp_capabilities[administrator]=1` alongside standard registration fields. The nonce required by the endpoint is publicly emitted into the `front_end_data` JavaScript object on every front-end page via `wp_enqueue_scripts`, making it trivially obtainable by any unauthenticated visitor before submitting the malicious request.

### 84. CVE-2026-103415｜Eclipse Foundation / NetX Duo
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:17:19.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:17:19.790 / 2026-10-14T18:17:19.790
- **官方描述（原文）**：When a TLS 1.3 client processes a HelloRetryRequest, it copies the server's cookie into its second ClientHello without checking that the cookie fits in the outgoing packet. Both the length and the contents of that cookie come from the peer, and the write happens before certificate authentication completes, so a malicious or compromised server can overwrite memory past the caller supplied TLS packet buffer without presenting a certificate. Only the client path is affected.

### 85. CVE-2026-102893｜zulip / zulip
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:29.987)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:29.987 / 2026-10-14T16:17:29.987
- **官方描述（原文）**：Zulip is an open-source team collaboration tool. In Zulip Server versions through 12.1, GenericOpenIdConnectBackend matches the identity provider email claim to an active account's delivery_email without rejecting an explicitly false email_verified claim. If a configured identity provider returns an email address that the authenticating user does not control together with email_verified=false, Zulip can log the user into the existing account for that address. Exploitation requires a misconfigured trusted identity provider, and deployments whose authoritative identity provider only emits email addresses controlled by the authenticating user are not affected. This issue is fixed in version 12.2.

### 86. CVE-2026-102748｜dgraph-io / dgraph
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:05.700)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:05.700 / 2026-10-14T19:17:05.813
- **官方描述（原文）**：Dgraph is an open source distributed GraphQL database. Prior to 25.4.0, Dgraph Zero registers administrative HTTP routes on port 6080 without authentication when the administrative interface is enabled. The /removeNode route accepts attacker-controlled id and group values and passes them to Server.RemoveNode, where group 0 can trigger ProposePeerRemoval. A remote unauthenticated attacker who can reach the Zero HTTP port can read topology through /state, allocate identifiers through /assign, access the exposed /moveTablet administrative route, or remove membership through /removeNode, disrupting the Zero control plane and destabilizing Alpha nodes that depend on Zero. The route registration occurs in dgraph/cmd/zero/run.go, and the demonstrated membership-removal path reaches Server.RemoveNode and ProposePeerRemoval. This issue is fixed in version 25.4.0.

### 87. CVE-2026-102476｜Eclipse Foundation / Eclipse Vert.x
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:17:17.503)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:17:17.503 / 2026-10-14T18:17:17.503
- **官方描述（原文）**：In Eclipse Vert.x versions [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the Vert.x HTTP client relies on an SSL context for efficiency purpose, the key of this cache should reflect entirely the SSL semantics of the desired SSL properties. It is possible for a client to ask for an SSL context and obtain an SSL context with weaker properties, for instance a context with hostname validation and obtain a context ignoring hostname validation. The impacted component is io.vertx:vertx-core.

### 88. CVE-2026-102182｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:06.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:06.080 / 2026-10-15T04:18:11.730
- **官方描述（原文）**：A Stack-based Buffer Overflow vulnerability in the kmd component of Juniper Networks Junos OS on MX Series allows an unauthenticated network attacker to execute code as root via specific IKE certificate-based packets. This issue affects Junos OS on MX Series: * All versions before 21.2R3-S11; * from 21.4 before 21.4R3-S12; * from 22.2 before 22.2R3-S8; * from 22.3 before 22.3R3-S5; * from 22.4 before 22.4R3-S9;

### 89. CVE-2026-102178｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:05.610)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:05.610 / 2026-10-14T17:18:05.610
- **官方描述（原文）**：A Stack-based Buffer Overflow vulnerability in the BGP routing daemon of Juniper Networks Junos OS and Junos OS Evolved allows a configured BGP flowspec peer to cause routing-engine compromise or a routing-daemon denial of service via flowspec route re-advertisement when BGP update-threading is enabled.

### 90. CVE-2026-102175｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:05.147)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:05.147 / 2026-10-14T17:18:05.147
- **官方描述（原文）**：A Heap-based Buffer Overflow vulnerability in the sdxd service-deployment daemon of Juniper Networks Junos OS and Junos OS Evolved allows a remote unauthenticated attacker who can control or intercept the configured SDX/SRC server connection to execute code as root or cause denial of service via a crafted frame received over the service-deployment TCP connection.

### 91. CVE-2026-102084｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:04.310)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:04.310 / 2026-10-15T04:18:11.560
- **官方描述（原文）**：An Improper Validation of Syntactic Correctness of Input vulnerability in the VPN daemon of Juniper Networks Junos OS on SRX Series allows an authenticated, network-based attacker to take complete control of the device. If an SRX device configured for AutoDiscovery VPN (ADVPN) receives a message from a peer that contains one or more specifically malformed attributes, this will cause a buffer overflow, which can allow remote code execution and therefore allow an attacker to take complete control of the device. To be able to carry out this attack an attacker must either have acquired the shared secret to impersonate a peer or have compromised an existing one, so this attack is considerably difficult. This issue affects Junos OS on SRX Series: * All versions before 23.2R2-S7.7; * from 23.4 before 23.4R2-S7; * from 24.2 before 24.2R2-S4; * from 24.4 before 24.4R2-S3; * from 25.2 before 25.2R2; * from 25.4 before 25.4R1-S3.

### 92. CVE-2026-102070｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:02.953)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:02.953 / 2026-10-14T21:17:31.687
- **官方描述（原文）**：A Reachable Assertion vulnerability in the Two-Way Active Measurement Protocol (TWAMP) client of Juniper Networks Junos OS allows an unauthenticated network-based attacker to cause rmopd service disruption via a specific TCP packet.

### 93. CVE-2026-102068｜Juniper Networks / Junos OS Evolved
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:02.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:02.647 / 2026-10-14T21:17:31.417
- **官方描述（原文）**：A Stack-based Buffer Overflow vulnerability in the kernel of Juniper Networks Junos OS Evolved allows an unauthenticated remote attacker to trigger a kernel panic via a crafted TCP packet when key-chain authentication is used for BGP or LDP.

### 94. CVE-2026-102062｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:18:01.737)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:18:01.737 / 2026-10-15T04:18:10.807
- **官方描述（原文）**：An Use of Externally-Controlled Format String vulnerability in the ipfd daemon of Juniper Networks Junos OS on SRX Series allows an unauthenticated network-based attacker to execute code with root privileges via a compromised or impersonated configured HTTPS feed server.

### 95. CVE-2026-102037｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:17:57.867)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:17:57.867 / 2026-10-14T17:17:57.867
- **官方描述（原文）**：An XML Injection vulnerability in the Unified Threat Management daemon (utmd) of Juniper Networks Junos OS on SRX Series devices allows an unauthenticated network attacker to commit arbitrary device configuration with root privileges via a malicious response from a configured custom URL-feed server.

### 96. CVE-2026-102031｜Juniper Networks / Junos OS Evolved
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:17:56.617)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:17:56.617 / 2026-10-14T17:17:56.617
- **官方描述（原文）**：An OS Command Injection vulnerability in TACACS of Juniper Networks Junos OS Evolved allows a low-privileged TACACS+-authenticated user to execute commands with root privileges when periodic TACACS+ authorization-refresh is enabled.

### 97. CVE-2026-101997｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:17:52.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:17:52.740 / 2026-10-14T17:17:52.740
- **官方描述（原文）**：An Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in ipfd of Juniper Networks Junos OS on SRX Series allows an unauthenticated network-based attacker to execute code with root privileges via a configured Security Intelligence feed connection.

### 98. CVE-2026-101990｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:17:51.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:17:51.587 / 2026-10-14T17:17:51.587
- **官方描述（原文）**：A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evolved allows a remote configured BGP peer to cause an rpd crash, or on Junos OS remote code-execution, via sending a flow-spec update which is selected for re-advertisement.

### 99. CVE-2026-101986｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:17:50.953)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:17:50.953 / 2026-10-15T04:18:10.627
- **官方描述（原文）**：An Improper Authentication vulnerability in J-Web of Juniper Networks Junos OS and Junos OS Evolved allows an unauthenticated network attacker to bypass J-Web authentication and execute CGI content with elevated privileges via a crafted HTTP request.

### 100. CVE-2026-101983｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:17:13.293)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:17:13.293 / 2026-10-15T04:18:10.453
- **官方描述（原文）**：A Stack-based Buffer Overflow vulnerability in the httpd process of Juniper Networks Junos OS and Junos OS Evolved allows an unauthenticated network attacker to cause remote code execution and denial of service via a J-Web virtual-domain configured.

### 101. CVE-2026-101982｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:17:13.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:17:13.120 / 2026-10-14T18:17:13.120
- **官方描述（原文）**：A Stack-based Buffer Overflow vulnerability in the routing protocol daemon (rpd) of Juniper Networks Junos OS and Junos OS Evolved allows a configured BGP/EVPN peer to cause root code execution on Junos OS or an rpd crash on Junos OS Evolved via protocol-valid route advertisements for an EVPN-VPWS service.

### 102. CVE-2026-101980｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:17:50.503)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:17:50.503 / 2026-10-14T21:17:24.973
- **官方描述（原文）**：An Integer Underflow vulnerability in the kernel of Juniper Networks Junos OS with Extended Echo configured allows an unauthenticated, network-based attacker to cause a denial of service by a kernel crash.

### 103. CVE-2026-101967｜Juniper Networks / Junos OS Evolved
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:17:49.100)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:17:49.100 / 2026-10-15T04:18:10.040
- **官方描述（原文）**：An OS Command Injection vulnerability in the bootzd zero-touch provisioning daemon of Juniper Networks Junos OS Evolved allows an unauthenticated attacker on the management LAN to execute commands as root via crafted DHCP response.

### 104. CVE-2026-101956｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:17:48.353)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:17:48.353 / 2026-10-15T04:18:09.493
- **官方描述（原文）**：An Improper Authentication vulnerability in the J-Web web management component of Juniper Networks Junos OS allows an unauthenticated remote attacker to execute arbitrary Junos commands with root privileges via the exposed J-Web web interface.

### 105. CVE-2026-101955｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:17:48.200)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:17:48.200 / 2026-10-14T17:17:48.200
- **官方描述（原文）**：A Stack-based Buffer Overflow vulnerability in the UTM Anti-Spam SBL of Juniper Networks Junos OS on SRX series allows an unauthenticated remote attacker to cause arbitrary code execution or a denial of service via a injected malformed DNS packet when Anti-Spam SBL inspection is enabled.

### 106. CVE-2026-101954｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:17:11.277)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:17:11.277 / 2026-10-14T18:17:11.277
- **官方描述（原文）**：An Improper Authentication vulnerability in the J-Web management interface and its NETCONF session handling of Juniper Networks Junos OS and Junos OS Evolved allows an unauthenticated network attacker to obtain root-level device configuration access and take over the device via a reachable J-Web HTTP or HTTPS service when web management is enabled.

### 107. CVE-2026-101950｜Juniper Networks / Junos OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T17:17:47.877)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T17:17:47.877 / 2026-10-14T17:17:47.877
- **官方描述（原文）**：A Heap-based Buffer Overflow vulnerability in the SVR component of Juniper Networks Junos OS on SRX Series allows an unauthenticated network attacker to cause a denial of service and potentially compromise confidentiality and integrity via malformed IPv4 packets reaching an interface configured for Secure Vector Routing.

### 108. CVE-2020-37282｜vworld4u / office-converter
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:16:59.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:16:59.520 / 2026-10-14T15:16:59.520
- **官方描述（原文）**：office-converter through 1.0.2 contains an OS command injection vulnerability that allows attackers to execute commands by supplying a crafted fileName to generatePdf() or generateHtml(). Attackers can embed $(...), backticks, or a closing quote with shell metacharacters in the file name, which is concatenated into an unoconv command run via child_process.exec(), executing commands with Node.js process privileges.

### 109. CVE-2020-37281｜Gravitee / Gravitee API Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:16:59.370)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:16:59.370 / 2026-10-14T17:17:34.023
- **官方描述（原文）**：Gravitee API Management through 4.12.22 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to impersonate any user by forging JWTs signed with the shipped default jwt.secret. Attackers knowing an existing user ID can sign an HS256 token with that subject and present it as a bearer token to the Management API, impersonating administrators to gain full platform control.

### 110. CVE-2026-92156｜nasa / fprime
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T18:19:34.920)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T18:19:34.920 / 2026-10-14T18:19:34.920
- **官方描述（原文）**：F´ (F Prime) is a framework that enables development and deployment of spaceflight and other embedded software applications. Prior to 4.3.0, Svc::EventManager loqQueue_internalInterfaceHandler packetization is vulnerable because EventManager accepts up to the framework LogBuffer maximum, but packet descriptor, event identifier, and time-tag metadata consume part of the larger ComBuffer and leave a smaller remaining budget for log arguments; serialization failure then reaches an assertion. When a deployment bridges events through GenericHub into EventManager and forwards a legal Fw::LogBuffer larger than EventManager remaining log-argument budget, under standard F Prime assertion handling, a legal bridged event payload aborts or resets the process, causing denial of service. This issue is fixed in version 4.3.0.

### 111. CVE-2026-62858｜YOURLS / YOURLS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:47.617)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:47.617 / 2026-10-14T18:17:38.607
- **官方描述（原文）**：YOURLS is a self-hosted, customizable URL shortener written in PHP. Prior to 1.10.5, yourls_get_request() extracted the request path without sanitization, after which yourls_sanitize_url() and yourls_esc_url() preserved dot and slash traversal sequences before an attacker-controlled keyword reached file_exists() and include() under YOURLS_PAGEDIR. An unauthenticated remote attacker could traverse outside the intended pages directory and include a local PHP file that was already present on the server, such as an uploaded or injected file, causing the file to execute in the YOURLS web process. This issue is fixed in version 1.10.5.

### 112. CVE-2026-25946｜Gitea / Gitea
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:19.393)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:19.393 / 2026-10-14T16:17:45.377
- **官方描述（原文）**：When OpenID sign-in is enabled, Gitea accepts a user-supplied OpenID URL and performs discovery requests without validating the destination against internal network addresses. An unauthenticated remote attacker can cause the server to contact loopback or private-network HTTP services. This can expose internal service behavior and enable interaction with resources that are not directly reachable by the attacker.

### 113. CVE-2026-110772｜we-promise / sure
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:13.353)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:13.353 / 2026-10-14T21:17:37.070
- **官方描述（原文）**：Sure 0.7.0 through 0.7.6-alpha.6 contains a missing authorization vulnerability in Transactions::BulkUpdatesController#create that allows family members to bypass account sharing permissions. Authenticated members with read_only or no share can submit arbitrary entry_ids to modify other members' transaction dates, names, notes, categories, merchants and tags, corrupting budgets and reports.

### 114. CVE-2026-110771｜Shopizer / Shopizer
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:13.210)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:13.210 / 2026-10-14T20:17:31.883
- **官方描述（原文）**：Shopizer through 3.2.5 contains an authorization bypass vulnerability that allows authenticated customers to post reviews as other customers by supplying a customerId field. Attackers can send crafted requests to POST /api/v1/auth/products/{id}/reviews to publish reviews and ratings attributed to other store customers, corrupting authorship and product ratings.

### 115. CVE-2026-110766｜colanode / colanode
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:12.460)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:12.460 / 2026-10-14T20:17:31.693
- **官方描述（原文）**：Colanode server through 0.4.7 contains a path traversal vulnerability that allows authenticated users to read arbitrary .jpeg files by supplying an encoded traversal sequence in avatarId. Attackers can send percent-encoded ../ sequences to GET /client/v1/avatars/:avatarId to escape the avatars directory and read .jpeg files belonging to other workspaces.

### 116. CVE-2026-110717｜meetecho / janus-gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:43.903)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:43.903 / 2026-10-14T18:17:36.223
- **官方描述（原文）**：Janus WebRTC Server through 1.4.3 contains a path traversal vulnerability in the Record&Play plugin that allows unauthenticated attackers to write files outside recordings_path via the record request filename. Attackers can supply filenames with path separators to create or truncate files ending in -audio.mjr, -video.mjr or -data.mjr anywhere the Janus process can write outside protected folders.

### 117. CVE-2026-110658｜freeswitch / sofia-sip
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:42.640)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:42.640 / 2026-10-14T20:17:30.733
- **官方描述（原文）**：Sofia-SIP through 1.13.18 contains a heap out-of-bounds read vulnerability in msg_multipart_parse() that allows unauthenticated remote attackers to crash the process by sending oversized MIME boundaries. Attackers can send an INVITE with a multipart Content-Type whose boundary exceeds the body length, causing memcmp to read past the heap buffer and crash the process.

### 118. CVE-2026-110657｜Khronos Group / nnef
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:42.500)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 4.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:42.500 / 2026-10-14T18:17:35.917
- **官方描述（原文）**：Khronos NNEF-Tools nnef through 1.0.10 and nnef-tools through 1.0.11 contain a path traversal vulnerability that allows attackers to write files outside the model directory via crafted variable labels. Attackers can supply a graph.nnef with '../' sequences or absolute paths in labels to create or overwrite '.dat' files when users convert, save, or generate weights.

### 119. CVE-2026-110625｜MacWarrior / clipbucket-v5
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:15.110)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:15.110 / 2026-10-14T21:17:35.573
- **官方描述（原文）**：ClipBucket v5 through 5.5.3-#206 contains a reflected cross-site scripting vulnerability in admin_area/flagged_item.php via the unencoded type GET parameter. Attackers can send crafted flagged_item.php?type= links to logged-in administrators or moderators to execute injected script in the admin panel origin.

### 120. CVE-2026-110619｜fatedier / frp
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:14.200)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:14.200 / 2026-10-14T17:18:25.920
- **官方描述（原文）**：frp 0.41.0 through 0.71.1 contains a missing authentication vulnerability that allows unauthenticated remote attackers to access pprof debug endpoints because handlers are registered on the root mux outside Basic Authentication. Attackers can query /debug/pprof/ endpoints on frps dashboard or frpc admin listeners to obtain cmdline, goroutine stacks, heap profiles, and trigger CPU profiling.

### 121. CVE-2026-110617｜rachelos / we-mp-rss
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:13.910)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:13.910 / 2026-10-14T18:17:34.920
- **官方描述（原文）**：we-mp-rss through 1.5.3 contains a missing authorization vulnerability in the /api/v1/wx/tools/export/download endpoint that allows unauthenticated attackers to download export archives because its authentication dependency is commented out. Attackers can supply an mp_id and guessable timestamp-based export filename to retrieve archives under data/docs, and set delete_after_download=true to delete them.

### 122. CVE-2026-110602｜kyz / libmspack
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:11.677)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:11.677 / 2026-10-14T18:17:34.547
- **官方描述（原文）**：libmspack through 0.11alpha contains an uninitialized pointer free vulnerability in kwajd_open() in mspack/kwajd.c that frees unzeroed filename and extra pointers on header read errors. Attackers can supply a truncated, empty, or wrong-signature KWAJ file to crash the process or obtain an arbitrary-free memory corruption primitive.

### 123. CVE-2026-110600｜brechtsanders / xlsxio
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:11.387)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:11.387 / 2026-10-14T21:17:35.453
- **官方描述（原文）**：xlsxio through 0.2.37 contains a NULL pointer dereference vulnerability in main_sheet_get_sheetfile_expat_callback_element_start() in lib/xlsxio_read.c that allows attackers to crash applications via crafted files. Attackers can supply a .xlsx file whose workbook.xml.rels contains a worksheet Relationship lacking an Id attribute, crashing the process when xlsxioread_sheet_open() is called.

### 124. CVE-2026-110599｜l-smash / l-smash
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:11.247)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:11.247 / 2026-10-14T17:18:25.453
- **官方描述（原文）**：L-SMASH through 2.14.5 contains a double free vulnerability in hevc_setup_first_summary() and h264_setup_first_summary() in importer/nalu_imp.c that frees borrowed codec-specific objects on error paths. Attackers can supply a crafted Annex-B elementary stream lacking a parseable SPS to lsmash_read_file() or the boxdumper, remuxer, or muxer tools, causing use-after-free, heap corruption, and crashes.

### 125. CVE-2026-110597｜syoyo / tinyexr
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:10.953)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:10.953 / 2026-10-14T18:17:34.423
- **官方描述（原文）**：Tinyexr through 3.2.0 contains a heap out-of-bounds read vulnerability in ParseEXRMultipartHeaderFromMemory() that allows attackers to read beyond buffers due to a stale remaining-size value. Attackers can supply a crafted multi-part EXR file whose later part headers bypass ReadAttribute() bounds checks, crashing applications or leaking adjacent heap memory into attribute values.

### 126. CVE-2026-110594｜MicroPyramid / BottleCRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:10.437)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:10.437 / 2026-10-14T17:18:25.330
- **官方描述（原文）**：BottleCRM 0.43 through 1.14.5 contains a regular expression denial of service vulnerability that allows authenticated organization administrators to block web workers via unbounded routing rule regex patterns. Attackers can create a routing rule with a catastrophically backtracking pattern evaluated by _match_condition() during case saves, exhausting workers shared across all tenants.

### 127. CVE-2026-110592｜MicroPyramid / BottleCRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:10.043)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:10.043 / 2026-10-14T18:17:34.303
- **官方描述（原文）**：BottleCRM 0.30 through 1.14.5 contains an HTML injection vulnerability in render_invoice_template() that allows authenticated organization members to inject markup into custom-template invoice PDFs. Attackers can place HTML and CSS in notes, terms, client name or address fields to overlay totals, payee and payment instructions in PDFs served via download, public links and emails.

### 128. CVE-2026-109971｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T10:17:53.440)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.7 (MEDIUM)
- **EPSS**：0.00126 / percentile=0.02077
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T10:17:53.440 / 2026-10-14T12:17:17.587
- **官方描述（原文）**：A flaw was found in the clevis PKCS#11 pin. The clevis-decrypt-pkcs11 script passes the PKCS#11 token PIN as a command-line argument to pkcs11-tool, making it visible to any local user through process listing or the /proc filesystem.

### 129. CVE-2026-103974｜lichess-org / lila
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:07.843)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:07.843 / 2026-10-14T20:17:29.167
- **官方描述（原文）**：lichess.org is the forever free, adless and open source chess server. Prior to commit c54596c9e1569d378fe20f80d4c790c6fdee54c4, a user who can add a chapter to a study can place attacker-controlled text in the PGN Annotator tag, which becomes Comment.Author.External and is returned verbatim by authorText. When a study node has at least two comments, ui/analyse/src/treeView/inlineView.ts interpolates that author string into HTML passed to the innerHTML hook without escaping it. Opening the affected study can therefore render stored attacker-controlled HTML and CSS for other viewers, including navigation to an attacker-controlled site, content spoofing, and CSS-based data exposure, although the site's content security policy blocks injected JavaScript. This vulnerability is fixed by commit c54596c9e1569d378fe20f80d4c790c6fdee54c4.

### 130. CVE-2026-102755｜dataease / dataease
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T19:17:05.857)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T19:17:05.857 / 2026-10-14T20:17:28.493
- **官方描述（原文）**：DataEase is an open source data visualization and analysis tool. Prior to 2.10.26, authenticated users with folder creation permission can store HTML-bearing names through datasource/createFolder or datasetTree/save. The datasource and dataset Move to dialogs in core/core-frontend/src/views/visualized/data/datasource/form/CreatDsGroup.vue and core/core-frontend/src/views/visualized/data/dataset/form/CreatDsGroup.vue read the stored name from a node title attribute and assign search-highlighted content to innerHTML. When another user opens a Move to dialog and types in its search box, attacker-controlled JavaScript can execute in the victim's DataEase session. This issue is fixed in version 2.10.26.

### 131. CVE-2016-20099｜l-smash / l-smash
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:16:58.003)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:16:58.003 / 2026-10-14T18:17:00.120
- **官方描述（原文）**：L-SMASH through 2.14.5 contains an infinite loop vulnerability in vc1_importer_probe() in importer/vc1_imp.c that allows attackers to hang applications via crafted input files. Attackers can supply a file consisting only of zero bytes, which lsmash_read_file() probes automatically, causing indefinite CPU consumption and denial of service.

### 132. CVE-2026-92392｜curl / curl
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T08:17:05.997)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：未確認
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T08:17:05.997 / 2026-10-15T04:18:29.190
- **官方描述（原文）**：During an upload, curl mishandles HTTP/2 `RST_STREAM` received from the server (with reason `HTTP_1_1_REQUIRED` or `REFUSED_STREAM`) leading to a use after free of a `struct Curl_easy` object.

### 133. CVE-2026-110655｜miniupnp project / miniupnpc
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T16:17:42.217)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T16:17:42.217 / 2026-10-14T19:17:11.257
- **官方描述（原文）**：miniupnpc through 2.3.3 contains a one-byte heap out-of-bounds read vulnerability in the minixml parseatt function that allows malicious UPnP gateways to read past buffer bounds via crafted replies. Attackers on the local network can spoof a gateway serving device descriptions or SOAP responses ending in '=' to crash the client.

### 134. CVE-2026-110627｜MacWarrior / clipbucket-v5
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:15.400)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:15.400 / 2026-10-14T18:17:35.167
- **官方描述（原文）**：ClipBucket v5 through 5.5.3-#206 contains a reflected cross-site scripting vulnerability in admin_area/index.php that allows attackers to inject HTML via the val parameter in mode=add_todo. Attackers can lure a logged-in administrator into submitting a cross-site POST form without CSRF protection, executing script in the admin panel origin.

### 135. CVE-2026-110604｜Michael R Sweet / Mini-XML
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-14T15:17:11.967)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-14T15:17:11.967 / 2026-10-14T17:18:25.567
- **官方描述（原文）**：Mini-XML 4.0.0 through 4.0.6 contains an off-by-one stack out-of-bounds write in mxml_strtod() when the locale decimal point is not '.'. Attackers can supply XML with a 63-digit REAL value followed by '.' to write a NUL byte past the 64-byte stack buffer, corrupting stack memory or crashing the process.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-76519｜Cisco / Secure Email Gateway
- **Title**：Cisco Secure Email Gateway Relative Path Traversal Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Secure Email Gateway contains a relative path traversal vulnerability that could allow an unauthenticated, remote attacker to write arbitrary files on the underlying operating system.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-105134｜Ahsay / AhsayCBS
- **Title**：Ahsay AhsayCBS Command Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.01843 / percentile=0.78594
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ahsay AhsayCBS contains a command injection vulnerability that could allow a remote attacker to execute operating system commands via manipulation of the random parameter in the Replication Receiver component’s /rps/api/json/UpdateReceivers.do endpoint. This vulnerability can be chained with CVE-2026-105133.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-0322｜Palo Alto Networks / PAN-OS
- **Title**：Palo Alto Networks PAN-OS Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Palo Alto Networks PAN-OS contains a code injection vulnerability that could allow an authenticated attacker with network access to execute arbitrary code with root privileges on the firewall.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-105133｜Ahsay / AhsayCBS
- **Title**：Ahsay AhsayCBS Improper Authentication Vulnerability
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00383 / percentile=0.30672
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ahsay AhsayCBS contains an improper authentication vulnerability that could allow a remote attacker to bypass authentication via manipulation of the random parameter in the API component’s checkSysPwd function. This vulnerability can be chained with CVE-2026-105134.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-77371 | P3 / 38 | getredash / redash | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110650 | P3 / 38 | anshulkharb / thumbnail | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110645 | P3 / 38 | ArsalanDotMe / video-stitch | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110632 | P3 / 38 | Report One / MyReport Updater | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110612 | P3 / 38 | wwwlike / vlife | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-108390 | P3 / 38 | hestiacp / hestiacp | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-65198 | WATCH / 20 | Huawei / openUBMC | v3.1 8.6 (HIGH) | 0.00189 / percentile=0.07967 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93748 | WATCH / 12 | kornelski / http-cache-semantics | v4.0 8.7 (HIGH) | 0.00569 / percentile=0.45808 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93687 | WATCH / 12 | micromatch / braces | v4.0 8.7 (HIGH) | 0.00757 / percentile=0.54161 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-65199 | WATCH / 12 | Huawei / openBMC | v3.1 5.4 (MEDIUM) | 0.0015 / percentile=0.03774 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-65200 | WATCH / 8 | Huawei / openBMC | v3.1 3.5 (LOW) | 0.00143 / percentile=0.0317 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-65197 | WATCH / 8 | H3C / HDM Family-A G5 | v3.1 3.1 (LOW) | 0.00098 / percentile=0.00739 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-73252 | WATCH / 30 | cesanta / mongoose | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55386 | WATCH / 30 | InvoiceShelf / InvoiceShelf | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-55383 | WATCH / 30 | InvoiceShelf / InvoiceShelf | v3.1 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-54566 | WATCH / 30 | shd101wyy / vscode-markdown-preview-enhanced | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-53999 | WATCH / 30 | radius-project / radius | v3.1 7.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-53612 | WATCH / 30 | util-linux / util-linux | v3.1 7.0 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-42093 | WATCH / 30 | getredash / redash | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110718 | WATCH / 30 | TurboDocx / html-to-docx | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110713 | WATCH / 30 | sahlberg / libsmb2 | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110712 | WATCH / 30 | sahlberg / libsmb2 | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110614 | WATCH / 30 | Yiuman / citrus | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110609 | WATCH / 30 | dromara / skyeye | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110607 | WATCH / 30 | BizSpring / BizSpring Shop | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105106 | WATCH / 30 | Koha Community / Koha | v3.1 8.8 (HIGH) | 0.01613 / percentile=0.75485 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

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
- EPSS 未確認：21；Exploitation status 未確認：0。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-15T05:25:00.357374+00:00`；Delta generated at：`2026-10-15T05:25:00.357374+00:00`。

---

## 可驗證資料來源

- **CVE-2026-76519** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76519) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-105134** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105134) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105134) · [Vendor / Advisory (ahsay.com)](https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-0322** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-0322) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (security.paloaltonetworks.com)](https://security.paloaltonetworks.com/CVE-2026-0322) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-105133** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105133) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105133) · [Vendor / Advisory (ahsay.com)](https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-65198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65198) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65198)
- **CVE-2026-93748** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93748) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93748)
- **CVE-2026-93687** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93687) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93687)
- **CVE-2026-65199** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65199) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65199)
- **CVE-2026-65200** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65200) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65200)
- **CVE-2026-65197** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65197) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65197)
- **CVE-2026-77371** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77371)
- **CVE-2026-110650** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110650)
- **CVE-2026-110645** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110645)
- **CVE-2026-110632** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110632)
- **CVE-2026-110612** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110612)
- **CVE-2026-108390** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108390)
- **CVE-2026-73252** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73252)
- **CVE-2026-55386** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55386)
- **CVE-2026-55383** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55383)
- **CVE-2026-54566** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54566)
- **CVE-2026-53999** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53999)
- **CVE-2026-53612** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53612)
- **CVE-2026-42093** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42093)
- **CVE-2026-110718** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110718)
- **CVE-2026-110713** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110713)
- **CVE-2026-110712** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110712)
- **CVE-2026-110614** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110614)
- **CVE-2026-110609** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110609)
- **CVE-2026-110607** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110607)
- **CVE-2026-105106** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105106) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105106)
- **CVE-2026-101895** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101895)
- **CVE-2025-71433** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-71433)
- **CVE-2026-97205** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97205)
- **CVE-2026-93483** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93483)
- **CVE-2026-93479** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93479)
- **CVE-2026-92152** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92152)
- **CVE-2026-91881** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91881)
- **CVE-2026-89310** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89310) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89310)
- **CVE-2026-86002** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86002)
- **CVE-2026-85714** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85714)
- **CVE-2026-77524** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77524)
- **CVE-2026-59774** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59774)
- **CVE-2026-55684** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55684)
- **CVE-2026-55683** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55683)
- **CVE-2026-55680** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55680)
- **CVE-2026-55573** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55573)
- **CVE-2026-55572** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55572)
- **CVE-2026-33796** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-33796)
- **CVE-2026-33792** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-33792)
- **CVE-2026-33789** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-33789)
- **CVE-2026-16741** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16741)
- **CVE-2026-16740** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16740)
- **CVE-2026-15176** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15176)
- **CVE-2026-14851** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-14851) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-14851)
- **CVE-2026-110911** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110911)
- **CVE-2026-110867** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110867)
- **CVE-2026-110864** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110864)
- **CVE-2026-110862** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110862)
- **CVE-2026-110858** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110858)
- **CVE-2026-110770** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110770)
- **CVE-2026-110649** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110649)
- **CVE-2026-110646** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110646)
- **CVE-2026-110644** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110644)
- **CVE-2026-110643** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110643)
- **CVE-2026-110640** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110640)
- **CVE-2026-110639** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110639)
- **CVE-2026-110638** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110638)
- **CVE-2026-110636** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110636)
- **CVE-2026-110635** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110635)
- **CVE-2026-110634** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110634)
- **CVE-2026-110631** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110631)
- **CVE-2026-110628** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110628)
- **CVE-2026-110616** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110616)
- **CVE-2026-110536** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110536)
- **CVE-2026-109439** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109439)
- **CVE-2026-108587** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108587)
- **CVE-2026-108336** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108336)
- **CVE-2026-108335** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108335)
- **CVE-2026-108291** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108291)
- **CVE-2026-108065** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108065)
- **CVE-2026-107594** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107594) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107594)
- **CVE-2026-107424** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107424)
- **CVE-2026-104748** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104748) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-104748)
- **CVE-2026-103415** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103415)
- **CVE-2026-102893** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102893)
- **CVE-2026-102748** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102748)
- **CVE-2026-102476** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102476)
- **CVE-2026-102182** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102182)
- **CVE-2026-102178** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102178)
- **CVE-2026-102175** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102175)
- **CVE-2026-102084** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102084)
- **CVE-2026-102070** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102070)
- **CVE-2026-102068** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102068)
- **CVE-2026-102062** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102062)
- **CVE-2026-102037** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102037)
- **CVE-2026-102031** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102031)
- **CVE-2026-101997** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101997)
- **CVE-2026-101990** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101990)
- **CVE-2026-101986** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101986)
- **CVE-2026-101983** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101983)
- **CVE-2026-101982** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101982)
- **CVE-2026-101980** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101980)
- **CVE-2026-101967** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101967)
- **CVE-2026-101956** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101956)
- **CVE-2026-101955** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101955)
- **CVE-2026-101954** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101954)
- **CVE-2026-101950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101950)
- **CVE-2020-37282** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-37282)
- **CVE-2020-37281** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-37281)
- **CVE-2026-92156** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92156)
- **CVE-2026-62858** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62858)
- **CVE-2026-25946** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-25946)
- **CVE-2026-110772** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110772)
- **CVE-2026-110771** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110771)
- **CVE-2026-110766** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110766)
- **CVE-2026-110717** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110717)
- **CVE-2026-110658** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110658)
- **CVE-2026-110657** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110657)
- **CVE-2026-110625** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110625)
- **CVE-2026-110619** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110619)
- **CVE-2026-110617** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110617)
- **CVE-2026-110602** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110602)
- **CVE-2026-110600** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110600)
- **CVE-2026-110599** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110599)
- **CVE-2026-110597** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110597)
- **CVE-2026-110594** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110594)
- **CVE-2026-110592** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110592)
- **CVE-2026-109971** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109971) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109971)
- **CVE-2026-103974** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103974)
- **CVE-2026-102755** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102755)
- **CVE-2016-20099** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-20099)
- **CVE-2026-92392** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92392)
- **CVE-2026-110655** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110655)
- **CVE-2026-110627** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110627)
- **CVE-2026-110604** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110604)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
