import unittest
import yahtzee


class TestYahtzeeScores(unittest.TestCase):
    def test_three_of_a_kind(self):
        roll = yahtzee.parse_roll("33356")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["three_of_a_kind"], 20, f"Expected 20, but got {scores['three_of_a_kind']}")
        self.assertEqual(scores["full_house"], 0, f"Expected 0, but got {scores['full_house']}")

    def test_full_house(self):
        roll = yahtzee.parse_roll("22555")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["full_house"], 25, f"Expected 25, but got {scores['full_house']}")
        self.assertEqual(scores["four_of_a_kind"], 0, f"Expected 0, but got {scores['four_of_a_kind']}")

    def test_small_straight(self):
        roll = yahtzee.parse_roll("12344")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["small_straight"], 30, f"Expected 30, but got {scores['small_straight']}")
        self.assertEqual(scores["large_straight"], 0, f"Expected 0, but got {scores['large_straight']}")

    def test_large_straight_also_counts_as_small(self):
        roll = yahtzee.parse_roll("23456")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["large_straight"], 40, f"Expected 40, but got {scores['large_straight']}")
        self.assertEqual(scores["small_straight"], 30, f"Expected 30, but got {scores['small_straight']}")

    def test_yahtzee(self):
        roll = yahtzee.parse_roll("44444")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["yahtzee"], 50, f"Expected 50, but got {scores['yahtzee']}")
        self.assertEqual(scores["four_of_a_kind"], 20, f"Expected 20, but got {scores['four_of_a_kind']}")

    def test_apply_score_does_not_mutate_original(self):
        scorecard = {category: None for category in yahtzee.CATEGORIES}
        new_scorecard = yahtzee.apply_score(scorecard, "sixes", 18)
        self.assertEqual(new_scorecard["sixes"], 18)
        self.assertIsNone(scorecard["sixes"], "apply_score should not mutate the original scorecard")
def test_upper_section(self):
        roll = yahtzee.parse_roll("35166")
        scores = yahtzee.generate_scores(roll)
        self.assertEqual(scores["ones"], 20, f"Expected 20, but got {scores['three_of_a_kind']}")
        self.assertEqual(scores["full_house"], 0, f"Expected 0, but got {scores['full_house']}")

if __name__ == "__main__":
    unittest.main()
