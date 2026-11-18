# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**112** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=111、NEW_KEV=1。
- Intelligence 候選：**30** 筆；P1 **1**、P2 **0**、P3 **1**、WATCH **28**。
- Baseline：state / generated_at=2026-11-17T08:41:13.667495+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-115731。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **112** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-115731｜Perforce / Puppet Enterprise
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00366 / percentile=0.30882
- **CISA KEV**：listed=true / date_added=2026-11-17 / due_date=2026-12-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-11-03T21:17:01.867 / 2026-11-18T05:19:01.130
- **官方描述（原文）**：Perforce Puppet Enterprise contains a deserialization of untrusted data vulnerability in Puppet’s report-processing code that allows a client with any CA-signed agent certificate to execute arbitrary code on the Puppet Server as the service user by submitting a report containing a crafted rich-data type through a PUT request. If the certificate authority automatically signs requests without strong verification, an unauthenticated network attacker can obtain a valid certificate and exploit the vulnerability.

### 2. CVE-2026-130603｜Eclipse Foundation / Eclipse Zenoh (zenoh-pico)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T14:17:47.153)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T14:17:47.153 / 2026-11-17T17:18:05.397
- **官方描述（原文）**：Eclipse Zenoh's zenoh-pico implementation, versions 0.7.2-rc up to but excluding 1.10.2, does not validate the Zenoh identifier (ZID) length when deserializing timestamps. An attacker-controlled length greater than 16 causes an out-of-bounds write to a fixed 16-byte identifier buffer and causes the subsequent zero-fill operation to receive a negative length converted to a large unsigned size. Truncated timestamp inputs can also cause out-of-bounds reads or assertion failures. A remote attacker able to deliver crafted timestamp-bearing Zenoh messages through an accepted transport can cause memory corruption and denial of service, with potential remote code execution in builds lacking appropriate binary protections. This issue is fixed in version 1.10.2. Depending on the release and message-decoding path, the unchecked timestamp identifier length causes a heap-based or stack-based buffer overflow. Ordinary-frame network message decoding moved from heap-backed storage to stack-local storage in version 1.5.0. Earlier affected releases already contained stack-based decoding paths, including reassembled fragmented messages.

### 3. CVE-2026-97698｜lepture / mistune
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T20:18:00.033)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T20:18:00.033 / 2026-11-17T20:18:00.177
- **官方描述（原文）**：Mistune is a Python Markdown parser with renderers and plugins. Prior to 3.3.4, parse_link_href performs an unbounded parenthesis-balancing scan to the end of the document for each unmatched opening parenthesis reached through an empty [] link label. In src/mistune/helpers.py and src/mistune/inline_parser.py, the empty label bypasses no_close_bracket_before, and no_link_before advances only past the short label, so successive [] ( candidates repeatedly scan the remaining document. Rendering untrusted Markdown with the default HTML renderer and no plugins can perform quadratic CPU work and keep a worker at 100 percent utilization. This issue is fixed in version 3.3.4.

### 4. CVE-2026-130627｜a2a-java / a2a-java-sdk-http-client-vertx
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T15:17:40.190)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T15:17:40.190 / 2026-11-17T19:17:56.787
- **官方描述（原文）**：The Vert.x HTTP client transport (a2a-java-sdk-http-client-vertx) hand-rolls a POST redirect follower that, when the documented PostBuilder.followRedirects(true) opt-in is enabled, re-issues the redirected request with the full request header map copied verbatim and performs no credential stripping and no same-authority check. A malicious, compromised, or mistyped agent that returns a 30x response with an absolute cross-host Location causes the client to forward the standard Authorization header (Bearer/Basic/OAuth) — plus every other header, including the allowlisted API-key headers — to the attacker-controlled authority. This breaks the project's own cross-transport invariant (SECURITY.md §8, OkHttpPostRedirectHeaderLeakTest) that credentials are stripped on cross-authority redirects even when redirects are followed. The sibling JDK and OkHttp/Android transports strip Authorization; Vert.x uniquely does not. This is a "fix introduced the bug" variant — the follower was added by the GHSA-9rhm hardening PR (3ae82912, refined by a5e76a0b).

### 5. CVE-2026-130626｜a2a-java / a2a-java-sdk-http-client
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T15:17:40.053)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T15:17:40.053 / 2026-11-17T19:17:56.660
- **官方描述（原文）**：The core JDK HTTP client (a2a-java-sdk-http-client) applies the GHSA-9rhm redirect-neutralization only to the POST path. JdkGetBuilder.get(), JdkGetBuilder.getAsyncSSE(), and JdkDeleteBuilder.delete() call the injected httpClient directly, with no redirect gate. An application that supplies a redirect-capable HttpClient (Redirect.NORMAL/ALWAYS) — which is the SDK-documented way to enable POST redirects — silently follows cross-authority redirects on every credentialed GET/DELETE request. The JDK strips Authorization cross-origin, but forwards the four allowlisted custom credential headers (X-API-Key, API-Key, X-Auth-Token, X-Authentication) to the attacker-controlled authority. This is an incomplete-fix variant of GHSA-9rhm: the fix hardened the default client and added a POST-only two-step opt-in, but never covered GET/DELETE.

### 6. CVE-2026-130591｜53AI / 53AIHub
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T14:17:46.007)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T14:17:46.007 / 2026-11-17T23:17:52.653
- **官方描述（原文）**：53AIHub before 0.5.5 contains a missing authentication vulnerability that allows unauthenticated attackers to read files by requesting /api/files/:file_id/preview and /api/file-version/:file_body_id without UserTokenAuth. Attackers can enumerate sequential numeric ids to read raw knowledge-base files and stored file versions belonging to any enterprise tenant.

### 7. CVE-2026-119726｜PocketBook / Obreey Products / PocketBook Reader
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T17:17:53.413)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T17:17:53.413 / 2026-11-17T17:17:53.413
- **官方描述（原文）**：Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in PocketBook / Obreey Products PocketBook Reader (Android) allows Exposure of Sensitive Information to an Unauthorized Actor. This issue affects PocketBook Reader (Android): 5.65.0.39561.release (com.obreey.reader).

### 8. CVE-2026-110782｜simplesamlphp / saml2
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T18:17:46.387)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T18:17:46.387 / 2026-11-17T19:17:45.227
- **官方描述（原文）**：The SimpleSAMLphp SAML2 library is a PHP library for SAML2 related functionality. From 6.2.2 until 6.2.4 and 7.0.0-rc2, HTTPArtifact::receive() in src/Binding/HTTPArtifact.php verifies a signed outer ArtifactResponse but returns an unsigned embedded SAML Response before calling verifyMessageSignature(). The signed path verifies with the artifact issuer's metadata keys without requiring the embedded Response issuer to match that artifact issuer. In a multi-IdP federation, an attacker controlling one trusted IdP can therefore return a validly signed outer ArtifactResponse containing an unsigned Response that claims a different IdP, bypassing the binding's embedded-message authentication. End-to-end impersonation requires a service provider using HTTP-Artifact and a downstream consumer that relies on the binding to authenticate the embedded Response rather than independently requiring a signature. This issue is fixed in versions 6.2.4 and 7.0.0-rc2.

### 9. CVE-2026-91618｜Oracle Corporation / Oracle Application Development Framework (ADF)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:26.123)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:26.123 / 2026-11-18T00:18:49.163
- **官方描述（原文）**：Vulnerability in the Oracle Application Development Framework (ADF) product of Oracle Fusion Middleware (component: Security Framework). The supported version that is affected is 12.2.1.4.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Application Development Framework (ADF). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Application Development Framework (ADF) accessible data as well as unauthorized access to critical data or complete access to all Oracle Application Development Framework (ADF) accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 10. CVE-2026-91585｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:25.783)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:25.783 / 2026-11-18T00:18:49.053
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: TopLink Integration). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via TCP to compromise Oracle WebLogic Server. Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 11. CVE-2026-91583｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:25.663)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:25.663 / 2026-11-18T00:18:48.943
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: TopLink Integration). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebLogic Server. Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 12. CVE-2026-91570｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:25.097)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:25.097 / 2026-11-18T01:17:57.163
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: TopLink Integration). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebLogic Server. Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 13. CVE-2026-91569｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:24.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:24.980 / 2026-11-17T22:19:24.980
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: TopLink Integration). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebLogic Server. While the vulnerability is in Oracle WebLogic Server, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 14. CVE-2026-91561｜Oracle Corporation / Oracle Service Bus
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:24.533)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:24.533 / 2026-11-17T22:19:24.533
- **官方描述（原文）**：Vulnerability in the Oracle Service Bus product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows low privileged attacker with network access via RMI to compromise Oracle Service Bus. While the vulnerability is in Oracle Service Bus, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Service Bus accessible data as well as unauthorized access to critical data or complete access to all Oracle Service Bus accessible data. CVSS 3.1 Base Score 9.6 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:N).

### 15. CVE-2026-91510｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:22.823)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:22.823 / 2026-11-17T22:19:22.823
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Access Manager accessible data as well as unauthorized access to critical data or complete access to all Oracle Access Manager accessible data and unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Access Manager. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:L).

### 16. CVE-2026-91507｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:22.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:22.587 / 2026-11-17T22:19:22.587
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Access Manager accessible data as well as unauthorized read access to a subset of Oracle Access Manager accessible data. CVSS 3.1 Base Score 9.3 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:N).

### 17. CVE-2026-91500｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:22.467)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:22.467 / 2026-11-17T22:19:22.467
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Access Manager accessible data as well as unauthorized access to critical data or complete access to all Oracle Access Manager accessible data and unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Access Manager. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:L).

### 18. CVE-2026-91470｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:22.223)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:22.223 / 2026-11-18T00:18:48.717
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server. Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 19. CVE-2026-91469｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:22.107)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:22.107 / 2026-11-17T22:19:22.107
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle WebLogic Server. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle WebLogic Server accessible data as well as unauthorized read access to a subset of Oracle WebLogic Server accessible data and unauthorized ability to cause a hang or frequently repeatable crash (complete DOS) of Oracle WebLogic Server. CVSS 3.1 Base Score 9.4 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:H).

### 20. CVE-2026-91456｜Oracle Corporation / Oracle WebLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:21.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:21.990 / 2026-11-18T00:18:48.597
- **官方描述（原文）**：Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core). Supported versions that are affected are 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via SOAP to compromise Oracle WebLogic Server. Successful attacks of this vulnerability can result in takeover of Oracle WebLogic Server. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 21. CVE-2026-69157｜ontola / atomic-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:18:12.620)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:18:12.620 / 2026-11-17T23:17:59.083
- **官方描述（原文）**：Atomic Server is an open source headless CMS and real-time database. From 0.29.0 to 0.40.2, Atomic Server provisions a well-known /setup invite with write enabled, the Drive root as its target, and usagesLeft set to one. construct_invite_redirect in server/src/plugins/invite.rs discards the redeemer identity, so an unauthenticated request containing an attacker-controlled public-key can create a new Agent and grant it write access to the entire Drive. On a fresh, unclaimed deployment, this permits reading, modifying, or deleting resources, changing permissions, and creating or altering Agents. No complete fixed version was verified as of this review.

### 22. CVE-2026-61680｜LabRedesCefetRJ / WeGIA
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:20.367)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:20.367 / 2026-11-17T22:19:20.527
- **官方描述（原文）**：WeGIA is a web manager for charitable institutions. Prior to 3.8.6, web/html/socio/sistema/cadastro_cobrancas_geracao.php performs privileged charge-generation operations without checking for an authenticated session. An unauthenticated remote requester who supplies valid charge-generation parameters can create arbitrary charge records, enabling financial record manipulation and large-scale billing corruption. This issue is fixed in version 3.8.6.

### 23. CVE-2026-61677｜LabRedesCefetRJ / WeGIA
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:20.193)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:20.193 / 2026-11-17T23:17:58.517
- **官方描述（原文）**：WeGIA is a web manager for charitable institutions. Prior to 3.8.7, web/html/socio/sistema/processa_edicao_socio.php updates member information without validating an authenticated session. An unauthenticated remote requester who supplies a target member identifier and replacement member fields can modify arbitrary member records, corrupt personal information, and cause loss of data integrity. This issue is fixed in version 3.8.7.

### 24. CVE-2026-61676｜LabRedesCefetRJ / WeGIA
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:20.023)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:20.023 / 2026-11-17T22:19:20.160
- **官方描述（原文）**：WeGIA is a web manager for charitable institutions. Prior to 3.8.7, web/html/socio/sistema/cadastro_cobranca.php creates billing records without checking for an authenticated session. An unauthenticated remote requester who supplies valid billing parameters can create arbitrary billing entries, enabling financial data manipulation and operational disruption. This issue is fixed in version 3.8.7.

### 25. CVE-2026-61675｜LabRedesCefetRJ / WeGIA
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:19.797)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:19.797 / 2026-11-17T22:19:19.990
- **官方描述（原文）**：WeGIA is a web manager for charitable institutions. Prior to 3.8.7, web/html/socio/sistema/atualiza_pagamentos.php performs payment-status database updates without checking whether the requester has an authenticated session. An unauthenticated remote requester can supply a payment identifier, payment date, and paid value to mark arbitrary payment records as paid or otherwise modify payment information, causing financial record corruption. This issue is fixed in version 3.8.7.

### 26. CVE-2026-28273｜ZoneMinder / zoneminder
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T19:18:00.103)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T19:18:00.103 / 2026-11-17T19:18:00.233
- **官方描述（原文）**：ZoneMinder is a free, open source closed-circuit television software application. Prior to 1.38.4, any authenticated user can use the /api/configs/edit/{name}.json endpoint to modify protected configuration settings because ConfigsController::edit() does not enforce the System=Edit authorization requirement and its system-variable protection is ineffective. An attacker can set ZM_PATH_FFMPEG to a command-bearing value and trigger an exec() sink in web/views/image.php or web/includes/Event.php by requesting frame extraction. This permits arbitrary command execution with the privileges of the web server user and can expose private camera feeds, recordings, and database data or establish persistence. This issue is fixed in version 1.38.4.

### 27. CVE-2026-131852｜OwnTracks / Recorder
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T00:18:43.127)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T00:18:43.127 / 2026-11-18T00:18:43.127
- **官方描述（原文）**：OwnTracks Recorder before 1.0.5 contains a format string vulnerability in json_response() and related output functions that allows unauthenticated attackers to execute code by storing a malicious tid value. Attackers can publish locations via POST /pub or MQTT with printf specifiers in tid, then read them back through GET /api/0/last to leak addresses and write memory.

### 28. CVE-2026-131088｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:18:08.687)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:18:08.687 / 2026-11-18T05:19:19.980
- **官方描述（原文）**：Improper input validation in WebAppInstalls in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had compromised the renderer process to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Low)

### 29. CVE-2026-131077｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:18:07.363)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:18:07.363 / 2026-11-18T05:19:18.843
- **官方描述（原文）**：Out of bounds write in Tint in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 30. CVE-2026-131061｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:18:05.430)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:18:05.430 / 2026-11-18T05:19:18.150
- **官方描述（原文）**：Buffer overflow in Color in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 31. CVE-2026-131057｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:18:04.947)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:18:04.947 / 2026-11-18T05:19:17.637
- **官方描述（原文）**：Out of bounds read in ANGLE in Google Chrome on on Android prior to 158.0.8127.36 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 32. CVE-2026-131054｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:18:04.570)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:18:04.570 / 2026-11-18T05:19:17.250
- **官方描述（原文）**：Out of bounds write in ANGLE in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 33. CVE-2026-131031｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:18:00.920)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:18:00.920 / 2026-11-18T05:19:16.097
- **官方描述（原文）**：Out of bounds write in GPU in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 34. CVE-2026-131025｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:18:00.137)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:18:00.137 / 2026-11-18T05:19:15.910
- **官方描述（原文）**：Out of bounds read in ANGLE in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 35. CVE-2026-130996｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:17:56.463)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:17:56.463 / 2026-11-18T05:19:14.090
- **官方描述（原文）**：Out of bounds write in ANGLE in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 36. CVE-2026-130994｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:17:56.223)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:17:56.223 / 2026-11-18T05:19:13.890
- **官方描述（原文）**：Use after free in WebGL in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 37. CVE-2026-130971｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:17:53.400)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:17:53.400 / 2026-11-18T05:19:11.900
- **官方描述（原文）**：Out of bounds write in ANGLE in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 38. CVE-2026-130910｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:17:45.100)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:17:45.100 / 2026-11-18T05:19:08.267
- **官方描述（原文）**：Protection mechanism failure in ANGLE in Google Chrome on on Android prior to 158.0.8127.36 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 39. CVE-2026-130870｜ClearFlask / ClearFlask
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T20:17:53.467)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T20:17:53.467 / 2026-11-17T20:17:53.467
- **官方描述（原文）**：ClearFlask before 2.7.3 contains an improper authorization vulnerability that allows any account holding an invitation ID to accept it regardless of invited email. Attackers who obtain a forwarded or shared invitation link can redeem it via accountAcceptInvitationAdmin or accountSignupAdmin to become project administrators.

### 40. CVE-2026-130868｜GreaterWMS / GreaterWMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T20:17:53.150)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T20:17:53.150 / 2026-11-17T20:17:53.150
- **官方描述（原文）**：GreaterWMS through 2.1.54 contains a predictable authentication token vulnerability that allows unauthenticated attackers to forge openid tokens by recomputing an unsalted MD5 hash of username and registration timestamp. Attackers who know a username and can bound its registration time can brute-force candidate openid values in the Token header to gain full read and write access to warehouse, staff, customer, supplier and order data.

### 41. CVE-2026-130856｜53AI / 53AIHub
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T20:17:51.240)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T20:17:51.240 / 2026-11-17T20:17:51.360
- **官方描述（原文）**：53AIHub before 0.5.5 contains a missing authentication vulnerability that allows remote unauthenticated attackers to reinitialize installed instances by calling the public POST /api/init endpoint. Attackers can reset an existing account's password, assign the top creator role, and obtain an access token to take over accounts and use admin-only API routes.

### 42. CVE-2026-130849｜BZFlag-Dev / bzflag
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T20:17:50.113)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T20:17:50.113 / 2026-11-17T20:17:50.113
- **官方描述（原文）**：BZFlag bzfs before 2.4.32 contains a heap out-of-bounds write vulnerability in NetHandler::tcpReceive() that allows remote unauthenticated attackers to corrupt heap memory by sending a TCP message with a body length of exactly 1024. Attackers can overwrite the tcplen receive offset with a negative value to write controlled bytes before the buffer, crashing the server or executing commands as the bzfs user.

### 43. CVE-2026-130840｜dataelement / BISHENG
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T20:17:48.737)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T20:17:48.737 / 2026-11-17T20:17:48.857
- **官方描述（原文）**：BISHENG before 3.0.0 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to impersonate administrators by abusing a hard-coded default jwt_secret used by AuthJwt. Attackers can forge an HS256 token offline naming user_id 1 with the admin role, send it as access_token_cookie, and gain full administrative access to users, workspaces, knowledge bases and workflows.

### 44. CVE-2026-130838｜Kozea / Radicale
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T20:17:48.413)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T20:17:48.413 / 2026-11-17T20:17:48.413
- **官方描述（原文）**：Radicale 3.3.0 before 3.8.3 contains an authorization bypass vulnerability that allows unauthenticated attackers to inherit group-based rights by reusing group memberships never reset between requests. Attackers can send credential-less requests after a group member logs in to read and write group-shared calendar and address book collections evaluated by the from_file rights backend.

### 45. CVE-2026-130802｜Hanshow Technology / Nebular Pro Electronic Shelf Labels
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T17:18:05.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T17:18:05.750 / 2026-11-17T20:17:46.463
- **官方描述（原文）**：The NFC authentication handshake relies on a fixed, static challenge instead of a unique, random value for every session. This allows an attacker to perform a "replay attack," successfully authenticating by simply sending the same pre-recorded response.

### 46. CVE-2026-130801｜Hanshow Technology / Nebular Pro Electronic Shelf Labels
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T17:18:05.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T17:18:05.647 / 2026-11-17T20:17:46.310
- **官方描述（原文）**：The device's command parser does not require asymmetric cryptographic signatures to validate incoming APDU packets. This enables an attacker to inject forged, unauthorized commands to manipulate device features and configurations once the initial handshake is bypassed.

### 47. CVE-2026-130587｜OpenFunction / OpenFunction
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T14:17:45.317)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T14:17:45.317 / 2026-11-17T17:18:05.160
- **官方描述（原文）**：OpenFunction through 1.2.0 contains a privilege escalation vulnerability that allows namespace tenants to create privileged host-access pods by supplying unrestricted PodSpec templates in Function and Serving resources. Attackers with only Function or Serving create permissions can set privileged, hostNetwork, hostPID, or hostPath fields to mount the worker node's root filesystem and escalate to node access.

### 48. CVE-2026-130583｜Rootways / Authorize.net CIM Pro extension for Magento 2
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T14:17:44.847)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T14:17:44.847 / 2026-11-17T14:17:44.847
- **官方描述（原文）**：Rootways Authorize.net CIM Pro extension for Magento 2 before 4.1.5 contains an unauthenticated server-side request forgery vulnerability in the Apple Pay merchant validation controller. Attackers can supply file://, gopher://, or dict:// URLs in the validationUrl parameter to read app/etc/env.php credentials and encryption keys or reach internal services and cloud metadata endpoints.

### 49. CVE-2026-129448｜Apache Software Foundation / Apache Roller
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T11:17:28.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T11:17:28.190 / 2026-11-17T12:17:48.687
- **官方描述（原文）**：Deserialization of Untrusted Data in Apache Roller versions 4.0.0 through 6.1.4 allows an unauthenticated remote attacker to execute arbitrary code. The XML-RPC endpoint accepts vendor extension types and deserializes them before authenticating the requester. This is the same vulnerability as CVE-2026-82384, which listed only Apache Roller 6.1.5 as affected. This issue is being actively exploited. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which disables the extension types and rejects XML-RPC requests when the XML-RPC feature is disabled. Users who cannot upgrade right away should set "enabledForExtensions" to "false" in WEB-INF/web.xml, or remove the "/roller-services/xmlrpc" servlet mapping, and restart Roller. Disabling XML-RPC in the administration UI is not enough, because older versions deserialize the request before checking that setting.

### 50. CVE-2026-129286｜N-able / N-central
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T11:17:27.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T11:17:27.943 / 2026-11-18T05:19:06.430
- **官方描述（原文）**：N-able N-central before 2026.4.1 HF3 does not validate version values and download locations in software update metadata. An attacker able to supply or modify the update metadata received by the server can write files outside the download directory and execute code as the N-central service account.

### 51. CVE-2026-129280｜N-able / N-central
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T11:17:27.187)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T11:17:27.187 / 2026-11-17T22:17:20.613
- **官方描述（原文）**：Multiple ServerUI and ServerUI2 SOAP operations in N-able N-central before 2026.4.1 HF3 do not verify the caller's session, permissions or customer scope. A remote attacker, in some cases without authentication, can read device and patch data, test passwords of user accounts, send messages to managed agents, and modify device and service settings belonging to other customers.

### 52. CVE-2026-129272｜N-able / N-central
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T11:17:26.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T11:17:26.110 / 2026-11-18T05:19:05.597
- **官方描述（原文）**：N-able N-central before 2026.4.1 HF3 uses a predictable credential to authenticate appliances to an agent-facing API. A remote, unauthenticated attacker who knows or guesses an appliance identifier can obtain a valid appliance token and session and impersonate that appliance.

### 53. CVE-2026-127369｜Oracle Corporation / Oracle Hyperion Financial Close Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:01.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:01.630 / 2026-11-18T00:18:39.400
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Manage). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via Oracle Net to compromise Oracle Hyperion Financial Close Management. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Financial Close Management accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Financial Close Management accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 54. CVE-2026-127362｜Oracle Corporation / Oracle Hyperion Financial Close Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:19:00.777)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:19:00.777 / 2026-11-18T00:18:39.283
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Manage). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Financial Close Management. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Financial Close Management accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Financial Close Management accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 55. CVE-2026-127327｜Oracle Corporation / Oracle AutoVue
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:56.737)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:56.737 / 2026-11-18T00:18:39.060
- **官方描述（原文）**：Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security). The supported version that is affected is 21.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle AutoVue. Successful attacks of this vulnerability can result in takeover of Oracle AutoVue. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 56. CVE-2026-127326｜Oracle Corporation / Oracle AutoVue
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:56.613)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:56.613 / 2026-11-18T01:17:52.420
- **官方描述（原文）**：Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security). The supported version that is affected is 21.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle AutoVue. Successful attacks of this vulnerability can result in takeover of Oracle AutoVue. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 57. CVE-2026-127325｜Oracle Corporation / Oracle AutoVue
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:56.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:56.490 / 2026-11-18T00:18:38.947
- **官方描述（原文）**：Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security). The supported version that is affected is 21.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle AutoVue. Successful attacks of this vulnerability can result in takeover of Oracle AutoVue. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 58. CVE-2026-127324｜Oracle Corporation / Oracle AutoVue
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:56.377)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:56.377 / 2026-11-18T00:18:38.833
- **官方描述（原文）**：Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security). The supported version that is affected is 21.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle AutoVue. Successful attacks of this vulnerability can result in takeover of Oracle AutoVue. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 59. CVE-2026-126969｜SmarterTools / SmarterMail
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T00:18:37.280)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T00:18:37.280 / 2026-11-18T00:18:37.280
- **官方描述（原文）**：SmarterTools SmarterMail Insufficient Entropy Authentication Bypass Vulnerability. This vulnerability allows remote attackers to bypass authentication on affected installations of SmarterTools SmarterMail. Authentication is not required to exploit this vulnerability. The specific flaw exists within the generation of Application Passwords. The issue results from using insufficient entropy in the generation of credentials. An attacker can leverage this vulnerability to bypass authentication on the system. Was ZDI-CAN-33568.

### 60. CVE-2026-126574｜ASUS / Control Center Datacenter
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T02:17:40.657)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T02:17:40.657 / 2026-11-18T02:17:40.657
- **官方描述（原文）**：Missing authorization vulnerability in ASUS Control Center Datacenter and Control Center Enterprise allows remote authenticated users with a low-privileged Viewer role to change the password of an Administrator account, thereby obtaining administrative privileges, via a crafted password update request. Refer to the ' Security Update for ASUS Control Center ' section on the ASUS Security Advisory for more information.

### 61. CVE-2026-126553｜Broadcom / AutoSys Workload Automation
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T17:17:59.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T17:17:59.527 / 2026-11-17T18:17:51.877
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Broadcom AutoSys Workload Automation (Workload Control Center (WCC) modules) on Windows, Linux allows Object Injection.This issue affects AutoSys Workload Automation: from 12.1 through 24.0.01.

### 62. CVE-2026-126552｜Broadcom / AutoSys Workload Automation
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T17:17:59.400)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T17:17:59.400 / 2026-11-17T18:17:51.760
- **官方描述（原文）**：Missing Authentication for Critical Function, OS Command Injection vulnerability in Broadcom AutoSys Workload Automation (Workload Control Center (WCC) modules) on Windows, Linux allows OS Command Injection.This issue affects AutoSys Workload Automation: from 12.1 through 24.0.01.

### 63. CVE-2026-126551｜Broadcom / AutoSys Workload Automation
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T17:17:59.260)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T17:17:59.260 / 2026-11-17T17:17:59.260
- **官方描述（原文）**：Use of Hard-coded Cryptographic Key vulnerability in Broadcom AutoSys Workload Automation (Workload Control Center (WCC) modules) on Windows, Linux allows Session Credential Falsification through Forging.This issue affects AutoSys Workload Automation: from 12.1 through 24.2.00.

### 64. CVE-2026-122150｜ICRTouch / TouchPoint POS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T16:17:40.853)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T16:17:40.853 / 2026-11-17T20:17:37.727
- **官方描述（原文）**：The PocketTouch and TouchPoint POS `CHECKPAYMENT` workflow accepts a caller-supplied clerk number without adequately verifying that the requesting client is authorized to act as that clerk. An attacker with access to the POS protocol may be able to specify another employee’s clerk identifier and submit payment-related requests under that identity.

### 65. CVE-2026-122149｜ICRTouch / TouchPoint POS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T16:17:40.747)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T16:17:40.747 / 2026-11-17T19:17:47.863
- **官方描述（原文）**：The PocketTouch and TouchPoint POS protocol includes a `SAVECONFIG` command that appears capable of overwriting till configuration files remotely. An attacker with network access to the POS socket service may be able to submit a crafted `SAVECONFIG` command and replace or modify terminal configuration data.

### 66. CVE-2026-122147｜ICRTouch / PocketTouch
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T16:17:40.643)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T16:17:40.643 / 2026-11-17T19:17:47.707
- **官方描述（原文）**：ICRTouch PocketTouch version 1.700 build 2025.3726 defines hard-coded default values for multiple credential fields, including a socket password and configuration and shutdown passwords. An additional email-related password field is initialized without a value.

### 67. CVE-2026-122142｜ICRTouch / Commander
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T16:17:40.287)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T16:17:40.287 / 2026-11-17T20:17:37.563
- **官方描述（原文）**：ICRTouch Commander administrative login interface does not adequately restrict repeated authentication attempts. The interface also returns distinguishable responses for multiple authentication states, including different behavior when a `siteID` value is supplied.

### 68. CVE-2026-122122｜ICRTouch / TouchTakeaway
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T16:17:39.963)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T16:17:39.963 / 2026-11-17T20:17:37.207
- **官方描述（原文）**：The order-tracking functionality in ICRTouch ByTable and TouchTakeaway does not adequately verify that a requester is authorized to access the specified order. An unauthenticated remote attacker can modify an order identifier to retrieve information associated with other customers’ orders.

### 69. CVE-2026-122055｜ICRTouch / PocketTouch
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T16:17:39.663)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T16:17:39.663 / 2026-11-17T20:17:37.053
- **官方描述（原文）**：ICRTouch PocketTouch version 1.700 build 2025.3726 contains a default socket password set to the literal value password. Where the default value remains unchanged and is accepted by a TouchPoint POS terminal, an attacker with network access to the terminal’s socket service may authenticate using publicly known credentials.

### 70. CVE-2026-119623｜TYPO3 / TYPO3 CMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T11:17:24.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T11:17:24.740 / 2026-11-17T12:17:44.280
- **官方描述（原文）**：The installer (first installation wizard) could be re-enabled on an already configured instance by placing a file whose name starts with FIRST_INSTALL in the public web root or the project root. The installer then became accessible without authentication, allowing for example to change the database connection and to create a new administrator and system maintainer account, which leads to remote code execution. As demonstrated in TYPO3-CORE-SA-2026-026, such a file could be created by an authenticated, low-privileged backend user without any further permissions. Other ways of creating files in the web root, as well as leftover or restored marker files, could be abused in the same way. With the fixed versions, the installer can no longer be re-enabled on an already configured instance by a marker file. A new internal setting $GLOBALS['TYPO3_CONF_VARS']['SYS']['isInstalling'] is stored in the system configuration and is only enabled while a new installation is running. Additionally, only the exact file names FIRST_INSTALL and FIRST_INSTALL.txt are accepted as marker files.

### 71. CVE-2026-119293｜signalwire / freeswitch
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T20:17:36.417)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T20:17:36.417 / 2026-11-17T23:17:45.473
- **官方描述（原文）**：FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to a software implementation that runs on any commodity hardware. In 1.11.2 and earlier, rtp_common_read() in src/switch_rtp.c uses one session-wide autoadj_tally to learn RTP sources that differ from the address negotiated in SDP. An unauthenticated remote attacker who sends plaintext RTP during call setup can make packets from one or more non-advertised sources reach the threshold before the legitimate endpoint, causing FreeSWITCH to adopt the source of the threshold-crossing packet as the media peer. The attacker can then receive call audio, inject media, and deny media to the legitimate endpoint without being on the media path. FreeSWITCH 1.11.2 adds two opt-in controls, but both default to zero and the release remains affected unless both are configured before RTP session creation. This vulnerability is fixed in 1.11.2.

### 72. CVE-2026-115139｜Oracle Corporation / Oracle Hyperion Infrastructure Technology
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:47.437)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:47.437 / 2026-11-17T22:18:47.437
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and Configuration). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Infrastructure Technology. Successful attacks require human interaction from a person other than the attacker and while the vulnerability is in Oracle Hyperion Infrastructure Technology, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Infrastructure Technology accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Infrastructure Technology accessible data. CVSS 3.1 Base Score 9.3 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N).

### 73. CVE-2026-115089｜Oracle Corporation / Oracle Hyperion Planning
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:41.757)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:41.757 / 2026-11-18T00:18:36.093
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Application Development Framework). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Planning. Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Planning. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 74. CVE-2026-115086｜Oracle Corporation / Oracle Hyperion Planning
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:41.407)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:41.407 / 2026-11-18T01:17:51.710
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via RMI to compromise Oracle Hyperion Planning. Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Planning. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 75. CVE-2026-115080｜Oracle Corporation / Oracle Hyperion Infrastructure Technology
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:40.703)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:40.703 / 2026-11-18T01:17:51.600
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and Configuration). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Infrastructure Technology. Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Infrastructure Technology. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 76. CVE-2026-115050｜Oracle Corporation / Oracle Hyperion Infrastructure Technology
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:37.100)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:37.100 / 2026-11-18T00:18:35.860
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and Configuration). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Infrastructure Technology. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Infrastructure Technology accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Infrastructure Technology accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 77. CVE-2026-115048｜Oracle Corporation / Oracle Hyperion Infrastructure Technology
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:36.870)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:36.870 / 2026-11-18T01:17:51.483
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Infrastructure Technology. Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Infrastructure Technology. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 78. CVE-2026-115047｜Oracle Corporation / Oracle Hyperion Infrastructure Technology
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:36.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:36.760 / 2026-11-18T01:17:51.377
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and Configuration). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Infrastructure Technology. Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Infrastructure Technology. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 79. CVE-2026-114980｜Oracle Corporation / Oracle AutoVue
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:28.903)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:28.903 / 2026-11-17T22:18:28.903
- **官方描述（原文）**：Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security Related Issues). The supported version that is affected is 21.1.0. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle AutoVue. While the vulnerability is in Oracle AutoVue, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle AutoVue. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 80. CVE-2026-114978｜Oracle Corporation / Oracle Hyperion Financial Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:28.660)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:28.660 / 2026-11-17T22:18:28.660
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Hyperion Financial Management. While the vulnerability is in Oracle Hyperion Financial Management, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Financial Management. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 81. CVE-2026-114956｜Oracle Corporation / Oracle Hyperion Planning
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:26.023)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:26.023 / 2026-11-17T22:18:26.023
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Planning. Successful attacks require human interaction from a person other than the attacker and while the vulnerability is in Oracle Hyperion Planning, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Hyperion Planning accessible data as well as unauthorized access to critical data or complete access to all Oracle Hyperion Planning accessible data. CVSS 3.1 Base Score 9.3 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N).

### 82. CVE-2026-114952｜Oracle Corporation / MySQL Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:25.530)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:25.530 / 2026-11-18T00:18:34.357
- **官方描述（原文）**：Vulnerability in the MySQL Server, MySQL Cluster product of Oracle MySQL (component: Client programs). Supported versions that are affected are MySQL Server: 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10; MySQL Cluster: 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4 and 26.10. Easily exploitable vulnerability allows unauthenticated attacker with network access via multiple protocols to compromise MySQL Server, MySQL Cluster. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all MySQL Server, MySQL Cluster accessible data as well as unauthorized access to critical data or complete access to all MySQL Server, MySQL Cluster accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 83. CVE-2026-114934｜Oracle Corporation / PeopleSoft Enterprise PeopleTools
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:23.437)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:23.437 / 2026-11-17T22:18:23.437
- **官方描述（原文）**：Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Integration Broker). Supported versions that are affected are 8.61-8.63. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PeopleTools. While the vulnerability is in PeopleSoft Enterprise PeopleTools, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all PeopleSoft Enterprise PeopleTools accessible data as well as unauthorized update, insert or delete access to some of PeopleSoft Enterprise PeopleTools accessible data. CVSS 3.1 Base Score 9.3 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N).

### 84. CVE-2026-114925｜Oracle Corporation / Oracle Applications Framework
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:22.387)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:22.387 / 2026-11-18T01:17:50.693
- **官方描述（原文）**：Vulnerability in the Oracle Applications Framework product of Oracle E-Business Suite (component: REST Services). Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Applications Framework. Successful attacks of this vulnerability can result in takeover of Oracle Applications Framework. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 85. CVE-2026-114924｜Oracle Corporation / Oracle Application Object Library
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:22.273)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:22.273 / 2026-11-18T01:17:50.573
- **官方描述（原文）**：Vulnerability in the Oracle Application Object Library product of Oracle E-Business Suite (component: Core). Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Application Object Library. Successful attacks of this vulnerability can result in takeover of Oracle Application Object Library. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 86. CVE-2026-114881｜Oracle Corporation / Document Management and Collaboration
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:17.107)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:17.107 / 2026-11-17T22:18:17.107
- **官方描述（原文）**：Vulnerability in the Document Management and Collaboration product of Oracle E-Business Suite (component: Attachments). Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Document Management and Collaboration. Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all Document Management and Collaboration accessible data and unauthorized ability to cause a hang or frequently repeatable crash (complete DOS) of Document Management and Collaboration. CVSS 3.1 Base Score 9.1 (Confidentiality and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H).

### 87. CVE-2026-114880｜Oracle Corporation / Document Management and Collaboration
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:16.987)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:16.987 / 2026-11-18T01:17:50.463
- **官方描述（原文）**：Vulnerability in the Document Management and Collaboration product of Oracle E-Business Suite (component: Attachments). Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Document Management and Collaboration. Successful attacks of this vulnerability can result in takeover of Document Management and Collaboration. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 88. CVE-2026-114863｜Oracle Corporation / Oracle Universal Work Queue
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:14.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:14.940 / 2026-11-18T01:17:50.343
- **官方描述（原文）**：Vulnerability in the Oracle Universal Work Queue product of Oracle E-Business Suite (component: Media Integration issues). Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Universal Work Queue. Successful attacks of this vulnerability can result in takeover of Oracle Universal Work Queue. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 89. CVE-2026-114862｜Oracle Corporation / PeopleSoft Enterprise PeopleTools
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:14.817)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:14.817 / 2026-11-18T00:18:34.240
- **官方描述（原文）**：Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Weblogic). Supported versions that are affected are 8.61-8.63. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PeopleTools. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all PeopleSoft Enterprise PeopleTools accessible data as well as unauthorized access to critical data or complete access to all PeopleSoft Enterprise PeopleTools accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 90. CVE-2026-114856｜Oracle Corporation / Oracle REST Data Services
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:14.213)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:14.213 / 2026-11-17T22:18:14.213
- **官方描述（原文）**：Vulnerability in Oracle REST Data Services (component: General). Supported versions that are affected are 24.2.0-26.3.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle REST Data Services. Successful attacks require human interaction from a person other than the attacker and while the vulnerability is in Oracle REST Data Services, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle REST Data Services. CVSS 3.1 Base Score 9.6 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H).

### 91. CVE-2026-114850｜Oracle Corporation / Oracle APEX
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:13.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:13.510 / 2026-11-18T01:17:50.093
- **官方描述（原文）**：Vulnerability in Oracle APEX (component: General). Supported versions that are affected are 24.1.22, 24.2.21, 26.1.5 and 26.2.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle APEX. Successful attacks of this vulnerability can result in takeover of Oracle APEX. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 92. CVE-2026-114849｜Oracle Corporation / Oracle APEX
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:13.393)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:13.393 / 2026-11-18T01:17:49.980
- **官方描述（原文）**：Vulnerability in Oracle APEX (component: General). Supported versions that are affected are 24.1.22, 24.2.21, 26.1.5 and 26.2.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTPS to compromise Oracle APEX. Successful attacks of this vulnerability can result in takeover of Oracle APEX. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 93. CVE-2026-114848｜Oracle Corporation / Oracle Database Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:13.277)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:13.277 / 2026-11-17T22:18:13.277
- **官方描述（原文）**：Vulnerability in the Oracle Text component of Oracle Database Server. Supported versions that are affected are 19.3-19.33, 21.3-21.24 and 23.4.0-23.26.3. Easily exploitable vulnerability allows low privileged attacker having Create Session privilege with network access via Oracle Net to compromise Oracle Text. While the vulnerability is in Oracle Text, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Text. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 94. CVE-2026-114847｜Oracle Corporation / Oracle Autonomous Health Framework
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:13.160)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:13.160 / 2026-11-18T00:18:34.130
- **官方描述（原文）**：Vulnerability in Oracle Autonomous Health Framework (component: Developer triaging platform). Supported versions that are affected are 26.4-26.10. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Autonomous Health Framework. Successful attacks of this vulnerability can result in unauthorized creation, deletion or modification access to critical data or all Oracle Autonomous Health Framework accessible data as well as unauthorized access to critical data or complete access to all Oracle Autonomous Health Framework accessible data. CVSS 3.1 Base Score 9.1 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N).

### 95. CVE-2026-114835｜Oracle Corporation / Oracle Access Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:11.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:11.710 / 2026-11-17T22:18:11.710
- **官方描述（原文）**：Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Admin Console). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.1.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Access Manager. While the vulnerability is in Oracle Access Manager, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Access Manager. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 96. CVE-2026-114826｜Oracle Corporation / Service Delivery Platform
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:10.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:10.630 / 2026-11-18T01:17:49.637
- **官方描述（原文）**：Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler). The supported version that is affected is 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via SOAP to compromise Service Delivery Platform. Successful attacks of this vulnerability can result in takeover of Service Delivery Platform. CVSS 3.1 Base Score 9.8 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

### 97. CVE-2026-114824｜Oracle Corporation / Oracle Platform Security for Java
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:10.373)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:10.373 / 2026-11-17T22:18:10.373
- **官方描述（原文）**：Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Thirdparty Jars). Supported versions that are affected are 12.2.1.4.0 and 14.1.2.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Platform Security for Java. While the vulnerability is in Oracle Platform Security for Java, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Platform Security for Java. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 98. CVE-2026-114822｜Oracle Corporation / Oracle Database Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:10.103)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:10.103 / 2026-11-17T22:18:10.103
- **官方描述（原文）**：Vulnerability in the RDBMS component of Oracle Database Server. Supported versions that are affected are 23.4.0-23.26.4. Easily exploitable vulnerability allows low privileged attacker having Create Session privilege with network access via Oracle Net to compromise RDBMS. While the vulnerability is in RDBMS, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of RDBMS. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 99. CVE-2026-114819｜Oracle Corporation / Oracle Database Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:09.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:09.980 / 2026-11-17T22:18:09.980
- **官方描述（原文）**：Vulnerability in the Oracle Text component of Oracle Database Server. Supported versions that are affected are 19.3-19.32, 21.3-21.24 and 23.4.0-23.26.3. Easily exploitable vulnerability allows low privileged attacker having Create Session privilege with network access via Oracle Net to compromise Oracle Text. While the vulnerability is in Oracle Text, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Text. CVSS 3.1 Base Score 9.9 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H).

### 100. CVE-2026-114785｜Oracle Corporation / Oracle Hyperion Planning
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:05.907)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:05.907 / 2026-11-17T22:18:05.907
- **官方描述（原文）**：Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security). The supported version that is affected is 11.2.26.0.000. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Hyperion Planning. Successful attacks require human interaction from a person other than the attacker and while the vulnerability is in Oracle Hyperion Planning, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Hyperion Planning. CVSS 3.1 Base Score 9.6 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H).

### 101. CVE-2026-114784｜Oracle Corporation / Oracle Business Intelligence Enterprise Edition
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:05.783)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:05.783 / 2026-11-17T22:18:05.783
- **官方描述（原文）**：Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Platform Security). Supported versions that are affected are 8.2.0.0.0 and 26.01.0.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Business Intelligence Enterprise Edition. While the vulnerability is in Oracle Business Intelligence Enterprise Edition, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in takeover of Oracle Business Intelligence Enterprise Edition. CVSS 3.1 Base Score 10.0 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

### 102. CVE-2026-114205｜ASUS / Control Center Express
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T02:17:39.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T02:17:39.980 / 2026-11-18T02:17:39.980
- **官方描述（原文）**：Incorrect authorization in ASUS Control Center Express allows a remote authenticated user with a low-privileged role to create an administrator account, resulting in administrative control of the management console and of the clients it manages. Refer to the ' Security Update for ASUS Control Center Express Agent ' section on the ASUS Security Advisory for more information.

### 103. CVE-2026-114204｜ASUS / Control Center Express
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T02:17:39.850)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T02:17:39.850 / 2026-11-18T02:17:39.850
- **官方描述（原文）**：Use of Hard-coded Cryptographic Key in ASUS Control Center Express allows a remote user to bypass authentication by forging a session token for an account with a recent valid login, resulting in administrative control of the management console and of the clients it manages. Refer to the ' Security Update for ASUS Control Center Express Agent ' section on the ASUS Security Advisory for more information.

### 104. CVE-2026-114202｜ASUS / Control Center Express
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-18T02:17:39.713)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-18T02:17:39.713 / 2026-11-18T02:17:39.713
- **官方描述（原文）**：Use of Hard-coded Cryptographic Key in ASUS Control Center Express allows a remote user to gain administrative privileges via a forged authentication token. Refer to the ' Security Update for ASUS Control Center Express Agent ' section on the ASUS Security Advisory for more information.

### 105. CVE-2026-101691｜Oracle Corporation / Oracle Mobile Field Service
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T22:18:04.460)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T22:18:04.460 / 2026-11-17T22:18:04.460
- **官方描述（原文）**：Vulnerability in the Oracle Mobile Field Service product of Oracle E-Business Suite (component: Admin UI). Supported versions that are affected are 12.2.3-12.2.15. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Mobile Field Service. While the vulnerability is in Oracle Mobile Field Service, attacks may significantly impact additional products (scope change). Successful attacks of this vulnerability can result in unauthorized access to critical data or complete access to all Oracle Mobile Field Service accessible data as well as unauthorized update, insert or delete access to some of Oracle Mobile Field Service accessible data. CVSS 3.1 Base Score 9.3 (Confidentiality and Integrity impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N).

### 106. CVE-2026-100397｜rucio / rucio
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T20:17:35.207)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T20:17:35.207 / 2026-11-17T22:17:22.407
- **官方描述（原文）**：Rucio is a scientific data management framework. From 1.14.0 until 35.9.1, 38.6.1, 40.4.2, and 41.1.1, validate_auth_token in lib/rucio/core/authentication.py does not distinguish short-lived SSH challenge nonces from authentication tokens stored in the same token table. An unauthenticated attacker can request /auth/ssh_challenge_token for an arbitrary account by supplying X-Rucio-Account, then present the returned X-Rucio-SSH-Challenge-Token as X-Rucio-Auth-Token to authenticate to other API endpoints as that account, including an administrative account. This issue is fixed in versions 35.9.1, 38.6.1, 40.4.2, and 41.1.1.

### 107. CVE-2025-62165｜pi-hole / FTL
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T21:17:34.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T21:17:34.990 / 2026-11-17T21:17:34.990
- **官方描述（原文）**：Pi-hole FTL is the core engine of the Pi-hole network-level advertisement and tracker blocker. From 6.0 until 6.7, CivetWeb permits unauthenticated clients to flood the WebUI login page and API invalid paths without connection or request-rate limits. Repeated requests can consume substantial CPU in request processing and session authentication, making the WebUI sluggish or unresponsive and potentially affecting the wider system and DNS service. Requests to selected invalid or redirecting paths also generate a log entry for each request, allowing network traffic to expand logs and exhaust constrained storage such as an SD card, while other request forms consume CPU without producing a corresponding request log. This vulnerability is fixed in 6.7.

### 108. CVE-2026-95849｜linkwarden / linkwarden
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T19:18:03.577)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T19:18:03.577 / 2026-11-17T20:17:59.920
- **官方描述（原文）**：Linkwarden is a self-hosted, open-source collaborative bookmark manager to collect, organize and archive webpages. Prior to 2.15.0, .github/workflows/check-branch.yml runs on the privileged pull_request_target event and interpolates the attacker-controlled github.head_ref source branch name unquoted into a run: shell script. An unauthenticated attacker can open a pull request from a fork with shell metacharacters in its branch name, causing arbitrary commands to execute in the base repository's privileged CI job before the branch comparison result matters. The job has access to GITHUB_TOKEN and any exposed secrets, allowing secret exfiltration and, when workflow token permissions allow repository writes, modification of repository content. This issue is fixed in version 2.15.0.

### 109. CVE-2026-130794｜frappe / hrms
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T20:17:45.290)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T20:17:45.290 / 2026-11-17T23:17:53.107
- **官方描述（原文）**：Frappe HR (hrms) before 16.9.0 contains a missing authorization vulnerability in the hrms.api.roster.get_events method that allows authenticated employees to view other employees' leave and shift data by bypassing User Permissions. Attackers with the Employee role can call get_events with empty filters for any date range to retrieve every employee's approved leave applications and shift assignments, including leave types, dates, shift locations and times.

### 110. CVE-2026-130633｜gpac / gpac
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T15:17:41.143)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T15:17:41.143 / 2026-11-17T19:17:57.043
- **官方描述（原文）**：GPAC before 26.02.0 contains a use-after-free vulnerability in gf_filter_pid_set_args_internal() that leaves a stale pointer after gf_props_reset_single() frees a parsed PID property value. Attackers can supply a crafted filelist input processed by MP4Box with -add, causing gf_props_del_property() to access freed memory and crash the application.

### 111. CVE-2026-130592｜thorsten / phpMyFAQ
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T14:17:46.257)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T14:17:46.257 / 2026-11-17T14:17:46.413
- **官方描述（原文）**：phpMyFAQ 4.0.12 through 4.0.19, 4.1.x before 4.1.12, and 4.2.0 pre-releases before 4.2.0-RC.1 contain a stored cross-site scripting vulnerability in startpage.twig, where top-ten FAQ titles are rendered with Twig's raw filter. Authenticated users with FAQ edit permission can save a question containing a double quote and event handler, which runs script for every start page visitor.

### 112. CVE-2024-43361｜ZoneMinder / zoneminder
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-17T19:17:42.580)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-17T19:17:42.580 / 2026-11-17T20:17:33.590
- **官方描述（原文）**：ZoneMinder is a free, open source closed-circuit television software application. Prior to 1.38.4, detaintPath() in web/includes/functions.php can be bypassed with a PHP stream-wrapper path when sanitizing modal.php input. A remote unauthenticated attacker can submit such a path through the affected input and potentially read unauthorized local files through local file inclusion. This issue is fixed in version 1.38.4.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-115731｜Perforce / Puppet Enterprise
- **Title**：Perforce Puppet Enterprise Deserialization of Untrusted Data Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、DELTA_NEW_KEV(+15)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.00366 / percentile=0.30882
- **CISA KEV**：listed=true / date_added=2026-11-17 / due_date=2026-12-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Perforce Puppet Enterprise contains a deserialization of untrusted data vulnerability in Puppet’s report-processing code that allows a client with any CA-signed agent certificate to execute arbitrary code on the Puppet Server as the service user by submitting a report containing a crafted rich-data type through a PUT request. If the certificate authority automatically signs requests without strong verification, an unauthenticated network attacker can obtain a valid certificate and exploit the vulnerability.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-130603 | P3 / 38 | Eclipse Foundation / Eclipse Zenoh (zenoh-pico) | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-97698 | WATCH / 30 | lepture / mistune | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-130627 | WATCH / 30 | a2a-java / a2a-java-sdk-http-client-vertx | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-130626 | WATCH / 30 | a2a-java / a2a-java-sdk-http-client | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-130591 | WATCH / 30 | 53AI / 53AIHub | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-119726 | WATCH / 30 | PocketBook / Obreey Products / PocketBook Reader | v4.0 8.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-110782 | WATCH / 30 | simplesamlphp / saml2 | v3.1 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91618 | WATCH / 28 | Oracle Corporation / Oracle Application Development Framework (ADF) | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-91585 | WATCH / 28 | Oracle Corporation / Oracle WebLogic Server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-91583 | WATCH / 28 | Oracle Corporation / Oracle WebLogic Server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-91570 | WATCH / 28 | Oracle Corporation / Oracle WebLogic Server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-91569 | WATCH / 28 | Oracle Corporation / Oracle WebLogic Server | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-91561 | WATCH / 28 | Oracle Corporation / Oracle Service Bus | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-91510 | WATCH / 28 | Oracle Corporation / Oracle Access Manager | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-91507 | WATCH / 28 | Oracle Corporation / Oracle Access Manager | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-91500 | WATCH / 28 | Oracle Corporation / Oracle Access Manager | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-91470 | WATCH / 28 | Oracle Corporation / Oracle WebLogic Server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-91469 | WATCH / 28 | Oracle Corporation / Oracle WebLogic Server | v3.1 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-91456 | WATCH / 28 | Oracle Corporation / Oracle WebLogic Server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-69157 | WATCH / 28 | ontola / atomic-server | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-61680 | WATCH / 28 | LabRedesCefetRJ / WeGIA | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-61677 | WATCH / 28 | LabRedesCefetRJ / WeGIA | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-61676 | WATCH / 28 | LabRedesCefetRJ / WeGIA | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-61675 | WATCH / 28 | LabRedesCefetRJ / WeGIA | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-28273 | WATCH / 28 | ZoneMinder / zoneminder | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-131852 | WATCH / 28 | OwnTracks / Recorder | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-131088 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-131077 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-131061 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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
- EPSS 未確認：29；Exploitation status 未確認：11。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-18T08:05:07.825955+00:00`；Delta generated at：`2026-11-18T08:05:07.825955+00:00`。

---

## 可驗證資料來源

- **CVE-2026-115731** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115731) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-115731) · [Vendor / Advisory (portal.perforce.com)](https://portal.perforce.com/s/cve/a91Qi000003IaHpIAK/report-deserialization-code-execution) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-130603** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130603)
- **CVE-2026-97698** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97698)
- **CVE-2026-130627** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130627)
- **CVE-2026-130626** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130626)
- **CVE-2026-130591** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130591)
- **CVE-2026-119726** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119726)
- **CVE-2026-110782** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110782)
- **CVE-2026-91618** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91618)
- **CVE-2026-91585** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91585)
- **CVE-2026-91583** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91583)
- **CVE-2026-91570** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91570)
- **CVE-2026-91569** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91569)
- **CVE-2026-91561** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91561)
- **CVE-2026-91510** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91510)
- **CVE-2026-91507** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91507)
- **CVE-2026-91500** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91500)
- **CVE-2026-91470** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91470)
- **CVE-2026-91469** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91469)
- **CVE-2026-91456** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91456)
- **CVE-2026-69157** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69157)
- **CVE-2026-61680** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61680)
- **CVE-2026-61677** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61677)
- **CVE-2026-61676** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61676)
- **CVE-2026-61675** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61675)
- **CVE-2026-28273** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-28273)
- **CVE-2026-131852** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131852)
- **CVE-2026-131088** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131088)
- **CVE-2026-131077** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131077)
- **CVE-2026-131061** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131061)
- **CVE-2026-131057** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131057)
- **CVE-2026-131054** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131054)
- **CVE-2026-131031** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131031)
- **CVE-2026-131025** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131025)
- **CVE-2026-130996** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130996)
- **CVE-2026-130994** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130994)
- **CVE-2026-130971** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130971)
- **CVE-2026-130910** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130910)
- **CVE-2026-130870** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130870)
- **CVE-2026-130868** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130868)
- **CVE-2026-130856** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130856)
- **CVE-2026-130849** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130849)
- **CVE-2026-130840** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130840)
- **CVE-2026-130838** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130838)
- **CVE-2026-130802** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130802)
- **CVE-2026-130801** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130801)
- **CVE-2026-130587** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130587)
- **CVE-2026-130583** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130583)
- **CVE-2026-129448** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129448)
- **CVE-2026-129286** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129286)
- **CVE-2026-129280** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129280)
- **CVE-2026-129272** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129272)
- **CVE-2026-127369** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127369)
- **CVE-2026-127362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127362)
- **CVE-2026-127327** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127327)
- **CVE-2026-127326** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127326)
- **CVE-2026-127325** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127325)
- **CVE-2026-127324** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127324)
- **CVE-2026-126969** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126969)
- **CVE-2026-126574** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126574)
- **CVE-2026-126553** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126553)
- **CVE-2026-126552** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126552)
- **CVE-2026-126551** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126551)
- **CVE-2026-122150** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122150)
- **CVE-2026-122149** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122149)
- **CVE-2026-122147** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122147)
- **CVE-2026-122142** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122142)
- **CVE-2026-122122** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122122)
- **CVE-2026-122055** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122055)
- **CVE-2026-119623** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119623)
- **CVE-2026-119293** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119293)
- **CVE-2026-115139** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115139)
- **CVE-2026-115089** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115089)
- **CVE-2026-115086** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115086)
- **CVE-2026-115080** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115080)
- **CVE-2026-115050** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115050)
- **CVE-2026-115048** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115048)
- **CVE-2026-115047** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115047)
- **CVE-2026-114980** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114980)
- **CVE-2026-114978** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114978)
- **CVE-2026-114956** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114956)
- **CVE-2026-114952** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114952)
- **CVE-2026-114934** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114934)
- **CVE-2026-114925** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114925)
- **CVE-2026-114924** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114924)
- **CVE-2026-114881** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114881)
- **CVE-2026-114880** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114880)
- **CVE-2026-114863** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114863)
- **CVE-2026-114862** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114862)
- **CVE-2026-114856** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114856)
- **CVE-2026-114850** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114850)
- **CVE-2026-114849** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114849)
- **CVE-2026-114848** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114848)
- **CVE-2026-114847** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114847)
- **CVE-2026-114835** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114835)
- **CVE-2026-114826** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114826)
- **CVE-2026-114824** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114824)
- **CVE-2026-114822** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114822)
- **CVE-2026-114819** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114819)
- **CVE-2026-114785** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114785)
- **CVE-2026-114784** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114784)
- **CVE-2026-114205** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114205)
- **CVE-2026-114204** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114204)
- **CVE-2026-114202** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114202)
- **CVE-2026-101691** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101691)
- **CVE-2026-100397** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100397)
- **CVE-2025-62165** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-62165)
- **CVE-2026-95849** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95849)
- **CVE-2026-130794** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130794)
- **CVE-2026-130633** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130633)
- **CVE-2026-130592** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130592)
- **CVE-2024-43361** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-43361)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
