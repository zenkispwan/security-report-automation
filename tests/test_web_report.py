import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_web_report import build
from scripts.validate_web_report import validate


class WebReportTests(unittest.TestCase):
    def test_build_and_validate_static_site(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "site"
            build(root)
            validate(root)
            self.assertTrue((root / "index.html").is_file())
            self.assertTrue((root / "events.html").is_file())
            self.assertTrue((root / "cve.html").is_file())
            self.assertTrue((root / "events.css").is_file())
            self.assertTrue((root / "cve.css").is_file())
            self.assertTrue((root / "events.js").is_file())
            self.assertTrue((root / "cve.js").is_file())
            self.assertTrue((root / "_headers").is_file())
            self.assertTrue((root / "data/daily_brief.json").is_file())
            self.assertTrue((root / "data/events.json").is_file())
            self.assertTrue((root / "data/cve_enrichment_zh.json").is_file())
            self.assertTrue((root / "data/intelligence.json").is_file())
            self.assertEqual(
                Path("data/daily_brief.json").read_bytes(),
                (root / "data/daily_brief.json").read_bytes(),
            )
            self.assertEqual(
                Path("data/events.json").read_bytes(),
                (root / "data/events.json").read_bytes(),
            )
            self.assertEqual(
                Path("data/cve_enrichment_zh.json").read_bytes(),
                (root / "data/cve_enrichment_zh.json").read_bytes(),
            )
            self.assertEqual(
                Path("data/intelligence.json").read_bytes(),
                (root / "data/intelligence.json").read_bytes(),
            )

    def test_web_shell_has_no_external_executable_dependency(self):
        index = Path("web/index.html").read_text(encoding="utf-8")
        events_page = Path("web/events.html").read_text(encoding="utf-8")
        cve_page = Path("web/cve.html").read_text(encoding="utf-8")
        for shell in (index, events_page, cve_page):
            self.assertNotIn('<script src="http', shell)
            self.assertNotIn('<link rel="stylesheet" href="http', shell)
            self.assertIn('./styles.css', shell)
        self.assertIn('./events.js', index)
        self.assertIn('./events.css', index)
        self.assertIn('./events.js', events_page)
        self.assertIn('./events.css', events_page)
        self.assertIn('./cve.js', cve_page)
        self.assertIn('./cve.css', cve_page)
        self.assertIn('./app.js', index)
        self.assertIn('每日資安事件報告', index)
        self.assertIn('今日情報摘要', index)
        self.assertIn('securityEventList', index)
        self.assertIn('./events.html', index)
        self.assertIn('technical-panel', index)

    def test_security_events_use_daily_brief_for_home_and_full_feed_for_archive(self):
        events = Path("web/events.js").read_text(encoding="utf-8")
        self.assertIn("fetch('./data/daily_brief.json'", events)
        self.assertIn("fetch('./data/events.json'", events)
        self.assertNotIn('fetch("http', events)
        self.assertNotIn("fetch('http", events)
        self.assertIn('headline_events', events)
        self.assertIn('RANSOMWARE', events)
        self.assertIn('ACTIVE_EXPLOITATION', events)
        self.assertIn('SUPPLY_CHAIN', events)
        self.assertIn('DATA_BREACH', events)
        self.assertIn('related_cves', events)
        self.assertIn('./cve.html?cve=', events)
        self.assertIn('cveEventChip', events)

    def test_full_event_page_has_filters_and_renders_entire_feed(self):
        page = Path("web/events.html").read_text(encoding="utf-8")
        events = Path("web/events.js").read_text(encoding="utf-8")
        self.assertIn('allSecurityEventList', page)
        self.assertIn('allEventSearch', page)
        self.assertIn('allEventSource', page)
        self.assertIn('allEventTypeFilters', page)
        self.assertIn("data-event-type=\"ACTIVE_EXPLOITATION\"", page)
        self.assertIn("data-event-type=\"RANSOMWARE\"", page)
        self.assertIn('loadAllSecurityEvents', events)
        self.assertIn('searchableEventText', events)
        self.assertIn('sourceSelect.addEventListener', events)
        self.assertIn("for (const item of filtered) root.append(securityEventCard(item))", events)

    def test_cve_detail_page_joins_facts_translation_and_related_events(self):
        page = Path("web/cve.html").read_text(encoding="utf-8")
        script = Path("web/cve.js").read_text(encoding="utf-8")
        self.assertIn('cveSummaryCard', page)
        self.assertIn('cveFactGrid', page)
        self.assertIn('cveRelatedEvents', page)
        self.assertIn("fetch('./data/intelligence.json'", script)
        self.assertIn("fetch('./data/events.json'", script)
        self.assertIn("fetch('./data/cve_enrichment_zh.json'", script)
        self.assertIn('description_zh', script)
        self.assertIn('related_cves', script)
        self.assertIn('https://nvd.nist.gov/vuln/detail/', script)

    def test_homepage_metrics_use_daily_brief(self):
        app = Path("web/app.js").read_text(encoding="utf-8")
        self.assertIn("fetch('./data/daily_brief.json'", app)
        self.assertIn("metric('重大事件'", app)
        self.assertIn("metric('已遭利用'", app)
        self.assertIn("metric('勒索軟體'", app)
        self.assertIn("metric('新 CISA KEV'", app)
        self.assertIn("metric('新 Critical CVE'", app)
        self.assertIn('brief.daily_changes', app)
        self.assertNotIn("fetch('./data/delta.json'", app)

    def test_cloudflare_static_assets_config_has_no_worker_script(self):
        config = json.loads(Path("wrangler.jsonc").read_text(encoding="utf-8"))
        self.assertEqual(config["assets"]["directory"], "./_site")
        self.assertEqual(config["compatibility_date"], "2026-09-10")
        self.assertNotIn("main", config)

        package = json.loads(Path("package.json").read_text(encoding="utf-8"))
        self.assertEqual(package["scripts"]["build:web"], "python3 scripts/build_web_report.py && python3 scripts/validate_web_report.py")
        self.assertEqual(package["scripts"]["deploy"], "wrangler deploy")
        self.assertIn("wrangler", package["devDependencies"])


if __name__ == "__main__":
    unittest.main()
