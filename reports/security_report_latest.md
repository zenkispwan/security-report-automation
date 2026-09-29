# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**74** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=1、NEW_CVE=73。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **6**、WATCH **24**。
- Baseline：state / generated_at=2026-09-28T06:07:26.258680+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **74** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-85526｜Canonical / LXD
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T14:17:20.423)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T14:17:20.423 / 2026-09-29T04:18:00.690
- **官方描述（原文）**：Path traversal in the Btrfs storage driver (unpackVolume) in Canonical LXD on Linux allows an authenticated user with instance creation privileges to delete or replace arbitrary files and directories on the host filesystem as root via a crafted subvolumes[].path entry in backup/optimized_header.yaml during a btrfs optimized backup import.

### 2. CVE-2026-85185｜Canonical / LXD
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T14:17:20.130)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T14:17:20.130 / 2026-09-28T17:17:51.013
- **官方描述（原文）**：Path traversal in the btrfs storage driver in Canonical LXD versions 4.0.2 and later (fixed in 4.0.14, 5.0.10, 5.21.8 and 6.10) on Linux allows an authenticated client with permission to create instances in a project to delete arbitrary files on the host as root. On hosts whose root filesystem is btrfs, the client can also place attacker-controlled content at arbitrary host paths, leading to full host compromise. The client does this with a crafted subvolume path containing ../ sequences, sent in either of two ways: in the optimized_header.yaml of an optimized btrfs backup, or in the btrfs migration header sent by a malicious migration source.

### 3. CVE-2026-101077｜Netcore / NR289-GE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T16:17:12.143)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T16:17:12.143 / 2026-09-28T21:02:16.150
- **官方描述（原文）**：A flaw has been found in Netcore NR289-GE 1.4.5102. This impacts the function process_request of the component boa_temp Handler. This manipulation causes missing authentication. The attack is possible to be carried out remotely. The exploit has been published and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 4. CVE-2026-101075｜Netcore / NR289-GE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T15:17:13.043)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T15:17:13.043 / 2026-09-28T21:02:16.150
- **官方描述（原文）**：A security vulnerability has been detected in Netcore NR289-GE 1.4.5102. The impacted element is the function system of the file /location_time.cgi of the component Location Time Handler. The manipulation of the argument mac leads to os command injection. Remote exploitation of the attack is possible. The exploit has been disclosed publicly and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 5. CVE-2026-101072｜Netcore / NR289-GE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T14:17:13.973)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T14:17:13.973 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A vulnerability was identified in Netcore NR289-GE 1.4.5102. This issue affects the function system of the file /ap_ip.cgi of the component CGI Handler. Such manipulation of the argument ip leads to os command injection. The attack can be launched remotely. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 6. CVE-2026-101039｜FAST / FAC1900R
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T11:16:43.600)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T11:16:43.600 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A vulnerability was identified in FAST FAC1900R 20190827_2.0.2. Affected by this issue is the function copy_msg_element of the component devdiscover Service. Such manipulation leads to stack-based buffer overflow. The attack can be executed remotely. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 7. CVE-2026-55160｜stringer-rss / stringer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:23.540)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:23.540 / 2026-09-28T19:16:49.873
- **官方描述（原文）**：Stringer is a self-hosted, anti-social RSS reader. Prior to commit 75cb095, an unrestricted Server-Side Request Forgery (SSRF) vulnerability allows any authenticated user to force the Stringer server to send arbitrary HTTP/HTTPS requests to internal networks, localhost services, and cloud metadata endpoints (e.g. AWS IMDS 169.254.169.254). When self-service signup is enabled (Setting::UserSignup), even a low-privileged registered user can exploit this to scan internal services or steal cloud IAM credentials. This issue has been patched via commit 75cb095.

### 8. CVE-2026-48100｜polybase / payy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T17:17:49.547)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T17:17:49.547 / 2026-09-28T18:17:22.120
- **官方描述（原文）**：Payy is an Ethereum L2 zk-rollup for privacy preserving and regulatory compliant transactions. Prior to version 1.3.0, agg_agg forwards the compacted message stream from its inner proofs into a public messages: [Field; 1000] array, but it never checks that the unused tail of the outer array is zero. A registered prover can build a valid agg_final proof for an approved rollup block while inserting an extra burn message after the real messages. RollupV1.verifyRollup() then parses that public input as a normal burn and transfers USDC from the rollup contract to the attacker. This is a severe circuit soundness failure: the proof system accepts a public statement whose messages array is not fully derived from the verified inner proofs. On the current deployment, verifyRollup() is restricted to the existing allowlisted prover, so a fresh public caller cannot submit the invalid proof directly. That gate limits who can reach L1 today; it does not make the circuit statement sound. The issue becomes permissionless under the prover model described in the Payy whitepaper. Section 3.3.2 states: "To join as a prover, the prover is required to submit a small stake", and Section 3.3.1 states that if a prover fails to submit, "other nodes can submit the block proof instead." In that model, an attacker only needs to become a registered prover and use public validator approval data for an already approved block. This issue has been patched in version 1.3.0.

### 9. CVE-2026-101907｜axios / axios
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:19.270)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.0 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:19.270 / 2026-09-28T19:16:48.163
- **官方描述（原文）**：Axios is a promise-based HTTP client for the browser and Node.js. From 1.17.0 until 1.20.0, the fetch adapter bypasses the maxRedirects: 0 redirect policy. An Axios request uses the fetch adapter with maxRedirects set to zero and receives a redirect response. The underlying fetch implementation follows the redirect instead of returning the redirect response unchanged. The redirected request can access internal responses or reach state-changing internal endpoints despite redirects being disabled. This issue is fixed in version 1.20.0.

### 10. CVE-2026-101906｜axios / axios
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:19.100)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:19.100 / 2026-09-28T20:17:09.200
- **官方描述（原文）**：Axios is a promise-based HTTP client for the browser and Node.js. From 1.15.0 until 1.20.0, Axios shouldBypassProxy applies a quadratic trailing-dot regular expression to redirect hostnames. HTTP_PROXY or HTTPS_PROXY is configured, NO_PROXY or no_proxy is non-empty, redirects are followed, and a crafted redirect Location contains many dots followed by a non-dot character. Hostname.replace(/.+$/, '') backtracks quadratically while processing the crafted redirect hostname. Synchronous regular-expression processing can block the Node.js event loop and cause denial of service. This issue is fixed in version 1.20.0.

### 11. CVE-2026-101903｜axios / axios
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:18.560)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:18.560 / 2026-09-28T18:17:18.560
- **官方描述（原文）**：Axios is a promise-based HTTP client for the browser and Node.js. From 1.16.1 until 1.20.0, the RFC 2397 regular expression allows slash characters on both sides of the media-type separator. An application passes an attacker-controlled malformed data URL containing many slash characters and no comma. the JavaScript regular-expression engine explores many separator placements before rejecting the URL. Synchronous excessive backtracking can block the Node.js event loop and cause denial of service. The affected identifiers are fromDataURI, DATA_URL_PATTERN, data:. This issue is fixed in version 1.20.0.

### 12. CVE-2026-101898｜axios / axios
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:17.860)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.0 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:17.860 / 2026-09-28T18:17:17.860
- **官方描述（原文）**：Axios is a promise-based HTTP client for the browser and Node.js. From 1.13.0 until 1.20.0, Axios HTTP/2 request setup does not consistently apply proxy settings and caller-supplied DNS lookup policy. An HTTPS request uses httpVersion: 2 with explicit config.proxy or environment-derived proxy settings, or relies on caller-supplied config.lookup DNS policy. The HTTP/2 path can connect without the configured proxy behavior or without applying the caller-supplied config.lookup policy before http2.connect(). Requests can bypass the intended proxy route or the caller-supplied DNS resolution policy. This issue is fixed in version 1.20.0.

### 13. CVE-2026-101081｜D-Link / DI-8400
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T17:17:47.817)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T17:17:47.817 / 2026-09-28T21:03:44.987
- **官方描述（原文）**：A security flaw has been discovered in D-Link DI-8400 16.07. This vulnerability affects the function menu_nat_more_asp of the file menu_nat_more.asp of the component Web Administration Service. The manipulation of the argument opt results in stack-based buffer overflow. The attack can be launched remotely. The exploit has been released to the public and may be used for attacks.

### 14. CVE-2026-101074｜Netcore / NR289-GE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T15:17:12.830)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.9 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T15:17:12.830 / 2026-09-28T21:02:16.150
- **官方描述（原文）**：A weakness has been identified in Netcore NR289-GE 1.4.5102. The affected element is the function password-check of the file /bin/boa of the component Authentication. Executing a manipulation of the argument Username can lead to stack-based buffer overflow. The attack may be launched remotely. The exploit has been made available to the public and could be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 15. CVE-2026-101038｜FAST / FAC1200R
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T11:16:43.423)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T11:16:43.423 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A vulnerability was determined in FAST FAC1200R 5.0_20201119_1.0.2. Affected by this vulnerability is the function MmtAtePrase of the component MmtAtePrase Parser. This manipulation causes stack-based buffer overflow. Remote exploitation of the attack is possible. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 16. CVE-2026-101008｜aaPanel / BaoTa
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T07:17:20.403)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T07:17:20.403 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A vulnerability was found in aaPanel BaoTa up to 11.8.0. Impacted is the function merge_split_file of the file /www/server/panel/class/files.py of the component File Merge Handler. Performing a manipulation of the argument split_file_path results in command injection. The attack is possible to be carried out remotely. The exploit has been made public and could be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 17. CVE-2026-101007｜aaPanel / BaoTa
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T07:17:20.197)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T07:17:20.197 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A vulnerability has been found in aaPanel BaoTa up to 11.8.0. This issue affects the function InputSql of the file class/database.py of the component Database Backup Handler. Such manipulation of the argument Password leads to os command injection. The attack can be executed remotely. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 18. CVE-2026-101002｜Netcore / NBR200V2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T06:16:29.783)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T06:16:29.783 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A security flaw has been discovered in Netcore NBR200V2 1.3.241127.071246. Affected is the function system of the file /usr/bin/network_tools of the component Tools Ping Handler. Performing a manipulation of the argument url results in os command injection. The attack can be initiated remotely. The exploit has been released to the public and may be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 19. CVE-2026-90924｜Innotim Software, Telecommunications and Consultancy Trade Ltd. Co. / Logsign SIEM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T14:17:21.720)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T14:17:21.720 / 2026-09-28T17:17:52.323
- **官方描述（原文）**：Use of default credentials vulnerability in Innotim Software, Telecommunications and Consultancy Trade Ltd. Co. Logsign SIEM allows Try Common or Default Usernames and Passwords. This issue affects Logsign SIEM: from 6.4.101 before 6.4.117.

### 20. CVE-2026-88804｜SUSE / Rancher
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T16:17:15.827)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T16:17:15.827 / 2026-09-28T18:17:26.073
- **官方描述（原文）**：An unauthenticated update of public UI settings could be used by remote attackers to execute a stored cross-site scripting attack in the Rancher UI, in SUSE Rancher 2.15 before 2.15.2, 2.14 before 2.14.6, 2.13 before 2.13.10, 2.12 before 2.12.14 and 2.11 before 2.11.18.

### 21. CVE-2026-87799｜Canonical / LXD
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T14:17:21.427)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T14:17:21.427 / 2026-09-29T04:18:01.037
- **官方描述（原文）**：Improper link resolution in the migration receive path in Canonical LXD versions 4.0 and later (fixed in 4.0.14, 5.0.10, 5.21.8 and 6.10) on Linux allows an authenticated client that can create instances or custom storage volumes in a project, or a malicious migration source server, to write attacker-controlled files to arbitrary paths on the target host as root, leading to full host compromise. The attacker does this with a crafted rsync or btrfs send stream that plants a symlink in the transferred volume, such as rootfs or root.img, and then writes through it.

### 22. CVE-2026-86102｜WatchGuard / WatchGuard AP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T17:17:51.267)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T17:17:51.267 / 2026-09-28T20:51:05.473
- **官方描述（原文）**：An OS command injection vulnerability in the WatchGuard AP internal API service allows an attacker with network access to the AP to execute arbitrary shell commands on the underlying operating system.

### 23. CVE-2026-82384｜Apache Software Foundation / Apache Roller
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T08:16:42.273)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T08:16:42.273 / 2026-09-29T04:18:00.500
- **官方描述（原文）**：Deserialization of Untrusted Data in Apache Roller 6.1.5 allows an unauthenticated remote attacker to cause deserialization of attacker-controlled bytes, because the XML-RPC endpoint accepts vendor extension types that are deserialized during request parsing, before authentication. The servlet is mapped unconditionally, so parsing occurs even when the global XML-RPC feature is set to disabled; no non-default configuration is required for this path. This can lead to remote code execution. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which disables the extension types and rejects requests when the XML-RPC feature is disabled.

### 24. CVE-2026-82378｜Apache Software Foundation / Apache Roller
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T08:16:41.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T08:16:41.540 / 2026-09-29T04:17:59.730
- **官方描述（原文）**：Incorrect Authorization in the OAuth 1.0a authorization endpoint of Apache Roller 6.1.5 allows an unauthenticated remote attacker who learns an outstanding request token for a configured site-wide consumer to bind that token to an arbitrary user account, including an administrator, by submitting an unsigned authorization request. The endpoint derives the authorizing identity from a request-supplied value rather than the authenticated session. Only installations that configure an OAuth 1.0a site-wide consumer are affected, and exploitation requires knowledge of one of its outstanding request tokens. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which binds authorization to the logged-in session.

### 25. CVE-2026-82377｜Apache Software Foundation / Apache Roller
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T08:16:41.417)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T08:16:41.417 / 2026-09-29T04:17:58.953
- **官方描述（原文）**：Missing Authorization in Apache Roller 6.1.5 allows an authenticated user to read, modify, or delete weblog content belonging to other weblogs through the legacy XML-RPC Blogger and MetaWeblog APIs, because the handlers authenticate the caller but do not verify the caller's permission on the weblog or entry actually affected. Only installations that enable the non-default global XML-RPC setting are affected; the per-weblog API flag defaults to enabled for UI-created weblogs. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which applies an explicit per-method permission check, or to keep the XML-RPC feature disabled.

### 26. CVE-2026-81867｜Google Cloud / Application Integration
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T11:16:48.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T11:16:48.070 / 2026-09-28T11:16:48.070
- **官方描述（原文）**：A Deserialization of Untrusted Data vulnerability in the JavaScript Task in Google Cloud Application Integration versions prior to 2026-06-28 on Google Cloud Platform allows an authenticated user with standard permissions to run arbitrary code on the shared production servers using a specially crafted script bypassing param guards. This vulnerability was patched on 28 June 2026, and no customer action is needed.

### 27. CVE-2026-73642｜Dayforce / Payroll
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T14:17:17.160)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T14:17:17.160 / 2026-09-28T18:17:24.290
- **官方描述（原文）**：Dayforce Payroll is vulnerable to Path Traversal in file download functionality. An unauthenticated attacker can sent GET request with file path parameter set to any path including an absolute local file path. Because vendor contact attempts were unsuccessful, the vulnerability has only been confirmed in version R2026.2.0 but may also affect other versions.

### 28. CVE-2026-73640｜Dayforce / Payroll
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T14:17:16.843)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T14:17:16.843 / 2026-09-28T18:17:24.013
- **官方描述（原文）**：Dayforce Payroll is vulnerable to Time Based-Blind SQL Injection in password recovery functionality. The unauthenticated attacker can prepare GET request with one of the parameters filled in with an arbitrary SQL query. The parameter is interpreted as part of SQL predicate resulting in Time-Based Blind SQL Injection. Because vendor contact attempts were unsuccessful, the vulnerability has only been confirmed in version R2026.2.0 but may also affect other versions.

### 29. CVE-2026-49994｜dannymcc / bluehood
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:22.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:22.250 / 2026-09-28T20:17:10.420
- **官方描述（原文）**：Bluehood monitors local bluetooth activity. Prior to version 0.7.1, when auth_enabled is set in Bluehood, only the HTML page handlers enforced session validation. The /api/* handlers (settings, devices, groups, per-device endpoints including /api/device/{mac}/notes) called no auth check at all. A network attacker reachable on the dashboard port could read Bluetooth tracking data and modify application state — including the heartbeat URL, prune retention, device groups, and per-device notes — without a session cookie. This issue has been patched in version 0.7.1.

### 30. CVE-2026-19759｜Google Cloud / Application Integration
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T11:16:45.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T11:16:45.337 / 2026-09-28T20:17:10.293
- **官方描述（原文）**：An Incorrect Authorization vulnerability in the task configuration in Google Cloud Application Integration versions prior to 2026-06-17 on Google Cloud Platform allows an authenticated Google Cloud user to execute arbitrary internal RPCs from inside Google's production network under a privileged identity using an internal-only task type. This vulnerability was patched on 17 June 2026, and no customer action is needed.

### 31. CVE-2026-12342｜SailPoint Technologies / IdentityIQ
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T16:17:13.460)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T16:17:13.460 / 2026-09-29T04:17:55.873
- **官方描述（原文）**：This vulnerability impacts all versions of IdentityIQ and allows an unauthenticated user remote code execution on the IdentityIQ server due to improper input validation of submitted web service API content.

### 32. CVE-2026-102422｜未確認 / shell-quote
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T04:17:55.707)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T04:17:55.707 / 2026-09-29T04:17:55.707
- **官方描述（原文）**：shell-quote's `quote()` function emits a `{ comment }` token as `#` followed by its text, which comments out the rest of the shell line, including the opening quote of any later string token. A line terminator (\n, \r, U+2028, U+2029) in that later string therefore ends the comment, and the rest of the string is parsed as shell input: `quote(['echo', 'ok', { comment: 'x' }, 'a\nid;#'])` runs `id` in sh, bash, dash, ksh and zsh. `parse()` emits a comment token for a `#` in the middle of a word (for example `http://example.com/#frag`), so callers that combine `parse()` output with another untrusted string, such as `quote(parse(untrustedCommand).concat(untrustedArg))`, are affected. The fix for CVE-2026-9277 rejected line terminators in the comment's own text, but not in the tokens after it. Fixed in 1.11.0: `quote()` throws a `TypeError` when a string after a `{ comment }` token contains a line terminator.

### 33. CVE-2026-102361｜gz-yami / mall4j
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T00:17:03.183)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T00:17:03.183 / 2026-09-29T00:17:03.183
- **官方描述（原文）**：mall4j through 4.0 contains a missing authentication vulnerability in the PUT /user/updatePwd endpoint that allows unauthenticated attackers to reset any storefront account password. Attackers can supply a target username in the request body to overwrite passwords without verification, enabling account takeover and access to orders and personal data.

### 34. CVE-2026-102334｜NginxProxyManager / nginx-proxy-manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T23:17:01.837)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T23:17:01.837 / 2026-09-28T23:17:01.837
- **官方描述（原文）**：Nginx Proxy Manager through 2.16.0 lacks rate-limiting on authentication endpoints, allowing unauthenticated attackers to make unlimited password guesses against any account. Attackers can brute-force login credentials via POST /api/tokens and subsequently guess TOTP codes via POST /api/tokens/2fa to gain full session access and administrative control.

### 35. CVE-2026-102268｜jpadilla / pyjwt
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T21:17:14.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T21:17:14.600 / 2026-09-28T21:17:14.600
- **官方描述（原文）**：PyJWT is a Python implementation of JSON Web Token standards. Prior to 2.14.0, is_pem_format in jwt/utils.py is affected because is_pem_format does not recognize every PEM representation accepted by the cryptography loader. This occurs when an application mixes HMAC and asymmetric algorithms and supplies a mutated public-key PEM as raw key bytes. As a result, HMACAlgorithm.prepare_key treats the unrecognized asymmetric public key as an HMAC secret. Consequently, an attacker who knows the public key can forge authenticated HMAC tokens. This issue is fixed in version 2.14.0.

### 36. CVE-2026-102240｜Netcore / NAP930
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-29T02:16:55.153)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-29T02:16:55.153 / 2026-09-29T02:16:55.153
- **官方描述（原文）**：A vulnerability was found in Netcore NAP930 0.1.241010.141410. This affects the function eval of the file /www/cgi-bin/network_tools of the component Network Tools CGI. The manipulation of the argument sid results in os command injection. The attack may be performed from remote. The exploit has been made public and could be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 37. CVE-2026-101894｜XhmikosR / decompress
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T17:17:48.830)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T17:17:48.830 / 2026-09-28T18:17:17.730
- **官方描述（原文）**：The decompress package for Node.js extracts archives. Prior to 10.2.2 and 11.1.4, the default decompress(input, output) API relies on lexical containment checks that do not account for the kernel following a planted symlink chain. An attacker can supply a crafted archive containing chained symlink entries so that a later entry resolves outside the output directory. This allows files outside output to be read or written, and overwriting startup scripts or configuration can lead to remote code execution. The maintained @xhmikosr/decompress package is fixed in 10.2.2 and 11.1.4, but the separately affected unmaintained decompress package remains unpatched through 4.2.1. This vulnerability results from a bypass of the incomplete hardening for CVE-2026-53486. @xhmikosr/decompress is fixed in versions 10.2.2 and 11.1.4.

### 38. CVE-2026-101891｜WatchGuard / WatchGuard AP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T17:17:48.677)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T17:17:48.677 / 2026-09-28T20:51:05.473
- **官方描述（原文）**：An improper access control vulnerability in an internal API service on WatchGuard Access Points allows an unauthenticated attacker with network access to the AP to obtain a valid API session.

### 39. CVE-2026-101110｜ordasoft.com / Book Library (Free) extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T19:16:47.243)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T19:16:47.243 / 2026-09-28T19:16:47.243
- **官方描述（原文）**：Joomla Extension - ordasoft.com - Unauthenticated SQL Injection in Book Library (Free) < 6.4.6 - site/booklibrary.php’s books() function reads the field and direction request parameters and passes each through a function called protectInjectionWithoutQuote(), whose only real protection is a keyword blacklist that, on detecting the literal substring select, wraps the value in $db->quote() instead of rejecting it. The value is then concatenated directly into an unquoted ORDER BY clause, a position where quoting provides no protection at all. Reaching the vulnerable code path requires two conditions: a first request to prime session-stored sort defaults, and a trailing decoy comment (-- xselect) that satisfies the blacklist’s substring check without altering the payload’s effect.

### 40. CVE-2026-101108｜ordasoft.com / Vehicle Manager (Free) extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T19:16:46.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T19:16:46.930 / 2026-09-28T19:16:46.930
- **官方描述（原文）**：Joomla Extension - ordasoft.com - Unauthenticated SQL Injection in Vehicle Manager (Free) < 6.5.8 - site/vehiclemanager.php reads the order_field and order_direction sort parameters at three separate anonymous-reachable frontend entry points (category listing, search, and the all-vehicles listing) through a sanitizing function that applies real escaping, but the value is then placed into an unquoted ORDER BY clause, where escaping has no protective effect.

### 41. CVE-2026-101076｜Netcore / NR289-GE
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T16:17:11.947)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T16:17:11.947 / 2026-09-28T21:02:16.150
- **官方描述（原文）**：A vulnerability was detected in Netcore NR289-GE 1.4.5102. This affects the function system of the file /set_ntp_server_ip.cgi of the component CGI Handler. The manipulation of the argument ntp_ip results in os command injection. The attack can be executed remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 42. CVE-2026-100752｜ordasoft.com / Real Estate Manager (Free) extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T19:16:46.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T19:16:46.060 / 2026-09-28T19:16:46.060
- **官方描述（原文）**：Joomla Extension - ordasoft.com - Unauthenticated SQL Injection in Real Estate Manager (Free) < 6.7.9 - site/realestatemanager.php builds the ORDER BY clause of three separate frontend property-listing queries (category browsing, search results, and the full property listing) from a request-controlled order_field parameter, concatenated directly into an unquoted SQL clause with no allow-list of real column names and no cast.

### 43. CVE-2026-86334｜Canonical / LXD
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T14:17:20.590)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.2 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T14:17:20.590 / 2026-09-28T18:17:25.683
- **官方描述（原文）**：Path traversal in the CLI client image export and copy functionality in Canonical LXD from 4.0.2 before 4.0.14, 5.0.10, 5.21.8, and 6.10 on all platforms allows a remote malicious or machine-in-the-middle image server to overwrite arbitrary local files and execute code on the client system via a crafted Content-Disposition header filename parameter during unified image export or copy operations into a local directory target.

### 44. CVE-2026-55156｜ooples / token-optimizer-mcp
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:23.203)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:23.203 / 2026-09-28T19:16:49.743
- **官方描述（原文）**：Token Optimizer MCP measures token savings per AI coding agent, optimizes context, and shares a live local knowledge graph across 16 CLI clients. Prior to version 5.1.0, the dashboard HTTP server in token-optimizer-mcp exposes /api/session-summary and /api/session-events with no authentication middleware — any network-accessible client can reach them without credentials. Both handlers concatenate the caller-supplied sessionId query parameter directly into a filesystem path via path.join, and Node.js normalizes .. segments at resolution time, allowing an unauthenticated attacker to read any .jsonl file reachable from the server's filesystem. This issue has been patched in version 5.1.0.

### 45. CVE-2026-101917｜jpadilla / pyjwt
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T21:17:13.210)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T21:17:13.210 / 2026-09-28T21:17:13.210
- **官方描述（原文）**：PyJWT is a Python implementation of JSON Web Token standards. Prior to 2.14.0, PyJWT get_signing_key_from_jwt is affected because unknown kid misses force refreshes without a negative cache or minimum refresh interval. This occurs when unauthenticated tokens repeatedly use the same unknown kid or varying kid values absent from the cached JWKS. As a result, each cache miss causes PyJWKClient to refresh the JWKS. Consequently, attacker traffic can amplify outbound requests to the configured JWKS endpoint. This issue is fixed in version 2.14.0.

### 46. CVE-2026-101913｜beaugunderson / ip-address
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:21.237)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:21.237 / 2026-09-28T19:16:48.690
- **官方描述（原文）**：ip-address is a library for parsing and manipulating IPv4 and IPv6 addresses in JavaScript. Prior to 10.5.1, the Address6 isLinkLocal method in src/ipv6.ts recognizes only fe80::/64 instead of the complete fe80::/10 IPv6 link-local range. An attacker-controlled address elsewhere in fe80::/10 can therefore pass a trust-boundary check that relies on isLinkLocal. The same address is identified as link-local by getType and getScope, exposing the inconsistent classification. A successful bypass can reach an on-link host outside the intended trust boundary. This issue is fixed in version 10.5.1.

### 47. CVE-2026-101912｜beaugunderson / ip-address
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:21.073)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:21.073 / 2026-09-28T20:17:09.327
- **官方描述（原文）**：ip-address is a library for parsing and manipulating IPv4 and IPv6 addresses in JavaScript. Prior to 10.7.1, the isInSubnet and isHostInSubnet methods in src/common.ts compare masked binary strings without validating that both operands use the same IP family. A cross-family containment check whose leading address bits match makes the masked strings compare equal even though IPv4 and IPv6 do not share an address space. An allowlist or denylist decision can therefore classify an address outside the intended range as contained. This issue is fixed in version 10.7.1.

### 48. CVE-2026-101910｜beaugunderson / ip-address
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:20.710)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:20.710 / 2026-09-28T19:16:48.560
- **官方描述（原文）**：ip-address is a library for parsing and manipulating IPv4 and IPv6 addresses in JavaScript. From 10.2.0 until 10.5.1, the Address6 isPrivate classifier in src/ipv6.ts does not recognize the NAT64 local-use range 64:ff9b:1::/48. Applications that combine isPrivate, isLoopback, and isLinkLocal for a trust-boundary decision can treat an internal IPv4 destination encoded through that range as external. Exploitation depends on a server network using an operator-selected NAT64 prefix within the local-use range. A successful bypass can cross the intended network trust boundary. This issue is fixed in version 10.5.1.

### 49. CVE-2026-101908｜axios / axios
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:19.440)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:19.440 / 2026-09-28T19:16:48.390
- **官方描述（原文）**：Axios is a promise-based HTTP client for the browser and Node.js. From 1.7.0 until 1.20.0, the fetch adapter constructs a Request with sanitized resolvedOptions but then calls fetch with the original fetchOptions. A separate same-process prototype-pollution flaw populates Object.prototype.headers so fetchOptions.headers resolves through inheritance. The inherited fetchOptions.headers value overrides the sanitized Request headers through the second argument to fetch after Request construction. Attacker-controlled request headers can alter authorization, caching, metadata-service access, or application-specific behavior. This issue is fixed in version 1.20.0.

### 50. CVE-2026-101904｜axios / axios
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:18.740)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:18.740 / 2026-09-28T18:17:18.740
- **官方描述（原文）**：Axios is a promise-based HTTP client for the browser and Node.js. From 1.0.0 until 1.20.0, the dispatchRequest function normalizes inherited Object.prototype.headers from a replacement request configuration. A separate same-process prototype-pollution flaw sets Object.prototype.headers, and trusted request interceptors return a new ordinary configuration without an own headers property. After the interceptor chain, dispatchRequest resolves the inherited headers during normalization. Downstream request processing can observe attacker-controlled headers, including authorization-related values. This issue is fixed in version 1.20.0.

### 51. CVE-2026-101902｜axios / axios
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:18.397)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:18.397 / 2026-09-28T20:17:09.063
- **官方描述（原文）**：Axios is a promise-based HTTP client for the browser and Node.js. From 0.27.2 until 0.34.0 and 1.20.0, Axios default-instance requests that omit an explicit method can read an inherited method value from Object.prototype. If another vulnerability in the same process pollutes Object.prototype.method, calls such as axios.request({ url }) and axios({ url }) can send a state-changing HTTP method instead of the expected default GET. Axios does not create the prototype pollution source. This is a read-side gadget in axios request dispatch. This issue is fixed in version 0.34.0 and 1.20.0.

### 52. CVE-2026-101900｜axios / axios
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T18:17:18.050)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T18:17:18.050 / 2026-09-28T18:17:18.050
- **官方描述（原文）**：Axios is a promise-based HTTP client for the browser and Node.js. From 1.12.0 until 1.20.0, ResolveConfig reads inherited Symbol.toStringTag, append, and getHeaders properties while resolving FormData headers. A separate same-process prototype-pollution flaw supplies an array or non-plain class instance whose inherited properties make it appear FormData-like; plain objects are blocked. The inherited getHeaders function can return attacker-controlled headers that resolveConfig merges into a fetch adapter request. Attacker-controlled headers can alter authorization, cache, metadata-service, or application-specific request behavior. This issue is fixed in version 1.20.0.

### 53. CVE-2026-101083｜未確認 / PMWeb
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T17:17:48.287)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T17:17:48.287 / 2026-09-28T21:03:44.987
- **官方描述（原文）**：A security vulnerability has been detected in PMWeb v7.x/v8.x/v2025.x. Impacted is an unknown function in the library encryptionhelper.dll. Such manipulation leads to information disclosure. The attack may be launched remotely. The vendor was contacted early about this disclosure but did not respond in any way.

### 54. CVE-2026-101069｜未確認 / dbgate
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T13:17:20.747)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T13:17:20.747 / 2026-09-28T15:17:12.440
- **官方描述（原文）**：A weakness has been identified in dbgate up to 7.3.1. Affected is the function exportModelSql of the file packages/api/src/controllers/databaseConnections.js of the component Export Handler. Executing a manipulation of the argument outputFile can lead to path traversal. The attack can be executed remotely. The exploit has been made available to the public and could be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 55. CVE-2026-101068｜未確認 / dbgate
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T13:17:20.530)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T13:17:20.530 / 2026-09-28T14:17:13.390
- **官方描述（原文）**：A security flaw has been discovered in dbgate up to 7.3.1. This impacts the function zipJsonLinesData of the file packages/api/src/utility/zipJsonLinesData.js of the component Create Connection Endpoint. Performing a manipulation of the argument filePath results in path traversal. Remote exploitation of the attack is possible. The exploit has been released to the public and may be used for attacks. PR #1530 / commit 5f99b4d82 (7.2.5) hardened other export endpoints with checkSecureExportFilePath but omitted this endpoint. The vendor was contacted early about this disclosure but did not respond in any way.

### 56. CVE-2026-101066｜未確認 / dbgate
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T13:17:20.080)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T13:17:20.080 / 2026-09-28T13:17:20.253
- **官方描述（原文）**：A vulnerability was determined in dbgate up to 7.3.1. The impacted element is the function createLink of the file packages/api/src/controllers/archive.js of the component Archive Link Creation. This manipulation of the argument linkedFolder causes path traversal. The attack may be initiated remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 57. CVE-2026-101055｜Thinkware / U3000
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T13:17:19.677)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T13:17:19.677 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A security flaw has been discovered in Thinkware U3000 up to 1.02.04. Affected by this vulnerability is the function GET_STATUS of the component TCP Service. The manipulation of the argument wifi_info results in information disclosure. The attack can be executed remotely. The exploit has been released to the public and may be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 58. CVE-2026-101052｜refly-ai / refly
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T12:17:35.977)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T12:17:35.977 / 2026-09-28T13:17:19.383
- **官方描述（原文）**：A security vulnerability has been detected in refly-ai refly up to 1.1.0. This issue affects some unknown processing of the file apps/api/src/modules/config/app.config.ts of the component JWT Token Handler. The manipulation with the input test leads to hard-coded credentials. It is possible to initiate the attack remotely. The exploit has been disclosed publicly and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 59. CVE-2026-101035｜aligungr / UERANSIM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T10:16:42.453)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T10:16:42.453 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A flaw has been found in aligungr UERANSIM up to 3.3.0. This affects the function DecodePlainMmMessage in the library src/lib/nas/encode.cpp of the component nr-gnb. Executing a manipulation can lead to uncaught exception. The attack can be launched remotely. The exploit has been published and may be used. This patch is called 1ae9bf2062b57595dbcbc4bc1d0a0ccf06815bac. It is best practice to apply a patch to resolve this issue.

### 60. CVE-2026-101017｜Trusted Domain Project / OpenDMARC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T09:17:05.503)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T09:17:05.503 / 2026-09-28T15:15:33.930
- **官方描述（原文）**：A vulnerability was found in Trusted Domain Project OpenDMARC up to 1.4.2. This vulnerability affects the function strcasecmp in the library libopendmarc/opendmarc_policy.c. The manipulation results in handling of exceptional conditions. The attack can be executed remotely. The exploit has been made public and could be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 61. CVE-2026-101016｜Trusted Domain Project / OpenDMARC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T09:17:05.340)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T09:17:05.340 / 2026-09-28T15:15:33.930
- **官方描述（原文）**：A vulnerability has been found in Trusted Domain Project OpenDMARC up to 1.4.2. This affects the function opendmarc_policy_parse_dmarc in the library libopendmarc/opendmarc_policy.c. The manipulation of the argument fo/rf/ri/pct/sp/adkim/aspf/rua/ruf leads to handling of exceptional conditions. Remote exploitation of the attack is possible. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 62. CVE-2026-101014｜Trusted Domain Project / OpenDMARC
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T09:17:03.893)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T09:17:03.893 / 2026-09-28T15:15:33.930
- **官方描述（原文）**：A vulnerability was detected in Trusted Domain Project OpenDMARC up to 1.4.2. Affected by this vulnerability is the function opendmarc_util_cleanup in the library libopendmarc/opendmarc_util.c of the component DMARC Record Parser. Performing a manipulation results in off-by-one. The attack may be initiated remotely. The exploit is now public and may be used. The patch is named b3b1da9264bc80324094a27c71e7369bdedc62ae. To fix this issue, it is recommended to deploy a patch.

### 63. CVE-2026-101005｜未確認 / October CMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T07:17:19.827)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T07:17:19.827 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A vulnerability was detected in October CMS up to 4.3.4. This affects the function validateExternalImageHost of the file System/Classes/ResizeImages.php of the component SSRF Protection. The manipulation results in server-side request forgery. The attack may be launched remotely. The exploit is now public and may be used. Upgrading to version 4.3.5 is able to mitigate this issue. You should upgrade the affected component.

### 64. CVE-2026-101004｜notionnext-org / NotionNext
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T06:16:31.570)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T06:16:31.570 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A security vulnerability has been detected in notionnext-org NotionNext up to 4.10.10. Affected by this issue is the function cleanCache of the file pages/api/cache.js of the component Authentication Guard. The manipulation of the argument token leads to missing authentication. The attack may be initiated remotely. Versions 4.1.0 - 4.9.5.2 allow unauthenticated exploitation due to missing method check. In versions 4.9.5.7 - 4.10.10 a guard present but only enforced when CACHE_REVALIDATION_TOKEN is set. Default deployments remain unprotected. The vendor was contacted early about this disclosure but did not respond in any way.

### 65. CVE-2026-100370｜rhukster / dom-sanitizer
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T21:17:10.280)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.7 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T21:17:10.280 / 2026-09-28T21:17:10.280
- **官方描述（原文）**：DOMSanitizer is a DOM/SVG/MathML Sanitizer for PHP 7.3+. Prior to version 1.0.15, the isDangerousUrl() method is responsible for rejecting dangerous URL values in the href and xlink:href attributes. The weakness is that "javascript:" is rejected as a scheme, while "data:" is rejected only when the literal substring onload appears in the URL value (/^data:.*onload/i). Because data: payloads are routinely Base64-encoded, the dangerous content (<script>, event handlers, etc.) is invisible to that substring test. A URL such as data:text/html;base64,… therefore survives in href / xlink:href, even though the decoded payload is active markup. This is an incomplete input-validation / sanitization defect in the sanitizer itself. This issue has been patched in version 1.0.15.

### 66. CVE-2026-101139｜Webkul / Bagisto
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T19:16:47.940)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T19:16:47.940 / 2026-09-28T21:03:44.987
- **官方描述（原文）**：A vulnerability was detected in Webkul Bagisto up to 2.4.6. This impacts an unknown function of the file /admin/sales/invoices/mass-update/state of the component Invoice Mass Status Update. Performing a manipulation results in missing authorization. The attack can be initiated remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure.

### 67. CVE-2026-101105｜code-projects / Matrimonial System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T19:16:46.693)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T19:16:46.693 / 2026-09-28T21:03:44.987
- **官方描述（原文）**：A vulnerability was determined in code-projects Matrimonial System 1.0. The affected element is the function processprofile_form of the file /create_profile of the component Profile Creation Endpoint. This manipulation of the argument fname causes sql injection. The attack is possible to be carried out remotely. The exploit has been publicly disclosed and may be utilized.

### 68. CVE-2026-101080｜Tencent / AI-Infra-Guard
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T16:17:12.820)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 0.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T16:17:12.820 / 2026-09-28T21:03:44.987
- **官方描述（原文）**：A vulnerability was identified in Tencent AI-Infra-Guard up to 4.5.2/4.6.2. This affects the function startsWith of the file skill_scan/tools/dir/dir_actions.py of the component File Access. The manipulation leads to path traversal. The attack needs to be performed locally. The exploit is publicly available and might be used. Upgrading to version 4.6.0 is able to mitigate this issue. The identifier of the patch is ac0384edc9dbea3b226edefcf50613bd8509134f. You should upgrade the affected component.

### 69. CVE-2026-101078｜deepseek-ai / deepseek-harness
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T16:17:12.370)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T16:17:12.370 / 2026-09-28T21:03:44.987
- **官方描述（原文）**：A vulnerability has been found in deepseek-ai deepseek-harness up to 0.1.7-rc.2. Affected is an unknown function of the file packages/sandbox/sandbox-local/src/profiles.ts of the component Landlock Backend. Such manipulation leads to improper isolation or compartmentalization. The attack must be carried out locally. The exploit has been disclosed to the public and may be used. It is advisable to implement a patch to correct this issue. The vendor was contacted early about this disclosure but did not respond in any way.

### 70. CVE-2026-101071｜Acrel Electric / Unet Web Service
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T14:17:13.770)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T14:17:13.770 / 2026-09-28T16:17:11.633
- **官方描述（原文）**：A vulnerability was determined in Acrel Electric Unet Web Service up to 20260814. This vulnerability affects unknown code of the file /exchange/attachment/upload of the component Upload Endpoint. This manipulation of the argument File causes unrestricted upload. The attack can be initiated remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 71. CVE-2026-101036｜FLB-Music / FLB-Music-Player
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T10:16:42.630)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T10:16:42.630 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A vulnerability has been found in FLB-Music FLB-Music-Player 1.1.8/1.1.9/1.2.0/1.2.1. This impacts the function path.join of the file /src/main/core/createParsedTrack.ts. The manipulation leads to path traversal. The attack must be carried out locally. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 72. CVE-2026-101011｜aaPanel / BaoTa
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T08:16:36.980)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T08:16:36.980 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A security flaw has been discovered in aaPanel BaoTa up to 11.8.0. This affects the function get_domain_status of the file /www/server/panel/mod/project/domain/domainMod.py of the component Domain Handler. The manipulation of the argument get results in sql injection. It is possible to launch the attack remotely. The exploit has been released to the public and may be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 73. CVE-2026-101010｜aaPanel / BaoTa
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-28T08:16:36.807)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-28T08:16:36.807 / 2026-09-28T15:16:04.793
- **官方描述（原文）**：A vulnerability was identified in aaPanel BaoTa up to 11.8.0. The impacted element is the function getData of the file /www/server/panel/class/data.py. The manipulation of the argument log_type leads to sql injection. It is possible to initiate the attack remotely. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 74. CVE-2026-77246｜sooperset / mcp-atlassian
- **Delta event**：CVSS_CHANGED (from=7.4; to=8.6)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-22T19:16:48.730 / 2026-09-28T14:31:10.220
- **官方描述（原文）**：MCP Atlassian is a Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Prior to 0.22.0, an HTTP transport deployment with READ_ONLY_MODE=false accepts a request without an Authorization identity and permits attacker-controlled Atlassian service headers, including X-Atlassian-Confluence-Url, to select a public attacker hostname or one allowed by MCP_ALLOWED_URL_DOMAINS. A caller can then invoke confluence_upload_attachment or the Jira attachment variant in src/mcp_atlassian/jira/attachments.py with a server-local file_path and cause the MCP process to send the file to the selected attachment endpoint. This issue is fixed in version 0.22.0.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-85526 | P3 / 38 | Canonical / LXD | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-85185 | P3 / 38 | Canonical / LXD | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101077 | P3 / 38 | Netcore / NR289-GE | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101075 | P3 / 38 | Netcore / NR289-GE | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101072 | P3 / 38 | Netcore / NR289-GE | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101039 | P3 / 38 | FAST / FAC1900R | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-55160 | WATCH / 30 | stringer-rss / stringer | v3.1 7.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-48100 | WATCH / 30 | polybase / payy | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101907 | WATCH / 30 | axios / axios | v4.0 7.0 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101906 | WATCH / 30 | axios / axios | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101903 | WATCH / 30 | axios / axios | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101898 | WATCH / 30 | axios / axios | v4.0 7.0 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101081 | WATCH / 30 | D-Link / DI-8400 | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101074 | WATCH / 30 | Netcore / NR289-GE | v4.0 8.9 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101038 | WATCH / 30 | FAST / FAC1200R | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101008 | WATCH / 30 | aaPanel / BaoTa | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101007 | WATCH / 30 | aaPanel / BaoTa | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-101002 | WATCH / 30 | Netcore / NBR200V2 | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90924 | WATCH / 28 | Innotim Software, Telecommunications and Consultancy Trade Ltd. Co. / Logsign SIEM | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-88804 | WATCH / 28 | SUSE / Rancher | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-87799 | WATCH / 28 | Canonical / LXD | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-86102 | WATCH / 28 | WatchGuard / WatchGuard AP | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-82384 | WATCH / 28 | Apache Software Foundation / Apache Roller | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-82378 | WATCH / 28 | Apache Software Foundation / Apache Roller | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-82377 | WATCH / 28 | Apache Software Foundation / Apache Roller | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-81867 | WATCH / 28 | Google Cloud / Application Integration | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-73642 | WATCH / 28 | Dayforce / Payroll | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-73640 | WATCH / 28 | Dayforce / Payroll | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-49994 | WATCH / 28 | dannymcc / bluehood | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-19759 | WATCH / 28 | Google Cloud / Application Integration | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：30。
- EPSS 未確認：30；Exploitation status 未確認：1。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-29T06:25:15.443632+00:00`；Delta generated at：`2026-09-29T06:25:15.443632+00:00`。

---

## 可驗證資料來源

- **CVE-2026-85526** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85526)
- **CVE-2026-85185** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85185)
- **CVE-2026-101077** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101077)
- **CVE-2026-101075** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101075)
- **CVE-2026-101072** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101072)
- **CVE-2026-101039** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101039)
- **CVE-2026-55160** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55160)
- **CVE-2026-48100** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48100)
- **CVE-2026-101907** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101907)
- **CVE-2026-101906** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101906)
- **CVE-2026-101903** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101903)
- **CVE-2026-101898** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101898)
- **CVE-2026-101081** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101081)
- **CVE-2026-101074** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101074)
- **CVE-2026-101038** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101038)
- **CVE-2026-101008** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101008)
- **CVE-2026-101007** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101007)
- **CVE-2026-101002** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101002)
- **CVE-2026-90924** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90924)
- **CVE-2026-88804** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88804)
- **CVE-2026-87799** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87799)
- **CVE-2026-86102** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86102)
- **CVE-2026-82384** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82384)
- **CVE-2026-82378** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82378)
- **CVE-2026-82377** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82377)
- **CVE-2026-81867** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81867)
- **CVE-2026-73642** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73642)
- **CVE-2026-73640** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73640)
- **CVE-2026-49994** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-49994)
- **CVE-2026-19759** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19759)
- **CVE-2026-12342** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12342)
- **CVE-2026-102422** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102422)
- **CVE-2026-102361** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102361)
- **CVE-2026-102334** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102334)
- **CVE-2026-102268** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102268)
- **CVE-2026-102240** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102240)
- **CVE-2026-101894** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101894)
- **CVE-2026-101891** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101891)
- **CVE-2026-101110** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101110)
- **CVE-2026-101108** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101108)
- **CVE-2026-101076** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101076)
- **CVE-2026-100752** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100752)
- **CVE-2026-86334** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86334)
- **CVE-2026-55156** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-55156)
- **CVE-2026-101917** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101917)
- **CVE-2026-101913** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101913)
- **CVE-2026-101912** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101912)
- **CVE-2026-101910** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101910)
- **CVE-2026-101908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101908)
- **CVE-2026-101904** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101904)
- **CVE-2026-101902** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101902)
- **CVE-2026-101900** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101900)
- **CVE-2026-101083** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101083)
- **CVE-2026-101069** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101069)
- **CVE-2026-101068** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101068)
- **CVE-2026-101066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101066)
- **CVE-2026-101055** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101055)
- **CVE-2026-101052** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101052)
- **CVE-2026-101035** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101035)
- **CVE-2026-101017** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101017)
- **CVE-2026-101016** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101016)
- **CVE-2026-101014** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101014)
- **CVE-2026-101005** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101005)
- **CVE-2026-101004** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101004)
- **CVE-2026-100370** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100370)
- **CVE-2026-101139** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101139)
- **CVE-2026-101105** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101105)
- **CVE-2026-101080** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101080)
- **CVE-2026-101078** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101078)
- **CVE-2026-101071** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101071)
- **CVE-2026-101036** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101036)
- **CVE-2026-101011** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101011)
- **CVE-2026-101010** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101010)
- **CVE-2026-77246** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77246)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
