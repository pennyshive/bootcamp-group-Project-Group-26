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


def check_kinds(hand):
    # Initialize our tracking variables to False before we start checking
    found_four = False
    found_three = False

    # Go through each item in the hand one by one
    for item in hand:
        # Start counting how many times this specific 'item' appears
        count = 0
        # Look at every other item in the hand to compare
        for compare_item in hand:
            if item == compare_item:
                count += 1
        
        # Check our count after comparing with the whole hand
        if count == 4:
            found_four = True
        elif count == 3:
            found_three = True

    # After checking everything, determine the result
    if found_four:
        return "Four of a Kind!"
    elif found_three:
        return "Three of a Kind!"
    else:
        return "Nothing special."
def apply_score(scorecard, category, points):
    new_scorecard = dict(scorecard)
    new_scorecard[category] = points
    return new_scorecard
    
