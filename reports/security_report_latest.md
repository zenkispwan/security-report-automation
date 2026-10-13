# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**50** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=1、NEW_CVE=49。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **1**、WATCH **29**。
- Baseline：state / generated_at=2026-10-12T06:47:58.696313+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **50** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-109390｜AnyDesk / AnyDesk
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T15:17:07.980)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T15:17:07.980 / 2026-10-13T04:17:13.987
- **官方描述（原文）**：AnyDesk before 8.0.3 allows unauthenticated remote attackers to execute arbitrary code via a heap-based buffer overflow, as demonstrated on Linux for command execution as root without the victim approving desktop control. In the stream packet handler for mode 5 in the session protocol, a payload length value is not validated.

### 2. CVE-2026-97229｜GitLab / GitLab
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-13T02:17:00.840)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T02:17:00.840 / 2026-10-13T02:17:00.840
- **官方描述（原文）**：GitLab has remediated an issue in GitLab CE/EE affecting all versions from 19.2 before 19.2.8, 19.3 before 19.3.5, and 19.4 before 19.4.2 that, under certain conditions, could have allowed an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.

### 3. CVE-2026-96119｜IBM / i
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-13T00:17:02.053)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T00:17:02.053 / 2026-10-13T00:17:02.053
- **官方描述（原文）**：IBM i 7.3, 7.4, 7.5, and 7.6 could allow a remote authenticated attacker to obtain sensitive information or execute arbitrary code on the system due to improper data sanitization by the HTTP Server Administration web application.

### 4. CVE-2026-96012｜IBM / Db2 Mirror for i
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T20:17:10.723)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T20:17:10.723 / 2026-10-13T04:17:23.643
- **官方描述（原文）**：IBM Db2 Mirror for i 7.4, 7.5, and 7.6 is vulnerable to privilege escalation. An authenticated attacker could craft a malicious request that bypasses additional authorization and input validation checks to execute malicious code. An attacker could exploit this vulnerability to obtain elevated privileges on the system.

### 5. CVE-2026-93582｜OTRS GmbH (former OTRS AG) / OTRS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T07:16:37.717)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：0.00392 / percentile=0.31323
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T07:16:37.717 / 2026-10-12T07:16:37.717
- **官方描述（原文）**：The HTTP Basic Authentication modules in ((OTRS)) Community Edition 6 and prior accept the authenticated username from either the REMOTE_USER or HTTP_REMOTE_USER environment variable. In CGI and mod_perl based deployments, HTTP request headers may be mapped to corresponding HTTP_* environment variables. As a result, an unauthenticated remote attacker can supply a crafted Remote-User request header which is exposed to the application as HTTP_REMOTE_USER. When HTTP Basic Authentication is configured as the authentication backend, OTRS trusts this value as an already authenticated username and does not perform an additional password verification. An attacker may therefore authenticate through the Generic Interface as an existing agent or customer user without knowing the corresponding credentials. The resulting privileges depend on the account being impersonated. Successful exploitation may allow access to confidential information and modification of data or configuration with the permissions of the affected user. Exploitation requires HTTP Basic Authentication to be configured as an authentication backend and a web server environment in which attacker-controlled HTTP headers are exposed through the corresponding HTTP_* environment variables. OTRS 7 and later are not affected by this attack vector due to the use of Mojolicious/Hypnotoad and does not expose arbitrary request headers through %ENV in the manner required for exploitation. The supported REMOTE_USER mechanism additionally requires validation through the configured SSO shared secret. The unused HTTP_REMOTE_USER fallback has nevertheless been removed as a security-hardening measure. Please note that ((OTRS)) Community Edition 6.x and before are vulnerable. Products based on the ((OTRS)) Community Edition also very likely to be affected

### 6. CVE-2026-92681｜Neo4j / @neo4j/graphql
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T16:17:07.323)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T16:17:07.323 / 2026-10-12T16:17:07.323
- **官方描述（原文）**：In @neo4j/graphql versions up to and including 7.6.3, @authentication directives applied at the schema level or on the Query or Mutation types are silently ignored for top-level fields annotated with @cypher. Only @authentication directives placed directly on the individual fields are enforced. An application that exposes a top-level @cypher field and relies on schema-level or type-level @authentication to protect it allows unauthenticated callers to invoke the field and run the configured Cypher statement with the privileges of the GraphQL service account, which may permit reading and modifying data. Fixed in 7.6.4.

### 7. CVE-2026-9191｜Progress Software Corporation / MarkLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T16:17:08.223)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T16:17:08.223 / 2026-10-12T16:17:08.223
- **官方描述（原文）**：Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not sufficiently isolate user-supplied code executed through certain REST and XDBC evaluation paths from HTTP request, response, and session state. An attacker able to execute code through an affected path could perform unauthorized actions or compromise an authenticated session.

### 8. CVE-2026-90920｜IBM / Maximo AI Service
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T22:17:05.683)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T22:17:05.683 / 2026-10-12T22:17:05.683
- **官方描述（原文）**：IBM Maximo AI Service 9.1.0, and 9.2.0 could allow a remote attacker to execute arbitrary code due to improper control of code generation.

### 9. CVE-2026-89111｜SAP_SE / SAP Cloud
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-13T01:16:47.890)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T01:16:47.890 / 2026-10-13T03:16:41.133
- **官方描述（原文）**：The SAP Cloud SDK for Python contains an OAuth2 SSRF vulnerability affecting multi-tenant BTP applications. An attacker who controls the tenant_subdomain parameter can redirect OAuth2 token requests to an attacker-controlled server, causing client credentials to be exfiltrated.

### 10. CVE-2026-89110｜SAP_SE / SAP NetWeaver Visual Composer
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-13T01:16:47.767)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T01:16:47.767 / 2026-10-13T01:16:47.767
- **官方描述（原文）**：SAP NetWeaver Visual Composer does not perform sufficient authorization checks in certain portal functionality. An attacker with low privileges could invoke internal operations on a preconfigured remote system. Depending on the remote connection configuration, this could lead to a full compromise of the remote system. This results in a high impact on confidentiality, integrity and availability.

### 11. CVE-2026-89108｜SAP_SE / SAP Manufacturing Integration and Intelligence (Configuration Service)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-13T01:16:47.637)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T01:16:47.637 / 2026-10-13T01:16:47.637
- **官方描述（原文）**：SAP Manufacturing Integration and Intelligence does not sufficiently enforce authorization boundaries within certain administrative functionality. An attacker with MII administrator privileges could submit a specially crafted request to provision an account with elevated privileges on the underlying Java application server. Successful exploitation could allow the attacker to gain administrative control over the underlying system, extending the impact beyond the vulnerable application. This results in a high impact on confidentiality, integrity and availability.

### 12. CVE-2026-89107｜SAP_SE / SAP S/4HANA (Manage Substitution/Validation Rules)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-13T01:16:47.507)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T01:16:47.507 / 2026-10-13T01:16:47.507
- **官方描述（原文）**：SAP S/4HANA (Manage Substitution/Validation Rules) does not sufficiently validate input processed by rule definition functionality that utilizes a domain-specific scripting language. An authenticated attacker with specific business privileges could submit specially crafted input, which is interpreted as executable ABAP code by the rule processing logic. Successful exploitation could allow the attacker to execute ABAP arbitrary code into the system, resulting in full compromise of the affected system and high impact on confidentiality, integrity, and availability of the system.

### 13. CVE-2026-87744｜Red Hat / Exploit Intelligence
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T19:16:40.277)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T19:16:40.277 / 2026-10-12T19:16:40.277
- **官方描述（原文）**：A flaw was found in Quarkus REST Data Panache. This vulnerability allows unauthenticated attackers to bypass security controls on generated endpoints. When a developer customizes a specific operation using @MethodProperties without explicitly re-declaring security roles, the code generator silently drops class-level security requirements. This results in the affected endpoint defaulting to permissive, unauthenticated access, potentially leading to unauthorized information disclosure or data modification.

### 14. CVE-2026-87689｜Rapid7 / Metasploit Framework
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-13T01:16:47.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T01:16:47.110 / 2026-10-13T01:16:47.110
- **官方描述（原文）**：The Metasploit Framework Web Service REST API (msf-ws) exposes the credential store through Msf::WebServices::CredentialServlet. Every mutating and read route in this servlet calls warden.authenticate! before processing a request, except the update_credential (PUT) and delete_credentials (DELETE) handlers for /api/v1/credentials, which omit the authentication call entirely. Because these handlers call directly into lib/msf/core/db_manager/cred.rb, which performs no authorization check of its own, any client able to reach the web service on its default 0.0.0.0:8080 listener can read, modify, or permanently delete every stored credential record — including passwords, hashes, and private keys stored for a shared team engagement — without presenting any authentication. All published versions of Metasploit Framework through 6.5.4 are affected. The issue is fixed in 6.5.5 by adding warden.authenticate! as the first statement in both handlers, matching the pattern used by every other route in the API.

### 15. CVE-2026-85956｜Progress Software Corporation / MarkLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T16:17:07.193)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T16:17:07.193 / 2026-10-12T16:17:07.193
- **官方描述（原文）**：Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 allow a remote attacker with delegated database-administrator privileges to perform backup or restore operations on forests outside the authorized database scope, which could result in unauthorized access to or modification of security-critical data.

### 16. CVE-2026-85955｜Progress Software Corporation / MarkLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T16:17:07.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T16:17:07.070 / 2026-10-12T16:17:07.070
- **官方描述（原文）**：Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 allow a remote attacker with query-execution access to invoke an XQuery evaluation function without the additional required evaluation privilege, which could result in server-side code execution with elevated permissions.

### 17. CVE-2026-85948｜Progress Software Corporation / MarkLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T16:17:06.173)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T16:17:06.173 / 2026-10-12T16:17:06.173
- **官方描述（原文）**：Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an XQuery injection flaw in a deprecated Management API package path. A remote attacker with manage-user-level privileges could exploit this flaw to obtain persistent unauthorized administrative control.

### 18. CVE-2026-85947｜Progress Software Corporation / MarkLogic Server
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T16:17:06.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T16:17:06.040 / 2026-10-12T16:17:06.040
- **官方描述（原文）**：Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an authorization flaw in certain forest-management operations. A remote attacker with forest-management privileges could exploit this flaw to create a persistent unauthorized administrator account, potentially resulting in complete unauthorized administrative control of the server.

### 19. CVE-2026-82110｜IBM / DataStage on Cloud Pak for Data
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T23:17:42.533)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T23:17:42.533 / 2026-10-12T23:17:42.533
- **官方描述（原文）**：IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due to improper validation of pathname during a path traversal.

### 20. CVE-2026-82103｜IBM / DataStage on Cloud Pak for Data
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T23:17:42.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T23:17:42.110 / 2026-10-12T23:17:42.110
- **官方描述（原文）**：IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to obtain sensitive information due to an exposure of sensitive information to an unauthorized actor.

### 21. CVE-2026-82101｜IBM / DataStage on Cloud Pak for Data
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T23:17:41.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T23:17:41.897 / 2026-10-12T23:17:41.897
- **官方描述（原文）**：IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to cause a denial of service due to a path traversal vulnerability.

### 22. CVE-2026-78357｜OTRS GmbH (former OTRS AG) / OTRS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T07:16:37.073)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00304 / percentile=0.21413
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T07:16:37.073 / 2026-10-12T07:16:37.073
- **官方描述（原文）**：Previously issued authentication tokens are not immediately invalidated when an OTRS agent or customer user account is deactivated or its password is changed. As a result, an existing JWT may remain valid until its regular expiration time, which can be approximately 16 hours. An attacker who has previously obtained a valid authentication token can therefore continue to access OTRS with the privileges of the affected agent or customer user even after the corresponding account has been deactivated or the user's password has been changed. The vulnerability does not allow an attacker to obtain authentication tokens by itself. Exploitation requires possession of a previously issued and still valid token. The actual impact depends on the privileges associated with the compromised token. Customer user tokens are limited to the permissions of the affected customer account, while agent tokens may provide access to broader ticket, customer, or administrative functionality depending on the assigned permissions. This issue affects OTRS: * 7.0.X * 8.0.X * 2023.X * 2024.X * 2025.X * 2026.X before 2026.7.X

### 23. CVE-2026-77366｜The-40-Thieves / obsidian-tc
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T18:17:23.830)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T18:17:23.830 / 2026-10-12T18:17:23.830
- **官方描述（原文）**：obsidian-tc is a governed, agent-ready Model Context Protocol server for Obsidian vaults. Prior to 1.3.1, tool dispatch does not compare the caller-controlled input.vault value with the vault bound to the caller, the JSON Web Token (JWT) has no vault claim, and the folder access-control list is shared globally. Any valid token can therefore select another configured vault and read, write, or delete its contents through affected tools. Version 1.3.1 fixes the vulnerability by binding tokens and request context to a vault and rejecting mismatched input.vault values before scope checks.

### 24. CVE-2026-57118｜MervinPraison / PraisonAI
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T19:16:38.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T19:16:38.940 / 2026-10-12T19:16:38.940
- **官方描述（原文）**：PraisonAI is a multi-agent teams system. Prior to praisonaiagents 1.6.59, AgentTeam.launch and the Agents alias register GET /{path}/list, POST /{path}, and `POST /{path}/{agent_id}' without access-control checks before listing agents or calling agent.chat. A remotely exposed server can therefore let unauthenticated clients enumerate agents, consume model resources, access connected private context, and trigger agent tools or workflow side effects. This vulnerability is fixed in praisonaiagents 1.6.59.

### 25. CVE-2026-53997｜NetHerman / Portal del Hermano (portaldelhermano.es)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T21:17:17.400)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T21:17:17.400 / 2026-10-12T21:17:17.400
- **官方描述（原文）**：Netherman Portal del Hermano (portaldelhermano.es) before 2026-10-06 contains a broken authentication vulnerability in its password-recovery flow at the POST /password/create-access and POST /password/email endpoints, allowing unauthenticated attackers to take over any member account across all tenants by exploiting the lack of rate limiting and distinct error messages that act as oracles for each of the four identity-verification factors (DNI, date of birth, phone number, last four IBAN digits). Attackers can confirm the DNI via the oracle, brute-force the date of birth and IBAN digits, obtain the phone number through open-source intelligence, then submit an attacker-controlled email field so the password reset link is delivered to them, enabling full account takeover including profile data, full IBAN, and fiscal documents.

### 26. CVE-2026-44828｜Qexo / Qexo
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T22:17:04.160)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T22:17:04.160 / 2026-10-12T22:17:04.160
- **官方描述（原文）**：Qexo is an open source online editor for static blogs. From 4.0.0 until 4.2.0, Qexo exposes /api/init_step/ through init_step_api without authentication, authorization, or a setup-completion guard. An unauthenticated requester with a valid CSRF token obtained from a public page can submit the first initialization step and reset the INIT setting, causing the instance to re-enter the setup flow. The setup response and /init/ page can expose stored PROVIDER configuration, including service credentials, in frontend content. This issue is fixed in version 4.2.0.

### 27. CVE-2026-109758｜Perforce / Helix Authentication Service
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-13T04:17:14.843)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-13T04:17:14.843 / 2026-10-13T04:17:14.843
- **官方描述（原文）**：Perforce Helix Authentication Service (HAS) deployments that retain the shipped default SCIM bearer token are vulnerable to unauthorized access when the SCIM endpoint is reachable by an attacker. In version 25.2, the installation templates contain a default credential which the installer copies into the active configuration; the installer and configuration script do not automatically replace that value with a random token. An attacker who knows the default token can authenticate to the SCIM API and perform user and group operations allowed by the configured provisioning backend. This issue can be chained with CVE-2026-61834 in affected releases of the scim-patch dependency. A crafted SCIM PATCH request can cause server-side prototype pollution, corrupt application state, and disrupt service availability, including health checks and SCIM or SSO requests. In a later test, this primitive was confirmed to enable remote code execution in a Node.js 24/Express deployment through available gadget chains involving child_process, EJS/Pug, or Passport. This vulnerability exists in version 2022.1 - 2025.2 of HAS however the underlying defect was removed in version 2026.1 which was released July 17th 2026. The vulnerability was identified in older versions of HAS after version 2026.1 was released.

### 28. CVE-2026-109575｜HAProxy / Data Plane API EE
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T20:17:09.443)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T20:17:09.443 / 2026-10-12T20:17:09.443
- **官方描述（原文）**：In HAProxy Data Plane API 2.2.0 through 3.4.3 (and corresponding Enterprise Edition releases), Server.ConfigureAPI() has process-global authentication logic that improperly drops security controls across multiple transport types. When a TLS Certificate Authority (tls_ca) is configured and a numeric TLS port (tls_port) is specified, the application globally disables Basic authentication on its shared internal request handler. Because this handler is shared concurrently among HTTP, HTTPS, and UNIX domain socket listeners, and mutual TLS (mTLS) client certificate verification (tls.RequireAndVerifyClientCert) is enforced exclusively on the HTTPS server path, all other simultaneously active non-mTLS listeners fail open. Consequently, an unauthenticated attacker capable of reaching an affected HTTP or UNIX management endpoint can completely bypass credentials to gain full API administrative access. This allows unauthorized remote or local actors to read sensitive, cleartext HAProxy configuration data or replace the managed configuration entirely via the raw configuration endpoint. This has been fixed in versions 3.4.4, 3.3.9, 3.2.17, 3.0.25, 2.9.29, and their respective EE backports by migrating to a per-request TLS connection-state validation model.

### 29. CVE-2026-109573｜thorsten / phpMyFAQ
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T23:17:22.557)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T23:17:22.557 / 2026-10-12T23:17:22.680
- **官方描述（原文）**：phpMyFAQ before 4.1.9 contains an SQL injection vulnerability in PdoMysql::escape(), which escapes single quotes with backslashes that are treated literally when MySQL or MariaDB runs in NO_BACKSLASH_ESCAPES mode. Unauthenticated attackers can send a Unicode right single quotation mark in the search parameter of api/autocomplete, which is normalized to an ASCII quote, to read credentials and configuration secrets, modify records, or drop tables.

### 30. CVE-2026-109569｜Th0rgal / sandboxed.sh
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T21:17:13.653)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T21:17:13.653 / 2026-10-12T21:17:13.653
- **官方描述（原文）**：sandboxed.sh through 1.3.0 contains a container escape vulnerability that allows code in container workspaces to access the host filesystem because nsenter attaches without --root. Agent-run code in a container workspace can resolve absolute paths on the host to read and modify host files, bypassing documented isolation.

### 31. CVE-2026-109566｜zofe / rapyd-admin
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T21:17:13.190)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T21:17:13.190 / 2026-10-12T21:17:13.190
- **官方描述（原文）**：Rapyd Admin from 9.0.0 before 9.20.0 contains a hard-coded credentials vulnerability that allows remote unauthenticated attackers to gain super-admin access through an AuthSeeder-created admin@laravel account with password admin. The account is seeded by the setup installer and silently re-created on every rpd:make run, letting attackers log in as a global super admin bypassing per-record authorization and tenant scoping.

### 32. CVE-2026-109423｜NetEase / NetEase Cloud Music for Windows
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T20:17:08.993)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T20:17:08.993 / 2026-10-12T20:17:08.993
- **官方描述（原文）**：NetEase Cloud Music client for Windows (cloudmusic.exe) versions 3.1.38 and 3.1.39.205426 contains a TLS certificate validation vulnerability that allows a network-adjacent attacker to intercept and decrypt HTTPS traffic by failing to validate the server certificate chain, verify the hostname, or consult any Windows certificate trust store. Attackers can perform a man-in-the-middle attack using a rogue certificate authority to decrypt traffic, capture the MUSIC_U session credential sent in authenticated API requests, and modify server responses in transit, enabling account takeover and transport-layer response forgery.

### 33. CVE-2026-109422｜NetEase / NetEase Cloud Music for Windows
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T20:17:08.840)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T20:17:08.840 / 2026-10-12T20:17:08.840
- **官方描述（原文）**：NetEase Cloud Music client for Windows (cloudmusic.exe) versions 3.1.38 and 3.1.39.205426 contains a remote code execution vulnerability in the renderer-process IPC bridge os.navigateExternal, which passes caller-supplied URLs to ShellExecuteW without validating the URL scheme. An attacker able to inject content into the renderer, such as by forging the /pc/upgrade/get API response using a publicly known AES key over an unvalidated TLS connection, can invoke os.navigateExternal with a file:// URL through an img onerror payload to execute arbitrary local binaries under the logged-in user's account.

### 34. CVE-2026-109399｜sbabic / swupdate
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T16:17:05.557)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T16:17:05.557 / 2026-10-12T16:17:05.557
- **官方描述（原文）**：SWUpdate through 2026.05.1 contains an improper certificate validation vulnerability in crypto/swupdate_cms_verify_openssl.c that trusts untrusted X.509 certificates embedded in CMS SignedData for chain building. Attackers holding a signing key from a sibling intermediate under the same root can embed that intermediate in the signature to install malicious updates.

### 35. CVE-2026-109394｜thirty bees / thirty bees
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T16:17:04.920)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T16:17:04.920 / 2026-10-12T16:17:04.920
- **官方描述（原文）**：Thirty bees through 1.7.0 contains an authentication bypass vulnerability in PasswordController::resolveCustomer() that allows unauthenticated attackers to reset registered customers' passwords using guest account tokens. Attackers can place a guest order with the victim's email, then use the guest secure key to reset and take over the victim's account when guest checkout is enabled.

### 36. CVE-2026-109391｜Square / Squash
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T16:17:04.373)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T16:17:04.373 / 2026-10-12T16:17:04.373
- **官方描述（原文）**：Square Squash through commit e73f280 contains an insecure deserialization vulnerability that allows unauthenticated attackers to store crafted YAML via the POST /api/1.0/symbolication endpoint. When occurrences referencing the attacker-controlled symbolication UUID are symbolicated, the stored values are passed to YAML.load with SafeYAML in unsafe mode, enabling arbitrary Ruby object deserialization and potential code execution.

### 37. CVE-2026-109373｜zitadel / zitadel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T17:17:35.110)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T17:17:35.110 / 2026-10-12T17:17:35.230
- **官方描述（原文）**：ZITADEL 3.0.0 before 4.19.2 contains an authentication bypass vulnerability in the Login V2 UI that allows unauthenticated attackers to obtain other users' session tokens by forging unsigned session cookies. Attackers can guess time-ordered session IDs around a victim's sign-in and supply them with empty tokens to receive rotated tokens, taking over accounts including MFA-completed administrator sessions.

### 38. CVE-2026-109372｜zitadel / zitadel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T17:17:34.800)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T17:17:34.800 / 2026-10-12T17:17:35.053
- **官方描述（原文）**：ZITADEL 4.x before 4.19.2 and 3.x through 3.4.15 contains an authentication bypass in the SAML identity-provider intent callback, which verifies the assertion signature using the provider named in the request URL but resolves the user from the login intent without checking they match. Attackers with organization-administrator permission can register a SAML provider with their own signing key to obtain authenticated sessions as any user linked to another SAML provider on the instance, including in other organizations.

### 39. CVE-2026-109357｜librenms / librenms
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T17:17:33.020)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T17:17:33.020 / 2026-10-12T17:17:33.020
- **官方描述（原文）**：LibreNMS before 26.9.0 contains an LDAP filter injection in ldap-authorization and ad-authorization modes because usernames are inserted unescaped into LDAP search filters and authentication only checks user existence. When REMOTE_USER is not forwarded, unauthenticated attackers can send a wildcard username via HTTP Basic Authorization (PHP_AUTH_USER) to match all users and groups and gain admin access.

### 40. CVE-2026-109321｜getgrav / grav-plugin-login-oauth
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T17:17:27.247)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T17:17:27.247 / 2026-10-12T17:17:27.247
- **官方描述（原文）**：Grav Login OAuth plugin (grav-plugin-login-oauth) before 1.4.3 provisions OAuth accounts as ordinary Grav users with a deterministic <provider>.<id> username and an unsalted MD5 hash of the provider identifier as the password, without disabling password login. Unauthenticated remote attackers who learn or guess a provider identifier can reproduce these credentials and log in, gaining administrative control of privileged accounts.

### 41. CVE-2026-109238｜unclecode / crawl4ai
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T17:17:14.420)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T17:17:14.420 / 2026-10-12T17:17:14.420
- **官方描述（原文）**：Crawl4AI 0.7.0 before 0.9.4 contains a server-side request forgery vulnerability that allows API clients to reach internal addresses by enabling link_preview_config on /crawl requests. Attackers can supply a controlled page with include_external and include_patterns set, causing AsyncUrlSeeder to fetch internal, private, and cloud-metadata links and return their parsed head data.

### 42. CVE-2026-108929｜Netcore / NR268
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T21:17:09.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T21:17:09.410 / 2026-10-12T21:17:09.410
- **官方描述（原文）**：A flaw has been found in Netcore NR268 1.7.121109. The affected element is the function execvp of the file /router/DDNSset.cgi of the component DDNS. Executing a manipulation of the argument Hostname can lead to argument injection. The attack can be launched remotely.

### 43. CVE-2026-108918｜Edimax / BR-6208AC
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T18:17:22.353)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T18:17:22.353 / 2026-10-12T18:17:22.353
- **官方描述（原文）**：A vulnerability was identified in Edimax BR-6208AC 1.32. Impacted is an unknown function of the file /goform/formWlanMP. The manipulation of the argument readE2P leads to command injection. It is possible to initiate the attack remotely. The exploit is publicly available and might be used. The vendor was contacted early about this disclosure but did not respond in any way. This vulnerability only affects products that are no longer supported by the maintainer.

### 44. CVE-2026-108917｜Edimax / BR-6208AC
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T18:17:22.163)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T18:17:22.163 / 2026-10-12T18:17:22.163
- **官方描述（原文）**：A vulnerability was determined in Edimax BR-6208AC 1.32. This issue affects some unknown processing of the file /goform/formAutoFWupgrade. Executing a manipulation of the argument tftpsIP can lead to command injection. The attack may be performed from remote. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way. This vulnerability only affects products that are no longer supported by the maintainer.

### 45. CVE-2026-108907｜Netcore / NR268
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T17:17:13.373)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T17:17:13.373 / 2026-10-12T17:17:13.373
- **官方描述（原文）**：A vulnerability was determined in Netcore NR268 1.7.121109. Affected is the function user_ok of the component CGI Execution. This manipulation causes improper authentication. The attack can be initiated remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 46. CVE-2026-108892｜Linksys / E1700
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T14:17:09.530)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T14:17:09.530 / 2026-10-12T14:17:09.530
- **官方描述（原文）**：A vulnerability was determined in Linksys E1700 1.0.0.4.003. This vulnerability affects the function ssid1MACFilter of the file /goform/ssid1MACFilter of the component Mac Filter. This manipulation of the argument newap_text_%d causes stack-based buffer overflow. The attack may be initiated remotely. The exploit has been publicly disclosed and may be utilized. The vendor was contacted early about this disclosure but did not respond in any way.

### 47. CVE-2026-108362｜Privasys / ra-tls-clients
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T20:17:08.073)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T20:17:08.073 / 2026-10-12T20:17:08.073
- **官方描述（原文）**：Privasys Remote Attestation TLS Clients provides multi-language utilities for verifying attested TLS connections. Prior to 0.11.0, TEE attestation evidence in Privasys attested TLS is accepted without requiring an explicitly authorized platform identity. When a network attacker can forge evidence or extract attestation secrets from a compromised unrevoked platform, the verifier accepts valid measurements from a different unrevoked TEE platform as though they came from the intended Attester. The attacker can impersonate the attested TLS endpoint. This issue is fixed in version 0.11.0.

### 48. CVE-2025-71429｜RVC-Boss / GPT-SoVITS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T21:17:07.817)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T21:17:07.817 / 2026-10-12T21:17:07.817
- **官方描述（原文）**：GPT-SoVITS through 20250606v2pro contains an OS command injection vulnerability in tools/uvr5/vr.py that allows unauthenticated attackers to execute commands via output folder paths. Attackers can enter shell substitutions like $(...) in the UVR5 WebUI output folder textboxes with mp3 or m4a export to run commands as the server user.

### 49. CVE-2020-37279｜karuppiah7890 / easy-pdf-merge
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-12T21:17:05.570)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-12T21:17:05.570 / 2026-10-12T21:17:05.570
- **官方描述（原文）**：easy-pdf-merge 0.1.0 through 0.2.6 contains an OS command injection vulnerability that allows attackers to execute commands by injecting shell metacharacters into source paths, destination path, or maxHeap option. Attackers can supply file names or options containing double quotes, semicolons, $() or backticks, which child_process.exec() runs through a shell with the Node.js process privileges.

### 50. CVE-2025-10162｜Unknown / Admin and Customer Messages After Order for WooCommerce: OrderConvo
- **Delta event**：CVSS_CHANGED (from=7.5; to=8.6)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：0.04437 / percentile=0.91175
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2025-10-07T06:15:32.677 / 2026-10-12T09:16:41.467
- **官方描述（原文）**：The Admin and Customer Messages After Order for WooCommerce: OrderConvo WordPress plugin through 15.1 does not validate the path of files to be downloaded, which could allow unauthenticated users (before version 15.0) and any authenticated user such as a Subscriber (versions 15.0 to 15.1) to read arbitrary files on the server via a path traversal attack; the fix released in version 14 was incomplete and no fixed version is available.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-109390 | P3 / 38 | AnyDesk / AnyDesk | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-97229 | WATCH / 28 | GitLab / GitLab | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-96119 | WATCH / 28 | IBM / i | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-96012 | WATCH / 28 | IBM / Db2 Mirror for i | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93582 | WATCH / 28 | OTRS GmbH (former OTRS AG) / OTRS | v3.1 9.4 (CRITICAL) | 0.00392 / percentile=0.31323 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-92681 | WATCH / 28 | Neo4j / @neo4j/graphql | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-9191 | WATCH / 28 | Progress Software Corporation / MarkLogic Server | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-90920 | WATCH / 28 | IBM / Maximo AI Service | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89111 | WATCH / 28 | SAP_SE / SAP Cloud | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89110 | WATCH / 28 | SAP_SE / SAP NetWeaver Visual Composer | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89108 | WATCH / 28 | SAP_SE / SAP Manufacturing Integration and Intelligence (Configuration Service) | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89107 | WATCH / 28 | SAP_SE / SAP S/4HANA (Manage Substitution/Validation Rules) | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-87744 | WATCH / 28 | Red Hat / Exploit Intelligence | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-87689 | WATCH / 28 | Rapid7 / Metasploit Framework | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-85956 | WATCH / 28 | Progress Software Corporation / MarkLogic Server | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-85955 | WATCH / 28 | Progress Software Corporation / MarkLogic Server | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-85948 | WATCH / 28 | Progress Software Corporation / MarkLogic Server | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-85947 | WATCH / 28 | Progress Software Corporation / MarkLogic Server | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-82110 | WATCH / 28 | IBM / DataStage on Cloud Pak for Data | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-82103 | WATCH / 28 | IBM / DataStage on Cloud Pak for Data | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-82101 | WATCH / 28 | IBM / DataStage on Cloud Pak for Data | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-78357 | WATCH / 28 | OTRS GmbH (former OTRS AG) / OTRS | v3.1 9.1 (CRITICAL) | 0.00304 / percentile=0.21413 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-77366 | WATCH / 28 | The-40-Thieves / obsidian-tc | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-57118 | WATCH / 28 | MervinPraison / PraisonAI | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-53997 | WATCH / 28 | NetHerman / Portal del Hermano (portaldelhermano.es) | v4.0 9.1 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-44828 | WATCH / 28 | Qexo / Qexo | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-109758 | WATCH / 28 | Perforce / Helix Authentication Service | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-109575 | WATCH / 28 | HAProxy / Data Plane API EE | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-109573 | WATCH / 28 | thorsten / phpMyFAQ | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-109569 | WATCH / 28 | Th0rgal / sandboxed.sh | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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
- EPSS 未確認：28；Exploitation status 未確認：26。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-13T07:14:09.345430+00:00`；Delta generated at：`2026-10-13T07:14:09.345430+00:00`。

---

## 可驗證資料來源

- **CVE-2026-109390** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109390)
- **CVE-2026-97229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97229)
- **CVE-2026-96119** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96119)
- **CVE-2026-96012** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96012)
- **CVE-2026-93582** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93582) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93582)
- **CVE-2026-92681** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92681)
- **CVE-2026-9191** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9191)
- **CVE-2026-90920** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90920)
- **CVE-2026-89111** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89111)
- **CVE-2026-89110** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89110)
- **CVE-2026-89108** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89108)
- **CVE-2026-89107** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89107)
- **CVE-2026-87744** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87744)
- **CVE-2026-87689** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87689)
- **CVE-2026-85956** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85956)
- **CVE-2026-85955** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85955)
- **CVE-2026-85948** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85948)
- **CVE-2026-85947** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85947)
- **CVE-2026-82110** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82110)
- **CVE-2026-82103** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82103)
- **CVE-2026-82101** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82101)
- **CVE-2026-78357** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78357) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-78357)
- **CVE-2026-77366** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77366)
- **CVE-2026-57118** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57118)
- **CVE-2026-53997** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53997)
- **CVE-2026-44828** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-44828)
- **CVE-2026-109758** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109758)
- **CVE-2026-109575** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109575)
- **CVE-2026-109573** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109573)
- **CVE-2026-109569** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109569)
- **CVE-2026-109566** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109566)
- **CVE-2026-109423** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109423)
- **CVE-2026-109422** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109422)
- **CVE-2026-109399** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109399)
- **CVE-2026-109394** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109394)
- **CVE-2026-109391** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109391)
- **CVE-2026-109373** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109373)
- **CVE-2026-109372** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109372)
- **CVE-2026-109357** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109357)
- **CVE-2026-109321** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109321)
- **CVE-2026-109238** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109238)
- **CVE-2026-108929** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108929)
- **CVE-2026-108918** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108918)
- **CVE-2026-108917** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108917)
- **CVE-2026-108907** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108907)
- **CVE-2026-108892** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108892)
- **CVE-2026-108362** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108362)
- **CVE-2025-71429** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-71429)
- **CVE-2020-37279** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-37279)
- **CVE-2025-10162** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-10162) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-10162)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
