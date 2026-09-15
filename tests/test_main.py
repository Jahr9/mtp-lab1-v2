import unittest

from main import average_score


class AverageScoreTests(unittest.TestCase):
    def test_several_scores(self):
        self.assertAlmostEqual(
            average_score([5, 4, 3, 5]), 4.25
        )

    def test_single_score(self):
        self.assertEqual(average_score([4]), 4.0)

    def test_empty_scores(self):
        with self.assertRaises(ValueError):
            average_score([])


if __name__ == "__main__":
    unittest.main()
