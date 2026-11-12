import unittest
from _helper import run, fixture


class TestPiiScan(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(run("pii-scan.py", fixture("pii_pass.txt"))[0], 0)

    def test_fail_ssn_card(self):
        rc, _, err = run("pii-scan.py", fixture("pii_fail_ssn_card.txt"))
        self.assertEqual(rc, 1)
        self.assertIn("SSN", err)
        self.assertIn("payment card number", err)

    def test_fail_misc(self):
        rc, _, err = run("pii-scan.py", fixture("pii_fail_misc.txt"))
        self.assertEqual(rc, 1)
        for k in ("bank routing number", "date of birth", "email + phone"):
            self.assertIn(k, err)

    def test_stdin_never_prints_values(self):
        rc, out, err = run("pii-scan.py", "-", stdin="card 4111111111111111 ssn 123-45-6789\n")
        self.assertEqual(rc, 1)
        blob = out + err
        for frag in ("4111", "1111", "123-45", "6789", "45-6789"):
            self.assertNotIn(frag, blob)

    def test_io_error(self):
        self.assertEqual(run("pii-scan.py", "/nonexistent")[0], 2)


if __name__ == "__main__":
    unittest.main()
