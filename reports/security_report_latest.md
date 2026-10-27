# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**34** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=1、EPSS_INCREASED=1、NEW_CVE=30、NEW_KEV=2。
- Intelligence 候選：**30** 筆；P1 **2**、P2 **0**、P3 **2**、WATCH **26**。
- Baseline：state / generated_at=2026-10-26T05:37:14.235919+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-109619、CVE-2026-109618。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **34** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-109619｜PHP Group / PHP
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.99997 / percentile=0.99989
- **CISA KEV**：listed=true / date_added=2026-10-26 / due_date=2026-10-29
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-21T14:17:09.823 / 2026-10-26T10:10:00.140
- **官方描述（原文）**：PHP contains a stale internal request-state vulnerability that allows for unauthenticated remote code execution.

### 2. CVE-2026-109618｜PHP Group / PHP
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.99981 / percentile=0.99981
- **CISA KEV**：listed=true / date_added=2026-10-26 / due_date=2026-10-29
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-21T14:17:09.357 / 2026-10-26T10:10:00.140
- **官方描述（原文）**：PHP contains an out-of-memory corruption vulnerability that allows for unauthenticated remote code execution.

### 3. CVE-2026-61447｜MervinPraison / PraisonAI
- **Delta event**：EPSS_INCREASED (from=0.0249; to=0.1524)
- **Risk**：P3 / score 58；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.1524 / percentile=0.96738
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-07-11T14:16:23.377 / 2026-10-25T15:10:00.147
- **官方描述（原文）**：PraisonAI before 1.6.78 contains a remote code execution vulnerability in CodeAgent._execute_python() that executes LLM-generated Python code without AST validation, import restrictions, or sandbox enforcement. Attackers can influence LLM output through prompt injection to exfiltrate all environment secrets and execute arbitrary code on the host system.

### 4. CVE-2026-107092｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T14:16:23.737)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T14:16:23.737 / 2026-10-26T18:41:21.450
- **官方描述（原文）**：NexoPOS v6.2.4 is vulnerable to Directory Traversal via the api/update endpoint.

### 5. CVE-2026-116235｜Oray / Pugongying X5 Pro
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T09:16:35.163)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：0.00614 / percentile=0.49118
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T09:16:35.163 / 2026-10-26T17:17:24.850
- **官方描述（原文）**：A flaw has been found in Oray Pugongying X5 Pro 7.6.1. Affected by this vulnerability is an unknown functionality of the component L2TP Authentication. This manipulation of the argument Username causes crlf injection. The attack may be initiated remotely. The exploit has been published and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 6. CVE-2026-116232｜Oray / Pugongying X5 Pro
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T08:17:17.837)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：0.00436 / percentile=0.37632
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T08:17:17.837 / 2026-10-26T17:17:24.717
- **官方描述（原文）**：A weakness has been identified in Oray Pugongying X5 Pro 7.6.1. This affects the function snmp_set of the component SNMP Handler. Executing a manipulation of the argument info.community can lead to crlf injection. It is possible to launch the attack remotely. The exploit has been made available to the public and could be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 7. CVE-2026-112345｜Sciener / TTLock
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T15:16:38.167)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T15:16:38.167 / 2026-10-26T18:41:21.450
- **官方描述（原文）**：TTLock Android application before v9.8.260718 and associated smart-lock firmware contain a hardcoded static AES key vulnerability that allows an attacker within Bluetooth range to decrypt the per-pairing session key transmitted during BLE pairing. Attackers can observe the pairing exchange, recover the persistent session key using the embedded defaultKey, and forge authenticated BLE requests to unlock the device, add fingerprints or access codes, and perform administrative actions without authentication or user interaction.

### 8. CVE-2026-93328｜Google Cloud / MCP Toolbox for Databases (googleapis/mcp-toolbox)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T15:16:45.813)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T15:16:45.813 / 2026-10-26T17:17:31.020
- **官方描述（原文）**：Path Traversal and Missing Authorization in cloud-storage source in Google Cloud MCP Toolbox for Databases (googleapis/mcp-toolbox) versions 1.2.0 through 1.4.0 allows an unauthenticated remote attacker to exfiltrate host files to external Google Cloud Storage buckets and overwrite arbitrary local files via crafted tool invocation parameters.

### 9. CVE-2026-77055｜boneIO / black_debian_images
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T15:16:43.123)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T15:16:43.123 / 2026-10-26T17:11:35.487
- **官方描述（原文）**：boneIO black_debian_images gives the boneio service account excessive privileges, including full passwordless sudo access and membership in the docker group. A local attacker who compromises the boneio user can use these privileges to escalate to root. This issue was fixed in version 1.6.0: the image removes the sudoers rule and the docker group membership when it is sealed, and devices already in the field have both removed by migrations shipped with boneio 1.6.0 and applied on first start after the upgrade. Privileged operations now go through helpers that accept only a fixed set of commands, with migrations verified against Ed25519 signatures.

### 10. CVE-2026-65184｜Vertiv / Avocent ACS8000
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T15:16:41.627)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T15:16:41.627 / 2026-10-26T18:41:21.450
- **官方描述（原文）**：The root-privileged `wsserver` terminal-bridge daemon builds a shell command from client-supplied WebSocket fields and passes it to `system()` and `popen()` without quoting, escaping, or character-set validation. The daemon's public-key session path performs no appliance-session check.

### 11. CVE-2026-59107｜WolfVision / Cynap Pro, Cynap Core Pro
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T14:16:38.973)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T14:16:38.973 / 2026-10-26T16:58:40.880
- **官方描述（原文）**：A security vulnerability has been identified in the vSolution Matrix file sharing feature. A shared cryptographic trust configuration could allow an attacker who obtains the matching private key to authenticate to an affected device via SSH as root. This vulnerability affects only devices configured as a vSolution Matrix main/master station with the file sharing feature enabled.

### 12. CVE-2026-59106｜WolfVision / Cynap Pure (Next Gen), Cynap Bridge
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T14:16:38.813)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T14:16:38.813 / 2026-10-26T16:58:40.880
- **官方描述（原文）**：A security vulnerability has been identified in the WolfProt interface implementation. Insufficient neutralization of user-controlled input could allow an unauthenticated attacker with network access to a vulnerable service to execute operating-system commands with the privileges of the affected application service.

### 13. CVE-2026-116747｜rajnandan1 / kener
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T22:16:59.463)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T22:16:59.463 / 2026-10-26T22:16:59.463
- **官方描述（原文）**：Kener 3.0.0 before 4.1.10 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge session tokens by using the hardcoded DUMMY_SECRET fallback key. When KENER_SECRET_KEY is empty or unset, attackers knowing an administrator email can sign a kener-user cookie to access /manage/api with full administrative privileges or forge password-reset tokens.

### 14. CVE-2026-116508｜TOTOLINK / A950RG
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T22:16:54.373)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T22:16:54.373 / 2026-10-26T22:16:54.373
- **官方描述（原文）**：A security flaw has been discovered in TOTOLINK A950RG 4.1.2cu.5268_B20221104. Affected by this issue is the function sub_402340 of the file infostat.cgi of the component Device-Information CGI. Performing a manipulation of the argument CONTENT_LENGTH results in stack-based buffer overflow. Remote exploitation of the attack is possible. The exploit has been released to the public and may be used for attacks.

### 15. CVE-2026-116485｜huangxd- / danmu_api
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T14:16:37.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T14:16:37.040 / 2026-10-26T18:41:21.450
- **官方描述（原文）**：danmu_api before 1.21.7 contains an authentication bypass vulnerability that allows unauthenticated attackers to modify server environment configuration when the default TOKEN is used and ADMIN_TOKEN is unset. Attackers can send POST requests to /api/env/set, /api/env/add, or /api/env/del to set ADMIN_TOKEN, lock out operators, redirect OTHER_SERVER or PROXY_URL for SSRF, and trigger redeployment.

### 16. CVE-2026-116214｜maccmspro / maccms10
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T14:16:34.173)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T14:16:34.173 / 2026-10-26T17:01:22.130
- **官方描述（原文）**：MacCMS v10 before 2026.1000.4054 contains an authentication bypass vulnerability that allows unauthenticated attackers to reset any member's password because check_msg() never compares msg_to. Attackers can request a recovery code to their own mailbox via user/findpass_msg, then submit it to user/findpass_reset with the victim's email or phone to take over the account.

### 17. CVE-2026-115905｜zip-rs / zip2
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T17:17:17.823)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T17:17:17.823 / 2026-10-26T18:39:42.503
- **官方描述（原文）**：zip is a zip library for Rust that supports reading and writing simple ZIP files. Through 9.0.4, ZipArchive treats Central Directory File Header filenames as authoritative while ZipStreamReader extracts using Local File Header filenames without reconciling the duplicate metadata in src/read/stream.rs. A crafted archive can therefore appear benign to a component that inspects the central directory but cause a streaming extractor to write a different attacker-selected path and content, potentially overwriting files used by a downstream service. This issue is fixed in version 9.0.5.

### 18. CVE-2026-115693｜benoitc / hackney
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T14:16:31.853)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T14:16:31.853 / 2026-10-26T16:59:16.113
- **官方描述（原文）**：Improper Certificate Validation vulnerability in hackney_ssl in benoitc hackney allows an on-path attacker to impersonate a server pinned to a private certificate authority via a certificate chain that ends in a publicly trusted root. hackney adds {partial_chain, fun hackney_ssl:partial_chain/1} to every verify_peer configuration. The callback returns any certificate in the peer chain whose public key matches a root in the bundled certifi store as the trust anchor, and OTP honours that callback over the configured cacerts. hackney_ssl:merge_ssl_opts/3 kept the callback when the caller replaced the trust store with cacerts or cacertfile in ssl_options, so a connection pinned to a private CA still accepted any chain that carried a publicly trusted root. The hostname check still applies, so the attacker needs a publicly trusted certificate for the pinned hostname. This issue affects hackney: from 1.24.0 before 4.9.0.

### 19. CVE-2026-115188｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T14:16:30.047)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T14:16:30.047 / 2026-10-26T16:17:16.027
- **官方描述（原文）**：An unrestricted file upload vulnerability exists in the campaign import feature of Mautic 7. When processing an uploaded campaign archive, the application copies the bundled asset files into a publicly accessible media directory without restricting their file names or types. An authenticated user with permission to create campaign imports can exploit this through the user interface or the API (/api/campaigns/import) to place arbitrary files, including server-side scripts, in the web root. Administrator privileges are not required. On web servers that honor per-directory configuration, such as the default Apache setup of the official Mautic Docker image, this leads to remote code execution with the privileges of the web server user, including access to the Mautic configuration, application secrets, and contact data.

### 20. CVE-2026-112346｜OpenHands / OpenHands Software Agent SDK
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T16:17:14.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T16:17:14.110 / 2026-10-26T18:39:42.503
- **官方描述（原文）**：OpenHands Software Agent SDK before 1.52.0 contains an unauthenticated remote code execution vulnerability where the DockerWorkspace and Apptainer workspace launchers bind the sandbox agent server to all network interfaces (0.0.0.0) with an empty session_api_keys list, disabling authentication by default. Attackers who can reach the published container port can send unauthenticated HTTP and WebSocket requests to execute arbitrary shell commands as root in the sandbox, access the mounted workspace, and read plaintext secrets from the secrets store.

### 21. CVE-2026-110720｜HashiCorp / Tooling
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T19:16:29.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T19:16:29.940 / 2026-10-26T20:17:49.013
- **官方描述（原文）**：Consul-k8s versions 0.42.0 and later are vulnerable to a cross-namespace authorization bypass in component ACL binding rules that may allow an attacker to obtain elevated Consul privileges. This vulnerability (CVE-2026-110720) is fixed in consul-k8s 2.1.0 and 1.8.18.

### 22. CVE-2026-110475｜CreditNirvana / CreditNirvana Collections Platform (CollectionWorkz)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T14:16:26.573)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T14:16:26.573 / 2026-10-26T14:21:33.887
- **官方描述（原文）**：This vulnerability exists in the CreditNirvana Collections Platform due to improper authentication and authorization controls at the platform login service. An unauthenticated remote attacker could exploit this vulnerability by manipulating authentication requests and accessing APIs without a valid authenticated session on the targeted system. Successful exploitation of this vulnerability could allow the attacker to enumerate platform users, establish sessions as arbitrary users including administrative users, access and modify sensitive information with the privileges of the impersonated user.

### 23. CVE-2026-107656｜Fortinet / FortiSandbox
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T14:16:24.147)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T14:16:24.147 / 2026-10-27T04:17:40.280
- **官方描述（原文）**：An authentication bypass using an alternate path or channel vulnerability in Fortinet FortiSandbox 5.0.0 through 5.0.6, FortiSandbox 4.4.0 through 4.4.9, FortiSandbox 4.2 all versions, FortiSandbox PaaS 5.0.0 through 5.0.6, FortiSandbox PaaS 4.4 all versions, FortiSandbox PaaS 4.2 all versions may allow attacker to execute unauthorized code or commands via crafted HTTP requests

### 24. CVE-2026-10757｜Esri / ArcGIS Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T18:17:34.580)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T18:17:34.580 / 2026-10-27T04:17:42.280
- **官方描述（原文）**：There is a SQL injection vulnerability in Esri ArcGIS Server versions 12.1 and earlier on Windows and Linux that may allow a remote attacker with privileges to access the service (which could, depending on the service being configured in a non-default access configuration “public”, include an anonymous attacker) to issue database specific functions that should not be allowed. A patch is provided for ArcGIS Server software in General Availability and Extended support status, which includes versions 12.1, 12.0, 11.5, 11.3, and 11.1. Other versions are in mature or retired status, which are not patch eligible. Users working with unlisted versions are advised to upgrade and apply the patch.

### 25. CVE-2026-102649｜padok-team / burrito
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T18:17:21.803)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T18:17:21.803 / 2026-10-26T18:39:42.503
- **官方描述（原文）**：Burrito is a Terraform Automation Collaboration Software (TACoS) Kubernetes operator. Prior to 0.13.0, `POST /api/webhook` accepts unsigned GitHub and GitLab events when a `TerraformRepository`'s credentials omit `webhookSecret` or set it to an empty value, including credentials configured for git authentication and polling. `Credential.WebhookSecret` is optional, and `go-playground/webhooks` skips signature or token verification when the secret is empty. Anyone who can reach `burrito-server`'s endpoint and knows a tracked repository's URL can forge events to create or delete `TerraformPullRequest` custom resources with attacker-chosen `Branch`, `Base`, and `ID` fields. For GitHub `pull_request` events, the controller fetches changed files using the real pull request number but does not cross-check the payload's branch against that pull request. Pairing a real, existing pull request number with an unrelated existing branch in the same repository can therefore cause an unauthorized `terraform plan` for affected layers using the operator's stored git and cloud credentials. Code analysis also indicates that the resulting plan can be posted to the real pull request's comment thread, exposing and misattributing another branch's infrastructure changes. Auto-apply is disabled for these temporary layers, so this vulnerability alone cannot force a `terraform apply`; plan-time provider and data-source code execution depends on the selected branch's contents. This issue is fixed in version 0.13.0.

### 26. CVE-2026-116339｜iFlytek / astron-agent
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T15:16:39.820)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T15:16:39.820 / 2026-10-26T18:41:21.450
- **官方描述（原文）**：A vulnerability was determined in iFlytek astron-agent up to 1.1.2. This affects an unknown function of the file core/memory/database/api/v1/exec_ddl.py of the component DDL Whitelist Handler. This manipulation causes incomplete blacklist. The attack may be initiated remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 27. CVE-2026-116256｜geesondog / RhaPHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T11:16:37.130)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T11:16:37.130 / 2026-10-26T17:17:25.113
- **官方描述（原文）**：A vulnerability was found in geesondog RhaPHP up to 7ae639ccf8dcb627faace096d030bd4cb4cfb905. Affected by this vulnerability is the function image of the file application/mp/controller/Show.php of the component Mp Module Media Proxy. The manipulation of the argument url results in server-side request forgery. The attack may be launched remotely. The exploit has been made public and could be used. This product operates on a rolling release basis, ensuring continuous delivery. Consequently, there are no version details for either affected or updated releases. The vendor was contacted early about this disclosure but did not respond in any way.

### 28. CVE-2026-116385｜Bdtask / Garage 24 Garage Management Software
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T18:17:43.773)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T18:17:43.773 / 2026-10-26T20:17:54.637
- **官方描述（原文）**：A security vulnerability has been detected in Bdtask Garage 24 Garage Management Software 1.0. This issue affects some unknown processing of the file /edit_profile of the component Profile. The manipulation of the argument first_name/last_name leads to cross site scripting. The attack may be initiated remotely. The exploit has been disclosed publicly and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 29. CVE-2026-116275｜AllenAI / AllenNLP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T14:16:35.353)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T14:16:35.353 / 2026-10-26T18:41:21.450
- **官方描述（原文）**：A vulnerability was found in AllenAI AllenNLP up to 2.10.1. This impacts the function Registrable.resolve_class_name of the file allennlp/common/registrable.py of the component Registrable Configuration Machinery. Performing a manipulation of the argument Type results in code injection. The attack may be initiated remotely. The exploit has been made public and could be used. The vendor was contacted early about this disclosure but did not respond in any way. This vulnerability only affects products that are no longer supported by the maintainer.

### 30. CVE-2026-116262｜未確認 / libimobiledevice
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T12:17:06.783)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T12:17:06.783 / 2026-10-26T17:17:25.383
- **官方描述（原文）**：A vulnerability was detected in libimobiledevice up to 1.4.0. The affected element is the function webinspector_receive_with_timeout of the file src/webinspector.c of the component Web Inspector. The manipulation results in heap-based buffer overflow. It is possible to launch the attack remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 31. CVE-2026-116259｜未確認 / libimobiledevice
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T11:16:37.670)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T11:16:37.670 / 2026-10-26T17:17:25.243
- **官方描述（原文）**：A security flaw has been discovered in libimobiledevice up to 1.4.0. This vulnerability affects the function afc_get_device_info_key of the file src/afc.c of the component Device Info Handler. Performing a manipulation of the argument Value results in memory corruption. The attack requires a local approach. The exploit has been released to the public and may be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 32. CVE-2026-116229｜ffxiv-teamcraft / FFXIV Teamcraft
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T08:17:17.227)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：0.00203 / percentile=0.1017
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T08:17:17.227 / 2026-10-26T17:17:24.560
- **官方描述（原文）**：A vulnerability was determined in ffxiv-teamcraft FFXIV Teamcraft up to 11.4.31. Impacted is the function clipboard.readText of the file apps/electron/src/preload.ts of the component Renderer-Process IPC Bridge. This manipulation causes cross site scripting. The attack is possible to be carried out remotely. The exploit has been publicly disclosed and may be utilized. Upgrading to version 11.4.32 is recommended to address this issue. Patch name: def118fdf36f8f3b615966893a132dd81d9cc3dc. Upgrading the affected component is recommended.

### 33. CVE-2026-116224｜fr0tt / benotes
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-26T07:17:09.590)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00232 / percentile=0.13934
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-26T07:17:09.590 / 2026-10-26T17:17:24.423
- **官方描述（原文）**：A vulnerability has been found in fr0tt benotes up to 2.8.1. This affects the function getUrlInfo of the file app/Http/Controllers/PostController.php of the component Bookmark Metadata Endpoint. The manipulation of the argument url leads to server-side request forgery. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 34. CVE-2026-105133｜Ahsay / AhsayCBS
- **Delta event**：CVSS_CHANGED (from=5.5; to=6.9)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：0.79236 / percentile=0.99596
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-04T07:16:33.087 / 2026-10-26T18:07:09.000
- **官方描述（原文）**：Ahsay AhsayCBS contains an improper authentication vulnerability that could allow a remote attacker to bypass authentication via manipulation of the random parameter in the API component’s checkSysPwd function. This vulnerability can be chained with CVE-2026-105134.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-109619｜PHP Group / PHP
- **Title**：PHP Stale Internal Request-State Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.99997 / percentile=0.99989
- **CISA KEV**：listed=true / date_added=2026-10-26 / due_date=2026-10-29
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：PHP contains a stale internal request-state vulnerability that allows for unauthenticated remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-109618｜PHP Group / PHP
- **Title**：PHP Memory Corruption Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.99981 / percentile=0.99981
- **CISA KEV**：listed=true / date_added=2026-10-26 / due_date=2026-10-29
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：PHP contains an out-of-memory corruption vulnerability that allows for unauthenticated remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-61447 | P3 / 58 | MervinPraison / PraisonAI | v4.0 10.0 (CRITICAL) | 0.1524 / percentile=0.96738 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107092 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-116235 | WATCH / 30 | Oray / Pugongying X5 Pro | v4.0 8.5 (HIGH) | 0.00614 / percentile=0.49118 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-116232 | WATCH / 30 | Oray / Pugongying X5 Pro | v4.0 8.6 (HIGH) | 0.00436 / percentile=0.37632 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112345 | WATCH / 30 | Sciener / TTLock | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93328 | WATCH / 28 | Google Cloud / MCP Toolbox for Databases (googleapis/mcp-toolbox) | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-77055 | WATCH / 28 | boneIO / black_debian_images | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-65184 | WATCH / 28 | Vertiv / Avocent ACS8000 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-59107 | WATCH / 28 | WolfVision / Cynap Pro, Cynap Core Pro | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-59106 | WATCH / 28 | WolfVision / Cynap Pure (Next Gen), Cynap Bridge | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-116747 | WATCH / 28 | rajnandan1 / kener | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-116508 | WATCH / 28 | TOTOLINK / A950RG | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-116485 | WATCH / 28 | huangxd- / danmu_api | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-116214 | WATCH / 28 | maccmspro / maccms10 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115905 | WATCH / 28 | zip-rs / zip2 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115693 | WATCH / 28 | benoitc / hackney | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115188 | WATCH / 28 | 未確認 / 未確認 | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-112346 | WATCH / 28 | OpenHands / OpenHands Software Agent SDK | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-110720 | WATCH / 28 | HashiCorp / Tooling | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-110475 | WATCH / 28 | CreditNirvana / CreditNirvana Collections Platform (CollectionWorkz) | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-107656 | WATCH / 28 | Fortinet / FortiSandbox | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-10757 | WATCH / 28 | Esri / ArcGIS Server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-102649 | WATCH / 28 | padok-team / burrito | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-116339 | WATCH / 22 | iFlytek / astron-agent | v4.0 5.5 (MEDIUM) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-116256 | WATCH / 22 | geesondog / RhaPHP | v4.0 5.5 (MEDIUM) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-116385 | WATCH / 18 | Bdtask / Garage 24 Garage Management Software | v4.0 2.0 (LOW) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-116275 | WATCH / 18 | AllenAI / AllenNLP | v4.0 2.1 (LOW) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-116262 | WATCH / 18 | 未確認 / libimobiledevice | v4.0 2.1 (LOW) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：3；缺少 Product：2；缺少 Title：28。
- EPSS 未確認：25；Exploitation status 未確認：11。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-27T05:49:02.764065+00:00`；Delta generated at：`2026-10-27T05:49:02.764065+00:00`。

---

## 可驗證資料來源

- **CVE-2026-109619** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109619) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109619) · [Vendor / Advisory (php.net)](https://www.php.net/) · [CISA](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-109618** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109618) · [Vendor / Advisory (php.net)](https://www.php.net/) · [CISA](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-61447** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61447) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-61447)
- **CVE-2026-107092** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107092)
- **CVE-2026-116235** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116235) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116235)
- **CVE-2026-116232** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116232) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116232)
- **CVE-2026-112345** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112345)
- **CVE-2026-93328** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93328)
- **CVE-2026-77055** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77055)
- **CVE-2026-65184** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65184)
- **CVE-2026-59107** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59107)
- **CVE-2026-59106** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59106)
- **CVE-2026-116747** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116747)
- **CVE-2026-116508** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116508)
- **CVE-2026-116485** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116485)
- **CVE-2026-116214** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116214)
- **CVE-2026-115905** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115905)
- **CVE-2026-115693** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115693)
- **CVE-2026-115188** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115188)
- **CVE-2026-112346** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112346)
- **CVE-2026-110720** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110720)
- **CVE-2026-110475** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110475)
- **CVE-2026-107656** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107656)
- **CVE-2026-10757** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-10757)
- **CVE-2026-102649** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102649)
- **CVE-2026-116339** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116339)
- **CVE-2026-116256** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116256)
- **CVE-2026-116385** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116385)
- **CVE-2026-116275** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116275)
- **CVE-2026-116262** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116262)
- **CVE-2026-116259** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116259)
- **CVE-2026-116229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116229) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116229)
- **CVE-2026-116224** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116224) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116224)
- **CVE-2026-105133** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105133) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105133) · [Vendor / Advisory (ahsay.com)](https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
