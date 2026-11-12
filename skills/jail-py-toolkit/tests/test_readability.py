import unittest
from _helper import run, load

EASY = "The cat sat on the mat. The dog ran to the park. We like to play.\n"
HARD = ("Notwithstanding the aforementioned organizational considerations, "
        "implementation of comprehensive interoperability methodologies "
        "necessitates substantial institutional commitment and "
        "multidisciplinary collaboration.\n")


class TestReadability(unittest.TestCase):
    def test_easy_passes(self):
        rc, out, err = run("readability.py", "--max-grade", "9", stdin=EASY)
        self.assertEqual(rc, 0, err)
        self.assertIn("grade", out)

    def test_hard_fails(self):
        rc, out, err = run("readability.py", "--max-grade", "9", stdin=HARD)
        self.assertEqual(rc, 1)
        self.assertIn("> max", err)
        self.assertIn("longest", out)

    def test_no_limit_exit_zero(self):
        self.assertEqual(run("readability.py", stdin=HARD)[0], 0)

    def test_empty_is_usage_error(self):
        self.assertEqual(run("readability.py", stdin="")[0], 2)

    def test_markdown_noise_ignored(self):
        m = load("readability.py")
        r = m.analyze("```\nsupercalifragilistic code block\n```\n"
                      "| a | b |\n# Title\nThe cat sat. [1] **Fact** The dog ran.\n")
        self.assertEqual(r["sentences"], 3)

    def test_syllables(self):
        m = load("readability.py")
        self.assertEqual(m.syllables("cat"), 1)
        self.assertEqual(m.syllables("water"), 2)
        self.assertGreaterEqual(m.syllables("organization"), 4)


if __name__ == "__main__":
    unittest.main()
