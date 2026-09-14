# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**4** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=4。
- Intelligence 候選：**20** 筆；P1 **13**、P2 **0**、P3 **3**、WATCH **4**。
- Baseline：state / generated_at=2026-09-13T05:30:44.355904+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-86218、CVE-2026-86060、CVE-2026-85706、CVE-2026-84869、CVE-2026-82078。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **4** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-90680｜D-Link / DIR-823G
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-14T04:16:36.353)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-14T04:16:36.353 / 2026-09-14T04:16:36.353
- **官方描述（原文）**：A security flaw has been discovered in D-Link DIR-823G 1.0.2B05_20181207. The impacted element is the function strcpy of the file /HNAP1/SetStaticRouteSettings of the component HNAP1. The manipulation of the argument PAddress/SubnetMask/Gateway results in stack-based buffer overflow. The attack can be launched remotely.

### 2. CVE-2026-90562｜langbot-app / LangBot
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-13T11:17:00.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-13T11:17:00.780 / 2026-09-13T11:17:00.780
- **官方描述（原文）**：LangBot before 4.10.11 generates password recovery keys with only 24 bits of entropy and applies no rate limiting to the unauthenticated reset-password endpoint. Remote attackers knowing the administrator email can exhaust the keyspace through concurrent requests to reset the admin password and gain account access.

### 3. CVE-2026-90561｜strapi / strapi
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-13T11:17:00.613)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-13T11:17:00.613 / 2026-09-13T11:17:00.613
- **官方描述（原文）**：Strapi versions 4.x through 4.26.2 and 5.x before 5.48.1 contain a stored cross-site scripting vulnerability in the content manager WYSIWYG preview component that fails to strip script tags from rich text. An Author-role user can store malicious script tags in rich text fields that execute in an Editor or Super Admin's session when the preview pane is expanded, enabling account takeover.

### 4. CVE-2026-81648｜Unknown / CryptoPayment Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-13T21:17:01.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-13T21:17:01.930 / 2026-09-13T21:17:01.930
- **官方描述（原文）**：The CryptoPayment Gateway WordPress plugin from 1.2.1 to 1.2.2 does not apply an authorization check on one of its AJAX endpoints, allowing unauthenticated users to invoke administrative operations, including deleting arbitrary files on the server, overwriting the payment gateway configuration and recovering stored wallet credentials in cleartext.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-86218｜N-able / N-central
- **Title**：N-able N-central Static Code Injection Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.00744 / percentile=0.52733
- **CISA KEV**：listed=true / date_added=2026-09-08 / due_date=2026-09-11
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：N-able N-central contains a static code injection vulnerability that could allow for pre-authentication remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-86060｜MikroTik / RouterOS
- **Title**：MikroTik RouterOS Improper Neutralization of Argument Delimiters in a Command Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.0102 / percentile=0.61439
- **CISA KEV**：listed=true / date_added=2026-09-10 / due_date=2026-09-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：MikroTik RouterOS contains an improper neutralization of argument delimiters in a command vulnerability which allows an attacked to change the trusted RouterOS policy mask, leading to privilege escalation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-85706｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Path Traversal Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.01164 / percentile=0.65458
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contains a path traversal vulnerability that allows an unauthenticated user to read arbitrary files due to an improper path confinement and missing authentication enforcement in the repository commits API.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-84869｜ConnectWise / ScreenConnect
- **Title**：ConnectWise ScreenConnect Improper Privilege Management and Missing Authorization Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：0.00691 / percentile=0.50841
- **CISA KEV**：listed=true / date_added=2026-09-11 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：ConnectWise ScreenConnect contains both an improper privilege management and missing authorization vulnerability that may allow an attacker to file transfer and execution through an active remote sessions without authorization or host confirmation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-82078｜PaperCut / NG/MF
- **Title**：PaperCut NG/MF Unsafe Reflection Vulnerability
- **Risk**：P1 / score 90；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：0.01691 / percentile=0.75778
- **CISA KEV**：listed=true / date_added=2026-08-31 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：PaperCut NG/MF contains an unsafe reflection vulnerability that allows an attacker to manipulate system configuration parameters and execute arbitrary Java bytecode residing on the application classpath under the security context of the PaperCut server process. This vulnerability can be chained with CVE-2026-81578.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-87491｜Google / Chromium V8
- **Title**：Google Chromium V8 Out of Bounds Write Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00859 / percentile=0.56439
- **CISA KEV**：listed=true / date_added=2026-09-09 / due_date=2026-09-23
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium V8 contains an out of bounds write vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-85880｜Microsoft / Windows
- **Title**：Microsoft Windows Heap-Based Buffer Overflow Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.00572 / percentile=0.45512
- **CISA KEV**：listed=true / date_added=2026-09-08 / due_date=2026-09-22
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft Windows Advanced Local Procedure Call contains a heap-based buffer overflow vulnerability that allows an attacker to elevate privileges locally.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2026-85046｜Google / Chromium V8
- **Title**：Google Chromium V8 Type Confusion Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.0126 / percentile=0.67929
- **CISA KEV**：listed=true / date_added=2026-09-04 / due_date=2026-09-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Google Chromium V8 contains a type confusion vulnerability that allows a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-81963｜Microsoft / Windows
- **Title**：Microsoft Windows Link Following Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：0.00631 / percentile=0.48283
- **CISA KEV**：listed=true / date_added=2026-09-08 / due_date=2026-09-22
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Microsoft Windows Update Stack contains a link following vulnerability that allows a local attacker to escalate privileges locally up to SYSTEM.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-81578｜PaperCut / NG/MF
- **Title**：PaperCut NG/MF Missing Authentication for Critical Function Vulnerability
- **Risk**：P1 / score 82；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：0.01617 / percentile=0.74654
- **CISA KEV**：listed=true / date_added=2026-08-31 / due_date=2026-09-14
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：PaperCut NG/MF contains a missing authentication for critical function vulnerability which allows an unauthenticated remote attacker to modify certain system configurations. This vulnerability can be chained with CVE-2026-82078.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-67277 | P1 / 82 | MikroTik / RouterOS | v4.0 8.8 (HIGH) | 0.00856 / percentile=0.56331 | listed=true / date_added=2026-09-10 / due_date=2026-09-13 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-42018 | P1 / 82 | JFrog / Artifactory | v3.1 7.5 (HIGH) | 0.0092 / percentile=0.58299 | listed=true / date_added=2026-09-11 / due_date=2026-09-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-42016 | P1 / 82 | JFrog / Artifactory | v3.1 8.8 (HIGH) | 0.00886 / percentile=0.57248 | listed=true / date_added=2026-09-11 / due_date=2026-09-25 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-66066 | P3 / 49 | rails / rails | v4.0 9.5 (CRITICAL) | 0.27861 / percentile=0.9798 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-43284 | P3 / 47 | Linux / Linux | v3.1 8.8 (HIGH) | 0.93235 / percentile=0.9983 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-42945 | P3 / 45 | F5 / NGINX Plus | v4.0 9.2 (CRITICAL) | 0.68047 / percentile=0.99282 | listed=false | status=none / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-90680 | WATCH / 28 | D-Link / DIR-823G | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-90562 | WATCH / 28 | langbot-app / LangBot | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-90561 | WATCH / 28 | strapi / strapi | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-81648 | WATCH / 28 | Unknown / CryptoPayment Gateway | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：20；缺少 Vendor：0；缺少 Product：0；缺少 Title：7。
- EPSS 未確認：4；Exploitation status 未確認：4。
- 結構化受影響版本未提供：20。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-14T05:34:43.748576+00:00`；Delta generated at：`2026-09-14T05:34:43.748576+00:00`。

---

## 可驗證資料來源

- **CVE-2026-86218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86218) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86218) · [Vendor / Advisory (status.n-able.com)](https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/) · [Vendor / Advisory (me.n-able.com)](https://me.n-able.com/s/security-advisory/aArVy0000002Ld3KAE/cve202686218-preauthentication-remote-code-execution) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-86060** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86060) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85706** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85706) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85706) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-84869** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84869) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84869) · [Vendor / Advisory (connectwise.com)](https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-82078** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82078) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-82078) · [Vendor / Advisory (papercut.com)](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/?lid=2oneu2wt0ct4) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-90680** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90680)
- **CVE-2026-90562** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90562)
- **CVE-2026-90561** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90561)
- **CVE-2026-81648** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81648)
- **CVE-2026-81578** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81578) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-81578) · [Vendor / Advisory (papercut.com)](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87491) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87491) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85880** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85880) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85880) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85046) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-81963** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81963) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-81963) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-67277** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67277) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-67277) · [Vendor / Advisory (mikrotik.com)](https://mikrotik.com/supportsec/september-2026-vulnerability/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-42018** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42018) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42018) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/jfrog-security-advisories) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-42016** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42016) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42016) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/jfrog-security-advisories) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-66066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66066) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-66066)
- **CVE-2026-43284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-43284) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-43284)
- **CVE-2026-42945** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42945) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42945)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
