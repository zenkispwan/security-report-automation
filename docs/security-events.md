# Security Events 首頁規則

首頁採 **News / Incident first**，不再把新 CVE 清單當成資安事件。

## 顯示條件

事件來源目前優先使用：

- BleepingComputer RSS
- SecurityWeek RSS
- CISA Advisories / News（來源可用時）

Collector 會抓取近期來源、分類事件、保留來源 URL，並從來源標題、摘要或文章本文抽取 `CVE-YYYY-NNNN`。

### CVE 關聯規則

CVE 只在來源文章／公告實際出現該 CVE 時才會掛到事件卡：

```text
新聞 / 官方公告
       ↓
事件分類
       ↓
文章文字是否明確提到 CVE？
       ├─ 是 → related_cves
       └─ 否 → 不顯示 CVE
```

NVD、CISA KEV、FIRST EPSS 中出現新的漏洞，不代表它自動成為首頁事件。完整漏洞資料仍保留在折疊的「技術漏洞資料」區。

## 事件類型

目前分類：

- `RANSOMWARE`
- `ACTIVE_EXPLOITATION`
- `SUPPLY_CHAIN`
- `DATA_BREACH`
- `THREAT_ACTIVITY`
- `VULNERABILITY_NEWS`

首頁最多顯示 6 筆，完整 `data/events.json` 最多保留 20 筆近期事件。

## Trust boundary

- Feed / article / advisory 負責事件 Facts。
- CVE 關聯由 deterministic regex 從來源文字抽取。
- 未在來源出現的 CVE 不猜測、不補掛。
- LLM 可在後續階段產生繁體中文摘要、產業影響與處置建議，但不得新增來源未支持的 CVE、利用狀態、受影響版本或事件事實。
- 若所有事件來源暫時失敗，保留上一份已驗證 `data/events.json`，避免用空白或模型生成內容覆蓋最後可信事件。
