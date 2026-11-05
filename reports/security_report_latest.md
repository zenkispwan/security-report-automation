# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**65** 筆符合目前門檻的重要變化；事件統計：CVSS_CHANGED=2、EPSS_INCREASED=1、NEW_CVE=61、NEW_KEV=1。
- Intelligence 候選：**30** 筆；P1 **2**、P2 **0**、P3 **3**、WATCH **25**。
- Baseline：state / generated_at=2026-11-04T07:06:27.852213+00:00 / available=true。
- 目前排序最前的 P1：CVE-2024-27834、CVE-2026-97229。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **65** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2024-27834｜Apple / Multiple Products
- **Delta event**：NEW_KEV (from=false; to=true)
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00598 / percentile=0.4875
- **CISA KEV**：listed=true / date_added=2026-11-04 / due_date=2026-11-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2024-05-14T15:13:06.953 / 2026-11-05T05:18:14.483
- **官方描述（原文）**：Apple iOS, iPadOS, macOS, Safari, tvOS and watchOS 10.5 contain an improper authentication vulnerability which could allow an attacker with arbitrary read and write capability to bypass pointer authentication.

### 2. CVE-2026-97229｜GitLab / Community Edition and Enterprise Edition
- **Delta event**：EPSS_INCREASED (from=0.27692; to=0.6522)
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.6522 / percentile=0.99256
- **CISA KEV**：listed=true / date_added=2026-10-29 / due_date=2026-11-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **Published / Updated**：2026-10-13T02:17:00.840 / 2026-11-02T13:30:16.800
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.

### 3. CVE-2026-121953｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:47.717)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:47.717 / 2026-11-04T19:17:35.897
- **官方描述（原文）**：FreeRDP before 3.32.2 has a use-after-free in the client's rdpgfx dynamic virtual channel: a duplicate-name channel with a new ChannelId overwrites the listener's single callback slot, which rdpgfx_on_close frees without clearing. A malicious RDP server can open and close such a channel, then send a PDU on the original channel to crash the client or potentially execute code.

### 4. CVE-2026-121952｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:47.530)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:47.530 / 2026-11-04T19:17:35.673
- **官方描述（原文）**：FreeRDP before 3.32.2 has an out-of-bounds write in the proxy because rdp_read_bitmap_cache_v2_capability_set rejects only numCellCaches values above 5, yet the bitmap cache v2 cell array is later accessed at fixed indices 0 through 4. A client connecting to the proxy can declare fewer than five cell caches in its Confirm Active, causing heap corruption, heap data leakage to the backend, or a crash.

### 5. CVE-2026-121939｜David-Crty / Databasement
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:28.210)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:28.210 / 2026-11-04T19:17:34.167
- **官方描述（原文）**：Databasement before 1.10.9 contains an authentication bypass vulnerability in OAuthService::findOrCreateLocalUser() that links OIDC identities to local users by email without checking email_verified. Attackers can register an identity provider account with a victim's unverified email to log in as any user, including the super-admin, and retain access after password resets.

### 6. CVE-2026-121964｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:49.683)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:49.683 / 2026-11-04T19:17:38.040
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a heap-based buffer overflow in the RD Gateway RPC client, where rpc_client_recv_fragment writes BIND_ACK and ALTER_CONTEXT_RESP fragments into a persistent PDU stream after checking only total capacity rather than remaining capacity from the current stream position. A malicious or compromised RD Gateway can send crafted RPC fragments with manipulated alloc_hint and frag_length values to overwrite client heap memory with attacker-controlled data, causing a crash or potentially arbitrary code execution.

### 7. CVE-2026-121963｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:49.500)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:49.500 / 2026-11-04T19:17:37.857
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a use-after-free vulnerability in the asynchronous dynamic rdpsnd channel that allows malicious RDP servers to trigger freed callback access by closing the channel with queued audio PDUs. Attackers can send a training PDU then close the channel so the playback thread reads the freed callback in rdpsnd_virtual_channel_write, crashing the client.

### 8. CVE-2026-121962｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:49.320)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:49.320 / 2026-11-04T19:17:37.680
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a heap buffer overflow in transport_default_read_pdu when handling partial Early User Authorization reads during PROTOCOL_HYBRID_EX CredSSP. A malicious RDP server can split the four-byte EUA result into short reads that advance the stream pointer beyond the 16 KiB allocation, causing an out-of-bounds write and client denial of service.

### 9. CVE-2026-121961｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:49.147)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:49.147 / 2026-11-04T19:17:37.463
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a use-after-free vulnerability in the freerdp-proxy DRDYNVC tracker when intercepting the drdynvc channel. A malicious target server can repeatedly send CREATE_REQUEST_PDU for an active channel id, racing front DATA handling to free a borrowed context and crash the proxy process.

### 10. CVE-2026-121960｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:48.970)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:48.970 / 2026-11-04T19:17:37.253
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a denial of service vulnerability in the NLA-enabled shadow server when a CredSSP TSRequest omits negoTokens. Unauthenticated attackers can send a crafted seven-byte TSRequest containing only the version field to trigger a fatal WINPR_ASSERT and abort the server process.

### 11. CVE-2026-121959｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:48.793)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:48.793 / 2026-11-04T19:17:37.020
- **官方描述（原文）**：FreeRDP before 3.32.2 contains an infinite loop vulnerability in websocket_context_read that fails to handle a zero BIO result with payload outstanding. A malicious RD Gateway can send a truncated WebSocket frame followed by a TLS close_notify, causing a client thread to spin and consume CPU until killed.

### 12. CVE-2026-121958｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:48.610)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:48.610 / 2026-11-04T19:17:36.827
- **官方描述（原文）**：FreeRDP through 3.32.1 has a heap out-of-bounds write in the RDPGFX client because the delete_surface callback truncates surface hash keys to 16 bits, leaving the surface table inconsistent so HashTable_GetKeys writes past its allocated key array. A malicious or man-in-the-middle RDP server can exploit this by creating surfaceId 0xFFFF, closing the RDPGFX channel, sending repeated DELETESURFACE PDUs, and then sending ENDFRAME or RESETGRAPHICS.

### 13. CVE-2026-121957｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:48.423)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:48.423 / 2026-11-04T19:17:36.640
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a use-after-free vulnerability that allows malicious RDP servers to corrupt client memory by racing the RDPGFX ResetGraphics handler against the planar bitmap decoder. Attackers can send ResetGraphics while concurrently sending compressed bitmaps of 32 bpp or more to trigger heap use-after-free or out-of-bounds read/write on shared planar buffers.

### 14. CVE-2026-121956｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:48.250)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:48.250 / 2026-11-04T19:17:36.447
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a double free in the WinPR Kerberos SSPI retrieveSomeTgt function, which installs the krb5 default realm into a target principal that has an empty realm without taking ownership of it. Unauthenticated remote clients can send a crafted NLA/CredSSP u2u TGT request whose server-name component contains '@' to corrupt the heap and crash the server process.

### 15. CVE-2026-121955｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:48.070)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:48.070 / 2026-11-04T19:17:36.260
- **官方描述（原文）**：FreeRDP before 3.32.2 contains a use-after-free vulnerability in Emulate_SCardReleaseContext that frees the emulated SCardContext before its worker thread is cancelled and joined. A malicious server can send ESTABLISHCONTEXT, a long-timeout GETSTATUSCHANGE, then RELEASECONTEXT smartcard IRPs to corrupt heap memory or crash clients using smartcard emulation.

### 16. CVE-2026-121954｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:47.890)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:47.890 / 2026-11-04T19:17:36.083
- **官方描述（原文）**：FreeRDP before 3.32.2 has a heap out-of-bounds write in the planar codec because freerdp_bitmap_planar_context_reset commits new dimensions before buffer reallocation succeeds, and a failed ResetGraphics is only logged. A malicious RDP server can send an oversized ResetGraphics PDU, then a GFX PLANAR command, to corrupt client heap memory and crash the client.

### 17. CVE-2026-121951｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:47.350)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:47.350 / 2026-11-04T19:17:35.493
- **官方描述（原文）**：FreeRDP 3.0.0 before 3.32.2 server-side RDP peer input parsing skips the six-byte body of a slow-path input event with an unknown message type without checking it lies within the packet's declared length, causing a WinPR stream assertion failure. A remote RDP client with an active session can send a truncated unknown input event to abort assertion-enabled server processes, causing denial of service.

### 18. CVE-2026-121950｜FreeRDP / FreeRDP
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T16:17:47.153)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T16:17:47.153 / 2026-11-04T19:17:35.283
- **官方描述（原文）**：FreeRDP before 3.32.2 does not check the product of surface dimensions in gdi_CreateSurface when handling an RDPGFX CREATE_SURFACE PDU, causing an integer wrap and heap buffer overflow on 32-bit builds and an approximately 4 GiB allocation on 64-bit builds. A malicious RDP server can send a CREATE_SURFACE PDU with width and height 32766 to a connecting client to corrupt heap memory or cause a denial of service.

### 19. CVE-2026-121945｜CoopCycle / coopcycle-web
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:29.313)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.2 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:29.313 / 2026-11-04T19:17:34.983
- **官方描述（原文）**：CoopCycle coopcycle-web before 6.20.1 contains a broken access control vulnerability that allows any courier to read and modify every incident because Incident operations only check ROLE_COURIER. Attackers can enumerate sequential incident ids and use PUT /api/incidents/{id}/action to re-price, cancel or reschedule other stores' orders and tasks.

### 20. CVE-2026-121941｜munt / libmt32emu
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:28.560)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:28.560 / 2026-11-04T21:18:06.527
- **官方描述（原文）**：libmt32emu before 2.8.4 contains a heap buffer overflow vulnerability in MidiStreamParserImpl::parseSysex that allows attackers to write past a heap allocation by supplying oversized unterminated SysEx messages. Attackers can feed more than 32768 SysEx data bytes through the mt32emu_parse_stream API via MIDI files, ports, or sequencer clients to corrupt heap memory and crash the application.

### 21. CVE-2026-121940｜Stonewuu / ai-fusion-video
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:28.393)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:28.393 / 2026-11-04T19:17:34.313
- **官方描述（原文）**：Stonewuu ai-fusion-video before 1.3.0 contains an insecure direct object reference vulnerability that allows authenticated users to access other users' projects by supplying unscoped object ids. Attackers can enumerate auto-increment ids on /api/project, /api/asset and /api/script handlers to read, overwrite, cascade-delete data, and add themselves as project members.

### 22. CVE-2026-97693｜xerrors / Yuxi
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T22:18:07.687)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T22:18:07.687 / 2026-11-04T22:18:07.687
- **官方描述（原文）**：Yuxi is a large-model-based intelligent knowledge base and knowledge graph agent development platform. From 0.6.0.beta1 until 0.7.1, there is insufficient isolation between execution-capable Docker sandboxes and trusted application services. A low-privileged authenticated user who can execute commands in their own sandbox can reach other tenants' sandbox APIs, access their files and secrets, execute commands in active sandboxes, and enumerate, create, or delete sandboxes through the unauthenticated provisioner without knowing administrator, database, or MinIO credentials. Sandboxes can also reach shared internal services; if shipped default service credentials remain unchanged, an attacker can use them, and if the exposed PostgreSQL account is a superuser, obtain command execution in the PostgreSQL container. These paths can disclose or modify cross-tenant data and sandbox state or cause denial of service through sandbox deletion without a container escape or kernel vulnerability. This vulnerability is fixed in 0.7.1. Existing deployments must separately rotate persisted PostgreSQL, Neo4j, or MinIO credentials that were previously set to documented or shipped defaults because upgrading the Compose files does not automatically rotate them.

### 23. CVE-2026-82418｜IBM / Watson Speech Services Cartridge
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T21:18:14.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T21:18:14.940 / 2026-11-04T21:18:15.060
- **官方描述（原文）**：IBM Watson Speech Services Cartridge 4.0.0 through 5.4.0 could allow a remote attacker to execute arbitrary code due to a use-after-free vulnerability.

### 24. CVE-2026-65555｜Uncanny Owl / Uncanny Toolkit for LearnDash
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:30.957)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:30.957 / 2026-11-04T15:17:47.323
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in Uncanny Owl Uncanny Toolkit for LearnDash uncanny-learndash-toolkit allows Privilege Escalation.This issue affects Uncanny Toolkit for LearnDash: from n/a through 3.8.2.

### 25. CVE-2026-57566｜readest / readest
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T22:18:06.850)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T22:18:06.850 / 2026-11-04T22:18:06.850
- **官方描述（原文）**：Readest is a modern, feature-rich ebook reader designed for seamless cross-platform access and an intuitive reading experience. Prior to 0.11.10, the unauthenticated /api/opds/proxy route in apps/readest-app/src/app/api/opds/proxy/route.ts accepted an attacker-controlled URL and fetched it server-side without restricting the scheme, blocking private, loopback, link-local, or metadata hosts, or revalidating destinations during automatic redirect following. The route also accepted caller-controlled outbound headers and Authorization values and reflected the upstream status and response body. A remote attacker could use the service as an open request proxy and, on Node, Docker, or other self-hosted deployments with internal-network access, retrieve cloud metadata or internal-service responses. Cloudflare Workers deployments restrict access to link-local and private destinations, which reduces the internal-network impact there, but the unauthenticated public fetch-and-reflect behavior remains. This issue is fixed in version 0.11.10.

### 26. CVE-2026-54384｜Shenzhen Shine Industrial Co., Ltd. / VitaFit
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T23:17:48.523)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T23:17:48.523 / 2026-11-04T23:17:48.523
- **官方描述（原文）**：VitaFit cloud API before 2026-10-30 contained an authentication bypass vulnerability that allows remote attackers to obtain a full session for a victim's account by submitting a linked Google or Facebook account identifier to the POST /front/login/sns/ endpoint without providing proof of ownership from the identity provider. Attackers can forge a login using an identifier exposed through account enumeration to read and modify the victim's profile and delete the account's authentication record, preventing the legitimate user from logging in.

### 27. CVE-2026-54378｜Shenzhen Shine Industrial Co., Ltd. / VitaFit
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T22:18:05.777)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T22:18:05.777 / 2026-11-04T22:18:05.777
- **官方描述（原文）**：VitaFit cloud API before 2026-10-30 contained a broken access control vulnerability that allows any authenticated user to obtain temporary AWS credentials by calling the POST /front/user/s3/token/ endpoint. Attackers can use these improperly scoped credentials to list the shared storage bucket and read or overwrite other users' stored files, enabling unauthorized cross-user data access and manipulation.

### 28. CVE-2026-52848｜glpi-project / glpi
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T23:17:46.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T23:17:46.560 / 2026-11-04T23:17:46.693
- **官方描述（原文）**：GLPI is a free asset and IT management software package. From 11.0.0 until 11.0.8, during the login phase, an unauthenticated user could use a crafted URL to skip one-time-password verification, defeating two-factor authentication. This issue is fixed in version 11.0.8.

### 29. CVE-2026-123025｜OPNsense / os-acme-client
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T07:17:25.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T07:17:25.897 / 2026-11-05T07:17:25.897
- **官方描述（原文）**：An OS Command Injection vulnerability was discovered in the Google Cloud DNS validation module of the OPNsense os-acme-client plugin through 4.17. The DnsGcloud::prepare() method decodes the dns_gcloud_key model field and directly interpolates the string fields gcloud_account and gcloud_project into a shell command passed to proc_open() via LeUtils::run_shell_command() without any validation or escaping. A remote authenticated user with privileges to issue or renew certificates through the WebGUI/API can achieve arbitrary code execution as root.

### 30. CVE-2026-122992｜G4KLX / DStarGateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T03:17:25.513)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T03:17:25.513 / 2026-11-05T03:17:25.513
- **官方描述（原文）**：In G4KLX DStarGateway and F4FXL DStarGateway before 7b75de6, dstarCallsignToAPRS in APRSUtils.cpp has an integer underflow via an empty RS-MS1A sender field.

### 31. CVE-2026-122313｜kyverno / kyverno
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T03:17:23.853)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T03:17:23.853 / 2026-11-05T03:17:23.853
- **官方描述（原文）**：Kyverno from 1.17.0 before 1.19.2 contains a privilege escalation vulnerability that allows namespace-scoped tenants to modify resources in other namespaces through NamespacedMutatingPolicy targetMatchConstraints.expression CEL output lacking namespace checks. Attackers can emit a literal target such as another tenant's RoleBinding, which the cluster-wide background controller then mutates to add attacker subjects or alter Roles, NetworkPolicies, and ConfigMaps.

### 32. CVE-2026-122311｜kyverno / kyverno
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T03:17:23.497)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T03:17:23.497 / 2026-11-05T03:17:23.497
- **官方描述（原文）**：Kyverno from 1.16.0 before 1.19.2 fails to validate path segments in the resource argument of resource.get() and resource.post(), allowing namespaced CEL policies to escape their namespace. Tenants who can create a NamespacedValidatingPolicy can insert .. segments to read and write arbitrary cluster objects using the admission controller's ServiceAccount, leading to cluster takeover.

### 33. CVE-2026-122310｜kyverno / kyverno
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T03:17:23.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T03:17:23.337 / 2026-11-05T03:17:23.337
- **官方描述（原文）**：Kyverno from 1.19.1 before 1.19.2 validates a Policy's context.apiCall urlPath after cleaning it but executes the raw path, whose fragment or query the Kubernetes client discards. A namespace-scoped user who can create a Policy can hide ../ segments behind # or ? to reach cluster-scoped endpoints with Kyverno's ServiceAccount, gaining cluster admin.

### 34. CVE-2026-122304｜kyverno / kyverno
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T03:17:22.353)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T03:17:22.353 / 2026-11-05T03:17:22.353
- **官方描述（原文）**：Kyverno from 1.17.0 before 1.19.2 contains an authorization bypass vulnerability that allows namespace admins to escape namespace confinement because the cleanup controller builds its context loader with a nil policy. Attackers can create a namespaced CleanupPolicy with apiCall or globalReference context entries to read cross-namespace Secrets and modify validatingwebhookconfigurations using the cleanup controller's ServiceAccount.

### 35. CVE-2026-122303｜kyverno / kyverno
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T03:17:22.197)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T03:17:22.197 / 2026-11-05T03:17:22.197
- **官方描述（原文）**：Kyverno from 1.17.0 before 1.19.2 contains an authorization bypass vulnerability that allows namespace tenants to overwrite resources in other namespaces via NamespacedMutatingPolicy mutate-existing targetMatchConstraints.expression. Attackers can return a CEL map literal fabricating a target with an attacker-chosen metadata.namespace, causing the privileged background controller to overwrite Secrets, Deployments, or policies cluster-wide.

### 36. CVE-2026-122302｜kyverno / kyverno
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T03:17:22.030)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T03:17:22.030 / 2026-11-05T03:17:22.030
- **官方描述（原文）**：Kyverno before 1.19.2 contains a privilege escalation vulnerability that allows namespace admins to create resources beyond their RBAC because generate-rule admission checks verify the controller's permissions, not the author's. Attackers can create a namespaced Policy with generate rules targeting other namespaces or cluster-scoped kinds, making the background controller create or clone resources cluster-wide.

### 37. CVE-2026-122220｜wpo365 / WPO365 | SEAMLESS WORDPRESS + MICROSOFT INTEGRATION (WPO365 | LOGIN)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T20:19:12.397)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T20:19:12.397 / 2026-11-04T20:19:12.397
- **官方描述（原文）**：WPO365 | LOGIN (wpo365-login) plugin before version 45.2 contains an authentication bypass by capture-replay vulnerability caused by a non-functional anti-replay check in Saml2_Service::check_message_id(), which never persists processed SAML message IDs to the wpo365_saml_message_ids transient due to a logic error that returns before saving. Attackers who capture a validly-signed SAMLResponse can replay it to the ACS endpoint repeatedly within its assertion validity window to log in as the victim, including administrators, without detection since the duplicate message ID check never triggers.

### 38. CVE-2026-122120｜Yealink / Plug-in Softwares
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T19:17:39.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T19:17:39.560 / 2026-11-04T19:17:39.560
- **官方描述（原文）**：In Yealink Plug-in Softwares before 2.35.219.0, there is an unauthorized file write vulnerability under specific scenarios, which may be exploited by attackers to achieve remote code execution.

### 39. CVE-2026-122051｜Edimax / BR-6208AC
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-05T00:17:24.013)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-05T00:17:24.013 / 2026-11-05T00:17:24.173
- **官方描述（原文）**：A flaw has been found in Edimax BR-6208AC 1.32. Affected by this vulnerability is an unknown functionality of the file /goform/mp. Executing a manipulation can lead to command injection. The attack may be launched remotely. The exploit has been published and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 40. CVE-2026-122013｜Comfast / CF-WR632AX
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T21:18:07.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T21:18:07.540 / 2026-11-04T21:18:07.710
- **官方描述（原文）**：A vulnerability was detected in Comfast CF-WR632AX 2.6.0.1. Affected by this vulnerability is an unknown functionality of the file /usr/bin/webmgnt of the component Multipart Parser. Performing a manipulation of the argument filename results in path traversal. It is possible to initiate the attack remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 41. CVE-2026-122006｜rubyonrails / Active Storage
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T15:17:42.940)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T15:17:42.940 / 2026-11-04T21:18:07.027
- **官方描述（原文）**：The activestorage gem before 8.1.4.1 for Ruby on Rails, when ImageMagick attachment processing occurs, can allow server read and write operations (e.g., reading secret_key_base) because the ImageMagick analyzer runs when a file is attached, and there is not an ImageMagick security policy to block unintended functionality.

### 42. CVE-2026-121933｜Linksys / E5350
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T20:19:11.607)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T20:19:11.607 / 2026-11-04T20:19:11.813
- **官方描述（原文）**：A flaw has been found in Linksys E5350 1.0.00.037. This impacts the function save_settings of the file /wizard/apply.cgi of the component Setup Wizard. Executing a manipulation of the argument wizard_router_pwd can lead to missing authentication. The attack may be launched remotely. The exploit has been published and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 43. CVE-2026-121932｜Linksys / E5350
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T19:17:33.440)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T19:17:33.440 / 2026-11-04T19:17:33.623
- **官方描述（原文）**：A vulnerability was detected in Linksys E5350 1.0.00.037. This affects the function system of the file /wizard/apply.cgi. Performing a manipulation of the argument ping_ip/traceroute_ip results in os command injection. The attack may be initiated remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.

### 44. CVE-2026-121640｜WatchGuard / AuthPoint Authentication Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T15:17:42.790)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T15:17:42.790 / 2026-11-04T19:17:31.920
- **官方描述（原文）**：An Authentication Bypass by Capture-replay vulnerability in WatchGuard AuthPoint Gateway allows an attacker who has observed a legitimate request between AuthPoint Gateway components to replay it and perform unauthorized administrative actions, including disrupting authentication services.

### 45. CVE-2026-121639｜WatchGuard / AuthPoint Authentication Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T15:17:42.600)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T15:17:42.600 / 2026-11-04T19:17:31.773
- **官方描述（原文）**：A Missing Authentication for Critical Function vulnerability in WatchGuard AuthPoint Gateway allows a remote unauthenticated attacker with network access to the AuthPoint Gateway host to disrupt authentication services and delete the local directory synchronization configuration.

### 46. CVE-2026-121638｜WatchGuard / AuthPoint Authentication Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T15:17:42.437)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T15:17:42.437 / 2026-11-04T19:17:31.637
- **官方描述（原文）**：An Improper Certificate Validation vulnerability in WatchGuard AuthPoint Gateway allows an attacker with an on-path network position to intercept and modify communications between the AuthPoint Gateway and local authentication providers.

### 47. CVE-2026-119481｜Crocoblock / JetFormBuilder
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:26.473)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:26.473 / 2026-11-04T15:17:40.793
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in Crocoblock JetFormBuilder jetformbuilder allows Privilege Escalation.This issue affects JetFormBuilder: from n/a through 3.6.7.1.

### 48. CVE-2026-115770｜pocket-id / pocket-id
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T23:17:18.767)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T23:17:18.767 / 2026-11-04T23:17:18.767
- **官方描述（原文）**：Pocket ID is an OIDC provider that allows users to authenticate with their passkeys to services. From 2.2.0 until 2.12.0, SendEmailVerification uses the token model in backend/internal/model/email_verification_token.go to bind an email-verification token only to the user's identifier, while UpdateUser can change the account email without invalidating the outstanding token and VerifyEmail marks the current address as verified. An ordinary user can request a token for an address they control, change the account to an arbitrary unused address, and redeem the old token so Pocket ID publishes the new address with email_verified set to true. The default affected configuration uses emailsVerified=false and allowOwnAccountEdit=true; the target address must not already belong to another Pocket ID user. A relying application that trusts a verified email for automatic account matching or provisioning can link the attacker's identity to another user's account, while applications that rely exclusively on the stable OIDC sub claim are not affected by that downstream consequence. This issue is fixed in version 2.12.0.

### 49. CVE-2026-114425｜SEPPmail AG / SEPPmail Secure Email Gateway (SEG)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T09:17:41.833)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00329 / percentile=0.26165
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T09:17:41.833 / 2026-11-04T14:11:57.473
- **官方描述（原文）**：SEPPmail Secure Email Gateway before 15.1.1 trusts a file path supplied in externally provided Large File Transfer attachment metadata. An unauthenticated remote sender can cause the mail-processing worker to disclose, move, or delete an accessible regular file when LFT is enabled and the message reaches an affected secure-mail processing path. The validated workers ran as root.

### 50. CVE-2026-114424｜SEPPmail AG / SEPPmail Secure Email Gateway (SEG)
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T09:17:41.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：0.00262 / percentile=0.18122
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T09:17:41.693 / 2026-11-04T14:11:57.473
- **官方描述（原文）**：SEPPmail Secure Email Gateway before 15.1.1 can evaluate attacker-influenced replacement text as Perl code in sender or recipient replacement rules. An unauthenticated remote sender can execute operating-system commands in the mail-processing worker context when an active rule uses message-derived replacement data and its search condition matches. The validated worker context was root.

### 51. CVE-2026-113780｜espressif / esp-idf
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T19:17:18.493)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T19:17:18.493 / 2026-11-04T19:17:18.493
- **官方描述（原文）**：ESF-IDF is the Espressif Internet of Things (IOT) Development Framework. From 5.5.5 until 5.5.6, 6.0.4, and 6.1.1, the esp_tee trap entry in esp_tee_vectors_plic.S and esp_tee_vectors_clic.S saves a caller-controlled register frame through the REE-supplied stack pointer before switching to the trusted TEE stack or validating the pointer. A local unprivileged REE application can direct this machine-mode write into TEE-exclusive memory on ESP32-C5, ESP32-C6, ESP32-C61, and ESP32-H2 devices, breaking the REE/TEE isolation boundary and potentially corrupting TEE control-flow data for code execution, denial of service, or system crashes. Both secure-service ecall and interrupt entry paths contain the vulnerable ordering. This issue is fixed in version 5.5.6 and is scheduled to be fixed in versions 6.0.4 and 6.1.1.

### 52. CVE-2026-113373｜Sonatype / Nexus Repository 3
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T20:18:56.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T20:18:56.750 / 2026-11-04T20:18:56.750
- **官方描述（原文）**：Sonatype Nexus Repository 3 Pro does not check the local account status when a user signs in through a configured SAML or OAuth2/OpenID Connect identity provider. A user whose account was disabled or locked by an administrator in Nexus Repository can sign in again with valid identity provider credentials for the same account, and then receives a new session with the roles of that account. The attacker needs no Nexus Repository session and no Nexus Repository privilege. The attacker needs a named account that holds valid credentials at the identity provider. The anonymous user is not part of this attack path.

### 53. CVE-2026-107846｜bitcoinjs / bitcoinjs-lib
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T19:17:18.130)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T19:17:18.130 / 2026-11-04T19:17:18.130
- **官方描述（原文）**：bitcoinjs-lib is a JavaScript Bitcoin library for Node.js and browsers. From 2.3.0 until 5.2.1, 6.1.8, and 7.0.2, fastMerkleRoot pads odd Merkle-tree levels by hashing the final node with itself but does not report adjacent duplicate hashes. The affected block-root verifier was introduced as Block.checkMerkleRoot() alongside Block.calculateMerkleRoot(), while later versions expose validation through checkTxRoots() and __checkMerkleRoot; these validation paths can accept a recomputed root without checking for mutation. A peer can append duplicate transactions so a different transaction list retains the original Merkle root, block header, proof of work, and block identifier. Consumers that rely on block-root validation, including explorers, exchange indexers, or SPV clients, can process a duplicated transaction twice or blacklist the shared block hash and reject the honest block. This issue is fixed in versions 5.2.1, 6.1.8, and 7.0.2.

### 54. CVE-2026-102895｜gpustack / gpustack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T22:17:44.613)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T22:17:44.613 / 2026-11-04T22:17:44.613
- **官方描述（原文）**：GPUStack is an open-source GPU cluster manager for AI model serving and GPU instance provisioning. Prior to 2.2.0, get_current_user in gpustack/api/auth.py treated a loopback request source as the built-in administrator when force_auth_localhost was false, which was the default. A remote request could appear to originate from 127.0.0.1 because client_ip_getter accepted a same-host reverse proxy peer or a client-supplied X-GPUStack-Real-IP loopback value. The bypass allowed unauthenticated administrative access, including user and model changes, persistent administrator API-key creation, disclosure of worker and cloud-provider secrets, and code execution through POST /v2/inference-backends/from-yaml. Exploitation was observed in the wild against a 2.1.1 deployment. This issue is fixed in version 2.2.0.

### 55. CVE-2026-102894｜gpustack / gpustack
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T22:17:44.440)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T22:17:44.440 / 2026-11-04T22:17:44.440
- **官方描述（原文）**：GPUStack is an open-source GPU cluster manager for AI model serving and GPU instance provisioning. From 0.7.1 until 2.2.2, the /auth/saml/callback endpoint decoded SAML XML, used its NameID and attributes to resolve or provision a user, and minted a gpustack_session JWT without calling OneLogin_Saml2_Auth.process_response to verify the signature, issuer, audience, destination, or time conditions. Any network client could submit an identity for an existing user, including an administrator, or provision a new non-administrator account, even when SAML was not configured. Response and Assertion identifiers were not consumed, so captured signed responses could also be replayed. This issue is fixed in version 2.2.2.

### 56. CVE-2025-71457｜vtenext / vtenext
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T21:17:40.340)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T21:17:40.340 / 2026-11-04T21:17:40.340
- **官方描述（原文）**：vtenext 25.02 before 25.02.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to change any account password via hub/rpwd.php without token verification. Attackers knowing a valid user_name can send action=change_password to RecoverPwd::displayChangePwd() and log in as administrators lacking two-factor authentication.

### 57. CVE-2026-121946｜zbateson / mail-mime-parser
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:29.477)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:29.477 / 2026-11-04T19:17:35.130
- **官方描述（原文）**：zbateson mail-mime-parser before 3.0.9 and 4.x before 4.0.6 contains a CRLF header injection vulnerability in message-building helpers that fail to strip CR and LF characters. Attackers supplying crafted MIME type, charset, encoding, micalg, or protocol values can inject extra header lines such as a forged Bcc into outgoing messages.

### 58. CVE-2026-121944｜irontec / sngrep
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:29.123)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:29.123 / 2026-11-04T19:17:34.800
- **官方描述（原文）**：sngrep through 1.9.0 contains an infinite loop vulnerability in capture_packet_reasm_ip() in src/capture.c that allows attackers to cause denial of service via crafted NFLOG TLVs. Attackers can supply a pcap file with link type NFLOG containing a non-payload TLV with length under 4, making the capture thread spin at full CPU and stop processing packets.

### 59. CVE-2026-121943｜irontec / sngrep
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:28.923)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:28.923 / 2026-11-04T19:17:34.610
- **官方描述（原文）**：Irontec sngrep through 1.9.0 contains an out-of-bounds stack read vulnerability in sip_check_packet and sip_validate_packet caused by an off-by-one length check on 10240-byte SIP payloads. Remote attackers can send a crafted UDP or TCP SIP packet or supply a pcap file to crash sngrep or leak adjacent stack bytes into displayed SIP fields.

### 60. CVE-2026-121942｜mchehab / zbar
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:28.740)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:28.740 / 2026-11-04T19:17:34.460
- **官方描述（原文）**：ZBar through 0.23.95 contains an out-of-bounds read vulnerability in _zbar_sq_decode() in zbar/sqcode.c that allows attackers to read heap memory outside the image buffer via crafted SQ code images. Attackers can supply an image with a skewed SQ code finder pattern near the edge, producing unchecked sample coordinates that crash the decoder and leak bytes into output.

### 61. CVE-2026-121938｜moyangzhan / langchain4j-aideepin
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:28.040)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.0 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:28.040 / 2026-11-04T19:17:34.013
- **官方描述（原文）**：langchain4j-aideepin before 3.31.0 contains an insecure direct object reference vulnerability that allows authenticated users to read other users' character-chat conversations by supplying their character uuid. Attackers can request GET /character/{uuid}, which CharacterService.detail resolves without an ownership check, to obtain victims' questions, AI answers, and attachment and audio URLs.

### 62. CVE-2026-121936｜cosin2077 / easyVoice
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:27.703)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:27.703 / 2026-11-04T19:17:33.683
- **官方描述（原文）**：easyVoice before 0.0.23 contains a server-side request forgery vulnerability that allows unauthenticated attackers to make the server send POST requests by supplying openaiBaseUrl with useLLM enabled. Attackers can target loopback and internal services through /api/v1/tts endpoints, using reflected error messages in the x-generate-tts-warning header to probe internal hosts and ports.

### 63. CVE-2026-121937｜blackholll / loonflow
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-04T13:17:27.870)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.3 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-04T13:17:27.870 / 2026-11-04T19:17:33.860
- **官方描述（原文）**：loonflow before r3.2.3 contains a missing authorization vulnerability in TicketFlowHistoryView that allows any authenticated user to read other users' ticket flow history by supplying a ticket UUID. Attackers can request the ticket_flow_history endpoint, which skips ticket_view_permission_check, to obtain approval comments and processor names, emails and phone numbers.

### 64. CVE-2026-118776｜digitalbazaar / forge
- **Delta event**：CVSS_CHANGED (from=3.7; to=5.3)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00131 / percentile=0.0269
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T19:17:20.147 / 2026-11-04T16:52:39.170
- **官方描述（原文）**：Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, the affected implementation used decipher.finish(), CBC and ECB modes, PKCS#7 padding to process the relevant input or security decision. node-forge validated only the final byte of PKCS#7 padding during CBC and ECB decryption and accepted zero, oversized, or mismatched padding bytes. Malformed ciphertext could consequently be accepted and up to four plaintext blocks could be silently removed, causing an integrity failure in applications that treated successful decryption as proof of valid padding. This issue is fixed in version 1.4.1.

### 65. CVE-2026-118775｜digitalbazaar / forge
- **Delta event**：CVSS_CHANGED (from=3.7; to=5.3)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、DELTA_CVSS_INCREASE(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：0.00313 / percentile=0.24377
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-29T19:17:20.007 / 2026-11-04T14:12:40.780
- **官方描述（原文）**：Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, asn1.oidToDer() in lib/asn1.js did not range-check the first two arcs of an OID. An application that accepted an untrusted OID string, checked or authorized that string, and then encoded it with asn1.oidToDer() could emit DER representing a different, trusted OID from the one that was checked. DER parsing is not affected. This issue is fixed in version 1.4.1.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2024-27834｜Apple / Multiple Products
- **Title**：Apple Multiple Products Improper Authentication Vulnerability
- **Risk**：P1 / score 89；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_MEDIUM(+4)、DELTA_NEW_KEV(+15)
- **CVSS**：v3.1 5.5 (MEDIUM)
- **EPSS**：0.00598 / percentile=0.4875
- **CISA KEV**：listed=true / date_added=2026-11-04 / due_date=2026-11-18
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apple iOS, iPadOS, macOS, Safari, tvOS and watchOS 10.5 contain an improper authentication vulnerability which could allow an attacker with arbitrary read and write capability to bypass pointer authentication.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-97229｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)、DELTA_EPSS_JUMP(+15)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.6522 / percentile=0.99256
- **CISA KEV**：listed=true / date_added=2026-10-29 / due_date=2026-11-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-121953 | P3 / 38 | FreeRDP / FreeRDP | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121952 | P3 / 38 | FreeRDP / FreeRDP | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121939 | P3 / 38 | David-Crty / Databasement | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-121964 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121963 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121962 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121961 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121960 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121959 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121958 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121957 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121956 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121955 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121954 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121951 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121950 | WATCH / 30 | FreeRDP / FreeRDP | v4.0 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121945 | WATCH / 30 | CoopCycle / coopcycle-web | v4.0 7.2 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121941 | WATCH / 30 | munt / libmt32emu | v4.0 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-121940 | WATCH / 30 | Stonewuu / ai-fusion-video | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97693 | WATCH / 28 | xerrors / Yuxi | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-82418 | WATCH / 28 | IBM / Watson Speech Services Cartridge | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-65555 | WATCH / 28 | Uncanny Owl / Uncanny Toolkit for LearnDash | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-57566 | WATCH / 28 | readest / readest | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-54384 | WATCH / 28 | Shenzhen Shine Industrial Co., Ltd. / VitaFit | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-54378 | WATCH / 28 | Shenzhen Shine Industrial Co., Ltd. / VitaFit | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-52848 | WATCH / 28 | glpi-project / glpi | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-123025 | WATCH / 28 | OPNsense / os-acme-client | v4.0 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-122992 | WATCH / 28 | G4KLX / DStarGateway | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：28。
- EPSS 未確認：28；Exploitation status 未確認：8。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-05T07:35:16.367660+00:00`；Delta generated at：`2026-11-05T07:35:16.367660+00:00`。

---

## 可驗證資料來源

- **CVE-2024-27834** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-27834) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2024-27834) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/120896) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/120898) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/120901) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/120902) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/120903) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/120905) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-97229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97229) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97229) · [Vendor / Advisory (ruby-lang.org)](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-121953** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121953)
- **CVE-2026-121952** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121952)
- **CVE-2026-121939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121939)
- **CVE-2026-121964** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121964)
- **CVE-2026-121963** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121963)
- **CVE-2026-121962** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121962)
- **CVE-2026-121961** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121961)
- **CVE-2026-121960** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121960)
- **CVE-2026-121959** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121959)
- **CVE-2026-121958** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121958)
- **CVE-2026-121957** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121957)
- **CVE-2026-121956** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121956)
- **CVE-2026-121955** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121955)
- **CVE-2026-121954** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121954)
- **CVE-2026-121951** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121951)
- **CVE-2026-121950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121950)
- **CVE-2026-121945** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121945)
- **CVE-2026-121941** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121941)
- **CVE-2026-121940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121940)
- **CVE-2026-97693** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97693)
- **CVE-2026-82418** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82418)
- **CVE-2026-65555** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-65555)
- **CVE-2026-57566** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-57566)
- **CVE-2026-54384** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54384)
- **CVE-2026-54378** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54378)
- **CVE-2026-52848** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-52848)
- **CVE-2026-123025** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123025)
- **CVE-2026-122992** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122992)
- **CVE-2026-122313** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122313)
- **CVE-2026-122311** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122311)
- **CVE-2026-122310** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122310)
- **CVE-2026-122304** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122304)
- **CVE-2026-122303** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122303)
- **CVE-2026-122302** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122302)
- **CVE-2026-122220** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122220)
- **CVE-2026-122120** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122120)
- **CVE-2026-122051** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122051)
- **CVE-2026-122013** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122013)
- **CVE-2026-122006** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122006)
- **CVE-2026-121933** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121933)
- **CVE-2026-121932** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121932)
- **CVE-2026-121640** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121640)
- **CVE-2026-121639** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121639)
- **CVE-2026-121638** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121638)
- **CVE-2026-119481** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119481)
- **CVE-2026-115770** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115770)
- **CVE-2026-114425** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114425) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114425)
- **CVE-2026-114424** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114424) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-114424)
- **CVE-2026-113780** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113780)
- **CVE-2026-113373** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113373)
- **CVE-2026-107846** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107846)
- **CVE-2026-102895** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102895)
- **CVE-2026-102894** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102894)
- **CVE-2025-71457** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-71457)
- **CVE-2026-121946** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121946)
- **CVE-2026-121944** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121944)
- **CVE-2026-121943** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121943)
- **CVE-2026-121942** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121942)
- **CVE-2026-121938** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121938)
- **CVE-2026-121936** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121936)
- **CVE-2026-121937** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121937)
- **CVE-2026-118776** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118776) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-118776)
- **CVE-2026-118775** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118775) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-118775)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
