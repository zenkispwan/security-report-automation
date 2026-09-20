# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**6** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=6。
- Intelligence 候選：**23** 筆；P1 **9**、P2 **0**、P3 **8**、WATCH **6**。
- Baseline：state / generated_at=2026-09-19T05:19:08.035619+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-65400、CVE-2026-76460、CVE-2026-87886、CVE-2026-87491、CVE-2026-67277。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **6** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-94084｜OISF / Suricata
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-20T02:16:53.717)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-20T02:16:53.717 / 2026-09-20T02:16:53.717
- **官方描述（原文）**：Suricata before 8.0.7 has an Http2ThreadMultiBuf use-after-free when a transaction is inspected by rules that use http.response_header with and without a transform.

### 2. CVE-2026-94083｜OISF / Suricata
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-20T02:16:53.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-20T02:16:53.520 / 2026-09-20T02:16:53.520
- **官方描述（原文）**：Suricata before 8.0.7 has a DoH2 type confusion that can cause an invalid free, because cleanup code for the HTTP2 state is executed even though the actual state is HTTP1 (when there is a DoH2 request with an HTTP1 to HTTP2 upgrade). This requires app-layer.protocols.doh2 to be enabled, which is the default in 8.x versions.

### 3. CVE-2026-93985｜Openpanel-dev / openpanel
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-19T12:16:41.873)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-19T12:16:41.873 / 2026-09-19T12:16:41.873
- **官方描述（原文）**：OpenPanel js-runtime through commit bad75bdd contains a sandbox escape vulnerability in the JavaScript webhook template validator that fails to block computed member access to constructor chains. Attackers with project write access can create webhook templates using computed property notation to access Function constructor and execute arbitrary code in the worker process.

### 4. CVE-2026-93741｜Totolink / A3002MU
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-19T06:16:30.557)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00644 / percentile=0.49421
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-19T06:16:30.557 / 2026-09-19T06:16:30.557
- **官方描述（原文）**：A security flaw has been discovered in Totolink A3002MU Hh-B20211125.1046. Affected by this vulnerability is the function formWlWds of the file /boafrm/formWlWds. The manipulation of the argument submit-url results in buffer overflow. It is possible to launch the attack remotely. The exploit has been released to the public and may be used for attacks.

### 5. CVE-2026-86591｜Unknown / Botiga Pro
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-19T07:16:33.063)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00184 / percentile=0.08209
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-19T07:16:33.063 / 2026-09-19T14:17:00.907
- **官方描述（原文）**：The Botiga Pro WordPress plugin before 1.6.5 does not perform any authorisation checks on one of its REST routes, allowing unauthenticated users to update arbitrary WordPress options with arbitrary values, which could lead to privilege escalation and a full site takeover. The same route also allows unauthenticated users to store arbitrary web scripts which are then executed on every page of the site's front end, as well as to move arbitrary posts to the trash.

### 6. CVE-2026-78030｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-19T11:16:37.667)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-19T11:16:37.667 / 2026-09-20T01:16:30.017
- **官方描述（原文）**：DBI versions before 1.653 for Perl load arbitrary modules via unvalidated dbm_type and dbm_mldbm attributes in DBD::DBM. DBD::DBM passes the dbm_type and dbm_mldbm connect attributes to require without checking that the value names a module. require treats a path-shaped string as a literal filename and does not consult @INC, so the attribute chooses the file that Perl loads and runs. The MLDBM::Serializer:: prefix that DBD::DBM prepends to dbm_mldbm is not a boundary: only the :: separators are rewritten to /, so a value containing / traverses out of the serializer directory. The value is also assigned to $MLDBM::Serializer, which MLDBM requires the same way when it ties the table. A caller that lets an untrusted party influence either attribute, for example through a DSN fragment or a parameter that selects a storage backend, runs the file-scope code of whatever module the value names. For example, my $dsn = "dbi:DBM:f_dir=/var/db;dbm_type=../../Untrusted.pm" my $dbh = DBI->connect( $dsn ); Note that DBD::Gofer forwards connect attributes to the server side, and DBI::ProxyServer checks only that a DSN starts with a driver prefix.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-65400｜Apple / macOS
- **Title**：Apple macOS Improper Authentication Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.10461 / percentile=0.95531
- **CISA KEV**：listed=true / date_added=2026-08-18 / due_date=2026-08-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apple macOS contains an improper authentication vulnerability that could allow an attacker on the network to authenticate to Screen Sharing without valid credentials.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-76460｜Cisco / Identity Services Engine
- **Title**：Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00784 / percentile=0.54531
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) contain an incorrect use of privileged APIs vulnerability that could allow an unauthenticated, remote attacker to gain unauthorized access to the affected device by bypassing the web-based management interface.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-87886｜Acronis / Backup
- **Title**：Acronis Backup Incorrect Default Permissions Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.0 7.8 (HIGH)
- **EPSS**：0.00254 / percentile=0.17351
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Acronis Backup plugin for cPanel & WHM and extension for Plesk contains an incorrect default permissions vulnerability that could allow for privilege escalation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-87491｜Google / Chromium V8
- **Title**：Google Chromium V8 Out of Bounds Write Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00997 / percentile=0.61191
- **CISA KEV**：listed=true / date_added=2026-09-09 / due_date=2026-09-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium V8 contains an out of bounds write vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-67277｜MikroTik / RouterOS
- **Title**：MikroTik RouterOS Missing Authentication for Critical Function Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：0.00869 / percentile=0.5721
- **CISA KEV**：listed=true / date_added=2026-09-10 / due_date=2026-09-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：MikroTik RouterOS contains a missing authenticaion for critical function vulnerability which allows kernel memory disclosure and denial of service in the btest service.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-58704｜Google / Pixel
- **Title**：Google Pixel Improper Authorization Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00207 / percentile=0.11172
- **CISA KEV**：listed=true / date_added=2026-09-16 / due_date=2026-09-19
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Pixel devices contain an improper authorization vulnerability in the cellular modem. A logic error may allow an attacker to bypass permission checks and escalate privileges.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-53266｜Linux / Kernel
- **Title**：Linux Kernel Out-of-Bounds Write Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00276 / percentile=0.20232
- **CISA KEV**：listed=true / date_added=2026-09-18 / due_date=2026-09-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Linux Kernel contains an out-of-bounds write vulnerability in the ebtables SNAT target which allows an ARP sender hardware address rewrite to write directly into a nonlinear socket-buffer fragment backed by a splice-imported file page. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2025-39682｜Linux / Kernel
- **Title**：Linux Kernel Improper Check for Unusual or Exceptional Conditions Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：0.012 / percentile=0.66794
- **CISA KEV**：listed=true / date_added=2026-09-18 / due_date=2026-09-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Linux Kernel contains an improper check for unusual or exceptional conditions vulnerability in the TLS receive path which allows a zero-length record retrieved from the rx_list to bypass the intended recvmsg() record-type handling, potentially causing subsequent TLS records to be processed using incorrect zero-copy and queuing assumptions. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2025-39964｜Linux / Kernel
- **Title**：Linux Kernel Race Condition Vulnerability
- **Risk**：P1 / score 74；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.0079 / percentile=0.54721
- **CISA KEV**：listed=true / date_added=2026-09-18 / due_date=2026-09-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Linux Kernel contains a race condition vulnerability which allows concurrent writes to the same AF_ALG socket causing data to be unpredictably interleaved and creating inconsistencies in the socket's internal state.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-66066 | P3 / 49 | rails / rails | v4.0 9.5 (CRITICAL) | 0.27861 / percentile=0.98007 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93868 | P3 / 38 | Cotonti / Cotonti | v4.0 9.2 (CRITICAL) | 0.00607 / percentile=0.47694 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93606 | P3 / 38 | patriksimek / vm2 | v4.0 10.0 (CRITICAL) | 0.00518 / percentile=0.43047 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93019 | P3 / 38 | 未確認 / 未確認 | v3.1 9.1 (CRITICAL) | 0.00606 / percentile=0.47632 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92701 | P3 / 38 | ultravioletrs / cocos | v3.1 9.1 (CRITICAL) | 0.00221 / percentile=0.1297 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-84383 | P3 / 38 | strukturag / libheif | v3.1 9.8 (CRITICAL) | 0.00641 / percentile=0.49288 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63647 | P3 / 38 | 1Panel-dev / CordysCRM | v4.0 9.3 (CRITICAL) | 0.00474 / percentile=0.40168 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-59163 | P3 / 38 | AxDSan / mnemosyne | v3.1 9.1 (CRITICAL) | 0.00251 / percentile=0.16922 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-94084 | WATCH / 28 | OISF / Suricata | v3.1 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94083 | WATCH / 28 | OISF / Suricata | v3.1 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93985 | WATCH / 28 | Openpanel-dev / openpanel | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93741 | WATCH / 28 | Totolink / A3002MU | v4.0 9.3 (CRITICAL) | 0.00644 / percentile=0.49421 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-86591 | WATCH / 28 | Unknown / Botiga Pro | v3.1 9.8 (CRITICAL) | 0.00184 / percentile=0.08209 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-78030 | WATCH / 28 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：23；缺少 Vendor：2；缺少 Product：2；缺少 Title：14。
- EPSS 未確認：4；Exploitation status 未確認：4。
- 結構化受影響版本未提供：23。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-20T05:33:34.476819+00:00`；Delta generated at：`2026-09-20T05:33:34.476819+00:00`。

---

## 可驗證資料來源

- **CVE-2026-65400** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65400) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65400) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148170) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148171) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148172) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-76460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76460) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87886** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87886) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87886) · [Vendor / Advisory (security-advisory.acronis.com)](https://security-advisory.acronis.com/advisories/SEC-10986) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87491) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87491) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-67277** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67277) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-67277) · [Vendor / Advisory (mikrotik.com)](https://mikrotik.com/supportsec/september-2026-vulnerability/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-94084** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94084)
- **CVE-2026-94083** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94083)
- **CVE-2026-93985** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93985)
- **CVE-2026-93741** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93741) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93741)
- **CVE-2026-86591** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86591) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86591)
- **CVE-2026-78030** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78030)
- **CVE-2026-58704** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58704) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-58704) · [Vendor / Advisory (source.android.com)](https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-53266** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53266) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-53266) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/bf84ad7c7a9ede46e31afaa41a1ba06a159e8c87) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/76280b78cc9f23bdc6438e10ad6dff148ef8375b) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/b7e91939ba9be805a62a257fa4e227dffbb88fa0) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/afd64b59c3de9bbbdd3759e834fdc55cda716e0b) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/153ea96c806aea395daba907a4f88480b6ad5093) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/b18675263db1147c8e1cab625400c13a0d87bd2d) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/c9b5ff59feffb92a147a84a5aa28acd2cb8ff4c5) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/67ba971ae02514d85818fe0c32549ab4bfa3bf49) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-39682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-39682) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-39682) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/2902c3ebcca52ca845c03182000e8d71d3a5196f) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/c09dd3773b5950e9cfb6c9b9a5f6e36d06c62677) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/3439c15ae91a517cf3c650ea15a8987699416ad9) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/29c0ce3c8cdb6dc5d61139c937f34cb888a6f42e) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/62708b9452f8eb77513115b17c4f8d1a22ebf843) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-39964** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-39964) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-39964) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/0f28c4adbc4a97437874c9b669fd7958a8c6d6ce) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/e4c1ec11132ec466f7362a95f36a506ce4dc08c9) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/1f323a48e9b5ebfe6dc7d130fdf5c3c0e92a07c8) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/7c4491b5644e3a3708f3dbd7591be0a570135b84) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/9aee87da5572b3a14075f501752e209801160d3d) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/45bcf60fe49b37daab1acee57b27211ad1574042) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/1b34cbbf4f011a121ef7b2d7d6e6920a036d5285) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-66066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66066) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-66066)
- **CVE-2026-93868** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93868) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93868)
- **CVE-2026-93606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93606) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93606)
- **CVE-2026-93019** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93019) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93019)
- **CVE-2026-92701** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92701) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-92701)
- **CVE-2026-84383** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84383) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84383)
- **CVE-2026-63647** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63647) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63647)
- **CVE-2026-59163** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59163) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-59163)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
