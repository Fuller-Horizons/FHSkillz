import unittest
from _helper import run, fixture


class TestDescCheck(unittest.TestCase):
    def test_pass(self):
        rc, _, err = run("desc-check.py", fixture("skills_pass"))
        self.assertEqual(rc, 0, err)

    def test_fail_long_core(self):
        rc, _, err = run("desc-check.py", fixture("skills_fail"))
        self.assertEqual(rc, 1)
        self.assertIn("core is 170 lines", err)

    def test_fail_description_rules(self):
        rc, _, err = run("desc-check.py", fixture("skills_fail"))
        self.assertIn("460 chars", err)
        self.assertIn("Do NOT use", err)
        self.assertIn("metadata.version", err)

    def test_not_a_dir(self):
        self.assertEqual(run("desc-check.py", "/nonexistent")[0], 2)


if __name__ == "__main__":
    unittest.main()
