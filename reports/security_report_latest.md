# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**8** 筆符合目前門檻的重要變化；事件統計：EPSS_INCREASED=6、NEW_CVE=2。
- Intelligence 候選：**30** 筆；P1 **28**、P2 **0**、P3 **0**、WATCH **2**。
- Baseline：state / generated_at=2026-10-25T05:31:38.364189+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-9082、CVE-2026-88779、CVE-2026-88772、CVE-2026-88771、CVE-2026-21589。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **8** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-9082｜Drupal / Core
- **Delta event**：EPSS_INCREASED (from=0.15701; to=0.89381)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.89381 / percentile=0.99782
- **CISA KEV**：listed=true / date_added=2026-05-22 / due_date=2026-05-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-05-20T20:16:41.230 / 2026-10-07T19:17:45.637
- **官方描述（原文）**：Drupal Core contains a SQL injection vulnerability that could allow for privilege escalation and remote code execution via specially crafted requests sent with the database abstraction API.

### 2. CVE-2026-88779｜Citrix / NetScaler
- **Delta event**：EPSS_INCREASED (from=0.00592; to=0.11388)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.11388 / percentile=0.95963
- **CISA KEV**：listed=true / date_added=2026-10-04 / due_date=2026-10-07
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-04T04:16:43.680 / 2026-10-05T13:35:24.663
- **官方描述（原文）**：Citrix NetScaler ADC (formerly Citrix ADC) and Citrix NetScaler Gateway (formerly Citrix Gateway) contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for a denial of service.

### 3. CVE-2026-88772｜Citrix / NetScaler
- **Delta event**：EPSS_INCREASED (from=0.05305; to=0.78162)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.78162 / percentile=0.99574
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-27T17:16:56.390 / 2026-09-28T12:26:47.670
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service

### 4. CVE-2026-88771｜Citrix / NetScaler
- **Delta event**：EPSS_INCREASED (from=0.05108; to=0.8216)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.8216 / percentile=0.99652
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-09-27T17:16:56.260 / 2026-09-29T04:18:01.603
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands.

### 5. CVE-2026-21589｜Atlassian / Multiple Products
- **Delta event**：EPSS_INCREASED (from=0.12711; to=0.99477)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.99477 / percentile=0.99943
- **CISA KEV**：listed=true / date_added=2026-10-15 / due_date=2026-10-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-05T22:16:58.423 / 2026-10-19T20:31:57.050
- **官方描述（原文）**：Multiple Atlassian products (Bitbucket Data Center ,Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye) contain a files or directories accessible to external parties vulnerability which could allow an unauthenticated attacker to access specific files within the web application root directory in affected versions.

### 6. CVE-2026-105133｜Ahsay / AhsayCBS
- **Delta event**：EPSS_INCREASED (from=0.05794; to=0.79236)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.79236 / percentile=0.99595
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-04T07:16:33.087 / 2026-10-15T13:47:06.283
- **官方描述（原文）**：Ahsay AhsayCBS contains an improper authentication vulnerability that could allow a remote attacker to bypass authentication via manipulation of the random parameter in the API component’s checkSysPwd function. This vulnerability can be chained with CVE-2026-105134.

### 7. CVE-2026-116199｜grokability / snipe-it
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-25T14:17:00.593)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-25T14:17:00.593 / 2026-10-25T14:17:00.593
- **官方描述（原文）**：Snipe-IT before 8.6.3 contains an authentication bypass in GoogleAuthController::handleGoogleCallback, which logs in the user whose username matches the Google account email without enforcing the activated flag. Deactivated users with email-shaped usernames and still-live Google identities can sign in via Google SSO and regain sessions at their original permission level, including admin.

### 8. CVE-2026-116163｜parse-community / parse-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-25T14:16:55.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-25T14:16:55.110 / 2026-10-25T14:16:55.110
- **官方描述（原文）**：Parse Server before 8.6.102 and 9.0.0 before 9.10.5-alpha.2 contains an authentication bypass because the validateSetUp, validateLogin, and validateUpdate methods of custom adapters subclassing AuthAdapter are never called, and an inherited default that accepts any authData is used instead. Attackers can supply arbitrary authData to sign up, link identities, log in as existing users, or skip custom additional authentication factors.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-9082｜Drupal / Core
- **Title**：Drupal Core SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.89381 / percentile=0.99782
- **CISA KEV**：listed=true / date_added=2026-05-22 / due_date=2026-05-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Drupal Core contains a SQL injection vulnerability that could allow for privilege escalation and remote code execution via specially crafted requests sent with the database abstraction API.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-88779｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：0.11388 / percentile=0.95963
- **CISA KEV**：listed=true / date_added=2026-10-04 / due_date=2026-10-07
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC (formerly Citrix ADC) and Citrix NetScaler Gateway (formerly Citrix Gateway) contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for a denial of service.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-88772｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.78162 / percentile=0.99574
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-88771｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Input Validation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.8216 / percentile=0.99652
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-21589｜Atlassian / Multiple Products
- **Title**：Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.99477 / percentile=0.99943
- **CISA KEV**：listed=true / date_added=2026-10-15 / due_date=2026-10-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Multiple Atlassian products (Bitbucket Data Center ,Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye) contain a files or directories accessible to external parties vulnerability which could allow an unauthenticated attacker to access specific files within the web application root directory in affected versions.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-105133｜Ahsay / AhsayCBS
- **Title**：Ahsay AhsayCBS Improper Authentication Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.79236 / percentile=0.99595
- **CISA KEV**：listed=true / date_added=2026-10-14 / due_date=2026-10-17
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ahsay AhsayCBS contains an improper authentication vulnerability that could allow a remote attacker to bypass authentication via manipulation of the random parameter in the API component’s checkSysPwd function. This vulnerability can be chained with CVE-2026-105134.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-9586｜Sangoma / Switchvox
- **Title**：Sangoma Switchvox SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.18979 / percentile=0.97281
- **CISA KEV**：listed=true / date_added=2026-09-02 / due_date=2026-09-05
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Sangoma Switchvox contains a SQL injection vulnerability which allows an unauthenticated remote attacker to execute arbitrary SQL statements against the backend PostgreSQL database using a single crafted request, including database operations and remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2026-9198｜IBM / Langflow
- **Title**：IBM Langflow Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.28658 / percentile=0.98124
- **CISA KEV**：listed=true / date_added=2026-08-04 / due_date=2026-08-07
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Langflow contains a code injection vulnerability that allows unauthenticated attackers to achieve full remote code execution on default Langflow deployments.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-63077｜JetBrains / TeamCity
- **Title**：JetBrains TeamCity Deserialization of Untrusted Data Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_CRITICAL(+20)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=true / date_added=2026-08-05 / due_date=2026-08-08
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JetBrains TeamCity contains a deserialization of untrusted data vulnerability that could allow unauthenticated remote code execution via the agent polling protocol.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-63030｜WordPress / Core
- **Title**：WordPress Core Interpretation Conflict Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.10649 / percentile=0.95766
- **CISA KEV**：listed=true / date_added=2026-07-21 / due_date=2026-07-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WordPress Core contains an interpretation conflict vulnerability that could allow an attacker to perform SQL Injection and achieve Remote Code Execution. This vulnerability can be chained with CVE-2026-60137.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-48939 | P1 / 100 | iCagenda / iCagenda | v4.0 10.0 (CRITICAL) | 0.20069 / percentile=0.97426 | listed=true / date_added=2026-07-10 / due_date=2026-07-13 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-48908 | P1 / 100 | JoomShaper / SP Page Builder | v4.0 10.0 (CRITICAL) | 0.88512 / percentile=0.9977 | listed=true / date_added=2026-07-07 / due_date=2026-07-10 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-24061 | P1 / 100 | GNU / InetUtils | v3.1 9.8 (CRITICAL) | 0.98984 / percentile=0.99929 | listed=true / date_added=2026-01-26 / due_date=2026-02-16 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-20316 | P1 / 100 | Cisco / Secure Firewall Management Center (FMC) | v3.1 5.3 (MEDIUM) | 0.35096 / percentile=0.98427 | listed=true / date_added=2026-07-29 / due_date=2026-08-01 | status=known_exploited / source=cisa_kev | Known |
| CVE-2026-20230 | P1 / 100 | Cisco / Unified Communications Manager | v3.1 8.6 (HIGH) | 0.882 / percentile=0.99765 | listed=true / date_added=2026-06-25 / due_date=2026-06-28 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-15410 | P1 / 100 | SonicWall / SMA1000 Appliances | v3.1 7.2 (HIGH) | 0.11791 / percentile=0.9605 | listed=true / date_added=2026-07-14 / due_date=2026-07-17 | status=known_exploited / source=cisa_kev | Known |
| CVE-2026-15409 | P1 / 100 | SonicWall / SMA1000 Appliances | v3.1 10.0 (CRITICAL) | 0.06795 / percentile=0.93953 | listed=true / date_added=2026-07-14 / due_date=2026-07-17 | status=known_exploited / source=cisa_kev | Known |
| CVE-2025-9377 | P1 / 100 | TP-Link / Multiple Routers | v4.0 8.6 (HIGH) | 0.37731 / percentile=0.98532 | listed=true / date_added=2025-09-03 / due_date=2025-09-24 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-68613 | P1 / 100 | n8n / n8n | v3.1 8.8 (HIGH) | 0.98994 / percentile=0.99929 | listed=true / date_added=2026-03-11 / due_date=2026-03-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-64446 | P1 / 100 | Fortinet / FortiWeb | v3.1 9.8 (CRITICAL) | 0.91078 / percentile=0.99806 | listed=true / date_added=2025-11-14 / due_date=2025-11-21 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-62593 | P1 / 100 | Ray-Project / Ray | v4.0 9.4 (CRITICAL) | 0.62459 / percentile=0.9918 | listed=true / date_added=2026-08-17 / due_date=2026-08-20 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-60710 | P1 / 100 | Microsoft / Windows | v3.1 7.8 (HIGH) | 0.04614 / percentile=0.9162 | listed=true / date_added=2026-04-13 / due_date=2026-04-27 | status=known_exploited / source=cisa_kev | Known |
| CVE-2025-55182 | P1 / 100 | Meta / React Server Components | v3.1 10.0 (CRITICAL) | 0.99802 / percentile=0.99957 | listed=true / date_added=2025-12-05 / due_date=2025-12-12 | status=known_exploited / source=cisa_kev | Known |
| CVE-2025-53690 | P1 / 100 | Sitecore / Multiple Products | v3.1 9.0 (CRITICAL) | 0.60601 / percentile=0.99139 | listed=true / date_added=2025-09-04 / due_date=2025-09-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-96951 | P1 / 95 | Microsoft / Windows | v3.1 8.8 (HIGH) | 0.09813 / percentile=0.95515 | listed=true / date_added=2026-10-13 / due_date=2026-10-16 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-42018 | P1 / 95 | JFrog / Artifactory | v3.1 7.5 (HIGH) | 0.09805 / percentile=0.95513 | listed=true / date_added=2026-09-11 / due_date=2026-09-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-18577 | P1 / 95 | N-able / N-central | v4.0 8.2 (HIGH) | 0.14622 / percentile=0.9663 | listed=true / date_added=2026-08-03 / due_date=2026-08-06 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-65400 | P1 / 90 | Apple / macOS | v3.1 9.8 (CRITICAL) | 0.01723 / percentile=0.77344 | listed=true / date_added=2026-08-18 / due_date=2026-08-21 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-116199 | WATCH / 28 | grokability / snipe-it | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-116163 | WATCH / 28 | parse-community / parse-server | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：2。
- EPSS 未確認：3；Exploitation status 未確認：2。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-26T05:37:14.235919+00:00`；Delta generated at：`2026-10-26T05:37:14.235919+00:00`。

---

## 可驗證資料來源

- **CVE-2026-9082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9082) · [Vendor / Advisory (drupal.org)](https://www.drupal.org/sa-core-2026-004)
- **CVE-2026-88779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88779) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88779) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-88772** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88772) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-88771** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88771) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88771) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772)
- **CVE-2026-21589** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21589) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (confluence.atlassian.com)](https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html?ref=labs.watchtowr.com) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-105133** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105133) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105133) · [Vendor / Advisory (ahsay.com)](https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-116199** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116199)
- **CVE-2026-116163** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116163)
- **CVE-2026-9586** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9586) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9586) · [Vendor / Advisory (sangomakb.atlassian.net)](https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9198) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9198) · [Vendor / Advisory (ibm.com)](https://www.ibm.com/support/pages/node/7278927) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-63077** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63077) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (blog.jetbrains.com)](https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/) · [Vendor / Advisory (jetbrains.com)](https://www.jetbrains.com/privacy-security/issues-fixed/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-63030** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63030) · [Vendor / Advisory (wordpress.org)](https://wordpress.org/news/2026/07/wordpress-7-0-2-release/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48939) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48939) · [Vendor / Advisory (icagenda.com)](https://www.icagenda.com/#download) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48908) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48908) · [Vendor / Advisory (extensions.joomla.org)](https://extensions.joomla.org/extension/sp-page-builder/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-24061** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-24061) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-24061) · [Vendor / Advisory (cgit.git.savannah.gnu.org)](https://cgit.git.savannah.gnu.org/cgit/inetutils.git) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/ccba9f748aa8d50a38d7748e2e60362edd6a32cc) · [Vendor / Advisory (codeberg.org)](https://codeberg.org/inetutils/inetutils/commit/fd702c02497b2f398e739e3119bed0b23dd7aa7b)
- **CVE-2026-20316** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20316) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20316) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-20230** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20230) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20230) · [Vendor / Advisory (cisco.com)](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cucm-ssrf-cXPnHcW.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-15410** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15410) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-15410) · [Vendor / Advisory (psirt.global.sonicwall.com)](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0008) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-15409** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15409) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-15409) · [Vendor / Advisory (psirt.global.sonicwall.com)](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0008) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-9377** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-9377) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-9377) · [Vendor / Advisory (tp-link.com)](https://www.tp-link.com/us/support/faq/4308/)
- **CVE-2025-68613** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-68613) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (github.com)](https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp)
- **CVE-2025-64446** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-64446) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-64446) · [Vendor / Advisory (fortiguard.com)](https://www.fortiguard.com/psirt/FG-IR-25-910)
- **CVE-2025-62593** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-62593) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-62593) · [Vendor / Advisory (github.com)](https://github.com/ray-project/ray/security/advisories/GHSA-q279-jhrf-cc6v) · [Vendor / Advisory (github.com)](https://github.com/ray-project/ray/commit/70e7c72780bdec075dba6cad1afe0832772bfe09) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-60710** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-60710) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-60710)
- **CVE-2025-55182** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-55182) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-55182) · [Vendor / Advisory (react.dev)](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components) · [Vendor / Advisory (github.com)](https://github.com/vercel-labs/fix-react2shell-next?tab=readme-ov-file)
- **CVE-2025-53690** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-53690) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-53690) · [Vendor / Advisory (support.sitecore.com)](https://support.sitecore.com/kb?id=kb_article_view&sysparm_article=KB1003865)
- **CVE-2026-96951** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96951) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-96951) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-96951)
- **CVE-2026-42018** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42018) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42018) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/jfrog-security-advisories) · [Vendor / Advisory (docs.jfrog.com)](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-18577** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18577) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-18577) · [Vendor / Advisory (documentation.n-able.com)](https://documentation.n-able.com/N-central/Release_Notes/GA/Content/N-central_2026.3_HF1_Release_Notes.htm) · [Vendor / Advisory (status.n-able.com)](https://status.n-able.com/2026/08/02/n-central-2026-3-hotfix-1-mitigation-for-cve-2026-18577/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-65400** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65400) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-65400) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148170) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148171) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/148172) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
