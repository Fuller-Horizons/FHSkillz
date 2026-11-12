import os
import tempfile
import unittest
from _helper import run

EXAMPLE = os.path.join(os.path.dirname(__file__), "..", "..", "jail-prototype", "references",
                       "example-scorecard-layouts.html")
GOOD = open(EXAMPLE, encoding="utf-8").read()


def lint(html, *flags):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
    try:
        return run("artifact-lint.py", f.name, *flags)
    finally:
        os.unlink(f.name)


class TestArtifactLint(unittest.TestCase):
    def test_example_passes_strict(self):
        rc, out, err = lint(GOOD, "--look", "--strict")
        self.assertEqual(rc, 0, err)

    def test_title_viewport_background(self):
        bad = (GOOD.replace("PROTOTYPE — wipe me · ", "")
                   .replace('<meta name="viewport" content="width=device-width, initial-scale=1">', "")
                   .replace("html, body { background:#ffffff;", "html, body {"))
        rc, _, err = lint(bad)
        self.assertEqual(rc, 1)
        for frag in ("PROTOTYPE", "viewport", "explicit background"):
            self.assertIn(frag, err)

    def test_outside_request_and_allow_host(self):
        bad = GOOD.replace("</head>", '<script src="https://cdn.example.com/x.js"></script></head>')
        rc, _, err = lint(bad)
        self.assertEqual(rc, 1)
        self.assertIn("outside request", err)
        rc, _, err = lint(bad, "--allow-host", "cdn.example.com")
        self.assertEqual(rc, 0, err)

    def test_local_asset_file(self):
        bad = GOOD.replace("</head>", '<link rel="stylesheet" href="styles.css"></head>')
        rc, _, err = lint(bad)
        self.assertEqual(rc, 1)
        self.assertIn("local asset file", err)

    def test_duplicate_review_ids(self):
        bad = GOOD.replace('data-review-id="7"', 'data-review-id="6"')
        rc, _, err = lint(bad)
        self.assertEqual(rc, 1)
        self.assertIn("duplicate data-review-id: 6", err)

    def test_variant_count_and_switch(self):
        bad = GOOD.replace('<section data-variant="C"', '<section data-variant="B"')
        rc, _, err = lint(bad)
        self.assertEqual(rc, 1)
        self.assertIn("exactly 3", err)
        bad2 = GOOD.replace('<div class="switch" data-variant-switch>', '<div class="switch">')
        rc, _, err = lint(bad2)
        self.assertEqual(rc, 1)
        self.assertIn("data-variant-switch controls; need exactly 1", err)

    def test_questions_need_copy_button(self):
        bad = GOOD.replace(' data-copy-feedback>', '>').replace("document.querySelector('[data-copy-feedback]')", "null")
        rc, _, err = lint(bad)
        self.assertEqual(rc, 1)
        self.assertIn("no data-copy-feedback", err)

    def test_revisions_legend(self):
        bad = GOOD.replace('[{"id":"r1","summary":"First round: three layouts for the weekly scorecard question"}]', '[{"id":"r1"}]')
        rc, _, err = lint(bad)
        self.assertEqual(rc, 1)
        self.assertIn("legend invalid", err)
        bad2 = GOOD.replace('<p class="small pt" data-review-id="7">', '<p class="small pt" data-review-id="7" data-rev="r9">')
        rc, _, err = lint(bad2)
        self.assertEqual(rc, 1)
        self.assertIn("not in the revisions legend: r9", err)

    def test_warnings_only_with_strict(self):
        plain = ('<!doctype html><html><head><meta name="viewport" content="width=device-width">'
                 '<title>PROTOTYPE x</title><style>body{background:#fff}</style></head><body>PROTOTYPE</body></html>')
        self.assertEqual(lint(plain)[0], 0)
        rc, _, err = lint(plain, "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("no data-review-id", err)

    def test_usage(self):
        self.assertEqual(run("artifact-lint.py", "missing.html")[0], 2)

    def test_sandbox_blocked_calls_need_try(self):
        bad = GOOD.replace("try { if (location.protocol !== 'about:') history.replaceState(null, '', '#variant-' + v); } catch (e) { /* not allowed here */ }",
                           "history.replaceState(null, '', '#variant-' + v);")
        rc, _, err = lint(bad)
        self.assertEqual(rc, 1)
        self.assertIn("history.replaceState outside try/catch", err)
        bad2 = GOOD.replace("<script>\n  const show", "<script>\n  localStorage.setItem('v','A');\n  const show")
        rc, _, err = lint(bad2)
        self.assertEqual(rc, 1)
        self.assertIn("localStorage outside try/catch", err)


if __name__ == "__main__":
    unittest.main()
