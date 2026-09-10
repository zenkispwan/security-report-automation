const state = { priority: 'ALL', query: '', items: [] };

const $ = (id) => document.getElementById(id);
const text = (value, fallback = '未確認') => {
  if (value === null || value === undefined || value === '') return fallback;
  return String(value);
};
const fmtNumber = (value, digits = 2) => {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return '未確認';
  return Number(value).toFixed(digits);
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

function el(tag, className, value) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (value !== undefined && value !== null) node.textContent = String(value);
  return node;
}

function append(parent, ...children) {
  for (const child of children) if (child) parent.append(child);
  return parent;
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

function sourceLinks(facts) {
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

function renderMetrics(intelligence, delta, metadata) {
  const root = $('metrics');
  root.replaceChildren();
  const summary = intelligence.summary || {};
  const watch = Math.max(0, (intelligence.selection?.selected_count || intelligence.items?.length || 0) - (summary.p1 || 0) - (summary.p2 || 0) - (summary.p3 || 0));
  root.append(
    metric('Daily Delta', delta.summary?.included_count ?? delta.items?.length ?? 0, '重要變化'),
    metric('P1', summary.p1 || 0, '立即優先'),
    metric('P2', summary.p2 || 0, '高優先'),
    metric('P3', summary.p3 || 0, '追蹤處理'),
    metric('WATCH', watch, '持續觀察'),
  );

  const deterministic = metadata.renderer === 'deterministic' || metadata.llm_body_used === false;
  $('modeBadge').textContent = deterministic ? 'Verified facts only · deterministic' : 'Grounded LLM enrichment';
  $('updatedAt').textContent = `報告更新：${fmtTime(metadata.generated_at || intelligence.generated_at)}`;
  $('footerGenerated').textContent = `Intelligence generated: ${fmtTime(intelligence.generated_at)} · Report generated: ${fmtTime(metadata.generated_at)}`;
}

function renderDelta(delta) {
  const root = $('deltaList');
  root.replaceChildren();
  const items = delta.items || [];
  $('deltaCount').textContent = `${items.length} changes`;
  if (!items.length) {
    const empty = el('article', 'delta-card');
    append(empty, el('h3', '', '目前沒有符合門檻的重大變化'), el('p', 'card-summary', '系統不會為了產生日報而重複或硬湊事件。'));
    root.append(empty);
    return;
  }

  for (const item of items) {
    const facts = item.facts || {};
    const card = el('article', 'delta-card');
    const top = el('div', 'card-top');
    const titleBox = el('div');
    const link = el('a', 'cve-link', item.cve || facts.cve || '未確認 CVE');
    const url = safeUrl(facts.source_url || facts.provenance?.nvd);
    if (url) { link.href = url; link.target = '_blank'; link.rel = 'noopener noreferrer'; }
    append(titleBox, link, el('p', 'product-line', `${text(facts.vendor)} / ${text(facts.product)}`));
    append(top, titleBox, priorityBadge(item.risk?.priority));
    card.append(top);

    const eventNames = (item.events || []).map((event) => event.type).filter(Boolean);
    card.append(el('p', 'card-summary', eventNames.length ? eventNames.join(' · ') : '狀態變化'));
    card.append(itemTags(item));
    const desc = el('p', 'card-summary', text(facts.description));
    card.append(desc, sourceLinks(facts));
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
  const cve = el('strong', '', item.cve || facts.cve || '未確認 CVE');
  const subtitle = el('span', '', `${text(facts.vendor)} / ${text(facts.product)}`);
  append(title, cve, subtitle);

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
  body.append(itemTags(item));
  body.append(el('p', '', text(facts.description)));

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
  for (const reason of risk.reasons || []) {
    reasons.append(el('li', '', `${text(reason.code)} (${Number(reason.points || 0) >= 0 ? '+' : ''}${text(reason.points, '0')})`));
  }
  if (reasons.children.length) {
    body.append(el('h3', '', 'Risk reasons'), reasons);
  }
  body.append(sourceLinks(facts));
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
    const [intelResp, deltaResp, metaResp] = await Promise.all([
      fetch('./data/intelligence.json', { cache: 'no-store' }),
      fetch('./data/delta.json', { cache: 'no-store' }),
      fetch('./data/report_metadata.json', { cache: 'no-store' }),
    ]);
    if (!intelResp.ok || !deltaResp.ok || !metaResp.ok) throw new Error('無法讀取報告資料');
    const [intelligence, delta, metadata] = await Promise.all([intelResp.json(), deltaResp.json(), metaResp.json()]);
    renderMetrics(intelligence, delta, metadata);
    renderDelta(delta);
    renderIntelligence(intelligence);
    wireFilters();
  } catch (error) {
    $('modeBadge').textContent = '資料載入失敗';
    $('deltaList').replaceChildren(el('article', 'delta-card', error.message || '無法載入資料'));
    $('intelligenceList').replaceChildren();
    $('emptyState').hidden = false;
    $('emptyState').textContent = '目前無法載入情報資料，請稍後再試。';
    console.error(error);
  }
}

load();
