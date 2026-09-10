const state = { priority: 'ALL', query: '', items: [] };

const $ = (id) => document.getElementById(id);
const text = (value, fallback = '未確認') => {
  if (value === null || value === undefined || value === '') return fallback;
  return String(value);
};
const fmtPercent = (value) => {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return '未確認';
  return `${(Number(value) * 100).toFixed(2)}%`;
};
const fmtTime = (value) => {
  if (!value) return '未確認';
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return text(value);
  return new Intl.DateTimeFormat('zh-TW', {
    timeZone: 'Asia/Taipei', year: 'numeric', month: '2-digit', day: '2-digit',
    hour: '2-digit', minute: '2-digit', hour12: false,
  }).format(date);
};
const safeUrl = (value) => {
  try {
    const url = new URL(value);
    return url.protocol === 'https:' ? url.toString() : null;
  } catch (_) {
    return null;
  }
};

const EVENT_LABELS = {
  active_exploitation: 'Active exploitation',
  zero_day: 'Zero-day',
  ransomware: 'Ransomware',
  supply_chain: 'Supply chain',
  data_breach: 'Data breach',
  malware_campaign: 'Malware campaign',
  phishing: 'Phishing',
  ddos_disruption: 'DDoS / disruption',
  vulnerability: 'Vulnerability',
  general: 'Security event',
};
const VERIFY_LABELS = {
  official_confirmed: '官方來源確認',
  corroborated: '多來源交叉確認',
  single_trusted_source: '單一可信來源',
  discovery_only: '僅搜尋發現',
};

function el(tag, className, value) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (value !== undefined && value !== null) node.textContent = String(value);
  return node;
}

function append(parent, ...children) {
  for (const child of children) if (child) parent.append(child);
}

function metric(label, value, note) {
  const card = el('article', 'metric-card');
  append(card, el('span', 'metric-label', label), el('strong', 'metric-value', value), el('span', 'metric-note', note));
  return card;
}

function priorityBadge(priority) {
  return el('span', `priority-badge ${String(priority || 'WATCH').toLowerCase()}`, text(priority, 'WATCH'));
}

function tag(label, kind = '') {
  return el('span', `tag ${kind}`.trim(), label);
}

function verificationBadge(event) {
  const status = event.verification?.status || 'discovery_only';
  const kind = status === 'official_confirmed' || status === 'corroborated' ? 'good' : status === 'single_trusted_source' ? 'info' : '';
  return tag(VERIFY_LABELS[status] || status, kind);
}

function eventSourceLinks(event) {
  const box = el('div', 'source-links');
  const seen = new Set();
  for (const source of event.sources || []) {
    const url = safeUrl(source.url);
    if (!url || seen.has(url)) continue;
    seen.add(url);
    const label = source.publisher || source.domain || '來源';
    const a = el('a', '', label);
    a.href = url;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    box.append(a);
  }
  return box;
}

function vulnerabilitySourceLinks(facts) {
  const box = el('div', 'source-links');
  const candidates = [
    ['NVD', facts?.provenance?.nvd || facts?.source_url],
    ['CISA KEV', facts?.provenance?.cisa_kev],
    ['FIRST EPSS', facts?.provenance?.epss],
  ];
  const seen = new Set();
  for (const [label, raw] of candidates) {
    const url = safeUrl(raw);
    if (!url || seen.has(url)) continue;
    seen.add(url);
    const a = el('a', '', label);
    a.href = url;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    box.append(a);
  }
  return box;
}

function itemTags(item) {
  const facts = item.facts || {};
  const cvss = facts.cvss || {};
  const tags = el('div', 'tag-row');
  if (facts.cisa_kev?.listed) tags.append(tag('CISA KEV', 'danger'));
  const exploit = facts.exploitation_status?.status;
  if (exploit && exploit !== 'none' && exploit !== 'unconfirmed') tags.append(tag(`Exploit: ${exploit}`, exploit === 'known_exploited' ? 'danger' : 'info'));
  if (facts.cisa_kev?.known_ransomware_campaign_use === 'Known') tags.append(tag('Ransomware use: Known', 'danger'));
  if (cvss.severity) tags.append(tag(`CVSS ${text(cvss.score)} ${cvss.severity}`, cvss.severity === 'CRITICAL' ? 'danger' : 'info'));
  if (facts.epss !== null && facts.epss !== undefined) tags.append(tag(`EPSS ${fmtPercent(facts.epss)}`, Number(facts.epss) >= 0.1 ? 'info' : ''));
  return tags;
}

function renderMetrics(events, eventDelta, intelligence, metadata) {
  const root = $('metrics');
  root.replaceChildren();
  const eventSummary = events.summary || {};
  const intelSummary = intelligence.summary || {};
  const official = (events.items || []).filter((x) => x.verification?.status === 'official_confirmed').length;
  const active = (events.items || []).filter((x) => x.event_type === 'active_exploitation').length;
  root.append(
    metric('New events', eventDelta.summary?.new_notable_count ?? eventDelta.items?.length ?? 0, '相對上次新增'),
    metric('P1 events', eventSummary.p1 || 0, '今日事件最高優先'),
    metric('Active exploit', active, '過去 24h 事件'),
    metric('Verified', official, '官方來源確認'),
    metric('CVE P1', intelSummary.p1 || 0, '漏洞處理層'),
  );

  const deterministic = metadata.renderer === 'deterministic' || metadata.llm_body_used === false;
  const mode = deterministic ? 'Verified facts · event-first' : 'Grounded LLM · event-first';
  $('modeBadge').textContent = mode;
  $('updatedAt').textContent = `事件更新：${fmtTime(events.generated_at)} · 報告：${fmtTime(metadata.generated_at)}`;
  $('footerGenerated').textContent = `Events: ${fmtTime(events.generated_at)} · Vulnerability intelligence: ${fmtTime(intelligence.generated_at)} · Report: ${fmtTime(metadata.generated_at)}`;
}

function eventTags(event) {
  const tags = el('div', 'tag-row');
  tags.append(tag(EVENT_LABELS[event.event_type] || event.event_type, event.event_type === 'active_exploitation' || event.event_type === 'zero_day' ? 'danger' : 'info'));
  tags.append(verificationBadge(event));
  tags.append(tag(`Relevance: ${text(event.relevance?.level, 'low')}`, event.relevance?.level === 'high' ? 'good' : ''));
  if (event.is_new) tags.append(tag('NEW', 'danger'));
  for (const signal of event.signals || []) {
    if (signal !== event.event_type) tags.append(tag(EVENT_LABELS[signal] || signal));
  }
  return tags;
}

function eventCard(event) {
  const card = el('article', `event-card ${String(event.priority || 'WATCH').toLowerCase()}`);
  const top = el('div', 'event-head');
  const titleBox = el('div', 'event-title-box');
  append(titleBox, el('h3', 'event-title', event.title), el('p', 'event-meta', `${fmtTime(event.last_seen)} · ${text(event.verification?.source_count, 0)} source(s)`));
  const score = el('div', 'event-score');
  append(score, priorityBadge(event.priority), el('strong', '', `Score ${text(event.score)}`));
  append(top, titleBox, score);
  card.append(top, eventTags(event));

  if (event.summary) card.append(el('p', 'event-summary', event.summary));

  const factGrid = el('div', 'event-fact-grid');
  const relevanceText = event.relevance?.scope === 'profile_matched'
    ? `${text(event.relevance?.level)} · profile matched`
    : event.relevance?.scope === 'general_enterprise'
      ? `${text(event.relevance?.level)} · general enterprise`
      : '未確認';
  factGrid.append(
    detailBox('Event type', EVENT_LABELS[event.event_type] || event.event_type),
    detailBox('Verification', VERIFY_LABELS[event.verification?.status] || text(event.verification?.status)),
    detailBox('Relevance', relevanceText),
    detailBox('First / last seen', `${fmtTime(event.first_seen)} / ${fmtTime(event.last_seen)}`),
  );
  card.append(factGrid);

  const confirmed = event.confirmed_cves || [];
  const unverified = event.unverified_cve_mentions || [];
  if (confirmed.length || unverified.length) {
    const cveBox = el('div', 'event-cves');
    if (confirmed.length) append(cveBox, el('span', 'event-cve-label', '已由 NVD / vulnerability layer 驗證'), el('strong', '', confirmed.join(', ')));
    if (unverified.length) append(cveBox, el('span', 'event-cve-label warning', '來源提及但尚未驗證'), el('strong', '', unverified.join(', ')));
    card.append(cveBox);
  }

  if ((event.linked_vulnerabilities || []).length) {
    const linked = el('div', 'linked-vulns');
    linked.append(el('span', 'event-cve-label', '關聯漏洞優先級'));
    for (const vuln of event.linked_vulnerabilities) {
      const row = el('span', 'linked-vuln');
      append(row, el('strong', '', text(vuln.cve)), priorityBadge(vuln.risk?.priority));
      linked.append(row);
    }
    card.append(linked);
  }

  const relevanceReasons = event.relevance?.reasons || [];
  if (relevanceReasons.length) {
    const reasons = el('ul', 'reason-list');
    for (const reason of relevanceReasons) reasons.append(el('li', '', `${text(reason.code)}: ${text(reason.detail)}`));
    card.append(el('h4', 'minor-heading', '相關性依據'), reasons);
  }
  card.append(eventSourceLinks(event));
  return card;
}

function renderEvents(events) {
  const root = $('eventList');
  root.replaceChildren();
  const items = events.items || [];
  $('eventCount').textContent = `${items.length} events`;
  $('eventEmpty').hidden = items.length !== 0;
  for (const event of items) root.append(eventCard(event));
}

function renderEventDelta(eventDelta) {
  const root = $('eventDeltaList');
  root.replaceChildren();
  const items = eventDelta.items || [];
  $('eventDeltaCount').textContent = `${items.length} new`;
  if (!items.length) {
    const empty = el('article', 'delta-card');
    append(empty, el('h3', '', '目前沒有新的重大資安事件'), el('p', 'card-summary', '這代表相對上一份 event state 沒有新增達 P1/P2/P3 門檻的事件；不會為了日報硬湊新聞。'));
    root.append(empty);
    return;
  }
  for (const event of items) {
    const card = el('article', 'delta-card');
    const top = el('div', 'card-top');
    append(top, el('h3', '', event.title), priorityBadge(event.priority));
    card.append(top, eventTags(event));
    card.append(el('p', 'card-summary', `${EVENT_LABELS[event.event_type] || event.event_type} · ${VERIFY_LABELS[event.verification?.status] || event.verification?.status}`));
    card.append(eventSourceLinks(event));
    root.append(card);
  }
}

function detailBox(label, value) {
  const box = el('div', 'detail-box');
  append(box, el('span', '', label), el('strong', '', value));
  return box;
}

function intelligenceCard(item) {
  const facts = item.facts || {};
  const risk = item.risk || {};
  const cvss = facts.cvss || {};
  const card = el('article', 'intel-card');
  card.dataset.priority = text(risk.priority, 'WATCH');
  card.dataset.search = [item.cve, facts.vendor, facts.product, facts.title, facts.description].filter(Boolean).join(' ').toLowerCase();

  const head = el('div', 'intel-head');
  const title = el('div', 'intel-title');
  append(title, el('strong', '', item.cve || facts.cve || '未確認 CVE'), el('span', '', `${text(facts.vendor)} / ${text(facts.product)}`));
  const riskStat = el('div', 'intel-stat');
  append(riskStat, el('span', '', 'Priority / Score'), priorityBadge(risk.priority), el('strong', '', `Score ${text(risk.score)}`));
  const cvssStat = el('div', 'intel-stat');
  append(cvssStat, el('span', '', 'CVSS'), el('strong', '', cvss.score !== null && cvss.score !== undefined ? `${cvss.score} ${text(cvss.severity, '')}`.trim() : '未確認'));
  const epssStat = el('div', 'intel-stat');
  append(epssStat, el('span', '', 'EPSS'), el('strong', '', fmtPercent(facts.epss)));
  append(head, title, riskStat, cvssStat, epssStat);
  card.append(head);

  const details = el('details');
  details.append(el('summary', '', '查看 verified facts、risk reasons 與來源'));
  const body = el('div', 'detail-body');
  body.append(itemTags(item), el('p', '', text(facts.description)));
  const grid = el('div', 'detail-grid');
  grid.append(
    detailBox('Exploitation', `${text(facts.exploitation_status?.status)} · ${text(facts.exploitation_status?.source)}`),
    detailBox('CISA KEV', facts.cisa_kev?.listed ? `Listed · ${text(facts.cisa_kev?.date_added)}` : 'Not listed'),
    detailBox('Ransomware use', text(facts.cisa_kev?.known_ransomware_campaign_use)),
    detailBox('Published / Updated', `${fmtTime(facts.published_time)} / ${fmtTime(facts.updated_time)}`),
    detailBox('EPSS percentile', fmtPercent(facts.epss_percentile)),
    detailBox('CWE', (facts.cwes || []).join(', ') || '未確認'),
  );
  body.append(grid);
  const reasons = el('ul', 'reason-list');
  for (const reason of risk.reasons || []) reasons.append(el('li', '', `${text(reason.code)} (${Number(reason.points || 0) >= 0 ? '+' : ''}${text(reason.points, '0')})`));
  if (reasons.children.length) body.append(el('h3', '', 'Risk reasons'), reasons);
  body.append(vulnerabilitySourceLinks(facts));
  details.append(body);
  card.append(details);
  return card;
}

function applyFilters() {
  const root = $('intelligenceList');
  let visible = 0;
  for (const card of root.children) {
    const priorityOk = state.priority === 'ALL' || card.dataset.priority === state.priority;
    const queryOk = !state.query || card.dataset.search.includes(state.query);
    const show = priorityOk && queryOk;
    card.hidden = !show;
    if (show) visible += 1;
  }
  $('intelCount').textContent = `${visible} / ${state.items.length}`;
  $('emptyState').hidden = visible !== 0;
}

function renderIntelligence(intelligence) {
  const root = $('intelligenceList');
  root.replaceChildren();
  const priorityOrder = { P1: 0, P2: 1, P3: 2, WATCH: 3 };
  state.items = [...(intelligence.items || [])].sort((a, b) => {
    const pa = priorityOrder[a.risk?.priority] ?? 9;
    const pb = priorityOrder[b.risk?.priority] ?? 9;
    return pa - pb || Number(b.risk?.score || 0) - Number(a.risk?.score || 0) || String(a.cve).localeCompare(String(b.cve));
  });
  for (const item of state.items) root.append(intelligenceCard(item));
  applyFilters();
}

function wireFilters() {
  $('searchInput').addEventListener('input', (event) => {
    state.query = event.target.value.trim().toLowerCase();
    applyFilters();
  });
  $('priorityFilters').addEventListener('click', (event) => {
    const button = event.target.closest('button[data-priority]');
    if (!button) return;
    state.priority = button.dataset.priority;
    for (const item of $('priorityFilters').querySelectorAll('button')) item.classList.toggle('active', item === button);
    applyFilters();
  });
}

async function load() {
  try {
    const responses = await Promise.all([
      fetch('./data/events.json', { cache: 'no-store' }),
      fetch('./data/event_delta.json', { cache: 'no-store' }),
      fetch('./data/intelligence.json', { cache: 'no-store' }),
      fetch('./data/delta.json', { cache: 'no-store' }),
      fetch('./data/report_metadata.json', { cache: 'no-store' }),
    ]);
    if (responses.some((response) => !response.ok)) throw new Error('無法讀取完整事件 / 漏洞情報資料');
    const [events, eventDelta, intelligence, vulnerabilityDelta, metadata] = await Promise.all(responses.map((response) => response.json()));
    renderMetrics(events, eventDelta, intelligence, metadata);
    renderEvents(events);
    renderEventDelta(eventDelta);
    renderIntelligence(intelligence);
    wireFilters();
    void vulnerabilityDelta;
  } catch (error) {
    $('modeBadge').textContent = '資料載入失敗';
    $('eventList').replaceChildren(el('article', 'event-card', error.message || '無法載入資料'));
    $('eventDeltaList').replaceChildren();
    $('intelligenceList').replaceChildren();
    $('eventEmpty').hidden = false;
    $('emptyState').hidden = false;
    $('emptyState').textContent = '目前無法載入情報資料，請稍後再試。';
    console.error(error);
  }
}

load();
