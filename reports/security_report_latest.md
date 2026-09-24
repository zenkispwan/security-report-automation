# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**69** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=69。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **3**、WATCH **27**。
- Baseline：state / generated_at=2026-09-23T05:23:24.189900+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **69** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-96758｜orval-labs / orval
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:25.083)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:25.083 / 2026-09-23T19:19:54.890
- **官方描述（原文）**：orval @orval/core before 8.28.0 contains a code injection vulnerability in the form-data serializer that fails to escape multipart property names in generated template literals. Attackers can inject ${...} expressions into OpenAPI schema property names that execute as live interpolation when the generated client builds FormData bodies with consumer process privileges.

### 2. CVE-2026-96757｜orval-labs / orval
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:24.923)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:24.923 / 2026-09-23T18:17:12.200
- **官方描述（原文）**：orval before 8.29.0 fails to escape OpenAPI media-type keys when emitting them into single-quoted Content-Type string literals in generated code. Attackers can inject JavaScript through crafted media-type keys in OpenAPI specifications that executes when generated fetch operations or mock resolvers are invoked.

### 3. CVE-2026-95848｜moquette-io / moquette
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:21.947)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:21.947 / 2026-09-23T19:19:53.790
- **官方描述（原文）**：Moquette is a lightweight Java MQTT broker. Prior to 0.18.1, when a configured authenticator or authorizator class cannot be loaded, Server.initializeAuthenticator and Server.initializeAuthorizatorPolicy treat the failure as though no custom class was configured and fall back to AcceptAllAuthenticator or PermitAllAuthorizatorPolicy. A misspelled class name, missing dependency, constructor failure, or classpath problem can therefore start the broker with authentication or authorization disabled even though the operator configured those controls. This issue is fixed in version 0.18.1.

### 4. CVE-2026-96673｜Photoview / Photoview
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T16:16:50.183)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T16:16:50.183 / 2026-09-23T17:17:24.103
- **官方描述（原文）**：Photoview through 2.4.0 contains an SQL injection vulnerability in the album download route that allows unauthenticated attackers to inject SQL by manipulating the album_id path segment. Attackers can supply crafted SQL expressions in the album_id parameter to extract arbitrary data from the database using time-based or blind injection techniques.

### 5. CVE-2026-96599｜isotope / isotope-core
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T15:17:33.237)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T15:17:33.237 / 2026-09-23T16:16:49.690
- **官方描述（原文）**：Isotope eCommerce through 2.9.10 derives order identifiers from uniqid() instead of a cryptographically secure source, allowing unauthenticated attackers to guess identifiers. Guest orders lack ownership verification, enabling attackers to access order details including billing address, customer information, and purchased files by supplying a guessed uid parameter.

### 6. CVE-2026-96541｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:54.080)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:54.080 / 2026-09-23T20:17:25.950
- **官方描述（原文）**：A denial-of-service flaw was found in gnome-remote-desktop. An unauthenticated remote attacker can open RDP connections without completing the handshake and retain the connection-throttling slots indefinitely because no pre-authentication handshake deadline is enforced. By exhausting the global connection limit, an attacker can prevent new RDP clients from connecting until a holding socket is closed.

### 7. CVE-2026-95847｜moquette-io / moquette
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:21.780)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:21.780 / 2026-09-23T18:12:04.247
- **官方描述（原文）**：Moquette is a lightweight Java MQTT broker. Prior to 0.18.1, H2PersistentQueue derives a session's message-map name as queue_ plus the client ID and its metadata-map name as queue_ plus the client ID plus _meta. A durable session whose client ID ends in _meta can therefore make its message map collide with another client's metadata map. The colliding sessions read and write the same H2 MVStore map with incompatible value types, which can corrupt queue head and tail data and cause message loss, misdelivery, failed queue reloads, or exposure of queued content across sessions. This issue is fixed in version 0.18.1.

### 8. CVE-2026-95843｜moquette-io / moquette
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:21.130)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:21.130 / 2026-09-23T18:17:11.630
- **官方描述（原文）**：Moquette is a lightweight Java MQTT broker. Prior to 0.18.1, PostOffice.subscribe parses a shared-subscription filter through SharedSubscriptionUtils.extractShareName before validating the complete $share/{shareName}/{topicFilter} structure. A remote client can send a filter such as $share/grp without a topic-filter portion, causing a StringIndexOutOfBoundsException while calculating the share name. The exception terminates command handling on the shared session event loop and can deny service to other client sessions assigned to that loop. This issue is fixed in version 0.18.1.

### 9. CVE-2026-95842｜moquette-io / moquette
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:20.970)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:20.970 / 2026-09-23T18:12:04.247
- **官方描述（原文）**：Moquette is a lightweight Java MQTT broker. Prior to 0.18.1, SessionEventLoop.run catches only InterruptedException, and SessionEventLoopGroup does not restart a terminated loop. An MQTT command that raises an uncaught exception can terminate an event loop shared by multiple client sessions, preventing every co-located client from processing PUBLISH, SUBSCRIBE, PUBACK, and other commands. An attacker can select client IDs that map across the available loops to disrupt session processing for the entire broker. This issue is fixed in version 0.18.1.

### 10. CVE-2026-93349｜frictionlessdata / frictionless-py
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:19.653)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:19.653 / 2026-09-23T19:19:44.883
- **官方描述（原文）**：Frictionless through 5.20.0rc1 contains an OS command injection vulnerability in the explore console command that allows an attacker who supplies a crafted Data Package descriptor to execute arbitrary operating system commands as the user who explores it. Attackers can place shell metacharacters in resource path values within a datapackage.json descriptor, which are passed unsanitized to os.system through a shell, causing arbitrary command execution in the victim's security context when they run the explore command against the untrusted package.

### 11. CVE-2026-91775｜LimeSurvey / LimeSurvey
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T18:17:11.097)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T18:17:11.097 / 2026-09-23T18:17:11.253
- **官方描述（原文）**：LimeSurvey fails to safely encode attacker-controlled content from a crafted .lss survey file when displaying import warnings, resulting in XSS in the administrative interface.

### 12. CVE-2026-86064｜klever-io / klever-go
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T20:17:19.960)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T20:17:19.960 / 2026-09-23T20:17:20.117
- **官方描述（原文）**：Klever-Go is the Go implementation of the Klever blockchain protocol. Prior to 1.7.20, the default-open GET /log WebSocket route configured in config/node/api.yaml and registered by network/api/api.go does not require authentication. The first client message is parsed as a logger Profile in network/api/logs/logSender.go and applied process-wide through Profile.Apply, allowing a remote client to change global log levels and formatting options until the connection closes. The same connection is registered as a log observer and can receive live process logs. An attacker can suppress normal logs, increase verbosity, distort operator visibility, and access operational information without credentials. This issue is fixed in version 1.7.20.

### 13. CVE-2026-82407｜klever-io / klever-go
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T20:17:16.707)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.0 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T20:17:16.707 / 2026-09-23T20:17:16.847
- **官方描述（原文）**：Klever-Go is the Go implementation of the Klever blockchain protocol. Prior to 1.7.20, core/kapp/validators/validators.go Register and the runtime validator update path accept a submitted BLSPublicKey without curve, prime-order subgroup, or nonzero validation. When a validator with a malformed key becomes eligible and is selected into a consensus group, MultiSigner.Reset and the corresponding signature verification creation path cannot deserialize the group key and cancel the slot. This causes repeated missed rounds and throughput degradation, and a network whose consensus group equals the eligible validator set can halt completely. Genesis validation is not affected because that path already performs CheckPublicKeyValid. This issue is fixed in version 1.7.20.

### 14. CVE-2026-77601｜OpenC3 / cosmos
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:18.380)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:18.380 / 2026-09-23T20:17:16.027
- **官方描述（原文）**：OpenC3 COSMOS provides the functionality needed to send commands to and receive data from one or more embedded systems. From 5.12.0 until 7.3.0, an authenticated actor can write the pypi_url setting through set_setting at POST /openc3-api/api, then cause OpenC3::PluginModel.install_phase2 in openc3/lib/openc3/models/plugin_model.rb to interpolate the value into a shell command while installing a plugin with Python dependency metadata. Shell metacharacters in the setting are interpreted by the command shell, allowing arbitrary operating-system commands to run as the openc3 service user with access to Redis and bucket credentials. Open-source deployments permit any authenticated user to reach the affected operations, while Enterprise deployments require an administrator. This issue is fixed in version 7.3.0.

### 15. CVE-2026-77394｜OpenC3 / cosmos
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:15.343)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:15.343 / 2026-09-23T20:17:15.660
- **官方描述（原文）**：OpenC3 COSMOS provides the functionality needed to send commands to and receive data from one or more embedded systems. From 5.0.6 until 7.3.0, an authenticated actor with system_set permission can store a shared screen through POST /openc3-api/screen whose BUTTON widget action is evaluated by openc3-cosmos-init/plugins/packages/openc3-vue-common/src/widgets/ButtonWidget.vue in another operator's browser session when the button is activated. The stored script runs in the COSMOS origin and can read localStorage.openc3Token, allowing theft of the victim's bearer token, account takeover, and actions with the victim's privileges. The permissive content security policy contributes to execution but is not the primary root cause. This issue is fixed in version 7.3.0.

### 16. CVE-2026-75131｜nm-l2tp / NetworkManager-l2tp
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:14.073)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:14.073 / 2026-09-23T20:17:14.513
- **官方描述（原文）**：NetworkManager-l2tp through 1.52.4, fixed in 1.52.6, contains a privilege escalation vulnerability that allows local users with permission to create VPN connections to execute arbitrary code as root by injecting pppd options through a crafted VPN username. Attackers can embed a double-quote character or whitespace in the username to break out of the pppd options file quoting context and include the pppd plugin directive, causing the privileged pppd process to load an attacker-controlled shared object.

### 17. CVE-2026-97055｜SigNoz / signoz
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T02:16:54.333)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T02:16:54.333 / 2026-09-24T02:16:54.333
- **官方描述（原文）**：SigNoz from v0.8.0 before v0.143.0 defaults the JWT tokenizer signing secret (tokenizer::jwt::secret, set via SIGNOZ_TOKENIZER_JWT_SECRET or the deprecated SIGNOZ_JWT_SECRET) to an empty string, and Config.Validate() does not reject the empty value, so a deployment that does not configure a secret starts up and both signs and verifies session tokens with an empty HMAC key. Because the JWT tokenizer was the default provider, any such deployment is affected. An unauthenticated attacker who knows the ID of an existing user can forge a valid session token for that user — including an administrator — by signing the id, orgId and email claims with an empty key; the organization ID (and whether an email is registered) can be obtained without authentication from /api/v2/sessions/context. A forged refresh token can be exchanged at /api/v2/sessions/rotate for a new token pair and cannot be revoked, so it remains usable for its full lifetime (30 days by default). Fixed in v0.143.0, which requires a JWT secret when the jwt provider is selected and changes the default provider to opaque.

### 18. CVE-2026-96891｜D-Link / DIR-825
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T03:16:58.950)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T03:16:58.950 / 2026-09-24T03:16:58.950
- **官方描述（原文）**：A vulnerability was identified in D-Link DIR-825 3.00b32. Affected is the function tunnel_set_params of the file tunnel.c of the component rp-l2tp. The manipulation of the argument peer_hostname leads to out-of-bounds write. The attack may be initiated remotely.

### 19. CVE-2026-96770｜Temporal Technologies, Inc. / s2s-proxy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:55.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:55.013 / 2026-09-23T20:17:27.193
- **官方描述（原文）**：All published s2s-proxy versions through 0.2.2 are affected. In versions 0.1.16 through 0.2.2, TLS server listeners use Go's RequireAnyClientCert mode when skipCAVerification is false. This mode checks that the client holds the certificate's private key but does not verify the certificate against the configured CA. An attacker can therefore use a self-signed certificate and key to establish a TLS and yamux connection, then invoke RPCs allowed by the proxy's configuration and Temporal credentials. No certificate or private key trusted by the deployment, and no Temporal credential, is required.

### 20. CVE-2026-96759｜orval-labs / orval
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:25.250)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:25.250 / 2026-09-23T18:16:08.337
- **官方描述（原文）**：orval before 8.29.0 fails to escape the operationId parameter when emitting it into generated TanStack Query mutator options metadata objects. Attackers can inject arbitrary JavaScript code through a crafted operationId in an OpenAPI specification that executes when generated hooks are called.

### 21. CVE-2026-96756｜orval-labs / orval
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:24.767)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:24.767 / 2026-09-23T20:17:27.057
- **官方描述（原文）**：orval versions before 8.30.0 contain a code injection vulnerability in the @orval/core factory generator that fails to escape date default values in new Date() calls. Attackers can inject arbitrary expressions through apostrophes in OpenAPI schema defaults to execute code with the privileges of the consumer process when factoryMethods and useDates options are enabled.

### 22. CVE-2026-96755｜orval-labs / orval
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:24.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:24.607 / 2026-09-23T18:16:08.337
- **官方描述（原文）**：orval versions 8.14.0 through 8.28.1 contain a code injection vulnerability in the @orval/effect generator that converts OpenAPI schema defaults into template literals. Attackers can inject arbitrary JavaScript expressions via schema defaults containing ${...} syntax, which are executed at module scope when the generated code is built or imported.

### 23. CVE-2026-96754｜orval-labs / orval
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:24.437)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:24.437 / 2026-09-23T17:17:24.437
- **官方描述（原文）**：orval versions before 8.29.0 contain a code injection vulnerability in the @orval/hono generator that fails to escape OpenAPI path values in single-quoted route literals. Attackers can craft an OpenAPI document with an apostrophe in a static path segment to inject arbitrary JavaScript code that executes when the generated TypeScript module is imported.

### 24. CVE-2026-96560｜ModelTC / LightLLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T14:17:11.073)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T14:17:11.073 / 2026-09-23T17:17:49.440
- **官方描述（原文）**：LightLLM through 1.2.0 contains a remote code execution vulnerability in the KV-transfer worker when started with --pd_trans_mode nccl, which exposes an unauthenticated RPyC control channel that deserializes attacker-supplied data. Attackers can send malicious pickled objects to the exposed RPyC ThreadedServer to execute arbitrary code with the privileges of the LightLLM service account.

### 25. CVE-2026-96276｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T15:17:32.317)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T15:17:32.317 / 2026-09-23T19:40:10.000
- **官方描述（原文）**：If a malicious SDK container declares an extension point with a crafted `directory` path, and a developer runs `flatpak build-init --writable-sdk --sdk-extension` with that SDK, attacker-chosen files could be written outside the working directory, since the target path is resolved via a function that allows `..` traversal.

### 26. CVE-2026-95601｜WBW Plugins / Product Filter by WBW
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:53.210)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:53.210 / 2026-09-23T19:39:08.847
- **官方描述（原文）**：Unauthenticated SQL Injection in Product Filter by WBW <= 3.1.7 versions.

### 27. CVE-2026-93577｜GitLab / GitLab
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T00:17:22.850)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T00:17:22.850 / 2026-09-24T00:17:22.850
- **官方描述（原文）**：GitLab has remediated an issue in GitLab CE/EE affecting all versions from 19.2 before 19.2.7, 19.3 before 19.3.3, and 19.4 before 19.4.1 that under certain conditions could have allowed an authenticated user to execute arbitrary code on the GitLab server due to an integer overflow issue when compiling a specially crafted regular expression in a CI/CD configuration.

### 28. CVE-2026-93352｜plank / laravel-mediable
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T22:16:59.523)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T22:16:59.523 / 2026-09-23T22:16:59.523
- **官方描述（原文）**：Laravel-Mediable 7.0.0 before 7.0.2 contains an incomplete patch for CVE-2026-49972 in which the .pht extension is absent from the forbidden_extensions blocklist in config/mediable.php. The blocklist introduced to address CVE-2026-49972 includes phpt but omits pht, which Apache executes as PHP via the default FilesMatch directive on Debian and Ubuntu systems. An attacker can upload a .pht file that passes all validation in MediaUploader::verifyExtension() and File::sanitizeFileName() because pht is not present in the blocklist, causing the file to be written to disk and executed as PHP when requested, enabling remote code execution with the privileges of the web server process.

### 29. CVE-2026-89078｜GitLab / GitLab
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T00:17:22.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T00:17:22.060 / 2026-09-24T00:17:22.060
- **官方描述（原文）**：GitLab has remediated an issue in GitLab CE/EE affecting all versions from 19.2 before 19.2.7, 19.3 before 19.3.3, and 19.4 before 19.4.1 that under certain conditions could have allowed an authenticated user to execute arbitrary code on the GitLab server due to a double free issue when parsing a specially crafted regular expression in a CI/CD configuration.

### 30. CVE-2026-87900｜WebPros / WP Toolkit for cPanel
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T20:17:20.613)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T20:17:20.613 / 2026-09-23T21:17:03.717
- **官方描述（原文）**：Argument injection in WP Toolkit for cPanel 6.11.2-10794 and earlier allows remote authenticated users to read arbitrary files and execute arbitrary code across customer accounts.

### 31. CVE-2026-87899｜WebPros / cPanel
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T20:17:20.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T20:17:20.480 / 2026-09-24T04:18:03.503
- **官方描述（原文）**：Execution with unnecessary privileges in cPanel allows remote authenticated users to execute arbitrary code with root privileges.

### 32. CVE-2026-87898｜WebPros / Plesk extension "Site Import"
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T20:17:20.340)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T20:17:20.340 / 2026-09-23T21:17:03.443
- **官方描述（原文）**：OS command injection in Plesk allows remote authenticated users to execute arbitrary code with root privileges.

### 33. CVE-2026-86708｜Zohocorp / ManageEngine Applications Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T14:17:09.467)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T14:17:09.467 / 2026-09-24T04:18:03.367
- **官方描述（原文）**：ZohoCorp ManageEngine Applications Manager versions 182200 and below were vulnerable to exposure of a Google Cloud service-account private key in the Applications Manager installer, which could allow an unauthenticated attacker to impersonate the service account and access or modify associated cloud resources.

### 34. CVE-2026-86350｜Apache Software Foundation / Apache Tomcat
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T12:17:08.350)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T12:17:08.350 / 2026-09-23T17:58:26.570
- **官方描述（原文）**：Inconsistent interpretation of HTTP/2 requests ('HTTP Request/Response smuggling') vulnerability in Apache Tomcat caused by a regression in fix for CVE-2026-41293 can trigger request header mix-up. This issue affects Apache Tomcat: from 11.0.22 through 11.0.25, from 10.1.55 through 10.1.59, from 9.0.118 through 9.0.121. Users are recommended to upgrade to version 11.0.26, 10.1.60 or 9.0.122, which fix the issue.

### 35. CVE-2026-86248｜Apache Software Foundation / Apache Tomcat
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T12:17:08.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T12:17:08.237 / 2026-09-23T17:58:26.570
- **官方描述（原文）**：CLIENT_CERT authentication does not fail as expected for some scenarios when soft fail is disabled vulnerability in Apache Tomcat. This issue affects Apache Tomcat: from 11.0.0-M14 through 11.0.25, from 10.1.22 through 10.1.59, from 9.0.92 through 9.0.121. Users are recommended to upgrade to version 11.0.26, 10.1.60 or 9.0.122, which fix the issue.

### 36. CVE-2026-86246｜Apache Software Foundation / Apache Tomcat Native
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T13:17:31.117)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T13:17:31.117 / 2026-09-23T19:19:41.770
- **官方描述（原文）**：Initialization of a resource with an insecure default vulnerability in Apache Tomcat Native enabled insecure options by default including ALLOW_CLIENT_RENEGOTIATION, NO_EXTENDED_MASTER_SECRET, IGNORE_UNEXPECTED_EOF and ALLOW_NO_DHE_KEX. This issue affects Apache Tomcat Native: from 2.0.0 through 2.0.15, from 1.3.0 through 1.3.8. Earlier unsupported versions may also be affected. Users are recommended to upgrade to version 2.0.16 or 1.3.9, which fix the issue.

### 37. CVE-2026-85724｜moquette-io / moquette
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:17.623)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:17.623 / 2026-09-23T18:12:04.247
- **官方描述（原文）**：Moquette is a lightweight Java MQTT broker. Prior to 0.18.1, when pattern-based ACL rules are configured, AuthorizationsCollector.canDoOperation substitutes client ID and username values directly into rules containing %c or %u and then treats the result as an MQTT topic filter. A client that uses + or # in either identity can broaden the substituted filter and gain cross-tenant read and write access. A # identity can also produce an invalid filter that triggers a NullPointerException in Topic.match and disrupts session processing. This issue is fixed in version 0.18.1.

### 38. CVE-2026-84719｜Red Hat / Red Hat Ansible Automation Platform 2.4 for RHEL 8
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T20:17:18.617)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T20:17:18.617 / 2026-09-24T04:18:02.470
- **官方描述（原文）**：A flaw was found in the Ansible Automation Platform automation-controller. When a WorkflowJobTemplate is copied, the deep-copy permission sanitizer validates only the inventory, unified_job_template, and credentials of each cloned node and fails to check the instance_groups (and execution_environment and labels) that were preserved from the original. A user with organization workflow-admin permission but no role on the referenced instance groups can copy a workflow, become its administrator, and launch jobs pinned to instance groups they are not authorized to use — including the control-plane instance group — bypassing the InstanceGroup use_role boundary and causing attacker-influenced automation to run in the control-plane execution context.

### 39. CVE-2026-84502｜Red Hat / Red Hat Ansible Automation Platform 2.4 for RHEL 8
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:40.377)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:40.377 / 2026-09-24T04:18:00.647
- **官方描述（原文）**：A flaw was found in Red Hat Ansible Automation Platform's automation- controller. The Project scm_url field is not validated against values that begin with a dash and is stored and passed verbatim to the git SCM module. Because the module runs git ls-remote with the URL as a positional argument and without a "--" separator, a git project URL such as "--upload-pack=<command>:x" is interpreted by git as the --upload-pack option and executed via a shell. A user with permission to create or modify a project in a single organization can thereby execute arbitrary commands on the control-plane task pod, with output reflected through the project update stdout endpoint, leading to cross-tenant compromise and in-cluster lateral movement

### 40. CVE-2026-84474｜Red Hat / Red Hat Ansible Automation Platform 2.4 for RHEL 8
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:39.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:39.930 / 2026-09-24T04:17:59.993
- **官方描述（原文）**：A flaw was found in Red Hat Ansible Automation Platform's automation- controller. The provisioning-callback secret (host_config_key) is exposed to users holding only the read-level view_jobtemplate permission -- both in the job template API representation and in the activity stream -- and the provisioning callback endpoint trusts a client-supplied X-Forwarded-For header to determine the calling host when the controller is deployed behind the AAP gateway with an empty proxy allow-list. By reading the secret and spoofing X-Forwarded-For to match any host in the job template's inventory, a minimally privileged or unauthenticated remote attacker can launch the job template against arbitrary managed hosts using the job template's credentials, resulting in privilege escalation and remote code execution on managed hosts.

### 41. CVE-2026-82843｜Unknown / WP OAuth Server ( Login with WordPress )
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T06:17:02.363)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：0.0018 / percentile=0.07859
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T06:17:02.363 / 2026-09-23T11:17:12.070
- **官方描述（原文）**：The WP OAuth Server ( Login with WordPress ) WordPress plugin before 6.4.0 does not bind the OpenID Connect identity assertion it issues to the authorization grant being exchanged, returning instead the assertion belonging to whichever user authenticated most recently, which allows users with the Subscriber role and above to obtain a validly signed identity assertion for another user, including an administrator, and authenticate as them at any application that uses the site for single sign-on.

### 42. CVE-2026-82331｜Apache Software Foundation / Apache BuildStream
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T07:16:46.493)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00195 / percentile=0.09537
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T07:16:46.493 / 2026-09-23T17:58:26.570
- **官方描述（原文）**：Improper link resolution before file access ('link following') vulnerability in the `tar` source plugin of Apache BuildStream running on Python < 3.12 allows malicious source tarballs to write files on the host, with the privileges of the user running BuildStream, via symlinks as part of source fetching. The impact of this issue is mitigated by: * BuildStream projects should only use trusted sources in their elements as otherwise the build output can also not be trusted * Tracking a source tarball pins its SHA256 hash, which prevents MITM attacks of users that are fetching an already tracked project * When running on Python >= 3.12, BuildStream >= 2.3.0 already makes use of the Python `tarfile` filter functionality, which blocks the symlink escape Users are recommended to upgrade to version 2.8.1, which fixes this issue.

### 43. CVE-2026-77602｜OpenC3 / cosmos
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:18.550)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:18.550 / 2026-09-23T19:19:18.683
- **官方描述（原文）**：OpenC3 COSMOS provides the functionality needed to send commands to and receive data from one or more embedded systems. From 5.1.0 until 7.3.0, authenticated non-administrator users can write content under targets_modified/ that is later executed by multiple configuration paths below the intended code-execution privilege tier. Table and command or telemetry definitions are processed through ConfigParser, PacketConfig, GENERIC_READ_CONVERSION, or GENERIC_WRITE_CONVERSION, allowing ERB rendering or Ruby and Python evaluation, while openc3-cosmos-script-runner-api/scripts/run_suite_analysis.rb executes suite procedure files through require. Storage uploads, screen saves, and script creation can place content in the overlay, and triggering table processing, a cmd/tlm reload, or suite analysis executes the content in cmd-tlm-api, decom microservices, or Script Runner with access to internal credentials and data. This issue is fixed in version 7.3.0.

### 44. CVE-2026-76183｜Apache Software Foundation / Apache Tomcat
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T12:17:06.537)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T12:17:06.537 / 2026-09-23T19:19:14.877
- **官方描述（原文）**：Authentication Bypass by Alternate Name vulnerability in Apache Tomcat allowed the security constraints for any WebSocket endpoint to be bypassed. This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.25, from 10.1.0-M1 through 10.1.59, from 9.0.0.M1 through 9.0.121. The following versions were EOS at the time the CVE was created but are known to be affected: from 8.5.0 through 8.5.100, from 7.0.43 through 7.0.109. Other unsupported versions may also be affected. Users are recommended to upgrade to version 11.0.26, 10.1.60 or 9.0.122, which fix the issue.

### 45. CVE-2026-75884｜Red Hat / Red Hat Ansible Automation Platform 2.4 for RHEL 8
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T20:17:14.637)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T20:17:14.637 / 2026-09-24T04:17:56.700
- **官方描述（原文）**：A flaw was found in AWX. The container group pod_spec_override field uses an incomplete blocklist that only restricts automountServiceAccountToken, allowing injection of initContainers, serviceAccountName overrides, and projected service account token volumes. An AAP platform administrator can exploit this to escalate privileges to OpenShift namespace-level access and exfiltrate namespace secrets.

### 46. CVE-2026-75799｜Unknown / YAHMAN Add-ons
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T06:17:01.710)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：0.00235 / percentile=0.14799
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T06:17:01.710 / 2026-09-23T18:13:31.210
- **官方描述（原文）**：The YAHMAN Add-ons WordPress plugin before 0.9.31 does not validate the type of the remote files it caches in a publicly accessible directory, allowing unauthenticated attackers to write arbitrary PHP files on the server and achieve RCE when the relevant feature is enabled.

### 47. CVE-2026-6928｜IBM / Concert
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T21:17:02.430)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T21:17:02.430 / 2026-09-23T21:17:02.430
- **官方描述（原文）**：IBM Concert 1.0.0 through 3.0.0 references or accesses memory after it has been freed. This allows an attacker who can influence program execution or input may exploit this condition to corrupt memory, cause application crashes, or execute arbitrary code.

### 48. CVE-2026-67404｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T21:17:01.517)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T21:17:01.517 / 2026-09-23T21:17:01.517
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. Prior to versions 3.13.15, 4.0.20, 4.1.11, 4.2.6, and 4.3.0, When no CA bundle is available, ssl_options/1 falls back to [{verify, verify_none}] with no warning. An attacker in a man-in-the-middle position can forge the JWKS response, which leads the broker to accept arbitrary JWTs. Preconditions include The OAuth2 plugin must be in use with no cacertfile configured and the OS CA bundle empty or unreadable (for example, in a minimal container), and the attacker must hold a network man-in-the-middle position.. This issue is fixed in versions 3.13.15, 4.0.20, 4.1.11, 4.2.6, and 4.3.0.

### 49. CVE-2026-6730｜IBM / Concert
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T21:17:02.053)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T21:17:02.053 / 2026-09-23T21:17:02.053
- **官方描述（原文）**：IBM Concert 1.0.0 through 3.0.0 is vulnerable to a buffer overflow, caused by improper bounds checking. A local user could overflow the buffer and execute arbitrary code on the system.

### 50. CVE-2026-67231｜rabbitmq / rabbitmq-server
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T21:17:00.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T21:17:00.940 / 2026-09-23T21:17:00.940
- **官方描述（原文）**：RabbitMQ is a messaging and streaming broker. Prior to versions 3.13.15, 4.0.20, 4.1.11, 4.2.6, and 4.3.0, The trust-store plugin installs a verify_fun that overrides {bad_cert, unknown_ca} / {bad_cert, selfsigned_peer} when the presented cert "matches" a whitelisted one. The match key is extract_issuer_id/1 → public_key:pkix_issuer_id/2 → {IssuerName, SerialNumber} , both fields are taken verbatim from the presented certificate body and contain no public-key, SKI, fingerprint or signature material. is_whitelisted/1 is a pure ets:member lookup; the stored full DER is used only for list/0 display and is never compared against the presented cert. cacerts is [], so the whitelisted cert is never used as a trust anchor for path validation either. TLS client-authentication bypass: an attacker who knows the issuer DN + serial of any whitelisted certificate can connect with a forged self-signed cert. Preconditions include rabbitmq_trust_store plugin enabled and used as the TLS verify_fun Attacker knows or can guess the {Issuer, Serial} of at least one whitelisted cert (non-secret; exposed via CLI/logs/any cert copy). This issue is fixed in versions 3.13.15, 4.0.20, 4.1.11, 4.2.6, and 4.3.0.

### 51. CVE-2026-6721｜IBM / Concert
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T21:17:01.927)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T21:17:01.927 / 2026-09-23T21:17:01.927
- **官方描述（原文）**：IBM Concert 1.0.0 through 3.0.0 allows an unauthenticated remote attacker can supply specially crafted input that is incorporated into OS commands, resulting in arbitrary command execution on the underlying system. Successful exploitation allows remote code execution with the privileges of the affected application.

### 52. CVE-2026-63132｜openbao / openbao
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:17:34.663)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:17:34.663 / 2026-09-23T20:17:12.490
- **官方描述（原文）**：OpenBao is an open source identity-based secrets management system. Prior to 2.6.0, OpenBao's handleLogicalRecovery path in http/logical.go compared the highly privileged recovery token with ordinary string equality. A remote unauthenticated attacker able to make repeated recovery mode requests and measure response timing could infer the recovery token. The recovered token could then authorize recovery mode operations that read or modify OpenBao data. This issue is fixed in version 2.6.0.

### 53. CVE-2026-59167｜JiHong88 / suneditor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T14:17:07.923)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T14:17:07.923 / 2026-09-23T18:12:04.247
- **官方描述（原文）**：SunEditor is a lightweight and powerful WYSIWYG editor in vanilla JavaScript with no dependencies. Prior to 2.47.11, the sanitizer in src/lib/core.js does not consistently reject namespaced or custom HTML elements, allowing event-handler attributes to remain on crafted elements. When an application renders attacker-controlled editor content and a user interacts with the element, the retained handler can execute script in the application's browser origin, enabling stored cross-site scripting, data exposure, or unauthorized browser-context actions. This issue is fixed in version 2.47.11.

### 54. CVE-2026-19599｜Zohocorp / ManageEngine OpManager
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T13:17:27.400)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T13:17:27.400 / 2026-09-24T04:17:48.027
- **官方描述（原文）**：ZohoCorp ManageEngine OpManager MSP versions 12.8.709 and below were vulnerable to a Remote Code Execution vulnerability in the Notification Profile module.

### 55. CVE-2026-18872｜IBM / Financial Transaction Manager (FTM) for RedHat OpenShift
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T16:16:41.720)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T16:16:41.720 / 2026-09-23T19:17:29.493
- **官方描述（原文）**：IBM Financial Transaction Manager (FTM) for RedHat OpenShift is vulnerable to stored cross-site scripting (CWE-79) in the FTM UI NetworkAcknowledgement React component (NetworkAcknowledgement.jsx:42). A malicious actor can inject script into stored network acknowledgement data that executes in authenticated operator browsers, enabling session hijacking and unauthorized operator-level payment actions.

### 56. CVE-2026-18467｜paytiumsupport / Paytium: Mollie payment forms & donations
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-24T02:16:52.943)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-24T02:16:52.943 / 2026-09-24T02:16:52.943
- **官方描述（原文）**：The Paytium: Mollie payment forms & donations plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 5.0.3. The 5.0.3 patch introduced a wp_hash()/hash_equals() signature gate on the pt-paytium-user-data field, but left a second filter — pt_cf_checkout_meta(), registered on the pt_meta_values hook after the signed builder — that copies every $_POST['pt_form_field'][*] key verbatim into the payment meta array without any signature verification; this allows the pt-user-role value it copies to overwrite the signed path's output, after which paytium_user_data_processing() reads the persisted _pt-user-role post meta and passes it directly as the role argument to wp_insert_user(). This makes it possible for unauthenticated attackers to register a new WordPress account with the administrator role and fully take over the site. Exploitation requires submitting a payment through a publicly-exposed [paytium] shortcode form and completing the resulting payment flow, after which the attacker can seize the new administrator account via the standard lost-password flow on their supplied email address.

### 57. CVE-2025-63564｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:14.323)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:14.323 / 2026-09-23T20:17:10.447
- **官方描述（原文）**：SQL injection vulnerability in Moodle Socialwall plugin v.3.0 through v.3.3 allows an attacker to execute arbitrary code via crafted HTTP requests

### 58. CVE-2026-96545｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:54.227)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:54.227 / 2026-09-23T20:17:26.073
- **官方描述（原文）**：An out-of-bounds heap read flaw was found in GIMP's TIM image loader. When a user opens a crafted 4bpp TIM image that causes promotion to an RGBA layer, the file-tim plug-in allocates an undersized row buffer but processes it using the larger RGBA row size. This can copy adjacent heap contents into the decoded image and may crash the plug-in.

### 59. CVE-2026-96514｜Neethuharii / CafeManagement
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:22.853)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:22.853 / 2026-09-23T20:17:25.800
- **官方描述（原文）**：A weakness has been identified in Neethuharii CafeManagement. Impacted is an unknown function of the file CafePortalLogin.php of the component Login Handler. This manipulation of the argument uname causes sql injection. It is possible to initiate the attack remotely. The exploit has been made available to the public and could be used for attacks. This product is using a rolling release to provide continious delivery. Therefore, no version details for affected nor updated releases are available. The vendor was contacted early about this disclosure but did not respond in any way.

### 60. CVE-2026-96513｜Neethuharii / CafeManagement
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T17:17:22.667)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T17:17:22.667 / 2026-09-23T19:19:53.940
- **官方描述（原文）**：A security flaw has been discovered in Neethuharii CafeManagement. This issue affects some unknown processing of the file AddProductCode.php. The manipulation of the argument image results in unrestricted upload. The attack may be performed from remote. The exploit has been released to the public and may be used for attacks. This product utilizes a rolling release system for continuous delivery, and as such, version information for affected or updated releases is not disclosed. The vendor was contacted early about this disclosure but did not respond in any way.

### 61. CVE-2026-92700｜caddyserver / caddy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:44.280)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:44.280 / 2026-09-23T20:17:22.137
- **官方描述（原文）**：Caddy is an extensible server platform that uses TLS by default. In version 2.11.3 and earlier, in modules/caddyhttp/fileserver/staticfiles.go, fileHidden() uses case-sensitive filepath.Match checks, so case variants can bypass hide rules on case-insensitive filesystems or when mixed-case paths coexist and expose files intended to be hidden.

### 62. CVE-2026-92284｜caddyserver / caddy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:43.940)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:43.940 / 2026-09-23T20:17:21.903
- **官方描述（原文）**：Caddy is an extensible server platform that uses TLS by default. In version 2.11.3 and earlier, in modules/caddyhttp/replacer.go, resolving http.request.body reads the complete request body with an unbounded io.Copy before request-body middleware limits apply, allowing memory exhaustion and process termination.

### 63. CVE-2026-88974｜wp-graphql / wp-graphql
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T15:17:23.893)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T15:17:23.893 / 2026-09-23T18:12:04.247
- **官方描述（原文）**：WPGraphQL provides a GraphQL API for WordPress sites. Prior to 2.22.2, the updatePost mutation in src/Mutation/PostObjectUpdate.php checks only the collection-level edit_posts capability and the post author, but does not enforce the object-level edit_post capability or require publish_posts for public status transitions. An authenticated Contributor can therefore publish the Contributor's own draft without editorial approval or modify the Contributor's previously published post despite lacking edit_published_posts, while posts owned by other authors remain protected. This issue is fixed in version 2.22.2.

### 64. CVE-2026-84091｜Unknown / SUMIT Payment Gateway for WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T13:17:30.623)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T13:17:30.623 / 2026-09-23T13:17:30.623
- **官方描述（原文）**：The SUMIT Payment Gateway for WooCommerce WordPress plugin before 4.0.0 does not verify with the payment provider that a payment notification is genuine before marking the corresponding order as paid, allowing unauthenticated users to mark a pending order paid without completing payment.

### 65. CVE-2026-73858｜solspace / craft-freeform
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T15:17:18.233)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T15:17:18.233 / 2026-09-23T18:12:04.247
- **官方描述（原文）**：Solspace Freeform plugin for Craft CMS 5.x is a super flexible form-building tool. From 5.0.0 through 5.10.13, submitted values from public Freeform forms can be evaluated by the isolated Twig renderer when rendered into HTML attributes. An unauthenticated attacker can place Twig expressions in submitted field values, including value attributes, and receive evaluated PHP, operating-system, or Craft filesystem-path constants in the form response. The isolated context was not shown to expose Craft globals, environment variables, credentials, arbitrary files, or code execution, so the confirmed impact is limited server and environment information disclosure and possible rendering errors. This issue is fixed in version 5.10.14.

### 66. CVE-2026-62998｜redaxo / core
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T15:17:15.293)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T15:17:15.293 / 2026-09-23T18:12:04.247
- **官方描述（原文）**：REDAXO is a PHP-based content management system. Prior to 5.21.2, rex_list::getSortColumn() in redaxo/src/core/lib/list.php accepts the sort request parameter without checking whether setColumnSortable() registered the requested column. An authenticated backend user can make prepareQuery() add an escaped but unauthorized ORDER BY identifier, allowing error-based enumeration of columns in joined tables and ordering by unselected sensitive fields such as rex_user.password. This issue is fixed in version 5.21.2.

### 67. CVE-2026-61834｜thomaspoignant / scim-patch
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T15:17:15.127)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T15:17:15.127 / 2026-09-23T17:17:15.923
- **官方描述（原文）**：scim-patch is a library for applying SCIM patch operations. Prior to 0.9.2, navigate() reads inherited properties and assign() uses prototype-chain membership checks while resolving attacker-controlled SCIM PATCH paths. A path or one of the dotted value keys beginning with an inherited property such as toString can therefore traverse into a shared built-in function object and add attacker-controlled properties, causing process-global mutation that may affect application logic reading inherited-method properties. This issue is fixed in version 0.9.2.

### 68. CVE-2026-96549｜sfturing / hosp_order
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:54.703)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 1.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:54.703 / 2026-09-23T20:17:26.200
- **官方描述（原文）**：A vulnerability has been found in sfturing hosp_order up to 627f426331da8086ce8fff2017d65b1ddef384f8. This vulnerability affects unknown code of the file ssm_pro/src/main/java/cn/sfturing/service/impl/CommonUserServiceImpl.java. Such manipulation leads to cleartext storage of sensitive information. The attack can only be performed from a local environment. The exploit has been disclosed to the public and may be used. This product takes the approach of rolling releases to provide continious delivery. Therefore, version details for affected and updated releases are not available. The project was informed of the problem early through an issue report but has not responded yet.

### 69. CVE-2026-96548｜sfturing / hosp_order
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-23T19:19:54.513)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-23T19:19:54.513 / 2026-09-23T19:39:08.847
- **官方描述（原文）**：A flaw has been found in sfturing hosp_order up to 627f426331da8086ce8fff2017d65b1ddef384f8. This affects an unknown part of the file ssm_pro/src/main/resources/jdbc.properties. This manipulation causes hard-coded credentials. It is possible to initiate the attack remotely. The attack's complexity is rated as high. It is indicated that the exploitability is difficult. The exploit has been published and may be used. This product is using a rolling release to provide continious delivery. Therefore, no version details for affected nor updated releases are available. The project was informed of the problem early through an issue report but has not responded yet.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-96758 | P3 / 38 | orval-labs / orval | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-96757 | P3 / 38 | orval-labs / orval | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-95848 | P3 / 38 | moquette-io / moquette | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-96673 | WATCH / 30 | Photoview / Photoview | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-96599 | WATCH / 30 | isotope / isotope-core | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-96541 | WATCH / 30 | Red Hat / Red Hat Enterprise Linux 10 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-95847 | WATCH / 30 | moquette-io / moquette | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-95843 | WATCH / 30 | moquette-io / moquette | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-95842 | WATCH / 30 | moquette-io / moquette | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93349 | WATCH / 30 | frictionlessdata / frictionless-py | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-91775 | WATCH / 30 | LimeSurvey / LimeSurvey | v4.0 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-86064 | WATCH / 30 | klever-io / klever-go | v3.1 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-82407 | WATCH / 30 | klever-io / klever-go | v4.0 7.0 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77601 | WATCH / 30 | OpenC3 / cosmos | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77394 | WATCH / 30 | OpenC3 / cosmos | v3.1 7.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-75131 | WATCH / 30 | nm-l2tp / NetworkManager-l2tp | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97055 | WATCH / 28 | SigNoz / signoz | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-96891 | WATCH / 28 | D-Link / DIR-825 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-96770 | WATCH / 28 | Temporal Technologies, Inc. / s2s-proxy | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96759 | WATCH / 28 | orval-labs / orval | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-96756 | WATCH / 28 | orval-labs / orval | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96755 | WATCH / 28 | orval-labs / orval | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96754 | WATCH / 28 | orval-labs / orval | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-96560 | WATCH / 28 | ModelTC / LightLLM | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-96276 | WATCH / 28 | Red Hat / Red Hat Enterprise Linux 10 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-95601 | WATCH / 28 | WBW Plugins / Product Filter by WBW | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-93577 | WATCH / 28 | GitLab / GitLab | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93352 | WATCH / 28 | plank / laravel-mediable | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-89078 | WATCH / 28 | GitLab / GitLab | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-87900 | WATCH / 28 | WebPros / WP Toolkit for cPanel | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |

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
- EPSS 未確認：30；Exploitation status 未確認：7。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-24T05:39:42.995467+00:00`；Delta generated at：`2026-09-24T05:39:42.995467+00:00`。

---

## 可驗證資料來源

- **CVE-2026-96758** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96758)
- **CVE-2026-96757** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96757)
- **CVE-2026-95848** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95848)
- **CVE-2026-96673** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96673)
- **CVE-2026-96599** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96599)
- **CVE-2026-96541** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96541)
- **CVE-2026-95847** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95847)
- **CVE-2026-95843** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95843)
- **CVE-2026-95842** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95842)
- **CVE-2026-93349** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93349)
- **CVE-2026-91775** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91775)
- **CVE-2026-86064** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86064)
- **CVE-2026-82407** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82407)
- **CVE-2026-77601** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77601)
- **CVE-2026-77394** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77394)
- **CVE-2026-75131** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75131)
- **CVE-2026-97055** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97055)
- **CVE-2026-96891** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96891)
- **CVE-2026-96770** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96770)
- **CVE-2026-96759** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96759)
- **CVE-2026-96756** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96756)
- **CVE-2026-96755** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96755)
- **CVE-2026-96754** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96754)
- **CVE-2026-96560** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96560)
- **CVE-2026-96276** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96276)
- **CVE-2026-95601** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95601)
- **CVE-2026-93577** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93577)
- **CVE-2026-93352** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93352)
- **CVE-2026-89078** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89078)
- **CVE-2026-87900** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87900)
- **CVE-2026-87899** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87899)
- **CVE-2026-87898** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87898)
- **CVE-2026-86708** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86708)
- **CVE-2026-86350** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86350)
- **CVE-2026-86248** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86248)
- **CVE-2026-86246** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86246)
- **CVE-2026-85724** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85724)
- **CVE-2026-84719** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84719)
- **CVE-2026-84502** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84502)
- **CVE-2026-84474** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84474)
- **CVE-2026-82843** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82843) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-82843)
- **CVE-2026-82331** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82331) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-82331)
- **CVE-2026-77602** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77602)
- **CVE-2026-76183** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76183)
- **CVE-2026-75884** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75884)
- **CVE-2026-75799** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75799) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-75799)
- **CVE-2026-6928** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-6928)
- **CVE-2026-67404** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67404)
- **CVE-2026-6730** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-6730)
- **CVE-2026-67231** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67231)
- **CVE-2026-6721** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-6721)
- **CVE-2026-63132** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63132)
- **CVE-2026-59167** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59167)
- **CVE-2026-19599** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19599)
- **CVE-2026-18872** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18872)
- **CVE-2026-18467** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18467)
- **CVE-2025-63564** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-63564)
- **CVE-2026-96545** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96545)
- **CVE-2026-96514** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96514)
- **CVE-2026-96513** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96513)
- **CVE-2026-92700** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92700)
- **CVE-2026-92284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92284)
- **CVE-2026-88974** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88974)
- **CVE-2026-84091** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84091)
- **CVE-2026-73858** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73858)
- **CVE-2026-62998** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62998)
- **CVE-2026-61834** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61834)
- **CVE-2026-96549** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96549)
- **CVE-2026-96548** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-96548)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
