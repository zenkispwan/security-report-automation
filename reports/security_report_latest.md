# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**88** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=2、EXPLOITATION_CHANGED=2、NEW_CVE=86。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **4**、WATCH **26**。
- Baseline：state / generated_at=2026-10-19T05:30:26.270237+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **88** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-95210｜未確認 / 未確認
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)；CVSS_CHANGED (from=9.1; to=4.8)
- **Risk**：WATCH / score 4；reasons：CVSS_MEDIUM(+4)
- **CVSS**：v3.1 4.8 (MEDIUM)
- **EPSS**：0.00228 / percentile=0.12674
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T18:18:33.370 / 2026-10-19T16:17:09.577
- **官方描述（原文）**：Improper certificate validation in gnutls v3.8.13 causes the application to accept certificates containing invalid extensions.

### 2. CVE-2026-88647｜未確認 / 未確認
- **Delta event**：EXPLOITATION_CHANGED (from=poc; to=none)；CVSS_CHANGED (from=9.1; to=6.5)
- **Risk**：WATCH / score 4；reasons：CVSS_MEDIUM(+4)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：0.00212 / percentile=0.10816
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-08T17:17:17.783 / 2026-10-19T16:17:08.333
- **官方描述（原文）**：A hostname verification bypass in GnuTLS v3.8.13 allows attackers to circumvent the Common Name fallback mechanism and eavesdrop on communications via a crafted certificate.

### 3. CVE-2026-78162｜Apache Software Foundation / Apache Camel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T11:17:19.037)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T11:17:19.037 / 2026-10-20T04:17:02.327
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Apache Camel. This issue affects Apache Camel: from 4.0.0 before 4.18.5, from 4.19.0 before 4.22.1. The camel-hazelcast component applies a default Hazelcast JavaSerializationFilterConfig to the instances it creates from its own configuration, a protection introduced by CVE-2026-43865. That change did not reach two of the configuration paths Camel builds itself, so those paths continued to create Hazelcast instances whose Java deserialization is unrestricted. ReplicatedHazelcastAggregationRepository extends HazelcastAggregationRepository but overrides doStart() without calling super.doStart(), keeping its own copy of the bootstrap block, and therefore never received the filter: a route using it without supplying a hazelcastInstance starts a Hazelcast member that deserializes values read from the backing ReplicatedMap with no class restriction. HazelcastDefaultComponent#getOrCreateHzClientInstance() builds its own ClientConfig when hazelcastMode=client is selected and neither a referenced ClientConfig nor hazelcastConfigUri is supplied, and likewise applied no filter, so client-mode endpoints behaved differently from node-mode endpoints for an otherwise identical configuration. In both cases an attacker able to publish into the Hazelcast cluster that the affected instance is attached to can cause a serialized Java object of their choosing to be deserialized inside Hazelcast's own serialization layer, before Camel processes the exchange, resulting in remote code execution. Hazelcast clusters have neither authentication nor TLS enabled by default. Selecting client mode is a topology choice rather than a security option, so neither path required the deployment to opt in to unsafe behaviour. Users are recommended to upgrade to version 4.23.0, which fixes the issue. If users are on the 4.22.x releases stream, then they are suggested to upgrade to 4.22.1. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.5. The 4.14.x releases stream and earlier reached end of life before this issue was resolved and will not receive a fix, so deployments on those lines must move to a supported release. For deployments that cannot upgrade immediately, supply an explicit Hazelcast configuration carrying a JavaSerializationFilterConfig, or inject a pre-built HazelcastInstance, since a user-supplied configuration is never overwritten by Camel. Alternatively set the JVM-wide filter -Djdk.serialFilter=!java.net.;java.;javax.;org.apache.camel.;!* and enable Hazelcast cluster authentication and TLS to restrict who can reach the cluster.

### 4. CVE-2026-112393｜python-pillow / Pillow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T21:17:07.613)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T21:17:07.613 / 2026-10-19T22:17:06.730
- **官方描述（原文）**：Pillow is a Python imaging library. From 2.0.0 until 13.0.0, Pillow has a heap buffer overflow and stale-heap disclosure in _tiffWriteProc when saving compressed TIFF data through libtiff to a target without a usable fileno(), such as BytesIO. The callback sizes its allocation from the prior buffer size instead of the current write position, allowing an attacker-controlled out-of-line TIFF tag or retained ICC profile to be copied beyond the allocation after libtiff seeks forward. This overflow can crash the process and may allow code execution. Independently, unwritten alignment gaps in compressed TIFF output larger than 64 KiB can disclose stale heap bytes without a crafted tag. File paths and targets with real file descriptors are unaffected. This issue is fixed in version 13.0.0.

### 5. CVE-2026-109432｜Camunda / Camunda 7
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T16:17:02.487)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T16:17:02.487 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：Camunda 7.24.0 before 7.24.14 and 7.23.0 before 7.23.17 contains an expression injection vulnerability where AdhocQueryValidator.validate() fails to check sub-query expression maps within the orQueries field exposed by TaskQueryDto, allowing authenticated users to bypass the enableExpressionsInAdhocQueries restriction. Attackers can supply a malicious JUEL expression such as dueAfterExpression inside an orQueries entry to achieve arbitrary Java reflection and invoke java.lang.Runtime.exec, resulting in operating-system command execution as the engine service user.

### 6. CVE-2026-107083｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T17:17:00.690)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T17:17:00.690 / 2026-10-19T21:17:04.470
- **官方描述（原文）**：SENAYAN Library Management System (SLiMS) Bulian (slims9_bulian) 9.8.0 is vulnerable to SQL Injection in admin/modules/reporting/customs/dl_detail.php via the parameter fileID.

### 7. CVE-2026-79986｜Apache Software Foundation / Apache Camel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T11:17:20.860)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T11:17:20.860 / 2026-10-20T04:17:05.727
- **官方描述（原文）**：Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Camel Azure Files component. This issue affects Apache Camel: from 4.0.0 before 4.18.5, from 4.19.0 before 4.22.1. The Camel remote-file consumers poll a directory on a remote server and build the absolute remote path of each file by concatenating the configured directory with the file name reported in the server's directory listing. That concatenation (FtpUtils.absoluteFilePath and GenericFileConsumer) applied no lexical normalization and no check that the result stayed inside the directory being polled, and the resulting path became the operand for every subsequent remote operation on the file: retrieval (FtpOperations.retrieveFile / SftpOperations, reached from GenericFileConsumer where the retrieve name is taken verbatim from GenericFile.getAbsoluteFilePath), deletion when delete=true (GenericFileDeleteProcessStrategy), and renaming when move, preMove, moveFailed or readLock=rename is configured (GenericFileProcessStrategySupport and GenericFileRenameExclusiveReadLockStrategy). Neither isValidFile nor isMatched performed any containment check. A listing entry that is not a single path segment therefore resolved to a path outside the configured polling directory, causing Camel to read, delete or rename files outside it using the endpoint's own credentials. A listing name is not route-controlled data. It is supplied by the remote server, and the FTP control channel carries no integrity protection at all, so an on-path attacker can rewrite a LIST response without holding any credentials; a compromised, malicious or multi-tenant server, or a server backed by a virtual filesystem, can emit such a name directly. Retrieval is reachable in a default consumer configuration, since the remote consumers download every listed file; deletion and renaming additionally require one of the disposition options above, all of which are common. Escape from the directory Camel was configured to poll is unconditional, while escape from the server's own account boundary additionally depends on whether that server confines the account. The jailStartingDirectory option, which is documented as restricting Camel to the starting directory and is enabled by default, governed producer writes and, since the localWorkDirectory containment work, consumer downloads to the local work directory - but it did not constrain this remote operand, so its name and description claimed a boundary that was not enforced here. The same entry point had already been recognised on the local side: the localWorkDirectory download path was constrained so that a remote file name containing parent-directory segments could not resolve outside the local work directory. The remote operand was the remaining half of that surface. This artifact provides the azure-files scheme. Its consumer derives from the same RemoteFileConsumer base class and composed the remote path through a plain concatenation helper, so it inherited the same unconstrained resolution. Reaching it requires a listing name that is not a single path segment, which the Azure Files REST service does not normally return; the exposure was corrected on the same basis as the other remote-file consumers rather than from a demonstrated proof of concept against this scheme. Upgrade to Apache Camel 4.23.0, which fixes the issue. Users on the 4.22.x releases stream should upgrade to 4.22.1. Users on the 4.18.x LTS releases stream should upgrade to 4.18.5. The 4.14.x stream reached end of life and does not receive this fix; users on it should move to a supported releases stream.

### 8. CVE-2026-79985｜Apache Software Foundation / Apache Camel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T11:17:20.647)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T11:17:20.647 / 2026-10-20T04:17:04.830
- **官方描述（原文）**：Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Camel SMB component. This issue affects Apache Camel: from 4.2.0 before 4.18.5, from 4.19.0 before 4.22.1. The Camel remote-file consumers poll a directory on a remote server and build the absolute remote path of each file by concatenating the configured directory with the file name reported in the server's directory listing. That concatenation (FtpUtils.absoluteFilePath and GenericFileConsumer) applied no lexical normalization and no check that the result stayed inside the directory being polled, and the resulting path became the operand for every subsequent remote operation on the file: retrieval (FtpOperations.retrieveFile / SftpOperations, reached from GenericFileConsumer where the retrieve name is taken verbatim from GenericFile.getAbsoluteFilePath), deletion when delete=true (GenericFileDeleteProcessStrategy), and renaming when move, preMove, moveFailed or readLock=rename is configured (GenericFileProcessStrategySupport and GenericFileRenameExclusiveReadLockStrategy). Neither isValidFile nor isMatched performed any containment check. A listing entry that is not a single path segment therefore resolved to a path outside the configured polling directory, causing Camel to read, delete or rename files outside it using the endpoint's own credentials. A listing name is not route-controlled data. It is supplied by the remote server, and the FTP control channel carries no integrity protection at all, so an on-path attacker can rewrite a LIST response without holding any credentials; a compromised, malicious or multi-tenant server, or a server backed by a virtual filesystem, can emit such a name directly. Retrieval is reachable in a default consumer configuration, since the remote consumers download every listed file; deletion and renaming additionally require one of the disposition options above, all of which are common. Escape from the directory Camel was configured to poll is unconditional, while escape from the server's own account boundary additionally depends on whether that server confines the account. The jailStartingDirectory option, which is documented as restricting Camel to the starting directory and is enabled by default, governed producer writes and, since the localWorkDirectory containment work, consumer downloads to the local work directory - but it did not constrain this remote operand, so its name and description claimed a boundary that was not enforced here. The same entry point had already been recognised on the local side: the localWorkDirectory download path was constrained so that a remote file name containing parent-directory segments could not resolve outside the local work directory. The remote operand was the remaining half of that surface. This artifact provides the smb scheme. Its consumer walks the share listing on its own rather than through RemoteFileConsumer, skipping only the exact "." and ".." entries, so a name carrying traversal segments in any other form was concatenated unchecked. Reaching it requires a server that emits a listing name which is not a single path segment, which a conforming SMB2 implementation does not do; the exposure was corrected on the same basis as the other remote-file consumers rather than from a demonstrated proof of concept against this scheme. Upgrade to Apache Camel 4.23.0, which fixes the issue. Users on the 4.22.x releases stream should upgrade to 4.22.1. Users on the 4.18.x LTS releases stream should upgrade to 4.18.5. The 4.14.x stream reached end of life and does not receive this fix; users on it should move to a supported releases stream.

### 9. CVE-2026-79984｜Apache Software Foundation / Apache Camel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T11:17:20.437)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T11:17:20.437 / 2026-10-20T04:17:04.390
- **官方描述（原文）**：Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Camel Mina SFTP component. This issue affects Apache Camel: from 4.18.0 before 4.18.5, from 4.19.0 before 4.22.1. The Camel remote-file consumers poll a directory on a remote server and build the absolute remote path of each file by concatenating the configured directory with the file name reported in the server's directory listing. That concatenation (FtpUtils.absoluteFilePath and GenericFileConsumer) applied no lexical normalization and no check that the result stayed inside the directory being polled, and the resulting path became the operand for every subsequent remote operation on the file: retrieval (FtpOperations.retrieveFile / SftpOperations, reached from GenericFileConsumer where the retrieve name is taken verbatim from GenericFile.getAbsoluteFilePath), deletion when delete=true (GenericFileDeleteProcessStrategy), and renaming when move, preMove, moveFailed or readLock=rename is configured (GenericFileProcessStrategySupport and GenericFileRenameExclusiveReadLockStrategy). Neither isValidFile nor isMatched performed any containment check. A listing entry that is not a single path segment therefore resolved to a path outside the configured polling directory, causing Camel to read, delete or rename files outside it using the endpoint's own credentials. A listing name is not route-controlled data. It is supplied by the remote server, and the FTP control channel carries no integrity protection at all, so an on-path attacker can rewrite a LIST response without holding any credentials; a compromised, malicious or multi-tenant server, or a server backed by a virtual filesystem, can emit such a name directly. Retrieval is reachable in a default consumer configuration, since the remote consumers download every listed file; deletion and renaming additionally require one of the disposition options above, all of which are common. Escape from the directory Camel was configured to poll is unconditional, while escape from the server's own account boundary additionally depends on whether that server confines the account. The jailStartingDirectory option, which is documented as restricting Camel to the starting directory and is enabled by default, governed producer writes and, since the localWorkDirectory containment work, consumer downloads to the local work directory - but it did not constrain this remote operand, so its name and description claimed a boundary that was not enforced here. The same entry point had already been recognised on the local side: the localWorkDirectory download path was constrained so that a remote file name containing parent-directory segments could not resolve outside the local work directory. The remote operand was the remaining half of that surface. This artifact provides the mina-sftp scheme, an alternative SFTP implementation whose consumer derives from the same RemoteFileConsumer base class and therefore inherited the same unconstrained resolution. Upgrade to Apache Camel 4.23.0, which fixes the issue. Users on the 4.22.x releases stream should upgrade to 4.22.1. Users on the 4.18.x LTS releases stream should upgrade to 4.18.5. The 4.14.x stream reached end of life and does not receive this fix; users on it should move to a supported releases stream.

### 10. CVE-2026-79983｜Apache Software Foundation / Apache Camel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T11:17:20.207)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T11:17:20.207 / 2026-10-20T04:17:04.003
- **官方描述（原文）**：Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Camel FTP component. This issue affects Apache Camel: from 4.0.0 before 4.18.5, from 4.19.0 before 4.22.1. The Camel remote-file consumers poll a directory on a remote server and build the absolute remote path of each file by concatenating the configured directory with the file name reported in the server's directory listing. That concatenation (FtpUtils.absoluteFilePath and GenericFileConsumer) applied no lexical normalization and no check that the result stayed inside the directory being polled, and the resulting path became the operand for every subsequent remote operation on the file: retrieval (FtpOperations.retrieveFile / SftpOperations, reached from GenericFileConsumer where the retrieve name is taken verbatim from GenericFile.getAbsoluteFilePath), deletion when delete=true (GenericFileDeleteProcessStrategy), and renaming when move, preMove, moveFailed or readLock=rename is configured (GenericFileProcessStrategySupport and GenericFileRenameExclusiveReadLockStrategy). Neither isValidFile nor isMatched performed any containment check. A listing entry that is not a single path segment therefore resolved to a path outside the configured polling directory, causing Camel to read, delete or rename files outside it using the endpoint's own credentials. A listing name is not route-controlled data. It is supplied by the remote server, and the FTP control channel carries no integrity protection at all, so an on-path attacker can rewrite a LIST response without holding any credentials; a compromised, malicious or multi-tenant server, or a server backed by a virtual filesystem, can emit such a name directly. Retrieval is reachable in a default consumer configuration, since the remote consumers download every listed file; deletion and renaming additionally require one of the disposition options above, all of which are common. Escape from the directory Camel was configured to poll is unconditional, while escape from the server's own account boundary additionally depends on whether that server confines the account. The jailStartingDirectory option, which is documented as restricting Camel to the starting directory and is enabled by default, governed producer writes and, since the localWorkDirectory containment work, consumer downloads to the local work directory - but it did not constrain this remote operand, so its name and description claimed a boundary that was not enforced here. The same entry point had already been recognised on the local side: the localWorkDirectory download path was constrained so that a remote file name containing parent-directory segments could not resolve outside the local work directory. The remote operand was the remaining half of that surface. This artifact provides the ftp, ftps and sftp schemes, all of which are affected. The reporter demonstrated the issue end to end against an ftp endpoint, driving a Camel route with a malicious server whose LIST response named a file outside the polled directory. Upgrade to Apache Camel 4.23.0, which fixes the issue. Users on the 4.22.x releases stream should upgrade to 4.22.1. Users on the 4.18.x LTS releases stream should upgrade to 4.18.5. The 4.14.x stream reached end of life and does not receive this fix; users on it should move to a supported releases stream.

### 11. CVE-2026-78165｜Apache Software Foundation / Apache Camel
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T11:17:19.643)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T11:17:19.643 / 2026-10-20T04:17:03.190
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Apache Camel Spring Redis component. This issue affects Apache Camel: from 2.11.0 before 4.18.5, from 4.19.0 before 4.22.1. RedisConfiguration.getSerializer lazily built a bare JdkSerializationRedisSerializer whenever no serializer option was configured, and that instance was used for every read the component performs. Spring's implementation delegates through DeserializingConverter to DefaultDeserializer, which reads the bytes with a ConfigurableObjectInputStream and installs no java.io.ObjectInputFilter on the stream, so an arbitrary serialized class graph was materialised and its readObject method executed. RedisConsumer.setBody applied that serializer to the raw bytes of every message published to the subscribed channels, before the Exchange was constructed and therefore before any route logic could inspect the message, so an actor able to issue PUBLISH on a subscribed channel reached the deserialization sink directly. The same default serializer backed the RedisTemplate built by RedisConfiguration.createDefaultTemplate, so the producer read commands GET, HGET, HGETALL and HVALS deserialized whatever was stored in the Redis keyspace, and SpringRedisIdempotentRepository shared that template. Configuring a custom redisTemplate did not close the consumer path, because RedisConsumer.setBody reads getSerializer directly rather than the serializer attached to the template, so a deployment that had wired a String serializer into its own template remained exposed on the consumer side unless it also set the serializer option. The component never constructed a java.io.ObjectInputStream itself, which is why earlier passes over the Camel codebase for unfiltered Java deserialization did not reach it. The behaviour dates back to the introduction of the component, first released in 2.11.0, and was unchanged until this fix. Users are recommended to upgrade to version 4.23.0, which fixes the issue. If users are on the 4.22.x releases stream, then they are suggested to upgrade to 4.22.1. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.5. The 4.14.x releases stream and earlier reached end of life before this issue was resolved and will not receive a fix, so deployments on those lines must move to a supported release. For deployments that cannot upgrade immediately, set the JVM-wide jdk.serialFilter system property, which the affected code path honours because it reads through a java.io.ObjectInputStream, for example -Djdk.serialFilter=!java.net.**;java.**;javax.**;org.apache.camel.**;!* ; or set the serializer endpoint option to a serializer that does not use Java serialization, such as StringRedisSerializer, noting that this must be set as the serializer option and not only on a custom redisTemplate. As defence in depth, require authentication on the Redis instance and restrict which clients may publish to the subscribed channels, and do not expose a Redis instance consumed by Camel to untrusted networks.

### 12. CVE-2026-53995｜mlflow / mlflow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T22:17:11.013)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T22:17:11.013 / 2026-10-19T22:17:11.013
- **官方描述（原文）**：MLflow 3.17.1 and earlier contains a path traversal vulnerability in the FileStore tracking backend that allows unauthenticated attackers to control filesystem paths by submitting a crafted trace ID containing traversal sequences to the POST /api/3.0/mlflow/traces endpoint. Attackers can exploit FileStore.start_trace() to write trace_info.yaml, request_metadata, and tag files with attacker-controlled metadata outside the intended experiment trace directory, subject to the server process's filesystem permissions. FileStore is the default tracking backend before MLflow 3.7.0 and opt-in thereafter (the default changed to a SQLite database), so deployments in the earlier part of the affected range are vulnerable without special configuration while later ones are affected only when FileStore is explicitly selected.

### 13. CVE-2026-112402｜python-pillow / Pillow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T22:17:07.633)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T22:17:07.633 / 2026-10-19T22:17:07.633
- **官方描述（原文）**：Pillow is a Python imaging library. Prior to 13.0.0, Pillow can double free image memory when ImagingScaleAffine encounters a selective allocation failure. The affected fast path handles Transform.EXTENT or pure scale-and-translate Transform.AFFINE operations with the default NEAREST resampling. The output image allocation must succeed while the additional per-column lookup allocation fails, after which the error path deletes image storage that later cleanup releases again. An attacker who can drive such a large Image.transform() operation under memory pressure may trigger the failure. This can crash the process and may corrupt memory. This issue is fixed in version 13.0.0.

### 14. CVE-2026-112397｜python-pillow / Pillow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T22:17:06.970)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T22:17:06.970 / 2026-10-19T22:17:06.970
- **官方描述（原文）**：Pillow is a Python imaging library. Prior to 13.0.0, Pillow's ImageMorph.MorphOp.apply() can access memory before a row buffer for a zero-width image. PPM and PGM input can create an image with width zero, and the native morphology routine indexes outrow[width - 1] without rejecting that geometry. An attacker can supply such an image to an application that applies a morphology operation. This can crash the process. This issue is fixed in version 13.0.0.

### 15. CVE-2026-112279｜rdesktop / rdesktop
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:05.977)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:05.977 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：rdesktop through 1.9.0 contains a heap out-of-bounds read vulnerability in process_bmpcache2() in orders.c that allows malicious RDP servers to crash clients via crafted revision-2 bitmap cache orders. Attackers can send an uncompressed order with large width/height or an underflowing mode nibble and short payload, causing memcpy() reads past the receive buffer and denial of service.

### 16. CVE-2026-112277｜rdesktop / rdesktop
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:05.663)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:05.663 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：rdesktop through 1.9.0 contains a heap out-of-bounds read vulnerability in process_plane() in bitmap.c that allows malicious RDP servers to crash clients by sending malformed 32 bpp compressed bitmaps. Attackers can declare a large bitmap geometry with a short compressed body in bitmap update PDUs or bitmap cache orders, causing unbounded reads past the receive buffer and denial of service.

### 17. CVE-2026-112269｜sgl-project / sglang
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:04.467)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:04.467 / 2026-10-19T19:17:27.590
- **官方描述（原文）**：SGLang through 0.5.22 with the Mooncake disaggregation backend accepts unauthenticated decode registration messages on the Prefill rank ZMQ PULL socket, allowing denial of service. Network-adjacent attackers can send many registrations with unique mooncake_session_id values and large nested-buffer frames to exhaust Prefill memory until the scheduler is OOM-killed.

### 18. CVE-2026-112266｜sgl-project / sglang
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:03.987)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:03.987 / 2026-10-19T15:17:05.480
- **官方描述（原文）**：SGLang through 0.5.22 contains a denial of service vulnerability that allows API clients to abort other users' in-flight generation requests by supplying a short client-controlled rid. Attackers can submit streaming /generate requests with single hex character rids and disconnect, triggering prefix-matching abort logic that terminates all other clients' requests.

### 19. CVE-2026-112264｜bentoml / BentoML
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:03.003)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:03.003 / 2026-10-19T21:13:39.973
- **官方描述（原文）**：BentoML through 1.4.39 contains a Dockerfile instruction injection vulnerability that allows attackers to add arbitrary build instructions by embedding newlines in docker.env mapping keys rendered by the legacy base.j2 template. Attackers can supply a crafted bentofile.yaml or imported bento archive so that bentoml containerize executes injected RUN instructions during docker build, accessing build secrets and poisoning images.

### 20. CVE-2026-112082｜sgl-project / SGLang
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T06:17:23.013)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.7 (HIGH)
- **EPSS**：0.00626 / percentile=0.4902
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T06:17:23.013 / 2026-10-19T17:17:11.123
- **官方描述（原文）**：A vulnerability was identified in sgl-project SGLang up to 0.5.19. This impacts the function Scheduler.expert_distribution_handle of the file python/sglang/srt/eplb/expert_distribution.py of the component Expert-Distribution Recording Endpoint. Such manipulation leads to denial of service. It is possible to launch the attack remotely. The exploit is publicly available and might be used. The pull request to fix this issue awaits acceptance.

### 21. CVE-2026-111759｜markdown-it / markdown-it
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T18:17:00.570)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T18:17:00.570 / 2026-10-19T21:13:39.973
- **官方描述（原文）**：markdown-it is a Markdown parser. Prior to 14.3.2 and 15.0.2, when typographer: true is enabled, specially crafted Markdown can cause quadratic processing time in the smartquotes rule, potentially leading to denial of service in applications processing untrusted input. Many opening double quotes followed by unmatched closing single quotes cause repeated scans of the entire opener stack. The same issue occurs with the quote types reversed. The default configuration (typographer: false) is not affected, but this option is enabled with high probability. This issue is fixed in versions 14.3.2 and 15.0.2.

### 22. CVE-2026-111755｜follow-redirects / follow-redirects
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T18:17:00.260)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T18:17:00.260 / 2026-10-19T21:13:39.973
- **官方描述（原文）**：follow-redirects is a Node.js HTTP and HTTPS client wrapper that automatically follows redirects. From 1.16.0 until 1.16.1, escapeRegex leaves valid header-name metacharacters unescaped in sensitiveHeaders. When an application declares a sensitive header whose name contains ^ or | and follows a cross-origin or HTTPS-to-HTTP redirect, unescaped regular-expression metacharacters prevent the generated filter from matching the declared header name, and the credential header is forwarded to an attacker-controlled redirect target. This issue is fixed in version 1.16.1.

### 23. CVE-2026-109431｜Camunda / Camunda 7
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T16:17:02.337)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T16:17:02.337 / 2026-10-19T21:13:39.973
- **官方描述（原文）**：Camunda 7.24.0 before 7.24.14 and 7.23.0 before 7.23.17 contains a missing authorization check vulnerability in engine-rest task sub-resources that allows authenticated attackers with no permission grants to access task comments and attachments by calling singular read and delete endpoints that lack the authorization-filtered checks enforced on their corresponding list endpoints. Attackers can exploit TaskAttachmentResourceImpl and TaskCommentResourceImpl methods such as getAttachment, getAttachmentData, deleteAttachment, and getComment using only a known object ID to read, download, or permanently delete task attachments and comments.

### 24. CVE-2026-90910｜Apache Software Foundation / Apache Answer
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T10:16:49.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T10:16:49.897 / 2026-10-19T20:45:51.597
- **官方描述（原文）**：Missing authentication for critical function vulnerability in Apache Answer. This issue affects Apache Answer: through 2.0.2. The reaction API did not enforce content visibility controls, allowing unauthorized users to read reaction metadata from restricted content or add and remove their own reactions. Users are recommended to upgrade to version 2.0.3, which fixes the issue.

### 25. CVE-2026-77936｜letta-ai / letta
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T01:17:20.107)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T01:17:20.107 / 2026-10-20T01:17:20.107
- **官方描述（原文）**：Letta through 0.16.8 ships a compose.yaml that does not enable LETTA_SERVER_SECURE, so the password middleware is never added and all API routes are unauthenticated, and it exposes a superuser PostgreSQL port with default credentials. Remote attackers can execute arbitrary Python via POST /v1/tools/run, manage /v1/admin users, or run OS commands via COPY PROGRAM.

### 26. CVE-2026-77933｜eosphoros-ai / DB-GPT
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T01:17:19.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T01:17:19.670 / 2026-10-20T01:17:19.783
- **官方描述（原文）**：DB-GPT through 0.8.2 contains a hardcoded credentials vulnerability in its default docker-compose.yml that sets a static MYSQL_ROOT_PASSWORD and publishes port 3306 on all interfaces. Attackers reaching port 3306 or the shared dbgptnet network can authenticate as root@% to gain full database access including FILE and SUPER privileges.

### 27. CVE-2026-77932｜eosphoros-ai / DB-GPT
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T01:17:19.503)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T01:17:19.503 / 2026-10-20T01:17:19.623
- **官方描述（原文）**：DB-GPT through 0.8.2 contains an unauthenticated remote code execution vulnerability because the /api/v1/chat/react-agent endpoint relies on a mock get_user_from_headers function that grants every caller the admin role. Unauthenticated attackers can send prompts that make the ReAct agent's unsandboxed code_interpreter and shell_interpreter tools run arbitrary Python or bash as root in the webserver container, including reaching the bundled database with default credentials.

### 28. CVE-2026-75128｜chatchat-space / Langchain-Chatchat
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T01:17:19.063)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T01:17:19.063 / 2026-10-20T01:17:19.063
- **官方描述（原文）**：Langchain-Chatchat through 0.3.1.3 exposes a POST /tools/call API endpoint that invokes any registered tool by name without authentication, leaving the always-registered shell tool callable. Remote attackers can send a single request naming the shell tool to execute arbitrary OS commands as the server user (root in the shipped Docker image).

### 29. CVE-2026-113380｜Signal / RingRTC
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T05:16:54.083)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T05:16:54.083 / 2026-10-20T05:16:54.083
- **官方描述（原文）**：In the RingRTC library before 2.72.0 for Signal, a peer that saturates a call's FSM queue can interfere with the ability of a local hangup to tear the call (with its audio and perhaps also video track) down.

### 30. CVE-2026-112900｜python-pillow / Pillow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T22:17:10.160)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T22:17:10.160 / 2026-10-19T22:17:10.160
- **官方描述（原文）**：Pillow is a Python imaging library. From 2.6.0 until 13.0.0, Pillow is vulnerable to argument injection when invoking Ghostscript for EPS input. EpsImagePlugin.Ghostscript passes a caller-controlled input filename after -f without converting it to a safe absolute path, so a name beginning with a hyphen can be interpreted as a Ghostscript option. An attacker who controls the filename can inject Ghostscript arguments. Arbitrary command execution specifically requires a leading @ argument-file filename and control of the referenced text file containing additional Ghostscript arguments; the reported chain reproduces with the default -dSAFER invocation. This issue is fixed in version 13.0.0.

### 31. CVE-2026-112780｜getgrav / grav
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T20:17:55.473)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T20:17:55.473 / 2026-10-19T20:17:55.587
- **官方描述（原文）**：Grav from 2.0.15 before 2.2.2 contains an allowlist bypass vulnerability that allows page editors to call arbitrary public static methods by renaming Flex form fields with replace-name@. Attackers with page-edit permission can smuggle data-*@ directives past the callable check to invoke Folder::delete, Folder::move, or Utils::download, deleting directories, overwriting files, or reading files.

### 32. CVE-2026-112779｜getgrav / grav-plugin-api
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T20:17:55.323)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T20:17:55.323 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：Grav API plugin (grav-plugin-api) 1.0.40 before 1.0.42 caches a full translation dictionary for every well-formed language code sent to the unauthenticated GET /api/v1/translations/{lang} endpoint, and 1.0.16 before 1.0.42 fails to check target and destination page rules in the sync and batch copy endpoints. Unauthenticated attackers can send small requests that each store about 560 KB to exhaust disk or APCu, while accounts with api.pages.write can overwrite translations or create pages that page-level rules deny.

### 33. CVE-2026-112776｜craftcms / cms
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T20:17:54.900)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T20:17:54.900 / 2026-10-19T20:59:50.503
- **官方描述（原文）**：Craft CMS from 5.0.0 before 5.11.0 contains an authorization bypass vulnerability that allows site-scoped GraphQL tokens to mutate other sites' content because requireAllowedSite() is not enforced. Attackers holding a site-A token can create entries in site B via supplied siteId and delete entries, categories, tags, and assets shared across sites.

### 34. CVE-2026-112403｜python-pillow / Pillow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T22:17:07.770)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T22:17:07.770 / 2026-10-19T22:17:07.770
- **官方描述（原文）**：Pillow is a Python imaging library. Prior to 13.0.0, Pillow's JPEG decoder can write a full-width scanline into a buffer sized for a requested draft scale. ImagingJpegDecode does not verify libjpeg's actual output width and component count after scaling is requested, and an 8-bit lossless SOF3 JPEG decoded by a build linked to libjpeg-turbo 3.x can ignore the requested downscaling geometry. An attacker can supply such a JPEG to an application that uses draft() or thumbnail() to request downscaling. This can corrupt heap memory, crash the process, or potentially allow code execution. Older libjpeg-turbo 2.x and IJG builds reject the SOF3 input. This issue is fixed in version 13.0.0.

### 35. CVE-2026-112398｜python-pillow / Pillow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T22:17:07.107)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T22:17:07.107 / 2026-10-19T22:17:07.107
- **官方描述（原文）**：Pillow is a Python imaging library. Prior to 13.0.0, Pillow's FlashPix JPEG-tile decoder can write decoded scanlines beyond the allocated tile buffer. FlashPix (FPX) JPEG decoding selects raw mode LA with two bytes per pixel, while an unrecognized JPEG mode can be decoded as JCS_UNKNOWN with four components, causing ImagingJpegDecode to write four-component scanlines into the two-byte tile buffer. An attacker can supply a crafted OLE2 FlashPix file to an application with the optional olefile dependency installed that opens or thumbnails untrusted input. This can corrupt heap memory and may allow arbitrary code execution. This issue is fixed in version 13.0.0.

### 36. CVE-2026-112377｜CCC-Attestation / attested-tls-poc
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T18:17:05.490)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T18:17:05.490 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：CCC Attestation SIG attested-tls-poc through commit 731ca82 fails to bind early attestation Evidence to the TLS connection, allowing attackers to relay valid Evidence from a genuine attester. Attackers holding an extracted attested TLS private key can forward the relying party's nonce to a genuine attester and replay its Evidence to impersonate the attested workload and intercept data.

### 37. CVE-2026-112296｜sunkaifei / FlyCms
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:08.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:08.510 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：FlyCms through commit edfdf724 contains a default credentials vulnerability that allows unauthenticated remote attackers to gain super administrator access via the flycms account with password admin123. Attackers can log in through POST /api/auth/login, solving only the image captcha, to obtain full control of site content, users and configuration.

### 38. CVE-2026-112292｜operacle / checkcle
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:07.903)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:07.903 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：CheckCle through 1.6.0 contains a missing authorization vulnerability that allows unauthenticated attackers to read, modify and delete records because shipped PocketBase collections use empty API rules. Attackers can query /api/collections/<name>/records endpoints to steal server_token values and alert_configurations secrets, disable alerting, alter status pages, or delete monitoring data.

### 39. CVE-2026-111862｜RankMath / Rank Math SEO PRO
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T17:17:04.507)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T17:17:04.507 / 2026-10-19T20:43:24.237
- **官方描述（原文）**：Rank Math SEO PRO for WordPress is affected by a supply-chain compromise in a subset of version 3.0.123 packages downloaded or updated between October 15, 2026 at 20:02 UTC and October 16, 2026 at 07:12 UTC. Rank Math states that the affected plugin files contained malware that could compromise a website if the plugin was activated and directs sites that activated an affected package to treat the website as compromised. The malware may establish persistent access, communicate with rank1cdn[.]com, recreate hidden backdoors on page visits, and expose WordPress credentials, database credentials, API keys, and other secrets accessible to the web server. Rank Math identifies three malicious wp_options keys, hidden PHP backdoors, unauthorized administrator accounts, a fake WordPress core file, PHP-executable .cache files, and a system cron marker as incident indicators. Only packages obtained during the vendor-confirmed window are claimed as affected; version 3.0.123 alone is not sufficient to establish compromise. Rank Math removed the affected files and released version 3.0.124 as the clean replacement.

### 40. CVE-2026-111406｜PT Norther Lights Production / MapSVG
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T10:16:46.007)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T10:16:46.007 / 2026-10-19T17:17:03.770
- **官方描述（原文）**：Unrestricted Upload of File with Dangerous Type vulnerability in PT Norther Lights Production MapSVG mapsvg-lite-interactive-vector-maps allows Upload a Web Shell to a Web Server.This issue affects MapSVG: from n/a through 8.16.1.

### 41. CVE-2026-111058｜mljar / mercury
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T16:17:03.957)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T16:17:03.957 / 2026-10-19T21:13:39.973
- **官方描述（原文）**：Mercury is a Python framework for sharing Jupyter notebooks as web applications and dashboards. Prior to 3.2.6, default tokenless deployments allow anonymous clients to create Jupyter kernels and send execute_request messages containing arbitrary Python. The endpoint blocklist does not cover /api/kernels, and the websocket wrapper previously tracked idle activity without authorizing executable messages. This issue is fixed in version 3.2.6.

### 42. CVE-2026-111057｜mljar / mercury
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T16:17:03.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T16:17:03.810 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：Mercury is a Python framework for sharing Jupyter notebooks as web applications and dashboards. From 3.0.0 until 3.2.4, a missing comma in BLOCKED_PATTERNS concatenates the /lab and /api/terminals regular-expression literals. Requests to /api/terminals therefore bypass the anonymous endpoint blocklist and reach Jupyter Server's terminal API. An unauthenticated attacker can use the resulting interactive operating-system shell to execute commands and access data available to the Mercury process. This issue is fixed in version 3.2.4.

### 43. CVE-2026-110887｜HivePress / HivePress
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T10:16:45.627)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T10:16:45.627 / 2026-10-19T17:17:02.427
- **官方描述（原文）**：Improper Control of Generation of Code ('Code Injection') vulnerability in HivePress HivePress hivepress allows Remote Code Inclusion.This issue affects HivePress: from n/a through 1.7.32.

### 44. CVE-2026-109442｜cas-bigdatalab / piflow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-20T01:17:10.383)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-20T01:17:10.383 / 2026-10-20T01:17:10.383
- **官方描述（原文）**：piflow 2.0.0 through 2.0.1 contains a remote code execution vulnerability in its DeepAgents chat agent, whose POST /chat and POST /chat/stream endpoints lack authentication. Attackers can instruct the agent to call the exec_shell tool, which runs arbitrary commands via subprocess.run without human approval or an allow-list, exposing environment secrets such as LLM API keys and database credentials.

### 45. CVE-2026-109437｜CognicellAI / Cognition
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T19:17:19.807)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T19:17:19.807 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：Cognition before 0.13.0 contains an unauthenticated remote code execution vulnerability due to defaulting its agent sandbox backend to local execution and shipping no authentication on its REST/SSE API. Attackers can create a session via POST /sessions and post a message via POST /sessions/{id}/messages without credentials, causing the Deep Agents ReAct loop to run attacker-directed shell commands through the local shell backend, resulting in remote code execution as the server process.

### 46. CVE-2026-107188｜Eptura / Archibus
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T17:17:01.080)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T17:17:01.080 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：A user can upload export reports with any file contents and specify any contents. JSP code can be uploaded, JSPX can be specified as the file extension, and anyone can browse to the uploaded file, leading to command execution. The authentication bypass vulnerability can be chained with this vulnerability to run code on the server without authentication.

### 47. CVE-2026-112301｜orbitale / imagemagick-php
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T21:17:06.863)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T21:17:06.863 / 2026-10-19T22:17:05.897
- **官方描述（原文）**：A security flaw has been discovered in orbitale imagemagick-php up to 3.3.5. Affected by this issue is the function Command::font of the file src/Command.php. The manipulation of the argument fontFile results in os command injection. The attack can be executed remotely. The exploit has been released to the public and may be used for attacks. The vendor was contacted early about this disclosure but did not respond in any way.

### 48. CVE-2026-112289｜KoalixSwitzerland / koalixcrm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:07.460)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:07.460 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：Koalixcrm through 1.14.0 contains a stored cross-site scripting vulnerability that allows staff users to inject script by storing malicious task titles rendered unescaped by Task.link_to_task(). Attackers can embed HTML or script that executes when administrators open the task changelist or change form, enabling actions like creating a superuser.

### 49. CVE-2026-112284｜xqq / libaribcaption
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:06.687)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 4.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:06.687 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：libaribcaption 1.1.0 through 1.1.2 contains a global out-of-bounds read in DecoderImpl::HandleGLGR() that reads past the 78-entry kLatinSpecialTable without an upper bound check. Attackers can supply crafted captions designating the Latin special set with ESC 28 4C followed by bytes 0x6F-0x7E to leak adjacent read-only data or crash decoding.

### 50. CVE-2026-112282｜VideoLAN / libbluray
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:06.403)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:06.403 / 2026-10-19T21:13:39.973
- **官方描述（原文）**：VideoLAN libbluray through 1.5.1 contains an out-of-bounds read vulnerability in clpi_access_point() that allows attackers to crash applications by supplying a ClipInfo file with an empty EP-map fine table. Attackers can place a crafted .clpi file in BDMV/CLIPINF with num_ep_fine set to zero and an unclamped ref_ep_fine_id, triggering reads during seeking for denial of service.

### 51. CVE-2026-112281｜nkoriyama / aribb24
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:06.260)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:06.260 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：libaribb24 (aribb24) through 1.0.3 contains a stack-based buffer overflow vulnerability in decoder_handle_csi() in src/decoder.c that allows attackers to write past a fixed 256-entry array by supplying unbounded CSI parameter bytes. Attackers can embed a caption statement with a CSI introducer and over 256 parameter bytes in media files or broadcast streams to crash FFmpeg or VLC or corrupt the return address.

### 52. CVE-2026-112276｜Netpbm / Netpbm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:05.520)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:05.520 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：Netpbm through 11.16.00 contains a heap out-of-bounds read vulnerability in rasttopnm that allows attackers to read heap memory by supplying Sun rasterfiles with short colormaps. Attackers can craft colormapped rasterfiles with pixel bytes exceeding the palette length to leak up to 255 adjacent heap bytes into the PNM output or crash the program.

### 53. CVE-2026-112274｜libtins / libtins
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:05.223)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:05.223 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：libtins through 4.6 contains an out-of-bounds read vulnerability in DNS::soa_record::init that allows remote attackers to read past buffer bounds by supplying SOA data lacking NUL terminators. Attackers can feed raw SOA RDATA without a zero byte to applications using the buffer constructor, causing strlen to overrun the heap buffer and possibly crash.

### 54. CVE-2026-112272｜emersion / libdisplay-info
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:04.937)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:04.937 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：Libdisplay-info 0.4.0 contains a heap out-of-bounds read vulnerability in the DisplayID v2 section parser in displayid2.c that allows attackers to read past the EDID buffer via oversized data block lengths. Attackers can supply a crafted EDID from a malicious monitor, KVM, capture device, or file to over-advance the parse cursor and crash applications.

### 55. CVE-2026-112271｜emersion / libdisplay-info
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:04.787)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:04.787 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：libdisplay-info through 0.4.0 contains a heap out-of-bounds read vulnerability in the DisplayID v1 section parser in displayid.c that occurs when a data block's declared length exceeds the section. Attackers can supply a crafted EDID from a malicious monitor, KVM, capture device, or EDID file to make is_all_zeroes read past the buffer, causing a possible crash.

### 56. CVE-2026-112267｜sgl-project / sglang
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:04.160)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:04.160 / 2026-10-19T20:17:53.240
- **官方描述（原文）**：SGLang through 0.5.22 in prefill/decode disaggregation mode contains a server-side request forgery vulnerability that allows unauthenticated attackers to trigger outbound requests via client-supplied bootstrap_host and bootstrap_port fields. Attackers sending crafted requests to the Decode worker's /generate endpoint can probe internal hosts and ports and block the shared scheduler loop, delaying other inference requests.

### 57. CVE-2026-112190｜Webkul / Aureus ERP
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T17:17:14.140)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T17:17:14.140 / 2026-10-19T19:17:26.100
- **官方描述（原文）**：A security vulnerability has been detected in Webkul Aureus ERP up to 1.6.0. This issue affects some unknown processing of the file composer.json. Such manipulation leads to insertion of sensitive information into debugging code. The attack may be launched remotely. The exploit has been disclosed publicly and may be used. The vendor was contacted early about this disclosure.

### 58. CVE-2026-112153｜vraj404 / Criminal-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T16:17:05.567)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T16:17:05.567 / 2026-10-19T20:43:24.237
- **官方描述（原文）**：A vulnerability was detected in vraj404 Criminal-Management-System up to 2808d057e7ddc5295519a487365b0cacfd0ba8c4. This affects the function mysqli_error of the file Officers/addOfficer.php of the component Officer Registration Form. Performing a manipulation of the argument offName/offID/ID/contact/gender/weapon/role results in sql injection. It is possible to initiate the attack remotely. The exploit is now public and may be used. This product is using a rolling release to provide continious delivery. Therefore, no version details for affected nor updated releases are available. The project was informed of the problem early through an issue report but has not responded yet.

### 59. CVE-2026-112152｜vraj404 / Criminal-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T16:17:05.403)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T16:17:05.403 / 2026-10-19T20:43:24.237
- **官方描述（原文）**：A security vulnerability has been detected in vraj404 Criminal-Management-System up to 2808d057e7ddc5295519a487365b0cacfd0ba8c4. Affected by this issue is the function mysqli_query of the file Officers/searchOff.php of the component Search Page. Such manipulation of the argument Search leads to sql injection. The attack may be performed from remote. The exploit has been disclosed publicly and may be used. This product utilizes a rolling release system for continuous delivery, and as such, version information for affected or updated releases is not disclosed. The project was informed of the problem early through an issue report but has not responded yet.

### 60. CVE-2026-112151｜vraj404 / Criminal Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T15:17:05.207)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T15:17:05.207 / 2026-10-19T20:43:24.237
- **官方描述（原文）**：A weakness has been identified in vraj404 Criminal Management System up to 2808d057e7ddc5295519a487365b0cacfd0ba8c4. Affected by this vulnerability is an unknown functionality of the file home.php of the component Submission Form. This manipulation of the argument id/name/offName/crime/dob/arrDate/crimeDate/sex/address/folder/more causes sql injection. The attack is possible to be carried out remotely. The exploit has been made available to the public and could be used for attacks. This product adopts a rolling release strategy to maintain continuous delivery. Therefore, version details for affected or updated releases cannot be specified. The project was informed of the problem early through an issue report but has not responded yet.

### 61. CVE-2026-112149｜vraj404 / Criminal-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T15:17:03.943)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T15:17:03.943 / 2026-10-19T20:43:24.237
- **官方描述（原文）**：A vulnerability was identified in vraj404 Criminal-Management-System up to 2808d057e7ddc5295519a487365b0cacfd0ba8c4. This impacts the function move_uploaded_file of the file home.php. The manipulation of the argument my_img leads to unrestricted upload. Remote exploitation of the attack is possible. The exploit is publicly available and might be used. This product follows a rolling release approach for continuous delivery, so version details for affected or updated releases are not provided. The project was informed of the problem early through an issue report but has not responded yet.

### 62. CVE-2026-112147｜ai-genius-automations / octoally
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T15:16:56.830)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T15:16:56.830 / 2026-10-19T20:43:24.237
- **官方描述（原文）**：A vulnerability was found in ai-genius-automations octoally up to 1.0.87. The impacted element is an unknown function of the file server/src/index.ts. Performing a manipulation of the argument path results in information disclosure. The attack may be initiated remotely. The exploit has been made public and could be used. Upgrading to version 1.0.88 is sufficient to resolve this issue. The patch is named 3898085c4e701be21377ebd9e91e10b941e47168. It is recommended to upgrade the affected component.

### 63. CVE-2026-112144｜satya-vinay / Events-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:01.967)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:01.967 / 2026-10-19T15:16:56.707
- **官方描述（原文）**：A weakness has been identified in satya-vinay Events-Management-System up to 437c77ceb69bf9fe2e3f4f46f7871b83f425383a. This affects an unknown part of the file project.sql. Executing a manipulation can lead to files or directories accessible. The attack may be performed from remote. The exploit has been made available to the public and could be used for attacks. This product utilizes a rolling release system for continuous delivery, and as such, version information for affected or updated releases is not disclosed. The project was informed of the problem early through an issue report but has not responded yet.

### 64. CVE-2026-112143｜satya-vinay / Events-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:01.800)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:01.800 / 2026-10-19T17:17:13.060
- **官方描述（原文）**：A security flaw has been discovered in satya-vinay Events-Management-System up to 437c77ceb69bf9fe2e3f4f46f7871b83f425383a. Affected by this issue is some unknown functionality. Performing a manipulation results in missing authentication. The attack is possible to be carried out remotely. The exploit has been released to the public and may be used for attacks. This product adopts a rolling release strategy to maintain continuous delivery. Therefore, version details for affected or updated releases cannot be specified. Multiple endpoints are affected. The project was informed of the problem early through an issue report but has not responded yet.

### 65. CVE-2026-112142｜satya-vinay / Events-Management-System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T13:16:57.303)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T13:16:57.303 / 2026-10-19T19:17:25.783
- **官方描述（原文）**：A vulnerability was identified in satya-vinay Events-Management-System up to 437c77ceb69bf9fe2e3f4f46f7871b83f425383a. Affected by this vulnerability is an unknown functionality of the file dodelete.php of the component Registration-Delete Handler. Such manipulation of the argument ID leads to sql injection. The attack can be executed remotely. The exploit is publicly available and might be used. This product implements a rolling release for ongoing delivery, which means version information for affected or updated releases is unavailable. The project was informed of the problem early through an issue report but has not responded yet.

### 66. CVE-2026-112139｜subhajitkhan / online-clinic-management-system
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T12:17:01.563)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T12:17:01.563 / 2026-10-19T17:17:12.927
- **官方描述（原文）**：A vulnerability has been found in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a29a578. This affects an unknown function of the file admindocview.php of the component Administrative Mutation Handler. The manipulation of the argument docid leads to sql injection. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used. This product uses a rolling release model to deliver continuous updates. As a result, specific version information for affected or updated releases is not available. The project was informed of the problem early through an issue report but has not responded yet.

### 67. CVE-2026-112083｜sgl-project / SGLang
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T06:17:23.377)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00419 / percentile=0.34772
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T06:17:23.377 / 2026-10-19T17:17:11.287
- **官方描述（原文）**：A security flaw has been discovered in sgl-project SGLang up to 0.5.19. Affected is the function WeightExporter.send_weights_to_remote_instance of the file python/sglang/srt/model_executor/model_runner_components/weight_exporter.py of the component Weight Exporter. Performing a manipulation of the argument group_name results in denial of service. The attack can be initiated remotely. The exploit has been released to the public and may be used for attacks. The pull request to fix this issue awaits acceptance.

### 68. CVE-2026-111925｜Mopidy / Mopidy
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:00.893)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:00.893 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：Mopidy before 4.0.5 contains a path traversal vulnerability that allows unauthenticated clients to access local files outside file/media_dirs because FileLibraryProvider.lookup() lacks a containment check. Attackers can call core.library.lookup or core.tracklist.add over JSON-RPC or WebSocket with file:// URIs to probe file existence, read tag metadata, and play out-of-sandbox files.

### 69. CVE-2026-111061｜Eugeny / russh
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T17:17:03.080)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T17:17:03.080 / 2026-10-19T19:17:22.890
- **官方描述（原文）**：russh is a Rust SSH client and server library that includes an SSH agent protocol implementation. Prior to 0.64.1, the agent server spawns a separate long-lived task for every SSH_AGENT_CONSTRAIN_LIFETIME record in a constrained add-key request. The loop accepts repeated lifetime records, clones the key blob into each task, and does not roll back tasks when later constraint parsing fails. An attacker that can speak the agent protocol locally or through agent forwarding can exhaust memory and tasks until the agent process is starved or terminated, denying SSH agent service. This issue is fixed in version 0.64.1.

### 70. CVE-2026-109433｜Camunda / Camunda 7
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T16:17:02.623)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.0 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T16:17:02.623 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：Camunda 7.24.0 before 7.24.14 and 7.23.0 before 7.23.17 contains an authorization bypass vulnerability in the Cockpit webapp that allows authenticated attackers to bypass permission checks due to an inverted comparison logic in AbstractCockpitPluginResource.isPermissionDisabled(). Attackers with minimal Cockpit access can exploit a non-empty disabledPermissions configuration to read all process instances, process definitions, and incidents engine-wide without triggering any logging, regardless of their actual data grants.

### 71. CVE-2025-55667｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T18:16:58.337)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T18:16:58.337 / 2026-10-19T21:14:14.150
- **官方描述（原文）**：A segmentation violation in the dump_isom_saps function (/mp4box/filedump.c) of GPAC MP4Box v2.5-DEV-rev1672-gc9a31d0e1-masterallows attackers to cause a Denial of Service (DoS) via supplying a crafted MP4 file.

### 72. CVE-2026-112251｜antoinersx / clawhost
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T19:17:26.953)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T19:17:26.953 / 2026-10-19T20:43:24.237
- **官方描述（原文）**：A vulnerability was detected in antoinersx clawhost up to 0.0.45. This affects the function handleRequest of the file apps/clawhostgo/src/main/services/reverseProxy.ts of the component Reverse Proxy. Performing a manipulation of the argument token results in open redirect. The attack can be initiated remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 73. CVE-2026-112195｜未確認 / FusionPBX
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T17:17:14.533)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T17:17:14.533 / 2026-10-19T20:43:24.237
- **官方描述（原文）**：A flaw has been found in FusionPBX up to 5.4.4/5.5.7/5.6.5. The affected element is an unknown function of the file app/dialplans/resources/classes/dialplan.php of the component Dialplan Editor. Executing a manipulation can lead to os command injection. The attack can be executed remotely. The exploit has been published and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 74. CVE-2026-112146｜D-Link / E15
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T14:17:02.317)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T14:17:02.317 / 2026-10-19T18:17:03.040
- **官方描述（原文）**：A vulnerability was detected in D-Link E15, M32, R15 and R32. This issue affects some unknown processing of the file /etc/emDaemon/passwd of the component MQTT Broker. The manipulation results in hard-coded credentials. It is possible to launch the attack remotely. The exploit is now public and may be used.

### 75. CVE-2026-112140｜llSourcell / Doctor-Dignity
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T12:17:01.740)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T12:17:01.740 / 2026-10-19T15:16:45.150
- **官方描述（原文）**：A vulnerability was found in llSourcell Doctor-Dignity up to 3f2ffb6c892f13b50a708d05900d3227acb40ded. This impacts the function _get_lib_module of the file python/mlc_chat/chat_module.py. The manipulation of the argument model_lib results in code injection. The attack may be launched remotely. The exploit has been made public and could be used. This product operates on a rolling release basis, ensuring continuous delivery. Consequently, there are no version details for either affected or updated releases. The project was informed of the problem early through an issue report but has not responded yet.

### 76. CVE-2026-112138｜diem-project / diem
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T12:17:01.383)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T12:17:01.383 / 2026-10-19T19:17:25.643
- **官方描述（原文）**：A flaw has been found in diem-project diem up to 5.1.3. The impacted element is the function dmOs::join of the file dmFrontPlugin/modules/dmCodeEditor/actions/actions.class.php of the component dmCodeEditor. Executing a manipulation can lead to path traversal. The attack can be launched remotely. The exploit has been published and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 77. CVE-2026-112107｜ztxz16 / fastllm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T12:17:00.937)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T12:17:00.937 / 2026-10-19T15:16:45.150
- **官方描述（原文）**：A flaw has been found in ztxz16 fastllm up to 1.8.2. Affected by this issue is the function SafeTensorItem::CreateBuffer of the file src/model.cpp of the component Safetensors Weight Loading. This manipulation of the argument data_offsets causes buffer overflow. The attack can be initiated remotely. The exploit has been published and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 78. CVE-2026-112102｜AXA Group / NLP.js
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T10:16:46.780)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T10:16:46.780 / 2026-10-19T17:17:12.490
- **官方描述（原文）**：A vulnerability was detected in AXA Group NLP.js 4.27.0. This impacts the function Evaluator.walkFunction of the file packages/evaluator/src/evaluator.js of the component Condition Expression Pipeline. The manipulation of the argument condition results in code injection. It is possible to launch the attack remotely. The exploit is now public and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 79. CVE-2026-112101｜BlackBeltTechnology / pi-agent-dashboard
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T10:16:46.610)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T10:16:46.610 / 2026-10-19T17:17:12.347
- **官方描述（原文）**：A vulnerability was determined in BlackBeltTechnology pi-agent-dashboard up to 0.8.0. The affected element is an unknown function of the file /BlackBeltTechnology/pi-agent-dashboard of the component WebSocket Gateway. Executing a manipulation of the argument cwd can lead to origin validation error. The attack can be executed remotely. The exploit has been publicly disclosed and may be utilized. Upgrading to version 0.9.0 is sufficient to fix this issue. This patch is called 48fd0bad5adfe76af9736599699d51a5f60019f6. It is recommended to upgrade the affected component.

### 80. CVE-2026-112098｜未確認 / DeepPavlov
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T09:17:07.917)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00315 / percentile=0.22968
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T09:17:07.917 / 2026-10-19T18:17:02.897
- **官方描述（原文）**：A security flaw has been discovered in DeepPavlov up to 1.7.0. Impacted is the function resolve of the file deeppavlov/core/common/params.py of the component Config Reference Resolver. The manipulation results in code injection. The attack can be launched remotely. The exploit has been released to the public and may be used for attacks. The project was informed of the problem early through an issue report but has not responded yet.

### 81. CVE-2026-112096｜SourceCodester / Inventory System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T09:17:07.570)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：0.00199 / percentile=0.09079
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T09:17:07.570 / 2026-10-19T17:17:12.053
- **官方描述（原文）**：A vulnerability has been found in SourceCodester Inventory System 1.0. This vulnerability affects unknown code of the file /api/transactions_handler.php?action=save_purchase of the component Purchase Records Handler. The manipulation of the argument Product_Name/Product_Code/Vendor_Name leads to cross site scripting. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used.

### 82. CVE-2026-112094｜michaelrsweet / mxml
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T08:17:03.623)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：0.0018 / percentile=0.07132
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T08:17:03.623 / 2026-10-19T18:17:02.750
- **官方描述（原文）**：A security vulnerability has been detected in michaelrsweet mxml 4.0.5/4.0.6. This affects the function mxml_load_data of the file mxml-file.c. The manipulation leads to use after free. The attack is possible to be carried out remotely. The exploit has been disclosed publicly and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 83. CVE-2026-112093｜subhajitkhan / online-clinic-management-system
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T08:17:03.440)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00273 / percentile=0.18466
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T08:17:03.440 / 2026-10-19T17:17:11.910
- **官方描述（原文）**：A vulnerability has been found in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a29a578. The impacted element is an unknown function of the file feedback.php. The manipulation of the argument msg leads to cross site scripting. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. Continious delivery with rolling releases is used by this product. Therefore, no version details of affected nor updated releases are available. The project was informed of the problem early through an issue report but has not responded yet.

### 84. CVE-2026-112092｜subhajitkhan / online-clinic-management-system
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T08:17:03.240)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00273 / percentile=0.18466
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T08:17:03.240 / 2026-10-19T17:17:11.760
- **官方描述（原文）**：A flaw has been found in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a29a578. The affected element is the function echo of the file doctorregistration.php of the component Doctor Registration. Executing a manipulation of the argument doc_name can lead to cross site scripting. It is possible to launch the attack remotely. The exploit has been published and may be used. This product takes the approach of rolling releases to provide continious delivery. Therefore, version details for affected and updated releases are not available. The project was informed of the problem early through an issue report but has not responded yet.

### 85. CVE-2026-112090｜Dav-ee / dairy-management-system
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T08:17:02.813)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.002 / percentile=0.0931
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T08:17:02.813 / 2026-10-19T18:17:02.610
- **官方描述（原文）**：A vulnerability was detected in Dav-ee dairy-management-system 31ace9692d1e1e6d64339a42c463b361319c615c/f31a584c3330c013b61f8b0306d9e0849c6d693d. This issue affects the function mysqli_real_escape_string of the file payment/pay.php. The manipulation of the argument f_no/farmer results in sql injection. The attack may be launched remotely. The exploit is now public and may be used. This product operates on a rolling release basis, ensuring continuous delivery. Consequently, there are no version details for either affected or updated releases. The project was informed of the problem early through an issue report but has not responded yet.

### 86. CVE-2026-112089｜Dav-ee / dairy-management-system
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T07:16:31.050)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：0.0021 / percentile=0.1058
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T07:16:31.050 / 2026-10-19T17:17:11.607
- **官方描述（原文）**：A security vulnerability has been detected in Dav-ee dairy-management-system 31ace9692d1e1e6d64339a42c463b361319c615c/f31a584c3330c013b61f8b0306d9e0849c6d693d. This vulnerability affects the function mysqli_query of the file employees/delete.php. The manipulation of the argument e_payroll_no leads to sql injection. The attack may be initiated remotely. The exploit has been disclosed publicly and may be used. This product uses a rolling release model to deliver continuous updates. As a result, specific version information for affected or updated releases is not available. The project was informed of the problem early through an issue report but has not responded yet.

### 87. CVE-2026-112088｜Dav-ee / dairy-management-system
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T07:16:30.873)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.002 / percentile=0.09307
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T07:16:30.873 / 2026-10-19T17:17:11.460
- **官方描述（原文）**：A weakness has been identified in Dav-ee dairy-management-system 31ace9692d1e1e6d64339a42c463b361319c615c/f31a584c3330c013b61f8b0306d9e0849c6d693d. This affects the function mysqli_query of the file farmers/add.php. Executing a manipulation of the argument f_no/f_id/f_name/f_locallity/f_ac/f_phone can lead to sql injection. The attack can be launched remotely. The exploit has been made available to the public and could be used for attacks. This product does not use versioning. This is why information about affected and unaffected releases are unavailable. The vendor was contacted early about this disclosure.

### 88. CVE-2026-112086｜未確認 / ESPnet
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-19T06:17:23.667)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00316 / percentile=0.23051
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-19T06:17:23.667 / 2026-10-19T18:17:02.463
- **官方描述（原文）**：A vulnerability was found in ESPnet up to 202610.post2. This affects the function build_model of the file espnet3/publication/inference_model.py of the component Inference Model Handler. The manipulation of the argument _target_ results in deserialization. It is possible to launch the attack remotely. The exploit has been made public and could be used. The patch is identified as f217b24f06de55e332cab10231469d5890dbbe00. It is best practice to apply a patch to resolve this issue.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-78162 | P3 / 38 | Apache Software Foundation / Apache Camel | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112393 | P3 / 38 | python-pillow / Pillow | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-109432 | P3 / 38 | Camunda / Camunda 7 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-107083 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-95210 | WATCH / 4 | 未確認 / 未確認 | v3.1 4.8 (MEDIUM) | 0.00228 / percentile=0.12674 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-88647 | WATCH / 4 | 未確認 / 未確認 | v3.1 6.5 (MEDIUM) | 0.00212 / percentile=0.10816 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-79986 | WATCH / 30 | Apache Software Foundation / Apache Camel | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79985 | WATCH / 30 | Apache Software Foundation / Apache Camel | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79984 | WATCH / 30 | Apache Software Foundation / Apache Camel | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-79983 | WATCH / 30 | Apache Software Foundation / Apache Camel | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-78165 | WATCH / 30 | Apache Software Foundation / Apache Camel | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-53995 | WATCH / 30 | mlflow / mlflow | v4.0 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112402 | WATCH / 30 | python-pillow / Pillow | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112397 | WATCH / 30 | python-pillow / Pillow | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112279 | WATCH / 30 | rdesktop / rdesktop | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112277 | WATCH / 30 | rdesktop / rdesktop | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112269 | WATCH / 30 | sgl-project / sglang | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112266 | WATCH / 30 | sgl-project / sglang | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112264 | WATCH / 30 | bentoml / BentoML | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-112082 | WATCH / 30 | sgl-project / SGLang | v4.0 7.7 (HIGH) | 0.00626 / percentile=0.4902 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111759 | WATCH / 30 | markdown-it / markdown-it | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-111755 | WATCH / 30 | follow-redirects / follow-redirects | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-109431 | WATCH / 30 | Camunda / Camunda 7 | v4.0 8.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-90910 | WATCH / 28 | Apache Software Foundation / Apache Answer | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-77936 | WATCH / 28 | letta-ai / letta | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-77933 | WATCH / 28 | eosphoros-ai / DB-GPT | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-77932 | WATCH / 28 | eosphoros-ai / DB-GPT | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-75128 | WATCH / 28 | chatchat-space / Langchain-Chatchat | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-113380 | WATCH / 28 | Signal / RingRTC | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-112900 | WATCH / 28 | python-pillow / Pillow | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：3；缺少 Product：3；缺少 Title：30。
- EPSS 未確認：27；Exploitation status 未確認：6。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-20T05:33:48.385179+00:00`；Delta generated at：`2026-10-20T05:33:48.385179+00:00`。

---

## 可驗證資料來源

- **CVE-2026-95210** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-95210) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-95210)
- **CVE-2026-88647** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88647) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88647)
- **CVE-2026-78162** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78162)
- **CVE-2026-112393** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112393)
- **CVE-2026-109432** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109432)
- **CVE-2026-107083** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107083)
- **CVE-2026-79986** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79986)
- **CVE-2026-79985** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79985)
- **CVE-2026-79984** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79984)
- **CVE-2026-79983** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79983)
- **CVE-2026-78165** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78165)
- **CVE-2026-53995** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53995)
- **CVE-2026-112402** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112402)
- **CVE-2026-112397** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112397)
- **CVE-2026-112279** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112279)
- **CVE-2026-112277** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112277)
- **CVE-2026-112269** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112269)
- **CVE-2026-112266** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112266)
- **CVE-2026-112264** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112264)
- **CVE-2026-112082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112082) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112082)
- **CVE-2026-111759** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111759)
- **CVE-2026-111755** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111755)
- **CVE-2026-109431** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109431)
- **CVE-2026-90910** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-90910)
- **CVE-2026-77936** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77936)
- **CVE-2026-77933** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77933)
- **CVE-2026-77932** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77932)
- **CVE-2026-75128** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75128)
- **CVE-2026-113380** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113380)
- **CVE-2026-112900** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112900)
- **CVE-2026-112780** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112780)
- **CVE-2026-112779** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112779)
- **CVE-2026-112776** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112776)
- **CVE-2026-112403** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112403)
- **CVE-2026-112398** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112398)
- **CVE-2026-112377** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112377)
- **CVE-2026-112296** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112296)
- **CVE-2026-112292** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112292)
- **CVE-2026-111862** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111862)
- **CVE-2026-111406** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111406)
- **CVE-2026-111058** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111058)
- **CVE-2026-111057** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111057)
- **CVE-2026-110887** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110887)
- **CVE-2026-109442** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109442)
- **CVE-2026-109437** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109437)
- **CVE-2026-107188** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107188)
- **CVE-2026-112301** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112301)
- **CVE-2026-112289** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112289)
- **CVE-2026-112284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112284)
- **CVE-2026-112282** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112282)
- **CVE-2026-112281** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112281)
- **CVE-2026-112276** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112276)
- **CVE-2026-112274** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112274)
- **CVE-2026-112272** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112272)
- **CVE-2026-112271** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112271)
- **CVE-2026-112267** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112267)
- **CVE-2026-112190** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112190)
- **CVE-2026-112153** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112153)
- **CVE-2026-112152** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112152)
- **CVE-2026-112151** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112151)
- **CVE-2026-112149** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112149)
- **CVE-2026-112147** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112147)
- **CVE-2026-112144** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112144)
- **CVE-2026-112143** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112143)
- **CVE-2026-112142** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112142)
- **CVE-2026-112139** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112139)
- **CVE-2026-112083** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112083) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112083)
- **CVE-2026-111925** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111925)
- **CVE-2026-111061** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111061)
- **CVE-2026-109433** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109433)
- **CVE-2025-55667** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-55667)
- **CVE-2026-112251** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112251)
- **CVE-2026-112195** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112195)
- **CVE-2026-112146** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112146)
- **CVE-2026-112140** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112140)
- **CVE-2026-112138** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112138)
- **CVE-2026-112107** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112107)
- **CVE-2026-112102** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112102)
- **CVE-2026-112101** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112101)
- **CVE-2026-112098** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112098) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112098)
- **CVE-2026-112096** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112096) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112096)
- **CVE-2026-112094** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112094) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112094)
- **CVE-2026-112093** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112093) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112093)
- **CVE-2026-112092** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112092) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112092)
- **CVE-2026-112090** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112090) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112090)
- **CVE-2026-112089** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112089) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112089)
- **CVE-2026-112088** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112088) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112088)
- **CVE-2026-112086** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112086) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-112086)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
