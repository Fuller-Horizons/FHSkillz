import unittest
import _helper  # noqa: F401  (sets sys.path)
import fh_patterns as fp

# Synthetic secret-shaped value assembled at runtime so no literal key is committed.
FAKE_AWS = "AKIA" + "ABCDEFGHIJKLMNOP"


def kinds(text, classes=("secret", "pii")):
    return [(h["cls"], h["kind"]) for h in fp.scan(text, classes)]


class TestFhPatterns(unittest.TestCase):
    def test_luhn(self):
        self.assertTrue(fp.luhn_ok("4111111111111111"))
        self.assertFalse(fp.luhn_ok("4111111111111112"))

    def test_card_detected_and_invalid_not(self):
        self.assertIn(("pii", "payment card number"), kinds("card 4111-1111-1111-1111"))
        self.assertEqual(kinds("card 4111111111111112"), [])

    def test_ssn_valid_and_excluded_areas(self):
        self.assertIn(("pii", "SSN"), kinds("123-45-6789"))
        for bad in ("000-12-3456", "666-12-3456", "900-12-3456", "123-00-6789", "123-45-0000"):
            self.assertEqual(kinds(bad), [], bad)

    def test_aba(self):
        self.assertTrue(fp.aba_ok("021000021"))
        self.assertFalse(fp.aba_ok("021000022"))
        self.assertIn(("pii", "bank routing number"), kinds("routing 021000021"))

    def test_dob_and_email_phone(self):
        self.assertIn(("pii", "date of birth"), kinds("DOB: 03/14/1985"))
        self.assertEqual(kinds("meeting on 03/14/1985"), [])
        self.assertIn(("pii", "email + phone"), kinds("a@example.test 631-555-0142"))
        self.assertEqual(kinds("a@example.test only"), [])

    def test_secret_class(self):
        self.assertIn(("secret", "AWS access key id"), kinds(FAKE_AWS))
        self.assertEqual(kinds(FAKE_AWS, ("pii",)), [])

    def test_values_never_in_results(self):
        text = "card 4111111111111111 ssn 123-45-6789 key " + FAKE_AWS
        blob = repr(fp.scan(text))
        for v in ("4111111111111111", "123-45-6789", FAKE_AWS, "6789"):
            self.assertNotIn(v, blob)
        for hit in fp.scan(text):
            self.assertEqual(set(hit), {"line", "cls", "kind"})

    def test_placeholder_not_flagged(self):
        self.assertEqual(kinds('password = "${DB_PASSWORD}"'), [])


if __name__ == "__main__":
    unittest.main()
