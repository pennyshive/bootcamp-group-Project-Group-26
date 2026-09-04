from collections import Counter
import random

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
    
    #The Upper section(ones to sixes)
    face = 1
    names = ["ones", "twos", "threes", "fours", "fives", "sixes"]
    for name in names:
        print(face, name)
        scores[name] = sum(d for d in roll if d == face)
        face += 1
    
    # Lower section — call each group member's function
    scores["three_of_a_kind"] = check_three_a_kind(roll)
    scores["four_of_a_kind"] = check_four_a_kind(roll)
    scores["full_house"] = check_full_house(roll)
    scores["small_straight"] = score_small_straight(roll)  
    scores["large_straight"] = score_large_straight(roll)   
    scores["yahtzee"] = check_yahtzee(roll)
    scores["chance"] = total
    return scores
    return scores

def check_three_a_kind(hand):
    # Initialize our tracking variables to False before we start checking
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
        if count == 3:
            found_three = True
       
    # After checking everything, determine the result
    if found_three:
        sum = 0 
        for item in hand:
            sum = sum + item
        return sum
       
    else:
        return 0
    

def check_four_a_kind(hand):
    # Initialize our tracking variables to False before we start checking
    found_four = False
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
       
    # After checking everything, determine the result
    if found_four:
        sum = 0 
        for item in hand:
            sum = sum + item
        return sum
    else:
        return 0


def apply_score(scorecard, category, points):
    new_scorecard = dict(scorecard)
    new_scorecard[category] = points
    return new_scorecard
    
def check_yahtzee(roll):
    """
    Checks if all 5 dice are the same.
    """
    if len(set(roll)) == 1:
        return "Yahtzee!"
    else:
        return "roll again."


def roll_dice():
    """
    Simulates rolling 5 dice.
    """
    return [random.randint(1, 6) for _ in range(5)]


def check_full_house(roll):
    """
    Checks if the roll is a full house (3 of one number and 2 of another).
    """
    matching_dice = set(roll)
    
    # A full house must have exactly two different numbers
    if len(matching_dice) != 2:
        return "Not a full house."
        
    first_digit = list(matching_dice)[0]
    count = roll.count(first_digit)
    
    # If the first number appears 2 or 3 times, the other must appear 3 or 2 times
    if count == 2 or count == 3:
        return "Full House!"
    else:
        return "Not a full house"
def score_small_straight(roll):
    """Checks for 4 consecutive numbers. Returns 30 if valid, else 0."""
    # Convert to a sorted list of unique values
    unique_roll = sorted(list(set(roll)))
    
    # Convert to a string to easily check for sub-sequences
    roll_str = "".join(map(str, unique_roll))
    
    # Check if any of the three possible 4-sequence combos exist in our unique dice
    if "1234" in roll_str or "2345" in roll_str or "3456" in roll_str:
        return 30
    return 0

def score_large_straight(roll):
    """Checks for 5 consecutive numbers. Returns 40 if valid, else 0."""
    unique_roll = sorted(list(set(roll)))
    
    # A large straight requires 5 unique elements
    if len(unique_roll == 5):
        # If it spans exactly 4 steps from min to max, it is consecutive (e.g., 5 - 1 = 4)
        if unique_roll[-1] - unique_roll[0] == 4:
            return 40
    return 0

# # --- Quick Test ---
# current_roll = [2, 3, 4, 4, 5]  # Contains 2-3-4-5 (Small Straight)

# # Save the scores to your dictionary
# scorecard["Small Straight"] = score_small_straight(current_roll)
# scorecard["Large Straight"] = score_large_straight(current_roll)

# print(scorecard)
# # Output: {'Small Straight': 30, 'Large Straight': 0}

