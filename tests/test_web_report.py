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
            self.assertTrue((root / "_headers").is_file())
            self.assertTrue((root / "data/intelligence.json").is_file())
            self.assertEqual(
                Path("data/intelligence.json").read_bytes(),
                (root / "data/intelligence.json").read_bytes(),
            )

    def test_web_shell_has_no_external_executable_dependency(self):
        index = Path("web/index.html").read_text(encoding="utf-8")
        self.assertNotIn('<script src="http', index)
        self.assertNotIn('<link rel="stylesheet" href="http', index)
        self.assertIn('./app.js', index)
        self.assertIn('./styles.css', index)

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
