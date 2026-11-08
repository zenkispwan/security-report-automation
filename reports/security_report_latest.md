# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**10** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=10。
- Intelligence 候選：**30** 筆；P1 **20**、P2 **0**、P3 **0**、WATCH **10**。
- Baseline：state / generated_at=2026-11-07T06:43:17.189212+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-97229、CVE-2026-9586、CVE-2026-9198、CVE-2026-9082、CVE-2026-88772。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **10** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-123966｜Tenda / AC19
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T14:17:01.800)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T14:17:01.800 / 2026-11-07T14:17:01.973
- **官方描述（原文）**：A vulnerability was determined in Tenda AC19 16.03.10.07. Affected by this issue is the function saveParentControlInfo of the file /goform/saveParentControlInfo. This manipulation of the argument deviceId causes heap-based buffer overflow. The attack is possible to be carried out remotely. The exploit has been publicly disclosed and may be utilized.

### 2. CVE-2026-123614｜imgproxy / imgproxy
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T02:16:56.983)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T02:16:56.983 / 2026-11-08T02:16:56.983
- **官方描述（原文）**：imgproxy from 4.0.0 before 4.0.16 contains an integer overflow in the ICO loader that allows remote attackers to trigger a heap buffer overflow via a crafted data_size value. Attackers can submit a crafted ICO image whose data_size wraps the allocation in vips/icoload.c, corrupting heap memory to crash the process or achieve code execution.

### 3. CVE-2026-123551｜OpenIdentityPlatform / OpenAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T02:16:46.603)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T02:16:46.603 / 2026-11-08T02:16:46.603
- **官方描述（原文）**：OpenAM from 14.0.0 before 16.1.4 contains an information disclosure vulnerability that allows unauthenticated attackers to read live session tokens from the notification WebSocket. Attackers can bypass the agent-only check through an unvalidated internal forward on legacy Liberty ID-FF endpoints, collecting iPlanetDirectoryPro tokens to hijack user and administrator sessions.

### 4. CVE-2026-123550｜OpenIdentityPlatform / OpenAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T02:16:46.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T02:16:46.410 / 2026-11-08T02:16:46.410
- **官方描述（原文）**：OpenAM before 16.1.4 contains an authentication bypass vulnerability in its SAML v2.0 service provider that accepts unsigned assertions on the ECP (PAOS) and HTTP-Artifact bindings when WantAssertionsSigned is false. Unauthenticated remote attackers can submit forged assertions to obtain sessions as any mapped user, including administrators, and hijack single sign-on to dependent applications.

### 5. CVE-2026-123549｜OpenIdentityPlatform / OpenAM
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-08T02:16:46.247)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-08T02:16:46.247 / 2026-11-08T02:16:46.247
- **官方描述（原文）**：OpenAM before 16.1.4 fails to enforce the Valid Creation Attributes list during self-registration, allowing anonymous attackers to set restricted attributes including group membership. Attackers can register through the legacy self-service REST endpoint or User Self-Service flow to join administrative groups and gain full administrative control of OpenAM.

### 6. CVE-2026-122041｜Themehigh / Checkout Field Editor for WooCommerce (Pro)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T13:16:36.067)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T13:16:36.067 / 2026-11-07T19:17:25.583
- **官方描述（原文）**：The Checkout Field Editor for WooCommerce (Pro) plugin for WordPress is vulnerable to unauthorized deletion of arbitrary attachments due to a missing capability/ownership check in the ajax_remove_uploaded() function in versions up to, and including, 3.8.0. The handler is registered for both wp_ajax and wp_ajax_nopriv and is gated solely by the 'file_handling_nonce' nonce, which is emitted inside the public checkout page markup (data-nonce attribute) whenever a File Upload checkout field is configured. This makes it possible for unauthenticated attackers to delete arbitrary attachments (including those belonging to other users or posts) by submitting a crafted attachment_id, which can lead to loss of important media and potential denial of service.

### 7. CVE-2026-120984｜Red Hat / Red Hat Build of Keycloak
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T14:17:01.580)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T14:17:01.580 / 2026-11-07T14:17:01.717
- **官方描述（原文）**：A flaw was found in the Keycloak server's client management component. When a client is created or imported with authorization services enabled, the system fails to properly clear an internal session attribute used during the setup process. This allows an authenticated attacker with client management permissions to bypass security controls and upload a malicious JavaScript policy, which is then executed on the server when an authorization request is made. Successful exploitation could allow the attacker to run arbitrary code on the server, potentially compromising the entire system.

### 8. CVE-2026-119075｜themegrill / Registration Form for WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T12:17:44.033)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T12:17:44.033 / 2026-11-07T19:17:19.637
- **官方描述（原文）**：The Registration Form for WooCommerce plugin for WordPress is vulnerable to privilege escalation due to a missing allow-list check in the FormHandler::validate_checkout_fields() function in versions up to, and including, 1.1.4 The My Account registration path (validate_fields()) validates a submitted 'tgwcfb/user-roles' value against the form's configured allowed roles, but the checkout registration path (validate_checkout_fields(), hooked to woocommerce_after_checkout_validation) stores the raw $_POST['user_roles'] value in $this->valid_data without any allow-list enforcement, and add_user_data() then injects that value into woocommerce_new_customer_data as the new account's role. This makes it possible for unauthenticated attackers to elevate their privileges to Administrator by supplying a user_roles=administrator parameter when creating an account during checkout, resulting in full site takeover.

### 9. CVE-2026-118066｜latepoint / Appointment Booking Plugin – LatePoint | Calendar & Scheduling for WordPress
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T12:17:43.717)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T12:17:43.717 / 2026-11-07T12:17:43.833
- **官方描述（原文）**：The Appointment Booking Plugin – LatePoint | Calendar & Scheduling for WordPress plugin for WordPress is vulnerable to Authentication Bypass via Account Takeover in all versions up to, and including, 5.7.6. This is due to the `OsModel::build_conditions_query()` function in `lib/models/model.php` comparing WHERE-clause values against the literal strings `'IS NULL'` and `'IS NOT NULL'` and concatenating a match directly into SQL without binding it as a parameter, a flaw that neither `sanitize_text_field()` nor the 5.7.5 `is_scalar()` hardening guard closes, since both pass the scalar sentinel through unchanged. This makes it possible for unauthenticated attackers to send `params[password_reset_token]=IS NOT NULL` to the public `customer_cabinet__change_password` AJAX route to match every non-null `account_nonse` value, resolving to the lowest-id customer and overwriting that customer's password to an attacker-chosen value — granting full access to their bookings, orders, and PII, and, when the `wp_users_as_customers` option is enabled, takeover of the linked WordPress subscriber or customer-role account. The attacker can first identify the target customer's email by sending `params[order_intent_key]=IS NOT NULL` to the public `steps__start_from_order_intent` route, which returns the name and email from the first matching order intent, and can then self-arm the required 15-minute password-reset freshness window by triggering a reset for that customer directly.

### 10. CVE-2026-104014｜naimurrahmannahid / Naimur Email OTP Verification for WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-07T12:17:41.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-07T12:17:41.313 / 2026-11-07T19:17:17.340
- **官方描述（原文）**：The Naimur Email OTP Verification for WooCommerce plugin for WordPress is vulnerable to authentication bypass in versions up to, and including, 2.1.0. This is due to the plugin's password-reset finalization endpoint (the wp_ajax_nopriv_ceovw_update_new_password action handled by CEOVW_AJAX::update_new_password()) authorizing the reset solely by the presence of a database row marking an email as 'VERIFIED', with no timestamp check, no session binding, and no per-reset token — combined with mark_otp_as_verified_for_reset() leaving the row in that state after a user enters their code (abandoning the flow leaves the row behind), and a scheduled 'ceovw_cleanup_expired_otps_event' cron that has no add_action() handler anywhere in the plugin so cleanup never runs. This makes it possible for unauthenticated attackers to take over any account whose owner previously requested and verified a password-reset code and did not immediately finish choosing a new password — the attacker needs only the victim's email address and a nonce that the plugin itself localizes publicly into the CEOVW_APP global on the WooCommerce account page for logged-out visitors, after which they call the endpoint, overwrite the victim's password, and are returned a live wordpress_logged_in_ session cookie for that user (full site takeover if the account is an administrator).


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-97229｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.6522 / percentile=0.99259
- **CISA KEV**：listed=true / date_added=2026-10-29 / due_date=2026-11-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-9586｜Sangoma / Switchvox
- **Title**：Sangoma Switchvox SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.18979 / percentile=0.97318
- **CISA KEV**：listed=true / date_added=2026-09-02 / due_date=2026-09-05
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Sangoma Switchvox contains a SQL injection vulnerability which allows an unauthenticated remote attacker to execute arbitrary SQL statements against the backend PostgreSQL database using a single crafted request, including database operations and remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-9198｜IBM / Langflow
- **Title**：IBM Langflow Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.28658 / percentile=0.9815
- **CISA KEV**：listed=true / date_added=2026-08-04 / due_date=2026-08-07
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Langflow contains a code injection vulnerability that allows unauthenticated attackers to achieve full remote code execution on default Langflow deployments.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-9082｜Drupal / Core
- **Title**：Drupal Core SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.89381 / percentile=0.99787
- **CISA KEV**：listed=true / date_added=2026-05-22 / due_date=2026-05-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Drupal Core contains a SQL injection vulnerability that could allow for privilege escalation and remote code execution via specially crafted requests sent with the database abstraction API.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-88772｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.76566 / percentile=0.99545
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-88771｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Input Validation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.81894 / percentile=0.99652
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-86950｜Apple / Multiple Products
- **Title**：Apple Multiple Products Out-of-Bounds Write Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.26166 / percentile=0.98005
- **CISA KEV**：listed=true / date_added=2026-09-29 / due_date=2026-10-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apple iOS, macOS, and iPadOS contain an out-of-bounds write vulnerability in CoreGraphics that may lead to arbitrary code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2026-6973｜Ivanti / Endpoint Manager Mobile (EPMM)
- **Title**：Ivanti Endpoint Manager Mobile (EPMM) Improper Input Validation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 7.2 (HIGH)
- **EPSS**：0.34454 / percentile=0.98424
- **CISA KEV**：listed=true / date_added=2026-05-07 / due_date=2026-05-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ivanti Endpoint Manager Mobile (EPMM) contains an improper input validation vulnerability that allows a remotely authenticated user with administrative access to achieve remote code execution.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-48939｜iCagenda / iCagenda
- **Title**：iCagenda Unrestricted Upload of File with Dangerous Type Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.20069 / percentile=0.97462
- **CISA KEV**：listed=true / date_added=2026-07-10 / due_date=2026-07-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：iCagenda contains an unrestricted upload of file with dangerous type vulnerability that allows the upload of arbitrary files in the file attachment feature, ultimately resulting in PHP code upload and execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-48908｜JoomShaper / SP Page Builder
- **Title**：JoomShaper SP Page Builder Unrestricted Upload of File with Dangerous Type Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.89176 / percentile=0.99782
- **CISA KEV**：listed=true / date_added=2026-07-07 / due_date=2026-07-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JoomShaper SP Page Builder contains an unrestricted upload of file with dangerous type vulnerability that allows unauthenticated users to upload arbitrary files, ultimately resulting in the upload and execution of PHP code.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-45321 | P1 / 100 | TanStack / TanStack | v3.1 9.6 (CRITICAL) | 0.03278 / percentile=0.885 | listed=true / date_added=2026-05-27 / due_date=2026-06-10 | status=known_exploited / source=cisa_kev | Known |
| CVE-2026-42208 | P1 / 100 | BerriAI / LiteLLM | v4.0 9.3 (CRITICAL) | 0.8942 / percentile=0.99788 | listed=true / date_added=2026-05-08 / due_date=2026-05-11 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-111497 | P1 / 100 | Google / Brotli | v4.0 9.2 (CRITICAL) | 0.82641 / percentile=0.99669 | listed=true / date_added=2026-10-27 / due_date=2026-11-10 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-110447 | P1 / 100 | Collabora / Collabora Online – Built-in CODE Server | v4.0 9.2 (CRITICAL) | 0.73307 / percentile=0.99464 | listed=true / date_added=2026-10-23 / due_date=2026-10-26 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-109619 | P1 / 100 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.99999 / percentile=0.99999 | listed=true / date_added=2026-10-26 / due_date=2026-10-29 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-109618 | P1 / 100 | PHP Group / PHP | v4.0 9.2 (CRITICAL) | 0.99999 / percentile=0.99999 | listed=true / date_added=2026-10-26 / due_date=2026-10-29 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-105134 | P1 / 100 | Ahsay / AhsayCBS | v4.0 10.0 (CRITICAL) | 0.81763 / percentile=0.99647 | listed=true / date_added=2026-10-14 / due_date=2026-10-17 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-68645 | P1 / 100 | Synacor / Zimbra Collaboration Suite (ZCS) | v3.1 8.8 (HIGH) | 0.48873 / percentile=0.98885 | listed=true / date_added=2026-01-22 / due_date=2026-02-12 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2025-68613 | P1 / 100 | n8n / n8n | v3.1 8.8 (HIGH) | 0.98994 / percentile=0.9993 | listed=true / date_added=2026-03-11 / due_date=2026-03-25 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2023-4911 | P1 / 100 | GNU / GNU C Library | v3.1 7.8 (HIGH) | 0.63769 / percentile=0.99226 | listed=true / date_added=2023-11-21 / due_date=2023-12-12 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-123966 | WATCH / 28 | Tenda / AC19 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-123614 | WATCH / 28 | imgproxy / imgproxy | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-123551 | WATCH / 28 | OpenIdentityPlatform / OpenAM | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-123550 | WATCH / 28 | OpenIdentityPlatform / OpenAM | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-123549 | WATCH / 28 | OpenIdentityPlatform / OpenAM | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-122041 | WATCH / 28 | Themehigh / Checkout Field Editor for WooCommerce (Pro) | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-120984 | WATCH / 28 | Red Hat / Red Hat Build of Keycloak | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-119075 | WATCH / 28 | themegrill / Registration Form for WooCommerce | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-118066 | WATCH / 28 | latepoint / Appointment Booking Plugin – LatePoint \| Calendar & Scheduling for WordPress | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-104014 | WATCH / 28 | naimurrahmannahid / Naimur Email OTP Verification for WooCommerce | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：10。
- EPSS 未確認：10；Exploitation status 未確認：7。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-08T06:49:44.174201+00:00`；Delta generated at：`2026-11-08T06:49:44.174201+00:00`。

---

## 可驗證資料來源

- **CVE-2026-97229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97229) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97229) · [Vendor / Advisory (ruby-lang.org)](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9586** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9586) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9586) · [Vendor / Advisory (sangomakb.atlassian.net)](https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9198) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9198) · [Vendor / Advisory (ibm.com)](https://www.ibm.com/support/pages/node/7278927) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9082) · [Vendor / Advisory (drupal.org)](https://www.drupal.org/sa-core-2026-004)
- **CVE-2026-88772** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88772) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-123966** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123966)
- **CVE-2026-123614** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123614)
- **CVE-2026-123551** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123551)
- **CVE-2026-123550** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123550)
- **CVE-2026-123549** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123549)
- **CVE-2026-122041** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122041)
- **CVE-2026-120984** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120984)
- **CVE-2026-119075** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119075)
- **CVE-2026-118066** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118066)
- **CVE-2026-104014** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104014)
- **CVE-2026-88771** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88771) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88771) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772)
- **CVE-2026-86950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86950) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86950) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149226) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149228) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149229) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-6973** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-6973) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-6973) · [Vendor / Advisory (hub.ivanti.com)](https://hub.ivanti.com/s/article/May-2026-Security-Advisory-Ivanti-Endpoint-Manager-Mobile-EPMM-Multiple-CVEs?language=en_US)
- **CVE-2026-48939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48939) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48939) · [Vendor / Advisory (icagenda.com)](https://www.icagenda.com/#download) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48908) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48908) · [Vendor / Advisory (extensions.joomla.org)](https://extensions.joomla.org/extension/sp-page-builder/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-45321** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45321) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-45321) · [Vendor / Advisory (github.com)](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)
- **CVE-2026-42208** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42208) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42208) · [Vendor / Advisory (github.com)](https://github.com/BerriAI/litellm/security/advisories/GHSA-r75f-5x8p-qvmc)
- **CVE-2026-111497** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-111497) · [Vendor / Advisory (github.com)](https://github.com/google/brotli/releases/tag/v1.2.1) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-110447** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110447) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-110447) · [Vendor / Advisory (help.nextcloud.com)](https://help.nextcloud.com/t/to-collabora-built-in-user-update-asap/250516) · [Vendor / Advisory (github.com)](https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-109619** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109619) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109619) · [Vendor / Advisory (php.net)](https://www.php.net/) · [CISA](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-109618** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-109618) · [Vendor / Advisory (php.net)](https://www.php.net/) · [CISA](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-105134** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105134) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105134) · [Vendor / Advisory (ahsay.com)](https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-68645** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-68645) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-68645) · [Vendor / Advisory (wiki.zimbra.com)](https://wiki.zimbra.com/wiki/Security_Center)
- **CVE-2025-68613** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-68613) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (github.com)](https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp)
- **CVE-2023-4911** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-4911) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-4911) · [Vendor / Advisory (sourceware.org)](https://sourceware.org/git/?p=glibc.git) · [Vendor / Advisory (access.redhat.com)](https://access.redhat.com/security/cve/cve-2023-4911) · [Vendor / Advisory (debian.org)](https://www.debian.org/security/2023/dsa-5514)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
