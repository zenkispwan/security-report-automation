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
            self.assertTrue((root / "events.css").is_file())
            self.assertTrue((root / "_headers").is_file())
            self.assertTrue((root / "data/events.json").is_file())
            self.assertTrue((root / "data/event_delta.json").is_file())
            self.assertTrue((root / "data/intelligence.json").is_file())
            for relative in ("data/events.json", "data/event_delta.json", "data/intelligence.json"):
                self.assertEqual(
                    Path(relative).read_bytes(),
                    (root / relative).read_bytes(),
                )

    def test_web_shell_is_event_first_and_has_no_external_executable_dependency(self):
        index = Path("web/index.html").read_text(encoding="utf-8")
        app = Path("web/app.js").read_text(encoding="utf-8")
        self.assertNotIn('<script src="http', index)
        self.assertNotIn('<link rel="stylesheet" href="http', index)
        self.assertIn('今天發生了什麼？', index)
        self.assertIn('./app.js', index)
        self.assertIn('./styles.css', index)
        self.assertIn('./events.css', index)
        self.assertIn("./data/events.json", app)
        self.assertIn("./data/event_delta.json", app)

    def test_cloudflare_static_assets_config_has_no_worker_script(self):
        config = json.loads(Path("wrangler.jsonc").read_text(encoding="utf-8"))
        self.assertEqual(config["name"], "security-report-automation")
        self.assertEqual(config["assets"]["directory"], "./_site")
        self.assertEqual(config["compatibility_date"], "2026-09-10")
        self.assertNotIn("main", config)

        package = json.loads(Path("package.json").read_text(encoding="utf-8"))
        self.assertEqual(package["scripts"]["build:web"], "python3 scripts/build_web_report.py && python3 scripts/validate_web_report.py")
        self.assertEqual(package["scripts"]["deploy"], "wrangler deploy")
        self.assertIn("wrangler", package["devDependencies"])


if __name__ == "__main__":
    unittest.main()
