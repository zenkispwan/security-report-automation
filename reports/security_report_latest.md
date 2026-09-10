# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**2** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=2。
- Intelligence 候選：**30** 筆；P1 **17**、P2 **0**、P3 **11**、WATCH **2**。
- Baseline：state / generated_at=2026-09-10T11:15:12.377256+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-31431、CVE-2026-20079、CVE-2025-67038、CVE-2025-14733、CVE-2022-41352。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **2** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-87962｜tdunning / t-digest
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T11:17:07.763)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T11:17:07.763 / 2026-09-10T13:20:32.920
- **官方描述（原文）**：t-digest versions 3.1 through 3.3 contain a denial of service vulnerability in MergingDigest.fromBytes that fails to validate length and capacity fields from serialized data. Attackers can supply crafted serialized digests with mismatched header fields to trigger ArrayIndexOutOfBoundsException or NegativeArraySizeException, aborting the parsing thread.

### 2. CVE-2026-9163｜GIS Informatics / GisLab Laboratory Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-10T13:20:33.663)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-10T13:20:33.663 / 2026-09-10T13:20:33.663
- **官方描述（原文）**：Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in GIS Informatics GisLab Laboratory Management System allows SQL Injection. This issue affects GisLab Laboratory Management System: from 1.4.03 before 1.5.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-31431｜Linux / Kernel
- **Title**：Linux Kernel Incorrect Resource Transfer Between Spheres Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.99907 / percentile=0.99966
- **CISA KEV**：listed=true / date_added=2026-05-01 / due_date=2026-05-15
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Linux Kernel contains an incorrect resource transfer between spheres vulnerability that could allow for privilege escalation.
- **CISA Required Action（原文）**："Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-20079｜Cisco / Secure Firewall Management Center (FMC) and Security Cloud Control (SCC) Firewall Management
- **Title**：Cisco Firewall Management Center Authentication Bypass Using an Alternate Path or Channel Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.35946 / percentile=0.98374
- **CISA KEV**：listed=true / date_added=2026-09-09 / due_date=2026-09-12
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Cisco Secure Firewall Management Center (FMC) Software and Cisco Security Cloud Control (SCC) Firewall Management contain an authentication Bypass using an alternate path or channel vulnerability that could allow an unauthenticated, remote attacker to bypass authentication and execute script files on an affected device to obtain root access to the underlying operating system.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2025-67038｜Lantronix / EDS5000
- **Title**：Lantronix EDS5000 Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.1926 / percentile=0.97168
- **CISA KEV**：listed=true / date_added=2026-06-23 / due_date=2026-06-26
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Lantronix EDS5000 contains a code injection vulnerability that could allow attackers to inject arbitrary OS commands into the username parameter. Injected commands are executed with root privileges.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2025-14733｜WatchGuard / Firebox
- **Title**：WatchGuard Firebox Out of Bounds Write Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.2651 / percentile=0.97885
- **CISA KEV**：listed=true / date_added=2025-12-19 / due_date=2025-12-26
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WatchGuard Fireware OS iked process contains an out of bounds write vulnerability in the OS iked process. This vulnerability may allow a remote unauthenticated attacker to execute arbitrary code and affects both the mobile user VPN with IKEv2 and the branch office VPN using IKEv2 when configured with a dynamic gateway peer.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2022-41352｜Synacor / Zimbra Collaboration Suite (ZCS)
- **Title**：Synacor Zimbra Collaboration Suite (ZCS) Arbitrary File Upload Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.95478 / percentile=0.99866
- **CISA KEV**：listed=true / date_added=2022-10-20 / due_date=2022-11-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Synacor Zimbra Collaboration Suite (ZCS) allows an attacker to upload arbitrary files using cpio package to gain incorrect access to any other user accounts.
- **CISA Required Action（原文）**：Apply updates per vendor instructions.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2022-37969｜Microsoft / Windows
- **Title**：Microsoft Windows Common Log File System (CLFS) Driver Privilege Escalation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.28275 / percentile=0.97996
- **CISA KEV**：listed=true / date_added=2022-09-14 / due_date=2022-10-05
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft Windows Common Log File System (CLFS) driver contains an unspecified vulnerability that allows for privilege escalation.
- **CISA Required Action（原文）**：Apply updates per vendor instructions.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2016-7255｜Microsoft / Win32k
- **Title**：Microsoft Win32k Privilege Escalation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2021-11-03 / due_date=2022-05-03
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft Win32k kernel-mode driver fails to properly handle objects in memory which allows for privilege escalation. Successful exploitation allows an attacker to run code in kernel mode.
- **CISA Required Action（原文）**：Apply updates per vendor instructions.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2016-4117｜Adobe / Flash Player
- **Title**：Adobe Flash Player Arbitrary Code Execution Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2022-03-03 / due_date=2022-03-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：An access of resource using incompatible type vulnerability exists within Adobe Flash Player that allows an attacker to perform remote code execution.
- **CISA Required Action（原文）**：The impacted product is end-of-life and should be disconnected if still in use.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-87491｜Google / Chromium V8
- **Title**：Google Chromium V8 Out of Bounds Write Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00291 / percentile=0.21438
- **CISA KEV**：listed=true / date_added=2026-09-09 / due_date=2026-09-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium V8 contains an out of bounds write vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-86218｜N-able / N-central
- **Title**：N-able N-central Static Code Injection Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.00744 / percentile=0.52602
- **CISA KEV**：listed=true / date_added=2026-09-08 / due_date=2026-09-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：N-able N-central contains a static code injection vulnerability that could allow for pre-authentication remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-85880 | P1 / 90 | Microsoft / Windows | v3.1 7.8 (HIGH) | 0.00572 / percentile=0.45396 | listed=true / date_added=2026-09-08 / due_date=2026-09-22 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-81963 | P1 / 90 | Microsoft / Windows | v3.1 7.8 (HIGH) | 0.00631 / percentile=0.48159 | listed=true / date_added=2026-09-08 / due_date=2026-09-22 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-75650 | P1 / 90 | Adobe / Commerce and Magento | v3.1 10.0 (CRITICAL) | 未確認 | listed=true / date_added=2026-09-08 / due_date=2026-09-11 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-19490 | P1 / 90 | Citrix / NetScaler | v4.0 9.3 (CRITICAL) | 0.03372 / percentile=0.88028 | listed=true / date_added=2026-09-09 / due_date=2026-09-12 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-25249 | P1 / 90 | Fortinet / Multiple Products | v3.1 9.8 (CRITICAL) | 0.00759 / percentile=0.53107 | listed=true / date_added=2026-09-09 / due_date=2026-09-12 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-85046 | P1 / 82 | Google / Chromium V8 | v3.1 8.8 (HIGH) | 未確認 | listed=true / date_added=2026-09-04 / due_date=2026-09-18 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-38352 | P1 / 82 | Linux / Kernel | v3.1 7.8 (HIGH) | 0.01254 / percentile=0.67698 | listed=true / date_added=2025-09-04 / due_date=2025-09-25 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-43284 | P3 / 47 | Linux / Linux | v3.1 8.8 (HIGH) | 0.93235 / percentile=0.99829 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2023-52251 | P3 / 47 | 未確認 / 未確認 | v3.1 8.8 (HIGH) | 0.8684 / percentile=0.99733 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-42945 | P3 / 45 | F5 / NGINX Plus | v4.0 9.2 (CRITICAL) | 0.68047 / percentile=0.99279 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-87930 | P3 / 38 | MaxSite / MaxSite CMS | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79576 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 0.00334 / percentile=0.26314 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79574 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 0.00166 / percentile=0.06168 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79571 | P3 / 38 | 未確認 / 未確認 | v3.1 9.1 (CRITICAL) | 0.00175 / percentile=0.07135 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79570 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 0.00153 / percentile=0.04774 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79569 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 0.00393 / percentile=0.32718 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-78997 | P3 / 38 | 未確認 / 未確認 | v3.1 9.3 (CRITICAL) | 0.00153 / percentile=0.04736 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-73309 | P3 / 38 | XenForo / XenForo | v4.0 9.1 (CRITICAL) | 0.00469 / percentile=0.39168 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-87962 | WATCH / 30 | tdunning / t-digest | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-9163 | WATCH / 28 | GIS Informatics / GisLab Laboratory Management System | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：7；缺少 Product：7；缺少 Title：13。
- EPSS 未確認：7；Exploitation status 未確認：0。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-10T13:45:25.158574+00:00`；Delta generated at：`2026-09-10T13:45:25.158574+00:00`。

---

## 可驗證資料來源

- **CVE-2026-31431** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-31431) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-31431) · [Vendor / Advisory (lore.kernel.org)](https://lore.kernel.org/linux-cve-announce/2026042214-CVE-2026-31431-3d65@gregkh/) · [Vendor / Advisory (xint.io)](https://xint.io/blog/copy-fail-linux-distributions#the-fix-6) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/about/)
- **CVE-2026-20079** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20079) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20079) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-67038** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-67038) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-67038) · [Vendor / Advisory (ltrxdev.atlassian.net)](https://ltrxdev.atlassian.net/wiki/spaces/LTRXTS/pages/2538438657/Latest+Firmware+for+the+EDS5000+series+EDS5008+EDS5016+EDS5032) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-14733** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-14733) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-14733) · [Vendor / Advisory (watchguard.com)](https://www.watchguard.com/wgrd-psirt/advisory/wgsa-2025-00027)
- **CVE-2022-41352** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-41352) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2022-41352) · [Vendor / Advisory (wiki.zimbra.com)](https://wiki.zimbra.com/wiki/Security_Center)
- **CVE-2026-87962** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87962)
- **CVE-2026-9163** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9163)
- **CVE-2022-37969** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-37969) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2022-37969) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-37969)
- **CVE-2016-7255** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-7255) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- **CVE-2016-4117** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-4117) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- **CVE-2026-87491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87491) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87491) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-86218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86218) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86218) · [Vendor / Advisory (status.n-able.com)](https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/) · [Vendor / Advisory (me.n-able.com)](https://me.n-able.com/s/security-advisory/aArVy0000002Ld3KAE/cve202686218-preauthentication-remote-code-execution) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85880** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85880) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85880) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-81963** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81963) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-81963) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-75650** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75650) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (helpx.adobe.com)](https://helpx.adobe.com/security/products/magento/apsb26-146.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-19490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19490) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-19490) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-25249** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-25249) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-25249) · [Vendor / Advisory (fortiguard.fortinet.com)](https://fortiguard.fortinet.com/psirt/FG-IR-25-084) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85046) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-38352** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-38352) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-38352) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=2c72fe18cc5f9f1750f5bc148cf1c94c29e106ff) · [Vendor / Advisory (source.android.com)](https://source.android.com/docs/security/bulletin/2025-09-01)
- **CVE-2026-43284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-43284) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-43284)
- **CVE-2023-52251** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-52251) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-52251)
- **CVE-2026-42945** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42945) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42945)
- **CVE-2026-87930** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87930)
- **CVE-2026-79576** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79576) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79576)
- **CVE-2026-79574** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79574) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79574)
- **CVE-2026-79571** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79571) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79571)
- **CVE-2026-79570** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79570) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79570)
- **CVE-2026-79569** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79569) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79569)
- **CVE-2026-78997** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78997) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-78997)
- **CVE-2026-73309** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73309) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-73309)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
