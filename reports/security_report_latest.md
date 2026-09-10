# 每日資安威脅情報簡報

## 執行摘要

* **Daily Delta 變化警示**：自上一份報告以來，系統偵測到 **8 筆新增漏洞事件（NEW_CVE）**，涵蓋 GeoVision 監視設備、Armiya 門禁系統、Joomla 外掛、SUSE 容器環境及 Google Cloud Gemini CLI。
* **整體風險佈局**：目前追蹤項目中，包含 **P1（立即處理）17 筆**、**P2（高風險排程）0 筆**、**P3（排程與監控）5 筆**，以及 8 筆屬 Watch 級別的新增漏洞。
* **最高優先處理目標**：已證實遭活躍利用（CISA KEV 列冊）且具極高風險之核心設備與系統，包含 Linux Kernel（CVE-2026-31431，EPSS 高達 99.91%）、Cisco FMC/SCC、WatchGuard Firebox、Synacor Zimbra、Citrix NetScaler 及 Fortinet 系列產品。
* **重點防護方向**：針對已列入 CISA KEV 且遭勒索軟體利用或具備 Pre-auth RCE / Auth Bypass 能力之外網暴露設備，應立即實施 24 小時內之緩解措施或更新。

---

## Daily Delta｜自上一份報告的重要變化

本次報告週期內共偵測到 **8 筆新增漏洞（NEW_CVE）**，目前風險評級均為 WATCH（風險分數 28）：

1. **CVE-2026-88285｜GeoVision Inc. GV-LPC2011/LPC2211**
   * **事實**：CVSS 9.4（CRITICAL）。PTZ 控制服務未經身份驗證即可從網路存取，允許遠端端點獲取 PTZ 資訊並發送 PTZ 或原始序列指令。
2. **CVE-2026-88278｜GeoVision Inc. GV-LPCLPC2011/2211**
   * **事實**：CVSS 9.8（CRITICAL）。未實施 WS-Security UsernameToken 新鮮度或 Nonce 重用保護，攻擊者可重放擷取的 PasswordDigest 權杖執行 ONVIF 操作。
3. **CVE-2026-8323｜Armiya Information Technologies Access Control System**
   * **事實**：CVSS 9.3（CRITICAL）。門禁系統存在未信任 URL 重定向（Open Redirect）漏洞，可被用於偽造資料來源。影響 Versiyon 2 之前版本。
4. **CVE-2026-7188｜Armiya Information Technologies Access Control System**
   * **事實**：CVSS 9.8（CRITICAL）。門禁系統存在 SQL 注入漏洞（SQL Injection）。影響 Versiyon 2 之前版本。
5. **CVE-2026-78082｜joomshaper.com SP Property extension for Joomla**
   * **事實**：CVSS 4.0 9.3（CRITICAL）。SP Property < 4.1.4 於搜尋與地圖過濾查詢時，未經轉義直接拼接請求參數，導致未經身份驗證的遠端盲 SQL 注入。
6. **CVE-2026-59679｜SUSE Container suse/kiosk/tigervnc-x11vnc:1.14-63.8**
   * **事實**：CVSS 4.0 9.2（CRITICAL）。libXfont2 堆疊邊界檢查缺陷，惡意字型伺服器可觸發攻擊者控制之 Heap 越界讀寫。
7. **CVE-2026-44950｜SUSE Container suse/kiosk/tigervnc-x11vnc:1.14-63.8**
   * **事實**：CVSS 4.0 9.5（CRITICAL）。libXfont2 複製字型位元圖時未驗證目標緩衝區邊界，重疊偏移量可導致可控內容之 Heap Buffer Overflow。
8. **CVE-2026-13745｜Google Cloud Gemini CLI**
   * **事實**：CVSS 4.0 9.2（CRITICAL）。Gemini CLI 與 GitHub Action 可透過未信任之本地 `.env` 檔案覆寫 `GEMINI_CLI_HOME`，實現任意程式碼執行。

---

## P1｜立即優先處理

以下列出最高風險、已確認遭野生利用（Active Exploitation / CISA KEV）的 10 項關鍵 P1 漏洞：

### 1. CVE-2026-31431｜Linux Kernel
* **Vendor / Product**: Linux / Kernel
* **已驗證風險 Facts**: CVSS 3.1 7.8（HIGH）、EPSS 0.99907（百分位 99.97%）、CISA KEV 已列冊（截止日 2026-05-15）、利用狀態為 active。
* **受影響版本**: 未確認。
* **為何優先**: 跨領域資源轉移錯誤漏洞，EPSS 利用機率極高（>99.9%），且已被證實於野生環境中活躍利用，可導致在地權限提升（Privilege Escalation）。
* **建議處置**: 依照 原廠/社群 指示套用修補程式；雲端服務請依 BOD 22-01 指引辦理；若無修補方案應考量停用。

### 2. CVE-2026-20079｜Cisco Secure FMC & SCC Firewall Management
* **Vendor / Product**: Cisco / Secure Firewall Management Center (FMC) & Security Cloud Control (SCC)
* **已驗證風險 Facts**: CVSS 3.1 10.0（CRITICAL）、EPSS 0.35946（百分位 98.37%）、CISA KEV 已列冊（截止日 2026-09-12）、利用狀態為 active。
* **受影響版本**: 未確認。
* **為何優先**: CVSS 達滿分 10.0，未授權遠端攻擊者可繞過身份驗證，在受影響設備上執行腳本並取得底層 OS 的 Root 權限。
* **建議處置**: 依 Cisco 官方通告套用修補措施，並遵循 CISA BOD 26-04 規範進行鑑識排查與網際網路暴露評估。

### 3. CVE-2025-14733｜WatchGuard Firebox
* **Vendor / Product**: WatchGuard / Firebox (Fireware OS)
* **已驗證風險 Facts**: CVSS 4.0 9.3（CRITICAL）、EPSS 0.2651（百分位 97.89%）、CISA KEV 已列冊、已知遭勒索軟體活動利用（Ransomware: Known）、利用狀態為 active。
* **受影響版本**: 未確認。
* **為何優先**: 位於 Fireware OS `iked` 程序之 Out-of-bounds Write 漏洞，影響外網 VPN 服務（IKEv2），且已被勒索軟體集團用於入侵。
* **建議處置**: 立即更新修補，並排查所有暴露於網際網路之 Firebox 設備是否有遭入侵跡象。

### 4. CVE-2022-41352｜Synacor Zimbra Collaboration Suite (ZCS)
* **Vendor / Product**: Synacor / Zimbra Collaboration Suite
* **已驗證風險 Facts**: CVSS 3.1 9.8（CRITICAL）、EPSS 0.95478（百分位 99.87%）、CISA KEV 已列冊、已知遭勒索軟體利用、利用狀態為 active。
* **受影響版本**: 未確認。
* **為何優先**: 可透過 `cpio` 套件上傳任意檔案，取得其他使用者帳戶權限，EPSS 極高且持續有勒索軟體攻擊記錄。
* **建議處置**: 依原廠安全指南更新 Zimbra 及相關系統解壓縮套件。

### 5. CVE-2022-37969｜Microsoft Windows CLFS Driver
* **Vendor / Product**: Microsoft / Windows
* **已驗證風險 Facts**: CVSS 3.1 7.8（HIGH）、EPSS 0.28275（百分位 98.00%）、CISA KEV 已列冊、已知遭勒索軟體利用、利用狀態為 active。
* **受影響版本**: 未確認。
* **為何優先**: 通用日誌檔案系統（CLFS）驅動程式漏洞，常被勒索軟體作為取得系統最高權限（SYSTEM）的後續利用鏈。
* **建議處置**: 實施 Windows 定期安全更新（Patch Tuesday）。

### 6. CVE-2016-7255｜Microsoft Win32k
* **Vendor / Product**: Microsoft / Win32k
* **已驗證風險 Facts**: CVSS 3.1 7.8（HIGH）、EPSS 未確認（null）、CISA KEV 已列冊、已知遭勒索軟體利用、利用狀態為 active。
* **受影響版本**: 未確認。
* **為何優先**: 核心模式驅動程式記憶體物件處理不當，允許攻擊者以 Kernel 模式執行程式碼，屬歷史但仍遭利用之特權提升漏洞。
* **建議處置**: 確保舊版 Windows 系統已套用相關安全更新或升級至受支援版本。

### 7. CVE-2016-4117｜Adobe Flash Player
* **Vendor / Product**: Adobe / Flash Player
* **已驗證風險 Facts**: CVSS 3.1 9.8（CRITICAL）、EPSS 未確認（null）、CISA KEV 已列冊、已知遭勒索軟體利用、利用狀態為 active。
* **受影響版本**: 未確認。
* **為何優先**: 遠端程式碼執行漏洞。產品已終止支援（EOL），若殘留於企業環境中將構成嚴重資安破口。
* **建議處置**: CISA 強制要求：該產品已 EOL，若仍在使用中必須立即解除安裝並斷開網路連接。

### 8. CVE-2026-86218｜N-able N-central
* **Vendor / Product**: N-able / N-central
* **已驗證風險 Facts**: CVSS 4.0 10.0（CRITICAL）、EPSS 0.00744、CISA KEV 已列冊（截止日 2026-09-11）、利用狀態為 active。
* **受影響版本**: 未確認。
* **為何優先**: 託管服務供應商（MSP）常用的管理工具，存在 Pre-authentication RCE（驗證前遠端程式碼執行），已被野生利用。
* **建議處置**: 立即套用 N-able 官方 Hotfix，並對 N-central 伺服器進行鑑識日誌排查。

### 9. CVE-2026-19490｜Citrix NetScaler ADC & Gateway
* **Vendor / Product**: Citrix / NetScaler
* **已驗證風險 Facts**: CVSS 4.0 9.3（CRITICAL）、EPSS 0.03372、CISA KEV 已列冊（截止日 2026-09-12）、利用狀態為 active。
* **受影響版本**: 未確認。
* **為何優先**: 當 NetScaler 設定為 AAA 虛擬伺服器或 Gateway（SSL VPN/ICA/CVPN/RDP Proxy）時，未授權遠端攻擊者可繞過身份驗證。
* **建議處置**: 立即安裝 Citrix 官方修補套件，檢視 Gateway 登入日誌與異常連線。

### 10. CVE-2025-25249｜Fortinet Multiple Products
* **Vendor / Product**: Fortinet / FortiOS, FortiSwitchManager, FortiSASE
* **已驗證風險 Facts**: CVSS 3.1 9.8（CRITICAL）、EPSS 0.00759、CISA KEV 已列冊（截止日 2026-09-12）、利用狀態為 active。
* **受影響版本**: 未確認。
* **為何優先**: Heap-based Buffer Overflow 漏洞，攻擊者可透過特製封包遠端執行未授權程式碼或指令。
* **建議處置**: 升級 FortiOS、FortiSwitchManager 與 FortiSASE 至原廠建議之安全版本。

---

### 其他 P1 追蹤項目一覽表

| CVE 編號 | Vendor / Product | CVSS | CISA KEV / 狀態 | 摘要說明 | 建議處置 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CVE-2026-87491** | Google / Chromium V8 | 8.8 (HIGH) | Listed / Active | V8 堆疊越界寫入，可經由特製網頁突破 Sandbox 執行程式碼 | 更新 Chrome / Edge / Opera 等瀏覽器 |
| **CVE-2026-85880** | Microsoft / Windows ALPC | 7.8 (HIGH) | Listed / Active | ALPC Heap Buffer Overflow，本地特權提升 | 實施 Windows 安全更新 |
| **CVE-2026-81963** | Microsoft / Windows Update Stack | 7.8 (HIGH) | Listed / Active | Update Stack 連結追蹤漏洞，本地提升至 SYSTEM | 實施 Windows 安全更新 |
| **CVE-2026-75650** | Adobe / Commerce & Magento | 10.0 (CRITICAL) | Listed / Active | 模板引擎未適當過濾特殊元素，可執行任意程式碼 | 更新 Adobe Commerce / Magento 系統 |
| **CVE-2025-67038** | Lantronix / EDS5000 | 9.3 (CRITICAL) | Listed / Active | 使用者名稱參數 OS 指令注入，取得 Root 權限 | 更新 EDS5000 韌體或限制存取 |
| **CVE-2026-85046** | Google / Chromium V8 | 8.8 (HIGH) | Listed / Active | V8 Type Confusion 漏洞，遠端程式碼執行 | 更新 Chromium 架構瀏覽器 |
| **CVE-2025-38352** | Linux / Kernel | 7.8 (HIGH) | Listed / Active | TOCTOU 競態條件漏洞，影響機密性與完整性 | 依各 Linux 發行版套用核心更新 |

---

## P2 / P3｜排程處理與監控

目前無 P2 項目。以下為 **P3 項目（共 5 筆）** 與 **Daily Delta 新增監控項目（共 8 筆）**。
P3 項目具備 PoC 或高 CVSS/EPSS，但尚未列入 CISA KEV，應納入常規修補排程與威脅監控。

| CVE 編號 | Priority / Risk Score | Vendor / Product | CVSS / EPSS | 狀態 / 理由 | 建議處置 / 監控理由 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CVE-2026-43284** | P3 (47) | Linux / Kernel | CVSS 8.8 / EPSS 93.24% | PoC 已公開 | ESP-in-UDP 封包解密不當；EPSS 高且有 PoC，需排程修補核心 |
| **CVE-2023-52251** | P3 (47) | provectus / kafka-ui | CVSS 8.8 / EPSS 86.84% | PoC 已公開 | 專案自 2024 年停更且**無官方修補版**；須限制 `/api/clusters` 存取 |
| **CVE-2026-87930** | P3 (38) | MaxSite / MaxSite CMS | CVSS 9.2 / EPSS 未確認 | PoC 已公開，近期發布 | Session Cookie 反序列化漏洞，攻擊者可注入 PHP 物件，排程修補 |
| **CVE-2026-79576** | P3 (38) | 未確認 / Digital-Infrastructure SSO | CVSS 9.8 / EPSS 0.33% | PoC 已公開，近期發布 | SSO 組件允許無密碼身份驗證為 Admin，建議限制存取並排查 |
| **CVE-2026-79574** | P3 (38) | 未確認 / mpush | CVSS 9.8 / EPSS 0.17% | PoC 已公開，近期發布 | Gateway server 廣播訊息觸發 RCE，排程關閉暴露埠口或修補 |
| **CVE-2026-88285** | WATCH (28) | GeoVision / GV-LPC2011/LPC2211 | CVSS 9.4 / EPSS 未確認 | Delta 新增漏洞 | 未授權 PTZ 控制服務暴露；隔離監視設備網路存取 |
| **CVE-2026-88278** | WATCH (28) | GeoVision / GV-LPC2011/LPC2211 | CVSS 9.8 / EPSS 未確認 | Delta 新增漏洞 | WS-Security 重放攻擊漏洞；檢查 ONVIF 介面驗證機制 |
| **CVE-2026-8323** | WATCH (28) | Armiya / Access Control System | CVSS 9.3 / EPSS 未確認 | Delta 新增漏洞 | Open Redirect 漏洞（Versiyon < 2）；納入門禁系統修補清單 |
| **CVE-2026-7188** | WATCH (28) | Armiya / Access Control System | CVSS 9.8 / EPSS 未確認 | Delta 新增漏洞 | SQL Injection 漏洞（Versiyon < 2）；限制門禁系統 Web 介面存取 |
| **CVE-2026-78082** | WATCH (28) | joomshaper.com / SP Property (Joomla) | CVSS 9.3 / EPSS 未確認 | Delta 新增漏洞 | Unauthenticated SQLi（< 4.1.4）；更新外網 Joomla 套件 |
| **CVE-2026-59679** | WATCH (28) | SUSE / Container tigervnc-x11vnc | CVSS 9.2 / EPSS 未確認 | Delta 新增漏洞 | libXfont2 堆疊 OOB Read/Write；更新容器基底映像檔 |
| **CVE-2026-44950** | WATCH (28) | SUSE / Container tigervnc-x11vnc | CVSS 9.5 / EPSS 未確認 | Delta 新增漏洞 | libXfont2 Heap Buffer Overflow；更新容器基底映像檔 |
| **CVE-2026-13745** | WATCH (28) | Google Cloud / Gemini CLI | CVSS 9.2 / EPSS 未確認 | Delta 新增漏洞 | `.env` 覆寫 RCE；檢查 CI/CD 與開發環境 `.env` 存取權限 |

---

## 建議行動

### 24 小時內（緊急處置）
1. **外網邊界設備防護**：
   * 針對 **Cisco FMC/SCC**（CVE-2026-20079）、**Citrix NetScaler**（CVE-2026-19490）、**WatchGuard Firebox**（CVE-2025-14733）、**Fortinet 系列**（CVE-2025-25249）等邊界系統，若暴露於網際網路，立即實施官方修補或存取控制清單（ACL）隔離。
2. **清除高風險廢置組件**：
   * 徹底檢查環境中是否殘留 **Adobe Flash Player**（CVE-2016-4117），若存在應強制移除並斷網。
3. **MSP 管理工具防禦**：
   * 使用 **N-able N-central**（CVE-2026-86218）之單位，立即安裝 Hotfix 4 並排查有無異常 RCE 日誌。

### 本週內（排程修補與處置）
1. **作業系統與核心更新**：
   * 更新 **Linux Kernel**（CVE-2026-31431、CVE-2025-38352）與 **Windows 系統**（CVE-2022-37969、CVE-2026-85880、CVE-2026-81963）。
2. **應用系統與電商平台更新**：
   * 完成 **Zimbra ZCS**（CVE-2022-41352）與 **Adobe Commerce / Magento**（CVE-2026-75650）安全更新。
   * 針對無官方修補程式之 **provectus kafka-ui**（CVE-2023-52251），實施嚴格網路隔離（如限制內網特定 IP 存取）。
3. **用戶端端點軟體更新**：
   * 推送 **Chromium 架構瀏覽器**（Chrome/Edge/Opera）更新，修補 V8 漏洞（CVE-2026-87491、CVE-2026-85046）。

### 持續監控（長遠防護）
1. **OT / 物聯網 / 門禁設備隔離**：
   * 針對 GeoVision 攝影機（CVE-2026-88285、CVE-2026-88278）、Armiya 門禁系統（CVE-2026-8323、CVE-2026-7188）、Lantronix 串口伺服器（CVE-2025-67038），一律劃分至獨立管理 VLAN，禁止直連網際網路。
2. **開發與容器安全監控**：
   * 檢視 CI/CD 流程中的 **Google Cloud Gemini CLI**（CVE-2026-13745）與 **SUSE 容器映像檔**（CVE-2026-59679、CVE-2026-44950），建立 `.env` 檔與第三方套件掃描機制。

---

## 產業影響

* **金融業與高科技製造業**：
  * **邊界與 VPN 威脅**：Citrix NetScaler、WatchGuard Firebox 及 Fortinet 為台灣金融與科技大廠常用之遠端辦公與 VPN 架構。若遭 Auth Bypass 或 Buffer Overflow 突破，攻擊者可進入內網並發動橫向移動。
  * **供應鏈風險**：N-able N-central 為託管服務（MSP）主要工具，若遭入侵可能演變為跨企業之供應鏈攻擊。
* **政府機關與關鍵基礎設施（CI）**：
  * **Linux 伺服器威脅**：Linux Kernel 漏洞（CVE-2026-31431）利用率極高，影響廣泛部署於政府與 CI 領域的 Linux 伺服器與雲端基礎設施。
  * **物理安全系統漏洞**：GeoVision 監視器與 Armiya 門禁系統漏洞凸顯 OT/IoT 設備防護死角，若連接至行政網路可能成為進入內網的跳板。
* **電子商務與零售業**：
  * **平台遭控風險**：Adobe Commerce / Magento（CVE-2026-75650）及 Joomla 外掛（CVE-2026-78082）之 RCE 與 SQLi 漏洞，易被用於竊取消費者支付卡片資訊或植入惡意腳本。

---

## 資料品質與未確認事項

1. **受影響與修補版本缺失**：
   * 輸入 Fact 中，大部分 CVE（如 CVE-2026-31431、CVE-2026-20079、CVE-2025-14733 等）未提供精確之「受影響版本」與「修補版本號」，需各單位資安人員至原廠 Advisory 進行二次確認。
2. **EPSS 數值缺漏**：
   * 部分舊漏洞或特定組件漏洞（如 CVE-2016-7255、CVE-2016-4117、CVE-2026-75650、CVE-2025-67038 及 Daily Delta 部分項目）之 EPSS 數據為 `null`，無法僅憑 EPSS 評估動態風險，必須以 CISA KEV 狀態為準。
3. **廠商資訊未確認**：
   * 部分漏洞（如 CVE-2023-52251、CVE-2026-79576、CVE-2026-79574）之 Vendor / Product 欄位在 Fact 中標示為 `null`，其詳細維護狀態（如 provectus kafka-ui 專案已停止維護）需由營運團隊進一步追蹤。

> **資料來源模式：Verified facts only。** 本次 Google Search grounding 未啟用；報告僅依 CISA KEV、NVD、FIRST EPSS 與 deterministic risk/delta 輸入進行整理分析，未確認資訊不以模型記憶補足。

---

## 可驗證資料來源

- **CVE-2026-31431** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-31431) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-31431) · [Vendor / Advisory (lore.kernel.org)](https://lore.kernel.org/linux-cve-announce/2026042214-CVE-2026-31431-3d65@gregkh/) · [Vendor / Advisory (xint.io)](https://xint.io/blog/copy-fail-linux-distributions#the-fix-6) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/about/)
- **CVE-2026-88285** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88285)
- **CVE-2026-88278** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88278)
- **CVE-2026-8323** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-8323)
- **CVE-2026-7188** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-7188)
- **CVE-2026-78082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-78082)
- **CVE-2026-59679** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-59679)
- **CVE-2026-44950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-44950)
- **CVE-2026-13745** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-13745)
- **CVE-2026-20079** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-20079) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-20079) · [Vendor / Advisory (sec.cloudapps.cisco.com)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-14733** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-14733) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-14733) · [Vendor / Advisory (watchguard.com)](https://www.watchguard.com/wgrd-psirt/advisory/wgsa-2025-00027)
- **CVE-2022-41352** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-41352) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2022-41352) · [Vendor / Advisory (wiki.zimbra.com)](https://wiki.zimbra.com/wiki/Security_Center)
- **CVE-2022-37969** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-37969) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2022-37969) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-37969)
- **CVE-2016-7255** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-7255) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- **CVE-2016-4117** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2016-4117) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- **CVE-2026-86218** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86218) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86218) · [Vendor / Advisory (status.n-able.com)](https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/) · [Vendor / Advisory (me.n-able.com)](https://me.n-able.com/s/security-advisory/aArVy0000002Ld3KAE/cve202686218-preauthentication-remote-code-execution) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-19490** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-19490) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-19490) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-25249** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-25249) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-25249) · [Vendor / Advisory (fortiguard.fortinet.com)](https://fortiguard.fortinet.com/psirt/FG-IR-25-084) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-87491** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87491) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-87491) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85880** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85880) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85880) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-81963** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-81963) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-81963) · [Vendor / Advisory (msrc.microsoft.com)](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-75650** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-75650) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (helpx.adobe.com)](https://helpx.adobe.com/security/products/magento/apsb26-146.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-67038** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-67038) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (ltrxdev.atlassian.net)](https://ltrxdev.atlassian.net/wiki/spaces/LTRXTS/pages/2538438657/Latest+Firmware+for+the+EDS5000+series+EDS5008+EDS5016+EDS5032) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-85046** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85046) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-85046) · [Vendor / Advisory (chromereleases.googleblog.com)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2025-38352** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-38352) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2025-38352) · [Vendor / Advisory (git.kernel.org)](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=2c72fe18cc5f9f1750f5bc148cf1c94c29e106ff) · [Vendor / Advisory (source.android.com)](https://source.android.com/docs/security/bulletin/2025-09-01)
- **CVE-2026-43284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-43284) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-43284)
- **CVE-2023-52251** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-52251) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2023-52251)
- **CVE-2026-87930** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-87930)
- **CVE-2026-79576** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79576) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79576)
- **CVE-2026-79574** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79574) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-79574)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
