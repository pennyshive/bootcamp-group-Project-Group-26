import unittest
import yahtzee


class TestUpperSection(unittest.TestCase):

    def test_ones(self):
        roll = yahtzee.parse_roll("11234")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["ones"], 2, f"Expected 2, but got {scores['ones']}")

    def test_ones_none_showing(self):
        roll = yahtzee.parse_roll("23456")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["ones"], 0, f"Expected 0, but got {scores['ones']}")

    def test_twos(self):
        roll = yahtzee.parse_roll("22234")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["twos"], 6, f"Expected 6, but got {scores['twos']}")

    def test_threes(self):
        roll = yahtzee.parse_roll("33356")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["threes"], 9, f"Expected 9, but got {scores['threes']}")

    def test_fours(self):
        roll = yahtzee.parse_roll("44412")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["fours"], 12, f"Expected 12, but got {scores['fours']}")

    def test_fives(self):
        roll = yahtzee.parse_roll("55556")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["fives"], 20, f"Expected 20, but got {scores['fives']}")

    def test_sixes(self):
        roll = yahtzee.parse_roll("66612")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["sixes"], 18, f"Expected 18, but got {scores['sixes']}")

    def test_sixes_none_showing(self):
        roll = yahtzee.parse_roll("11111")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["sixes"], 0, f"Expected 0, but got {scores['sixes']}")

    def test_upper_section_all_categories_present(self):
        roll = yahtzee.parse_roll("12345")
        scores = yahtzee.generate_scores(roll)
        for name in ["ones", "twos", "threes", "fours", "fives", "sixes"]:
            self.assertIn(name, scores, f"'{name}' is missing from scores")

    def test_other_dice_dont_affect_score(self):
        # Only sixes should count for "sixes", not fives
        roll = yahtzee.parse_roll("56666")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["sixes"], 24, f"Expected 24, but got {scores['sixes']}")
        self.assertEqual(scores["fives"], 5, f"Expected 5, but got {scores['fives']}")


if __name__ == "__main__":
    unittest.main()