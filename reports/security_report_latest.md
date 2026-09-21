# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**8** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=8。
- Intelligence 候選：**16** 筆；P1 **7**、P2 **0**、P3 **1**、WATCH **8**。
- Baseline：state / generated_at=2026-09-20T05:33:34.476819+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-65400、CVE-2026-76460、CVE-2026-87886、CVE-2026-87491、CVE-2026-67277。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **8** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-94107｜nivocart / nivocart
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-20T12:17:06.277)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-20T12:17:06.277 / 2026-09-20T12:17:06.277
- **官方描述（原文）**：NivoCart through 2.4.0 contains a predictable password reset token vulnerability in the forgotten.php endpoint that generates recovery codes using substr(md5(mt_rand()), 0, 10). Attackers who know an administrator's email address can request a password reset and predict the token to gain administrative account access without rate limiting or expiration.

### 2. CVE-2026-94097｜Netcore / NBR200V2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-21T00:16:59.793)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-21T00:16:59.793 / 2026-09-21T00:16:59.793
- **官方描述（原文）**：A vulnerability was determined in Netcore NBR200V2 1.3.241127.071246. This affects an unknown part of the file /www/cgi-bin/network_tools of the component CGI Diagnostic Endpoint. This manipulation of the argument param/key/val causes command injection. Remote exploitation of the attack is possible. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 3. CVE-2026-94089｜D-Link / DIR-868L
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-20T21:16:55.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-20T21:16:55.780 / 2026-09-20T21:16:55.780
- **官方描述（原文）**：A vulnerability was determined in D-Link DIR-868L 2.01b05. This issue affects the function strcpy of the file /webfa_authentication.cgi of the component Authentication Handler. Executing a manipulation of the argument id/password can lead to stack-based buffer overflow. The attack can be executed remotely. The exploit has been publicly disclosed and may be utilized.

### 4. CVE-2026-94003｜Comfast / CF-N1-S
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-20T12:17:05.403)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-20T12:17:05.403 / 2026-09-20T12:17:05.403
- **官方描述（原文）**：A vulnerability has been found in Comfast CF-N1-S 2.6.0.1. Impacted is the function get_css_path_from_uri of the file /cgi-bin/mbox-config of the component Web Management Interface. The manipulation leads to stack-based buffer overflow. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used.

### 5. CVE-2026-90817｜Vanderbilt University / REDCap
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-20T13:17:44.973)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-20T13:17:44.973 / 2026-09-20T13:17:44.973
- **官方描述（原文）**：An unauthenticated Remote Code Execution vulnerability was found in the survey passthrough routing and Data Import processing logic, in which a malicious user could potentially exploit it by manipulating HTTP requests to access an unintended controller route from a public survey context and by supplying a crafted file-path/stream parameter during import handling. If successfully exploited, this could allow the attacker to remotely execute arbitrary code on the REDCap server. The attacker does not have to be authenticated in order to exploit this, but exploitation requires knowledge of a valid public survey hash. This vulnerability exists in REDCap 13.3.0 and higher.

### 6. CVE-2026-88857｜OrdaSoft.com / OrdaSoft Joomla Gallery free extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-20T18:16:54.443)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-20T18:16:54.443 / 2026-09-20T18:16:54.443
- **官方描述（原文）**：Joomla Extension - OrdaSoft.com - Authenticated, Privileged Remote Code Execution in OrdaSoft Joomla Gallery extension for Joomla < 6.2.7 - The extensions saveWatermark() copied an uploaded file into a web-accessible directory using the client-supplied filename exactly as sent, with no extension check, no content check, and no filename sanitisation of any kind. An authenticated core.manage user could upload a .php file disguised with an image Content-Type header and execute it directly by requesting the resulting path.

### 7. CVE-2026-88856｜OrdaSoft.com / OrdaSoft Joomla Gallery free extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-20T18:16:54.280)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-20T18:16:54.280 / 2026-09-20T18:16:54.280
- **官方描述（原文）**：Joomla Extension - OrdaSoft.com - Authenticated, Privileged Remote Code Execution in OrdaSoft Joomla Gallery extension for Joomla < 6.2.7 - The extensions updateOSGallery(), reached via task=update_osgallery, read a JSON request body and called the value of a method field as a live PHP function, passing the value of a package field as its single argument, with no allow-list or is_callable() check of any kind. Any function name compatible with a single argument was directly reachable, including system, exec, shell_exec, and passthru.

### 8. CVE-2026-88854｜OrdaSoft.com / OrdaSoft Joomla Gallery free extension for Joomla
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-20T18:16:53.987)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-20T18:16:53.987 / 2026-09-20T18:16:53.987
- **官方描述（原文）**：Joomla Extension - OrdaSoft.com - Unauthenticated SQL Injection in OrdaSoft Joomla Gallery extension for Joomla < 6.2.7 - The extensions showSearchResult() and showSearchResultAjax() read the textsearch/searchText request parameter with $input->getVar(), which is not a real Joomla filter method and falls through to a filter that strips HTML tags but does not touch quotes or SQL syntax. The value is concatenated directly into a LIKE clause with no escaping. The endpoint requires no login of any kind: mod_osgallery_search is a public, commonly-published search box. Any anonymous site visitor can inject a UNION SELECT and read arbitrary database content.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-65400｜Apple / macOS
- **Title**：Apple macOS Improper Authentication Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.10461 / percentile=0.95532
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
- **EPSS**：0.00784 / percentile=0.54529
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
- **EPSS**：0.00254 / percentile=0.1733
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
- **EPSS**：0.00869 / percentile=0.57207
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
- **EPSS**：0.00207 / percentile=0.11161
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
- **EPSS**：0.00276 / percentile=0.20224
- **CISA KEV**：listed=true / date_added=2026-09-18 / due_date=2026-09-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Linux Kernel contains an out-of-bounds write vulnerability in the ebtables SNAT target which allows an ARP sender hardware address rewrite to write directly into a nonlinear socket-buffer fragment backed by a splice-imported file page. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-66066 | P3 / 49 | rails / rails | v4.0 9.5 (CRITICAL) | 0.27861 / percentile=0.98007 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-94107 | WATCH / 28 | nivocart / nivocart | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94097 | WATCH / 28 | Netcore / NBR200V2 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94089 | WATCH / 28 | D-Link / DIR-868L | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-94003 | WATCH / 28 | Comfast / CF-N1-S | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-90817 | WATCH / 28 | Vanderbilt University / REDCap | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-88857 | WATCH / 28 | OrdaSoft.com / OrdaSoft Joomla Gallery free extension for Joomla | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-88856 | WATCH / 28 | OrdaSoft.com / OrdaSoft Joomla Gallery free extension for Joomla | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-88854 | WATCH / 28 | OrdaSoft.com / OrdaSoft Joomla Gallery free extension for Joomla | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：16；缺少 Vendor：0；缺少 Product：0；缺少 Title：9。
- EPSS 未確認：8；Exploitation status 未確認：8。
- 結構化受影響版本未提供：16。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-21T05:41:16.010287+00:00`；Delta generated at：`2026-09-21T05:41:16.010287+00:00`。

---

## 可驗證資料來源

- **CVE-2026-65400** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65400) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65400) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148170) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148171) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148172) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-76460** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-76460) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87886** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87886) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87886) · [Vendor / Advisory (security-advisory.acronis.com)](https://security-advisory.acronis.com/advisories/SEC-10986) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87491) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87491) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-67277** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67277) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-67277) · [Vendor / Advisory (mikrotik.com)](https://mikrotik.com/supportsec/september-2026-vulnerability/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-94107** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94107)
- **CVE-2026-94097** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94097)
- **CVE-2026-94089** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94089)
- **CVE-2026-94003** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-94003)
- **CVE-2026-90817** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90817)
- **CVE-2026-88857** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88857)
- **CVE-2026-88856** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88856)
- **CVE-2026-88854** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88854)
- **CVE-2026-58704** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58704) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-58704) · [Vendor / Advisory (source.android.com)](https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-53266** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53266) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-53266) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/bf84ad7c7a9ede46e31afaa41a1ba06a159e8c87) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/76280b78cc9f23bdc6438e10ad6dff148ef8375b) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/b7e91939ba9be805a62a257fa4e227dffbb88fa0) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/afd64b59c3de9bbbdd3759e834fdc55cda716e0b) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/153ea96c806aea395daba907a4f88480b6ad5093) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/b18675263db1147c8e1cab625400c13a0d87bd2d) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/c9b5ff59feffb92a147a84a5aa28acd2cb8ff4c5) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/67ba971ae02514d85818fe0c32549ab4bfa3bf49) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-66066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66066) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-66066)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
