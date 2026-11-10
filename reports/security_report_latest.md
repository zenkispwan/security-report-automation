# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**42** 筆符合目前門檻的重要變化；事件統計：EXPLOITATION_CHANGED=1、NEW_CVE=38、NEW_KEV=4、RANSOMWARE_USE_CHANGED=1。
- Intelligence 候選：**30** 筆；P1 **4**、P2 **0**、P3 **0**、WATCH **26**。
- Baseline：state / generated_at=2026-11-09T07:27:59.747862+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-123218、CVE-2026-123158、CVE-2026-116779、CVE-2026-102895。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **42** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-123218｜IBM / Aspera Faspex
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00396 / percentile=0.34123
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-07T04:17:28.900 / 2026-11-10T05:17:59.200
- **官方描述（原文）**：IBM Aspera Faspex contains an incorrect authorization vulnerability that could allow an authenticated user to craft a specific message to bypass authorization, causing privilege escalations.

### 2. CVE-2026-123158｜OpenBSD / OpenSSH
- **Delta event**：NEW_KEV (from=false; to=true)；EXPLOITATION_CHANGED (from=poc; to=known_exploited)；RANSOMWARE_USE_CHANGED (from=未確認; to=Unknown)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)、DELTA_EXPLOIT_ESCALATION(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.01014 / percentile=0.63482
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-05T16:17:47.110 / 2026-11-10T05:17:58.923
- **官方描述（原文）**：OpenBSD OpenSSH on Linux contains an unexpected status code or return value vulnerability that could allow for authentication bypass.

### 3. CVE-2026-116779｜SignalWire / FreeSwitch
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01299 / percentile=0.70632
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-05T20:17:44.790 / 2026-11-10T05:17:57.830
- **官方描述（原文）**：SignalWire FreeSwitch contains a code injection vulnerability that permits configuration and credential disclosure, arbitrary call control, and command execution.

### 4. CVE-2026-102895｜GPUStack / GPUStack
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00331 / percentile=0.2646
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-04T22:17:44.613 / 2026-11-10T05:17:40.970
- **官方描述（原文）**：GPUStack contains an improper authentication vulnerability which could allow unauthenticated administrative access, including user and model changes, persistent administrator API-key creation, disclosure of worker and cloud-provider secrets, and code execution through POST /v2/inference-backends/from-yaml.

### 5. CVE-2026-112314｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T19:16:39.867)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T19:16:39.867 / 2026-11-09T20:18:04.227
- **官方描述（原文）**：clnttcp_call() in lib/rpc/clnt_tcp.c in MIT Kerberos 5 (aka krb5) does not free the RPC reply verifier between retries, which allows remote attackers to cause a denial of service (memory leak in GSS-RPC client programs) by injecting RPC replies with mismatched XIDs or by triggering authentication retries.

### 6. CVE-2026-89126｜SAP_SE / SAP Web Dispatcher
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:22.420)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:22.420 / 2026-11-10T01:17:22.420
- **官方描述（原文）**：SAP Web Dispatcher does not sufficiently validate certain network input processed by an internal component. An unauthenticated attacker could send specially crafted network traffic to trigger a memory corruption condition in the affected functionality. Successful exploitation could allow the attacker to execute arbitrary code and fully compromise the system, resulting in a high impact on confidentiality, integrity and availability of the system.

### 7. CVE-2026-89119｜SAP_SE / SAP Web Dispatcher and Internet Communication Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:22.103)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:22.103 / 2026-11-10T01:17:22.103
- **官方描述（原文）**：SAP Web Dispatcher and SAP NetWeaver Application Server ABAP (Internet Communication Manager) do not perform sufficient request validation in certain administrative functionality. In the context of Application Server ABAP and SAP Web Dispatcher, an unauthenticated attacker could trick a logged-on administrator into visiting a malicious link. Visiting the link could cause unintended actions in the administrator's session. Successful exploitation could lead to a full compromise of the underlying operating system, resulting in a high impact on confidentiality, integrity, and availability.

### 8. CVE-2026-89103｜SAP_SE / SAP Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:21.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:21.013 / 2026-11-10T01:17:21.013
- **官方描述（原文）**：SAP Gateway activates the default Access Control List with high privileges allowing categorization of external attacker as internal application server. As a result an unauthenticated attacker with network access to the SAP Gateway could exploit this weakness to potentially perform unauthorized actions within the application environment, resulting in a high impact on the confidentiality, integrity, and availability of the affected system.

### 9. CVE-2026-76965｜SAP_SE / SAP NetWeaver and ABAP Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:20.387)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:20.387 / 2026-11-10T01:17:20.387
- **官方描述（原文）**：SAP NetWeaver Application Server ABAP and ABAP Platform does not perform necessary authorization checks for certain internal functionality. An attacker with low privileges could invoke affected functionality to execute arbitrary operating system commands on the underlying host. Successful exploitation could impact resources beyond the vulnerable component, resulting in a high impact on confidentiality, integrity and availability of the system.

### 10. CVE-2026-76964｜SAP_SE / SAP NetWeaver AS ABAP (Internet Communication Manager)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:20.240)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:20.240 / 2026-11-10T01:17:20.240
- **官方描述（原文）**：SAP NetWeaver Application Server ABAP does not sufficiently validate certain network input processed by an internal component. An unauthenticated attacker could send specially crafted network traffic to trigger a memory corruption condition in the affected functionality. Successful exploitation could allow the attacker to execute arbitrary code and fully compromise the system, resulting in a high impact on confidentiality, integrity and availability of the system.

### 11. CVE-2026-13312｜Axis Communications AB / AXIS Camera Station Pro
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T06:17:08.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T06:17:08.587 / 2026-11-10T06:17:08.587
- **官方描述（原文）**：A vulnerability that could allow an attacker to compromise a system.

### 12. CVE-2026-125384｜go2ismail / Asp.Net-Core-Inventory-Order-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T00:17:11.667)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T00:17:11.667 / 2026-11-10T00:17:11.667
- **官方描述（原文）**：INDOTALENT WHMS before 10.20261109 contains a default credentials vulnerability that allows unauthenticated attackers to gain administrator access because UserAdminSeeder creates admin@root.com with password 123456. Attackers can log in with these credentials, which carry every admin role and no forced password change, to fully control deployments that kept them.

### 13. CVE-2026-125383｜go2ismail / Asp.Net-Core-Inventory-Order-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T00:17:11.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T00:17:11.510 / 2026-11-10T00:17:11.510
- **官方描述（原文）**：INDOTALENT WHMS (Asp.Net-Core-Inventory-Order-Management-System) before 10.20261109 contains an authentication bypass vulnerability caused by a hard-coded JWT signing key, issuer and audience in appsettings.json. Unauthenticated remote attackers can forge tokens for any user ID and role that the Tokens/DI.cs validator trusts, gaining administrator access to the entire API.

### 14. CVE-2026-125370｜kubero-dev / kubero
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T00:17:09.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T00:17:09.237 / 2026-11-10T00:17:09.370
- **官方描述（原文）**：Kubero 3.0.0 through 3.1.1 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to forge administrative JWTs by using a hardcoded fallback signing secret when JWT_SECRET is unset. Attackers can sign tokens with arbitrary role, userGroups and permissions claims, which JwtStrategy.validate() trusts without a database lookup, to take control of pipelines, applications, users and API tokens.

### 15. CVE-2026-125120｜Automattic / mongoose
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T23:17:22.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T23:17:22.587 / 2026-11-09T23:17:22.587
- **官方描述（原文）**：Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. Prior to 6.13.11, 7.8.12, 8.24.3, and 9.9.2, Mongoose countDocuments() does not apply the configured sanitizeFilter query selector injection defense. An application that enables sanitizeFilter and passes attacker-controlled filter values to countDocuments() can therefore process query operator objects as operators rather than literal values, causing the count to include documents that should not match and potentially undermining authorization or application logic based on that count. This issue is fixed in versions 6.13.11, 7.8.12, 8.24.3, and 9.9.2.

### 16. CVE-2026-125086｜D-Link / M60
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:19.640)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:19.640 / 2026-11-10T01:17:19.810
- **官方描述（原文）**：A vulnerability has been found in D-Link M60 1.12.B01. Impacted is the function system of the file /etc/emDaemon/mosquitto.conf of the component emDaemon MQTT Broker. Such manipulation leads to hard-coded credentials. The attack can be executed remotely. The exploit has been disclosed to the public and may be used.

### 17. CVE-2026-124600｜GeoVision Inc. / GV-Face
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:18.467)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:18.467 / 2026-11-10T01:17:18.467
- **官方描述（原文）**：GV-Face transmits sensitive user credentials and related authentication data over unencrypted HTTP connections. The HTTP traffic is not encrypted, an attacker with the ability to intercept network traffic.

### 18. CVE-2026-124580｜Chengdu Feiyuxing Technology / VW2100
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T08:17:02.923)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.02794 / percentile=0.8653
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T08:17:02.923 / 2026-11-09T08:17:03.070
- **官方描述（原文）**：A vulnerability was found in Chengdu Feiyuxing Technology VW2100 and VEC10GP 1.0 B-MB3W202-210825-r11775. This impacts the function handle_wechat_cn_wifi of the file var/html/webserver of the component Weixin Auth Endpoint. The manipulation of the argument extend results in os command injection. The attack can be executed remotely. The exploit has been made public and could be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 19. CVE-2026-124079｜rConfig / rConfig Core
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T13:17:07.503)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T13:17:07.503 / 2026-11-09T13:17:07.503
- **官方描述（原文）**：rConfig Core 8.0.0 before 8.2.19 and rConfig Pro before 8.4.1 contain a deserialization of untrusted data vulnerability that allows unauthenticated network attackers to execute arbitrary code by pushing a crafted serialized job onto the Redis-backed Laravel Horizon queue, which runs without authentication in affected deployments. Laravel's CallQueuedHandler unserializes the job without class restrictions, allowing attackers to instantiate the existing App\\Jobs\\TaskDownloadRun class and invoke an attacker-controlled Artisan command. Attackers can leverage the bundled laravel/tinker package to execute arbitrary PHP and operating system commands as the queue worker's user, write a persistent web shell into the web-served storage/app/public directory, and read database credentials, stored device credentials, and API tokens. Where Redis is not directly reachable, authenticated attackers can deliver the payload through the application by configuring a device target that points at the rConfig server's loopback address.

### 20. CVE-2026-124001｜nasa-jpl / ION-DTN
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T19:16:48.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T19:16:48.003 / 2026-11-09T19:16:48.147
- **官方描述（原文）**：NASA JPL ION-DTN 2.2.1b through 4.2.0 contains an integer overflow vulnerability in the Datagram Retransmission (DGR) convergence layer that allows attackers to corrupt heap memory by sending a maliciously crafted 64-bit svcDataLength value that wraps a 32-bit allocation size calculation. Attackers can exploit the dgr_receive API's unchecked memcpy operation using synthetic datagrams or DGR traffic over internal IPC or custom transports to trigger an out-of-bounds write, leading to denial of service or potential remote code execution.

### 21. CVE-2026-123870｜Eclipse Foundation / otterdog
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T09:16:58.653)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.00302 / percentile=0.23141
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T09:16:58.653 / 2026-11-09T09:16:58.653
- **官方描述（原文）**：The otterdog webapp evaluates a format-string built from the incoming GitHub webhook JSON body using Python's eval(). When the GITHUB_WEBHOOK_SECRET configuration value is unset or empty (the code default is None), the HMAC signature check is skipped entirely, allowing an unauthenticated network client to reach the eval() sink with attacker-controlled input and execute arbitrary Python on the webapp host.

### 22. CVE-2026-123815｜pyload / pyload
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T22:18:37.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T22:18:37.943 / 2026-11-09T22:18:38.067
- **官方描述（原文）**：pyLoad is a free and open-source download manager written in Python. Prior to 0.5.0b3.dev102, UnTar._safe_extractall in src/pyload/plugins/extractors/UnTar.py validates archive member paths and link targets but does not call TarInfo.isdev to reject special tar member types before calling tarfile.extractall. On supported Python 3.9 through 3.13 runtimes, tarfile defaults to the fully_trusted extraction filter, so a user with ADD and STATUS permissions can cause extraction of a crafted archive containing character devices, block devices, or FIFOs. Python 3.14 defaults to a safe extraction filter. When pyLoad runs with operating-system privileges that permit device creation, including the official root-based Docker deployment, the archive can expose raw devices and compromise the host. Non-root deployments can still create FIFOs that cause hangs or IPC confusion. This issue is fixed in version 0.5.0b3.dev102.

### 23. CVE-2026-123807｜SignalK / signalk-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T22:18:36.663)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T22:18:36.663 / 2026-11-09T22:18:36.663
- **官方描述（原文）**：Signal K Server is a server application that runs on a central hub in a boat. From 2.0.0 until 2.34.0 for Signal K Server and from 1.0.0 until 1.5.3 for @signalk/resources-provider, the v2 REST route GET /signalk/v2/api/resources/:resourceType/:resourceId accepts an unsafe resourceId that can escape the intended resource directory. The route passes the attacker-controlled resourceId through src/api/resources/index.ts to FileStore.getResource() in packages/resources-provider-plugin/src/filestorage.ts without adequate path containment, allowing arbitrary JSON files reachable by the server to be read. Related PUT and DELETE resource operations can write or delete files outside the storage root. Deployments with allow_readonly enabled permit anonymous reads, while other deployments require a readonly user token. Reading security.json exposes the HS256 JWT signing secret and password hashes, allowing an attacker to forge an administrator token. Administrative access to POST /skServer/providers can then create an Execute provider that runs commands with the server process privileges and persists its configuration across restarts. This issue is fixed in Signal K Server 2.34.0 and @signalk/resources-provider 1.5.3.

### 24. CVE-2026-123800｜supertokens / supertokens-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T19:16:46.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T19:16:46.647 / 2026-11-09T19:16:46.647
- **官方描述（原文）**：SuperTokens Core is an open source authentication server. From 6.0.0 until 6.0.24, 7.0.23, 8.0.7, 9.0.6, 9.1.6, 9.2.7, 9.3.5, 10.0.8, 10.1.9, 11.0.9, 11.1.4, 11.2.4, 11.3.8, 11.4.8, 12.0.11, 12.1.2, 12.2.1, and 12.3.1, Multitenancy.checkPermissionsForCreateOrUpdate in src/main/java/io/supertokens/multitenancy/Multitenancy.java does not adequately authorize updates to a parent connection URI domain or the base tenant. In a licensed multi-tenant deployment with multiple applications under one non-default connection URI domain and separate api_keys, an attacker holding one application's valid API key can update the parent domain because the CUD-target branch checks the domain without requiring the source application and tenant to be public. Because api_keys is not protected, the attacker can replace the parent key and then sibling application keys, read or modify sibling users, obtain sessions as those users, establish persistence through a sibling dashboard user, and lock out the sibling application's own key. In the advisory's v2 create or update handlers, omitting the optional identifier produces a base-tenant target that skips the permission branches and enterprise-feature gate, allowing changes to firstFactors, required secondary factors, and recipe-enabled flags that affect login integrity and availability. The base-target variant still rejects coreConfig and does not establish key theft. This issue is fixed in versions 6.0.24, 7.0.23, 8.0.7, 9.0.6, 9.1.6, 9.2.7, 9.3.5, 10.0.8, 10.1.9, 11.0.9, 11.1.4, 11.2.4, 11.3.8, 11.4.8, 12.0.11, 12.1.2, 12.2.1, and 12.3.1.

### 25. CVE-2026-123270｜Redpanda Data / Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T18:17:25.207)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T18:17:25.207 / 2026-11-09T18:17:25.207
- **官方描述（原文）**：Redpanda Connect versions 4.39 to 4.110 contain a missing authentication vulnerability that enables unauthenticated remote code execution (RCE). In streams mode, the management HTTP API is exposed on `0.0.0.0:4195`, but authentication is disabled by default and there is no authentication gate protecting the stream CRUD routes. An unauthenticated attacker with network access to TCP/4195 can `POST` a malicious pipeline definition to `/streams/{id}` that includes code-executing processors such as `command`, `subprocess`, `ffi`, or unsafe `sql_raw`, thereby achieving arbitrary RCE on the host with the permissions of the Redpanda Connect service account. Because pipelines can also return command output in-band via HTTP, this vulnerability enables full host compromise, credential theft, and data exfiltration with no user interaction or credentials required. Starting with v4.111, the API endpoint was reconfigured as opt-in, so this and later versions are no longer vulnerable by default. However, RCE remains achievable on v4.111 and later if the management API is manually enabled via the `--bind-http` flag.

### 26. CVE-2026-120017｜SAP_SE / SAP NetWeaver AS ABAP and ABAP Platform (SAML2 Service Provider)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:16.803)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:16.803 / 2026-11-10T01:17:16.803
- **官方描述（原文）**：SAP NetWeaver AS ABAP and ABAP Platform does not perform sufficient verification of incoming authentication assertions under certain configurations. An unauthenticated attacker could submit specially crafted data to bypass authentication and impersonate arbitrary users, including privileged accounts. Successful exploitation could cause a full system compromise, with the impact potentially extending to connected components and systems beyond the affected system. This results in a high impact on confidentiality, integrity, and availability of the application.

### 27. CVE-2026-119756｜arendst / Tasmota
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T18:17:22.320)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T18:17:22.320 / 2026-11-09T23:17:13.907
- **官方描述（原文）**：Tasmota through 16.0.0, fixed in commit e97e1e4, contains a heap out-of-bounds write vulnerability in SendReceiveDeviceGroupMessage() that allows unauthenticated attackers on the local network to corrupt heap memory by sending crafted Device Groups messages over UDP port 4447 that cause the log_remaining counter to go negative and writes to exceed the fixed 512-byte buffer. Attackers can exploit this flaw to crash the device or potentially achieve native code execution on ESP8266 and ESP32 platforms that lack ASLR and heap cookies.

### 28. CVE-2026-118462｜CompuGroup Medical / Infantia
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T12:16:37.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T12:16:37.130 / 2026-11-09T12:16:37.130
- **官方描述（原文）**：Update components download and execute code without proper authenticity verification, relying on ignored hashes or forgeable checksums. Some update paths also permit archive traversal or script execution.

### 29. CVE-2026-115934｜craftcms / cms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T23:17:12.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T23:17:12.470 / 2026-11-09T23:17:12.470
- **官方描述（原文）**：An unauthenticated SQL injection can occur on the front end of any site that uses craft.search to perform a search, allowing stacked query execution and enabling escalation to an administrator. Note that this only affects MySQL/MariaDB. Impact * SQL injection — The attribute parameter is concatenated into the query unsanitized, and because PDO runs with emulated prepares, stacked statements execute. This gives unauthenticated read and write access to the application database. * Privilege escalation to administrator — The write primitive was used to set the admin flag on user ID 1 in the users table, confirmed by reading the value back. Craft short-circuits its permission checks on this single column, so no further changes were needed. The same primitive can overwrite any account’s password hash. Update to the patched versions (4.18.9 and 5.11.2) to get the fix. If you cannot update immediately, you can block front-end requests with %5Battribute%5D and [attribute] anywhere in the query string as a temporary mitigation.

### 30. CVE-2026-115646｜Hitachi / HiRDB Server Version 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T05:17:48.627)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T05:17:48.627 / 2026-11-10T05:17:48.627
- **官方描述（原文）**：Partial String Comparison Vulnerability in HiRDB. This issue affects HiRDB Server Version 10: from 10-00 before 10-12-01; HiRDB Server Version 9: from 09-50-06 through 09-66-22; HiRDB Server with Additional Function Version 9: from 09-50-/F through 09-66/V; HiRDB Server Version 9(32): from 09-50-06 through 09-66-22; HiRDB Server with Additional Function Version 9(32): from 09-50-/F through 09-66-/V.

### 31. CVE-2026-115252｜Unknown / Confection WordPress Cable
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T11:17:21.143)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T11:17:21.143 / 2026-11-09T14:17:06.253
- **官方描述（原文）**：The Confection WordPress Cable WordPress plugin from 0.4.0 to 0.4.7 does not perform any capability or nonce checks before saving its settings and writing one of them, unmodified, into a standalone PHP file that it then serves, allowing unauthenticated users to execute arbitrary PHP code on the server.

### 32. CVE-2026-110469｜Fundacja Widzialni / WidzialniCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T13:17:03.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T13:17:03.910 / 2026-11-09T18:17:19.690
- **官方描述（原文）**：WidzialniCMS is vulnerable to Unrestricted File Upload in the /panel/upload.php endpoint. Due to a client-controlled permission check parameter and insufficient validation of the uploadPath parameter, an unauthenticated attacker can upload arbitrary files to any locations on the server, leading to Remote Code Execution. This issue has been fixed in version 2.5.

### 33. CVE-2026-110468｜Fundacja Widzialni / WidzialniCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T13:17:03.687)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T13:17:03.687 / 2026-11-09T18:17:19.563
- **官方描述（原文）**：WidzialniCMS is vulnerable to Unrestricted File Upload in the /panel/controllers/save_photo.php endpoint. Due to a client-controlled permission check parameter and insufficient validation of the currentpath parameter, an unauthenticated attacker can upload arbitrary files to any locations on the server, leading to Remote Code Execution. This issue has been fixed in version 2.5.

### 34. CVE-2026-109803｜SAP_SE / SAP NetWeaver Knowledge Management (XML Forms)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:14.477)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:14.477 / 2026-11-10T01:17:14.477
- **官方描述（原文）**：SAP NetWeaver Knowledge Management (XML Forms) does not sufficiently restrict the selection of XSL transformations processed by the affected functionality. Under certain conditions, an authenticated user with access to the affected functionality could cause an unauthorized XSL transformation to be processed, potentially leading to arbitrary code execution in the application context. Successful exploitation could impact the confidentiality, integrity, and availability of the application.

### 35. CVE-2026-109798｜SAP_SE / SAP BusinessObjects Business Intelligence Platform (Web Intelligence)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:13.747)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:13.747 / 2026-11-10T01:17:13.747
- **官方描述（原文）**：SAP BusinessObjects Business Intelligence Platform (Web Intelligence) does not properly restrict external entity resolution when processing OLAP connection requests. An authenticated attacker could exploit this vulnerability to access restricted resources, enabling them to read sensitive files on the server and reach internal systems that are not otherwise exposed, impacting resources beyond the vulnerable component, resulting in a high impact on confidentiality and a low impact on both integrity and availability.

### 36. CVE-2026-109795｜SAP_SE / S4CRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:13.330)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:13.330 / 2026-11-10T01:17:13.330
- **官方描述（原文）**：SAP NetWeaver does not perform necessary authorization checks and lacks sufficient input validation in certain remote-enabled functionality. An attacker with low privileges could send specially crafted input through a remote interface to inject and execute arbitrary code within the affected system. Successful exploitation could extend the attacker's reach beyond the vulnerable component, resulting in a high impact on confidentiality, integrity and availability.

### 37. CVE-2026-107246｜WebPros / Plesk extension "Site Import"
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T01:17:12.880)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T01:17:12.880 / 2026-11-10T01:17:12.880
- **官方描述（原文）**：The Plesk extension "Site Import" before 1.13.2 does not properly validate domain and session identifiers, allowing path traversal. This lets a non-owner subscription user redirect a privileged backend session into a directory they control, resulting in arbitrary code execution as root.

### 38. CVE-2026-104989｜Chaos Software / V-Ray Swarm
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T17:17:07.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T17:17:07.237 / 2026-11-09T18:17:19.433
- **官方描述（原文）**：Uncontrolled search path element in package upload feature in Chaos Software V-Ray versions through 2.0.19 allows remote unauthenticated attackers to execute arbitrary code via redirecting access to libraries

### 39. CVE-2026-112319｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T19:16:40.727)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T19:16:40.727 / 2026-11-09T20:18:04.357
- **官方描述（原文）**：The GSS-RPC layer in MIT Kerberos 5 (aka krb5) does not enforce size limits on XDR-decoded data, which allows remote authenticated users to cause a denial of service (memory exhaustion or excessive CPU consumption in kadmind) via crafted RPC requests that trigger unbounded memory allocations during XDR decoding.

### 40. CVE-2026-124621｜kongxin-github / Java_Library_Management_System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T11:17:24.960)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T11:17:24.960 / 2026-11-09T12:16:38.107
- **官方描述（原文）**：A vulnerability was determined in kongxin-github Java_Library_Management_System up to 70a6eb6b96fe64575d8051f1a59055bfc5dc5885. This affects the function UpdateAdmin.deleteuser/UpdateAdmin.updateadmin/UpdateAdmin.updatepass/Book.addbook/Book.modifybook/Book.deletebook/Category.addcategory/Category.setcategory/Landing.sureadmin of the file src/view/MainInterface.java of the component Swing UI Layer. This manipulation causes improper authorization. Remote exploitation of the attack is possible. The exploit has been publicly disclosed and may be utilized. This product follows a rolling release approach for continuous delivery, so version details for affected or updated releases are not provided. The project was informed of the problem early through an issue report but has not responded yet.

### 41. CVE-2026-124587｜elizaOS / eliza
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T10:17:08.950)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T10:17:08.950 / 2026-11-09T23:17:20.170
- **官方描述（原文）**：A vulnerability was identified in elizaOS eliza 2.0.3-beta.7. The affected element is an unknown function of the file packages/app/platforms/electrobun/src/lifecycle/api-base-owner.ts of the component HTTP Server. Such manipulation leads to information disclosure. It is possible to launch the attack remotely. The exploit is publicly available and might be used. The name of the patch is cf6fa193017e70884e01c5bb7890f74b6b2b79d2. A patch should be applied to remediate this issue.

### 42. CVE-2026-124582｜未確認 / WebTorrent
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-09T09:16:59.053)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00425 / percentile=0.37093
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-09T09:16:59.053 / 2026-11-09T23:17:20.017
- **官方描述（原文）**：A vulnerability was identified in WebTorrent up to 2.8.5/3.0.21. Affected by this vulnerability is the function getFileModtimes of the file torrent.js of the component File Path Handler. Such manipulation of the argument file.path leads to path traversal. The attack may be performed from remote. The exploit is publicly available and might be used. The reported GitHub issue was closed with the label "not planned".


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-123218｜IBM / Aspera Faspex
- **Title**：IBM Aspera Faspex Incorrect Authorization Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00396 / percentile=0.34123
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：IBM Aspera Faspex contains an incorrect authorization vulnerability that could allow an authenticated user to craft a specific message to bypass authorization, causing privilege escalations.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-123158｜OpenBSD / OpenSSH
- **Title**：OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)、DELTA_EXPLOIT_ESCALATION(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.01014 / percentile=0.63482
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：OpenBSD OpenSSH on Linux contains an unexpected status code or return value vulnerability that could allow for authentication bypass.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-116779｜SignalWire / FreeSwitch
- **Title**：SignalWire FreeSwitch Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.01299 / percentile=0.70632
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：SignalWire FreeSwitch contains a code injection vulnerability that permits configuration and credential disclosure, arbitrary call control, and command execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-102895｜GPUStack / GPUStack
- **Title**：GPUStack Improper Authentication Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00331 / percentile=0.2646
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GPUStack contains an improper authentication vulnerability which could allow unauthenticated administrative access, including user and model changes, persistent administrator API-key creation, disclosure of worker and cloud-provider secrets, and code execution through POST /v2/inference-backends/from-yaml.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-112314 | WATCH / 30 | Red Hat / Red Hat Enterprise Linux 10 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89126 | WATCH / 28 | SAP_SE / SAP Web Dispatcher | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89119 | WATCH / 28 | SAP_SE / SAP Web Dispatcher and Internet Communication Manager | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89103 | WATCH / 28 | SAP_SE / SAP Gateway | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76965 | WATCH / 28 | SAP_SE / SAP NetWeaver and ABAP Platform | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-76964 | WATCH / 28 | SAP_SE / SAP NetWeaver AS ABAP (Internet Communication Manager) | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-13312 | WATCH / 28 | Axis Communications AB / AXIS Camera Station Pro | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-125384 | WATCH / 28 | go2ismail / Asp.Net-Core-Inventory-Order-Management-System | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-125383 | WATCH / 28 | go2ismail / Asp.Net-Core-Inventory-Order-Management-System | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-125370 | WATCH / 28 | kubero-dev / kubero | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-125120 | WATCH / 28 | Automattic / mongoose | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-125086 | WATCH / 28 | D-Link / M60 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124600 | WATCH / 28 | GeoVision Inc. / GV-Face | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124580 | WATCH / 28 | Chengdu Feiyuxing Technology / VW2100 | v4.0 9.3 (CRITICAL) | 0.02794 / percentile=0.8653 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124079 | WATCH / 28 | rConfig / rConfig Core | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-124001 | WATCH / 28 | nasa-jpl / ION-DTN | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-123870 | WATCH / 28 | Eclipse Foundation / otterdog | v4.0 9.5 (CRITICAL) | 0.00302 / percentile=0.23141 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-123815 | WATCH / 28 | pyload / pyload | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-123807 | WATCH / 28 | SignalK / signalk-server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-123800 | WATCH / 28 | supertokens / supertokens-core | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-123270 | WATCH / 28 | Redpanda Data / Connect | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-120017 | WATCH / 28 | SAP_SE / SAP NetWeaver AS ABAP and ABAP Platform (SAML2 Service Provider) | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-119756 | WATCH / 28 | arendst / Tasmota | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-118462 | WATCH / 28 | CompuGroup Medical / Infantia | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115934 | WATCH / 28 | craftcms / cms | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-115646 | WATCH / 28 | Hitachi / HiRDB Server Version 10 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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
- EPSS 未確認：24；Exploitation status 未確認：23。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-10T07:54:06.032342+00:00`；Delta generated at：`2026-11-10T07:54:06.032342+00:00`。

---

## 可驗證資料來源

- **CVE-2026-123218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123218) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-123218) · [Vendor / Advisory (ibm.com)](https://www.ibm.com/support/pages/node/7295921) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-123158** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123158) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-123158) · [Vendor / Advisory (openssh.org)](https://www.openssh.org/releasenotes.html) · [Vendor / Advisory (alpinelinux.org)](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/) · [Vendor / Advisory (github.com)](https://github.com/openssh/openssh-portable/commit/4353fdc43ef646c43a8dda7025cc1a898caf1482) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-116779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116779) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116779) · [Vendor / Advisory (github.com)](https://github.com/signalwire/freeswitch/security/advisories/GHSA-mg63-h38w-8p9p) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-102895** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102895) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-102895) · [Vendor / Advisory (github.com)](https://github.com/gpustack/gpustack/security/advisories/GHSA-gj9m-f8ph-pmhr) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-112314** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112314)
- **CVE-2026-89126** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89126)
- **CVE-2026-89119** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89119)
- **CVE-2026-89103** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89103)
- **CVE-2026-76965** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76965)
- **CVE-2026-76964** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76964)
- **CVE-2026-13312** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13312)
- **CVE-2026-125384** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125384)
- **CVE-2026-125383** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125383)
- **CVE-2026-125370** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125370)
- **CVE-2026-125120** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125120)
- **CVE-2026-125086** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125086)
- **CVE-2026-124600** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124600)
- **CVE-2026-124580** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124580) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124580)
- **CVE-2026-124079** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124079)
- **CVE-2026-124001** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124001)
- **CVE-2026-123870** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123870) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-123870)
- **CVE-2026-123815** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123815)
- **CVE-2026-123807** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123807)
- **CVE-2026-123800** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123800)
- **CVE-2026-123270** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123270)
- **CVE-2026-120017** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120017)
- **CVE-2026-119756** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119756)
- **CVE-2026-118462** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118462)
- **CVE-2026-115934** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115934)
- **CVE-2026-115646** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115646)
- **CVE-2026-115252** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115252)
- **CVE-2026-110469** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110469)
- **CVE-2026-110468** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110468)
- **CVE-2026-109803** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109803)
- **CVE-2026-109798** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109798)
- **CVE-2026-109795** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109795)
- **CVE-2026-107246** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107246)
- **CVE-2026-104989** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104989)
- **CVE-2026-112319** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112319)
- **CVE-2026-124621** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124621)
- **CVE-2026-124587** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124587)
- **CVE-2026-124582** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124582) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124582)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
