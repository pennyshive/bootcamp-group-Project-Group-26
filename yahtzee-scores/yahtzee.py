from collections import Counter
CATEGORIES = [
    "ones",
    "twos",
    "threes",
    "fours",
    "fives",
    "sixes",
    "three_of_a_kind",
    "four_of_a_kind",
    "full_house",
    "small_straight",
    "large_straight",
    "yahtzee",
    "chance",
]


def parse_roll(text):
    dice = [int(char) for char in text.strip() if char.isdigit()]

    return dice

def has_run(values, length):
    run = 1
    for i in range(1, len(values)):
        if values[i] == values[i - 1] + 1:   # checks consecutively
            run += 1
            if run >= length:
                return True
        else:
            run = 1   # reseting after all 3 runs have been made
    return False

def generate_scores(roll):
    counts = Counter(roll)   #counts how many times each dices landed on each number
    total = sum(roll)    #This is the sum of the roll 
    scores = {}
    print(counts)
    print(total)
    #The Upper section(ones to sixes)
    face = 1
    names = ["ones", "twos", "threes", "fours", "fives", "sixes"]
    for name in names:
        print(face, name)
        scores[name] = sum(d for d in roll if d == face)
        face += 1
    print(scores)
    return scores

def apply_score(scorecard, category, points):
    new_scorecard = dict(scorecard)
    new_scorecard[category] = points
    return new_scorecard
    