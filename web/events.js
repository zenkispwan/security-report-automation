const EVENT_LIMIT = 6;

const EVENT_WEIGHTS = {
  RANSOMWARE_USE_CHANGED: 100,
  EXPLOITATION_CHANGED: 95,
  NEW_KEV: 90,
  EPSS_INCREASED: 80,
  NEW_CVE: 50,
};

const eventText = (value, fallback = '未確認') => {
  if (value === null || value === undefined || value === '') return fallback;
  return String(value);
};

const eventPercent = (value) => {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return '未確認';
  return `${(Number(value) * 100).toFixed(2)}%`;
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
    NEW_KEV: '新增 CISA KEV',
    EPSS_INCREASED: 'EPSS 顯著上升',
    EXPLOITATION_CHANGED: '利用狀態變更',
    RANSOMWARE_USE_CHANGED: '勒索軟體關聯變更',
    NEW_CVE: '新高風險 CVE',
  };
  return labels[type] || type || '重大狀態變化';
}

function exploitationLabel(status) {
  const labels = {
    known_exploited: '已知遭利用',
    active: '活躍利用',
    poc: '公開 PoC',
    none: '未觀測利用',
    unconfirmed: '未確認',
  };
  return labels[status] || eventText(status);
}

function shouldHighlight(item, event) {
  const type = event?.type;
  if (['NEW_KEV', 'EPSS_INCREASED', 'EXPLOITATION_CHANGED', 'RANSOMWARE_USE_CHANGED'].includes(type)) return true;
  if (type !== 'NEW_CVE') return false;

  const facts = item.facts || {};
  const severity = facts.cvss?.severity;
  const exploitation = facts.exploitation_status?.status;
  const priority = item.risk?.priority;
  return severity === 'CRITICAL' || ['known_exploited', 'active', 'poc'].includes(exploitation) || ['P1', 'P2'].includes(priority);
}

function flattenSecurityEvents(delta) {
  const rows = [];
  for (const item of delta.items || []) {
    for (const event of item.events || []) {
      if (!shouldHighlight(item, event)) continue;
      rows.push({ item, event });
    }
  }

  return rows.sort((a, b) => {
    const weight = (EVENT_WEIGHTS[b.event.type] || 0) - (EVENT_WEIGHTS[a.event.type] || 0);
    if (weight) return weight;
    const risk = Number(b.item.risk?.score || 0) - Number(a.item.risk?.score || 0);
    if (risk) return risk;
    const bTime = new Date(b.item.facts?.updated_time || 0).getTime() || 0;
    const aTime = new Date(a.item.facts?.updated_time || 0).getTime() || 0;
    return bTime - aTime;
  });
}

function eventNarrative(item, event) {
  const facts = item.facts || {};
  const cve = item.cve || facts.cve || '未確認 CVE';
  const exploitation = exploitationLabel(facts.exploitation_status?.status);

  switch (event.type) {
    case 'NEW_KEV':
      return `CISA 已將 ${cve} 納入 Known Exploited Vulnerabilities；目前利用狀態為「${exploitation}」。`;
    case 'EPSS_INCREASED': {
      const from = eventPercent(event.from);
      const to = eventPercent(event.to);
      const delta = Number(event.delta);
      const deltaText = Number.isFinite(delta) ? `，增加 ${(delta * 100).toFixed(2)} 個百分點` : '';
      return `${cve} 的 EPSS 由 ${from} 上升至 ${to}${deltaText}。這代表利用機率訊號升高，但不等同已確認遭利用。`;
    }
    case 'EXPLOITATION_CHANGED':
      return `${cve} 的 exploitation status 由「${exploitationLabel(event.from)}」變更為「${exploitationLabel(event.to)}」。`;
    case 'RANSOMWARE_USE_CHANGED':
      return `${cve} 的 CISA known ransomware campaign use 由「${eventText(event.from)}」變更為「${eventText(event.to)}」。`;
    case 'NEW_CVE': {
      const cvss = facts.cvss || {};
      const cvssText = cvss.score !== null && cvss.score !== undefined ? `CVSS ${cvss.score} ${eventText(cvss.severity, '')}`.trim() : 'CVSS 未確認';
      return `${cve} 新進入本次觀測範圍；${cvssText}，利用狀態為「${exploitation}」。`;
    }
    default:
      return `${cve} 出現新的 verified state change。`;
  }
}

function eventSourceLinks(facts) {
  const box = eventEl('div', 'security-event-sources');
  const candidates = [
    ['NVD', facts?.provenance?.nvd || facts?.source_url],
    ['CISA KEV', facts?.provenance?.cisa_kev],
    ['FIRST EPSS', facts?.provenance?.epss],
  ];
  const seen = new Set();
  for (const [label, raw] of candidates) {
    const url = eventSafeUrl(raw);
    if (!url || seen.has(url)) continue;
    seen.add(url);
    const link = eventEl('a', '', label);
    link.href = url;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    box.append(link);
  }
  return box;
}

function eventFacts(item, event) {
  const facts = item.facts || {};
  const row = eventEl('div', 'security-event-facts');
  const values = [];

  values.push(`Priority ${eventText(item.risk?.priority, 'WATCH')} · Score ${eventText(item.risk?.score)}`);
  if (facts.cvss?.score !== null && facts.cvss?.score !== undefined) values.push(`CVSS ${facts.cvss.score} ${eventText(facts.cvss?.severity, '')}`.trim());
  if (facts.epss !== null && facts.epss !== undefined) values.push(`EPSS ${eventPercent(facts.epss)}`);
  if (facts.cisa_kev?.listed) values.push(`KEV due ${eventText(facts.cisa_kev?.due_date)}`);
  if (event.type === 'EPSS_INCREASED' && event.delta !== null && event.delta !== undefined) values.push(`EPSS Δ +${(Number(event.delta) * 100).toFixed(2)} pp`);

  for (const value of values) row.append(eventEl('span', '', value));
  return row;
}

function securityEventCard(item, event) {
  const facts = item.facts || {};
  const card = eventEl('article', `security-event-card event-${String(event.type || 'change').toLowerCase()}`);

  const top = eventEl('div', 'security-event-top');
  const badge = eventEl('span', 'security-event-badge', eventTypeLabel(event.type));
  const time = eventEl('span', 'security-event-time', `更新 ${eventTime(facts.updated_time)}`);
  eventAppend(top, badge, time);

  const heading = eventEl('h3', 'security-event-title');
  const cveLink = eventEl('a', '', item.cve || facts.cve || '未確認 CVE');
  const cveUrl = eventSafeUrl(facts.source_url || facts.provenance?.nvd);
  if (cveUrl) {
    cveLink.href = cveUrl;
    cveLink.target = '_blank';
    cveLink.rel = 'noopener noreferrer';
  }
  heading.append(cveLink);

  const product = eventEl('p', 'security-event-product', `${eventText(facts.vendor)} / ${eventText(facts.product)}`);
  const narrative = eventEl('p', 'security-event-summary', eventNarrative(item, event));

  eventAppend(card, top, heading, product, narrative, eventFacts(item, event), eventSourceLinks(facts));
  return card;
}

async function loadSecurityEvents() {
  const root = document.getElementById('securityEventList');
  const count = document.getElementById('securityEventCount');
  if (!root || !count) return;

  try {
    const response = await fetch('./data/delta.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('無法讀取 verified Daily Delta');
    const delta = await response.json();
    const events = flattenSecurityEvents(delta);
    const visible = events.slice(0, EVENT_LIMIT);

    root.replaceChildren();
    count.textContent = events.length > visible.length ? `${visible.length} / ${events.length}` : `${visible.length}`;

    if (!visible.length) {
      const empty = eventEl('article', 'security-event-empty');
      eventAppend(empty, eventEl('h3', '', '目前沒有高訊號重大事件'), eventEl('p', '', 'Daily Delta 仍會保留完整變化；系統不會為了填滿版面而製造事件。'));
      root.append(empty);
      return;
    }

    for (const row of visible) root.append(securityEventCard(row.item, row.event));
  } catch (error) {
    root.replaceChildren();
    root.append(eventEl('article', 'security-event-empty', error.message || '目前無法載入重大事件'));
    count.textContent = '載入失敗';
    console.error(error);
  }
}

loadSecurityEvents();
