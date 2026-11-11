# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**107** 筆符合目前門檻的重要變化；事件統計：EPSS_INCREASED=1、NEW_CVE=102、NEW_KEV=6。
- Intelligence 候選：**30** 筆；P1 **7**、P2 **0**、P3 **1**、WATCH **22**。
- Baseline：state / generated_at=2026-11-10T07:54:06.032342+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-125350、CVE-2026-116606、CVE-2026-20320、CVE-2026-124194、CVE-2026-111560。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **107** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-125350｜Google / Chromium
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T18:17:35.237)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-10T18:17:35.237 / 2026-11-11T05:19:38.220
- **官方描述（原文）**：Google Chromium contains a use-after-free vulnerability in the XML component that could allow a remote attacker to execute arbitrary code inside the sandbox via a specially crafted webpage. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.

### 2. CVE-2026-116606｜Barracuda Networks / Barracuda Email Security Gateway (ESG)
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.01602 / percentile=0.76026
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-02T13:17:37.017 / 2026-11-11T05:19:26.320
- **官方描述（原文）**：Barracuda Networks Email Security Gateway (ESG) contains an authentication bypass using an alternate path or channel that could allow an unauthenticated remote attacker to invoke a configuration-import function and restore a crafted, compatible backup archive, resulting in unauthorized modification of the appliance’s global configuration. This vulnerability can be chained with CVE-2026-111560.

### 3. CVE-2026-20320｜Cisco / BroadWorks
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00385 / percentile=0.32917
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-08-19T17:18:40.433 / 2026-11-11T05:19:43.487
- **官方描述（原文）**：Cisco BroadWorks contains an improper restriction of XML external entity reference vulnerability that could allow an unauthenticated, remote attacker to read sensitive configuration information on an affected system.

### 4. CVE-2026-124194｜Microsoft / Office
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:20:48.180)；NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-10T19:20:48.180 / 2026-11-11T05:19:35.990
- **官方描述（原文）**：Microsoft Office Outlook contains a missing user interaction for potentially unsafe action vulnerability that allows an unauthorized attacker to perform spoofing over a network.

### 5. CVE-2026-111560｜Barracuda Networks / Multiple Products
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：0.0106 / percentile=0.6483
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-02T13:17:35.190 / 2026-11-11T05:19:20.373
- **官方描述（原文）**：Barracuda Networks Email Security Gateway (ESG), Load Balancer, Application Delivery Controller (ADC), Message Archiver (BMA), WAF Control Center (WCC), Web Application Firewall (WAF), and Web Security Gateway (WSG) contain an OS command injection vulnerability. This vulnerability could allow an authenticated administrator to inject OS commands that execute with root privileges when the crafted timezone value is subsequently processed. This vulnerability can be chained with CVE-2026-116606

### 6. CVE-2026-111793｜Openwave Messaging Limited / Webtop Media Transcoder
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：0.00274 / percentile=0.19971
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-16T19:17:05.680 / 2026-11-11T05:19:21.073
- **官方描述（原文）**：Openwave Messaging Limited Webtop Media Transcoder contains an incorrect resource transfer between spheres vulnerability that may allow an authenticated user to process and convert unintended document types if bypassing the Webmail experience.

### 7. CVE-2026-123158｜OpenBSD / OpenSSH
- **Delta event**：EPSS_INCREASED (from=0.01014; to=0.16501)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.16501 / percentile=0.97016
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-05T16:17:47.110 / 2026-11-10T13:48:52.110
- **官方描述（原文）**：OpenBSD OpenSSH on Linux contains an unexpected status code or return value vulnerability that could allow for authentication bypass.

### 8. CVE-2026-125757｜mailcow / mailcow: dockerized
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T16:17:23.107)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T16:17:23.107 / 2026-11-10T17:17:31.177
- **官方描述（原文）**：mailcow: dockerized before 2026-11 contains a server-side template injection vulnerability that allows domain administrators to execute commands in the shared rspamd container by storing a malicious domain-wide footer. Attackers can embed a Jinja macro with an os.execute default value, rendered by the rspamd MOO_FOOTER prefilter, to read or inject mail for every tenant and disable filtering.

### 9. CVE-2026-59986｜alanxz / rabbitmq-c
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T17:17:45.043)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T17:17:45.043 / 2026-11-10T17:17:45.043
- **官方描述（原文）**：rabbitmq-c is a C-language AMQP client library for RabbitMQ. Prior to version 0.17.0, the bounds check (*offset = o + len) <= encoded.len overflows when o + len > SIZE_MAX on 32-bit systems. len is a uint32_t read from the AMQP wire as a BYTES/UTF8 field length. The overflow wraps the check to a small value that passes, producing a decoded amqp_bytes_t with a multi-GB .len pointing into a small frame buffer. This results in an out-of-bounds read of up to ~4GB of process memory on 32-bit systems (ARM, MIPS, x86 ILP32, embedded IoT AMQP clients). Enabling information disclosure or denial of service. Not exploitable on 64-bit systems where size_t is 64-bit. This issue has been patched in version 0.17.0.

### 10. CVE-2026-107356｜U.S. Geological Survey / Area Species Management Research Program
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:14.577)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:14.577 / 2026-11-10T22:18:14.577
- **官方描述（原文）**：U.S. Geological Survey Area Species Management Research Program (ARMI) accepts any uploaded file and stores the file under '/uploads/{upload-file}'. A remote, authenticated attacker could upload a crafted PHP file that executes and returns command output from the server when accessed. Fixed on 2026-07-20.

### 11. CVE-2026-96157｜Microsoft / Windows 10 Version 1607
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:22:13.027)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:22:13.027 / 2026-11-11T05:19:56.570
- **官方描述（原文）**：Heap-based buffer overflow in Microsoft Windows Media Foundation allows an unauthorized attacker to execute code over a network.

### 12. CVE-2026-96078｜Microsoft / Windows 10 Version 1607
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:22:06.210)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:22:06.210 / 2026-11-11T05:19:56.380
- **官方描述（原文）**：Heap-based buffer overflow in Microsoft Color Management allows an unauthorized attacker to execute code over a network.

### 13. CVE-2026-96067｜Microsoft / Windows 10 Version 1607
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:22:04.777)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:22:04.777 / 2026-11-11T05:19:56.193
- **官方描述（原文）**：Integer overflow or wraparound in Microsoft Color Management allows an unauthorized attacker to execute code over a network.

### 14. CVE-2026-95962｜Microsoft / Windows 10 Version 1809
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:51.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:51.060 / 2026-11-10T22:21:16.110
- **官方描述（原文）**：Use after free in Windows Virtual Filtering Platform (VFP) allows an unauthorized attacker to execute code over a network.

### 15. CVE-2026-95901｜Microsoft / Windows 10 Version 1607
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:43.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:43.510 / 2026-11-11T05:19:55.997
- **官方描述（原文）**：Double free in Windows Microsoft DirectMusic allows an unauthorized attacker to execute code over a network.

### 16. CVE-2026-95882｜Microsoft / Windows 10 Version 1607
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:41.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:41.527 / 2026-11-11T05:19:55.797
- **官方描述（原文）**：Stack-based buffer overflow in Windows Microsoft DirectMusic allows an unauthorized attacker to execute code over a network.

### 17. CVE-2026-89324｜XTemos / Basel Post Types
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:21:14.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:21:14.003 / 2026-11-10T22:21:14.137
- **官方描述（原文）**：The Basel Post Types plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 1.18. The vulnerability exists because a missing-quotes coding error in the defined() call for SECURE_AUTH_SALT inside BASEL_Auth::get_config() causes PHP to evaluate the constant's value rather than its name, making the check always fail and permanently falling back to the static hardcoded salt 2NlBUibcszrVtNmDnxqDbwCOpLWq91eatIz6O1O that is publicly visible in the theme source code; because this salt is static and known, an attacker can compute a valid Opauth signature entirely offline and submit a forged ?opauth callback to the unauthenticated init hook endpoint processed by register_or_login. This makes it possible for unauthenticated attackers to authenticate as any existing WordPress user, including administrators, by forging a callback tied to a known target account email address — bypassing all password verification, multi-factor authentication, and ownership checks, and receiving a fully authenticated session cookie via wc_set_customer_auth_cookie(). Exploitation requires WooCommerce to be active and at least one Basel social-login provider (Facebook, Google, or VKontakte) to be configured with a valid app_id and app_secret in the theme settings.

### 18. CVE-2026-88243｜Microsoft / Windows Server 2016
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:33.783)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:33.783 / 2026-11-11T05:19:54.337
- **官方描述（原文）**：Out-of-bounds read in Windows DHCP Server allows an unauthorized attacker to execute code over a network.

### 19. CVE-2026-88234｜Microsoft / Windows Server 2016
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:32.247)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:32.247 / 2026-11-11T05:19:54.160
- **官方描述（原文）**：Release of invalid pointer or reference in Windows iSCSI allows an unauthorized attacker to execute code over a network.

### 20. CVE-2026-88218｜Microsoft / Windows 10 Version 1607
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:28.907)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:28.907 / 2026-11-11T05:19:53.953
- **官方描述（原文）**：Double free in Windows DNS allows an unauthorized attacker to execute code over a network.

### 21. CVE-2026-85844｜Microsoft / Windows 10 Version 1607
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:25.653)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:25.653 / 2026-11-11T05:19:53.740
- **官方描述（原文）**：Authentication bypass using an alternate path or channel in Windows Kerberos allows an unauthorized attacker to elevate privileges over a network.

### 22. CVE-2026-82509｜vlang / v
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T14:17:36.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T14:17:36.290 / 2026-11-10T14:17:36.290
- **官方描述（原文）**：V programming language standard library net.http through version 0.5.2 prior to commit 4077484 contains a TLS certificate validation bypass vulnerability that allows on-path attackers to intercept HTTPS traffic by exploiting the default false value of SSLConnectConfig.validate and FetchConfig.validate, which completes TLS handshakes without verifying certificates in both the mbedtls and OpenSSL backends. Attackers can present an expired, self-signed, wrong-hostname, or untrusted-root certificate to successfully complete the handshake via http.get, http.post, or http.fetch, enabling interception or modification of HTTPS traffic unless validate: true is explicitly configured.

### 23. CVE-2026-82391｜zephyrproject / zephyr
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:21:05.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:21:05.710 / 2026-11-10T22:21:05.823
- **官方描述（原文）**：The HTTP/2 front-end of the Zephyr HTTP server aliased connection receive state as a scratch output. In subsys/net/lib/http/http_server_http2.c, handle_http2_static_fs_resource() passed &client->data_len as the file_size out-parameter of http_server_find_file(). client->data_len is the count of unprocessed bytes remaining in the fixed-size per-connection receive buffer client->buffer[CONFIG_HTTP_SERVER_CLIENT_BUFFER_SIZE] (256 bytes by default), an invariant every frame handler and the socket receive path rely on. Serving any static file therefore replaced that bounded value with the file's on-disk size, and nothing resets it afterwards. The defect is reached by an unauthenticated HTTP/2 GET for any file under the web root, in applications that register a static-filesystem resource (HTTP_RESOURCE_TYPE_STATIC_FS) with CONFIG_FILE_SYSTEM=y; CONFIG_HTTP_SERVER_VERSION_2 is enabled by default and no TLS or credentials are required on this path. Once client->data_len exceeds the buffer size, the frame dispatch loop in subsys/net/lib/http/http_server_core.c keeps parsing past the end of the received data, and the peer controls the bytes at client->cursor, so it can choose which fabricated frame the state machine consumes next by appending bytes after its request. The inflated length defeats the only guards on the buffer. parse_http_frame_header() and the per-frame handlers read and skip up to a 24-bit frame length beyond the buffer (out-of-bounds read); the compaction memmove(client->buffer, client->cursor, client->data_len) at the end of request handling copies the file-size number of bytes into the 256-byte buffer, overflowing the rest of struct http_client_ctx — including the current_detail/current_stream pointers, the parser_settings function-pointer table and the inactivity_timer work handler — and the adjacent client contexts in static memory; and the subsequent zsock_recv(client->fd, client->buffer + client->data_len, sizeof(client->buffer) - client->data_len, 0) underflows its size argument, writing attacker-supplied data of attacker-chosen length out of bounds. The impact is remote memory corruption in the server's single address space: at minimum a crash or hang of the device, and plausibly control-data overwrite leading to code execution. The HTTP/1 and HTTP/3 static-filesystem handlers already used a local variable and are unaffected; the fix makes the HTTP/2 handler use a local size_t file_size as well.

### 24. CVE-2026-80095｜Microsoft / Microsoft SharePoint Server Subscription Edition
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:22.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:22.760 / 2026-11-10T19:21:22.877
- **官方描述（原文）**：Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a network.

### 25. CVE-2026-66801｜Microsoft / Microsoft GDK
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:17.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:17.250 / 2026-11-10T22:19:15.130
- **官方描述（原文）**：Heap-based buffer overflow in Xbox allows an unauthorized attacker to execute code over a network.

### 26. CVE-2026-64682｜NauelG / astro-blocks
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T05:19:52.120)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T05:19:52.120 / 2026-11-11T05:19:52.120
- **官方描述（原文）**：AstroBlocks is a block-first CMS for Astro projects. Prior to version 3.4.0, admin session tokens can be forged due to a hard-coded fallback JWT secret and a mismatched environment variable name. An attacker who knows the public fallback value (readable in the published package) can forge a valid session token with role: "owner" and obtain full administrative control of the CMS — creating/deleting content, users, media, redirects, and configuration. This issue has been patched in version 3.4.0.

### 27. CVE-2026-64678｜nitrite / nitrite-java
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T05:19:51.937)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T05:19:51.937 / 2026-11-11T05:19:51.937
- **官方描述（原文）**：NOsql Object (NO2 a.k.a Nitrite) database is an open source nosql embedded document store. Prior to version 4.4.1, when Nitrite opens a database file, MVStoreUtils.openOrCreate() automatically checks for a legacy v1-format store and, on detecting one (or hitting a compatibility error while opening), triggers an automatic migration path. This path deserializes stored values using NitriteDataType.deserialize(byte[]), which passes the raw bytes directly to java.io.ObjectInputStream.readObject() via a custom NitriteObjectInputStream subclass. That subclass overrides only readClassDescriptor() — solely to remap a handful of known legacy class names to their current equivalents — and implements no class allowlist, blocklist, or ObjectInputFilter (JEP 290). Any Serializable class reachable on the embedding application's classpath can therefore be instantiated via readObject(), with readObject()/readExternal()/readResolve() callbacks invoked unconditionally. If a suitable gadget class (e.g. from commons-collections or similar) happens to be present on the classpath, this is a precondition for remote code execution. This issue has been patched in version 4.4.1.

### 28. CVE-2026-64670｜walinejs / waline
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T05:19:51.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T05:19:51.527 / 2026-11-11T05:19:51.527
- **官方描述（原文）**：Waline is a comment system with backend support. In versions 3.15.2 and prior, @waline/client renders the comment editor's live preview with marked and no sanitizer (utils/markdown.ts), and the preview is injected with v-html. When a comment is edited, the editor is seeded with the comment's raw, un-sanitized body (orig). Only administrators and the comment owner can edit. So an administrator who clicks Edit on an attacker's comment renders that attacker's raw HTML in their own session: an unauthenticated commenter achieves privilege-escalation stored XSS against a moderator with a single Edit click. At time of publication, there are no publicly available patches.

### 29. CVE-2026-63011｜Intermesh / groupoffice
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T17:17:45.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T17:17:45.980 / 2026-11-10T21:19:32.157
- **官方描述（原文）**：Group-Office is an enterprise customer relationship management and groupware tool. Prior to versions 6.8.167, 25.0.102, and 26.0.27, the Contact/labels JMAP endpoint in GroupOffice accepts a fully attacker-controlled template string (tpl parameter) that is passed without restriction to TemplateParser::parse(). When the template contains an [assign] block whose expression includes a {{...}} variable reference, the engine calls eval() on the expanded expression after running it through a validateExpression() guard. The guard double-quotes unrecognized tokens, but PHP 7+ allows a string enclosed in parentheses to be invoked as a function ("system")("id") is valid PHP and calls system("id"). A single authenticated HTTP request is sufficient to execute arbitrary OS commands as the web server user (www-data). This issue has been patched in versions 6.8.167, 25.0.102, and 26.0.27.

### 30. CVE-2026-61887｜未確認 / Intel(R) TDX Migration Trust Domain (MigTD)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T18:17:44.703)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T18:17:44.703 / 2026-11-10T18:17:44.703
- **官方描述（原文）**：Missing critical step in authentication in the MigTD SPDM rebind implementation for the Intel(R) TDX Migration Trust Domain (MigTD) within Ring 0: Hypervisor may allow an escalation of privilege and information disclosure. Network adversary with an unauthenticated user combined with a low complexity attack may enable remote code execution. This result may potentially occur via adjacent access when attack requirements are not present without special internal knowledge and requires no user interaction. The potential vulnerability may impact the confidentiality (high), integrity (high) and availability (high) of the vulnerable system, resulting in subsequent system confidentiality (high), integrity (high) and availability (high) impacts.

### 31. CVE-2026-61547｜alanxz / rabbitmq-c
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T17:17:45.650)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T17:17:45.650 / 2026-11-10T17:17:45.650
- **官方描述（原文）**：rabbitmq-c is a C-language AMQP client library for RabbitMQ. Prior to version 0.17.0, a heap buffer overflow exists in rabbitmq-c when the public amqp_send_frame() API is used to serialize an oversized AMQP_FRAME_BODY. The issue occurs because amqp_frame_to_bytes() copies frame.payload.body_fragment.len bytes into the connection outbound buffer without validating that the body fragment fits within the allocated frame buffer. An application that passes an oversized body frame to amqp_send_frame() can trigger a heap out-of-bounds write, resulting in process crash and memory corruption. This issue has been patched in version 0.17.0.

### 32. CVE-2026-61473｜未確認 / Intel(R) TDX Migration Trust Domain (MigTD)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T18:17:44.563)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T18:17:44.563 / 2026-11-10T18:17:44.563
- **官方描述（原文）**：Authentication bypass by capture-replay in the MigTD for the Intel(R) TDX Migration Trust Domain (MigTD) within Ring 0: Hypervisor may allow an escalation of privilege. System software adversary with a privileged user combined with a low complexity attack may enable escalation of privilege. This result may potentially occur via local access when attack requirements are not present without special internal knowledge and requires no user interaction. The potential vulnerability may impact the confidentiality (high), integrity (high) and availability (none) of the vulnerable system, resulting in subsequent system confidentiality (high), integrity (high) and availability (none) impacts.

### 33. CVE-2026-44685｜未確認 / Intel(R) TDX Migration Trust Domain (MigTD)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T18:17:40.273)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T18:17:40.273 / 2026-11-10T22:06:57.400
- **官方描述（原文）**：Authentication bypass by spoofing in the MigTD rebinding protocol for the Intel(R) TDX Migration Trust Domain (MigTD) within Ring 0: Hypervisor may allow an escalation of privilege. System software adversary with a privileged user combined with a low complexity attack may enable local code execution. This result may potentially occur via local access when attack requirements are not present without special internal knowledge and requires no user interaction. The potential vulnerability may impact the confidentiality (high), integrity (high) and availability (high) of the vulnerable system, resulting in subsequent system confidentiality (high), integrity (high) and availability (high) impacts.

### 34. CVE-2026-126542｜WWBN / AVideo
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T01:17:15.547)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T01:17:15.547 / 2026-11-11T01:17:15.680
- **官方描述（原文）**：WWBN AVideo 6.5 through 29.7.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to log in as any user via Hybridauth social login display names. Attackers can set their X, Facebook, Yahoo or LinkedIn display name to a victim's username and withhold email, causing login.json.php or oauth2.php to log them in as that account, including administrators, without a password.

### 35. CVE-2026-126539｜directus / directus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-11T01:17:15.173)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-11T01:17:15.173 / 2026-11-11T01:17:15.173
- **官方描述（原文）**：Directus before 12.1.0 contains an authorization bypass vulnerability that allows unauthenticated attackers to skip permission checks by sending a failed auth message on public-mode WebSocket connections. Attackers can send an invalid token so handleAuthRequest sets accountability to null, then read, create, update or delete records in any user-defined collection.

### 36. CVE-2026-126261｜Fortinet / FortiManager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T23:17:20.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T23:17:20.897 / 2026-11-10T23:17:20.897
- **官方描述（原文）**：A improper authorization vulnerability in Fortinet FortiManager 8.0.0, FortiManager 7.6.0 through 7.6.7, FortiManager 7.4.0 through 7.4.5, FortiManager 7.2.0 through 7.2.8 may allow an unauthenticated attacker that can reach the FGFM port to execute code or commands via crafted FGFM packets.

### 37. CVE-2026-126187｜react / react
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T23:17:20.687)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T23:17:20.687 / 2026-11-10T23:17:20.687
- **官方描述（原文）**：React is a JavaScript library for building user interfaces. From 19.0.0 until 19.0.9, 19.1.10, 19.2.9, and 19.3.1, the react-server-dom-webpack, react-server-dom-parcel, and react-server-dom-turbopack packages are vulnerable to unauthenticated remote code execution through crafted payloads targeting frameworks that support React Server Components. The vulnerability only affects extremely rare cases where responses transport multiple typed arrays and an attacker-controlled value. Applications whose React code does not use a server are not affected. Applications that do not use a framework, bundler, or bundler plugin that supports React Server Components are not affected. This issue is fixed in versions 19.0.9, 19.1.10, 19.2.9, and 19.3.1.

### 38. CVE-2026-126087｜AWS / openjd-sessions
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:13.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:13.740 / 2026-11-10T19:21:13.740
- **官方描述（原文）**：Untrusted search path in the cross-user process launcher in Open Job Description (OpenJD) Sessions for Python before 0.11.0, as used in the AWS Deadline Cloud worker agent before 0.33.0, on Linux might allow an authenticated remote user with permission to submit jobs to a queue to execute arbitrary code as the worker agent OS user and obtain the AWS credentials held by the worker agent via a crafted job that modifies the PATH environment variable. To remediate this issue, users of customer-managed fleets should upgrade the Deadline Cloud worker agent to version 0.33.0 or later, which includes OpenJD Sessions 0.11.0. Service-managed fleets were remediated service-side.

### 39. CVE-2026-126082｜rails / rails
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T21:19:26.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T21:19:26.980 / 2026-11-10T21:19:26.980
- **官方描述（原文）**：Active Storage makes it simple to upload and reference files in cloud services and attach those files to Active Record objects. Prior to 8.1.4.1 and 8.0.5.2, a Rails application that processes attachments with ImageMagick may allow an unauthenticated attacker to write arbitrary files on the server and, when attachments are stored with the Disk service, to read arbitrary files readable by the application process. Those files typically include secret_key_base and credentials for external systems, which may in turn allow escalation to remote code execution or lateral movement to those systems. ImageMagick selects a coder from the content of the file it is given, and some coders act on files named inside the image rather than on the image itself. Active Storage constrained none of ImageMagick's coders, and the ImageMagick analyzer runs when a file is attached, so an attacker who can upload a crafted file may be able to invoke one. Attaching the upload is sufficient; no variant, preview, or analyze call is required. One specific attack chain has been reported, but other attack chains may exist. An application is affected when it uses ImageMagick for Active Storage image processing through config.active_storage.variant_processor = :mini_magick, runs ImageMagick under a security policy that does not already deny the involved coders, and allows uploads from untrusted users. This issue is fixed in versions 8.1.4.1 and 8.0.5.2.

### 40. CVE-2026-126065｜openobserve / openobserve
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T21:19:24.310)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T21:19:24.310 / 2026-11-10T21:19:24.447
- **官方描述（原文）**：OpenObserve is a cloud-native observability platform. Prior to 1.1.0, the shared authentication validator in src/api/common/src/auth/validator.rs accepts an empty or whitespace-only HTTP Basic password for an account whose password_ext value is missing or empty. SSO-provisioned and migration-created users can have this state, allowing an unauthenticated attacker who knows an affected user's email address and organization to authenticate on protected non-ingestion API routes with the victim's role and permissions. A compromised privileged account can expose or modify telemetry, alerts, streams, users, and security configuration. An account with search permission can submit a DataFusion COPY ... TO statement through the search API to create or overwrite attacker-controlled files at service-process-writable locations, creating a conditional escalation to pre-authentication remote code execution. This issue is fixed in version 1.1.0.

### 41. CVE-2026-125883｜N-able / N-central
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:31.143)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:31.143 / 2026-11-10T22:18:31.143
- **官方描述（原文）**：Improper restriction of XML external entity reference vulnerability in N-able N-central allows XML Schema Poisoning. This issue affects N-central: before 26.4.1.

### 42. CVE-2026-125881｜N-able / N-central
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:30.860)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:30.860 / 2026-11-10T22:18:30.860
- **官方描述（原文）**：Server-Side request forgery (SSRF) vulnerability in N-able N-central allows Server Side Request Forgery. This issue affects N-central: before 26.4.1.

### 43. CVE-2026-125758｜aptabase / aptabase
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T16:17:23.267)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T16:17:23.267 / 2026-11-10T16:17:23.267
- **官方描述（原文）**：Aptabase before commit 61d4c01 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge sign-in links by using the publicly known example AUTH_SECRET. Attackers can enumerate registered e-mails via /api/_auth/signin, forge HS256 JWTs redeemed by /api/_auth/continue, impersonate users, export analytics data, and transfer app ownership.

### 44. CVE-2026-125347｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T18:17:34.843)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T18:17:34.843 / 2026-11-11T05:19:37.613
- **官方描述（原文）**：Incorrect authorization in FileSystem in Google Chrome prior to 157.0.8103.50 allowed a remote attacker leveraging social engineering to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 45. CVE-2026-125331｜HarnessRouter / harnessrouter
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:10.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:10.630 / 2026-11-10T19:21:10.630
- **官方描述（原文）**：HarnessRouter is a self-hosted unified API for running agent harnesses with sessions, streaming, files, cancellation, and failure handling. Prior to 0.31.8, a console that is not in self-hosted mode attaches the server's internal key to requests carrying an Authorization header before validating the bearer, while the service-only PUT and GET /v1/orgs/{org}/connections/{name}, PUT /v1/orgs/{org}/policy/{backend}, and /internal/* routes trust that key and take the organization from the URL. In a multi-organization deployment, a remote caller can use a made-up bearer to rewrite another organization's provider connection to an attacker-controlled endpoint, causing later prompts to be disclosed and attacker-controlled responses to influence tasks. This issue is fixed in version 0.31.8.

### 46. CVE-2026-125298｜AsiaInfo International / Business Support System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:30.240)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:30.240 / 2026-11-10T22:18:30.240
- **官方描述（原文）**：AsiaInfo Business Support System (BSS) 9.2.0 through 9.2.40 does not correctly verify cryptographic signatures for JSON Web Tokens (JWT). A remote, unauthenticated attacker could forge a well-formed JWT without a valid signature and use it to execute privileged actions. Fixed in 9.2.41.

### 47. CVE-2026-125297｜AsiaInfo International / Business Support System
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:30.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:30.080 / 2026-11-10T22:18:30.080
- **官方描述（原文）**：AsiaInfo Business Support System (BSS) 9.2.0 through 9.2.40 accepts unauthenticated requests via the management API '/bss/sysmgnt/api/'. A remote, unauthenticated attacker could provision a new account with administrative privileges or take over existing accounts, and perform other administrative actions. Fixed in 9.2.41.

### 48. CVE-2026-124917｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T14:17:25.483)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T14:17:25.483 / 2026-11-10T21:19:18.507
- **官方描述（原文）**：Sandbox escape due to use-after-free in the Widget: Gtk component. This vulnerability was fixed in Firefox 160, Firefox ESR 153.7, Thunderbird 160, and Thunderbird 153.7.

### 49. CVE-2026-124903｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T14:17:23.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T14:17:23.990 / 2026-11-10T21:19:16.820
- **官方描述（原文）**：Sandbox escape due to use-after-free in the IPC component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, Firefox ESR 153.7, Thunderbird 160, and Thunderbird 153.7.

### 50. CVE-2026-124900｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T14:17:23.663)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T14:17:23.663 / 2026-11-10T19:20:59.537
- **官方描述（原文）**：Sandbox escape due to use-after-free in the DOM: Service Workers component. This vulnerability was fixed in Firefox 160 and Thunderbird 160.

### 51. CVE-2026-124864｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T14:17:18.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T14:17:18.810 / 2026-11-10T21:19:10.790
- **官方描述（原文）**：Sandbox escape due to use-after-free in the DOM: Service Workers component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, Firefox ESR 153.7, Thunderbird 160, and Thunderbird 153.7.

### 52. CVE-2026-124861｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T14:17:18.447)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T14:17:18.447 / 2026-11-10T21:19:10.263
- **官方描述（原文）**：Sandbox escape due to use-after-free in the Audio/Video: cubeb component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, Firefox ESR 153.7, Thunderbird 160, and Thunderbird 153.7.

### 53. CVE-2026-124859｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T14:17:18.210)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T14:17:18.210 / 2026-11-10T21:19:09.913
- **官方描述（原文）**：Sandbox escape due to incorrect boundary conditions in the Storage: Cache API component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, Firefox ESR 153.7, Thunderbird 160, and Thunderbird 153.7.

### 54. CVE-2026-124853｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T14:17:17.007)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T14:17:17.007 / 2026-11-10T21:19:08.977
- **官方描述（原文）**：Sandbox escape due to incorrect boundary conditions in the Graphics: Text component. This vulnerability was fixed in Firefox 160, Firefox ESR 115.45, Firefox ESR 153.7, Thunderbird 160, and Thunderbird 153.7.

### 55. CVE-2026-121908｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:27.533)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:27.533 / 2026-11-11T05:19:32.047
- **官方描述（原文）**：Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 56. CVE-2026-121906｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:27.400)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:27.400 / 2026-11-11T05:19:31.917
- **官方描述（原文）**：Adobe Connect is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability that could lead to arbitrary file system read. An attacker could exploit this vulnerability to access sensitive files and directories outside the intended access scope. Exploitation of this issue does not require user interaction. Scope is changed.

### 57. CVE-2026-121904｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:27.280)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:27.280 / 2026-11-10T22:18:27.280
- **官方描述（原文）**：Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low-privileged attacker to inject malicious scripts into vulnerable form fields. Malicious JavaScript may be executed in a victim's browser when they browse to the page containing the vulnerable field, potentially gaining elevated access or control over the victim's account or session. Scope is changed.

### 58. CVE-2026-121902｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:27.143)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:27.143 / 2026-11-11T05:19:31.767
- **官方描述（原文）**：Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution. An attacker could exploit this vulnerability to execute arbitrary SQL commands, potentially compromising the confidentiality, integrity, and availability of the application. Exploitation of this issue does not require user interaction.

### 59. CVE-2026-121898｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:26.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:26.897 / 2026-11-11T05:19:31.460
- **官方描述（原文）**：Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 60. CVE-2026-121896｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:26.773)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:26.773 / 2026-11-11T05:19:31.323
- **官方描述（原文）**：Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 61. CVE-2026-121894｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:26.650)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:26.650 / 2026-11-11T05:19:31.170
- **官方描述（原文）**：Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary SQL commands, potentially gaining elevated access or control over the victim's account or session. Exploitation of this issue does not require user interaction. Scope is changed.

### 62. CVE-2026-121892｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:26.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:26.520 / 2026-11-11T05:19:31.020
- **官方描述（原文）**：Adobe Connect is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 63. CVE-2026-121889｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:26.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:26.180 / 2026-11-11T05:19:30.863
- **官方描述（原文）**：Adobe Connect is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation. Exploitation of this issue does not require user interaction. Scope is changed.

### 64. CVE-2026-121887｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:26.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:26.060 / 2026-11-11T05:19:30.710
- **官方描述（原文）**：Adobe Connect is affected by an Improper Restriction of XML External Entity Reference ('XXE') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 65. CVE-2026-121683｜Ivanti / Cloud Services Application
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T16:17:17.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T16:17:17.900 / 2026-11-10T16:17:17.900
- **官方描述（原文）**：Missing authentication in Ivanti Cloud Services Application version 5.0.8 allows a remote unauthenticated attacker to add and delete arbitrary trusted EPM Core certificate entries.

### 66. CVE-2026-121653｜ivanti / Endpoint Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T16:17:17.580)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T16:17:17.580 / 2026-11-11T05:19:30.540
- **官方描述（原文）**：SQL injection in the Core of Ivanti Endpoint Manager before version 2024 SU8 allows a remote unauthenticated attacker to achieve remote code execution.

### 67. CVE-2026-121529｜Fortinet / FortiClientMac
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T20:18:56.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T20:18:56.790 / 2026-11-10T21:19:03.030
- **官方描述（原文）**：A origin validation error vulnerability in Fortinet FortiClientMac 7.4.0 through 7.4.7, FortiClientWindows 7.4.0 through 7.4.7, FortiClientWindows 7.2.0 through 7.2.14, FortiClientWindowsPAM 7.4.7, FortiClientWindowsPAM 7.2.14 may allow an unauthorized remote attacker to execute unauthorized code or commands. Successful exploitation requires interaction with the victim.

### 68. CVE-2026-121370｜Arista Networks / EOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T20:18:56.507)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T20:18:56.507 / 2026-11-10T22:18:25.777
- **官方描述（原文）**：On affected platforms running Arista EOS with Precision Time Protocol (PTP) configured, an unauthenticated attacker with network access to a PTP-enabled port can create a denial of service (DoS) condition by sending traffic to the system.

### 69. CVE-2026-121356｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:25.637)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:25.637 / 2026-11-11T05:19:30.253
- **官方描述（原文）**：Adobe Connect is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalation. Exploitation of this issue does not require user interaction. Scope is changed.

### 70. CVE-2026-121355｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:25.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:25.510 / 2026-11-10T22:18:25.510
- **官方描述（原文）**：Adobe Connect is affected by an Incorrect Authorization vulnerability that could result in privilege escalation. An attacker could exploit this vulnerability to gain elevated access to sensitive information or functionality. Exploitation of this issue does not require user interaction.

### 71. CVE-2026-121354｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:25.373)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:25.373 / 2026-11-11T05:19:30.097
- **官方描述（原文）**：Adobe Connect is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability that could lead to arbitrary file system read. An attacker could exploit this vulnerability to access sensitive files and directories outside the intended access scope. Exploitation of this issue does not require user interaction. Scope is changed.

### 72. CVE-2026-121353｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:25.217)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:25.217 / 2026-11-11T05:19:29.943
- **官方描述（原文）**：Adobe Connect is affected by an Improper Neutralization of CRLF Sequences ('CRLF Injection') vulnerability that could result in arbitrary code execution in the context of the current user, potentially gaining elevated access or control over the victim's account or session. Exploitation of this issue does not require user interaction. Scope is changed.

### 73. CVE-2026-121352｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:25.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:25.060 / 2026-11-11T05:19:29.783
- **官方描述（原文）**：Adobe Connect is affected by an Incorrect Authorization vulnerability that could result in privilege escalation. An attacker could exploit this vulnerability to gain unauthorized access to sensitive resources. Exploitation of this issue does not require user interaction. Scope is changed.

### 74. CVE-2026-121351｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:24.910)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:24.910 / 2026-11-11T05:19:29.630
- **官方描述（原文）**：Adobe Connect is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability that could lead to arbitrary file system read. An attacker could exploit this vulnerability to access sensitive files and directories outside the intended access scope. Exploitation of this issue does not require user interaction. Scope is changed.

### 75. CVE-2026-121349｜Adobe / Adobe Connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:24.643)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:24.643 / 2026-11-11T05:19:29.477
- **官方描述（原文）**：Adobe Connect is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to gain elevated access or control over the victim's account or session. Exploitation of this issue does not require user interaction. Scope is changed.

### 76. CVE-2026-121295｜Arista Networks / EOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T20:18:55.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T20:18:55.750 / 2026-11-10T20:18:55.750
- **官方描述（原文）**：On affected platforms running Arista EOS configured as S-BFD peers, an unauthenticated attacker could send a crafted S-BFD PDU to an initiator device. This crafted PDU could cause the kernel on the initiator device to crash, resulting in an unexpected device reboot.

### 77. CVE-2026-121289｜Arista Networks / EOS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T20:18:54.283)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T20:18:54.283 / 2026-11-10T20:18:54.283
- **官方描述（原文）**：On affected platforms running Arista EOS with BGP configured, a specially crafted packet can cause the BGP agent to crash. Successful exploitation causes the BGP agent process to terminate, resulting in the loss of all BGP sessions on the affected device and possible disruption to network routing until the process recovers. Due to the nature of the vulnerability, it may also be possible for a sophisticated attacker to achieve arbitrary code execution, which could compromise the confidentiality and integrity of the affected system.

### 78. CVE-2026-120808｜MongoDB / MongoDB Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T20:18:51.180)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T20:18:51.180 / 2026-11-10T22:08:59.707
- **官方描述（原文）**：An issue exists in MongoDB's macOS TLS client implementation where certificate chain-of-trust validation is bypassed for outbound connections to IPv6-addressed peers. When a MongoDB process using the Apple SecureTransport TLS backend connects to an IPv6 target, the trust evaluation result from SecTrustEvaluate is silently discarded, regardless of whether the peer's certificate is trusted. An on-path party could exploit this by presenting a self-signed certificate containing the target's IPv6 address in the Subject Alternative Name to intercept and modify encrypted inter-node or external service traffic. This issue only affects MongoDB processes running on macOS with the Apple SecureTransport TLS provider.

### 79. CVE-2026-120779｜Microsoft / Visual Studio Code
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:20:27.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:20:27.040 / 2026-11-10T19:20:27.167
- **官方描述（原文）**：Improper control of generation of code ('code injection') in Visual Studio Code allows an unauthorized attacker to execute code over a network.

### 80. CVE-2026-120002｜Microsoft / Microsoft SharePoint Server Subscription Edition
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:20:26.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:20:26.080 / 2026-11-10T19:20:26.207
- **官方描述（原文）**：Incorrect authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a network.

### 81. CVE-2026-119990｜Microsoft / Azure Open AI
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:20:24.280)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:20:24.280 / 2026-11-11T05:19:28.737
- **官方描述（原文）**：Missing authentication for critical function in Azure OpenAI allows an unauthorized attacker to elevate privileges over a network.

### 82. CVE-2026-119958｜Microsoft / Windows 10 Version 1607
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:20:19.857)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:20:19.857 / 2026-11-11T05:19:28.517
- **官方描述（原文）**：Out-of-bounds write in Windows LDAP - Lightweight Directory Access Protocol allows an unauthorized attacker to execute code over a network.

### 83. CVE-2026-119446｜nerves-hub / nerves_hub_web
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T11:16:40.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T11:16:40.290 / 2026-11-10T17:17:23.017
- **官方描述（原文）**：Session Fixation vulnerability in the CLI login flow in nerves-hub nerves_hub_web allows an unauthenticated attacker to obtain an API token for another user's account via a crafted login link. Starting a CLI login with POST /api/auth/cli_session needs no authentication and returns a polling token, a confirmation URL that carries that token, and a confirmation code. When a signed-in user opens that URL and clicks Confirm, NervesHub.Accounts.verify_cli_session_token/2 creates an API token for the user's account and stores it on the login, and the next poll of GET /api/auth/cli_session/<token> returns it to whoever started the login. The confirmation code is only displayed and is never compared with anything, so it cannot show that the person confirming is the one who started the login. The confirm form carries a CSRF token and the page cannot be framed, so the attacker has to persuade the user to open the link and click the button themselves. This issue affects nerves_hub: from 2.5.0 before 2.5.3.

### 84. CVE-2026-119017｜Adobe / Adobe Experience Manager 6.5
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:24.520)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:24.520 / 2026-11-11T05:19:28.120
- **官方描述（原文）**：Adobe Experience Manager is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 85. CVE-2026-118740｜Microsoft / Aspire Dashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:19:50.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:19:50.740 / 2026-11-10T20:18:25.297
- **官方描述（原文）**：Missing authorization in Aspire allows an unauthorized attacker to bypass a security feature over a network.

### 86. CVE-2026-118383｜MongoDB / MongoDB Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T21:18:58.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T21:18:58.980 / 2026-11-10T22:08:59.707
- **官方描述（原文）**：A use-after-free in the replication component of MongoDB Server can occur when a newly elected replica set primary completes catch-up. The condition can be caused by requests that do not require authentication, and may result in the server terminating unexpectedly or, under certain conditions, arbitrary code execution in the context of the server process. Replica set members are affected, including the shard and config server replica set members of sharded clusters; standalone mongod instances are not.

### 87. CVE-2026-116945｜Microsoft / Microsoft SQL Server 2017 (GDR)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:19:27.737)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:19:27.737 / 2026-11-11T05:19:26.887
- **官方描述（原文）**：Heap-based buffer overflow in SQL Server allows an unauthorized attacker to execute code over a network.

### 88. CVE-2026-116928｜Microsoft / Windows 10 Version 1607
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:19:21.287)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:19:21.287 / 2026-11-11T05:19:26.693
- **官方描述（原文）**：Out-of-bounds write in Microsoft Windows Search Component allows an unauthorized attacker to execute code over a network.

### 89. CVE-2026-114371｜Adobe / Adobe Experience Manager as a Cloud Service
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:22.617)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:22.617 / 2026-11-11T05:19:25.677
- **官方描述（原文）**：Adobe Experience Manager is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 90. CVE-2026-114162｜Microsoft / Azure Privileged Identity Management (PIM)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:19:09.807)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:19:09.807 / 2026-11-10T20:18:02.503
- **官方描述（原文）**：Incorrect authorization in Microsoft Graph allows an authorized attacker to elevate privileges over a network.

### 91. CVE-2026-114160｜Microsoft / Azure Managed Grafana
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:19:09.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:19:09.527 / 2026-11-11T02:17:08.860
- **官方描述（原文）**：Server-side request forgery (ssrf) in Azure Managed Grafana allows an unauthorized attacker to elevate privileges over a network.

### 92. CVE-2026-114146｜Microsoft / .NET 10.0 installed on Linux
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:19:07.683)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:19:07.683 / 2026-11-10T20:18:00.820
- **官方描述（原文）**：Incorrect authorization in ASP.NET Core allows an authorized attacker to elevate privileges over a network.

### 93. CVE-2026-113580｜Adobe / Adobe Experience Manager as a Cloud Service
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:22.493)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:22.493 / 2026-11-11T05:19:25.530
- **官方描述（原文）**：Adobe Experience Manager is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 94. CVE-2026-113579｜Adobe / Adobe Experience Manager as a Cloud Service
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:18:22.360)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:18:22.360 / 2026-11-11T05:19:25.387
- **官方描述（原文）**：Adobe Experience Manager is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could result in arbitrary code execution in the context of the current user. A low-privileged attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

### 95. CVE-2026-112967｜Microsoft / Windows 10 Version 1809
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:18:46.937)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:18:46.937 / 2026-11-11T05:19:21.273
- **官方描述（原文）**：Heap-based buffer overflow in Windows Xbox Live Networking Service allows an unauthorized attacker to execute code over a network.

### 96. CVE-2026-112136｜Siemens / Mendix Studio Pro 11
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T12:17:16.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T12:17:16.540 / 2026-11-10T17:17:20.530
- **官方描述（原文）**：A vulnerability has been identified in Mendix Studio Pro 11 (All versions >= V11.15.0 < V11.16.0), Mendix Studio Pro 11.12 (All versions >= V11.12.6 < V11.12.7). The affected products MCP Server does not properly restrict its HTTP listener to the loopback interface, leaving it potentially exposed to remote systems. This could allow an attacker with network access to interact with the MCP Server remotely.

### 97. CVE-2026-109467｜Microsoft / Azure DevOps
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:18:15.890)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:18:15.890 / 2026-11-10T22:18:15.530
- **官方描述（原文）**：Improper authentication in Azure DevOps allows an authorized attacker to execute code over a network.

### 98. CVE-2026-109454｜Microsoft / Microsoft SharePoint Server Subscription Edition
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:18:14.347)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:18:14.347 / 2026-11-10T21:18:04.087
- **官方描述（原文）**：Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allows an authorized attacker to perform spoofing over a network.

### 99. CVE-2026-108186｜Zoom Communications / Zoom Workplace
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T16:17:14.183)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T16:17:14.183 / 2026-11-11T05:19:16.987
- **官方描述（原文）**：Improper Input Validation in Zoom Workplace for Windows may allow an unauthenticated user to conduct an escalation of privilege via network access.

### 100. CVE-2026-102166｜Arista Networks / Wi-Fi Access Point
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T20:17:21.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T20:17:21.237 / 2026-11-10T20:17:21.237
- **官方描述（原文）**：Arista C-260 and C-250 access points ship with fleet-wide static cryptographic keys used for firmware image verification and SSLP authentication. An attacker who is able to access these keys would be able to create modified firmware that will pass verification checks. This vulnerability is specific to the C-260 and C-250 models; other access point models enforce digitally signed upgrade images with secure boot and are not affected by this issue.

### 101. CVE-2026-67177｜Chargemap / Chargemap
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:19:18.140)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:19:18.140 / 2026-11-10T22:19:18.140
- **官方描述（原文）**：Chargemap contains a stored cross site scripting vulnerability. A remote, unauthenticated attacker could craft a payload in the username field of the account registration page and associate the new account with a victim's email. The attacker could send a forgotten password request to the victim, and the payload would execute when a victim opens the link. Fixed 2026-07-17.

### 102. CVE-2026-67176｜Chargemap / Chargemap
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:19:17.910)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:19:17.910 / 2026-11-10T22:19:17.910
- **官方描述（原文）**：Chargemap contains an open redirect vulnerability in the authentication login endpoint. A remote, unauthenticated attacker could send a crafted URL to a victim and redirect them to an attacker controlled domain. Fixed 2026-07-17.

### 103. CVE-2026-67175｜Chargemap / Chargemap
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T22:19:17.603)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T22:19:17.603 / 2026-11-10T22:19:17.603
- **官方描述（原文）**：Chargemap contains a stored cross-site scripting vulnerability that allows a remote, authenticated attacker to craft a malicious payload in the user profile page that executes when another user views the attacker's profile. Fixed 2026-07-17.

### 104. CVE-2026-125333｜digitalbazaar / forge
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T19:21:10.943)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T19:21:10.943 / 2026-11-10T21:46:40.673
- **官方描述（原文）**：Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. From 0.1.2 until 1.4.3, forge.http uses _trimString() in lib/http.js to remove trailing whitespace from response header values and cookie names and values with a regular expression that can take quadratic time. A malicious server or on-path attacker can supply a long whitespace run followed by a non-whitespace character in a response header, causing response.readHeader() or response.getCookies() to repeatedly scan the input and block the Node.js event loop or browser tab for minutes. Applications are affected only when they use forge.http with a socket pool to communicate with an untrusted server; forge.http is not loaded by require('node-forge'), and the issue has no confidentiality or integrity impact. This issue is fixed in version 1.4.3.

### 105. CVE-2026-124016｜postalsys / postal-mime
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T20:19:04.337)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T20:19:04.337 / 2026-11-10T21:19:06.983
- **官方描述（原文）**：postal-mime before 4.2.1 contains an algorithmic complexity denial of service vulnerability that allows unauthenticated remote attackers to cause excessive CPU consumption in the PostalMime.processLine() function by crafting deeply nested multipart email messages with boundary lines sharing long prefixes with open boundaries. Attackers can deliver a malicious email with nesting up to the default maxNestingDepth of 256, causing per-line parsing cost to scale as O(depth x shared prefix length) and blocking the Node.js event loop for seconds per message.

### 106. CVE-2026-125749｜vas3k / TaxHacker
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T16:17:20.893)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T16:17:20.893 / 2026-11-10T17:17:30.910
- **官方描述（原文）**：TaxHacker through 0.8.5 contains an insecure direct object reference vulnerability in app/(app)/settings/actions.ts that allows authenticated users to modify other users' data by supplying an arbitrary userId. Attackers can invoke Server Actions like deleteCategoryAction or editFieldAction with a victim's UUID to delete categories, clear transaction assignments, or alter LLM prompts.

### 107. CVE-2026-124503｜sooperset / mcp-atlassian
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-10T10:16:43.760)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00538 / percentile=0.4562
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-10T10:16:43.760 / 2026-11-10T17:17:25.227
- **官方描述（原文）**：A vulnerability was identified in sooperset mcp-atlassian up to 0.24.0. This issue affects the function validate_safe_path of the file src/mcp_atlassian/utils/io.py. The manipulation of the argument path leads to path traversal. The attack may be initiated remotely. The exploit is publicly available and might be used. Upgrading to version 0.24.1 is capable of addressing this issue. Upgrading the affected component is recommended. This CVE was requested by the vendor.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-125350｜Google / Chromium
- **Title**：Google Chromium Use-After-Free Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium contains a use-after-free vulnerability in the XML component that could allow a remote attacker to execute arbitrary code inside the sandbox via a specially crafted webpage. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-116606｜Barracuda Networks / Barracuda Email Security Gateway (ESG)
- **Title**：Barracuda Networks Email Security Gateway (ESG) Authentication Bypass Using an Alternate Path or Channel Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.01602 / percentile=0.76026
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Barracuda Networks Email Security Gateway (ESG) contains an authentication bypass using an alternate path or channel that could allow an unauthenticated remote attacker to invoke a configuration-import function and restore a crafted, compatible backup archive, resulting in unauthorized modification of the appliance’s global configuration. This vulnerability can be chained with CVE-2026-111560.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-20320｜Cisco / BroadWorks
- **Title**：Cisco BroadWorks Improper Restriction of XML External Entity Reference Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00385 / percentile=0.32917
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco BroadWorks contains an improper restriction of XML external entity reference vulnerability that could allow an unauthenticated, remote attacker to read sensitive configuration information on an affected system.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-124194｜Microsoft / Office
- **Title**：Microsoft Office Outlook Missing User Interaction for Potentially Unsafe Action Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft Office Outlook contains a missing user interaction for potentially unsafe action vulnerability that allows an unauthorized attacker to perform spoofing over a network.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-111560｜Barracuda Networks / Multiple Products
- **Title**：Barracuda Networks Multiple Products OS Command Injection Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：0.0106 / percentile=0.6483
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Barracuda Networks Email Security Gateway (ESG), Load Balancer, Application Delivery Controller (ADC), Message Archiver (BMA), WAF Control Center (WCC), Web Application Firewall (WAF), and Web Security Gateway (WSG) contain an OS command injection vulnerability. This vulnerability could allow an authenticated administrator to inject OS commands that execute with root privileges when the crafted timezone value is subsequently processed. This vulnerability can be chained with CVE-2026-116606
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-111793｜Openwave Messaging Limited / Webtop Media Transcoder
- **Title**：Openwave Messaging Limited Webtop Media Transcoder Incorrect Resource Transfer Between Spheres Vulnerability
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：0.00274 / percentile=0.19971
- **CISA KEV**：listed=true / date_added=2026-11-10 / due_date=2026-11-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Openwave Messaging Limited Webtop Media Transcoder contains an incorrect resource transfer between spheres vulnerability that may allow an authenticated user to process and convert unintended document types if bypassing the Webmail experience.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-123158｜OpenBSD / OpenSSH
- **Title**：OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.16501 / percentile=0.97016
- **CISA KEV**：listed=true / date_added=2026-11-09 / due_date=2026-11-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：OpenBSD OpenSSH on Linux contains an unexpected status code or return value vulnerability that could allow for authentication bypass.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-125757 | P3 / 38 | mailcow / mailcow: dockerized | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-59986 | WATCH / 30 | alanxz / rabbitmq-c | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107356 | WATCH / 30 | U.S. Geological Survey / Area Species Management Research Program | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-96157 | WATCH / 28 | Microsoft / Windows 10 Version 1607 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96078 | WATCH / 28 | Microsoft / Windows 10 Version 1607 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96067 | WATCH / 28 | Microsoft / Windows 10 Version 1607 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95962 | WATCH / 28 | Microsoft / Windows 10 Version 1809 | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95901 | WATCH / 28 | Microsoft / Windows 10 Version 1607 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95882 | WATCH / 28 | Microsoft / Windows 10 Version 1607 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-89324 | WATCH / 28 | XTemos / Basel Post Types | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-88243 | WATCH / 28 | Microsoft / Windows Server 2016 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-88234 | WATCH / 28 | Microsoft / Windows Server 2016 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-88218 | WATCH / 28 | Microsoft / Windows 10 Version 1607 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-85844 | WATCH / 28 | Microsoft / Windows 10 Version 1607 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-82509 | WATCH / 28 | vlang / v | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-82391 | WATCH / 28 | zephyrproject / zephyr | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-80095 | WATCH / 28 | Microsoft / Microsoft SharePoint Server Subscription Edition | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-66801 | WATCH / 28 | Microsoft / Microsoft GDK | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-64682 | WATCH / 28 | NauelG / astro-blocks | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-64678 | WATCH / 28 | nitrite / nitrite-java | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-64670 | WATCH / 28 | walinejs / waline | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-63011 | WATCH / 28 | Intermesh / groupoffice | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-61887 | WATCH / 28 | 未確認 / Intel(R) TDX Migration Trust Domain (MigTD) | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：1；缺少 Product：0；缺少 Title：23。
- EPSS 未確認：25；Exploitation status 未確認：8。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-11T07:22:39.370628+00:00`；Delta generated at：`2026-11-11T07:22:39.370628+00:00`。

---

## 可驗證資料來源

- **CVE-2026-125350** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125350) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-116606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116606) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-116606) · [Vendor / Advisory (trust.barracuda.com)](https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection) · [Vendor / Advisory (github.com)](https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0042.md) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-20320** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20320) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20320) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bworks-xxe-uwUd7CEt) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-124194** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124194) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-124194)
- **CVE-2026-111560** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111560) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111560) · [Vendor / Advisory (trust.barracuda.com)](https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection) · [Vendor / Advisory (github.com)](https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0041.md) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-111793** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111793) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111793) · [Vendor / Advisory (github.com)](https://github.com/GISOpenwave/security-advisories-public/blob/main/CAN-2026-2032674.md) · [Vendor / Advisory (jvn.jp)](https://jvn.jp/en/vu/JVNVU93403064/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-123158** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123158) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-123158) · [Vendor / Advisory (openssh.org)](https://www.openssh.org/releasenotes.html) · [Vendor / Advisory (alpinelinux.org)](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/) · [Vendor / Advisory (github.com)](https://github.com/openssh/openssh-portable/commit/4353fdc43ef646c43a8dda7025cc1a898caf1482) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-125757** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125757)
- **CVE-2026-59986** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59986)
- **CVE-2026-107356** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107356)
- **CVE-2026-96157** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96157)
- **CVE-2026-96078** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96078)
- **CVE-2026-96067** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96067)
- **CVE-2026-95962** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95962)
- **CVE-2026-95901** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95901)
- **CVE-2026-95882** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95882)
- **CVE-2026-89324** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89324)
- **CVE-2026-88243** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88243)
- **CVE-2026-88234** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88234)
- **CVE-2026-88218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88218)
- **CVE-2026-85844** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85844)
- **CVE-2026-82509** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82509)
- **CVE-2026-82391** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82391)
- **CVE-2026-80095** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80095)
- **CVE-2026-66801** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66801)
- **CVE-2026-64682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-64682)
- **CVE-2026-64678** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-64678)
- **CVE-2026-64670** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-64670)
- **CVE-2026-63011** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63011)
- **CVE-2026-61887** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61887)
- **CVE-2026-61547** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61547)
- **CVE-2026-61473** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61473)
- **CVE-2026-44685** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-44685)
- **CVE-2026-126542** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126542)
- **CVE-2026-126539** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126539)
- **CVE-2026-126261** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126261)
- **CVE-2026-126187** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126187)
- **CVE-2026-126087** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126087)
- **CVE-2026-126082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126082)
- **CVE-2026-126065** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126065)
- **CVE-2026-125883** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125883)
- **CVE-2026-125881** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125881)
- **CVE-2026-125758** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125758)
- **CVE-2026-125347** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125347)
- **CVE-2026-125331** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125331)
- **CVE-2026-125298** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125298)
- **CVE-2026-125297** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125297)
- **CVE-2026-124917** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124917)
- **CVE-2026-124903** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124903)
- **CVE-2026-124900** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124900)
- **CVE-2026-124864** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124864)
- **CVE-2026-124861** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124861)
- **CVE-2026-124859** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124859)
- **CVE-2026-124853** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124853)
- **CVE-2026-121908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121908)
- **CVE-2026-121906** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121906)
- **CVE-2026-121904** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121904)
- **CVE-2026-121902** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121902)
- **CVE-2026-121898** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121898)
- **CVE-2026-121896** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121896)
- **CVE-2026-121894** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121894)
- **CVE-2026-121892** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121892)
- **CVE-2026-121889** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121889)
- **CVE-2026-121887** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121887)
- **CVE-2026-121683** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121683)
- **CVE-2026-121653** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121653)
- **CVE-2026-121529** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121529)
- **CVE-2026-121370** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121370)
- **CVE-2026-121356** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121356)
- **CVE-2026-121355** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121355)
- **CVE-2026-121354** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121354)
- **CVE-2026-121353** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121353)
- **CVE-2026-121352** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121352)
- **CVE-2026-121351** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121351)
- **CVE-2026-121349** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121349)
- **CVE-2026-121295** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121295)
- **CVE-2026-121289** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121289)
- **CVE-2026-120808** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120808)
- **CVE-2026-120779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120779)
- **CVE-2026-120002** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120002)
- **CVE-2026-119990** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119990)
- **CVE-2026-119958** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119958)
- **CVE-2026-119446** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119446)
- **CVE-2026-119017** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119017)
- **CVE-2026-118740** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118740)
- **CVE-2026-118383** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118383)
- **CVE-2026-116945** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116945)
- **CVE-2026-116928** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116928)
- **CVE-2026-114371** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114371)
- **CVE-2026-114162** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114162)
- **CVE-2026-114160** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114160)
- **CVE-2026-114146** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114146)
- **CVE-2026-113580** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113580)
- **CVE-2026-113579** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113579)
- **CVE-2026-112967** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112967)
- **CVE-2026-112136** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112136)
- **CVE-2026-109467** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109467)
- **CVE-2026-109454** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109454)
- **CVE-2026-108186** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108186)
- **CVE-2026-102166** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102166)
- **CVE-2026-67177** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67177)
- **CVE-2026-67176** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67176)
- **CVE-2026-67175** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67175)
- **CVE-2026-125333** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125333)
- **CVE-2026-124016** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124016)
- **CVE-2026-125749** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125749)
- **CVE-2026-124503** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124503) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-124503)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
