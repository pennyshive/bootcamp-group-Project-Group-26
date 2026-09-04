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

    print(len(scores))
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
        if count >= 4:
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
        return 50
    else:
        return 0


def roll_dice():
    """
    Simulates rolling 5 dice.
    """
    roll = [random.randint(1, 6) for _ in range(5)]
    return "".join(str(x) for x in roll)


def check_full_house(roll):
    """
    Checks if the roll is a full house (3 of one number and 2 of another).
    """
    matching_dice = set(roll)
    
    # A full house must have exactly two different numbers
    if len(matching_dice) != 2:
        return check_four_a_kind(roll)
        
    first_digit = list(matching_dice)[0]
    count = roll.count(first_digit)
    
    # If the first number appears 2 or 3 times, the other must appear 3 or 2 times
    if count == 2 or count == 3:
        return 25
    else:
        return check_four_a_kind(roll)
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
    if len(unique_roll) == 5:
        # If it spans exactly 4 steps from min to max, it is consecutive (e.g., 5 - 1 = 4)
        if unique_roll[-1] - unique_roll[0] == 4:
            return 40
    return 0

player_scores= {}
player_tolal = []
computer_scores = {}
computer_tolal = []
print("Let's play Yahtzee")
name = input("What is your name ?")
rolls = []

while len(player_scores)<13 and len(computer_scores)<13:
    user_choice = ""
    while user_choice == "" and user_choice == "roll again":
        roll = roll_dice()
        print(parse_roll(roll))
        print("this is your roll " + roll)
        print("This is your scores :",generate_scores(parse_roll(roll)))
        user_choice = input(name + " type (as is without the ('') which one you want"+str(CATEGORIES))
        current_score = generate_scores(parse_roll(roll))
        print(current_score)
        if user_choice == 'roll again':
            if has_run(1):
                print("this is your roll")
            roll = roll_dice()
            print("This is your scores :",generate_scores(parse_roll(roll)))
        else:
            player_scores=apply_score(generate_scores(parse_roll(roll)),user_choice,generate_scores[user_choice])
    print("This is computer's scorecard :" ,player_scores)
    computer_choice= ""
    while computer_choice == "":
        computer_points = 0
        roll = roll_dice()
        current_score = generate_scores(parse_roll(roll))
        print(current_score)
        current_points =0
        for key, value in current_score.items():
                if value > current_points :
                    computer_choice=key
                else:
                    continue
        computer_scores[computer_choice] = current_score[computer_choice]
        print("This is computer's scorecard :" ,computer_scores) # this is the print statement
