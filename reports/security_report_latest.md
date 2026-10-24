# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**290** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=1、NEW_CVE=288、NEW_KEV=2。
- Intelligence 候選：**30** 筆；P1 **2**、P2 **0**、P3 **1**、WATCH **27**。
- Baseline：state / generated_at=2026-10-20T05:33:48.385179+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-114625、CVE-2026-110447。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **200** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-114625｜Arista / VeloCloud Orchestrator
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T21:17:16.870)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00555 / percentile=0.45586
- **CISA KEV**：listed=true / date_added=2026-10-23 / due_date=2026-10-26
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-22T21:17:16.870 / 2026-10-24T04:18:17.510
- **官方描述（原文）**：Arista VeloCloud Orchestrator on-prem contains a SQL injection vulnerability that may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator.

### 2. CVE-2026-110447｜Collabora / Collabora Online – Built-in CODE Server
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.01225 / percentile=0.68615
- **CISA KEV**：listed=true / date_added=2026-10-23 / due_date=2026-10-26
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-14T03:17:20.683 / 2026-10-24T04:18:17.157
- **官方描述（原文）**：Collabora Collabora Online – Built-in CODE Server when used within the NextCloud platform contains an OS command injection vulnerability that allows for remote code execution when the CODE server isn't running.

### 3. CVE-2021-48014｜FanRuan / FineReport
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T11:17:04.390)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.01669 / percentile=0.76617
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T11:17:04.390 / 2026-10-23T22:16:51.227
- **官方描述（原文）**：FineReport 9.0 contains a path traversal vulnerability in the /WebReport/ReportServer design_save_svg operation that allows unauthenticated attackers to write arbitrary files via the filePath parameter. Attackers can send a POST request with directory traversal sequences in filePath and a __CONTENT__ payload to write a JSP webshell and achieve remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 4. CVE-2026-109618｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T14:17:09.357)
- **Risk**：WATCH / score 33；reasons：CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.1162 / percentile=0.96047
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T14:17:09.357 / 2026-10-23T16:26:54.713
- **官方描述（原文）**：PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

### 5. CVE-2026-115506｜libexpat / libexpat
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T20:17:06.620)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.0035 / percentile=0.27483
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T20:17:06.620 / 2026-10-23T21:17:22.280
- **官方描述（原文）**：libexpat through 2.9.0 contains a denial of service vulnerability because billion laughs protection in accountingDiffTolerated() in xmlparse.c detects entity amplification too late. Attackers can supply a moderately sized XML document with a large DTD and nested entity expansions to consume tens of seconds of CPU per parse.

### 6. CVE-2026-114087｜triggerdotdev / trigger.dev
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T01:17:33.450)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T01:17:33.450 / 2026-10-22T16:17:33.827
- **官方描述（原文）**：Trigger.dev before 4.5.6 self-hosted Docker Compose deployments using the default secrets from hosting/docker/.env.example allow authentication bypass because the hardcoded MAGIC_LINK_SECRET lets anyone forge valid magic link tokens. Unauthenticated attackers can log in as any email address, then reach Postgres, Redis, and ClickHouse with default credentials from runner containers on infrastructure networks, compromising all tenant data.

### 7. CVE-2026-113678｜froxlor / froxlor
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T16:17:12.613)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00446 / percentile=0.37809
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T16:17:12.613 / 2026-10-23T02:16:56.567
- **官方描述（原文）**：Froxlor before 2.3.15 contains a symlink following vulnerability in Statistics::makeChownWithNewStats that allows authenticated customers to take ownership of arbitrary host directories by abusing the root-run traffic cron. Attackers can replace the goaccess statistics directory in their document root with a symlink, causing chown -R to hand root-owned trees to them and enabling root escalation.

### 8. CVE-2024-58396｜YouDataSum / CPAS Audit Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T11:17:06.203)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.00389 / percentile=0.31867
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T11:17:06.203 / 2026-10-23T22:16:51.653
- **官方描述（原文）**：YouDataSum CPAS Audit Management System V4 contains a path traversal vulnerability that allows unauthenticated attackers to read arbitrary files by manipulating the fileId parameter. Attackers can send GET requests to /cpasm4/plugInManController/downPlugs with ../ sequences in fileId to retrieve system files like /etc/passwd. Exploitation evidence was first observed by the Shadowserver Foundation on 2025-01-13.

### 9. CVE-2022-51025｜Penta Security Systems / WAPPLES
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T11:17:05.593)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00373 / percentile=0.30072
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T11:17:05.593 / 2026-10-23T22:16:51.500
- **官方描述（原文）**：Penta Security WAPPLES 4.0.54.1, 5.0, and 6.0 contains a path traversal vulnerability that allows authenticated attackers to download arbitrary files via the name parameter of /webapi/file/transfer. Attackers can send GET requests with type=db_backup and ../ sequences in name to read files like /etc/passwd, and a hardcoded systemi account makes authentication effectively trivial. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-19.

### 10. CVE-2019-25778｜SeaCMS / SeaCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T11:17:03.777)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：0.00377 / percentile=0.3054
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T11:17:03.777 / 2026-10-23T22:16:51.077
- **官方描述（原文）**：SeaCMS through 8.7 contains an unauthenticated SQL injection vulnerability that allows remote attackers to manipulate database queries by injecting SQL through the rlist[] array parameter. Attackers can send GET requests to /comment/api/index.php with crafted rlist[] values using backtick-quoted variables and extractvalue to extract database information via error messages. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 11. CVE-2017-20289｜Broadstreet / Ad Widget
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T11:17:03.063)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T11:17:03.063 / 2026-10-23T22:16:50.180
- **官方描述（原文）**：Broadstreet Ad Widget plugin for WordPress 2.2.0 before 2.12.0 contains a local file inclusion vulnerability that allows authenticated users to execute attacker-chosen PHP files by passing unsanitized input to require in views/modal/index.php. Attackers can supply directory traversal sequences in the 'step' parameter, optionally with a null byte, to include local files and execute PHP code. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-19.

### 12. CVE-2026-97785｜Microsoft / Microsoft Entra application proxy
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T22:20:13.483)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00598 / percentile=0.47969
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T22:20:13.483 / 2026-10-23T19:43:46.190
- **官方描述（原文）**：Improper authentication in AAD App Proxy allows an unauthorized attacker to elevate privileges over a network.

### 13. CVE-2026-97631｜TianoCore / EDK2
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T17:17:02.027)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.00432 / percentile=0.36541
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T17:17:02.027 / 2026-10-22T17:40:46.877
- **官方描述（原文）**：EDK2 contains a vulnerability in BIOS where a user may cause “Out-of-bounds Write”, Classic Buffer Overflow, and “Incorrect Calculation of Buffer Size” by remote access. Successful exploitation of this vulnerability can lead to arbitrary code execution. It could also impact Confidentiality, Integrity, and Availability.

### 14. CVE-2026-94267｜Unknown / Advanced Custom Fields: Extended
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T06:17:08.200)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：0.00192 / percentile=0.08398
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T06:17:08.200 / 2026-10-23T14:20:57.920
- **官方描述（原文）**：The Advanced Custom Fields: Extended WordPress plugin before 0.9.2.8, Advanced Custom Fields: Extended PRO WordPress plugin before 0.9.2.8 does not perform any capability check when updating a post through one of its front-end form actions, allowing unauthenticated visitors to overwrite arbitrary posts, including the ones in which the site stores its own field definitions, which in turn leads to arbitrary code execution on the server. Exploitation requires the site to publish a form whose post-update action maps both its target and its content to visitor-submitted values.

### 15. CVE-2026-83938｜Microsoft / Azure Kubernetes Configuration Service
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T22:19:18.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T22:19:18.540 / 2026-10-23T19:43:46.190
- **官方描述（原文）**：Missing authentication for critical function in Azure Kubernetes Configuration Service allows an unauthorized attacker to elevate privileges over a network.

### 16. CVE-2026-79876｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:18:00.050)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.00171 / percentile=0.06133
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:18:00.050 / 2026-10-23T20:17:25.207
- **官方描述（原文）**：A sensitive information disclosure vulnerability in the Wi-Fi frame processing of AOS-10 could allow an unauthenticated adjacent attacker to access sensitive information. Successful exploitation could allow an attacker to retrieve information which could be used to potentially gain further access to network services supported by AOS-10, or to interrupt the normal operation of the affected service.

### 17. CVE-2026-79875｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:59.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.00164 / percentile=0.05369
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:59.943 / 2026-10-23T20:17:25.103
- **官方描述（原文）**：A vulnerability has been identified in the PAPI protocol of AOS-8 that could potentially allow an unauthenticated adjacent attacker to circumvent existing authentication controls. Successful exploitation could allow an attacker to gain administrative access, modify system configurations, and access or manipulate sensitive data.

### 18. CVE-2026-79874｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:59.837)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.00164 / percentile=0.0537
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:59.837 / 2026-10-23T20:17:24.997
- **官方描述（原文）**：An authentication bypass in the API of AOS-10 allows an unauthenticated adjacent attacker to circumvent existing authentication controls. Successful exploitation could allow an attacker to gain administrative access, modify system configurations, and access or manipulate sensitive data.

### 19. CVE-2026-79873｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:59.727)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.00164 / percentile=0.0537
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:59.727 / 2026-10-23T20:17:24.900
- **官方描述（原文）**：Authentication bypass vulnerabilities in the PAPI protocol of AOS-10 could allow an unauthenticated adjacent attacker to circumvent existing authentication controls. Successful exploitation could allow an attacker to gain administrative access, modify system configurations, and access or manipulate sensitive data on affected devices.

### 20. CVE-2026-79872｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:59.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00262 / percentile=0.17087
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:59.600 / 2026-10-23T20:17:24.807
- **官方描述（原文）**：A buffer overflow vulnerability exists in the underlying operating system of AOS that could lead to unauthenticated remote code execution by an unauthenticated remote attacker. Successful exploitation of this vulnerability results in the ability to execute arbitrary code as a privileged user on the underlying operating system.

### 21. CVE-2026-79871｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:59.493)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00182 / percentile=0.07388
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:59.493 / 2026-10-23T20:17:24.713
- **官方描述（原文）**：A sensitive information disclosure vulnerability in the command line interface of AOS-10 could allow an unauthenticated remote attacker to access sensitive information. Successful exploitation could allow an attacker to retrieve information which could be used to potentially gain further access to network services supported by AOS-10.

### 22. CVE-2026-79870｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:59.390)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00182 / percentile=0.07387
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:59.390 / 2026-10-23T20:17:24.620
- **官方描述（原文）**：An authentication bypass vulnerability in the PAPI protocol of AOS-8 could allow an unauthenticated adjacent attacker to circumvent existing authentication controls. Successful exploitation could allow an attacker to gain administrative access, modify system configurations, access or manipulate sensitive data, and disrupt network operations.

### 23. CVE-2026-79869｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:59.280)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00182 / percentile=0.07387
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:59.280 / 2026-10-23T20:17:24.523
- **官方描述（原文）**：Authentication bypass vulnerabilities in the affected interface of AOS-10 could allow an unauthenticated adjacent attacker to circumvent existing authentication controls. Successful exploitation could allow an attacker to execute arbitrary commands as a privileged user on the underlying operating system.

### 24. CVE-2026-79868｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:59.177)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00182 / percentile=0.07387
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:59.177 / 2026-10-23T20:17:24.430
- **官方描述（原文）**：Authentication bypass vulnerabilities in the affected interface of AOS-8 could allow an unauthenticated adjacent attacker to circumvent existing authentication controls. Successful exploitation could allow an attacker to gain administrative access, modify system configurations, and access or manipulate sensitive data, leading to complete compromise of the affected system.

### 25. CVE-2026-79867｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:59.067)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00182 / percentile=0.07388
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:59.067 / 2026-10-23T20:17:24.333
- **官方描述（原文）**：Authentication bypass vulnerabilities in the affected interface of AOS-8 could allow an unauthenticated adjacent attacker to circumvent existing authentication controls and run arbitrary commands on the underlying host. Successful exploitation could allow an attacker to execute arbitrary commands on the underlying operating system leading to complete system compromise.

### 26. CVE-2026-79866｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:58.960)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00195 / percentile=0.08747
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:58.960 / 2026-10-23T20:17:24.223
- **官方描述（原文）**：An unauthenticated path traversal vulnerability exists in the PAPI protocol in AOS-8. Successful exploitation of this vulnerability could allow an unauthenticated adjacent attacker to read, modify, and delete files on the underlying operating system.

### 27. CVE-2026-79865｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:58.850)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00195 / percentile=0.08747
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:58.850 / 2026-10-23T20:17:24.127
- **官方描述（原文）**：A memory corruption vulnerability in the affected interface of AOS-10 could allow an unauthenticated adjacent attacker to achieve remote code execution. Successful exploitation could allow an attacker to execute arbitrary code as a privileged user on the underlying operating system.

### 28. CVE-2026-79864｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:58.743)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.0021 / percentile=0.10602
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:58.743 / 2026-10-23T20:17:24.027
- **官方描述（原文）**：Command injection vulnerabilities exist in the affected interface of AOS-10 that could allow an unauthenticated adjacent attacker to perform command injection. Successful exploitation could allow an attacker to execute arbitrary commands as a privileged user on the underlying operating system.

### 29. CVE-2026-79863｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:58.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00195 / percentile=0.08747
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:58.630 / 2026-10-23T20:17:23.933
- **官方描述（原文）**：Buffer overflow vulnerabilities in the affected interface of AOS-10 or AOS-8 could allow an unauthenticated adjacent attacker to execute arbitrary code by sending specially crafted data to the affected interface. Successful exploitation could allow an attacker to execute arbitrary code as a privileged user on the underlying operating system.

### 30. CVE-2026-79862｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:58.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00195 / percentile=0.08746
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:58.520 / 2026-10-23T20:17:23.837
- **官方描述（原文）**：Buffer overflow vulnerabilities in the affected interface of AOS-10 or AOS-8 could allow an unauthenticated adjacent attacker to execute arbitrary code by sending specially crafted data to the affected interface. Successful exploitation could allow an attacker to execute arbitrary code as a privileged user on the underlying operating system.

### 31. CVE-2026-79861｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:58.407)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00422 / percentile=0.35443
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:58.407 / 2026-10-23T20:17:23.727
- **官方描述（原文）**：There is a command injection vulnerability in AOS-10 that could lead to unauthenticated remote code execution by sending specially crafted PAPI packets. Successful exploitation of this vulnerability results in the ability to execute arbitrary code as a privileged user on the underlying operating system.

### 32. CVE-2026-79860｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:58.303)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00358 / percentile=0.28342
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:58.303 / 2026-10-23T20:17:23.633
- **官方描述（原文）**：Buffer overflow vulnerabilities exist in an underlying service of AOS-8 that could lead to unauthenticated remote code execution by sending specially crafted packets destined to the PAPI (Aruba's access point management protocol) UDP port 8211. Successful exploitation could allow an attacker to execute arbitrary code as a privileged user on the underlying operating system.

### 33. CVE-2026-79859｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:58.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00358 / percentile=0.28342
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:58.190 / 2026-10-23T20:17:23.540
- **官方描述（原文）**：Buffer overflow vulnerabilities exist in the affected interface of AOS-8 that could lead to unauthenticated remote code execution. Successful exploitation could allow an attacker to execute arbitrary code as a privileged user on the underlying operating system.

### 34. CVE-2026-79858｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:58.083)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00358 / percentile=0.28341
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:58.083 / 2026-10-24T04:18:19.467
- **官方描述（原文）**：An unauthenticated SQL injection vulnerability exists in the PAPI protocol in AOS-8. Successful exploitation could allow an unauthenticated remote attacker to obtain and modify sensitive information in the underlying database and to interrupt the normal operation of the affected service.

### 35. CVE-2026-79857｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:57.963)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00393 / percentile=0.32319
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:57.963 / 2026-10-24T04:18:19.337
- **官方描述（原文）**：There is a command injection vulnerability in the PAPI protocol (Aruba's access point management protocol) of AOS-8 that could lead to unauthenticated remote code execution by sending specially crafted packets to the affected UDP port. Successful exploitation of this vulnerability results in the ability to execute arbitrary code as a privileged user on the underlying operating system.

### 36. CVE-2026-79856｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:57.857)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00358 / percentile=0.28342
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:57.857 / 2026-10-24T04:18:19.187
- **官方描述（原文）**：A buffer overflow vulnerability exists in the PAPI protocol of AOS-8 that could allow an unauthenticated remote attacker to circumvent existing authentication controls. Successful exploitation could allow an attacker to gain administrative access, modify system configurations, and access or manipulate sensitive data.

### 37. CVE-2026-79855｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:57.743)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00422 / percentile=0.35444
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:57.743 / 2026-10-24T04:18:19.057
- **官方描述（原文）**：An authentication bypass vulnerability in the SSH daemon of AOS-8 allows an unauthenticated remote attacker to circumvent existing authentication controls. Successful exploitation allows an attacker to gain administrative privileges leading to complete compromise of the AOS-8 host.

### 38. CVE-2026-79854｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:57.627)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00358 / percentile=0.28341
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:57.627 / 2026-10-24T04:18:18.923
- **官方描述（原文）**：A vulnerability in the affected interface of AOS-10 could allow an unauthenticated remote attacker to conduct SQL injection attacks against the AOS-10 instance. Successful exploitation could allow an attacker to execute arbitrary commands on the underlying operating system.

### 39. CVE-2026-79853｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:57.513)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00358 / percentile=0.28341
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:57.513 / 2026-10-23T20:17:22.893
- **官方描述（原文）**：Sensitive information disclosure vulnerabilities in the affected interface of AOS-10 could allow an unauthenticated remote attacker to obtain sensitive information from the affected system. Successful exploitation could allow an attacker to execute arbitrary commands on the underlying operating system.

### 40. CVE-2026-79852｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:57.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00358 / percentile=0.28343
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:57.410 / 2026-10-24T04:18:18.780
- **官方描述（原文）**：A vulnerability in the web-based management interface of AOS could allow an unauthenticated remote attacker to conduct SQL injection attacks against the AOS instance. Successful exploitation could allow an attacker to execute arbitrary commands on the underlying operating system.

### 41. CVE-2026-79851｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:57.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00499 / percentile=0.41875
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:57.290 / 2026-10-23T20:17:22.683
- **官方描述（原文）**：Buffer overflow vulnerabilities exist in the affected interface of AOS-10 that could lead to unauthenticated remote code execution. Successful exploitation could allow an attacker to execute arbitrary code as a privileged user on the underlying operating system, leading to complete system compromise.

### 42. CVE-2026-79850｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:57.183)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.004 / percentile=0.33077
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:57.183 / 2026-10-23T20:17:22.573
- **官方描述（原文）**：Vulnerabilities in the affected interface of AOS-8 could allow an unauthenticated remote attacker to bypass existing authentication controls and run arbitrary commands on the underlying host. Successful exploitation could allow an attacker to execute arbitrary commands as root on the underlying operating system leading to complete system compromise.

### 43. CVE-2026-79849｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:57.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00539 / percentile=0.44613
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:57.070 / 2026-10-23T20:17:22.467
- **官方描述（原文）**：Vulnerabilities in the affected interface of AOS-8 could allow an unauthenticated remote attacker to conduct SQL injection attacks against an affected AOS-8 instance. Successful exploitation could allow an attacker to execute arbitrary commands on the underlying operating system.

### 44. CVE-2026-79848｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:56.850)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00539 / percentile=0.44613
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:56.850 / 2026-10-23T20:17:22.353
- **官方描述（原文）**：Vulnerabilities in the affected interface of AOS-8 could allow an unauthenticated remote attacker to conduct SQL injection attacks against an affected AOS-8 instance. Successful exploitation could allow an attacker to execute arbitrary commands on the underlying operating system.

### 45. CVE-2026-79847｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:56.633)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00499 / percentile=0.41876
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:56.633 / 2026-10-23T20:17:22.247
- **官方描述（原文）**：Buffer overflow vulnerabilities in the affected interface of AOS-10 could lead to unauthenticated remote code execution by sending specially crafted packets to the affected interface. Successful exploitation of this vulnerability results in the ability to execute arbitrary code as a privileged user on the underlying operating system.

### 46. CVE-2026-79846｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:56.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00499 / percentile=0.41876
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:56.490 / 2026-10-23T20:17:22.130
- **官方描述（原文）**：Command injection vulnerabilities exist in the affected interface of AOS-8 that could allow an unauthenticated remote attacker to run arbitrary commands on the underlying host if certain preconditions outside of the attacker's control are met. Successful exploitation could allow an attacker to execute arbitrary commands on the underlying operating system.

### 47. CVE-2026-79844｜Hewlett Packard Enterprise (HPE) / ArubaOS (AOS)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:56.367)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.004 / percentile=0.33077
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:56.367 / 2026-10-23T20:17:22.017
- **官方描述（原文）**：Authentication bypass vulnerabilities in the affected interface of AOS-10 could allow an unauthenticated remote attacker to run arbitrary commands on the underlying host if certain preconditions outside of the attacker's control are met. Successful exploitation could allow an attacker to execute arbitrary commands on the underlying operating system.

### 48. CVE-2026-63244｜WizLearn Technologies Pte. Ltd. / Learning Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T08:16:55.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00536 / percentile=0.44389
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T08:16:55.320 / 2026-10-23T19:57:42.660
- **官方描述（原文）**：An authentication bypass vulnerability in WizLearn Technologies' Learning Management System (LMS) could allow an unauthenticated remote attacker to bypass password authentication and the OAuth authentication flow by sending a specially crafted POST request, potentially resulting in unauthorised access to user accounts and full administrative control of the LMS platform.

### 49. CVE-2026-57116｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:10.690)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:10.690 / 2026-10-23T13:17:10.827
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. From version 4.2.1 to before version 4.6.59, PraisonAI's AgentOS FastAPI deployment surface remains unauthenticated in current main and in releases after the published patched version for GHSA-pm96-6xpr-978x / CVE-2026-40151. The chat route directly calls agent.chat(request.message). No-auth and wrong-bearer requests both execute the deployed agent. This is broader than passive metadata disclosure. In any deployment where AgentOS wraps agents with tools, private context, memory, API integrations, or cost-bearing model calls, an unauthenticated reachable client can drive those agents. This issue has been patched in version 4.6.59.

### 50. CVE-2026-55981｜Creative Labs / Creative Sound Blaster Katana V2, V2X, SE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T07:16:38.420)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00304 / percentile=0.21992
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T07:16:38.420 / 2026-10-23T19:42:24.553
- **官方描述（原文）**：A firmware verification vulnerability in Creative Sound Blaster Katana could allow an attacker to modify a legitimate firmware image and upload the modified firmware to an affected device.

### 51. CVE-2026-55486｜intranda / goobi-viewer-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T15:17:33.657)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T15:17:33.657 / 2026-10-23T16:28:32.357
- **官方描述（原文）**：The Goobi viewer is a web application that allows digitised material to be displayed in a web browser. From version 25.08 to before version 26.05, the IIIF Auth 2.0 endpoints auth/login and auth/token in AuthorizationFlowResource accept an origin query parameter without validation and then (1) embed it into the Content-Security-Policy: frame-ancestors response header and (2) embed it into an HTML response body as a JavaScript single-quoted postMessage argument. Because the attacker controls both the login and token calls that initiate the flow, the unescaped value yields reflected XSS. This issue has been patched in version 26.05.

### 52. CVE-2026-54630｜Part-DB / Part-DB-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T04:18:17.007)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00234 / percentile=0.13475
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T04:18:17.007 / 2026-10-23T19:36:32.410
- **官方描述（原文）**：Part-DB is an open source inventory management system for electronic components. Prior to version 2.12.1, the part attachment upload handler stores uploaded files under the web-served media directory using the client-supplied file extension, and its extension blocklist does not include phar. AttachmentSubmitHandler::renameBlacklistedExtensions() rewrites dangerous extensions (php, phtml, sh, cgi, py, js, html, htaccess, ...) to .txt, but phar is absent from the list, so a .phar file keeps its extension. Public attachments (the default) are written into public/media/, which is the Apache document root. The shipped Apache configuration routes .phar to PHP-FPM, so the stored file is executed as PHP on request. The per-attachment-type extension filter is empty by default and is not consulted by the upload handler in a way that blocks this, and a non-admin user in the default users group can create an attachment type with no filter and attach files to parts. Any authenticated user in the default users group uploads a .phar attachment to a part and fetches it under /media/, executing arbitrary PHP as the www-data web user. Ability to exploit depends on the webserver config, docker image contained the vulnerability by default. This issue has been patched in version 2.12.1.

### 53. CVE-2026-53942｜conda / infrastructure
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T15:17:32.157)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T15:17:32.157 / 2026-10-23T19:42:24.553
- **官方描述（原文）**：Conda Organization Infrastructure is a centralized location for infrastructure codes. Prior to commit 9c0f238, a GitHub Actions Pwn Request vulnerability appears to remain present in conda/conda. The affected workflow is .github/workflows/update.yml. It is triggered by issue_comment events containing @conda-bot render or @conda-bot recreate. For the render path, the workflow obtains the pull request head repository and branch from the PR API, checks out that PR-controlled repository/ref using secrets.SYNC_TOKEN, and then runs conda/actions/template-files@7f6830b1428a9bd47f0b068892c77eae95207037. The external template-files action reads its default configuration and templates from the checked-out working directory. In the confirmed finding, that action uses an unsandboxed Jinja2 environment to render attacker-controlled template content. This creates a Pwn Request chain in which an untrusted PR/comment path can reach template rendering in a privileged token context. This issue has been patched via commit 9c0f238.

### 54. CVE-2026-53921｜openwrt / odhcpd
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T14:17:53.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T14:17:53.710 / 2026-10-23T19:37:11.060
- **官方描述（原文）**：odhcpd is the DHCPv6, DHCPv4, and router-advertisement server used by OpenWrt. Prior to version 25.12, odhcpd's DHCPv6 IA response handler writes past the end of a fixed 512-byte stack buffer (pdbuf) when a single DHCPv6 REQUEST carries enough IA options to nearly exhaust the reply space. Two independent overflow sites exist in the same call chain, both reachable from the network via a single unauthenticated UDP packet. odhcpd runs as root on OpenWrt; embedded targets often lack stack canaries and ASLR, making code execution realistic. This issue has been patched in version 25.12.

### 55. CVE-2026-46652｜intranda / goobi-viewer-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T15:17:31.593)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T15:17:31.593 / 2026-10-23T16:28:32.357
- **官方描述（原文）**：The Goobi viewer is a web application that allows digitised material to be displayed in a web browser. From version 24.03 to before version 26.05, ExternalFilesDownloader.getFilename() extracts the destination filename from a server-supplied Content-Disposition response header and passes it directly to Path.resolve() without stripping directory components. This allows for a malicious HTTP server that the viewer fetches from to supply an absolute path or ../ traversal sequences as the filename, writing attacker-controlled content to an arbitrary path writable by the Tomcat process. When targeting the deployed web-application directory, this yields remote code execution as the tomcat OS user. This issue has been patched in version 26.05.

### 56. CVE-2026-46651｜intranda / goobi-viewer-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T15:17:31.453)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T15:17:31.453 / 2026-10-23T16:28:32.357
- **官方描述（原文）**：The Goobi viewer is a web application that allows digitised material to be displayed in a web browser. From version 24.03 to before version 26.05, the DownloadTaskEndpoint WebSocket endpoint (/tasks/download/monitor.socket) in goobi-viewer-core accepts download requests from unauthenticated users. This issue has been patched in version 26.05.

### 57. CVE-2026-25784｜Hallo Welt! GmbH / BlueSpice
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T09:17:06.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00345 / percentile=0.26906
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T09:17:06.943 / 2026-10-23T19:57:42.660
- **官方描述（原文）**：Initialization of a Resource with an Insecure Default vulnerability in Hallo Welt! GmbH BlueSpice (container image bluespice/wiki) allows privilege escalation. The default value of $mwsgTokenAuthenticatorServiceCIDR in the container's LocalSettings.php was intended to restrict internal service authentication to the container network, but evaluated to an empty string when the environment variable WIKI_SERVICE_TOKEN_AUTH_ALLOWED was not set. An empty value disables the IP restriction in the token authenticator component (mwstake/mediawiki-component-token-authenticator). As a result, any user with read access to the wiki (anonymous users on publicly readable wikis) could obtain an application token from the REST API and use it to get a session with sysop privileges as the internal service user. This issue affects BlueSpice: from 5.2.3 before 5.2.7, and the 5.2.7 container images published before 2026-10-19 15:37 UTC.

### 58. CVE-2026-19677｜onPhase / onPhase Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T02:16:57.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T02:16:57.560 / 2026-10-23T19:45:03.547
- **官方描述（原文）**：An authentication bypass vulnerability in the public onPhase/ frevvo registration form version 11.0.14 allows an unauthenticated remote attacker to authenticate as an arbitrary tenant user, obtain TenantAdmin and Designer privileges, and execute arbitrary operating system commands via manipulation of registration parameters containing a valid tenant name and existing user identifier.

### 59. CVE-2026-115931｜GitroomHQ / postiz-app
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T23:17:43.263)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T23:17:43.263 / 2026-10-23T23:17:43.263
- **官方描述（原文）**：Postiz lets a signed-in user ask the backend to run a function on one of their connected channels. The backend did not restrict which functions can be requested, so a user could call internal helper functions that were never meant to be reachable from the web interface. One of those helpers reads a file from the server's disk. A user who connects a channel whose stored token is a file path can have the backend return the contents of any file it can read, including its environment, which holds the secret used to sign login sessions, the database address and the credentials of connected services. Another helper makes the backend process exit with a single request. Self-registration is open by default, so no existing account and no action by another user is needed.

### 60. CVE-2026-115893｜bytecodealliance / wasmtime
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T22:16:58.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T22:16:58.820 / 2026-10-23T22:16:58.947
- **官方描述（原文）**：Wasmtime is a runtime for WebAssembly. Prior to 36.0.19, 48.0.7, and 49.0.4, the Cranelift compiler backend on aarch64 can compile a Wasm br_table instruction with more than approximately 256,000 targets so that it has an incorrect conditional branch target. The branch can then jump to arbitrary other code at a user-controlled offset, allowing a user-controlled Wasm module to escape the sandbox on aarch64 engines using the default Cranelift backend. This issue is fixed in versions 36.0.19, 48.0.7, and 49.0.4.

### 61. CVE-2026-115889｜bytecodealliance / wasmtime
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T22:16:58.400)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T22:16:58.400 / 2026-10-23T22:16:58.550
- **官方描述（原文）**：Wasmtime is a runtime for WebAssembly. Prior to 36.0.19 and 43.0.0, the Cranelift compiler backend bit-packs SSA value indices in a way that can silently overflow in release builds when compiling a sufficiently large or specially crafted Wasm function with many SSA values. The overflow can make Cranelift reference incorrect IR values, causing arbitrary miscompilation, type confusion, and other attacker-controlled effects that may escape the Wasm sandbox on any architecture using the default Cranelift backend. This issue is fixed in versions 36.0.19 and 43.0.0.

### 62. CVE-2026-115812｜AWS / multi-model-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T18:17:21.460)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T18:17:21.460 / 2026-10-23T19:23:01.467
- **官方描述（原文）**：Relative path traversal during model archive extraction in Amazon Web Services Multi Model Server 1.1.11 and earlier might allow remote actors to execute arbitrary code via a crafted model archive. Multi Model Server is end of life and no fixed version is available. Users should discontinue use of Multi Model Server and migrate to a supported model serving solution.

### 63. CVE-2026-115727｜Fosowl / AgenticSeek
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T12:18:13.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T12:18:13.560 / 2026-10-23T15:17:30.460
- **官方描述（原文）**：AgenticSeek before commit 409840c contains a remote code execution vulnerability because llm_server/app.py hardcodes Flask debug mode while binding to all interfaces. Attackers who reach the server port and obtain the derivable Werkzeug debugger PIN can execute Python code and operating system commands with llm_server privileges.

### 64. CVE-2026-115547｜Okta / Okta Access Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T04:18:16.030)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00444 / percentile=0.37653
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T04:18:16.030 / 2026-10-23T16:44:17.950
- **官方描述（原文）**：An input validation issue in the Okta Access Gateway (OAG) Admin Console allows the processing of specially formatted configuration values. An authenticated administrator can leverage this to execute system commands within the context of the OAG service account.

### 65. CVE-2026-115384｜bytecodealliance / wasmtime
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:45.543)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00312 / percentile=0.22857
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:45.543 / 2026-10-22T19:17:45.653
- **官方描述（原文）**：Wasmtime 39.0.0 before 48.0.4 and 49.0.0 before 49.0.2 contains a stack buffer overflow vulnerability that allows malicious guests to write ~16KB to the native stack via unvalidated async callback result types. Attackers can supply components with mistyped component-model-async callback functions to overwrite return addresses, crashing the host or escaping the sandbox.

### 66. CVE-2026-115377｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:44.460)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00405 / percentile=0.33657
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:44.460 / 2026-10-23T17:06:36.030
- **官方描述（原文）**：Incus before 6.0.7, 6.1.0 before 7.0.2, and 7.1.0 before 7.5.0 contains an arbitrary file write vulnerability that allows malicious migration sources to write host files by planting symlinks in transferred volumes. Attackers can craft rsync or btrfs receive streams with a symlink such as rootfs pointing to the host root, writing files as root for full host compromise.

### 67. CVE-2026-115375｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:44.133)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00405 / percentile=0.33657
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:44.133 / 2026-10-23T17:06:36.030
- **官方描述（原文）**：Incus 7.0.0 before 7.0.2 and 7.1.0 before 7.5.0 contains a path traversal vulnerability that allows clients able to create instances to write files on the host. The flaw stems from unvalidated dependent custom volume names in instance backup index.yaml files. Attackers can import a crafted instance backup with ../ sequences in dependent volume names to create root-owned directories with controlled content, leading to full host compromise.

### 68. CVE-2026-115372｜lxc / incus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:43.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：0.00362 / percentile=0.28816
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:43.670 / 2026-10-23T17:06:36.030
- **官方描述（原文）**：Incus from 7.3.0 before 7.5.0 contains a project restriction bypass that allows restricted project users to set block.create_options through volume update, copy, and move operations. Attackers can set the option on a custom volume and trigger a copy or move onto a formatting pool to inject arguments into mkfs executed as root.

### 69. CVE-2026-115353｜lepture / mistune
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:41.227)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00387 / percentile=0.31651
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:41.227 / 2026-10-22T19:17:41.337
- **官方描述（原文）**：Mistune before 3.3.0 contains a path traversal vulnerability in the RST include directive that allows attackers to read arbitrary files by supplying relative or absolute paths. Attackers can submit markdown containing include directives referencing ../ sequences or absolute paths to embed sensitive files like credentials or environment data in rendered HTML.

### 70. CVE-2026-115324｜mem0ai / mem0
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T11:17:51.263)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00326 / percentile=0.24489
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T11:17:51.263 / 2026-10-22T17:39:56.760
- **官方描述（原文）**：mem0 0.1.117 before 1.0.8 contains an sql injection vulnerability in mem0/vector_stores/databricks.py that allows attackers to inject SQL by influencing stored memory content. Attackers can supply crafted memory text, metadata, or message names that reach unescaped insert() and update() string interpolation to execute injected SQL on the configured Databricks SQL warehouse.

### 71. CVE-2026-114612｜BerriAI / litellm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:37.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00235 / percentile=0.13629
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:37.540 / 2026-10-23T19:42:24.553
- **官方描述（原文）**：LiteLLM is a proxy server (AI Gateway) to call LLM APIs in OpenAI (or native) format. From 1.87.0 until 1.100.4, 1.101.3, 1.102.2, 1.103.1, and 1.104.0-rc.2, the proxy reuses one cryptographic context for at-rest secrets and session tokens, allowing an authenticated internal user to have crafted metadata containing a forged administrator credential encrypted and returned by the API-key flow. Replaying that ciphertext as a bearer token causes the proxy to trust the forged proxy administrator identity, permitting administrative access and arbitrary commands through the MCP stdio endpoint. Versions 1.87.0 through 1.90.x require EXPERIMENTAL_UI_LOGIN to be enabled, while versions after 1.91.0 are exploitable in the default configuration. This issue was fixed in LiteLLM 1.100.4, 1.101.3, 1.102.2, 1.103.1, and 1.104.0-rc.2.

### 72. CVE-2026-114611｜schorschii / OCO-Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T18:17:28.377)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00229 / percentile=0.1293
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T18:17:28.377 / 2026-10-23T19:57:42.660
- **官方描述（原文）**：OCO-Server is a self-hosted endpoint management application for computer inventory, software deployment, and mobile device management. Prior to 1.2.3,the Apple MDM enrollment endpoint `frontend/api-mdm.php` verifies the signed enrollment-request plist with `openssl_pkcs7_verify(..., PKCS7_NOVERIFY, ...)`. `PKCS7_NOVERIFY` disables signer certificate chain and trust validation, so the signature only has to be self-consistent with whatever certificate is embedded in the PKCS#7 blob. A self-signed certificate from an unrelated attacker is accepted. Because the endpoint trusts the `SERIAL` field taken from the unverified payload, anyone who knows a registered device's serial number can sign a forged plist (`SERIAL` = victim device, attacker-chosen `UDID`) with an arbitrary self-signed certificate; POST it unauthenticated to `/api-mdm.php/profile` (Content-Type: `application/pkcs7-signature`); and receive the victim device's freshly minted MDM identity: a certificate with `CN=<serial>` issued by the server's internal MDM device CA, bundled with its private key in a PKCS#12 payload inside the returned `.mobileconfig` enrollment profile. Additionally, the victim's `mobile_device` database row is silently overwritten with the attacker-supplied `UDID` (device-record hijack). With the stolen certificate and key, the attacker can impersonate the victim device on all subsequent MDM traffic (`/checkin`, `/mdm`, `/parameters`), which authenticate callers by the certificate CN (the serial number) via `checkSignature()` in the same file. This yields control over the victim device's MDM relationship: reading its management data, replacing its push token, and disrupting or redirecting its enrollment. Version 1.2.3 fixes the issue.

### 73. CVE-2026-114607｜better-auth / better-auth
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T17:16:58.577)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00347 / percentile=0.27075
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T17:16:58.577 / 2026-10-23T15:17:26.763
- **官方描述（原文）**：Better Auth is an authentication and authorization library for TypeScript. From 1.4.0-beta.18 until 1.7.7, deployments that enable Magic Link with storeToken set to plain, or with storeToken set to hashed and the global verification.storeIdentifier setting also set to hashed, enable a built-in social or Generic OAuth provider, and use account.storeStateStrategy set to database can accept an OAuth sign-in state value as a Magic Link token. These settings can cause Magic Link verification records and OAuth state to resolve to the same stored identifier, allowing an unauthenticated attacker to start OAuth sign-in for a known email address and redeem the returned state through Magic Link without controlling the mailbox or completing the provider callback. The attacker can obtain a normal session for an existing user, or create an account incorrectly marked as email verified when sign-up is enabled. This issue is fixed in version 1.7.7.

### 74. CVE-2026-114357｜DJI / CrystalSky ZS600C
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T14:17:49.820)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T14:17:49.820 / 2026-10-23T16:28:32.357
- **官方描述（原文）**：Missing authentication for a critical function in the Android Debug Bridge daemon (adbd) in DJI CrystalSky ZS600C firmware v0.3.9.7 through v0.6.6.9 allows an attacker to obtain an unauthenticated shell (uid 2000), a foothold for privilege escalation to root. The device ships with ro.adb.secure=0 (no host key authorization) and USB ADB enabled by default; ADB over TCP is not enabled by default but, once enabled (e.g. via the shipped /system/bin/adbd_tcp.sh or 'setprop persist.adb.tcp.port 5555'), the same unauthenticated shell is reachable over the network (CVSS 4.0 base 9.3).

### 75. CVE-2026-114220｜NewType Infortech / NT OneAPP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T05:16:50.020)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00158 / percentile=0.04575
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T05:16:50.020 / 2026-10-22T19:17:37.153
- **官方描述（原文）**：NT OneAPP developed by NewType Infortech has an Improper Certificate Validation vulnerability. Unauthenticated network-adjacent attackers can perform a man-in-the-middle attack by failing to validate the server certificate and the hostname, thereby intercepting or modifying communications between the application and the server.

### 76. CVE-2026-114219｜NewType Infortech / NT OneAPP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T05:16:49.170)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00272 / percentile=0.18521
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T05:16:49.170 / 2026-10-22T19:17:37.027
- **官方描述（原文）**：NT OneAPP developed by NewType Infortech has a Hard-coded Credentials vulnerability. Unauthenticated remote attackers can obtain the hard-coded cryptographic key and decrypt login request contents, thereby obtaining users' plaintext account credentials and device information.

### 77. CVE-2026-112862｜xnau webdesign / Participants Database
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T09:17:06.393)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00313 / percentile=0.23039
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T09:17:06.393 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in xnau webdesign Participants Database participants-database allows Object Injection.This issue affects Participants Database: from n/a through 2.7.8.5.

### 78. CVE-2026-112860｜xnau webdesign / Participants Database
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T09:17:06.280)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.00236 / percentile=0.13829
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T09:17:06.280 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in xnau webdesign Participants Database participants-database allows Blind SQL Injection.This issue affects Participants Database: from n/a through 2.7.8.5.

### 79. CVE-2026-112859｜ThemeREX Group / Little Birdies
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:07.700)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:07.700 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Little Birdies little-birdies allows Object Injection.This issue affects Little Birdies: from n/a through 1.3.16.

### 80. CVE-2026-112858｜axiomthemes / Rhodos
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:07.573)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:07.573 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in axiomthemes Rhodos rhodos allows Object Injection.This issue affects Rhodos: from n/a through 1.3.3.

### 81. CVE-2026-112857｜axiomthemes / Reprizo
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:07.447)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:07.447 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in axiomthemes Reprizo reprizo allows Object Injection.This issue affects Reprizo: from n/a through 1.0.8.

### 82. CVE-2026-112856｜ThemeREX Group / Vagabonds
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:07.323)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:07.323 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Vagabonds vagabonds allows Object Injection.This issue affects Vagabonds: from n/a through 1.3.10.

### 83. CVE-2026-112855｜axiomthemes / Redy
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:07.197)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:07.197 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in axiomthemes Redy redy allows Object Injection.This issue affects Redy: from n/a through 1.3.5.

### 84. CVE-2026-112854｜axiomthemes / Holistic Center
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:07.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:07.070 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in axiomthemes Holistic Center holistic-center allows Object Injection.This issue affects Holistic Center: from n/a through 1.2.6.

### 85. CVE-2026-112853｜axiomthemes / Hallelujah
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:06.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:06.940 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in axiomthemes Hallelujah hallelujah allows Object Injection.This issue affects Hallelujah: from n/a through 1.1.1.

### 86. CVE-2026-112851｜ThemeREX Group / HotLock
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:06.697)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:06.697 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group HotLock hotlock allows Object Injection.This issue affects HotLock: from n/a through 1.3.9.

### 87. CVE-2026-112848｜AivahThemes / Hostme v2
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:06.310)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:06.310 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in AivahThemes Hostme v2 hostmev2 allows Object Injection.This issue affects Hostme v2: from n/a through 7.0.

### 88. CVE-2026-112847｜ThemeREX / ZenSoul
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:06.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:06.190 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX ZenSoul zensoul allows Object Injection.This issue affects ZenSoul: from n/a through 1.13.

### 89. CVE-2026-112846｜ThemeREX Group / Save Life
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T13:17:06.057)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T13:17:06.057 / 2026-10-23T16:06:31.143
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Save Life save-life allows Object Injection.This issue affects Save Life: from n/a through 1.2.14.

### 90. CVE-2026-112832｜CozyThemes / Rootblox
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T11:17:33.163)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.0044 / percentile=0.37186
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T11:17:33.163 / 2026-10-22T15:15:23.833
- **官方描述（原文）**：Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in CozyThemes Rootblox rootblox allows PHP Local File Inclusion.This issue affects Rootblox: from n/a through 1.0.6.

### 91. CVE-2026-112327｜TMS / Amelia
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T09:17:14.680)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.00241 / percentile=0.14438
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T09:17:14.680 / 2026-10-22T15:15:23.833
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in TMS Amelia ameliabooking allows SQL Injection.This issue affects Amelia: from n/a through 2.4.11.

### 92. CVE-2026-112241｜Brainstorm Force / SureCart
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T09:17:14.157)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00346 / percentile=0.26952
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T09:17:14.157 / 2026-10-22T15:15:23.833
- **官方描述（原文）**：Authentication Bypass by Spoofing vulnerability in Brainstorm Force SureCart surecart allows Authentication Abuse.This issue affects SureCart: from n/a through 4.9.5.

### 93. CVE-2026-111594｜InterSystems / IRIS for Health
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T22:18:01.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00183 / percentile=0.0753
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T22:18:01.060 / 2026-10-23T19:43:46.190
- **官方描述（原文）**：InterSystems IRIS for Health has TLS/SSL encryption turned off by default, which may enable an attacker to view transmitted data and use that data to log into the device.

### 94. CVE-2026-111497｜Google / Brotli
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T14:17:37.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.0048 / percentile=0.40511
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T14:17:37.190 / 2026-10-24T04:18:17.357
- **官方描述（原文）**：A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream. Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1.2.1.

### 95. CVE-2026-110243｜Kiloview / E3 Firmware
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T23:18:22.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00395 / percentile=0.32577
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T23:18:22.520 / 2026-10-23T19:57:42.660
- **官方描述（原文）**：The network management service on affected Kiloview E3 NDI encoder firmware fails to validate the network interface name accepted by its link maintenance address configuration endpoint before passing it to a shell command, unlike sibling handlers that perform the same validation. An authenticated web user with permission to configure network settings can exploit this to execute arbitrary operating system commands as root.

### 96. CVE-2026-110063｜Microsoft / VM Inspector for Azure Virtual Machines
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T22:18:00.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.00888 / percentile=0.58949
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T22:18:00.750 / 2026-10-23T19:43:46.190
- **官方描述（原文）**：Improper link resolution before file access ('link following') in VM Inspector for Azure Virtual Machines allows an unauthorized attacker to elevate privileges over a network.

### 97. CVE-2026-109619｜PHP Group / PHP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T14:17:09.823)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.05991 / percentile=0.933
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T14:17:09.823 / 2026-10-23T16:06:48.917
- **官方描述（原文）**：PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

### 98. CVE-2026-109122｜Kiloview / E3 Firmware
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T22:17:59.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00403 / percentile=0.33467
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T22:17:59.930 / 2026-10-23T19:57:42.660
- **官方描述（原文）**：The network management service on affected Kiloview E3 NDI encoder firmware fails to sanitize one field used when configuring static routes via the web management API. An authenticated web user with permission to configure static routes can exploit this to execute arbitrary operating system commands as root, and the malicious configuration persists across reboots. Successful exploitation could result in full device compromise, including exposure of stored credentials and cryptographic material.

### 99. CVE-2026-107861｜Kiloview / E3 Firmware
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T23:18:17.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00395 / percentile=0.32577
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T23:18:17.190 / 2026-10-23T19:57:42.660
- **官方描述（原文）**：The system control service on affected Kiloview E3 NDI encoder firmware fails to sanitize the hostname parameter accepted by its device naming endpoint, passing it unquoted into a shell command. An authenticated web user with access to this function can embed characters to execute arbitrary operating system commands as root, resulting in full device compromise.

### 100. CVE-2026-107685｜agentjido / req_llm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T12:18:06.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T12:18:06.410 / 2026-10-23T19:57:42.660
- **官方描述（原文）**：Improper Certificate Validation vulnerability in the WebSocket streaming client in agentjido req_llm allows an on-path attacker to read and modify OpenAI WebSocket sessions, including the authorization bearer token, via a TLS certificate the client does not trust. ReqLLM.Streaming.WebSocketSession.Client.start/3 in lib/req_llm/streaming/web_socket_session/client.ex starts WebSockex without TLS options, and WebSockex defaults to insecure: true, which connects with verify: :verify_none. The option allowlist also drops any caller-supplied cacerts or ssl_options, so an application cannot turn verification on. The OpenAI Responses, Realtime, and Codex WebSocket paths reach this client and send the API key or OAuth access token in the authorization header. HTTP streaming through Finch and the HTTP/2 duplex session through Mint verify certificates and are not affected. This issue affects req_llm: from 1.9.0 before 1.29.0.

### 101. CVE-2026-105014｜Microsoft / Azure Pipelines
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T22:17:52.183)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00667 / percentile=0.51316
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T22:17:52.183 / 2026-10-24T04:18:16.820
- **官方描述（原文）**：Improper neutralization of special elements used in a command ('command injection') in Azure Pipelines allows an unauthorized attacker to execute code over a network.

### 102. CVE-2026-102785｜yootheme.com / YOOtheme Pro extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T13:17:27.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.00701 / percentile=0.52688
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T13:17:27.470 / 2026-10-22T17:36:46.950
- **官方描述（原文）**：Joomla Extension - yootheme.com - Unauthenticated remote code execution in YOOtheme Pro 5.0.0-5.0.52 - YOOtheme Pro’s publicly accessible image transformation handler incompletely binds normalized image operations and the output destination to its request signature. An unauthenticated remote attacker can reuse a signature disclosed in a legitimate public image URL, inject additional image operations, traverse out of the intended cache directory, and write an attacker-controlled PNG/PHP polyglot to an executable public media directory.

### 103. CVE-2025-30054｜CGM / CGM CLININET
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T09:17:05.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T09:17:05.290 / 2026-10-23T16:28:32.357
- **官方描述（原文）**：CGM CLININET is vulnerable to local privilege escalation. The service that processes incoming HL7 messages runs with root privileges, but due to incorrect permissions, its scripts and configuration files can be modified by the uhcapache user. An attacker with uhcapache privileges can modify these files to execute arbitrary code as root. The vulnerability was confirmed to affect versions up to 2026.MS3 but later versions may also be vulnerable.

### 104. CVE-2025-30050｜CGM / CGM CLININET
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T09:17:04.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T09:17:04.810 / 2026-10-23T16:28:32.357
- **官方描述（原文）**：CGM CLININET is vulnerable to Code Injection in the RunCGI.pm component, which dynamically imports the module specified as a query parameter and executes code from untrusted data provided by the user. An attacker from adjacent network can supply a crafted query parameter to have an attacker-controlled module imported which results in arbitrary code execution with root privileges. This issue was fixed in version 2026.MS3

### 105. CVE-2025-30047｜CGM / CGM CLININET
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T09:17:04.573)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T09:17:04.573 / 2026-10-23T16:28:32.357
- **官方描述（原文）**：CGM CLININET is vulnerable to Remote Code Execution caused by deserialization of untrusted data. The server exposes an HTTP-based API, used by the administrative module, that exchanges data using Java object serialization. An attacker within the same local network is able to send requests to this API and transmit a crafted serialized object. When it is deserialized, it allows arbitrary code execution with root privileges on the server. This issue was fixed in version 2026.MS3

### 106. CVE-2025-30046｜CGM / CGM CLININET
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-23T09:17:04.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-23T09:17:04.450 / 2026-10-23T16:28:32.357
- **官方描述（原文）**：In the CGM CLININET application server, multiple processes responsible for HL7 communication with external systems run with root privileges while processing untrusted data received from those external systems. An attacker in adjacent network able to send data to these HL7 communication processes can achieve remote code execution with root privileges. The vulnerability was confirmed to affect versions up to 2026.MS3 but later versions may also be vulnerable.

### 107. CVE-2022-51026｜bytebase / bytebase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T19:17:30.883)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00613 / percentile=0.48722
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T19:17:30.883 / 2026-10-23T19:57:42.660
- **官方描述（原文）**：Bytebase 0.12.0 before 1.0.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to log in as any user. The flaw stems from trusting client-supplied GitLab provider configuration in the POST /api/auth/login/GITLAB_SELF_HOST endpoint. Attackers can set instanceUrl to a server they control that returns an active user with a chosen email. Bytebase then issues session tokens for that principal, letting attackers impersonate existing users including the Owner or create new members.

### 108. CVE-2021-48016｜DedeCMS / DedeCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T11:17:04.690)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00441 / percentile=0.37258
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T11:17:04.690 / 2026-10-22T17:40:46.877
- **官方描述（原文）**：DedeCMS through 5.8.1-beta contains a PHP code injection vulnerability in ShowMsg() where the HTTP Referer header is written into a DedeTemplate string and included. Unauthenticated attackers can send a crafted Referer to /plus/flink.php?dopost=save with an empty validate code to execute arbitrary PHP and system commands. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 109. CVE-2026-114400｜polonel / trudesk
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T13:18:31.217)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：0.00523 / percentile=0.43558
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T13:18:31.217 / 2026-10-23T19:17:44.007
- **官方描述（原文）**：Trudesk through 1.2.11 contains a missing authentication vulnerability that allows unauthenticated attackers to download private ticket attachments under /uploads. Because express.static serves the public/ directory before the hasAuth-guarded /uploads mount, attackers who know or guess a ticket ObjectId and filename can retrieve confidential attachments.

### 110. CVE-2026-114396｜polonel / trudesk
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T13:18:30.493)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00477 / percentile=0.4026
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T13:18:30.493 / 2026-10-22T15:44:59.783
- **官方描述（原文）**：Trudesk through 1.2.11 contains a server-side JavaScript injection vulnerability that allows authenticated users to inject code into a MongoDB $where clause via the search parameter. Attackers can close the regular expression in GET /api/v1/tickets/search to loop mongod for denial of service or leak full ticket documents including internal notes.

### 111. CVE-2026-114117｜vyperlang / vyper
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T01:17:38.070)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：0.00207 / percentile=0.10206
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T01:17:38.070 / 2026-10-22T17:00:33.203
- **官方描述（原文）**：Vyper 0.3.8 through 0.5.0b1 contains an optimizer miscompilation in which (msg.value | K) or (len(msg.data) | K), where K is any nonzero integer literal, is compiled to the constant 1 when used as a ternary expression branch under -O gas (the default) or -O codesize. Affected contracts use the wrong value in storage writes, arithmetic, indexes, return values, or events without warning or revert, which can record deposits incorrectly and lock funds.

### 112. CVE-2026-114102｜cthackers / adm-zip
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T01:17:35.897)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.00291 / percentile=0.20546
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T01:17:35.897 / 2026-10-22T16:17:34.273
- **官方描述（原文）**：adm-zip before 0.6.1 contains a denial of service vulnerability that allows unauthenticated attackers to crash the Node.js process via a malformed ZIP file, because inflateAsync in methods/inflater.js lacks a zlib stream error listener. Attackers can supply a ZIP with corrupted DEFLATE data processed by readFileAsync, readAsTextAsync, extractAllToAsync, or getDataAsync, triggering an uncatchable exception that terminates all in-flight requests.

### 113. CVE-2026-114092｜triggerdotdev / trigger.dev
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T01:17:34.247)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：0.00436 / percentile=0.36868
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T01:17:34.247 / 2026-10-22T16:17:33.980
- **官方描述（原文）**：Trigger.dev before 4.5.0 performs no authentication or organization check in the action handler of the dashboard run replay route (resources.taskruns.$runParam.replay) and looks up the run by friendlyId alone. A remote attacker who knows a victim's run friendlyId can replay it into an environment of their choosing, exposing the victim's task payload or running the task again with the victim's secrets.

### 114. CVE-2026-114067｜triggerdotdev / trigger.dev
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T01:17:30.250)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T01:17:30.250 / 2026-10-22T18:17:27.520
- **官方描述（原文）**：Trigger.dev 4.5.0 before 4.6.2 contains an improper authorization vulnerability in the PUT snapshot-url session endpoint that allows public session token holders to obtain presigned S3 write URLs. End users can overwrite their own session's durable chat snapshot to forge the agent's conversation history, since the route lacks a secret-key-only check.

### 115. CVE-2026-114042｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T01:17:26.513)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00254 / percentile=0.16016
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T01:17:26.513 / 2026-10-22T19:17:36.527
- **官方描述（原文）**：FreeRDP 3.32.0 contains a use-after-free vulnerability in the drdynvc channel that frees a pool-owned stream with the owned-stream deallocator when totalLength is smaller than the chunk size. A malicious RDP server can send a single well-formed Virtual Channel PDU to trigger the free and crash the client during teardown.

### 116. CVE-2026-113722｜pypa / virtualenv
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T20:17:18.810)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.00167 / percentile=0.05685
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T20:17:18.810 / 2026-10-23T02:16:57.087
- **官方描述（原文）**：virtualenv is a tool for creating isolated virtual python environments. Prior to 21.14.9, virtualenv's ScriptMakerCustom and pip pass an incompletely quoted interpreter path to distlib ScriptMaker when generating POSIX console scripts. When the path contains a space or produces a shebang longer than 127 bytes, distlib emits a /bin/sh wrapper whose double-quoted interpreter path still expands command substitutions and backticks. An attacker who influences the environment destination can therefore execute commands with the user's privileges when the user later runs a generated launcher; environment creation and activation do not trigger the command. Existing launchers are not repaired by upgrading virtualenv alone and must be regenerated, while a later independent pip installation or upgrade can reintroduce an affected launcher because pip's vendored distlib is unchanged. The virtualenv fix is released in version 21.14.9.

### 117. CVE-2026-113658｜apostrophecms / apostrophe
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T17:17:36.917)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00538 / percentile=0.44539
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T17:17:36.917 / 2026-10-23T02:16:56.200
- **官方描述（原文）**：ApostropheCMS is an open-source Node.js content management system. Prior to 4.33.0, the unauthenticated Rich Text CSV conversion route writes a multipart upload to the system temporary directory before checking its extension and does not remove the staged file when that validation rejects it. Repeated large rejected uploads, using the normal public CSRF cookie, can persistently consume temporary-disk capacity and may disrupt ApostropheCMS and other services that depend on the same partition. This issue is fixed in version 4.33.0.

### 118. CVE-2026-113606｜Stirling-Tools / Stirling-PDF
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T16:17:10.623)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00298 / percentile=0.2131
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T16:17:10.623 / 2026-10-23T02:16:55.600
- **官方描述（原文）**：Stirling-PDF 3.0.0 through 3.2.0 contains an authorization bypass vulnerability that allows authenticated users to access other users' stored files by pointing a processing folder at the server storage directory. Attackers can create a folder via POST /api/v1/processing-folders targeting storage/<victimUserId>, list files, and run pipelines to read, modify, or destroy victims' files.

### 119. CVE-2026-113390｜DrayTek / Vigor2960
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T13:16:40.463)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：0.02136 / percentile=0.81881
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T13:16:40.463 / 2026-10-22T22:18:03.607
- **官方描述（原文）**：A flaw has been found in DrayTek Vigor2960 1.5.1.6 Revision 8218. Affected by this issue is the function sub_182B0 of the file /cgi-bin/mainfunction.cgi of the component CGI Interface. This manipulation of the argument usefile/usescript/option causes os command injection. Remote exploitation of the attack is possible. The exploit has been published and may be used. The vendor explains: "2960 1.5.1.7 has corrected many security issues. And 2960 is EoS with limited support, only major issues would be reviewed(e.g. unauthenticated vuln.)". This vulnerability only affects products that are no longer supported by the maintainer.

### 120. CVE-2026-113354｜Finsys / dockhand
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T11:17:19.843)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：0.00238 / percentile=0.14085
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T11:17:19.843 / 2026-10-22T22:18:03.123
- **官方描述（原文）**：Dockhand before 1.0.46 contains an arbitrary file read vulnerability that allows non-admin users with stacks:edit permission to read files through the path parameter of /api/system/files/content. Attackers can supply absolute paths to read /etc/shadow, /etc/passwd, git .git/config credentials, and SSH keys from the Dockhand container.

### 121. CVE-2026-113331｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:19:27.610)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:19:27.610 / 2026-10-22T23:18:29.610
- **官方描述（原文）**：Memory corruption in Controls in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to potentially execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: Low)

### 122. CVE-2026-113147｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:19:07.123)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00486 / percentile=0.40983
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:19:07.123 / 2026-10-22T23:18:27.260
- **官方描述（原文）**：Improper input validation in WebShare in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to potentially execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 123. CVE-2026-113146｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:19:06.993)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00385 / percentile=0.31338
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:19:06.993 / 2026-10-22T23:18:27.113
- **官方描述（原文）**：Memory corruption in PerformanceAPIs in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to potentially execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 124. CVE-2026-113141｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:19:06.430)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00385 / percentile=0.31338
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:19:06.430 / 2026-10-22T23:18:26.953
- **官方描述（原文）**：Use after free in Transactions Platform in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 125. CVE-2026-113118｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:19:03.890)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.0035 / percentile=0.27489
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:19:03.890 / 2026-10-22T23:18:26.473
- **官方描述（原文）**：Memory corruption in Extensions in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 126. CVE-2026-113022｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:18:53.043)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.0042 / percentile=0.35224
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:18:53.043 / 2026-10-23T13:17:08.260
- **官方描述（原文）**：Memory corruption in PDFium in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to potentially execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 127. CVE-2026-113009｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:18:51.440)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00385 / percentile=0.31338
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:18:51.440 / 2026-10-22T23:18:24.557
- **官方描述（原文）**：Use after free in WindowControlsOverlay in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 128. CVE-2026-112995｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:18:49.097)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00385 / percentile=0.31338
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:18:49.097 / 2026-10-23T13:17:08.110
- **官方描述（原文）**：Use after free in Animation in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 129. CVE-2026-112940｜tox-dev / filelock
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T15:17:16.827)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：0.00116 / percentile=0.01549
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T15:17:16.827 / 2026-10-22T22:18:02.827
- **官方描述（原文）**：filelock is a platform-independent file lock for Python. From 3.20.4 until 4.2.1, ReadWriteLock let SQLite reopen the database and side files by name; on POSIX systems an attacker with rename access in a non-sticky parent can swap those names to cause overwrite or unlink operations, while a writable adjacent hot journal is additionally required for attacker-chosen content overwrites. This issue is fixed in version 4.2.1.

### 130. CVE-2026-111765｜a2aproject / a2a-java
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T16:17:00.830)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00675 / percentile=0.51616
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T16:17:00.830 / 2026-10-22T22:18:01.380
- **官方描述（原文）**：A2A Java SDK is the official Java SDK for the Agent2Agent (A2A) Protocol. Starting in version 1.3.0.Final and prior to version 1.3.2.Final, the AndroidA2AHttpClient synchronous POST path overrides the disabled-redirect setting in AndroidA2AHttpClient.createConnection() with the PostBuilder default followRedirects value of true, leaving a residual of the earlier credential-redirect fix. JSONRPCTransport and RestTransport add interceptor-produced authentication headers and call synchronous post() without disabling redirects. AuthInterceptor permits X-API-Key, API-Key, X-Auth-Token, and X-Authentication headers; Android's repackaged OkHttp strips Authorization on cross-authority redirects but retains these nonstandard headers, disclosing a complete configured API key or token to another authority. The additional exposure applies when redirect or front-door behavior is compromised separately from the credential-handling component, or those components operate in different trust domains; a completely malicious initial origin already receives the credential on the first request. Autonomous clients require no human action, while user-invoked workflows can require interaction. Explicit followRedirects(false) prevents the redirected request. The demonstrated impact is credential disclosure, not subsequent credential use, integrity or availability impact, code execution, or host compromise. This issue is fixed in version 1.3.2.Final.

### 131. CVE-2026-111756｜follow-redirects / follow-redirects
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T18:17:18.070)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：0.00365 / percentile=0.2922
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T18:17:18.070 / 2026-10-23T02:16:54.423
- **官方描述（原文）**：follow-redirects is a Node.js HTTP and HTTPS client wrapper that automatically follows redirects. From version 1.16.0 to before version 1.16.1, follow-redirects removes sensitive credential headers (Authorization, Proxy-Authorization, Cookie, and any caller-declared sensitiveHeaders) before following a redirect that crosses to a different host or downgrades to a less secure protocol. The removal routine iterates the caller's headers container with for...in and matches header names against a filter. This assumes the headers container is a plain object keyed by header names. Node's underlying http.request, which follow-redirects is a drop-in replacement for, also accepts headers as an alternating array of names and values. For an array, for...in yields the numeric indices "0", "1", "2" and so on, which never match a header-name filter, so nothing is removed. An application that sends array-form headers and follows an attacker-controlled cross-origin redirect therefore forwards its Authorization, Cookie, and Proxy-Authorization headers verbatim to the attacker-controlled destination, with no error or warning. The sensitiveHeaders option added to fix CVE-2026-40895 / GHSA-r4q5-vmmm-2653 is equally ineffective, because it relies on the same helper. This is an unauthenticated confidentiality vulnerability: any remote server the victim application contacts can harvest the victim's credential headers by responding with a cross-origin redirect. This issue has been patched in version 1.16.1.

### 132. CVE-2016-20104｜EyeLock / nano NXT
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:14.193)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:14.193 / 2026-10-23T16:16:50.360
- **官方描述（原文）**：EyeLock nano NXT 3.05.1193, 3.04.1108, 3.03.944, and 3.01.646 contain a path traversal vulnerability that allows unauthenticated attackers to read arbitrary files via the 'path' parameter. Attackers can send GET requests to /scripts/logdownload.php with traversal sequences like ../../etc/passwd, which readfile() returns unvalidated, disclosing local system files. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-19.

### 133. CVE-2016-20100｜Ian Howatson / Memphis Documents Library
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:13.520)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:13.520 / 2026-10-23T03:16:30.053
- **官方描述（原文）**：Memphis Documents Library plugin for WordPress before 3.1.6 contains a path traversal vulnerability that allows unauthenticated attackers to read arbitrary files via the mdocs-img-preview parameter. Attackers can send GET requests with traversal sequences to mdocs_img_preview() in mdocs-downloads.php to download wp-config.php containing database credentials. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-22.

### 134. CVE-2015-20128｜FooSun / DotNetCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:13.357)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:13.357 / 2026-10-23T16:16:50.197
- **官方描述（原文）**：FooSun DotNetCMS 1.0 and 2.0 contains an SQL injection vulnerability that allows unauthenticated attackers to manipulate MSSQL queries through the CityId parameter. Attackers can send GET requests to /user/City_ajax.aspx with UNION SELECT payloads in CityId, concatenated unsanitized into the sys_City query, to extract database information. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 135. CVE-2015-20124｜Aspose / Aspose Importer & Exporter
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:13.060)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:13.060 / 2026-10-22T17:40:46.877
- **官方描述（原文）**：Aspose Importer & Exporter plugin for WordPress before 3.0 contains a path traversal vulnerability that allows unauthenticated attackers to download arbitrary files via the unsanitized 'file' parameter. Attackers can send GET requests to aspose_import_export_download.php with traversal sequences like ../../../wp-config.php to read database credentials. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-20.

### 136. CVE-2014-125134｜ChurcHope / ChurcHope
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:12.720)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:12.720 / 2026-10-23T03:16:29.903
- **官方描述（原文）**：ChurcHope theme for WordPress before 2.2 contains a path traversal vulnerability that allows unauthenticated attackers to download arbitrary files through the 'file' parameter of /wp-content/themes/churchope/lib/downloadlink.php. Attackers can supply directory traversal sequences to read sensitive files like wp-config.php or /etc/passwd, exposing database credentials. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-18.

### 137. CVE-2014-125133｜imithemes / NativeChurch
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:12.560)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:12.560 / 2026-10-23T16:16:50.017
- **官方描述（原文）**：NativeChurch theme for WordPress before 1.6.2 contains a path traversal vulnerability that allows unauthenticated attackers to download arbitrary files through the file parameter of download.php. Attackers can send GET requests with directory traversal sequences in the file parameter to retrieve sensitive files like wp-config.php. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-19.

### 138. CVE-2026-9869｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:23.143)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00791 / percentile=0.5584
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:23.143 / 2026-10-23T23:19:51.180
- **官方描述（原文）**：A stack-based buffer overflow vulnerability exists in the boa formTR069Config functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 139. CVE-2026-9827｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:23.020)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00976 / percentile=0.61797
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:23.020 / 2026-10-23T23:19:51.073
- **官方描述（原文）**：A arbitrary file write vulnerability exists in the boa formUploadFile functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 140. CVE-2026-9817｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:22.900)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00791 / percentile=0.55842
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:22.900 / 2026-10-23T23:19:50.960
- **官方描述（原文）**：A stack-based buffer overflow vulnerability exists in the boa formUploadFile functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 141. CVE-2026-9814｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:22.773)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.013 / percentile=0.70227
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:22.773 / 2026-10-23T23:19:50.850
- **官方描述（原文）**：An OS command injection vulnerability exists in the boa formWizard newPass functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 142. CVE-2026-96639｜python-pillow / Pillow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T21:20:32.217)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00565 / percentile=0.46227
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T21:20:32.217 / 2026-10-22T16:46:48.920
- **官方描述（原文）**：Pillow is a Python imaging library. From 11.0.0 until 13.0.0, multi-frame loaders can retain an ImagingCore allocation created for a narrow frame mode while a later frame of the same dimensions changes the logical mode and decoder tiles to wider RGB or CMYK data. ImageFile.load_prepare() reuses the stale native storage because _im is non-null without verifying that its mode and size still match. Crafted PSD, MPO, DCX, or MIC frame transitions can then write wider pixels into the narrow allocation, causing native out-of-bounds writes and crashes. The MPO path can also cause a native over-read and, in demonstrated runtime-specific profiles, command execution. This issue is fixed in version 13.0.0.

### 143. CVE-2026-9660｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:22.613)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00791 / percentile=0.55841
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:22.613 / 2026-10-23T23:19:50.730
- **官方描述（原文）**：Multiple exploitable stack-based buffer overflow vulnerabilities exist in the boa formFilter functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger these vulnerabilities. This vulnerability deals with the vpnPassword parameter.

### 144. CVE-2026-9659｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:22.410)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00791 / percentile=0.55841
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:22.410 / 2026-10-22T15:31:24.813
- **官方描述（原文）**：Multiple exploitable stack-based buffer overflow vulnerabilities exist in the boa formFilter functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger these vulnerabilities. This vulnerability deals with the vpnUser parameter.

### 145. CVE-2026-96355｜Drupal / Webform
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T02:17:05.433)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00427 / percentile=0.35905
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T02:17:05.433 / 2026-10-23T04:18:23.770
- **官方描述（原文）**：Improper Neutralization of Special Elements Used in a Template Engine vulnerability in Drupal Webform allows Code Injection. This issue affects Webform versions: from 0.0.0 to 6.2.12, from 6.3.0 to 6.3.1.

### 146. CVE-2026-92559｜IBM / App Connect Enterprise
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:21:07.190)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00633 / percentile=0.49723
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:21:07.190 / 2026-10-23T12:18:18.907
- **官方描述（原文）**：IBM App Connect Enterprise 13.0.1.0 through 13.0.8.2 could allow a remote attacker to obtain sensitive information due to binding to an unrestricted IP address.

### 147. CVE-2026-91665｜Oracle Corporation / Oracle Essbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:21:06.960)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00412 / percentile=0.34334
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:21:06.960 / 2026-10-22T23:20:33.240
- **官方描述（原文）**：Vulnerability in Oracle Essbase (component: Security). The supported version that is affected is 21.8.3.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via TCP to compromise Oracle Essbase. Successful attacks of this vulnerability can result in takeover of Oracle Essbase. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 148. CVE-2026-91663｜Oracle Corporation / Oracle Essbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:21:06.723)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00286 / percentile=0.20023
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:21:06.723 / 2026-10-23T17:18:32.390
- **官方描述（原文）**：Vulnerability in Oracle Essbase (component: Security). The supported version that is affected is 21.8.3.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via T3, IIOP to compromise Oracle Essbase. While the vulnerability is in Oracle Essbase, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Essbase. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 149. CVE-2026-91658｜Oracle Corporation / Oracle Essbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:21:06.150)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00286 / percentile=0.20024
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:21:06.150 / 2026-10-23T17:19:01.540
- **官方描述（原文）**：Vulnerability in Oracle Essbase (component: Security). The supported version that is affected is 21.8.3.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Essbase. While the vulnerability is in Oracle Essbase, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Essbase. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 150. CVE-2026-91656｜Oracle Corporation / Oracle Essbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:21:05.920)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00208 / percentile=0.10408
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:21:05.920 / 2026-10-23T14:35:07.820
- **官方描述（原文）**：Vulnerability in Oracle Essbase (component: Federated Partitions). The supported version that is affected is 21.8.3.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Essbase. While the vulnerability is in Oracle Essbase, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all Oracle Essbase accessible data as well as unauthorized update, insert or delete access to some of Oracle Essbase accessible data and unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Essbase. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:L/A:L).

### 151. CVE-2026-91655｜Oracle Corporation / Oracle Essbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:21:05.803)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00208 / percentile=0.10407
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:21:05.803 / 2026-10-23T14:56:48.697
- **官方描述（原文）**：Vulnerability in Oracle Essbase (component: Security). The supported version that is affected is 21.8.3.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Essbase. While the vulnerability is in Oracle Essbase, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all Oracle Essbase accessible data as well as unauthorized update, insert or delete access to some of Oracle Essbase accessible data and unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Essbase. CVSS 3.1 Base Score 9.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:L/A:L).

### 152. CVE-2026-91644｜Oracle Corporation / Oracle Essbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:21:04.543)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.00218 / percentile=0.11622
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:21:04.543 / 2026-10-23T14:58:05.110
- **官方描述（原文）**：Vulnerability in Oracle Essbase (component: Security). The supported version that is affected is 21.8.3.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Essbase. While the vulnerability is in Oracle Essbase, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all Oracle Essbase accessible data as well as unauthorized update, insert or delete access to some of Oracle Essbase accessible data. CVSS 3.1 Base Score 9.3 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N).

### 153. CVE-2026-91638｜Oracle Corporation / Oracle Essbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:21:03.817)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:21:03.817 / 2026-10-23T17:19:18.217
- **官方描述（原文）**：Vulnerability in Oracle Essbase (component: Security). The supported version that is affected is 21.8.3.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Essbase. While the vulnerability is in Oracle Essbase, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Essbase. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 154. CVE-2026-91637｜Oracle Corporation / Oracle Essbase
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:21:03.693)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:21:03.693 / 2026-10-23T14:56:37.227
- **官方描述（原文）**：Vulnerability in Oracle Essbase (component: Security). The supported version that is affected is 21.8.3.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Essbase. While the vulnerability is in Oracle Essbase, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Essbase. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 155. CVE-2026-91403｜Oracle Corporation / Oracle Java SE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T22:16:50.243)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00392 / percentile=0.32169
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T22:16:50.243 / 2026-10-23T12:18:17.197
- **官方描述（原文）**：Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition product of Oracle Java SE (component: JSSE). Supported versions that are affected are Oracle Java SE: 8u511, 8u511-perf, 11.0.33, 17.0.21, 21.0.13, 25.0.5, 27.0.1; Oracle GraalVM for JDK: 17.0.21 and 21.0.13; Oracle GraalVM Enterprise Edition: 21.3.20. Easily exploitable vulnerability allows unauthenticated attacker with network access via multiple protocols to compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition accessible data as well as unauthorized access to critical data or complete access to all Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition accessible data. Note: This vulnerability can be exploited by using APIs in the specified Component, e.g., through a web service which supplies data to the APIs. This vulnerability also applies to Java deployments, typically in clients running sandboxed Java Web Start applications or sandboxed Java applets, that load and run untrusted code (e.g., code that comes from the internet) and rely on the Java sandbox for security. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 156. CVE-2026-91305｜Oracle Corporation / JD Edwards EnterpriseOne Tools
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:20:32.243)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:20:32.243 / 2026-10-22T23:20:33.117
- **官方描述（原文）**：Vulnerability in the JD Edwards EnterpriseOne Tools product of Oracle JD Edwards (component: Installation Security). Supported versions that are affected are 9.2.0.0-9.2.26.5. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise JD Edwards EnterpriseOne Tools. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all JD Edwards EnterpriseOne Tools accessible data as well as unauthorized access to critical data or complete access to all JD Edwards EnterpriseOne Tools accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 157. CVE-2026-91299｜Oracle Corporation / JD Edwards EnterpriseOne Orchestrator
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:20:31.557)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:20:31.557 / 2026-10-23T12:18:17.050
- **官方描述（原文）**：Vulnerability in the JD Edwards EnterpriseOne Orchestrator product of Oracle JD Edwards (component: E1 IOT Orchestrator Security). Supported versions that are affected are 9.2.0.0-9.2.26.5. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise JD Edwards EnterpriseOne Orchestrator. While the vulnerability is in JD Edwards EnterpriseOne Orchestrator, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of JD Edwards EnterpriseOne Orchestrator. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 158. CVE-2026-91265｜Oracle Corporation / JD Edwards EnterpriseOne Tools
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:20:27.557)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:20:27.557 / 2026-10-22T23:20:32.367
- **官方描述（原文）**：Vulnerability in the JD Edwards EnterpriseOne Tools product of Oracle JD Edwards (component: Enterprise Infrastructure SEC). Supported versions that are affected are 9.2.0.0-9.2.26.5. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise JD Edwards EnterpriseOne Tools. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all JD Edwards EnterpriseOne Tools accessible data as well as unauthorized access to critical data or complete access to all JD Edwards EnterpriseOne Tools accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 159. CVE-2026-89035｜MikroTik / RouterOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T18:17:30.277)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00274 / percentile=0.18769
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T18:17:30.277 / 2026-10-22T17:39:56.760
- **官方描述（原文）**：MikroTik RouterOS through 7.24.5 contains a session token replay vulnerability in the WebFig interface that allows attackers to bypass authentication by replaying captured session tokens across new ECDH sessions. The makeSessionKey function in libucrypto.so generates tokens using fixed salts without incorporating channel-specific or session-specific input, and the user service validates tokens against the login store without verifying channel context, enabling stolen tokens to grant persistent administrative access until the token store is explicitly cleared. This vulnerability extends the impact of CVE-2025-61481, which identified the underlying transport-layer exposure without a corresponding fix.

### 160. CVE-2026-87095｜Acronis / Acronis Cyber Infrastructure
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T11:17:09.463)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.0 9.1 (CRITICAL)
- **EPSS**：0.00242 / percentile=0.14499
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T11:17:09.463 / 2026-10-22T17:21:57.293
- **官方描述（原文）**：Sensitive information disclosure and manipulation due to improper authorization checks. The following products are affected: Acronis Cyber Infrastructure (ACI) before build 6.0.1-112, Acronis Cyber Infrastructure (ACI) before build 6.1.1-64, Acronis Cyber Infrastructure (ACI) before build 6.2.1-71.

### 161. CVE-2026-76531｜Splunk / Splunk SOAR
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T23:17:30.117)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00378 / percentile=0.30574
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T23:17:30.117 / 2026-10-22T16:57:10.180
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, Cisco has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76531 are related to files or directories accessible to external parties and are grouped under the Common Weakness Enumeration (CWE) CWE-552.

### 162. CVE-2026-76475｜Cisco / Cisco Emergency Responder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T17:19:07.253)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.0025 / percentile=0.15482
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T17:19:07.253 / 2026-10-22T14:17:46.217
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency Responder, Cisco Prime Collaboration Deployment, Cisco Unified Communications Manager (Unified CM), Cisco Unified Communications Manager IM &amp; Presence Service (Unified CM IM&amp;P), Cisco Unified Communications Manager Session Management Edition (Unified CM SME), and Cisco Unity Connection have conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76475 are related to issues concerning improper neutralization of input during web page generation that are grouped under the Common Weakness Enumeration (CWE) Base CWE-79.

### 163. CVE-2026-76474｜Cisco / Cisco Emergency Responder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T17:19:07.113)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00357 / percentile=0.2825
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T17:19:07.113 / 2026-10-22T23:19:07.677
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency Responder, Cisco Prime Collaboration Deployment, Cisco Unified Communications Manager (Unified CM), Cisco Unified Communications Manager IM &amp; Presence Service (Unified CM IM&amp;P), Cisco Unified Communications Manager Session Management Edition (Unified CM SME), and Cisco Unity Connection have conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76474 are related to issues concerning improper authentication that are grouped under the Common Weakness Enumeration (CWE) Class CWE-287.

### 164. CVE-2026-76473｜Cisco / Cisco Emergency Responder
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T17:19:06.973)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00356 / percentile=0.28166
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T17:19:06.973 / 2026-10-22T23:19:07.543
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, engineering teams for Cisco Emergency Responder, Cisco Prime Collaboration Deployment, Cisco Unified Communications Manager (Unified CM), Cisco Unified Communications Manager IM &amp; Presence Service (Unified CM IM&amp;P), Cisco Unified Communications Manager Session Management Edition (Unified CM SME), and Cisco Unity Connection have conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76473 are related to issues concerning improper control of a resource through its lifetime that are grouped under the Common Weakness Enumeration (CWE) Class CWE-74. &nbsp;

### 165. CVE-2026-76466｜Cisco / Cisco TelePresence Video Communication Server (VCS) Expressway
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T17:19:06.813)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00381 / percentile=0.30934
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T17:19:06.813 / 2026-10-22T23:19:07.397
- **官方描述（原文）**：A vulnerability in the database service feature of Cisco Expressway Series could allow an unauthenticated, remote attacker with network access to a Cisco Expressway device to execute arbitrary operating system commands as&nbsp;root. This vulnerability is due to the use of persistent cookies. Additionally, there is insufficient validation of client certificates when the TLS Verify Mode is set to Enabled for clustering, which means that client certificates are not validated. An attacker with possession of the cookies could exploit this vulnerability by connecting to the database service and invoking specific remote procedure call (RPC) commands. A successful exploit could allow the attacker to execute arbitrary commands as root on the underlying operating system of an affected device. Note: Cisco Expressway Series refers to Cisco Expressway Core (Expressway-C) devices and Cisco Expressway Edge (Expressway-E) devices.

### 166. CVE-2026-76302｜Splunk / Splunk Enterprise
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T23:17:28.273)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00378 / percentile=0.30574
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T23:17:28.273 / 2026-10-22T16:57:10.180
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, Cisco has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76302 are related to improper neutralization and are grouped under the Common Weakness Enumeration (CWE) CWE-707.

### 167. CVE-2026-76299｜Splunk / Splunk Enterprise
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T23:17:27.940)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00253 / percentile=0.15856
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T23:17:27.940 / 2026-10-22T16:57:10.180
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, Cisco has conducted a comprehensive internal security review. This review resulted in a software hardening release that addresses multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-76299 are related to improper access control and are grouped under the Common Weakness Enumeration (CWE) CWE-284.

### 168. CVE-2026-71195｜OpenStack / Manila
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T06:16:49.393)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T06:16:49.393 / 2026-10-22T17:36:46.950
- **官方描述（原文）**：In OpenStack Manila before 23.0.1, multiple Manila API operations on public shares do not verify that the caller owns the share. The API controllers authorize operations against the caller's own project context, then load a foreign public share without re-authorizing against the share's actual owner. This affects the following operations: allow_access: grant data-plane read/write access to another tenant's share; deny_access: revoke the owner's existing access rules; update_access: escalate access level (e.g., ro to rw); create_share_backup: exfiltrate share data via a backup created under the attacker's project; soft_delete: move a foreign share to the recycle bin; restore: interfere with the owner's deletion workflow; export location metadata: create, update, and delete metadata on foreign export locations; access rule listing: disclose IPs, usernames, and CephFS keys. Any authenticated project member can exploit these operations on any public share. The share UUID is visible since the share is public.

### 169. CVE-2026-42026｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:19.730)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00791 / percentile=0.55841
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:19.730 / 2026-10-23T23:17:44.147
- **官方描述（原文）**：Multiple exploitable stack-based buffer overflow vulnerabilities exist in the boa formIpv6Setup dhcp_dns functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger these vulnerabilities. This vulnerability concerns the dhcp_dns2 parameter.

### 170. CVE-2026-42025｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:19.610)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00791 / percentile=0.55841
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:19.610 / 2026-10-23T23:17:44.033
- **官方描述（原文）**：Multiple exploitable stack-based buffer overflow vulnerabilities exist in the boa formIpv6Setup dhcp_dns functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger these vulnerabilities. This vulnerability concerns the dhcp_dns1 parameter.

### 171. CVE-2026-42024｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:19.490)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00791 / percentile=0.5584
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:19.490 / 2026-10-23T23:17:43.937
- **官方描述（原文）**：Multiple stack-based buffer overflow vulnerabilities exist in the boa formIpv6Setup static network configuration functionality of Totolink X2000R TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327. A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger these vulnerabilities. This vulnerability concerns the static_gw parameter.

### 172. CVE-2026-42023｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:19.373)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00791 / percentile=0.5584
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:19.373 / 2026-10-23T23:17:43.830
- **官方描述（原文）**：Multiple stack-based buffer overflow vulnerabilities exist in the boa formIpv6Setup static network configuration functionality of Totolink X2000R TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327. A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger these vulnerabilities. This vulnerability concerns the static_ipv6 parameter.

### 173. CVE-2026-42022｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:19.257)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00737 / percentile=0.54008
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:19.257 / 2026-10-23T23:17:43.730
- **官方描述（原文）**：Multiple stack-based buffer overflow vulnerabilities exist in the boa formIpv6Setup static network configuration functionality of Totolink X2000R TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327. A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger these vulnerabilities. This vulnerability concerns the static_dns2 parameter.

### 174. CVE-2026-42021｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:19.140)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00737 / percentile=0.54009
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:19.140 / 2026-10-23T23:17:43.620
- **官方描述（原文）**：Multiple stack-based buffer overflow vulnerabilities exist in the boa formIpv6Setup static network configuration functionality of Totolink X2000R TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327. A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger these vulnerabilities. This vulnerability concerns the static_dns1 parameter.

### 175. CVE-2026-42020｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:19.020)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00737 / percentile=0.54009
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:19.020 / 2026-10-22T15:31:24.813
- **官方描述（原文）**：Multiple stack-based buffer overflow vulnerabilities exist in the boa formIpv6Setup pppoe functionality of Totolink X2000R TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327. A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger these vulnerabilities. This vulnerability concerns the pppoe_dns2 parameter.

### 176. CVE-2026-42019｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:18.903)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00737 / percentile=0.54008
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:18.903 / 2026-10-22T15:31:24.813
- **官方描述（原文）**：Multiple stack-based buffer overflow vulnerabilities exist in the boa formIpv6Setup pppoe functionality of Totolink X2000R TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327. A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger these vulnerabilities. This vulnerability concerns the pppoe_dns1 parameter.

### 177. CVE-2026-41223｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:18.783)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00737 / percentile=0.54009
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:18.783 / 2026-10-22T15:31:24.813
- **官方描述（原文）**：A stack-based buffer overflow vulnerability exists in the boa formMapDelDevice macstr functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 178. CVE-2026-41222｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:18.653)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00737 / percentile=0.54008
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:18.653 / 2026-10-22T15:31:24.813
- **官方描述（原文）**：A stack-based buffer overflow vulnerability exists in the boa formParentControl url functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 179. CVE-2026-40627｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:18.517)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.01043 / percentile=0.63807
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:18.517 / 2026-10-22T15:31:24.813
- **官方描述（原文）**：An os command injection vulnerability exists in the boa formWsc targetAPSsid functionality of Totolink X2000R TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327. A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 180. CVE-2026-40615｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:18.393)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00737 / percentile=0.54009
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:18.393 / 2026-10-22T15:31:24.813
- **官方描述（原文）**：A stack-based buffer overflow vulnerability exists in the boa formParentControl deviceName functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 181. CVE-2026-35499｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:18.277)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.01043 / percentile=0.63807
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:18.277 / 2026-10-23T23:17:43.507
- **官方描述（原文）**：An os command injection vulnerability exists in the boa formWsc peerRptPin functionality of Totolink X2000R TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327. A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 182. CVE-2026-33568｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:18.157)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.01043 / percentile=0.63807
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:18.157 / 2026-10-22T15:31:24.813
- **官方描述（原文）**：A OS command injection vulnerability exists in the boa formMapDelDevice macstr functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 183. CVE-2026-28763｜totolink / Totolink
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T21:17:18.037)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00737 / percentile=0.5401
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T21:17:18.037 / 2026-10-22T15:31:24.813
- **官方描述（原文）**：A stack-based buffer overflow vulnerability exists in the boa formMapDelDevice hostname functionality of X2000R (version(s): TOTOLINK-X2000R-Gh-V1.0.0-B20250421.1327). A specially crafted HTTP request can lead to arbitrary code execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.

### 184. CVE-2026-20043｜Cisco / Cisco Cyber Vision
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T17:18:27.087)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T17:18:27.087 / 2026-10-22T23:18:31.190
- **官方描述（原文）**：As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco owned Open Source Snort 3 Software engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. The vulnerabilities tracked by CVE-2026-20043 are related to issues concerning out-of-bounds writes that are grouped under the Common Weakness Enumeration (CWE) Base CWE-787.

### 185. CVE-2026-114575｜TOTOLINK / A950RG
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-22T01:16:58.533)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.0221 / percentile=0.82468
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-22T01:16:58.533 / 2026-10-22T15:15:23.833
- **官方描述（原文）**：A flaw has been found in TOTOLINK A950RG 4.1.2cu.5268_B20221104. Affected by this issue is the function UploadCustomModule of the file lib/cste_modules/product.so. Executing a manipulation of the argument FileMd5 can lead to command injection. The attack can be launched remotely. The exploit has been published and may be used.

### 186. CVE-2026-114509｜laravel / framework
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T22:16:49.710)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00403 / percentile=0.33448
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T22:16:49.710 / 2026-10-22T17:29:28.470
- **官方描述（原文）**：Laravel is a web application framework. Prior to 12.68.0 and 13.29.0, TokenGuard configured as a standard token-based API guard does not reject a crafted non-string credential. Under affected MySQL or MariaDB configurations, the authentication lookup can match an unintended existing user, allowing an unauthenticated attacker to bypass authentication and take over an account on routes protected by TokenGuard. This issue is fixed in versions 12.68.0 and 13.29.0.

### 187. CVE-2026-114493｜LocalAI / LocalAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T18:17:28.120)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.0038 / percentile=0.3083
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T18:17:28.120 / 2026-10-22T17:39:56.760
- **官方描述（原文）**：LocalAI v4.6.0 through v4.11.0 contains a server-side request forgery vulnerability in core/gallery/gallery.go that validates only the initial gallery config URL. Attackers can submit a config URL through POST /models/apply that redirects to internal or cloud metadata addresses, receiving those internal responses as gallery content.

### 188. CVE-2026-114403｜PHPOffice / PHPPresentation
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T13:18:31.753)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00477 / percentile=0.40272
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T13:18:31.753 / 2026-10-22T17:39:56.760
- **官方描述（原文）**：PHPOffice PHPPresentation through 1.2.0 contains an insecure deserialization vulnerability that allows attackers to instantiate arbitrary PHP objects by supplying a crafted presentation file. Attackers can upload a ZIP containing PhpPresentation.xml that IOFactory::load passes to unserialize(), enabling gadget-chain code execution, file writes, or denial of service.

### 189. CVE-2026-114383｜TOTOLINK / EX200
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T22:16:49.077)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00653 / percentile=0.50698
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T22:16:49.077 / 2026-10-22T15:15:23.833
- **官方描述（原文）**：A weakness has been identified in TOTOLINK EX200 5.2.3c.7200. This impacts the function setWiFiAclAddConfig of the file /cgi-bin/cstecgi.cgi of the component wireless.so. This manipulation of the argument macAddress causes stack-based buffer overflow. The attack can be initiated remotely. The exploit has been made available to the public and could be used for attacks.

### 190. CVE-2026-114382｜TOTOLINK / EX200
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T22:16:48.910)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00667 / percentile=0.51299
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T22:16:48.910 / 2026-10-22T15:15:23.833
- **官方描述（原文）**：A security flaw has been discovered in TOTOLINK EX200 5.2.3c.7200. This affects the function setStaticDhcpConfig of the file /cgi-bin/cstecgi.cgi of the component lan.so. The manipulation of the argument Comment results in stack-based buffer overflow. It is possible to launch the attack remotely. The exploit has been released to the public and may be used for attacks.

### 191. CVE-2026-114139｜getsentry / sentry-javascript
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T21:17:56.353)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00407 / percentile=0.33843
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T21:17:56.353 / 2026-10-22T17:29:28.470
- **官方描述（原文）**：Sentry-Javascript is an official Sentry SDKs for JavaScript. From 9.36.0 until 9.47.2, 10.75.2, and 11.0.0-rc.1, the webpack integration for @sentry/nextjs skips application middleware for every request path under a configured tunnelRoute, while the tunnel rewrite serves only the exact tunnel path with valid o and p query parameters. When an application route directly collides with the tunnel path or a root dynamic segment resolves under it, an unauthenticated request can reach that route without middleware authorization. Exploitation requires tunnelRoute, a webpack build, a colliding route, and middleware being the only authorization control. This issue is fixed in versions 9.47.2, 10.75.2, and 11.0.0-rc.1.

### 192. CVE-2026-114119｜Best Practice Software / Bp Premier
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T01:17:38.353)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00428 / percentile=0.36037
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T01:17:38.353 / 2026-10-22T17:40:46.877
- **官方描述（原文）**：Best Practice Software Bp Premier before 1.14.1.1128 uses a hardcoded Microsoft SQL Server administrative password that is shared across all installations and cannot be changed without breaking the application. Attackers with network access to the database instance can authenticate as sysadmin, bypass application authentication, and execute operating system commands as SYSTEM.

### 193. CVE-2026-114108｜HKUDS / Vibe-Trading
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T01:17:36.820)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00357 / percentile=0.2821
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T01:17:36.820 / 2026-10-22T17:40:46.877
- **官方描述（原文）**：HKUDS Vibe-Trading from 0.1.0 before 0.1.7 contains a missing authentication vulnerability that allows unauthenticated attackers to access the FastAPI surface because require_auth() returns early when API_AUTH_KEY is unset. Attackers can post messages to /sessions/{id}/messages to trigger root shell commands via BashTool, upload .py or .sh files via /upload, read session histories, and obtain partial API keys.

### 194. CVE-2026-114053｜vllm-project / vllm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T01:17:28.083)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00462 / percentile=0.39077
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T01:17:28.083 / 2026-10-22T15:44:59.783
- **官方描述（原文）**：vLLM from 0.7.3 before 0.31.0 forwards the request-supplied mm_processor_kwargs.code_revision to Transformers AutoProcessor.from_pretrained, letting clients select which revision of a model's dynamic processor code is imported when trust_remote_code is enabled. An attacker controlling a revision in the served model repository can send a multimodal request to the unauthenticated /tokenize endpoint to execute arbitrary Python in the vLLM API process.

### 195. CVE-2026-113788｜uselagoon / lagoon
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-21T16:17:26.440)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.0031 / percentile=0.22702
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-21T16:17:26.440 / 2026-10-23T16:16:51.237
- **官方描述（原文）**：Lagoon is an application delivery platform for Kubernetes. Versions prior to 2.33.1 have a vulnerability in the `ssh` service in Lagoon core that would allow an attacker to execute arbitrary code which could lead to, among other things, elevated administrative permissions. It is mitigated by the fact that an attacker must have a Lagoon user account. Exploitation may be detected by checking the container logs of the `ssh` service for: `too many arguments`. The vulnerability was fixed in Lagoon v2.33.2, which is included in the `lagoon/lagoon-core` helm chart v1.62.2. As a workaround, the `ssh` service in Lagoon core can be disabled. The `ssh-portal` service and components are not effected and can continue to be used.

### 196. CVE-2026-113682｜networknt / light-4j
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T16:17:13.210)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：0.00477 / percentile=0.40224
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T16:17:13.210 / 2026-10-23T14:17:32.900
- **官方描述（原文）**：Networknt light-4j from 2.1.5 before 2.4.0 contains an authentication bypass vulnerability in BasicAuthHandler that allows unauthenticated attackers to log in as LDAP/AD-delegated users. Attackers can send a Basic Authorization header with a known username and empty password, triggering an unauthenticated LDAP bind that is accepted as successful authentication.

### 197. CVE-2026-113342｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:19:28.877)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:19:28.877 / 2026-10-22T23:18:29.913
- **官方描述（原文）**：Memory corruption in Network in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 198. CVE-2026-113336｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:19:28.177)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:19:28.177 / 2026-10-22T23:18:29.763
- **官方描述（原文）**：Memory corruption in Compositing in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 199. CVE-2026-113328｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:19:27.257)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:19:27.257 / 2026-10-22T23:18:29.457
- **官方描述（原文）**：Improper input validation in Privacy in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 200. CVE-2026-113300｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T22:19:24.157)
- **Risk**：WATCH / score 20；reasons：CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：0.00494 / percentile=0.41546
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T22:19:24.157 / 2026-10-22T23:18:29.307
- **官方描述（原文）**：Out of bounds write in Forms in Google Chrome prior to 156.0.8078.47 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Low)


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-114625｜Arista / VeloCloud Orchestrator
- **Title**：Arista VeloCloud Orchestrator SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00555 / percentile=0.45586
- **CISA KEV**：listed=true / date_added=2026-10-23 / due_date=2026-10-26
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Arista VeloCloud Orchestrator on-prem contains a SQL injection vulnerability that may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-110447｜Collabora / Collabora Online – Built-in CODE Server
- **Title**：Collabora Online – Built-in CODE Server OS Command Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.01225 / percentile=0.68615
- **CISA KEV**：listed=true / date_added=2026-10-23 / due_date=2026-10-26
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Collabora Collabora Online – Built-in CODE Server when used within the NextCloud platform contains an OS command injection vulnerability that allows for remote code execution when the CODE server isn't running.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2021-48014 | P3 / 38 | FanRuan / FineReport | v4.0 9.3 (CRITICAL) | 0.01669 / percentile=0.76617 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-109618 | WATCH / 33 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.1162 / percentile=0.96047 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-115506 | WATCH / 30 | libexpat / libexpat | v4.0 8.7 (HIGH) | 0.0035 / percentile=0.27483 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-114087 | WATCH / 30 | triggerdotdev / trigger.dev | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-113678 | WATCH / 30 | froxlor / froxlor | v4.0 9.4 (CRITICAL) | 0.00446 / percentile=0.37809 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2024-58396 | WATCH / 30 | YouDataSum / CPAS Audit Management System | v4.0 8.7 (HIGH) | 0.00389 / percentile=0.31867 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2022-51025 | WATCH / 30 | Penta Security Systems / WAPPLES | v4.0 7.1 (HIGH) | 0.00373 / percentile=0.30072 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2019-25778 | WATCH / 30 | SeaCMS / SeaCMS | v4.0 8.8 (HIGH) | 0.00377 / percentile=0.3054 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2017-20289 | WATCH / 30 | Broadstreet / Ad Widget | v4.0 7.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97785 | WATCH / 28 | Microsoft / Microsoft Entra application proxy | v3.1 10.0 (CRITICAL) | 0.00598 / percentile=0.47969 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-97631 | WATCH / 28 | TianoCore / EDK2 | v4.0 9.5 (CRITICAL) | 0.00432 / percentile=0.36541 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94267 | WATCH / 28 | Unknown / Advanced Custom Fields: Extended | v3.1 9.0 (CRITICAL) | 0.00192 / percentile=0.08398 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-83938 | WATCH / 28 | Microsoft / Azure Kubernetes Configuration Service | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79876 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.3 (CRITICAL) | 0.00171 / percentile=0.06133 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79875 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.3 (CRITICAL) | 0.00164 / percentile=0.05369 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79874 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.3 (CRITICAL) | 0.00164 / percentile=0.0537 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79873 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.3 (CRITICAL) | 0.00164 / percentile=0.0537 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79872 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.4 (CRITICAL) | 0.00262 / percentile=0.17087 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79871 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.6 (CRITICAL) | 0.00182 / percentile=0.07388 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79870 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.6 (CRITICAL) | 0.00182 / percentile=0.07387 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79869 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.6 (CRITICAL) | 0.00182 / percentile=0.07387 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79868 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.6 (CRITICAL) | 0.00182 / percentile=0.07387 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79867 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.6 (CRITICAL) | 0.00182 / percentile=0.07388 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79866 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.6 (CRITICAL) | 0.00195 / percentile=0.08747 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79865 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.6 (CRITICAL) | 0.00195 / percentile=0.08747 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79864 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.6 (CRITICAL) | 0.0021 / percentile=0.10602 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79863 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.6 (CRITICAL) | 0.00195 / percentile=0.08747 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79862 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / ArubaOS (AOS) | v3.1 9.6 (CRITICAL) | 0.00195 / percentile=0.08746 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：28。
- EPSS 未確認：3；Exploitation status 未確認：18。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-24T05:13:58.138489+00:00`；Delta generated at：`2026-10-24T05:13:58.138489+00:00`。

---

## 可驗證資料來源

- **CVE-2026-114625** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114625) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114625) · [Vendor / Advisory (arista.com)](https://www.arista.com/en/support/advisories-notices/security-advisory/24838-security-advisory-0199) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-110447** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110447) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-110447) · [Vendor / Advisory (help.nextcloud.com)](https://help.nextcloud.com/t/to-collabora-built-in-user-update-asap/250516) · [Vendor / Advisory (github.com)](https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2021-48014** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-48014) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2021-48014)
- **CVE-2026-109618** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109618)
- **CVE-2026-115506** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115506) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115506)
- **CVE-2026-114087** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114087)
- **CVE-2026-113678** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113678) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113678)
- **CVE-2024-58396** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-58396) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2024-58396)
- **CVE-2022-51025** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-51025) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2022-51025)
- **CVE-2019-25778** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-25778) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2019-25778)
- **CVE-2017-20289** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2017-20289)
- **CVE-2026-97785** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97785) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97785)
- **CVE-2026-97631** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97631) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97631)
- **CVE-2026-94267** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94267) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-94267)
- **CVE-2026-83938** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-83938)
- **CVE-2026-79876** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79876) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79876)
- **CVE-2026-79875** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79875) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79875)
- **CVE-2026-79874** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79874) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79874)
- **CVE-2026-79873** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79873) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79873)
- **CVE-2026-79872** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79872) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79872)
- **CVE-2026-79871** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79871) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79871)
- **CVE-2026-79870** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79870) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79870)
- **CVE-2026-79869** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79869) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79869)
- **CVE-2026-79868** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79868) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79868)
- **CVE-2026-79867** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79867) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79867)
- **CVE-2026-79866** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79866) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79866)
- **CVE-2026-79865** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79865) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79865)
- **CVE-2026-79864** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79864) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79864)
- **CVE-2026-79863** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79863) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79863)
- **CVE-2026-79862** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79862) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79862)
- **CVE-2026-79861** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79861) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79861)
- **CVE-2026-79860** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79860) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79860)
- **CVE-2026-79859** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79859) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79859)
- **CVE-2026-79858** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79858) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79858)
- **CVE-2026-79857** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79857) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79857)
- **CVE-2026-79856** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79856) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79856)
- **CVE-2026-79855** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79855) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79855)
- **CVE-2026-79854** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79854) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79854)
- **CVE-2026-79853** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79853) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79853)
- **CVE-2026-79852** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79852) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79852)
- **CVE-2026-79851** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79851) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79851)
- **CVE-2026-79850** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79850) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79850)
- **CVE-2026-79849** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79849) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79849)
- **CVE-2026-79848** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79848) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79848)
- **CVE-2026-79847** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79847) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79847)
- **CVE-2026-79846** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79846) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79846)
- **CVE-2026-79844** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79844) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79844)
- **CVE-2026-63244** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63244) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63244)
- **CVE-2026-57116** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57116)
- **CVE-2026-55981** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55981) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-55981)
- **CVE-2026-55486** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55486)
- **CVE-2026-54630** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54630) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-54630)
- **CVE-2026-53942** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53942)
- **CVE-2026-53921** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53921)
- **CVE-2026-46652** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46652)
- **CVE-2026-46651** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-46651)
- **CVE-2026-25784** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-25784) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-25784)
- **CVE-2026-19677** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19677)
- **CVE-2026-115931** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115931)
- **CVE-2026-115893** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115893)
- **CVE-2026-115889** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115889)
- **CVE-2026-115812** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115812)
- **CVE-2026-115727** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115727)
- **CVE-2026-115547** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115547) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115547)
- **CVE-2026-115384** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115384) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115384)
- **CVE-2026-115377** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115377) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115377)
- **CVE-2026-115375** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115375) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115375)
- **CVE-2026-115372** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115372) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115372)
- **CVE-2026-115353** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115353) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115353)
- **CVE-2026-115324** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115324) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115324)
- **CVE-2026-114612** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114612) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114612)
- **CVE-2026-114611** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114611) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114611)
- **CVE-2026-114607** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114607) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114607)
- **CVE-2026-114357** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114357)
- **CVE-2026-114220** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114220) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114220)
- **CVE-2026-114219** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114219) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114219)
- **CVE-2026-112862** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112862) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112862)
- **CVE-2026-112860** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112860) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112860)
- **CVE-2026-112859** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112859)
- **CVE-2026-112858** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112858)
- **CVE-2026-112857** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112857)
- **CVE-2026-112856** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112856)
- **CVE-2026-112855** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112855)
- **CVE-2026-112854** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112854)
- **CVE-2026-112853** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112853)
- **CVE-2026-112851** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112851)
- **CVE-2026-112848** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112848)
- **CVE-2026-112847** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112847)
- **CVE-2026-112846** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112846)
- **CVE-2026-112832** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112832) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112832)
- **CVE-2026-112327** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112327) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112327)
- **CVE-2026-112241** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112241) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112241)
- **CVE-2026-111594** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111594) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111594)
- **CVE-2026-111497** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111497)
- **CVE-2026-110243** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110243) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-110243)
- **CVE-2026-110063** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110063) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-110063)
- **CVE-2026-109619** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109619) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109619)
- **CVE-2026-109122** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109122) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109122)
- **CVE-2026-107861** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107861) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-107861)
- **CVE-2026-107685** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107685)
- **CVE-2026-105014** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105014) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105014)
- **CVE-2026-102785** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102785) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-102785)
- **CVE-2025-30054** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-30054)
- **CVE-2025-30050** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-30050)
- **CVE-2025-30047** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-30047)
- **CVE-2025-30046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-30046)
- **CVE-2022-51026** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-51026) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2022-51026)
- **CVE-2021-48016** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-48016) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2021-48016)
- **CVE-2026-114400** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114400) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114400)
- **CVE-2026-114396** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114396) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114396)
- **CVE-2026-114117** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114117) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114117)
- **CVE-2026-114102** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114102) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114102)
- **CVE-2026-114092** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114092) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114092)
- **CVE-2026-114067** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114067)
- **CVE-2026-114042** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114042) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114042)
- **CVE-2026-113722** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113722) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113722)
- **CVE-2026-113658** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113658) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113658)
- **CVE-2026-113606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113606) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113606)
- **CVE-2026-113390** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113390) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113390)
- **CVE-2026-113354** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113354) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113354)
- **CVE-2026-113331** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113331)
- **CVE-2026-113147** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113147) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113147)
- **CVE-2026-113146** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113146) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113146)
- **CVE-2026-113141** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113141) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113141)
- **CVE-2026-113118** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113118) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113118)
- **CVE-2026-113022** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113022) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113022)
- **CVE-2026-113009** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113009) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113009)
- **CVE-2026-112995** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112995) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112995)
- **CVE-2026-112940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112940) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112940)
- **CVE-2026-111765** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111765) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111765)
- **CVE-2026-111756** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111756) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111756)
- **CVE-2016-20104** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-20104)
- **CVE-2016-20100** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-20100)
- **CVE-2015-20128** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2015-20128)
- **CVE-2015-20124** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2015-20124)
- **CVE-2014-125134** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2014-125134)
- **CVE-2014-125133** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2014-125133)
- **CVE-2026-9869** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9869) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9869)
- **CVE-2026-9827** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9827) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9827)
- **CVE-2026-9817** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9817) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9817)
- **CVE-2026-9814** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9814) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9814)
- **CVE-2026-96639** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96639) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96639)
- **CVE-2026-9660** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9660) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9660)
- **CVE-2026-9659** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9659) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9659)
- **CVE-2026-96355** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96355) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96355)
- **CVE-2026-92559** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92559) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-92559)
- **CVE-2026-91665** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91665) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91665)
- **CVE-2026-91663** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91663) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91663)
- **CVE-2026-91658** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91658) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91658)
- **CVE-2026-91656** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91656) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91656)
- **CVE-2026-91655** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91655) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91655)
- **CVE-2026-91644** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91644) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91644)
- **CVE-2026-91638** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91638)
- **CVE-2026-91637** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91637)
- **CVE-2026-91403** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91403) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-91403)
- **CVE-2026-91305** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91305)
- **CVE-2026-91299** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91299)
- **CVE-2026-91265** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91265)
- **CVE-2026-89035** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89035) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-89035)
- **CVE-2026-87095** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87095) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87095)
- **CVE-2026-76531** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76531) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76531)
- **CVE-2026-76475** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76475) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76475)
- **CVE-2026-76474** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76474) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76474)
- **CVE-2026-76473** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76473) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76473)
- **CVE-2026-76466** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76466) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76466)
- **CVE-2026-76302** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76302) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76302)
- **CVE-2026-76299** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76299) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76299)
- **CVE-2026-71195** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71195)
- **CVE-2026-42026** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42026) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42026)
- **CVE-2026-42025** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42025) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42025)
- **CVE-2026-42024** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42024) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42024)
- **CVE-2026-42023** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42023) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42023)
- **CVE-2026-42022** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42022) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42022)
- **CVE-2026-42021** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42021) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42021)
- **CVE-2026-42020** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42020) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42020)
- **CVE-2026-42019** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42019) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42019)
- **CVE-2026-41223** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-41223) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-41223)
- **CVE-2026-41222** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-41222) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-41222)
- **CVE-2026-40627** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-40627) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-40627)
- **CVE-2026-40615** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-40615) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-40615)
- **CVE-2026-35499** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-35499) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-35499)
- **CVE-2026-33568** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-33568) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-33568)
- **CVE-2026-28763** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-28763) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-28763)
- **CVE-2026-20043** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20043)
- **CVE-2026-114575** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114575) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114575)
- **CVE-2026-114509** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114509) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114509)
- **CVE-2026-114493** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114493) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114493)
- **CVE-2026-114403** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114403) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114403)
- **CVE-2026-114383** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114383) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114383)
- **CVE-2026-114382** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114382) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114382)
- **CVE-2026-114139** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114139) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114139)
- **CVE-2026-114119** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114119) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114119)
- **CVE-2026-114108** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114108) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114108)
- **CVE-2026-114053** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114053) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114053)
- **CVE-2026-113788** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113788) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113788)
- **CVE-2026-113682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113682) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113682)
- **CVE-2026-113342** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113342)
- **CVE-2026-113336** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113336)
- **CVE-2026-113328** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113328)
- **CVE-2026-113300** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113300) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-113300)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
