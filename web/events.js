const EVENT_LIMIT = 6;

const eventText = (value, fallback = '未確認') => {
  if (value === null || value === undefined || value === '') return fallback;
  return String(value);
};

const eventTime = (value) => {
  if (!value) return '未確認';
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return eventText(value);
  return new Intl.DateTimeFormat('zh-TW', {
    timeZone: 'Asia/Taipei',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  }).format(date);
};

const eventSafeUrl = (value) => {
  try {
    const url = new URL(value);
    return url.protocol === 'https:' ? url.toString() : null;
  } catch (_) {
    return null;
  }
};

function eventEl(tag, className, value) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (value !== undefined && value !== null) node.textContent = String(value);
  return node;
}

function eventAppend(parent, ...children) {
  for (const child of children) if (child) parent.append(child);
  return parent;
}

function eventTypeLabel(type) {
  const labels = {
    RANSOMWARE: '勒索軟體',
    ACTIVE_EXPLOITATION: '已遭利用 / 零時差',
    SUPPLY_CHAIN: '供應鏈事件',
    DATA_BREACH: '資料外洩',
    THREAT_ACTIVITY: '攻擊活動',
    VULNERABILITY_NEWS: '漏洞新聞',
  };
  return labels[type] || type || '資安事件';
}

function priorityLabel(priority) {
  const labels = {
    CRITICAL: '重大',
    HIGH: '高',
    MEDIUM: '中',
  };
  return labels[priority] || eventText(priority, '未分級');
}

function eventChip(label, className = '') {
  return eventEl('span', `security-event-chip ${className}`.trim(), label);
}

function cveEventChip(cve) {
  const value = String(cve || '').toUpperCase();
  const link = eventEl('a', 'security-event-chip cve-chip cve-chip-link', value);
  link.href = `./cve.html?cve=${encodeURIComponent(value)}`;
  link.title = `查看 ${value} CVE 詳情`;
  return link;
}

function securityEventCard(item) {
  const type = String(item.event_type || 'event').toLowerCase();
  const card = eventEl('article', `security-event-card event-${type}`);

  const top = eventEl('div', 'security-event-top');
  const badges = eventEl('div', 'security-event-badges');
  badges.append(
    eventEl('span', 'security-event-badge', eventTypeLabel(item.event_type)),
    eventEl('span', `security-event-priority priority-${String(item.priority || 'medium').toLowerCase()}`, priorityLabel(item.priority)),
  );
  const time = eventEl('span', 'security-event-time', eventTime(item.published_at));
  eventAppend(top, badges, time);

  const heading = eventEl('h3', 'security-event-title');
  const displayTitle = item.title_zh || item.title;
  const displaySummary = item.summary_zh || item.summary;
  const link = eventEl('a', '', eventText(displayTitle, '未命名事件'));
  const sourceUrl = eventSafeUrl(item.source_url);
  if (sourceUrl) {
    link.href = sourceUrl;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
  }
  heading.append(link);

  const translationLabel = item.title_zh || item.summary_zh ? ' · 繁中翻譯' : '';
  const source = eventEl('p', 'security-event-product', `${eventText(item.source_name)} · ${eventTypeLabel(item.event_type)}${translationLabel}`);
  const summary = eventEl('p', 'security-event-summary', eventText(displaySummary, '來源未提供摘要，請開啟原始報導查看細節。'));

  const chips = eventEl('div', 'security-event-facts');
  const cves = item.related_cves || [];
  for (const cve of cves.slice(0, 6)) chips.append(cveEventChip(cve));
  if (cves.length > 6) chips.append(eventChip(`+${cves.length - 6} CVE`));
  if ((item.matched_intelligence_cves || []).length) chips.append(eventChip('本日漏洞情報有追蹤', 'tracked-chip'));
  if (!cves.length) chips.append(eventChip('無 CVE 關聯'));

  const footer = eventEl('div', 'security-event-sources');
  if (sourceUrl) {
    const sourceLink = eventEl('a', '', `閱讀原文 · ${eventText(item.source_name)}`);
    sourceLink.href = sourceUrl;
    sourceLink.target = '_blank';
    sourceLink.rel = 'noopener noreferrer';
    footer.append(sourceLink);
  }

  eventAppend(card, top, heading, source, summary, chips, footer);
  return card;
}

async function fetchSecurityEvents() {
  const response = await fetch('./data/events.json', { cache: 'no-store' });
  if (!response.ok) throw new Error('無法讀取最新資安事件');
  return response.json();
}

async function fetchDailyBrief() {
  const response = await fetch('./data/daily_brief.json', { cache: 'no-store' });
  if (!response.ok) throw new Error('無法讀取每日資安事件報告');
  return response.json();
}

async function loadSecurityEvents() {
  const root = document.getElementById('securityEventList');
  const count = document.getElementById('securityEventCount');
  const freshness = document.getElementById('securityEventFreshness');
  if (!root || !count) return;

  try {
    const payload = await fetchDailyBrief();
    const events = payload.headline_events || [];
    const total = Number(payload.summary?.event_count || events.length);
    const visible = events.slice(0, EVENT_LIMIT);

    root.replaceChildren();
    count.textContent = total > visible.length ? `${visible.length} / ${total}` : `${visible.length}`;
    if (freshness) {
      const translated = Number(payload.summary?.translated_event_count || 0);
      const translationNote = translated ? ` · ${translated} 筆事件已有繁中` : '';
      freshness.textContent = payload.generated_at ? `Daily Brief 更新：${eventTime(payload.generated_at)}${translationNote}` : '等待第一次 Daily Brief';
    }

    if (!visible.length) {
      const empty = eventEl('article', 'security-event-empty');
      eventAppend(
        empty,
        eventEl('h3', '', '目前沒有符合條件的近期事件'),
        eventEl('p', '', '首頁只顯示 Daily Brief 中的重大資安新聞、攻擊事件或官方公告；不會把單純新增的 CVE 當成新聞。'),
      );
      root.append(empty);
      return;
    }

    for (const item of visible) root.append(securityEventCard(item));
  } catch (error) {
    root.replaceChildren();
    root.append(eventEl('article', 'security-event-empty', error.message || '目前無法載入重大事件'));
    count.textContent = '載入失敗';
    console.error(error);
  }
}

function searchableEventText(item) {
  return [
    item.title,
    item.title_zh,
    item.summary,
    item.summary_zh,
    item.source_name,
    item.event_type,
    ...(item.related_cves || []),
  ].filter(Boolean).join(' ').toLowerCase();
}

async function loadAllSecurityEvents() {
  const root = document.getElementById('allSecurityEventList');
  const count = document.getElementById('allEventCount');
  const freshness = document.getElementById('allEventFreshness');
  const search = document.getElementById('allEventSearch');
  const sourceSelect = document.getElementById('allEventSource');
  const filterGroup = document.getElementById('allEventTypeFilters');
  const empty = document.getElementById('allEventEmpty');
  if (!root || !count || !search || !sourceSelect || !filterGroup) return;

  try {
    const payload = await fetchSecurityEvents();
    const events = payload.items || [];
    let activeType = 'ALL';

    const sources = [...new Set(events.map((item) => item.source_name).filter(Boolean))].sort((a, b) => a.localeCompare(b));
    for (const sourceName of sources) {
      const option = document.createElement('option');
      option.value = sourceName;
      option.textContent = sourceName;
      sourceSelect.append(option);
    }

    if (freshness) {
      const translated = payload.translation?.translated_items || 0;
      const translationNote = translated ? ` · ${translated} 筆繁中翻譯` : '';
      freshness.textContent = payload.generated_at ? `更新 ${eventTime(payload.generated_at)}${translationNote}` : '等待第一次事件收集';
    }

    const render = () => {
      const query = search.value.trim().toLowerCase();
      const source = sourceSelect.value;
      const filtered = events.filter((item) => {
        if (activeType !== 'ALL' && item.event_type !== activeType) return false;
        if (source !== 'ALL' && item.source_name !== source) return false;
        if (query && !searchableEventText(item).includes(query)) return false;
        return true;
      });

      root.replaceChildren();
      count.textContent = `顯示 ${filtered.length} / ${events.length} 筆`;
      if (empty) empty.hidden = filtered.length > 0;
      for (const item of filtered) root.append(securityEventCard(item));
    };

    filterGroup.addEventListener('click', (event) => {
      const button = event.target.closest('[data-event-type]');
      if (!button) return;
      activeType = button.dataset.eventType || 'ALL';
      for (const item of filterGroup.querySelectorAll('[data-event-type]')) item.classList.toggle('active', item === button);
      render();
    });
    search.addEventListener('input', render);
    sourceSelect.addEventListener('change', render);
    render();
  } catch (error) {
    root.replaceChildren();
    root.append(eventEl('article', 'security-event-empty', error.message || '目前無法載入事件清單'));
    count.textContent = '載入失敗';
    console.error(error);
  }
}

loadSecurityEvents();
loadAllSecurityEvents();
