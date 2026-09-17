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
  const link = eventEl('a', '', eventText(item.title, '未命名事件'));
  const sourceUrl = eventSafeUrl(item.source_url);
  if (sourceUrl) {
    link.href = sourceUrl;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
  }
  heading.append(link);

  const source = eventEl('p', 'security-event-product', `${eventText(item.source_name)} · ${eventTypeLabel(item.event_type)}`);
  const summary = eventEl('p', 'security-event-summary', eventText(item.summary, '來源未提供摘要，請開啟原始報導查看細節。'));

  const chips = eventEl('div', 'security-event-facts');
  const cves = item.related_cves || [];
  for (const cve of cves.slice(0, 6)) chips.append(eventChip(cve, 'cve-chip'));
  if (cves.length > 6) chips.append(eventChip(`+${cves.length - 6} CVE`));
  if ((item.matched_intelligence_cves || []).length) chips.append(eventChip('本日漏洞情報有追蹤', 'tracked-chip'));
  if (!cves.length) chips.append(eventChip('無 CVE 關聯'));

  const footer = eventEl('div', 'security-event-sources');
  if (sourceUrl) {
    const sourceLink = eventEl('a', '', `閱讀來源 · ${eventText(item.source_name)}`);
    sourceLink.href = sourceUrl;
    sourceLink.target = '_blank';
    sourceLink.rel = 'noopener noreferrer';
    footer.append(sourceLink);
  }

  eventAppend(card, top, heading, source, summary, chips, footer);
  return card;
}

async function loadSecurityEvents() {
  const root = document.getElementById('securityEventList');
  const count = document.getElementById('securityEventCount');
  const freshness = document.getElementById('securityEventFreshness');
  if (!root || !count) return;

  try {
    const response = await fetch('./data/events.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('無法讀取最新資安事件');
    const payload = await response.json();
    const events = payload.items || [];
    const visible = events.slice(0, EVENT_LIMIT);

    root.replaceChildren();
    count.textContent = events.length > visible.length ? `${visible.length} / ${events.length}` : `${visible.length}`;
    if (freshness) freshness.textContent = payload.generated_at ? `事件更新：${eventTime(payload.generated_at)}` : '等待第一次事件收集';

    if (!visible.length) {
      const empty = eventEl('article', 'security-event-empty');
      eventAppend(
        empty,
        eventEl('h3', '', '目前沒有符合條件的近期事件'),
        eventEl('p', '', '首頁只顯示即時來源中的資安新聞、攻擊事件或官方公告；不會把單純新增的 CVE 當成新聞。'),
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

loadSecurityEvents();
