# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**105** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=102、NEW_KEV=3。
- Intelligence 候選：**30** 筆；P1 **3**、P2 **0**、P3 **7**、WATCH **20**。
- Baseline：state / generated_at=2026-09-18T05:24:29.078693+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-53266、CVE-2025-39682、CVE-2025-39964。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **105** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-53266｜Linux / Kernel
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00121 / percentile=0.02189
- **CISA KEV**：listed=true / date_added=2026-09-18 / due_date=2026-09-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-06-25T09:16:44.643 / 2026-09-19T04:17:53.580
- **官方描述（原文）**：Linux Kernel contains an out-of-bounds write vulnerability in the ebtables SNAT target which allows an ARP sender hardware address rewrite to write directly into a nonlinear socket-buffer fragment backed by a splice-imported file page. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.

### 2. CVE-2025-39682｜Linux / Kernel
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：0.00505 / percentile=0.42129
- **CISA KEV**：listed=true / date_added=2026-09-18 / due_date=2026-09-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2025-09-05T18:15:44.670 / 2026-09-19T04:17:35.263
- **官方描述（原文）**：Linux Kernel contains an improper check for unusual or exceptional conditions vulnerability in the TLS receive path which allows a zero-length record retrieved from the rx_list to bypass the intended recvmsg() record-type handling, potentially causing subsequent TLS records to be processed using incorrect zero-copy and queuing assumptions. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.

### 3. CVE-2025-39964｜Linux / Kernel
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00323 / percentile=0.25599
- **CISA KEV**：listed=true / date_added=2026-09-18 / due_date=2026-09-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2025-10-13T14:15:34.737 / 2026-09-19T04:17:48.307
- **官方描述（原文）**：Linux Kernel contains a race condition vulnerability which allows concurrent writes to the same AF_ALG socket causing data to be unpredictably interleaved and creating inconsistencies in the socket's internal state.

### 4. CVE-2026-93868｜Cotonti / Cotonti
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:34.633)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:34.633 / 2026-09-18T21:18:49.023
- **官方描述（原文）**：Cotonti through 1.0.0 derives password recovery validation tokens from md5(microtime()) in users.passrecover.php, creating a predictable token space of approximately one million values per second. Unauthenticated attackers can read the server Date header, precompute candidate tokens within a narrow time window, and probe them against the passrecover authentication endpoint to reset any account password including administrators.

### 5. CVE-2026-93606｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:12.500)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:12.500 / 2026-09-18T18:18:31.267
- **官方描述（原文）**：vm2 (npm) versions 3.12.0 and earlier contain a sandbox escape in `VM` and `NodeVM`. When an embedder exposes a host API that returns a host-realm Promise, the bridge's rejection sanitizer (hostPromiseSanitizeReject / makeSanitizedPromiseCallback / normalizeHostPromiseCallbacks in lib/bridge.js) only wraps `then`/`catch` rejection slots that hold a function, and the sandbox-side `Symbol.species`/`.then` neutralization is installed only on the sandbox intrinsic `Promise.prototype`, so it never applies to a host Promise. Code running inside the sandbox can overwrite `p.constructor[Symbol.species]` on the host Promise and then call `p.then()` with no `onRejected` handler; V8 substitutes its internal Thrower, which re-throws the raw host rejection value into a resolve/reject closure captured by the attacker. This delivers an unsanitized, fully functional bridge proxy of the host object to sandboxed code, bypassing handleException and hostPromiseSanitizeReject. If the rejection value is host-pivotable (for example a host `process` object), this results in arbitrary code execution on the host. Fixed in 3.12.1.

### 6. CVE-2026-93019｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:04.480)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:04.480 / 2026-09-18T18:18:17.967
- **官方描述（原文）**：Imager versions before 1.036 for Perl exit the process reading a TGA with a colour map length of 32768 or more in tga_palette_read. The reader unpacks the two-byte colour map length into a signed short, so a length of 32768 or more becomes negative. tga_palette_read() casts that value to size_t and asks mymalloc() for a size near SIZE_MAX. The allocation fails and Imager's allocator calls exit(3). Reading an attacker-supplied file through Imager->read() triggers an uncatchable exit.

### 7. CVE-2026-92701｜ultravioletrs / cocos
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:18:16.103)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:18:16.103 / 2026-09-18T20:17:30.040
- **官方描述（原文）**：trusted execution environments. In versions up to and including 0.8.2, the intra-handshake attested TLS (aTLS) Intel TDX verification path does not copy the expected current-session freshness value into the TDX quote-body policy before quote validation, so structurally valid TDX QuoteV4 Evidence is accepted without checking that its REPORT_DATA field matches the reportData expected for the current session. A relying party using this path can therefore accept Evidence with a mismatched or reused reportData and release application data after the handshake, enabling session-misbinding to an unintended attestation context. The issue is fixed in version 0.9.0.

### 8. CVE-2026-84383｜strukturag / libheif
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:11.707)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:11.707 / 2026-09-18T16:17:11.853
- **官方描述（原文）**：libheif is a HEIF and AVIF file format decoder and encoder. From 1.22.0 until 1.23.2, a crafted HEIF, HEIC, or AVIF item graph using nested iden and auxl references can make HeifPixelImage::transfer_channel_from_image_as() append duplicate Alpha planes with different bit depths to m_storage. HeifPixelImage::scale_nearest_neighbor() in libheif/image/pixelimage.cc allocates the destination Alpha plane using the first plane's 8-bit depth, then iterates a later 10-bit or 12-bit Alpha component and writes uint16_t samples into the same 8-bit allocation. The output geometry controls the overflow extent and the encoded sample values control the data written, allowing a remote file processed by heif_decode_image() to cause a heap out-of-bounds write. This issue is fixed in version 1.23.2.

### 9. CVE-2026-63647｜1Panel-dev / CordysCRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:20.773)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:20.773 / 2026-09-18T21:17:04.883
- **官方描述（原文）**：CordysCRM is an open source AI-powered customer relationship management system that supports private deployment. Prior to 1.7.2, SseController exposes the anonymous /sse/subscribe, /sse/broadcast, and /sse/close endpoints because ShiroFilter.addPublicPathFilters permits the SSE paths, and the endpoints trust the caller-controlled userId instead of deriving an identity from an authenticated principal. An unauthenticated caller can use /sse/subscribe to read another user's workflow events, approval requests, mentions, and alerts, use /sse/broadcast to inject SYSTEM_HEARTBEAT messages into another user's stream, or use /sse/close to terminate another user's channel. This vulnerability is fixed in 1.7.2.

### 10. CVE-2026-59163｜AxDSan / mnemosyne
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:17:07.807)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:17:07.807 / 2026-09-18T18:17:07.807
- **官方描述（原文）**：Mnemosyne is a memory layer for artificial intelligence agents. Prior to v3.10.1, the auth check in mnemosyne/core/sync_server.py parsed the JWT's header and payload using base64 decoding, then passed the token to a jwt library call with options that effectively disabled signature verification. The server accepted any well-formed token regardless of the signature, including tokens with alg: none and tokens signed with the wrong key. The fix in v3.10.1 replaces the broken decode with a from-scratch HS256 verifier using only the Python standard library. For users who cannot upgrade immediately, restrict network access to the sync server endpoint to trusted clients only. Firewall, reverse proxy with mTLS, or localhost bind with SSH tunnel are all viable. The vulnerability is not exploitable against an unreachable endpoint.

### 11. CVE-2026-93838｜sgl-project / sglang
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:33.900)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:33.900 / 2026-09-18T21:18:48.890
- **官方描述（原文）**：SGLang versions through 0.5.20 contain an unbounded memory allocation vulnerability in handle_staging_req() that fails to validate chunk_idx from ZMQ STAGING_REQ frames in prefill/decode disaggregation deployments. Attackers with access to the decode engine's internal ZMQ rank port can send a frame with an extremely large chunk_idx value, causing the scheduler to allocate memory until the system runs out and terminates the process.

### 12. CVE-2026-93753｜TehShrike / deepmerge
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:18:34.487)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:18:34.487 / 2026-09-18T20:17:33.767
- **官方描述（原文）**：deepmerge through 4.3.1 contains a prototype poisoning vulnerability in the mergeObject() function that fails to properly validate keys being written to target objects. Attackers can supply malicious source objects in merge operations to inject attacker-controlled properties into the returned object's prototype, causing applications to inherit unintended values when accessing properties without own-property checks.

### 13. CVE-2026-93752｜NV / CSSOM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:18:34.320)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:18:34.320 / 2026-09-18T20:17:33.640
- **官方描述（原文）**：CSSOM through 0.5.0 contains a denial of service vulnerability in CSSStyleDeclaration.setProperty() that fails to validate reserved property names. Attackers can supply a stylesheet with a declaration named length to replace the internal counter and trigger excessive memory allocation during cssText serialization, causing process termination.

### 14. CVE-2026-93750｜kornelski / http-cache-semantics
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:18:33.633)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:18:33.633 / 2026-09-18T18:18:33.633
- **官方描述（原文）**：http-cache-semantics through 4.2.0 contains a cache validation vulnerability in the _varyMatches() function that fails to properly validate Vary header wildcards due to byte-for-byte string comparison. Attackers can request URLs previously fetched by other clients to receive cached responses intended for different users, disclosing sensitive information across clients.

### 15. CVE-2026-93748｜kornelski / http-cache-semantics
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:18:33.330)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:18:33.330 / 2026-09-18T20:17:33.510
- **官方描述（原文）**：http-cache-semantics through 4.2.0 fails to properly validate security-zeroed cache entries when processing client max-stale directives, allowing unauthenticated attackers to retrieve cached responses belonging to other users. Attackers can request the same URL with a large max-stale value to obtain another user's Set-Cookie session credentials from shared-cache entries that were deliberately zeroed for security reasons.

### 16. CVE-2026-93690｜garycourt / uri-js
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:16.000)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:16.000 / 2026-09-18T20:17:33.377
- **官方描述（原文）**：uri-js through 4.4.1 contains a denial of service vulnerability in the removeDotSegments function that loops infinitely when a path segment begins with Unicode line or paragraph separators. Attackers can trigger this by calling removeDotSegments directly or through normalize/resolve functions with IRI handling enabled, causing the Node.js event loop to block indefinitely until heap exhaustion.

### 17. CVE-2026-93687｜micromatch / braces
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:15.507)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:15.507 / 2026-09-18T17:17:07.183
- **官方描述（原文）**：braces through 3.0.3 contains a stack overflow vulnerability in the recursive AST walkers that lack depth guards. Attackers can supply deeply nested brace patterns under the character limit to exhaust the call stack and terminate the Node.js process with an uncaught RangeError.

### 18. CVE-2026-93658｜uutils / coreutils
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T15:17:22.360)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T15:17:22.360 / 2026-09-18T17:17:07.043
- **官方描述（原文）**：uutils coreutils versions before 0.10.0 apply setuid or setgid mode to install destinations before finalizing ownership changes, allowing privileged users to leave setuid executables owned by the privileged invoker when ownership changes fail. Attackers can execute leftover setuid files with elevated privileges when ownership change operations fail on capability-restricted systems.

### 19. CVE-2026-93599｜rustls / webpki
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:11.410)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:11.410 / 2026-09-18T15:17:21.760
- **官方描述（原文）**：rustls-webpki through 0.103.12 (and 0.104.0-alpha releases before 0.104.0-alpha.7) contains a reachable panic in bit_string_flags() in src/der.rs. The input guard fails to reject a named-bit BIT STRING whose content is exactly [0x00] (zero padding bits and no data bytes), so raw_bits.len() - 1 underflows on the empty slice and the subsequent index operation panics (subtract-with-overflow in debug, index-out-of-bounds in release). The condition is reachable through the public API BorrowedCertRevocationList::from_der() when a CRL contains an issuingDistributionPoint extension with such an onlySomeReasons value. Exploitation requires an application that explicitly opts in to CRL revocation checking by passing RevocationOptions to verify_for_usage() and that parses CRL bytes obtained from a source the attacker can influence; the default rustls configuration, which does not use RevocationOptions, is unaffected. A crafted CRL causes a denial of service via the panic. Fixed in 0.103.13 and 0.104.0-alpha.7.

### 20. CVE-2026-93594｜ArcadeData / arcadedb
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:10.587)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:10.587 / 2026-09-18T15:17:21.587
- **官方描述（原文）**：ArcadeDB (Maven artifact com.arcadedb:arcadedb-engine) through 26.8.1 enforces its per-type/per-record access-control rules only in LocalBucket, keyed on file id. Query-execution paths that reach record data through LSM index files or the TimeSeries engine never invoke that permission check, so an authenticated user who is denied readRecord/deleteRecord on a type can still, with a single ordinary SQL statement, read the type's indexed key values and record IDs (e.g. SELECT key, rid FROM INDEX:Type[field]), read MAX/MIN values via the index shortcut, read and count TimeSeries samples, learn the type's record count, and delete index entries (DELETE FROM INDEX:Type[field]), which desynchronizes the index from the data and can defeat unique constraints. Index and type names needed for exploitation are discoverable because SELECT FROM schema:indexes is unfiltered. The issue affects both embedded and server deployments and all transports (HTTP, Bolt, Postgres, Gremlin) once a principal is bound. Fixed in 26.9.1.

### 21. CVE-2026-93592｜vllm-project / vllm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:10.267)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:10.267 / 2026-09-18T18:18:28.510
- **官方描述（原文）**：vLLM versions before 0.28.0 fail to validate the lower bound of token IDs in the /v1/embeddings and /pooling endpoints, allowing unauthenticated attackers to crash the engine by submitting negative token IDs. A single request with a negative token ID triggers a CUDA device-side assertion that poisons the GPU context, causing all subsequent requests to fail until the process restarts.

### 22. CVE-2026-93591｜siyuan-note / siyuan
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:10.097)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:10.097 / 2026-09-18T20:17:33.037
- **官方描述（原文）**：SiYuan versions before 3.8.3 contain an SQL injection vulnerability in the graph.go query2Stmt function where tag values are concatenated raw into SQL string literals without escaping single quotes. A publish-mode reader or anonymous visitor can inject SQL via inline HTML span tags in the getGraph endpoint to execute arbitrary queries on the read-write database and exfiltrate private data across notebooks.

### 23. CVE-2026-93558｜Red Hat / Red Hat AMQ Broker 7
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T15:17:19.590)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T15:17:19.590 / 2026-09-18T21:18:46.593
- **官方描述（原文）**：A flaw was found in Netty's WebSocketServerExtensionHandler. A remote, unauthenticated attacker can exploit this vulnerability by using HTTP/1.1 pipelining to send requests faster than the application can respond. This leads to an unbounded growth of a per-connection queue, consuming excessive memory. Eventually, this can cause the Java Virtual Machine (JVM) to exhaust its heap, resulting in a Denial of Service (DoS) for the affected server.

### 24. CVE-2026-89059｜Red Hat / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T08:17:01.783)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T08:17:01.783 / 2026-09-18T19:06:08.407
- **官方描述（原文）**：A flaw was found in RESTEasy's IIOImageProvider, which decodes attacker-supplied image request bodies without enforcing any limit on the declared image dimensions or pixel count. A remote, unauthenticated attacker can send a small crafted image declaring enormous dimensions to trigger a very large memory allocation, exhausting the JVM heap and resulting in a denial of service.

### 25. CVE-2026-89058｜Red Hat / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T08:17:01.653)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T08:17:01.653 / 2026-09-18T19:06:08.407
- **官方描述（原文）**：A flaw was found in RESTEasy's CorsFilter, which, when configured to allow all origins ("*"), reflects the request's Origin header back in the Access-Control-Allow-Origin response together with Access-Control-Allow-Credentials: true. This permissive cross-origin policy allows a malicious website to make credentialed cross-origin requests and read authenticated responses from a victim's session, resulting in a loss of confidentiality.

### 26. CVE-2026-88622｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:02.480)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:02.480 / 2026-09-18T15:17:17.453
- **官方描述（原文）**：NUUO Network Video Recorder 2.0.0 is vulnerable to Command Injection in handle_import_privilege.php.

### 27. CVE-2026-84447｜strukturag / libheif
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:12.677)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:12.677 / 2026-09-18T18:17:17.017
- **官方描述（原文）**：libheif is a HEIF and AVIF file format decoder and encoder. In 1.23.1 and earlier, crafted grid, iovl, and iden reference graphs can repeatedly decode the same base image because processed_ids is copied per branch and ImageItem::decode_image() has no shared operation budget. This vulnerability is fixed in 1.23.2.

### 28. CVE-2026-84384｜strukturag / libheif
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:11.900)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:11.900 / 2026-09-18T18:17:16.907
- **官方描述（原文）**：libheif is a HEIF and AVIF file format decoder and encoder. From 1.19.0 until 1.23.2, crafted HEIF or AVIF mime metadata and unci image data can cause decompress_brotli() and do_inflate() to grow accumulated output without an effective size limit or MemoryHandle accounting. The brotli path has no output bound, while the zlib path checks only a small temporary buffer in a branch that valid streams do not reach, and overlapping icef units can decompress the same payload repeatedly. HeifContext::interpret_heif_file_images() processes multiple compressed metadata items during file opening, allowing a small file to consume unbounded memory and terminate the process. This issue is fixed in version 1.23.2.

### 29. CVE-2026-81505｜frain-dev / convoy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:17:02.103)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:17:02.103 / 2026-09-18T18:17:16.290
- **官方描述（原文）**：Convoy is a cloud native webhooks gateway. Prior to 26.6.8, Convoy's GET /api/v1/projects/{projectID}/sources/{sourceID} endpoint authorizes access to the project in the URL, but Handler.GetSource calls sources.Service.FindSourceByID() and fetches the Source only by sourceID without confirming that its ProjectID matches the authorized project. An authenticated user or project-scoped API key holder can substitute another tenant's Source identifier and receive that Source's complete record, including unredacted AMQP, Kafka, SQS, or Google PubSub credentials. The list endpoint remains project-scoped; the single-item Source lookup is affected. This issue is fixed in version 26.6.8.

### 30. CVE-2026-77301｜cthackers / adm-zip
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:17:00.507)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:17:00.507 / 2026-09-18T18:17:14.163
- **官方描述（原文）**：adm-zip is a JavaScript library for creating and extracting ZIP archives in Node.js. Prior to 0.6.1, getData() in zipEntry.js trusts an entry's central-directory uncompressed size and allocates output memory before validating that value against the actual compressed data and decompression result. A small crafted ZIP can declare a multi-gigabyte uncompressed size, causing Buffer.alloc and decompression handling to commit excessive resident memory before CRC validation reports an error. Applications that read entries from untrusted archives can therefore be terminated by the operating system or suffer service-wide memory exhaustion. This issue is fixed in version 0.6.1.

### 31. CVE-2026-7006｜Sublime HQ Pty Ltd / Sublime Text 4
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:09.940)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.0 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:09.940 / 2026-09-18T17:17:01.830
- **官方描述（原文）**：Sublime Text for Windows through Build 4192 (Sublime Text 4) and Build 3207 (Sublime Text 3) contains a local privilege escalation vulnerability that allows unprivileged local attackers to execute arbitrary code with elevated privileges by abusing the update staging mechanism. Attackers can place a malicious DLL in the user-writable staging directory under %LOCALAPPDATA%, mark it read-only to bypass cleanup, and have the elevated installer copy it into the protected installation directory, causing the DLL to execute in the context of any higher-privileged user who subsequently launches the application.

### 32. CVE-2026-63419｜AcademySoftwareFoundation / OpenImageIO
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:07.687)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:07.687 / 2026-09-18T18:17:10.357
- **官方描述（原文）**：OpenImageIO is a toolset for reading, writing, and manipulating image files of any image file format relevant to VFX / animation. Prior to 3.0.21.0, 3.1.16.0, and 3.2.0.3-beta1, A zbuffer-only tiled iff is exposed with a 16-bit public imagespec while the decoder retains a 32-bit internal pixel size. iffinput::read_native_tile() copies according to m_header.pixel_bytes() rather than imagespec::tile_bytes(true), and a failed read can leave m_buf nonempty so a later call copies partially initialized data into the undersized caller buffer, resulting in a heap out-of-bounds write and memory corruption. The affected implementation is identified by src/iff.imageio/iffinput.cpp, IffInput::read_native_tile(), ImageSpec::tile_bytes(true), m_header.pixel_bytes(), ZBUFFER, and m_buf, which define the relevant source path, functions, state, and trigger. This issue is fixed in versions 3.0.21.0, 3.1.16.0, and 3.2.0.3-beta1.

### 33. CVE-2026-58197｜stacklok / toolhive
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:16:57.880)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:16:57.880 / 2026-09-18T17:16:57.880
- **官方描述（原文）**：ToolHive is a utility designed to simplify the deployment and management of Model Context Protocol servers. Prior to ToolHive CLI 0.30.1 and ToolHive Studio 0.38.0, locally run MCP server containers use the default network permission profile without network isolation, permitting access to host.docker.internal while ToolHive API and MCP proxy endpoints are reachable without authentication. A malicious or compromised MCP server can use the Docker gateway to contact host-local services, other ToolHive-managed MCP proxies, or the ToolHive control plane without escaping the container. This access can expose data and logs, invoke sibling MCP tools, alter process or workload state, and disrupt services. ToolHive Studio additionally sends network_isolation as false and overrides the backend's secure isolation default. This issue is fixed in ToolHive CLI 0.30.1 and ToolHive Studio 0.38.0.

### 34. CVE-2025-61682｜SemanticMediaWiki / SemanticMediaWiki
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:03.717)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:03.717 / 2026-09-18T18:17:04.307
- **官方描述（原文）**：Semantic MediaWiki is a free, open-source extension to MediaWiki that lets users store and query data within the wiki's pages. Versions starting in 3.1.0 and prior to 7.0.0 insert the unsanitized value of a data attribute into the DOM as HTML, allowing for stored XSS through wikitext. Version 7.0.0 patches the issue.

### 35. CVE-2017-20284｜Caucho Technology, Inc. / Resin
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:16:58.540)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:16:58.540 / 2026-09-18T20:16:58.540
- **官方描述（原文）**：Caucho Resin contains a path traversal vulnerability in the documentation webapp (resin-doc) that allows remote unauthenticated attackers to read arbitrary files by supplying a relative path through the inputFile request parameter of the jndi-appconfig tutorial servlet. Attackers can craft requests with directory traversal sequences to the servlet endpoint to read files outside the intended tutorial directory on the underlying system. Exploitation evidence was first observed by the Shadowserver Foundation on 2021-12-10.

### 36. CVE-2026-93839｜ModelTC / LightLLM
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:34.047)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:34.047 / 2026-09-18T20:17:34.047
- **官方描述（原文）**：LightLLM through 1.2.0 contains an authentication bypass vulnerability in the /pd_register WebSocket endpoint that allows unauthenticated attackers to register arbitrary nodes by supplying crafted JSON without peer address validation. Attackers can disclose full user prompts routed to their socket, trigger denial of service by replacing legitimate nodes, or make the PD Master issue requests to internal network addresses.

### 37. CVE-2026-93762｜MongoDB Inc. / Mongoid
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:18:35.053)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:18:35.053 / 2026-09-18T19:05:01.127
- **官方描述（原文）**：Mongoid contains an unsafe reflection weakness in the query path used for embedded documents. An application that passes an externally supplied field name to certain in-memory query methods may allow an unauthenticated party to obtain unintended disclosure of stored document data and to permanently remove stored records.

### 38. CVE-2026-93740｜Totolink / A3002MU
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T22:17:10.890)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T22:17:10.890 / 2026-09-18T22:17:10.890
- **官方描述（原文）**：A vulnerability was identified in Totolink A3002MU Hh-B20211125.1046. Affected is the function formWlEncrypt of the file /boafrm/formWlEncrypt. The manipulation of the argument submit-url leads to buffer overflow. It is possible to initiate the attack remotely. The exploit is publicly available and might be used.

### 39. CVE-2026-93659｜concretecms-community-store / community_store
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T15:17:22.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T15:17:22.510 / 2026-09-18T18:18:32.290
- **官方描述（原文）**：Concrete CMS Community Store before 2.7.8 renders customer-supplied order fields without HTML escaping in checkout and admin views. Unauthenticated attackers can store script payloads in billing name, email, or phone fields that execute in authenticated manager sessions to create rogue accounts or exfiltrate data.

### 40. CVE-2026-93605｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:12.340)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:12.340 / 2026-09-18T14:19:12.453
- **官方描述（原文）**：vm2 NodeVM versions before 3.12.1 contain a sandbox escape vulnerability where the DANGEROUS_BUILTINS denylist omits child_process despite blocking other host-spawning modules. Attackers can require child_process and execute arbitrary commands on the host system when NodeVM is configured with builtin:['*'] or explicit child_process allowance.

### 41. CVE-2026-93603｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:12.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:12.003 / 2026-09-18T14:19:12.123
- **官方描述（原文）**：vm2 through 3.12.0 (fixed in 3.12.1) does not correctly handle a nullish `this` receiver in the apply trap of its bridge (lib/bridge.js): when sandboxed code calls a host-provided non-strict (sloppy-mode) function without a receiver — e.g. `fn()`, a detached method, `fn.call()`, `fn.apply(undefined)`, `Reflect.apply(fn, undefined, [])`, or `fn.bind()()` — the undefined receiver is passed straight through to the host call, and V8 substitutes the host realm's global object for `this`. vm2 then wraps and returns that object to the sandbox, giving sandboxed script a live proxy of the host global. This allows a complete sandbox escape: untrusted script can reach `process` and execute arbitrary code/commands on the host (for example via `process.getBuiltinModule('child_process').execSync`). Exploitation requires that the embedding application expose at least one non-strict host function to the sandbox; strict-mode and ES module host functions are not affected.

### 42. CVE-2026-92702｜ultravioletrs / cocos
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:18:16.257)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:18:16.257 / 2026-09-18T18:18:16.257
- **官方描述（原文）**：Cocos AI is a confidential computing system for running AI workloads inside trusted execution environments. In versions up to and including 0.8.2, the intra-handshake attested TLS (aTLS) AMD SEV-SNP verification path does not enforce attestation freshness when the expected reportData value is nil, empty, or omitted, leaving the SEV-SNP policy ReportData unset so the verifier accepts unrelated or stale Evidence not bound to the current connection. A relying party that uses this path without an expected reportData as a trust or authorization decision can be induced to trust an unintended attestation context; a supplied non-empty reportData is still validated. The issue is fixed in version 0.9.0.

### 43. CVE-2026-92229｜wpmudev / Forminator Forms – Contact Form, Payment Form & Custom Form Builder
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-19T03:17:17.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-19T03:17:17.040 / 2026-09-19T03:17:17.040
- **官方描述（原文）**：The The Forminator Forms – Contact Form, Payment Form & Custom Form Builder plugin for WordPress is vulnerable to arbitrary shortcode execution in all versions up to, and including, 1.57.2. This is due to the software allowing users to execute an action that does not properly validate a value before running do_shortcode. This makes it possible for unauthenticated attackers to execute arbitrary shortcodes.

### 44. CVE-2026-89274｜brechtvds / WP Recipe Maker
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-19T03:17:16.587)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-19T03:17:16.587 / 2026-09-19T03:17:16.587
- **官方描述（原文）**：The WP Recipe Maker plugin for WordPress is vulnerable to Arbitrary Shortcode Execution in all versions up to, and including, 10.8.1. The vulnerability exists because `WPRM_Metadata::sanitize_metadata()` recursively calls `do_shortcode()` on every scalar field of the recipe's structured metadata array — including the `reviewBody` field, which is populated verbatim from the `comment_content` of approved `wprm-comment-rating` comments — without sanitizing or stripping shortcode tokens before execution; the subsequent `wp_strip_all_tags()` and `strip_shortcodes()` calls operate only on the output string after execution has already fully occurred, providing no protection against server-side shortcode invocation. This makes it possible for unauthenticated attackers to execute arbitrary registered WordPress shortcodes server-side on every recipe page render, causing shortcode output — such as attachment captions, private post fields, or other data exposed by installed shortcodes — to be embedded in the page's JSON-LD `reviewBody` metadata and disclosed to all visitors who load the recipe page. Successful exploitation requires the attacker's rated comment to pass the site's comment approval threshold, either via auto-approval or moderator action, before the injected shortcode begins executing on page loads.

### 45. CVE-2026-85497｜CareCam / HMT.CM2507 Firmware
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:17:04.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:17:04.790 / 2026-09-18T19:03:28.367
- **官方描述（原文）**：CareCam CM2507 IP cameras store the device's root-account password using a fixed legacy password hash that provides insufficient resistance to offline cracking. An attacker who obtains the firmware image or password database could recover the associated credential, which may also be reusable across other devices running the same firmware.

### 46. CVE-2026-84738｜Unknown / AF Companion
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T06:16:39.307)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00224 / percentile=0.13302
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T06:16:39.307 / 2026-09-18T19:08:32.830
- **官方描述（原文）**：The AF Companion WordPress plugin before 2.2.0 does not validate the type of files uploaded through one of its import features, allowing users with a low-privileged store-management role to upload arbitrary files, including PHP ones, leading to Remote Code Execution.

### 47. CVE-2026-84434｜Gravity Forms / Gravity Forms
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-19T03:17:15.573)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-19T03:17:15.573 / 2026-09-19T03:17:15.573
- **官方描述（原文）**：The Gravity Forms plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and including, 3.1.0.4 via the upload_file function. This is due to a mismatch between the field validation pipeline and the file persistence pipeline, where hidden file upload fields bypass extension validation and a rejected file's intact upload state is later passed to upload_file() without re-validation. This makes it possible for unauthenticated attackers to upload files that may be executable, which makes remote code execution possible. Exploitation requires the targeted form to contain a File Upload field with its Visibility set to 'Hidden'; the vulnerability is reachable by unauthenticated attackers on any publicly accessible form meeting this condition.

### 48. CVE-2026-84082｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:27.743)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:27.743 / 2026-09-18T20:17:27.743
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 could allow a remote attacker to execute arbitrary SQL commands due to improper neutralization of special elements used in an SQL command.

### 49. CVE-2026-84078｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:27.480)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:27.480 / 2026-09-18T20:17:27.480
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is vulnerable to a missing authentication vulnerability in the LoadBalancerServlet. An unauthenticated user can access privileged load-balancer operations, potentially resulting in unauthorized actions and impact to the integrity and availability of the affected system.

### 50. CVE-2026-84075｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:27.103)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:27.103 / 2026-09-18T20:17:27.103
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 could allow a remote attacker to bypass security restrictions due to missing authentication for the ChangeTrackerServlet.

### 51. CVE-2026-84073｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:26.830)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:26.830 / 2026-09-18T20:17:26.830
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary SQL commands due to improper neutralization of special elements used in an SQL command.

### 52. CVE-2026-84064｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:26.440)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:26.440 / 2026-09-18T20:17:26.440
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary SQL commands due to improper neutralization of special elements used in an SQL command.

### 53. CVE-2026-84031｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:26.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:26.060 / 2026-09-18T21:18:44.080
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary code due to improper neutralization of input during web page generation.

### 54. CVE-2026-82967｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:25.513)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:25.513 / 2026-09-18T20:17:25.513
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is vulnerable to an authentication bypass that allows an unauthenticated remote attacker to bypass IP-based access controls and access the Guardium management interface.

### 55. CVE-2026-82832｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:24.643)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:24.643 / 2026-09-18T20:17:24.643
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 could allow a remote authenticated attacker to execute arbitrary code due to improper neutralization of input during web page generation.

### 56. CVE-2026-82340｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:24.517)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:24.517 / 2026-09-18T20:17:24.517
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is vulnerable to unauthenticated insecure deserialization and attacker-controlled reflective method dispatch in the Change Audit System (CAS) listener. A network attacker able to reach TCP port 16017 may submit crafted serialized messages and potentially cause unintended code execution in the Guardium appliance.

### 57. CVE-2026-81657｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:23.997)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:23.997 / 2026-09-18T20:17:23.997
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 could allow a remote unauthenticated attacker to execute arbitrary code on the system due to the deserialization of untrusted data.

### 58. CVE-2026-81321｜CareCam / HMT.CM2507 Firmware
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:17:01.953)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:17:01.953 / 2026-09-18T19:03:28.367
- **官方描述（原文）**：CM2507 IP cameras store configured wireless network credentials in cleartext within the device filesystem. An attacker who obtains filesystem access through physical access, a debugging interface, or another vulnerability could recover the configured network identifier and pre-shared key.

### 59. CVE-2026-80442｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:23.343)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:23.343 / 2026-09-18T20:17:23.343
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is vulnerable to an authenticated OS command injection vulnerability in the exportCertificate functionality. Successful exploitation could allow an attacker to execute unauthorized commands and impact the confidentiality, integrity, and availability of the affected system.

### 60. CVE-2026-80441｜IBM / Guardium Data Protection
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:23.217)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:23.217 / 2026-09-18T20:17:23.217
- **官方描述（原文）**：IBM Guardium Data Protection 12.2 is vulnerable to an unauthenticated second-order SQL injection vulnerability in the generateInsertQuery functionality of change-tracker-data.sql. A remote attacker could inject malicious SQL that is subsequently processed by the application, potentially resulting in compromise of the confidentiality, integrity, and availability of the affected system.

### 61. CVE-2026-77240｜ArnasDon / wacrm
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:17:00.360)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:17:00.360 / 2026-09-18T17:17:00.360
- **官方描述（原文）**：WACRM is a self-hostable CRM template for WhatsApp. In version 0.7.0 and earlier, the profiles_update row-level security policy in supabase/migrations/017_account_sharing.sql permits authenticated users to modify their own account_role and account_id, allowing a viewer to self-promote or move into another tenant and then access or modify tenant resources. Separately, match_ai_knowledge_fts and match_ai_knowledge_semantic in supabase/migrations/030_ai_knowledge.sql run as SECURITY DEFINER, accept a caller-controlled p_account_id, and omit an is_account_member check, allowing an authenticated non-member to read another tenant's knowledge-base chunks. This vulnerability is fixed with commit e01f7ed37184f972ace8fb2da5c3e37e56a6050f.

### 62. CVE-2026-75885｜Red Hat / Red Hat OpenShift Container Platform 4
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T22:17:10.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T22:17:10.313 / 2026-09-18T22:17:10.313
- **官方描述（原文）**：A flaw was found in the OpenShift console. Unauthenticated access to the `/api/devfile/` and `/api/devfile/samples/` endpoints allows a remote attacker to send crafted devfile payloads. This can lead to Server-Side Request Forgery (SSRF), where the console pod makes requests to internal services and reflects partial responses to the attacker. Additionally, by sending repeated large requests without a specified content length, an attacker can cause unbounded memory growth, leading to a Denial of Service (DoS).

### 63. CVE-2026-75878｜IBM / Sterling File Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:21.363)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:21.363 / 2026-09-18T20:17:21.363
- **官方描述（原文）**：IBM Sterling File Gateway could allow a remote attacker to bypass authentication and obtain a fully authenticated session due to improper authentication via an unvalidated SSO header.

### 64. CVE-2026-75031｜Interchange / Interchange
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:09.043)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:09.043 / 2026-09-18T19:06:08.407
- **官方描述（原文）**：In the interchange/interchange project, a critical remote code execution (RCE) vulnerability was found in the “quick question” admin feature. In default installations arbitrary Perl code can be injected and executed server-side by unauthenticated users. The Perl code normally runs within a Safe container which limits the scope of what it can do, unless the non-default AllowGlobal directive is configured for the catalog being accessed.CTOR]

### 65. CVE-2026-67101｜HCL Software / HCL BigFix Service Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T08:17:00.740)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：0.00268 / percentile=0.19258
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T08:17:00.740 / 2026-09-18T13:44:57.517
- **官方描述（原文）**：HCL BigFix Service Management is affected by a Server-Side Request Forgery (SSRF) vulnerability in its search functionality, which could allow an attacker to force the application server to send requests to internal systems that are not accessible from the internet.

### 66. CVE-2026-67100｜HCL Software / HCL BigFix Service Management
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T08:17:00.603)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00353 / percentile=0.28953
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T08:17:00.603 / 2026-09-18T18:17:11.110
- **官方描述（原文）**：HCL BigFix Service Management is affected by SQL Injection flaw and a Cross-Tenant Data Exposure flaw vulnerabilities. which could allow an authenticated attacker to inject database commands to extract sensitive system details, as well as manipulate request values to gain unauthorized access to full personal profile data and PII across different organizations.

### 67. CVE-2026-61781｜pgpartman / pg_partman
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:19.003)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:19.003 / 2026-09-18T21:17:02.257
- **官方描述（原文）**：pg_partman is a PostgreSQL extension that manages partitioned tables by time or ID. Prior to 5.5.0, create_partition_time() reads the writable part_config.time_encoder text value and interpolates it without identifier quoting into a dynamically executed SELECT statement. A role with the documented partman_user INSERT and UPDATE privileges can store SQL rather than a function name. When pg_partman_bgw later creates a child partition for a text- or UUID-keyed set, the worker executes the stored SQL with pg_partman_bgw.role privileges, which default to PostgreSQL superuser. The persistent configuration row can repeatedly restore elevated access on later maintenance ticks, and successful exploitation can permit database-wide compromise and operating-system command execution as the PostgreSQL service account. This issue is fixed in version 5.5.0.

### 68. CVE-2026-61682｜kcp-dev / kcp
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:07.523)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:07.523 / 2026-09-18T16:17:07.523
- **官方描述（原文）**：kcp is a Kubernetes-like control plane for form-factors and use-cases beyond Kubernetes and container workloads. Prior to 0.31.4 and 0.32.2, the kcp front-proxy does not remove inbound X-Remote-User, X-Remote-Group, or X-Remote-Extra-* identity headers before forwarding requests to shards. Any authenticated tenant can inject X-Remote-Group: system:masters, authorization.kcp.io/warrant, authentication.kcp.io/scopes, or a group used for per-workspace required-group gating, and the shard trusts these values as authenticated identity assertions. This allows cross-workspace impersonation, authorization bypass, and arbitrary reading, writing, or deletion of resources, secrets, RBAC data, APIExports, APIBindings, and LogicalClusters. This issue is fixed in versions 0.31.4 and 0.32.2.

### 69. CVE-2026-61550｜Icinga / icinga2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:17:08.217)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:17:08.217 / 2026-09-18T18:17:08.217
- **官方描述（原文）**：Icinga 2 is an open source monitoring system. From 2.8 until 2.14.9, 2.15.4, and 2.16.2, certificate update JSON-RPC message handling does not validate that the sender is a trusted endpoint. An unauthenticated network attacker able to connect to TCP port 5665 can replace the node certificate and trusted CA certificate, impersonate a trusted node, and take control of the node. This issue is fixed in versions 2.14.9, 2.15.4, and 2.16.2.

### 70. CVE-2026-58264｜FluidSynth / fluidsynth
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:18.107)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:18.107 / 2026-09-18T20:17:18.107
- **官方描述（原文）**：FluidSynth is a software synthesizer based on the SoundFont 2 specifications. From 1.1.2 until 2.5.6, the FluidSynth command handler accepts a pitch_bend_range command whose channel argument is not bounds checked before the supplied value is written through the selected synth channel. An out-of-range channel can therefore cause an out-of-bounds heap write, leading to denial of service or possible code execution. The issue is remotely reachable when the TCP server is enabled through new_fluid_server() or fluidsynth -s, and it is locally reachable through malicious commands delivered to the FluidSynth shell on standard input. Applications that do not use the shell, command handler, or TCP server are not affected. This issue is fixed in version 2.5.6.

### 71. CVE-2026-28198｜Cohesity / NetBackup Flex OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T12:17:24.717)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T12:17:24.717 / 2026-09-18T19:24:36.593
- **官方描述（原文）**：An authenticated, low-privileged user with access to the NetBackup Flex OS management shell could bypass the cryptographic signature verification step of a privileged support command by supplying a specially formed access credential. Successful exploitation grants the attacker an unrestricted root shell with full control over the Flex appliance host and all hosted containers, completely compromising confidentiality, integrity, and availability.

### 72. CVE-2026-28197｜Cohesity / NetBackup Flex OS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T12:17:24.573)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T12:17:24.573 / 2026-09-18T19:24:36.593
- **官方描述（原文）**：An authenticated, low-privileged user with access to the NetBackup Flex OS management shell could supply a specially crafted input to a privileged administrative command, causing it to execute arbitrary code with root-level permissions. Successful exploitation grants the attacker unrestricted control over the Flex appliance host and all hosted containers, fully compromising confidentiality, integrity, and availability.

### 73. CVE-2026-13684｜Synology / DiskStation Manager (DSM)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T09:16:39.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00455 / percentile=0.38816
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T09:16:39.237 / 2026-09-18T20:17:08.373
- **官方描述（原文）**：An improper encoding or escaping of output vulnerability in SCGI in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2-72806-9, 7.3.2-86009-4 and 7.4-90075 allows remote attackers to read or write arbitrary files and conduct denial-of-service attacks.

### 74. CVE-2026-13639｜Synology / DiskStation Manager (DSM)
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T09:16:38.757)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00505 / percentile=0.42152
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T09:16:38.757 / 2026-09-18T20:17:06.860
- **官方描述（原文）**：An insufficient entropy vulnerability in login logic in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2-72806-9, 7.3.2-86009-4 and 7.4-90075 allows remote attackers to read or write arbitrary files and conduct denial-of-service attacks.

### 75. CVE-2026-10858｜IBM / MQ for HPE NonStop
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:05.310)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:05.310 / 2026-09-19T04:17:51.203
- **官方描述（原文）**：IBM MQ for HPE NonStop 8.1.0 through 8.1.0.40 could allow an authenticated attacker to cause a denial of service or potentially execute arbitrary code due to a heap buffer underflow when processing multi-segment messages.

### 76. CVE-2026-10747｜IBM / MQ Appliance
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:04.413)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:04.413 / 2026-09-19T04:17:50.817
- **官方描述（原文）**：IBM MQ Appliance could allow a remote attacker to cause a denial of service or potentially execute arbitrary code due to a heap buffer overflow in protocol message processing before authentication.

### 77. CVE-2025-66455｜InternLM / lmdeploy
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:17:04.420)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:17:04.420 / 2026-09-18T20:17:00.043
- **官方描述（原文）**：LMDeploy is a toolkit for compressing, deploying, and serving large language models. Starting in version 0.9.2 and prior to version 0.16.0, LMDeploy's PyTorch DistServe/PD-disaggregation control plane used `recv_pyobj()` to deserialize messages received through a ZeroMQ PULL socket. PyZMQ implements `recv_pyobj()` using Python pickle deserialization, which can execute arbitrary code while reconstructing an object. The peer address used by the receiver was supplied through the `POST /distserve/p2p_connect` HTTP endpoint. An attacker who could reach an affected DistServe API server could cause the server to connect to an attacker-controlled ZeroMQ endpoint and deserialize a crafted pickle payload. API-key authentication is not enabled unless the operator explicitly configures it. As a result, affected DistServe deployments without API keys allowed unauthenticated remote code execution with the privileges of the LMDeploy serving process. This issue affects the PyTorch backend when PD-disaggregation/DistServe is enabled. Ordinary deployments that do not use the affected disaggregated-serving path do not expose this data flow. The fix was released in LMDeploy 0.16.0. Users who cannot upgrade immediately should prevent untrusted clients from reaching `/distserve/*` endpoints, restrict the DistServe HTTP and ZeroMQ control planes to trusted cluster networks, configure API-key authentication, and block arbitrary outbound ZeroMQ connections from serving nodes. These measures reduce exposure but do not make pickle deserialization safe.

### 78. CVE-2025-53837｜xwiki / xwiki-rendering
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:03.527)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:03.527 / 2026-09-18T16:17:03.527
- **官方描述（原文）**：XWiki Rendering is a generic rendering system that converts textual input in a given syntax (wiki syntax, HTML, etc) into another syntax (XHTML, etc). Prior to versions 14.10.2 and 15.0 RC1, any user who can edit their own user profile or any other document can execute arbitrary script macros including Groovy and Python macros that allow remote code execution including unrestricted read and write access to all wiki contents. The reason is that rendering output is included as content of HTML macros without further escaping and it is thus possible to close the HTML macro and inject script macros that are executed with programming rights. This has been patched in XWiki 14.10.2 and 15.0 RC1 by making sure that rendering output cannot close the surrounding HTML macro. A possible workaround is available. It is, in principle, possible to add escaping to all places where rendering output is used in wiki documents, but at the moment there is no list of them.

### 79. CVE-2025-15399｜IBM / Common Licensing
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:02.387)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:02.387 / 2026-09-19T04:17:32.617
- **官方描述（原文）**：IBM Common Licensing Agent 9.0, Agent 9.0.0.1, Agent 9.0.0.2, ART 9.0, ART 9.0.0.1, and ART 9.0.0.2 is vulnerable to cross-site request forgery which could allow an attacker to execute malicious and unauthorized actions transmitted from a user that the website trusts.

### 80. CVE-2023-5778｜ABB / Freelance Controller DCP
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:17:14.870)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:17:14.870 / 2026-09-18T17:49:08.457
- **官方描述（原文）**：Improper handling of length parameter inconsistency vulnerability in ABB Freelance Controller DCP, ABB Freelance Controller AC700, ABB Freelance Controller AC800, and ABB Freelance Controller AC900. This issue affects Freelance Controller DCP: through 2013, 2013 SP1, 2016, 2016 SP1, 2019, and 2019 SP1; Freelance Controller AC700: through 2013, 2013 SP1, 2016, 2016 SP1, 2019, and 2019 SP1; Freelance Controller AC800: through 2013, 2013 SP1, 2016, 2016 SP1, 2019, and 2019 SP1; Freelance Controller AC900: through 2013, 2013 SP1, 2016, 2016 SP1, 2019, and 2019 SP1.

### 81. CVE-2023-54399｜Hongjing / e-HR
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T19:16:40.757)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T19:16:40.757 / 2026-09-18T19:16:40.757
- **官方描述（原文）**：Hongjing e-HR before 8.2 contains a SQL injection vulnerability in the /servlet/codesettree endpoint where the categories query parameter is passed to a database query without sanitization after HRMS-encoding is stripped. An unauthenticated remote attacker can supply a crafted UNION SELECT payload to read arbitrary database content, including credential tables such as operuser. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.

### 82. CVE-2026-93873｜Cotonti / Cotonti
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T20:17:35.400)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T20:17:35.400 / 2026-09-18T21:18:49.167
- **官方描述（原文）**：Cotonti through 1.0.0 fails to validate anti-CSRF tokens in the contact plugin submission handler, allowing attackers to forge messages. Attackers can auto-submit contact forms from attacker-controlled pages to send forged messages attributed to authenticated victims to the administrator inbox.

### 83. CVE-2026-93736｜mealie-recipes / mealie
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:16.170)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:16.170 / 2026-09-18T18:18:32.810
- **官方描述（原文）**：Mealie before 3.21.0 fails to validate user ownership in the ratings and favorites endpoints, allowing authenticated attackers to read any user's recipe ratings and favorites by specifying arbitrary user IDs in the URL path. Attackers can access private recipe identifiers, rating values, and favorite flags belonging to other users across different groups or households.

### 84. CVE-2026-93604｜patriksimek / vm2
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:12.167)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:12.167 / 2026-09-18T14:19:12.287
- **官方描述（原文）**：vm2 through 3.12.0 exposes Node.js's crypto.setFips() function to untrusted guest code when an embedder explicitly allowlists the crypto builtin for a NodeVM (require.builtin: ['crypto']). The builtin sanitizer (sanitizeCryptoModule in lib/builtin.js) replaces crypto.setEngine but leaves crypto.setFips callable, and the readonly wrapper used to expose the host module does not localize side effects of forwarded host functions. Guest code can therefore call crypto.setFips() to change the FIPS mode of the entire host process; the modified mode is subsequently observed by trusted host code (crypto.getFips() changed from 0 to 1 in the reported test), crossing the NodeVM isolation boundary. Fixed in vm2 3.12.1.

### 85. CVE-2026-93597｜ArcadeData / arcadedb
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:11.083)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:11.083 / 2026-09-18T18:18:29.630
- **官方描述（原文）**：ArcadeDB versions before 26.9.1 fail to validate IPv6 transition addresses in the SSRF guard used by IMPORT DATABASE and server commands. Authenticated attackers can supply URLs resolving to NAT64, 6to4, or Teredo addresses embedding RFC 1918 or loopback IPv4 payloads to reach internal services and cloud metadata endpoints.

### 86. CVE-2026-93596｜ArcadeData / arcadedb
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:19:10.917)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:19:10.917 / 2026-09-18T18:18:29.093
- **官方描述（原文）**：ArcadeDB before 26.9.1 (com.arcadedb:arcadedb-engine <= 26.8.1) fails to bind the authenticated principal onto the DatabaseAsyncTransaction async worker threads used by the parallel edge-connect phase of POST /api/v1/batch/{database}. Because those workers have no current user, LocalDatabase.checkPermissionsOnFile returns early and allows the write, bypassing per-type CREATE_RECORD/UPDATE_RECORD ACL enforcement. In deployments that rely on per-type or per-group ACLs, an authenticated low-privilege user holding CREATE_RECORD on an edge type E but with CREATE_RECORD/UPDATE_RECORD revoked on a vertex type V can submit a graph edge-load batch request (with parallelFlush at its default value of true) and durably append edges to protected vertices of type V by writing records into V's <V>_out_edges/<V>_in_edges buckets, resulting in unauthorized modification of graph adjacency. Setting parallelFlush=false causes the request to be correctly rejected. This is an incomplete fix of GHSA-c23x-pqcj-7hfm, which bound the principal only on the HTTP handler thread.

### 87. CVE-2026-93578｜Red Hat / Red Hat build of Apache Camel for Spring Boot 4
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T11:17:22.170)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T11:17:22.170 / 2026-09-18T19:06:08.407
- **官方描述（原文）**：A flaw was found in Netty's Online Certificate Status Protocol (OCSP) Client. The client fails to verify the 'id-kp-OCSPSigning' Extended Key Usage (EKU) in OCSP responder certificates. A remote attacker, holding any valid certificate issued by the same Certificate Authority (CA), can exploit this by forging 'GOOD' OCSP responses for revoked certificates. This bypasses certificate revocation checks, allowing applications using Netty's OCSP Client to accept certificates that should have been revoked, leading to an authorization bypass.

### 88. CVE-2026-93534｜spatie / Scotty
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:17:06.290)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:17:06.290 / 2026-09-18T19:14:56.310
- **官方描述（原文）**：A vulnerability was identified in spatie Scotty up to 1.4.2. Affected is the function SelfUpdater::update of the file app/Updater/SelfUpdater.php of the component Self Update Handler. Such manipulation leads to download of code without integrity check. It is possible to launch the attack remotely. Upgrading to version 1.4.3 is able to address this issue. The name of the patch is 4b4e11bfc98e3a2159bb2b3d9b040293fcc44744. It is advisable to upgrade the affected component.

### 89. CVE-2026-93505｜未確認 / SveltyCMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T15:17:19.230)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T15:17:19.230 / 2026-09-18T19:14:56.310
- **官方描述（原文）**：A vulnerability was found in SveltyCMS 0.0.6. This vulnerability affects unknown code of the file src/utils/media/media-service.server.ts of the component SVG Media Upload. Performing a manipulation results in cross site scripting. The attack can be initiated remotely. The patch is named 05b4f9efeb79e9d72a693232334d7529687f896f. Applying a patch is the recommended action to fix this issue.

### 90. CVE-2026-92747｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:18:16.547)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.0 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:18:16.547 / 2026-09-18T23:16:33.163
- **官方描述（原文）**：A flaw was found in `cockpit-machines`. This vulnerability allows a local attacker with the ability to inspect running processes to expose sensitive guest virtual machine (VM) credentials, such as `rootPassword` and `userPassword`. This occurs when the `install_machine.py` script passes these credentials as a JSON command-line argument during VM creation or installation. The exposure is limited to the period when the installation workflow is active and depends on host process-visibility policies.

### 91. CVE-2026-84992｜imzbf / md-editor-v3
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:17:17.277)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:17:17.277 / 2026-09-18T18:17:17.277
- **官方描述（原文）**：md-editor-v3 is a Markdown editor for Vue 3 developed in JSX and TypeScript. Prior to 6.5.4, MdPreview's useMarkdownIt() highlight callback in packages/MdEditor/layouts/Content/composition/useMarkdownIt.ts inserts a fenced-code language value into class and language HTML attributes without escaping or consistently quoting it. Both highlighted and non-highlighted rendering paths reach this return value, while XSSPlugin filters only existing html_block and html_inline tokens before rendering and therefore cannot inspect the renderer-generated HTML. An attacker who can supply Markdown can use crafted fenced-code metadata to execute JavaScript in the application origin when a victim renders it, including as stored cross-site scripting when the host persists the Markdown. This issue is fixed in version 6.5.4

### 92. CVE-2026-81627｜Red Hat / Red Hat Enterprise Linux 10
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T11:17:18.490)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.7 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T11:17:18.490 / 2026-09-18T19:06:08.407
- **官方描述（原文）**：A flaw was found in QEMU. The VAPIC setup hypercall in hw/i386/vapic.c does not validate that the writable RAM alias remains within the option ROM window. A privileged guest user on a Q35/KVM machine can position this alias over locked SMRAM, bypassing chipset D_LCK protection and injecting code into System Management Mode memory.

### 93. CVE-2026-79294｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T14:18:48.077)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T14:18:48.077 / 2026-09-18T16:17:09.747
- **官方描述（原文）**：Cross Site Scripting vulnerability in Moonshot AI Kimi version as of 2026-07-18 allows a remote attacker to execute arbitrary code via the HTML artifact Preview rendering; public Share view component

### 94. CVE-2026-77385｜zoriya / Kyoo
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:17:14.357)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:17:14.357 / 2026-09-18T20:17:22.717
- **官方描述（原文）**：Kyoo is a self-hosted media server focused on movies, series, and anime. Prior to 5.1.0, a registered user with the core.play permission could supply a base64-encoded filesystem path to the transcoder. The path handling in transcoder/src/api/path.go cleaned the value and checked only that it began with Settings.SafePath before getHash processed it, while transcoder/src/api/streams.go served the accepted path without verifying a Kyoo catalog record. This missing catalog-level authorization allowed the user to retrieve hidden, temporary, operational, or other uncataloged files beneath the media directory when the path was known or guessed. This vulnerability is fixed in 5.1.0.

### 95. CVE-2026-77339｜F1bonacc1 / process-compose
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:17:00.663)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:17:00.663 / 2026-09-18T17:17:00.663
- **官方描述（原文）**：Process Compose is a scheduler and orchestrator for non-containerized applications. Prior to 1.120.0, the MCP SSE listener in src/mcp/server.go accepts browser-origin requests to /sse and the returned message endpoint without validating the Host header, validating the Origin header, or authenticating the caller. When MCP SSE is enabled, a malicious website can use DNS rebinding to reach the loopback listener and issue MCP requests. If expose_control_tools is enabled, the attacker can enumerate process state, read or search logs, truncate logs, and start, stop, restart, or scale local processes; configured user-defined tools can expose additional commands and output. The Gin REST API token middleware does not protect this separately started MCP listener. This issue is fixed in version 1.120.0.

### 96. CVE-2026-69186｜c-ares / c-ares
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T18:17:11.637)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T18:17:11.637 / 2026-09-18T20:17:21.143
- **官方描述（原文）**：c-ares is an asynchronous resolver library. Prior to 1.34.7, ares_dns_parse() trusts the attacker-controlled ANCOUNT, NSCOUNT, and ARCOUNT fields before confirming that the DNS response contains enough bytes for the claimed records. Because process_answer() invokes parsing before transaction ID and question validation, a malicious DNS response can cause ares_dns_record_rr_prealloc() and ares_array_set_size() to reserve disproportionate heap memory for a tiny message. Repeated responses create large allocation and release cycles that can degrade or deny name resolution, without causing memory corruption or information disclosure. This issue is fixed in version 1.34.7.

### 97. CVE-2026-65970｜AcademySoftwareFoundation / OpenImageIO
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:08.590)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:08.590 / 2026-09-18T17:16:59.900
- **官方描述（原文）**：OpenImageIO is a toolset for reading, writing, and manipulating image files of any image file format relevant to VFX / animation. Prior to 3.1.16.0, a crafted ZIP-compressed TIFF processed with TIFF multithreading enabled can make TIFFInput::read_native_scanlines() return through an error path while asynchronous strip-decompression work remains queued. Because task_set is declared before ok and compressed_scratch, those captured objects are destroyed before the task-set destructor waits, allowing worker tasks to use stale stack and heap storage, resulting in a use-after-scope crash and denial of service. The affected implementation is identified by src/tiff.imageio/tiffinput.cpp, TIFFInput::read_native_scanlines(), task_set, ok, compressed_scratch, and uncompress_one_strip(), which define the relevant source path, functions, state, and trigger. This issue is fixed in 3.1.16.0.

### 98. CVE-2026-63406｜anycable / anycable
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:16:59.620)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:16:59.620 / 2026-09-18T18:17:10.247
- **官方描述（原文）**：AnyCable is a realtime server for reliable two-way communication that supports any backend. Prior to 1.6.15, the telemetry subsystem in telemetry/config.go enables tracking with a hardcoded public authToken, while clusterFingerprint in telemetry/telemetry.go reads the full configuration file and raw os.Args returned by anycableCLIArgs, including values supplied through --secret, --jwt_secret, and --http_rpc_secret. These inputs are passed to generateDigest, where sha256.New produces the hexadecimal fingerprint that is sent as telemetry. The available source therefore does not show raw credentials leaving the process or establish the advisory's claimed confidentiality loss, although the stable fingerprint is derived from secret-bearing configuration and the default telemetry client uses publicly known authentication material. This issue is fixed in version 1.6.15.

### 99. CVE-2026-63405｜anycable / anycable
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:16:59.463)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:16:59.463 / 2026-09-18T18:17:10.130
- **官方描述（原文）**：AnyCable is a realtime server for reliable two-way communication that supports any backend. Prior to 1.6.15, the Pusher-compatible REST API in pusher/http.go includes the caller-supplied body_md5 value in the HMAC input but does not calculate the digest of the received request body or compare it with the signed value. An attacker who obtains a legitimate signed POST request can retain its query parameters and auth_signature while replacing the body, causing Handler and handleEvents to accept and broadcast attacker-selected event content. The absence of an auth_timestamp freshness check also allows the captured signature to be replayed indefinitely. This can forge server-side events, modify application state, or deliver attacker-controlled messages to WebSocket clients within the signed request's application context. This issue is fixed in version 1.6.15.

### 100. CVE-2026-59956｜AcademySoftwareFoundation / OpenImageIO
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:07.290)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:07.290 / 2026-09-18T18:17:07.990
- **官方描述（原文）**：OpenImageIO is a toolset for reading, writing, and manipulating image files of any image file format relevant to VFX / animation. Prior to 3.0.20.0, 3.1.15.0, and 3.2.0.3-beta1, An uncompressed 16-bit iff image with a z-buffer makes iffinput::readimg() allocate a temporary scanline from m_header.rgba_count but copy from it using m_header.pixel_bytes(), whose stride also includes z-buffer bytes. the oversized memcpy reads beyond the temporary heap buffer and copies adjacent memory into the output image, resulting in a crash or disclosure of adjacent heap data. The affected implementation is identified by src/iff.imageio/iffinput.cpp, IffInput::readimg(), m_header.rgba_count, and m_header.pixel_bytes(), which define the relevant source path, functions, state, and trigger. This issue is fixed in versions 3.0.20.0, 3.1.15.0, and 3.2.0.3-beta1.

### 101. CVE-2026-59181｜AcademySoftwareFoundation / OpenImageIO
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:07.137)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:07.137 / 2026-09-18T17:16:58.077
- **官方描述（原文）**：OpenImageIO is a toolset for reading, writing, and manipulating image files of any image file format relevant to VFX / animation. Prior to 3.0.20.0, 3.1.15.0, and 3.2.0.3-beta1, A crafted cineon file can supply a numberofelements value greater than the format maximum of eight. cineoninput::open() uses that unchecked value as the loop bound while filling the fixed strings[8] array, writing pointers beyond the stack buffer and into adjacent state, resulting in memory corruption and denial of service. The affected implementation is identified by src/cineon.imageio/cineoninput.cpp, CineonInput::open(), numberOfElements, and strings[8], which define the relevant source path, functions, state, and trigger. This issue is fixed in versions 3.0.20.0, 3.1.15.0, and 3.2.0.3-beta1.

### 102. CVE-2026-93650｜未確認 / Saleor
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T19:17:24.973)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.9 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T19:17:24.973 / 2026-09-18T20:17:33.177
- **官方描述（原文）**：A vulnerability was determined in Saleor up to 3.20.118/3.21.54/3.22.47/3.23.14. This vulnerability affects the function get_client_ip of the file saleor/account/throttling.py. Executing a manipulation can lead to improper restriction of excessive authentication attempts. The attack can be executed remotely. The attack requires a high level of complexity. It is stated that the exploitability is difficult. The exploit has been publicly disclosed and may be utilized. The projects own issue #19203 internal ticket admits "IP can be spoofed in most deployments" and that its REAL_IP_ENVIRON-type setting bypasses get_client_ip; fix (right-to-left RFC 7239 hop selection) proposed but still unmerged. The vendor explains within an email, that "[t]his is not a vulnerability, this is working at intended, Saleor expects XFF to be configured properly".

### 103. CVE-2026-93531｜gedelumbung / HospitalManagement
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T16:17:14.773)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T16:17:14.773 / 2026-09-18T19:14:56.310
- **官方描述（原文）**：A weakness has been identified in gedelumbung HospitalManagement up to c2d45543789a3887067d3915f69d44cfc2cf76a8. This vulnerability affects unknown code. This manipulation causes cross-site request forgery. The attack may be initiated remotely. The exploit has been made available to the public and could be used for attacks. This product uses a rolling release model to deliver continuous updates. As a result, specific version information for affected or updated releases is not available. The project was informed of the problem early through an issue report but has not responded yet.

### 104. CVE-2026-61633｜nanomq / nanomq
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:16:58.340)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:16:58.340 / 2026-09-18T18:17:09.433
- **官方描述（原文）**：NanoMQ is an MQTT broker. Prior to 0.24.14, the NanoMQ client function nni_mqtt_msg_decode_unsubscribe() in nng/src/supplemental/mqtt/mqtt_codec.c does not handle a failed read_uint16() while counting topics in a malformed UNSUBSCRIBE packet. A zero-length topic followed by trailing data can leave buf.curpos unchanged while topic_count continues to increase, allowing a malicious MQTT broker to hang a connecting MQTT 3.1.1 client, consume CPU and memory, and repeatedly deny service when automatic reconnection is enabled. The broker-side nmq_unsubinfo_decode path is not affected. This issue is fixed in version 0.24.14.

### 105. CVE-2026-44639｜nanomq / nanomq
- **Delta event**：NEW_CVE (from=未確認; to=2026-09-18T17:16:57.127)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 3.7 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-09-18T17:16:57.127 / 2026-09-18T18:17:06.990
- **官方描述（原文）**：NanoMQ is an MQTT broker. Prior to 0.24.14, NanoMQ's MQTT v5 property decoder in nng/src/supplemental/mqtt/mqtt_codec.c uses property_append() to walk the entire linked list for each property added by decode_buf_properties(). A remote unauthenticated client can supply a PUBLISH or SUBSCRIBE packet containing many User Properties, causing O(N²) linked-list insertion and CPU work that makes the broker unresponsive; repeated packets can sustain the denial of service. This issue is fixed in version 0.24.14.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-53266｜Linux / Kernel
- **Title**：Linux Kernel Out-of-Bounds Write Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.00121 / percentile=0.02189
- **CISA KEV**：listed=true / date_added=2026-09-18 / due_date=2026-09-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Linux Kernel contains an out-of-bounds write vulnerability in the ebtables SNAT target which allows an ARP sender hardware address rewrite to write directly into a nonlinear socket-buffer fragment backed by a splice-imported file page. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2025-39682｜Linux / Kernel
- **Title**：Linux Kernel Improper Check for Unusual or Exceptional Conditions Vulnerability
- **Risk**：P1 / score 97；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：0.00505 / percentile=0.42129
- **CISA KEV**：listed=true / date_added=2026-09-18 / due_date=2026-09-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Linux Kernel contains an improper check for unusual or exceptional conditions vulnerability in the TLS receive path which allows a zero-length record retrieved from the rx_list to bypass the intended recvmsg() record-type handling, potentially causing subsequent TLS records to be processed using incorrect zero-copy and queuing assumptions. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2025-39964｜Linux / Kernel
- **Title**：Linux Kernel Race Condition Vulnerability
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00323 / percentile=0.25599
- **CISA KEV**：listed=true / date_added=2026-09-18 / due_date=2026-09-21
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Linux Kernel contains a race condition vulnerability which allows concurrent writes to the same AF_ALG socket causing data to be unpredictably interleaved and creating inconsistencies in the socket's internal state.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-93868 | P3 / 38 | Cotonti / Cotonti | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93606 | P3 / 38 | patriksimek / vm2 | v4.0 10.0 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93019 | P3 / 38 | 未確認 / 未確認 | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-92701 | P3 / 38 | ultravioletrs / cocos | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-84383 | P3 / 38 | strukturag / libheif | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-63647 | P3 / 38 | 1Panel-dev / CordysCRM | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-59163 | P3 / 38 | AxDSan / mnemosyne | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-93838 | WATCH / 30 | sgl-project / sglang | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93753 | WATCH / 30 | TehShrike / deepmerge | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93752 | WATCH / 30 | NV / CSSOM | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93750 | WATCH / 30 | kornelski / http-cache-semantics | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93748 | WATCH / 30 | kornelski / http-cache-semantics | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93690 | WATCH / 30 | garycourt / uri-js | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93687 | WATCH / 30 | micromatch / braces | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93658 | WATCH / 30 | uutils / coreutils | v4.0 7.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93599 | WATCH / 30 | rustls / webpki | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93594 | WATCH / 30 | ArcadeData / arcadedb | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93592 | WATCH / 30 | vllm-project / vllm | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93591 | WATCH / 30 | siyuan-note / siyuan | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-93558 | WATCH / 30 | Red Hat / Red Hat AMQ Broker 7 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89059 | WATCH / 30 | Red Hat / 未確認 | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-89058 | WATCH / 30 | Red Hat / 未確認 | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-88622 | WATCH / 30 | 未確認 / 未確認 | v3.1 8.8 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-84447 | WATCH / 30 | strukturag / libheif | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-84384 | WATCH / 30 | strukturag / libheif | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-81505 | WATCH / 30 | frain-dev / convoy | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-77301 | WATCH / 30 | cthackers / adm-zip | v3.1 7.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

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

- Intelligence items：30；缺少 Vendor：2；缺少 Product：4；缺少 Title：27。
- EPSS 未確認：27；Exploitation status 未確認：0。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-09-19T05:19:08.035619+00:00`；Delta generated at：`2026-09-19T05:19:08.035619+00:00`。

---

## 可驗證資料來源

- **CVE-2026-53266** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-53266) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-53266) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/bf84ad7c7a9ede46e31afaa41a1ba06a159e8c87) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/76280b78cc9f23bdc6438e10ad6dff148ef8375b) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/b7e91939ba9be805a62a257fa4e227dffbb88fa0) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/afd64b59c3de9bbbdd3759e834fdc55cda716e0b) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/153ea96c806aea395daba907a4f88480b6ad5093) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/b18675263db1147c8e1cab625400c13a0d87bd2d) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/c9b5ff59feffb92a147a84a5aa28acd2cb8ff4c5) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/67ba971ae02514d85818fe0c32549ab4bfa3bf49) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-39682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-39682) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-39682) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/2902c3ebcca52ca845c03182000e8d71d3a5196f) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/c09dd3773b5950e9cfb6c9b9a5f6e36d06c62677) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/3439c15ae91a517cf3c650ea15a8987699416ad9) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/29c0ce3c8cdb6dc5d61139c937f34cb888a6f42e) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/62708b9452f8eb77513115b17c4f8d1a22ebf843) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-39964** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-39964) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-39964) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/0f28c4adbc4a97437874c9b669fd7958a8c6d6ce) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/e4c1ec11132ec466f7362a95f36a506ce4dc08c9) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/1f323a48e9b5ebfe6dc7d130fdf5c3c0e92a07c8) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/7c4491b5644e3a3708f3dbd7591be0a570135b84) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/9aee87da5572b3a14075f501752e209801160d3d) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/45bcf60fe49b37daab1acee57b27211ad1574042) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/stable/c/1b34cbbf4f011a121ef7b2d7d6e6920a036d5285) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-93868** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93868)
- **CVE-2026-93606** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93606)
- **CVE-2026-93019** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93019)
- **CVE-2026-92701** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92701)
- **CVE-2026-84383** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84383)
- **CVE-2026-63647** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63647)
- **CVE-2026-59163** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59163)
- **CVE-2026-93838** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93838)
- **CVE-2026-93753** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93753)
- **CVE-2026-93752** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93752)
- **CVE-2026-93750** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93750)
- **CVE-2026-93748** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93748)
- **CVE-2026-93690** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93690)
- **CVE-2026-93687** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93687)
- **CVE-2026-93658** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93658)
- **CVE-2026-93599** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93599)
- **CVE-2026-93594** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93594)
- **CVE-2026-93592** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93592)
- **CVE-2026-93591** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93591)
- **CVE-2026-93558** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93558)
- **CVE-2026-89059** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89059)
- **CVE-2026-89058** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89058)
- **CVE-2026-88622** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88622)
- **CVE-2026-84447** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84447)
- **CVE-2026-84384** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84384)
- **CVE-2026-81505** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81505)
- **CVE-2026-77301** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77301)
- **CVE-2026-7006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-7006)
- **CVE-2026-63419** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63419)
- **CVE-2026-58197** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58197)
- **CVE-2025-61682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-61682)
- **CVE-2017-20284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2017-20284)
- **CVE-2026-93839** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93839)
- **CVE-2026-93762** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93762)
- **CVE-2026-93740** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93740)
- **CVE-2026-93659** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93659)
- **CVE-2026-93605** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93605)
- **CVE-2026-93603** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93603)
- **CVE-2026-92702** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92702)
- **CVE-2026-92229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92229)
- **CVE-2026-89274** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89274)
- **CVE-2026-85497** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85497)
- **CVE-2026-84738** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84738) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-84738)
- **CVE-2026-84434** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84434)
- **CVE-2026-84082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84082)
- **CVE-2026-84078** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84078)
- **CVE-2026-84075** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84075)
- **CVE-2026-84073** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84073)
- **CVE-2026-84064** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84064)
- **CVE-2026-84031** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84031)
- **CVE-2026-82967** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82967)
- **CVE-2026-82832** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82832)
- **CVE-2026-82340** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82340)
- **CVE-2026-81657** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81657)
- **CVE-2026-81321** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81321)
- **CVE-2026-80442** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80442)
- **CVE-2026-80441** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-80441)
- **CVE-2026-77240** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77240)
- **CVE-2026-75885** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75885)
- **CVE-2026-75878** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75878)
- **CVE-2026-75031** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75031)
- **CVE-2026-67101** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67101) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-67101)
- **CVE-2026-67100** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-67100) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-67100)
- **CVE-2026-61781** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61781)
- **CVE-2026-61682** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61682)
- **CVE-2026-61550** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61550)
- **CVE-2026-58264** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-58264)
- **CVE-2026-28198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-28198)
- **CVE-2026-28197** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-28197)
- **CVE-2026-13684** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13684) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-13684)
- **CVE-2026-13639** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13639) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-13639)
- **CVE-2026-10858** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-10858)
- **CVE-2026-10747** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-10747)
- **CVE-2025-66455** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-66455)
- **CVE-2025-53837** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-53837)
- **CVE-2025-15399** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-15399)
- **CVE-2023-5778** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-5778)
- **CVE-2023-54399** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-54399)
- **CVE-2026-93873** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93873)
- **CVE-2026-93736** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93736)
- **CVE-2026-93604** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93604)
- **CVE-2026-93597** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93597)
- **CVE-2026-93596** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93596)
- **CVE-2026-93578** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93578)
- **CVE-2026-93534** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93534)
- **CVE-2026-93505** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93505)
- **CVE-2026-92747** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-92747)
- **CVE-2026-84992** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84992)
- **CVE-2026-81627** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81627)
- **CVE-2026-79294** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79294)
- **CVE-2026-77385** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77385)
- **CVE-2026-77339** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77339)
- **CVE-2026-69186** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69186)
- **CVE-2026-65970** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65970)
- **CVE-2026-63406** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63406)
- **CVE-2026-63405** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63405)
- **CVE-2026-59956** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59956)
- **CVE-2026-59181** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59181)
- **CVE-2026-93650** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93650)
- **CVE-2026-93531** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93531)
- **CVE-2026-61633** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-61633)
- **CVE-2026-44639** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-44639)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
