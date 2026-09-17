const cveText = (value, fallback = '未確認') => {
  if (value === null || value === undefined || value === '') return fallback;
  return String(value);
};

const cveTime = (value) => {
  if (!value) return '未確認';
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return cveText(value);
  return new Intl.DateTimeFormat('zh-TW', {
    timeZone: 'Asia/Taipei', year: 'numeric', month: '2-digit', day: '2-digit',
    hour: '2-digit', minute: '2-digit', hour12: false,
  }).format(date);
};

const cvePercent = (value) => {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return '未確認';
  return `${(Number(value) * 100).toFixed(2)}%`;
};

const cveSafeUrl = (value) => {
  try {
    const url = new URL(value);
    return url.protocol === 'https:' ? url.toString() : null;
  } catch (_) {
    return null;
  }
};

function cveEl(tag, className, value) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (value !== undefined && value !== null) node.textContent = String(value);
  return node;
}

function cveAppend(parent, ...children) {
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

function sourceLink(label, rawUrl) {
  const url = cveSafeUrl(rawUrl);
  if (!url) return null;
  const link = cveEl('a', '', label);
  link.href = url;
  link.target = '_blank';
  link.rel = 'noopener noreferrer';
  return link;
}

function factCard(label, value, note = '') {
  const card = cveEl('article', 'cve-fact-card');
  card.append(cveEl('span', 'cve-fact-label', label), cveEl('strong', 'cve-fact-value', value));
  if (note) card.append(cveEl('span', 'cve-fact-note', note));
  return card;
}

function relatedEventCard(item) {
  const type = String(item.event_type || 'event').toLowerCase();
  const card = cveEl('article', `security-event-card event-${type}`);
  const top = cveEl('div', 'security-event-top');
  const badges = cveEl('div', 'security-event-badges');
  badges.append(cveEl('span', 'security-event-badge', eventTypeLabel(item.event_type)));
  if (item.priority) badges.append(cveEl('span', `security-event-priority priority-${String(item.priority).toLowerCase()}`, item.priority === 'CRITICAL' ? '重大' : item.priority));
  cveAppend(top, badges, cveEl('span', 'security-event-time', cveTime(item.published_at)));

  const heading = cveEl('h3', 'security-event-title');
  const link = cveEl('a', '', item.title_zh || item.title || '未命名事件');
  const url = cveSafeUrl(item.source_url);
  if (url) {
    link.href = url;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
  }
  heading.append(link);
  const source = cveEl('p', 'security-event-product', `${cveText(item.source_name)} · ${eventTypeLabel(item.event_type)}${item.title_zh || item.summary_zh ? ' · 繁中翻譯' : ''}`);
  const summary = cveEl('p', 'security-event-summary', item.summary_zh || item.summary || '來源未提供摘要。');
  const footer = cveEl('div', 'security-event-sources');
  const original = sourceLink(`閱讀原文 · ${cveText(item.source_name)}`, item.source_url);
  if (original) footer.append(original);
  cveAppend(card, top, heading, source, summary, footer);
  return card;
}

function renderUnknownCve(cve, events) {
  document.getElementById('cvePageTitle').textContent = cve;
  document.getElementById('cvePageSubtitle').textContent = '此 CVE 由目前事件來源提到，但尚未進入本日 prioritized intelligence 清單。';
  document.getElementById('cvePriorityBadge').textContent = '未列入本日優先清單';

  const summary = document.getElementById('cveSummaryCard');
  const title = cveEl('h3', '', `${cve} · 技術資料未納入本日 intelligence`);
  const text = cveEl('p', 'cve-description', '目前不補猜 Vendor、Product、CVSS、EPSS 或漏洞描述。可查看下方實際提到此 CVE 的事件，或前往 NVD 取得官方漏洞紀錄。');
  const links = cveEl('div', 'security-event-sources');
  links.append(sourceLink('查看 NVD', `https://nvd.nist.gov/vuln/detail/${encodeURIComponent(cve)}`));
  cveAppend(summary, title, text, links);
  renderRelatedEvents(cve, events);
}

function renderKnownCve(cve, item, enrichment, events) {
  const facts = item.facts || {};
  const risk = item.risk || {};
  const cvss = facts.cvss || {};
  const zh = enrichment || {};

  document.title = `${cve}｜CVE 詳情`;
  document.getElementById('cvePageTitle').textContent = cve;
  document.getElementById('cvePageSubtitle').textContent = `${cveText(facts.vendor)} / ${cveText(facts.product)}`;
  document.getElementById('cvePriorityBadge').textContent = `${cveText(risk.priority, 'WATCH')} · Score ${cveText(risk.score)}`;
  document.getElementById('cveUpdatedAt').textContent = `更新：${cveTime(facts.updated_time)}`;

  const summary = document.getElementById('cveSummaryCard');
  const translated = Boolean(zh.title_zh || zh.description_zh);
  const heading = cveEl('h3', '', zh.title_zh || facts.title || cve);
  const sourceLine = cveEl('p', 'security-event-product', `${cveText(facts.vendor)} · ${cveText(facts.product)}${translated ? ' · 繁中翻譯' : ''}`);
  const description = cveEl('p', 'cve-description', zh.description_zh || facts.description || '來源未提供漏洞描述。');
  cveAppend(summary, heading, sourceLine, description);

  if (translated && (facts.title || facts.description)) {
    const original = document.createElement('details');
    original.className = 'cve-original-text';
    original.append(cveEl('summary', '', '查看英文原始說明'));
    const body = cveEl('div', 'cve-original-body');
    if (facts.title) body.append(cveEl('strong', '', facts.title));
    if (facts.description) body.append(cveEl('p', '', facts.description));
    original.append(body);
    summary.append(original);
  }

  const sources = cveEl('div', 'security-event-sources');
  const candidates = [
    ['NVD', facts.provenance?.nvd || facts.source_url],
    ['CISA KEV', facts.provenance?.cisa_kev],
    ['FIRST EPSS', facts.provenance?.epss],
  ];
  const seen = new Set();
  for (const [label, raw] of candidates) {
    const url = cveSafeUrl(raw);
    if (!url || seen.has(url)) continue;
    seen.add(url);
    sources.append(sourceLink(label, url));
  }
  summary.append(sources);

  const grid = document.getElementById('cveFactGrid');
  grid.replaceChildren(
    factCard('Priority / Score', `${cveText(risk.priority, 'WATCH')} / ${cveText(risk.score)}`),
    factCard('CVSS', cvss.score !== null && cvss.score !== undefined ? `${cvss.score} ${cveText(cvss.severity, '')}`.trim() : '未確認', cveText(cvss.version, '')),
    factCard('EPSS', cvePercent(facts.epss), `Percentile ${cvePercent(facts.epss_percentile)}`),
    factCard('CISA KEV', facts.cisa_kev?.listed ? '已列入' : '未列入', facts.cisa_kev?.listed ? `Added ${cveText(facts.cisa_kev.date_added)} · Due ${cveText(facts.cisa_kev.due_date)}` : ''),
    factCard('Exploitation', cveText(facts.exploitation_status?.status), cveText(facts.exploitation_status?.source, '')),
    factCard('Ransomware use', cveText(facts.cisa_kev?.known_ransomware_campaign_use)),
    factCard('CWE', (facts.cwes || []).join(', ') || '未確認'),
    factCard('Published / Updated', `${cveTime(facts.published_time)} / ${cveTime(facts.updated_time)}`),
  );

  renderRelatedEvents(cve, events);
}

function renderRelatedEvents(cve, events) {
  const root = document.getElementById('cveRelatedEvents');
  const related = (events.items || []).filter((item) => (item.related_cves || []).map((value) => String(value).toUpperCase()).includes(cve));
  document.getElementById('cveEventCount').textContent = `${related.length}`;
  root.replaceChildren();
  if (!related.length) {
    root.append(cveEl('article', 'security-event-empty', '目前事件資料中沒有直接提到此 CVE 的新聞或公告。'));
    return;
  }
  for (const event of related) root.append(relatedEventCard(event));
}

async function loadCvePage() {
  const cve = String(new URLSearchParams(window.location.search).get('cve') || '').toUpperCase();
  if (!/^CVE-\d{4}-\d{4,7}$/.test(cve)) {
    document.getElementById('cvePageTitle').textContent = 'CVE 參數無效';
    document.getElementById('cvePageSubtitle').textContent = '請從事件卡或 CVE 清單點擊有效的 CVE 編號。';
    document.getElementById('cvePriorityBadge').textContent = '無法載入';
    return;
  }

  try {
    const [intelResp, eventsResp, zhResp] = await Promise.all([
      fetch('./data/intelligence.json', { cache: 'no-store' }),
      fetch('./data/events.json', { cache: 'no-store' }),
      fetch('./data/cve_enrichment_zh.json', { cache: 'no-store' }),
    ]);
    if (!intelResp.ok || !eventsResp.ok || !zhResp.ok) throw new Error('無法讀取 CVE 資料');
    const [intelligence, events, enrichment] = await Promise.all([intelResp.json(), eventsResp.json(), zhResp.json()]);
    const item = (intelligence.items || []).find((row) => String(row.cve || row.facts?.cve || '').toUpperCase() === cve);
    const zh = (enrichment.items || []).find((row) => String(row.cve || '').toUpperCase() === cve);
    if (!item) {
      renderUnknownCve(cve, events);
      return;
    }
    renderKnownCve(cve, item, zh, events);
  } catch (error) {
    document.getElementById('cvePageTitle').textContent = cve;
    document.getElementById('cvePageSubtitle').textContent = error.message || '無法載入 CVE 詳情';
    document.getElementById('cvePriorityBadge').textContent = '資料載入失敗';
    console.error(error);
  }
}

loadCvePage();
