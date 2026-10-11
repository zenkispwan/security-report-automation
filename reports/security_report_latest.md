# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**69** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=69。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **0**、WATCH **30**。
- Baseline：state / generated_at=2026-10-10T06:32:50.093293+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **69** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-93945｜Axiomthemes / Balance
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:07.057)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00331 / percentile=0.24327
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:07.057 / 2026-10-10T08:17:07.057
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Axiomthemes Balance balance allows Object Injection.This issue affects Balance: from n/a through 1.12.0.

### 2. CVE-2026-93944｜ThemeREX Group / Camelia
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:06.930)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00313 / percentile=0.22328
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:06.930 / 2026-10-10T08:17:06.930
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Camelia camelia allows Object Injection.This issue affects Camelia: from n/a through 1.2.15.

### 3. CVE-2026-93943｜ThemeREX Group / Convex
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:06.803)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00313 / percentile=0.22328
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:06.803 / 2026-10-10T08:17:06.803
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Convex convex allows Object Injection.This issue affects Convex: from n/a through 1.16.0.

### 4. CVE-2026-93942｜ThemeREX Group / Dwell
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:06.683)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00313 / percentile=0.22328
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:06.683 / 2026-10-10T08:17:06.683
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Dwell dwell allows Object Injection.This issue affects Dwell: from n/a through 1.16.0.

### 5. CVE-2026-93941｜ThemeREX Group / Edema
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:06.557)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00331 / percentile=0.24327
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:06.557 / 2026-10-10T08:17:06.557
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Edema edema allows Object Injection.This issue affects Edema: from n/a through 1.2.2.2.

### 6. CVE-2026-93940｜ThemeREX Group / Greeny
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:06.433)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00331 / percentile=0.24327
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:06.433 / 2026-10-10T08:17:06.433
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Greeny greeny allows Object Injection.This issue affects Greeny: from n/a through 2.10.0.

### 7. CVE-2026-93938｜ThemeREX Group / Hogwords
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:06.310)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00331 / percentile=0.24328
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:06.310 / 2026-10-10T08:17:06.310
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Hogwords hogwords allows Object Injection.This issue affects Hogwords: from n/a through 1.2.7.

### 8. CVE-2026-93937｜ThemeREX Group / Hygia
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:06.187)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00331 / percentile=0.24327
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:06.187 / 2026-10-10T08:17:06.187
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Hygia hygia allows Object Injection.This issue affects Hygia: from n/a through 1.21.0.

### 9. CVE-2026-93936｜ThemeREX Group / IPharm
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:06.060)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00331 / percentile=0.24326
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:06.060 / 2026-10-10T08:17:06.060
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group IPharm ipharm allows Object Injection.This issue affects IPharm: from n/a through 1.2.4.

### 10. CVE-2026-93935｜ThemeREX Group / Let's Play
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:05.933)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00313 / percentile=0.22329
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:05.933 / 2026-10-10T08:17:05.933
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Let's Play playhockey allows Object Injection.This issue affects Let's Play: from n/a through 1.1.15.

### 11. CVE-2026-93934｜ThemeREX Group / Partiso
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:05.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00313 / percentile=0.22328
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:05.810 / 2026-10-10T08:17:05.810
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Partiso partiso allows Object Injection.This issue affects Partiso: from n/a through 1.1.13.

### 12. CVE-2026-93933｜ThemeREX Group / Rosalinda
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:05.680)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00313 / percentile=0.22327
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:05.680 / 2026-10-10T08:17:05.680
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Rosalinda rosalinda allows Object Injection.This issue affects Rosalinda: from n/a through 1.2.4.

### 13. CVE-2026-93932｜ThemeREX Group / Smart Casa
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:05.547)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00313 / percentile=0.22327
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:05.547 / 2026-10-10T08:17:05.547
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Smart Casa smart-casa allows Object Injection.This issue affects Smart Casa: from n/a through 1.0.12.

### 14. CVE-2026-93931｜ThemeREX Group / Smash
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:05.427)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00313 / percentile=0.22329
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:05.427 / 2026-10-10T08:17:05.427
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Smash smash allows Object Injection.This issue affects Smash: from n/a through 1.12.0.

### 15. CVE-2026-93930｜ThemeREX Group / Tantra
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:05.300)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00313 / percentile=0.22327
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:05.300 / 2026-10-10T08:17:05.300
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Tantra tantra allows Object Injection.This issue affects Tantra: from n/a through 2.9.0.

### 16. CVE-2026-93929｜ThemeREX Group / Travesia
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:05.183)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.0032 / percentile=0.23031
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:05.183 / 2026-10-10T08:17:05.183
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Travesia travesia allows Object Injection.This issue affects Travesia: from n/a through 1.1.16.

### 17. CVE-2026-93927｜Axiomthemes / Veto
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:05.050)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.0032 / percentile=0.2303
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:05.050 / 2026-10-10T08:17:05.050
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Axiomthemes Veto veto allows Object Injection.This issue affects Veto: from n/a through 1.6.0.

### 18. CVE-2026-81797｜ThemeRex / Buzz Stone | Magazine & Viral Blog WordPress Theme
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:47.507)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:47.507 / 2026-10-10T20:16:47.507
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Buzz Stone | Magazine & Viral Blog WordPress Theme <= 1.0.2 versions.

### 19. CVE-2026-78535｜ThemeRex / Photolia
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:47.380)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:47.380 / 2026-10-10T20:16:47.380
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Photolia <= 1.0.3 versions.

### 20. CVE-2026-78533｜AncoraThemes / Qwery
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:47.133)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:47.133 / 2026-10-10T20:16:47.133
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Qwery <= 3.6.1 versions.

### 21. CVE-2026-78531｜ThemeREX / Jacqueline
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:46.830)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:46.830 / 2026-10-10T20:16:46.830
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Jacqueline <= 2.22 versions.

### 22. CVE-2026-78529｜ThemeREX / Alliance
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:46.590)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:46.590 / 2026-10-10T20:16:46.590
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Alliance <= 3.11 versions.

### 23. CVE-2026-66569｜axiomthemes / Kicker
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:46.467)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:46.467 / 2026-10-10T20:16:46.467
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Kicker <= 2.2.1 versions.

### 24. CVE-2026-66568｜axiomthemes / Original
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:46.347)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:46.347 / 2026-10-10T20:16:46.347
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Original <= 1.9.0 versions.

### 25. CVE-2026-66567｜AncoraThemes / Anesta
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:46.223)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:46.223 / 2026-10-10T20:16:46.223
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Anesta <= 1.5.3 versions.

### 26. CVE-2026-66565｜axiomthemes / FC United
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:45.980)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:45.980 / 2026-10-10T20:16:45.980
- **官方描述（原文）**：Unauthenticated PHP Object Injection in FC United <= 1.1.1 versions.

### 27. CVE-2026-66564｜ThemeREX / ShiftCV
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:45.857)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:45.857 / 2026-10-10T20:16:45.857
- **官方描述（原文）**：Unauthenticated PHP Object Injection in ShiftCV <= 3.0.14 versions.

### 28. CVE-2026-66563｜ThemeREX / Windsor
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:45.737)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:45.737 / 2026-10-10T20:16:45.737
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Windsor <= 2.10 versions.

### 29. CVE-2026-66483｜ThemeREX / Education Center
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:45.613)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:45.613 / 2026-10-10T20:16:45.613
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Education Center <= 3.6.12 versions.

### 30. CVE-2026-66482｜AncoraThemes / Drone Media
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:45.493)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:45.493 / 2026-10-10T20:16:45.493
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Drone Media <= 2.2.0 versions.

### 31. CVE-2026-62129｜WPFunnels / Creator LMS
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:44.780)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:44.780 / 2026-10-10T20:16:44.780
- **官方描述（原文）**：Contributor Arbitrary File Upload in Creator LMS <= 1.2.21 versions.

### 32. CVE-2026-62125｜ThemeREX / Asia Garden
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:44.660)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:44.660 / 2026-10-10T20:16:44.660
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Asia Garden <= 1.3.1 versions.

### 33. CVE-2026-62124｜ThemeREX / N7 | Golf Club Sports & Events
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:44.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:44.540 / 2026-10-10T20:16:44.540
- **官方描述（原文）**：Unauthenticated PHP Object Injection in N7 | Golf Club Sports & Events <= 2.21 versions.

### 34. CVE-2026-62123｜ThemeREX / Invetex
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:44.420)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:44.420 / 2026-10-10T20:16:44.420
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Invetex <= 2.18 versions.

### 35. CVE-2026-62120｜ThemeREX / Law Office
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:44.300)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:44.300 / 2026-10-10T20:16:44.300
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Law Office <= 3.20 versions.

### 36. CVE-2026-62090｜ThemeREX / WineShop
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:42.617)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:42.617 / 2026-10-10T20:16:42.617
- **官方描述（原文）**：Unauthenticated PHP Object Injection in WineShop <= 3.20 versions.

### 37. CVE-2026-62087｜ThemeREX / Equadio
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:42.497)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:42.497 / 2026-10-10T20:16:42.497
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Equadio <= 1.1.4 versions.

### 38. CVE-2026-62086｜ThemeREX / Juno
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:42.377)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:42.377 / 2026-10-10T20:16:42.377
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Juno <= 2.25 versions.

### 39. CVE-2026-62077｜BoldThemes / Avala
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:42.143)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:42.143 / 2026-10-10T20:16:42.143
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Avala <= 1.1.4 versions.

### 40. CVE-2026-62076｜The4 / Kalles
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:42.023)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:42.023 / 2026-10-10T20:16:42.023
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Kalles <= 1.1.7.1 versions.

### 41. CVE-2026-62054｜ThemeREX / Yacht Rental
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:40.760)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:40.760 / 2026-10-10T20:16:40.760
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Yacht Rental <= 2.6 versions.

### 42. CVE-2026-62053｜ThemeREX / Wine House
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:40.633)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:40.633 / 2026-10-10T20:16:40.633
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Wine House <= 3.20 versions.

### 43. CVE-2026-62052｜ThemeREX / Tipsy
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:40.510)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:40.510 / 2026-10-10T20:16:40.510
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Tipsy <= 1.6 versions.

### 44. CVE-2026-62051｜ThemeREX / Stargaze
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:40.387)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:40.387 / 2026-10-10T20:16:40.387
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Stargaze <= 1.10 versions.

### 45. CVE-2026-62050｜ThemeREX / Splendour
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:40.260)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:40.260 / 2026-10-10T20:16:40.260
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Splendour <= 1.23 versions.

### 46. CVE-2026-62046｜ThemeREX Group / Gutentype
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:04.777)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.0032 / percentile=0.23031
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:04.777 / 2026-10-10T08:17:04.777
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Gutentype gutentype allows Object Injection.This issue affects Gutentype: from n/a through 2.1.12.

### 47. CVE-2026-62045｜ThemeREX Group / Booklovers
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:04.647)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.0032 / percentile=0.2303
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:04.647 / 2026-10-10T08:17:04.647
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in ThemeREX Group Booklovers booklovers allows Object Injection.This issue affects Booklovers: from n/a through 2.13.0.

### 48. CVE-2026-62032｜Designinvento / DirectoryPress
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:39.357)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:39.357 / 2026-10-10T20:16:39.357
- **官方描述（原文）**：Unauthenticated Local File Inclusion in DirectoryPress <= 3.6.27 versions.

### 49. CVE-2026-62031｜Stylemix / uListing
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:39.237)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:39.237 / 2026-10-10T20:16:39.237
- **官方描述（原文）**：Unauthenticated SQL Injection in uListing <= 2.2.0 versions.

### 50. CVE-2026-62025｜Tailored Media / Tailored Tools
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:38.870)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:38.870 / 2026-10-10T20:16:38.870
- **官方描述（原文）**：Unauthenticated Arbitrary File Upload in Tailored Tools <= 3.0.3 versions.

### 51. CVE-2026-62024｜CodeBard / CodeBard Help Desk
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:38.750)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:38.750 / 2026-10-10T20:16:38.750
- **官方描述（原文）**：Subscriber Arbitrary File Upload in CodeBard Help Desk <= 1.1.2 versions.

### 52. CVE-2026-62022｜Select-Themes / Tonda Membership
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:38.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:38.630 / 2026-10-10T20:16:38.630
- **官方描述（原文）**：Unauthenticated Privilege Escalation in Tonda Membership <= 1.0.1 versions.

### 53. CVE-2026-42723｜AncoraThemes / CleanSkin
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:37.270)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:37.270 / 2026-10-10T20:16:37.270
- **官方描述（原文）**：Unauthenticated PHP Object Injection in CleanSkin <= 1.5.0 versions.

### 54. CVE-2026-42719｜Sarah Giles / Dynamic User Directory
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:37.030)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:37.030 / 2026-10-10T20:16:37.030
- **官方描述（原文）**：Subscriber PHP Object Injection in Dynamic User Directory <= 2.4 versions.

### 55. CVE-2026-42718｜Pluggabl / Booster for WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:36.907)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:36.907 / 2026-10-10T20:16:36.907
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Booster for WooCommerce <= 8.4.0 versions.

### 56. CVE-2026-42716｜payever / Payever - WooCommerce Gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:36.630)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:36.630 / 2026-10-10T20:16:36.630
- **官方描述（原文）**：Unauthenticated PHP Object Injection in Payever - WooCommerce Gateway <= 4.8.2 versions.

### 57. CVE-2026-42696｜Royal Plugins / SiteVault – Backup, Restore, Migration &amp; Cloning
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:35.313)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:35.313 / 2026-10-10T20:16:35.313
- **官方描述（原文）**：Unauthenticated Remote Code Execution (RCE) in SiteVault – Backup, Restore, Migration &amp; Cloning <= 1.5.19 versions.

### 58. CVE-2026-40800｜ELEXtensions / ELEX WooCommerce Advanced Bulk Edit Products, Prices & Attributes
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:33.863)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:33.863 / 2026-10-10T20:16:33.863
- **官方描述（原文）**：Subscriber SQL Injection in ELEX WooCommerce Advanced Bulk Edit Products, Prices & Attributes <= 1.5.3 versions.

### 59. CVE-2026-39801｜Sergey / AIWU
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T20:16:33.483)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T20:16:33.483 / 2026-10-10T20:16:33.483
- **官方描述（原文）**：Subscriber Privilege Escalation in AIWU <= 1.5.9 versions.

### 60. CVE-2026-108707｜WuKongOpenSource / Wukong_HRM
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-11T02:16:39.477)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-11T02:16:39.477 / 2026-10-11T02:16:39.477
- **官方描述（原文）**：Wukong_HRM through commit 186115e contains an authentication bypass vulnerability in ParamAspect that allows unauthenticated attackers to call every HRM API endpoint by omitting the AUTH-TOKEN header. Attackers gain HR administrator access to read payslips, salary history and employee personal data, download attachments, and modify or delete company-wide HR records.

### 61. CVE-2026-108598｜floci-io / floci
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T19:16:58.347)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T19:16:58.347 / 2026-10-10T19:16:58.347
- **官方描述（原文）**：Floci 1.1.0 before 2.2.0 contains a code injection vulnerability in VtlTemplateEngine that allows unauthenticated attackers to execute commands via unrestricted Velocity mapping templates. Attackers can create a REST API with a MOCK integration whose template uses $util reflection to reach Runtime or ProcessBuilder, executing OS commands in the Floci JVM.

### 62. CVE-2026-108551｜ferdikoomen / openapi-typescript-codegen
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T15:16:58.273)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T15:16:58.273 / 2026-10-10T15:16:58.273
- **官方描述（原文）**：openapi-typescript-codegen through 0.31.0 contains a code injection vulnerability that allows attackers controlling an OpenAPI document to inject JavaScript by supplying unescaped values interpolated into single-quoted string literals. Attackers can embed a single quote in path keys, parameter names, servers[0].url, or info.version to execute arbitrary JavaScript when generated clients are imported or service methods called.

### 63. CVE-2026-108549｜chenhg5 / cc-connect
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T15:16:57.973)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T15:16:57.973 / 2026-10-10T15:16:58.087
- **官方描述（原文）**：cc-connect through 1.5.0 contains a missing authentication vulnerability in the MAX platform adapter webhook mode in platform/max/max.go that accepts unauthenticated updates when no webhook_secret is configured. Remote attackers reaching the webhook listener on port 8080 can forge updates with an allowed or admin user_id to run privileged commands like /shell on the host.

### 64. CVE-2026-106610｜miniOrange / miniorange otp verification
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T19:16:57.187)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T19:16:57.187 / 2026-10-10T19:16:57.187
- **官方描述（原文）**：Incorrect Privilege Assignment vulnerability in miniOrange miniorange otp verification miniorange-otp-verification allows Privilege Escalation.This issue affects miniorange otp verification: from n/a through 5.5.7.

### 65. CVE-2026-105892｜rtCamp Inc. / rtMedia for WordPress, BuddyPress and bbPress
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T19:16:56.990)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T19:16:56.990 / 2026-10-10T19:16:56.990
- **官方描述（原文）**：Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in rtCamp Inc. rtMedia for WordPress, BuddyPress and bbPress buddypress-media allows Path Traversal.This issue affects rtMedia for WordPress, BuddyPress and bbPress: from n/a through 4.7.13.

### 66. CVE-2026-105889｜Tickera / Tickera
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T17:17:00.063)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T17:17:00.063 / 2026-10-10T17:17:00.063
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Tickera Tickera tickera-event-ticketing-system allows Blind SQL Injection.This issue affects Tickera: from n/a through 3.6.0.6.

### 67. CVE-2026-104803｜whyun / WPCOM Member
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T08:17:04.210)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.00449 / percentile=0.37118
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T08:17:04.210 / 2026-10-10T08:17:04.210
- **官方描述（原文）**：The WPCOM Member plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 1.7.27 via the `uuid` and `code` parameters of the social-login callback handler registered on the `init` hook. The vulnerability exists because the `login` function's social-login flow performs no nonce validation, no OAuth state verification, and no per-visitor namespace isolation in the session store, allowing an unauthenticated attacker to issue a crafted GET request that writes an attacker-named, attacker-valued entry into the global session namespace (bypassing the per-visitor prefix by prepending an underscore), then issue a second GET request triggering `weapp_new_user()` to read that forged entry and resolve the attacker-supplied `openid` value to a bound WordPress account before `wp_set_auth_cookie()` establishes a fully authenticated session. This makes it possible for unauthenticated attackers to log in as any WordPress user — including administrators — whose bound social provider identifier (openid/unionid) is known or discoverable. Successful exploitation requires that the target site has at least one social provider configured (which activates the vulnerable handler) and that the attacker knows or can enumerate the victim account's bound openid or unionid.

### 68. CVE-2026-104801｜themeisle / PPOM – Product Addons & Custom Fields for WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T07:16:40.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：0.00755 / percentile=0.53807
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T07:16:40.560 / 2026-10-10T07:16:40.560
- **官方描述（原文）**：The PPOM – Product Addons & Custom Fields for WooCommerce plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient file path validation in the rename_files function in all versions up to, and including, 34.0.10 This makes it possible for unauthenticated attackers to delete arbitrary files on the server, which can easily lead to remote code execution when the right file is deleted (such as wp-config.php). The relocated file is moved byte-identically into the publicly accessible wp-content/uploads/ppom_files/confirmed/ directory, meaning the attack also results in arbitrary file read for any web-readable file on the server.

### 69. CVE-2026-104398｜VillaTheme / AFFI – Affiliate Marketing for WooCommerce
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-10T17:16:59.937)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-10T17:16:59.937 / 2026-10-10T17:16:59.937
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in VillaTheme AFFI – Affiliate Marketing for WooCommerce affi-affiliate-marketing-for-woo allows Object Injection.This issue affects AFFI – Affiliate Marketing for WooCommerce: from n/a through 1.0.10.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-93945 | WATCH / 28 | Axiomthemes / Balance | v3.1 9.8 (CRITICAL) | 0.00331 / percentile=0.24327 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93944 | WATCH / 28 | ThemeREX Group / Camelia | v3.1 9.8 (CRITICAL) | 0.00313 / percentile=0.22328 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93943 | WATCH / 28 | ThemeREX Group / Convex | v3.1 9.8 (CRITICAL) | 0.00313 / percentile=0.22328 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93942 | WATCH / 28 | ThemeREX Group / Dwell | v3.1 9.8 (CRITICAL) | 0.00313 / percentile=0.22328 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93941 | WATCH / 28 | ThemeREX Group / Edema | v3.1 9.8 (CRITICAL) | 0.00331 / percentile=0.24327 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93940 | WATCH / 28 | ThemeREX Group / Greeny | v3.1 9.8 (CRITICAL) | 0.00331 / percentile=0.24327 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93938 | WATCH / 28 | ThemeREX Group / Hogwords | v3.1 9.8 (CRITICAL) | 0.00331 / percentile=0.24328 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93937 | WATCH / 28 | ThemeREX Group / Hygia | v3.1 9.8 (CRITICAL) | 0.00331 / percentile=0.24327 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93936 | WATCH / 28 | ThemeREX Group / IPharm | v3.1 9.8 (CRITICAL) | 0.00331 / percentile=0.24326 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93935 | WATCH / 28 | ThemeREX Group / Let's Play | v3.1 9.8 (CRITICAL) | 0.00313 / percentile=0.22329 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93934 | WATCH / 28 | ThemeREX Group / Partiso | v3.1 9.8 (CRITICAL) | 0.00313 / percentile=0.22328 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93933 | WATCH / 28 | ThemeREX Group / Rosalinda | v3.1 9.8 (CRITICAL) | 0.00313 / percentile=0.22327 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93932 | WATCH / 28 | ThemeREX Group / Smart Casa | v3.1 9.8 (CRITICAL) | 0.00313 / percentile=0.22327 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93931 | WATCH / 28 | ThemeREX Group / Smash | v3.1 9.8 (CRITICAL) | 0.00313 / percentile=0.22329 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93930 | WATCH / 28 | ThemeREX Group / Tantra | v3.1 9.8 (CRITICAL) | 0.00313 / percentile=0.22327 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93929 | WATCH / 28 | ThemeREX Group / Travesia | v3.1 9.8 (CRITICAL) | 0.0032 / percentile=0.23031 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-93927 | WATCH / 28 | Axiomthemes / Veto | v3.1 9.8 (CRITICAL) | 0.0032 / percentile=0.2303 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-81797 | WATCH / 28 | ThemeRex / Buzz Stone \| Magazine & Viral Blog WordPress Theme | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-78535 | WATCH / 28 | ThemeRex / Photolia | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-78533 | WATCH / 28 | AncoraThemes / Qwery | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-78531 | WATCH / 28 | ThemeREX / Jacqueline | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-78529 | WATCH / 28 | ThemeREX / Alliance | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-66569 | WATCH / 28 | axiomthemes / Kicker | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-66568 | WATCH / 28 | axiomthemes / Original | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-66567 | WATCH / 28 | AncoraThemes / Anesta | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-66565 | WATCH / 28 | axiomthemes / FC United | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-66564 | WATCH / 28 | ThemeREX / ShiftCV | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-66563 | WATCH / 28 | ThemeREX / Windsor | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-66483 | WATCH / 28 | ThemeREX / Education Center | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-66482 | WATCH / 28 | AncoraThemes / Drone Media | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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
- EPSS 未確認：13；Exploitation status 未確認：30。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-11T06:38:54.512909+00:00`；Delta generated at：`2026-10-11T06:38:54.512909+00:00`。

---

## 可驗證資料來源

- **CVE-2026-93945** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93945) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93945)
- **CVE-2026-93944** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93944) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93944)
- **CVE-2026-93943** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93943) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93943)
- **CVE-2026-93942** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93942) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93942)
- **CVE-2026-93941** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93941) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93941)
- **CVE-2026-93940** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93940) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93940)
- **CVE-2026-93938** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93938) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93938)
- **CVE-2026-93937** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93937) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93937)
- **CVE-2026-93936** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93936) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93936)
- **CVE-2026-93935** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93935) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93935)
- **CVE-2026-93934** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93934) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93934)
- **CVE-2026-93933** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93933) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93933)
- **CVE-2026-93932** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93932) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93932)
- **CVE-2026-93931** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93931) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93931)
- **CVE-2026-93930** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93930) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93930)
- **CVE-2026-93929** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93929) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93929)
- **CVE-2026-93927** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-93927) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-93927)
- **CVE-2026-81797** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81797)
- **CVE-2026-78535** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78535)
- **CVE-2026-78533** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78533)
- **CVE-2026-78531** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78531)
- **CVE-2026-78529** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78529)
- **CVE-2026-66569** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66569)
- **CVE-2026-66568** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66568)
- **CVE-2026-66567** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66567)
- **CVE-2026-66565** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66565)
- **CVE-2026-66564** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66564)
- **CVE-2026-66563** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66563)
- **CVE-2026-66483** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66483)
- **CVE-2026-66482** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-66482)
- **CVE-2026-62129** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62129)
- **CVE-2026-62125** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62125)
- **CVE-2026-62124** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62124)
- **CVE-2026-62123** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62123)
- **CVE-2026-62120** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62120)
- **CVE-2026-62090** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62090)
- **CVE-2026-62087** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62087)
- **CVE-2026-62086** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62086)
- **CVE-2026-62077** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62077)
- **CVE-2026-62076** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62076)
- **CVE-2026-62054** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62054)
- **CVE-2026-62053** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62053)
- **CVE-2026-62052** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62052)
- **CVE-2026-62051** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62051)
- **CVE-2026-62050** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62050)
- **CVE-2026-62046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62046) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-62046)
- **CVE-2026-62045** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62045) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-62045)
- **CVE-2026-62032** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62032)
- **CVE-2026-62031** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62031)
- **CVE-2026-62025** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62025)
- **CVE-2026-62024** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62024)
- **CVE-2026-62022** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62022)
- **CVE-2026-42723** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42723)
- **CVE-2026-42719** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42719)
- **CVE-2026-42718** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42718)
- **CVE-2026-42716** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42716)
- **CVE-2026-42696** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42696)
- **CVE-2026-40800** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-40800)
- **CVE-2026-39801** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-39801)
- **CVE-2026-108707** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108707)
- **CVE-2026-108598** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108598)
- **CVE-2026-108551** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108551)
- **CVE-2026-108549** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-108549)
- **CVE-2026-106610** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-106610)
- **CVE-2026-105892** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105892)
- **CVE-2026-105889** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105889)
- **CVE-2026-104803** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104803) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-104803)
- **CVE-2026-104801** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104801) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-104801)
- **CVE-2026-104398** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104398)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
