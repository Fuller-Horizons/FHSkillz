import unittest
from _helper import run

FAKE_AWS = "AKIA" + "ABCDEFGHIJKLMNOP"


class TestSecretScan(unittest.TestCase):
    def test_clean_stdin(self):
        rc, out, _ = run("secret-scan.py", "-", stdin="hello world\n")
        self.assertEqual(rc, 0)
        self.assertIn("clean", out)

    def test_found_exit1_and_no_value_printed(self):
        rc, out, err = run("secret-scan.py", "-", stdin="key = " + FAKE_AWS + "\n")
        self.assertEqual(rc, 1)
        self.assertIn(":1: AWS access key id", err)
        self.assertNotIn("AKIA", out + err)

    def test_assignment_value_not_printed(self):
        rc, out, err = run("secret-scan.py", "-", stdin='password = "hunter2hunter2"\n')
        self.assertEqual(rc, 1)
        self.assertNotIn("hunter", out + err)

    def test_missing_file_exit2(self):
        rc, _, _ = run("secret-scan.py", "/nonexistent/file")
        self.assertEqual(rc, 2)


if __name__ == "__main__":
    unittest.main()
