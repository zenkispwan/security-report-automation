# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**101** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=3、NEW_CVE=97、NEW_KEV=1。
- Intelligence 候選：**30** 筆；P1 **1**、P2 **0**、P3 **2**、WATCH **27**。
- Baseline：state / generated_at=2026-09-29T06:25:15.443632+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-86950。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **101** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-86950｜Apple / Multiple Products
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00812 / percentile=0.55295
- **CISA KEV**：listed=true / date_added=2026-09-29 / due_date=2026-10-02
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-28T20:17:11.193 / 2026-09-30T04:18:33.497
- **官方描述（原文）**：Apple iOS, macOS, and iPadOS contain an out-of-bounds write vulnerability in CoreGraphics that may lead to arbitrary code execution.

### 2. CVE-2026-77177｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T16:17:11.363)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T16:17:11.363 / 2026-09-29T20:17:26.403
- **官方描述（原文）**：Open GenAI Stack (aka ogx-ai) 2026-06-11, as used in the Meta AI backend for WhatsApp and other products, allows code execution because prompt injection (with Jinja2 template syntax) can be used to achieve server-side expression evaluation without sanitization.

### 3. CVE-2026-39117｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:20.130)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:20.130 / 2026-09-29T21:28:02.477
- **官方描述（原文）**：An issue in AltumCode 66Uptime before v.54.0.0 and 66Uptime ping-servers plugin before v.2.0.0 allows a remote attacker to execute arbitrary code via the index.php

### 4. CVE-2026-95389｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:15.010)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.00392 / percentile=0.30703
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:15.010 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：SCTP protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 5. CVE-2026-95387｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:14.713)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：0.00454 / percentile=0.36922
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:14.713 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：SPDY protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 6. CVE-2026-102878｜hangwin / mcp-chrome-bridge
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:18.620)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:18.620 / 2026-09-29T21:17:18.297
- **官方描述（原文）**：mcp-chrome-bridge through 1.0.31 contains an origin validation error in the native-server HTTP API that allows attackers to bypass CORS restrictions. Attackers can craft malicious web pages that make cross-origin requests to the local server and invoke browser automation tools including script execution, page content reading, and screenshot capture.

### 7. CVE-2026-102826｜steveukx / git-js
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T19:17:24.883)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T19:17:24.883 / 2026-09-29T20:17:17.797
- **官方描述（原文）**：simple-git, an interface for running git commands in any node.js application, enables applications to execute Git operations from JavaScript. Prior to 4.0.0, the default blockUnsafeOperationsPlugin does not completely reject configuration includes supplied through customArgs to git.clone(). The missing include.path classification permits Git to load an attacker-controlled configuration file, and the initial remediation does not cover includeIf.<condition>.path, allowing the same file-loading primitive through a conditional include. A loaded configuration can set an executable Git option such as core.sshCommand, which Git invokes during the clone operation with the privileges of the Node.js process. Exploitation requires the application to pass attacker-influenced custom arguments and requires an attacker-controlled file that the process can read. This issue is fixed in 4.0.0.

### 8. CVE-2026-102809｜PX4 / PX4-Autopilot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:14.220)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:14.220 / 2026-09-29T19:17:23.657
- **官方描述（原文）**：PX4 Autopilot through 1.17.0 contains an uncontrolled stack allocation vulnerability in the file2 test command that fails to validate the write chunk size parameter. Attackers with shell access can supply an excessively large value to the -c option to trigger stack overflow and crash the flight controller.

### 9. CVE-2026-102634｜sgl-project / sglang
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T17:17:07.147)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T17:17:07.147 / 2026-09-29T18:17:09.033
- **官方描述（原文）**：SGLang through 0.5.20 in prefill/decode disaggregation mode fails to validate duplicate bootstrap_room fields in /generate requests with Mooncake KV transfer backend. Unauthenticated attackers can send concurrent requests with identical bootstrap_room values to crash scheduler processes or hang other users' requests until transfer timeout.

### 10. CVE-2026-102570｜MacWarrior / clipbucket-v5
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T15:17:18.917)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.0 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T15:17:18.917 / 2026-09-29T15:17:18.917
- **官方描述（原文）**：ClipBucket v5 through 5.5.3-#197 contains a time-based blind SQL injection vulnerability in the language update function where the language_id parameter is concatenated unescaped into the WHERE clause of an UPDATE statement. An authenticated administrator with basic_settings permission can inject arbitrary SQL payloads to extract or modify database contents.

### 11. CVE-2026-102360｜dmonad / lib0
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T14:17:20.117)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T14:17:20.117 / 2026-09-29T14:17:20.117
- **官方描述（原文）**：A missing bounds check in the binary decoder in lib0, versions 0.2.1-0.2.117 and earlier and 1.0.0-rc.32 and earlier, lets any unauthenticated remote peer read adjacent process memory and receive it back. `readUint8Array` never compares the wire-supplied length against the decoder's own view, so one over-long length prefix returns whatever the host process allocated next: other tenants' document content, personal data, and live bearer session tokens**, recovered in full and at will. An attacker who can supply bytes to a lib0 decoder which means any peer that can open a socket, including before authentication reads adjacent process memory and, where the consumer echoes, stores or re-serves the decoded value, receives it back. This is patched in version 0.2.118 and 1.0.0-rc.33.

### 12. CVE-2015-20122｜Yonyou / A6 OA
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T15:17:11.023)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T15:17:11.023 / 2026-09-29T17:17:00.423
- **官方描述（原文）**：Seeyon A6 collaborative office automation platform contains an unauthenticated SQL injection vulnerability in the attach_ids parameter of the file attachment download endpoint that allows remote attackers to extract arbitrary database contents without prior authentication. Attackers can inject UNION-based SQL statements through the attach_ids request parameter in downloadAtt.jsp to retrieve sensitive information including credentials and system configuration data. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-17.

### 13. CVE-2026-96587｜Viidure / Dashcam Android Application
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T21:19:39.987)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T21:19:39.987 / 2026-09-29T22:19:05.860
- **官方描述（原文）**：The Viidure Android application embeds permanent, plaintext cloud storage credentials within its compiled code. These credentials provide full access to critical platform storage, including the ability to read, modify, or delete operational files such as firmware and application binaries.

### 14. CVE-2026-96431｜Flowring Technology Corp / Agentflow 4.0
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T09:17:11.183)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00275 / percentile=0.17883
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T09:17:11.183 / 2026-09-29T21:33:56.530
- **官方描述（原文）**：Unrestricted Upload of File with Dangerous Type in the /WebAgenda/download/uploadFile.jsp API endpoint of Flowring Agentflow 4.0 version before 2023/03/24 allows remote authenticated users to execute arbitrary system commands via a malicious file.

### 15. CVE-2026-96429｜Flowring Technology Corp / Agentflow 4.0
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T09:17:10.917)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00277 / percentile=0.18132
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T09:17:10.917 / 2026-09-29T21:33:56.530
- **官方描述（原文）**：SQL Injection in the /WebAgenda/SMBAjaxConfigProcess.do API endpoint of Flowring Agentflow 4.0 version before 2025/08/08 allows remote attackers to execute arbitrary SQL commands via the id parameter.

### 16. CVE-2026-96428｜Flowring Technology Corp / Agentflow 4.0
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T09:17:10.687)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00342 / percentile=0.25173
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T09:17:10.687 / 2026-09-29T21:33:56.530
- **官方描述（原文）**：SQL Injection in the /WebAgenda/SMBAjaxAutoComplete.do API endpoint of Flowring Agentflow 4.0 version before 2025/08/08 allows remote attackers to execute arbitrary SQL commands via the words parameter.

### 17. CVE-2026-95357｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:28.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:28.760 / 2026-09-30T04:18:48.873
- **官方描述（原文）**：Out of bounds write in GPU in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 18. CVE-2026-95356｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:28.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:28.647 / 2026-09-30T04:18:48.677
- **官方描述（原文）**：Use after free in WindowDialog in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 19. CVE-2026-95350｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:27.920)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:27.920 / 2026-09-30T04:18:47.487
- **官方描述（原文）**：Buffer overflow in ANGLE in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 20. CVE-2026-95349｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:27.807)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:27.807 / 2026-09-30T04:18:47.287
- **官方描述（原文）**：Buffer overflow in WebGL in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 21. CVE-2026-95347｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:27.580)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:27.580 / 2026-09-30T04:18:46.903
- **官方描述（原文）**：Use after free in Updater in Google Chrome on on Mac prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code outside the sandbox via crafted network traffic. (Chromium security severity: Medium)

### 22. CVE-2026-95339｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:26.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:26.480 / 2026-09-30T04:18:45.760
- **官方描述（原文）**：Use after free in ServiceWorker in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 23. CVE-2026-95331｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:25.563)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:25.563 / 2026-09-30T04:18:44.847
- **官方描述（原文）**：Out of bounds write in ANGLE in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 24. CVE-2026-95329｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:25.330)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:25.330 / 2026-09-30T04:18:44.677
- **官方描述（原文）**：Out of bounds write in WebGL in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 25. CVE-2026-95325｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:24.873)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:24.873 / 2026-09-30T04:18:44.313
- **官方描述（原文）**：Use after free in ANGLE in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 26. CVE-2026-95318｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:24.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:24.060 / 2026-09-30T04:18:42.847
- **官方描述（原文）**：Buffer overflow in Video in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 27. CVE-2026-95313｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:23.463)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:23.463 / 2026-09-30T04:18:42.443
- **官方描述（原文）**：Use after free in Fullscreen in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 28. CVE-2026-95311｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:23.227)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:23.227 / 2026-09-30T04:18:41.493
- **官方描述（原文）**：Free of non-heap memory in Fonts in Google Chrome prior to 154.0.8037.57 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)

### 29. CVE-2026-95310｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:23.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:23.110 / 2026-09-30T04:18:41.337
- **官方描述（原文）**：Use after free in AdFilter in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 30. CVE-2026-95299｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:21.837)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:21.837 / 2026-09-30T04:18:40.683
- **官方描述（原文）**：Use after free in GPU in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 31. CVE-2026-95283｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:19.733)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:19.733 / 2026-09-30T04:18:39.620
- **官方描述（原文）**：Buffer overflow in Tint in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 32. CVE-2026-95281｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:19.507)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:19.507 / 2026-09-30T04:18:38.837
- **官方描述（原文）**：Buffer overflow in ANGLE in Google Chrome on on Android prior to 154.0.8037.57 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 33. CVE-2026-95277｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:19.037)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:19.037 / 2026-09-30T04:18:38.283
- **官方描述（原文）**：Use after free in Views in Google Chrome prior to 154.0.8037.57 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 34. CVE-2026-86131｜WatchGuard / Fireware OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T00:16:36.817)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T00:16:36.817 / 2026-09-30T00:16:36.817
- **官方描述（原文）**：A code injection vulnerability in WatchGuard Fireware OS's BOVPN Over TLS client configuration handling allows an attacker who controls the remote VPN server to execute arbitrary commands as root on the connecting Firebox.

### 35. CVE-2026-85520｜MyPresta / Google Merchant Center Feed
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T12:17:12.283)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T12:17:12.283 / 2026-09-29T15:17:30.297
- **官方描述（原文）**：Google Merchant Center Feed (gmfeed) module for PrestaShop is vulnerable to unauthenticated arbitrary file write in the feed.php endpoint. An unauthenticated attacker can send a crafted request that controls the output file name, path, extension, and content through request parameters. Due to the lack of authentication and input validation, the request is processed successfully, allowing an attacker to write and execute arbitrary PHP code, resulting in remote code execution (RCE). This issue was fixed in version 2.3.9.

### 36. CVE-2026-84436｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:17.823)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:17.823 / 2026-09-30T04:18:33.010
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is vulnerable to command injection in the certificate export CLI functionality, allowing a privileged authenticated CLI user to execute arbitrary commands with root privileges.

### 37. CVE-2026-84154｜Dassault Systèmes / GEOVIA Geospatial Data Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T08:17:21.297)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00355 / percentile=0.26699
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T08:17:21.297 / 2026-09-29T17:17:10.507
- **官方描述（原文）**：A Code Injection vulnerability affecting GEOVIA Geospatial Data Manager from Release 3DEXPERIENCE R2024x through Release 3DEXPERIENCE R2026x could allow an attacker to execute arbitrary code on the server.

### 38. CVE-2026-82973｜psyb0t / docker-mailbox
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:52.963)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:52.963 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：Improper neutralization of CRLF sequences in IMAP command construction in psyb0t/docker-mailbox before 0.4.13 allows a remote unauthenticated attacker, when bearer-token authentication is not configured, to inject additional IMAP commands into an authenticated upstream mailbox connection via crafted folder, UID, or search values.

### 39. CVE-2026-8066｜Hitachi Energy / RTU500 series CMU firmware
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:13.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.01157 / percentile=0.658
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:13.250 / 2026-09-29T21:39:02.570
- **官方描述（原文）**：A directory traversal vulnerability in the file upload functionality of Hitachi Energy RTU500 end-of-life versions allows an unauthenticated attacker to write or overwrite arbitrary files on the device file system. Depending on the files affected, successful exploitation could result in unauthorized modification of device data or disruption of the device’s intended operation.

### 40. CVE-2026-8065｜Hitachi Energy / RTU500 series CMU firmware
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:13.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00577 / percentile=0.45384
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:13.110 / 2026-09-29T21:39:02.570
- **官方描述（原文）**：An authentication bypass vulnerability in the firmware update endpoint of Hitachi Energy RTU500 end-of-life versions allows an unauthenticated attacker to upload arbitrary firmware through a crafted POST request. Successful exploitation could allow the attacker to modify device functionality or compromise the integrity or availability of the device.

### 41. CVE-2026-79538｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:27.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:27.510 / 2026-09-29T21:28:02.477
- **官方描述（原文）**：metatool-ai MetaMCP up to and including 2.4.22 is vulnerable to Code Execution in the internal MCP inspector proxy endpoint GET /mcp-proxy/server/stdio (createTransport, STDIO branch, routers/mcp-proxy/server.ts).

### 42. CVE-2026-76725｜Hewlett Packard Enterprise (HPE) / Instant ON
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:24.580)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:24.580 / 2026-09-29T21:39:02.570
- **官方描述（原文）**：A vulnerability has been identified in a management protocol of HPE Networking Instant ON APs that could allow an unauthenticated adjacent attacker to circumvent existing authentication controls. Successful exploitation could result in a complete bypass of security restrictions, potentially leading to remote code execution with elevated privileges.

### 43. CVE-2026-76724｜Hewlett Packard Enterprise (HPE) / Instant ON
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:24.453)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:24.453 / 2026-09-29T21:39:02.570
- **官方描述（原文）**：A command injection vulnerability exists in CLI of the affected HPE Networking Instant ON APs that could allow an unauthenticated adjacent attacker to perform command injection by sending specially crafted packets. Successful exploitation could allow an attacker to execute arbitrary commands as a privileged user on the underlying operating system.

### 44. CVE-2026-76723｜Hewlett Packard Enterprise (HPE) / Instant ON
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:24.327)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:24.327 / 2026-09-29T21:39:02.570
- **官方描述（原文）**：Buffer overflow vulnerabilities exist in the affected interface of HPE Networking Instant ON APS that could allow an unauthenticated adjacent attacker to achieve remote code execution. Successful exploitation could allow an attacker to execute arbitrary commands on the underlying operating system.

### 45. CVE-2026-76722｜Hewlett Packard Enterprise (HPE) / Instant ON
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:24.207)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:24.207 / 2026-09-29T21:39:02.570
- **官方描述（原文）**：Uncontrolled Format string vulnerabilities exist in the affected interface of HPE Networking Instant ON APs that could allow an unauthenticated remote attacker to run arbitrary commands on the underlying host. Successful exploitation could result in a Denial-of-service or potential remote code execution.

### 46. CVE-2026-76721｜Hewlett Packard Enterprise (HPE) / Instant ON
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:24.073)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:24.073 / 2026-09-29T21:39:02.570
- **官方描述（原文）**：Buffer overflow vulnerability exists in the affected interface of HPE Networking Instant ON that could allow an unauthenticated remote attacker to run arbitrary code on the underlying host. Successful exploitation could allow an attacker to execute arbitrary code as a privileged user on the underlying operating system.

### 47. CVE-2026-7192｜Shenzhen Dbit Network Equipment / T-CPE301K 4G Mini WiFi Router
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:52.447)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:52.447 / 2026-09-29T21:35:31.350
- **官方描述（原文）**：A stack-based buffer overflow vulnerability in the Dbit T-CPE301K 4G WiFi minirouter allows an authenticated attacker to cause a denial of service (DoS) and a system reboot via a manipulated HTTP POST request directed at the endpoint ‘/js/common/do_cmd.js’ endpoint containing an excessively long parameter, which overwrites the PC and RA registers.

### 48. CVE-2026-71379｜Toptech Systems / TMS7
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T22:18:21.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T22:18:21.560 / 2026-09-29T22:18:21.560
- **官方描述（原文）**：The file export endpoint allows any unauthenticated attacker to export arbitrary database tables by sending a crafted POST request.

### 49. CVE-2026-70356｜Toptech Systems / TMS7
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T22:18:16.140)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T22:18:16.140 / 2026-09-29T22:18:16.140
- **官方描述（原文）**：The TMS file upload endpoint fails to enforce server-side file type restrictions, allowing an attacker to upload and execute arbitrary PHP files on the web server.

### 50. CVE-2026-53988｜Finsys / dockhand
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:20.403)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:20.403 / 2026-09-29T20:17:20.403
- **官方描述（原文）**：Dockhand before 1.0.40 contains an authentication bypass vulnerability in its git webhook endpoints that allows unauthenticated remote attackers to trigger arbitrary stack redeployments by exploiting a null webhook secret guard condition. Attackers can enumerate sequential stack IDs and send unsigned webhook requests to force git clone and docker compose operations, enabling denial of service or, when combined with write access to the tracked git branch, container escape and full host compromise via attacker-controlled docker-compose.yml with privileged bind mounts.

### 51. CVE-2026-22094｜EVbee / DC 80
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T15:17:21.453)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T15:17:21.453 / 2026-09-29T19:00:37.883
- **官方描述（原文）**：The firmware for the EVbee DC-80 has a weak hardcoded root password, which allows attackers to login as root using the SSH daemon that is exposed to the network.

### 52. CVE-2026-15390｜DENX Software Engineering / Das U-Boot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:11.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:11.237 / 2026-09-29T11:16:42.610
- **官方描述（原文）**：Das U-Boot with CONFIG_IP_DEFRAG=y parameter fails to clear IP reassembly state after delivering a complete datagram. An attacker who can deliver fragmented IP traffic can execute arbitrary code by sending duplicated last-fragment IP packets. This issue was fixed in commit b1aec609bb5e0d08c25c888c91935287ab4ee5fa in version 2026.07.

### 53. CVE-2026-103110｜Pexip / Infinity
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T04:18:29.077)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T04:18:29.077 / 2026-09-30T04:18:29.077
- **官方描述（原文）**：Pexip Infinity before 38.2, plus 39.0, 39.1 and 40.0, is affected by improper input validation that allows a remote attacker to execute code remotely as an unprivileged user on a Pexip Infinity Conferencing Node.

### 54. CVE-2026-103056｜beenuar / AiSOC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-30T01:16:37.050)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-30T01:16:37.050 / 2026-09-30T01:16:37.050
- **官方描述（原文）**：AiSOC versions 7.2.0 before 12.0.0 contain a command injection vulnerability in the actions service that builds CrowdStrike Real Time Response command strings by interpolating unescaped action parameters in crowdstrike_rtr.py and endpoint.py. Authenticated users can inject single quotes into file_path, path, script_name, or script_args parameters to break out of quoted arguments and execute arbitrary commands on managed endpoints with SYSTEM or root privileges.

### 55. CVE-2026-103041｜ModelTC / LightLLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T23:17:21.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T23:17:21.630 / 2026-09-29T23:17:21.760
- **官方描述（原文）**：LightLLM through 1.2.0 multimodal deployments expose an unauthenticated RPyC cache service with pickle deserialization enabled on all interfaces. Attackers can send crafted serialized objects to exposed cache methods to execute arbitrary code with service privileges.

### 56. CVE-2026-103040｜ModelTC / LightLLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T23:17:21.447)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T23:17:21.447 / 2026-09-29T23:17:21.573
- **官方描述（原文）**：LightLLM through 1.2.0 contains a remote code execution vulnerability in the router profiler service when started with --enable_profiling flag. The service exposes an unauthenticated RPyC server with pickle deserialization enabled, allowing attackers to execute arbitrary code by sending crafted serialized objects to the profiler command queue.

### 57. CVE-2026-102829｜steveukx / git-js
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T19:17:25.367)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T19:17:25.367 / 2026-09-29T19:17:25.367
- **官方描述（原文）**：simple-git, an interface for running git commands in any node.js application, enables applications to execute Git operations from JavaScript. Prior to 2.0.1 of the argv-parser package, parseEnv omits VISUAL from GitEnvKeys, so prepareEnv drops the value before vulnerabilityCheck can classify it as allowUnsafeEditor. A consuming application that forwards attacker-influenced environment values can therefore allow Git to invoke an attacker-selected editor during operations such as commit amendment or interactive rebase when no higher-priority editor setting overrides VISUAL and Git's terminal prerequisites are met. The executable runs with the privileges of the Node.js process. This issue is fixed in argv-parser 2.0.1.

### 58. CVE-2026-102828｜steveukx / git-js
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T19:17:25.207)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T19:17:25.207 / 2026-09-29T19:17:25.207
- **官方描述（原文）**：simple-git, an interface for running git commands in any node.js application, enables applications to execute Git operations from JavaScript. From 3.15.0 until 4.0.1, the default blockUnsafeOperationsPlugin does not classify trailer.<token>.cmd as unsafe configuration. An application that passes attacker-controlled values through SimpleGitOptions.config or inline -c arguments can therefore allow Git to invoke an attacker-selected shell command when git interpret-trailers processes the configured trailer. The command executes with the operating-system identity and permissions of the Node.js process. This issue is fixed in 4.0.1.

### 59. CVE-2026-102761｜Eclipse Foundation / NetX Duo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:13.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:13.450 / 2026-09-29T19:00:16.623
- **官方描述（原文）**：NetX Duo's WebSocket client resets the unmasking cursor to the first `NX_PACKET` each time it advances through a chained packet, while the loop's upper bound belongs to the current packet. With the standard contiguous packet-pool layout, a masked server frame split across two packets therefore drives the XOR loop through the first packet's unused payload area and on through the second packet's `NX_PACKET` control block. The four-byte WebSocket masking key controls the bytes written, so the corruption is attacker-chosen rather than incidental.

### 60. CVE-2026-102710｜Eclipse Foundation / eclipse-threadx/threadx
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T18:17:10.020)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T18:17:10.020 / 2026-09-29T19:00:16.623
- **官方描述（原文）**：Attacker model / Preconditions: a loaded `TXM_MODULE_USER_MODE | TXM_MODULE_MEMORY_PROTECTION` module issuing kernel dispatch calls, on a build with `TX_ENABLE_EVENT_TRACE`. A user-mode, memory-protected module can register an arbitrary function pointer as the global trace-full callback. The kernel calls it directly — no validation, no trampoline — from privileged kernel code when the trace buffer wraps. An invalid pointer faults the kernel (DoS). A pointer into the module's own code was observed running with kernel privilege (`CONTROL.nPRIV = 0`), confirmed at runtime with a register capture inside that code.

### 61. CVE-2026-102425｜balbooa.com / Balbooa Forms extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T17:17:06.210)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T17:17:06.210 / 2026-09-29T21:39:02.570
- **官方描述（原文）**：Joomla Extension - balbooa.com - Unauthenticated RCE via field shortcode injection in Balbooa Forms < 2.4.3.4 - Balbooa Forms supports administrator-defined PHP code which runs after a public form submission. The feature also supports form-field shortcodes inside that PHP. Before calling `eval()`, the component replaces each shortcode with the raw value submitted by the visitor, leading to an RCE vector. A public form must use the product's optional PHP-after-submission action and interpolate an attacker-controlled field shortcode inside a double-quoted PHP string to be vulnerable.

### 62. CVE-2026-102331｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:16.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:16.587 / 2026-09-30T04:18:27.317
- **官方描述（原文）**：Buffer overflow in ANGLE in Google Chrome on on Android prior to 154.0.8037.92 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)

### 63. CVE-2026-102316｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:14.787)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:14.787 / 2026-09-30T04:18:24.230
- **官方描述（原文）**：Use after free in Views in Google Chrome prior to 154.0.8037.92 allowed a remote attacker leveraging social engineering to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 64. CVE-2026-102309｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:13.933)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:13.933 / 2026-09-30T04:18:23.983
- **官方描述（原文）**：Use after free in FullScreen in Google Chrome prior to 154.0.8037.92 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 65. CVE-2026-102308｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:13.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:13.810 / 2026-09-30T04:18:23.777
- **官方描述（原文）**：Use after free in Views in Google Chrome prior to 154.0.8037.92 allowed a remote attacker leveraging social engineering to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 66. CVE-2026-102306｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:13.573)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:13.573 / 2026-09-30T04:18:23.513
- **官方描述（原文）**：Use after free in Bluetooth in Google Chrome prior to 154.0.8037.92 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 67. CVE-2026-102304｜Google / Chrome
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:13.327)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:13.327 / 2026-09-30T04:18:23.210
- **官方描述（原文）**：Use after free in Passwords in Google Chrome prior to 154.0.8037.92 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)

### 68. CVE-2026-100819｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:47.193)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:47.193 / 2026-09-30T04:18:19.200
- **官方描述（原文）**：Sandbox escape due to incorrect boundary conditions in the XPCOM component. This vulnerability was fixed in Firefox ESR 153.4, Firefox 157, Firefox ESR 115.42, and Firefox ESR 140.17.

### 69. CVE-2026-100818｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:47.037)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:47.037 / 2026-09-29T21:27:41.130
- **官方描述（原文）**：Sandbox escape due to use-after-free in the Widget: Gtk component. This vulnerability was fixed in Firefox ESR 153.4, Firefox 157, and Firefox ESR 140.17.

### 70. CVE-2026-100811｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:46.230)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:46.230 / 2026-09-30T04:18:16.847
- **官方描述（原文）**：Sandbox escape due to use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox ESR 153.4, Firefox 157, and Firefox ESR 140.17.

### 71. CVE-2026-100804｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:45.493)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:45.493 / 2026-09-30T04:18:14.320
- **官方描述（原文）**：Sandbox escape due to use-after-free in the Preferences: Backend component. This vulnerability was fixed in Firefox 157.

### 72. CVE-2026-100800｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:45.073)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:45.073 / 2026-09-30T04:18:13.863
- **官方描述（原文）**：Sandbox escape due to use-after-free in the Disability Access APIs component. This vulnerability was fixed in Firefox ESR 153.4 and Firefox 157.

### 73. CVE-2026-100786｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:43.583)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:43.583 / 2026-09-29T21:27:41.130
- **官方描述（原文）**：Sandbox escape due to use-after-free in the Graphics component. This vulnerability was fixed in Firefox ESR 153.4, Firefox 157, Firefox ESR 115.42, and Firefox ESR 140.17.

### 74. CVE-2026-100778｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:42.577)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:42.577 / 2026-09-29T21:27:41.130
- **官方描述（原文）**：Sandbox escape due to use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox ESR 153.4, Firefox 157, Firefox ESR 115.42, and Firefox ESR 140.17.

### 75. CVE-2026-100770｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:41.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:41.250 / 2026-09-29T21:27:41.130
- **官方描述（原文）**：Sandbox escape due to use-after-free in the DOM: Content Processes component. This vulnerability was fixed in Firefox ESR 153.4, Firefox 157, Firefox ESR 115.42, and Firefox ESR 140.17.

### 76. CVE-2026-100762｜Mozilla / Firefox
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T13:17:40.470)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T13:17:40.470 / 2026-09-29T21:27:41.130
- **官方描述（原文）**：Sandbox escape due to use-after-free in the DOM: Content Processes component. This vulnerability was fixed in Firefox ESR 153.4, Firefox 157, Firefox ESR 115.42, and Firefox ESR 140.17.

### 77. CVE-2026-100291｜Anjvision / YSSD-RTMP-H5
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T20:17:09.300)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T20:17:09.300 / 2026-09-29T22:17:04.057
- **官方描述（原文）**：In Anjvision YSSD‑RTMP‑H5 firmware version 3.3.2.4, several ONVIF service endpoints process management requests without enforcing required authentication. This could allow an unauthorized attacker to access sensitive device operations.

### 78. CVE-2023-54400｜Fumasoft / Fumeng Cloud
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T16:17:04.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T16:17:04.070 / 2026-09-29T16:17:04.070
- **官方描述（原文）**：Fumasoft Fumeng Cloud contains a SQL injection vulnerability in the AjaxMethod.ashx endpoint that allows unauthenticated remote attackers to inject arbitrary SQL through the Name parameter of the getEmpByname action without any authentication. Attackers can exploit UNION-based SQL injection techniques against the Microsoft SQL Server backend to extract, disclose, and modify database contents, with potential for further compromise of the underlying server. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-18.

### 79. CVE-2026-96423｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:17.220)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00134 / percentile=0.02428
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:17.220 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：X11 protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 80. CVE-2026-96422｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:17.077)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00134 / percentile=0.02428
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:17.077 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：Frame protocol metadissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 81. CVE-2026-96421｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:16.930)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00134 / percentile=0.02428
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:16.930 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：USB HID protocol dissector infinite loop and memory leak in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 82. CVE-2026-96419｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:16.640)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00187 / percentile=0.0741
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:16.640 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：Profile import crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service and possible code execution

### 83. CVE-2026-96418｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:16.500)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.0014 / percentile=0.02799
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:16.500 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：TIFF protocol dissector infinite loop in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 84. CVE-2026-96416｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:16.200)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.0014 / percentile=0.02799
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:16.200 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：IEEE 802.11 protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 85. CVE-2026-96415｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:16.047)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.0014 / percentile=0.028
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:16.047 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：Catapult DCT2000 protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 86. CVE-2026-95395｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:15.900)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00141 / percentile=0.02811
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:15.900 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：IEEE C37.118 Synchrophasor protocol dissector memory leak in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 87. CVE-2026-95394｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:15.757)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.7 (MEDIUM)
- **EPSS**：0.00136 / percentile=0.02531
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:15.757 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：Microsoft Network Monitor file parser large loop in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 88. CVE-2026-95393｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:15.610)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.7 (MEDIUM)
- **EPSS**：0.00128 / percentile=0.02056
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:15.610 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：CSN.1 protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 89. CVE-2026-95392｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:15.457)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00159 / percentile=0.04295
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:15.457 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：MBIM protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 90. CVE-2026-95390｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:15.160)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00141 / percentile=0.02811
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:15.160 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：PEAK CAN TRC file parser crash in 4.6.0 to 4.6.8 allows denial of service

### 91. CVE-2026-95388｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:14.867)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.0014 / percentile=0.028
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:14.867 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：Sharkd utility crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service

### 92. CVE-2026-95386｜Wireshark Foundation / Wireshark
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T10:17:14.560)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00141 / percentile=0.02811
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T10:17:14.560 / 2026-09-29T21:36:39.547
- **官方描述（原文）**：TTL file parser infinite loop in 4.6.0 to 4.6.8 allows denial of service

### 93. CVE-2026-102616｜risesoft-y9 / WorkFlow-Engine
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T19:17:19.703)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T19:17:19.703 / 2026-09-29T20:17:16.973
- **官方描述（原文）**：A vulnerability was detected in risesoft-y9 WorkFlow-Engine up to 9.6.10. Impacted is the function getByIdAndYear of the file CustomHistoricProcessServiceImpl.java of the component OAuth2 Resource Filter. Performing a manipulation of the argument year/processInstanceId results in sql injection. Remote exploitation of the attack is possible. The exploit is now public and may be used. The sink is injectable on two independent positions, not just one. The vendor was contacted early about this disclosure but did not respond in any way.

### 94. CVE-2026-102568｜pardus / pardus-parental-control
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T15:17:18.443)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T15:17:18.443 / 2026-09-29T18:17:08.903
- **官方描述（原文）**：Pardus Parental Control before 0.7.0 contains an incorrect authorization vulnerability in the polkit policy that allows unprivileged local users to disable parental controls as root. Attackers can invoke PPCActivator.py with the --disable argument via pkexec to remove all restrictions including DNS filtering and application limits without authentication.

### 95. CVE-2026-102507｜BishopFox / sliver
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T12:17:09.943)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T12:17:09.943 / 2026-09-29T18:17:07.853
- **官方描述（原文）**：Sliver C2 framework version 1.7.7 and earlier contains an unhandled panic vulnerability in the operator gRPC handler that allows an attacker controlling a compromised implant to crash the entire teamserver by returning a malformed or empty Download response. Attackers can send zero-length or 1-3 byte data payloads through a hostile implant session to trigger an out-of-bounds slice access in the vendored Binject library's BinaryMagic function, which propagates unrecovered through the operator gRPC interceptor chain and terminates the server process, affecting all connected operators.

### 96. CVE-2026-102491｜mahonelau / kykms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T15:17:17.813)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T15:17:17.813 / 2026-09-29T18:57:24.350
- **官方描述（原文）**：A vulnerability was identified in mahonelau kykms up to 8f130c2d85842d5b44caae78cc46d65e505949f7. The impacted element is the function QueryGenerator.doMultiFieldsOrder of the file QueryGenerator.java of the component SqlInjectionUtil. The manipulation of the argument column leads to sql injection. Remote exploitation of the attack is possible. The exploit is publicly available and might be used. This product follows a rolling release approach for continuous delivery, so version details for affected or updated releases are not provided. The vendor was contacted early about this disclosure but did not respond in any way.

### 97. CVE-2026-102822｜Eugeny / russh
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T19:17:24.190)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.7 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T19:17:24.190 / 2026-09-29T20:17:17.673
- **官方描述（原文）**：Russh is a Rust SSH client and server library. Prior to 0.63.1, a connection configured to permit mac=none can negotiate it with a MAC-requiring CTR or CBC block cipher because the selection logic validates needs_mac() only when MAC selection fails. A remote peer can then send a packet with a decrypted length of zero, causing russh/src/cipher/mod.rs to shrink the previously read block before indexing buffer.buffer[16..], which panics and terminates the connection task. This issue is fixed in version 0.63.1.

### 98. CVE-2026-102601｜thephpleague / flysystem
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T16:17:06.343)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.5 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T16:17:06.343 / 2026-09-29T16:17:06.343
- **官方描述（原文）**：Flysystem is an open source file storage library for PHP. Prior to 3.35.3, the default WhitespacePathNormalizer in src/WhitespacePathNormalizer.php used by Filesystem across adapters calls preg_match with the u modifier and treats both false and 0 as falsy. A path containing malformed UTF-8 causes PCRE to return false, so paths that also contain control characters bypass CorruptedPathDetected::forPath() in normalizePath(). Filesystem::write() can store such names and Filesystem::listContents() can return the raw ANSI escape sequences, allowing hidden or spoofed terminal file listings when an administrator displays them. This issue is fixed in version 3.35.3.

### 99. CVE-2026-77265｜sooperset / mcp-atlassian
- **Delta event**：CVSS_CHANGED (from=5.9; to=7.5)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：0.00261 / percentile=0.16056
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T18:17:18.647 / 2026-09-29T19:00:07.850
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, header-supplied Jira or Confluence URLs are resolved and validated before the HTTP client resolves the hostname again for the connection. An unauthenticated caller can use a DNS-rebinding hostname that returns a public address during validation and an internal address during connection, causing requests to internal or metadata services. The advisory traces the vulnerable input and processing flow through X-Atlassian-Jira-Url, X-Atlassian-Confluence-Url, validate_url_for_ssrf, and DNS rebinding, which identify the affected entry points, controls, and code paths. This issue is fixed in version 0.22.0.

### 100. CVE-2026-88420｜未確認 / 未確認
- **Delta event**：CVSS_CHANGED (from=6.1; to=5.4)
- **Risk**：WATCH / score 14；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：0.00178 / percentile=0.06638
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-25T13:17:16.787 / 2026-09-29T16:17:13.200
- **官方描述（原文）**：A reflected cross-site scripting (XSS) vulnerability in the EntryAbstract.save() component of APSL puput v1.2.1 through v2.2.0 allows authenticated attackers with Wagtail Editor privileges to execute arbitrary code in the context of the victim's browser via a crafted payload.

### 101. CVE-2026-63498｜grokability / snipe-it
- **Delta event**：CVSS_CHANGED (from=8.7; to=5.4)
- **Risk**：WATCH / score 14；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：0.00242 / percentile=0.13789
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T17:17:05.513 / 2026-09-29T16:50:21.113
- **官方描述（原文）**：Snipe-IT is an IT asset/license management system. Prior to 8.7.0, the uploaded-files API endpoint GET /api/v1/{object_type}/{id}/files/{file_id} allows an authenticated user with file-management access to upload XML and XSLT attachments and request them with the inline=true parameter. The app/Http/Controllers/Api/UploadedFilesController.php show() path does not apply the safe-inline allowlist used by the equivalent web controller, so the browser can process an attacker-controlled xml-stylesheet reference and execute JavaScript generated by the stylesheet in the Snipe-IT origin. A victim who is authorized to view the object must open the attachment URL, after which the script can read same-origin data and perform authenticated actions with the victim's privileges. This issue is fixed in version 8.7.0.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-86950｜Apple / Multiple Products
- **Title**：Apple Multiple Products Out-of-Bounds Write Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00812 / percentile=0.55295
- **CISA KEV**：listed=true / date_added=2026-09-29 / due_date=2026-10-02
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apple iOS, macOS, and iPadOS contain an out-of-bounds write vulnerability in CoreGraphics that may lead to arbitrary code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-77177 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-39117 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-95389 | WATCH / 30 | Wireshark Foundation / Wireshark | v3.1 8.1 (HIGH) | 0.00392 / percentile=0.30703 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-95387 | WATCH / 30 | Wireshark Foundation / Wireshark | v3.1 8.1 (HIGH) | 0.00454 / percentile=0.36922 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102878 | WATCH / 30 | hangwin / mcp-chrome-bridge | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102826 | WATCH / 30 | steveukx / git-js | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102809 | WATCH / 30 | PX4 / PX4-Autopilot | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102634 | WATCH / 30 | sgl-project / sglang | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102570 | WATCH / 30 | MacWarrior / clipbucket-v5 | v4.0 7.0 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102360 | WATCH / 30 | dmonad / lib0 | v3.1 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2015-20122 | WATCH / 30 | Yonyou / A6 OA | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-96587 | WATCH / 28 | Viidure / Dashcam Android Application | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96431 | WATCH / 28 | Flowring Technology Corp / Agentflow 4.0 | v4.0 9.3 (CRITICAL) | 0.00275 / percentile=0.17883 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96429 | WATCH / 28 | Flowring Technology Corp / Agentflow 4.0 | v4.0 9.3 (CRITICAL) | 0.00277 / percentile=0.18132 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96428 | WATCH / 28 | Flowring Technology Corp / Agentflow 4.0 | v4.0 9.3 (CRITICAL) | 0.00342 / percentile=0.25173 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95357 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95356 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95350 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95349 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95347 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95339 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95331 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95329 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95325 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95318 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95313 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95311 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95310 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95299 | WATCH / 28 | Google / Chrome | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：2；缺少 Product：2；缺少 Title：29。
- EPSS 未確認：24；Exploitation status 未確認：0。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-30T06:11:13.755032+00:00`；Delta generated at：`2026-09-30T06:11:13.755032+00:00`。

---

## 可驗證資料來源

- **CVE-2026-86950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86950) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86950) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149226) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149228) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149229) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-77177** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77177)
- **CVE-2026-39117** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-39117)
- **CVE-2026-95389** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95389) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95389)
- **CVE-2026-95387** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95387) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95387)
- **CVE-2026-102878** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102878)
- **CVE-2026-102826** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102826)
- **CVE-2026-102809** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102809)
- **CVE-2026-102634** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102634)
- **CVE-2026-102570** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102570)
- **CVE-2026-102360** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102360)
- **CVE-2015-20122** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2015-20122)
- **CVE-2026-96587** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96587)
- **CVE-2026-96431** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96431) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96431)
- **CVE-2026-96429** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96429) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96429)
- **CVE-2026-96428** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96428) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96428)
- **CVE-2026-95357** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95357)
- **CVE-2026-95356** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95356)
- **CVE-2026-95350** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95350)
- **CVE-2026-95349** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95349)
- **CVE-2026-95347** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95347)
- **CVE-2026-95339** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95339)
- **CVE-2026-95331** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95331)
- **CVE-2026-95329** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95329)
- **CVE-2026-95325** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95325)
- **CVE-2026-95318** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95318)
- **CVE-2026-95313** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95313)
- **CVE-2026-95311** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95311)
- **CVE-2026-95310** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95310)
- **CVE-2026-95299** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95299)
- **CVE-2026-95283** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95283)
- **CVE-2026-95281** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95281)
- **CVE-2026-95277** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95277)
- **CVE-2026-86131** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86131)
- **CVE-2026-85520** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85520)
- **CVE-2026-84436** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84436)
- **CVE-2026-84154** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84154) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84154)
- **CVE-2026-82973** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82973)
- **CVE-2026-8066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-8066) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-8066)
- **CVE-2026-8065** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-8065) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-8065)
- **CVE-2026-79538** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79538)
- **CVE-2026-76725** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76725)
- **CVE-2026-76724** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76724)
- **CVE-2026-76723** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76723)
- **CVE-2026-76722** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76722)
- **CVE-2026-76721** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76721)
- **CVE-2026-7192** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-7192)
- **CVE-2026-71379** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-71379)
- **CVE-2026-70356** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70356)
- **CVE-2026-53988** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53988)
- **CVE-2026-22094** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-22094)
- **CVE-2026-15390** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15390)
- **CVE-2026-103110** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103110)
- **CVE-2026-103056** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103056)
- **CVE-2026-103041** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103041)
- **CVE-2026-103040** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103040)
- **CVE-2026-102829** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102829)
- **CVE-2026-102828** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102828)
- **CVE-2026-102761** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102761)
- **CVE-2026-102710** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102710)
- **CVE-2026-102425** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102425)
- **CVE-2026-102331** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102331)
- **CVE-2026-102316** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102316)
- **CVE-2026-102309** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102309)
- **CVE-2026-102308** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102308)
- **CVE-2026-102306** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102306)
- **CVE-2026-102304** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102304)
- **CVE-2026-100819** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100819)
- **CVE-2026-100818** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100818)
- **CVE-2026-100811** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100811)
- **CVE-2026-100804** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100804)
- **CVE-2026-100800** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100800)
- **CVE-2026-100786** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100786)
- **CVE-2026-100778** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100778)
- **CVE-2026-100770** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100770)
- **CVE-2026-100762** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100762)
- **CVE-2026-100291** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100291)
- **CVE-2023-54400** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-54400)
- **CVE-2026-96423** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96423) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96423)
- **CVE-2026-96422** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96422) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96422)
- **CVE-2026-96421** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96421) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96421)
- **CVE-2026-96419** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96419) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96419)
- **CVE-2026-96418** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96418) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96418)
- **CVE-2026-96416** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96416) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96416)
- **CVE-2026-96415** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96415) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96415)
- **CVE-2026-95395** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95395) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95395)
- **CVE-2026-95394** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95394) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95394)
- **CVE-2026-95393** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95393) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95393)
- **CVE-2026-95392** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95392) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95392)
- **CVE-2026-95390** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95390) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95390)
- **CVE-2026-95388** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95388) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95388)
- **CVE-2026-95386** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95386) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95386)
- **CVE-2026-102616** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102616)
- **CVE-2026-102568** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102568)
- **CVE-2026-102507** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102507)
- **CVE-2026-102491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102491)
- **CVE-2026-102822** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102822)
- **CVE-2026-102601** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102601)
- **CVE-2026-77265** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77265) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-77265)
- **CVE-2026-88420** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88420) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88420)
- **CVE-2026-63498** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63498) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63498)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
