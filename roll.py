import random

def random_roll(n):
    """
    Return a random roll of n dices.
    :param n:  Amount of dices in the roll
    :return:  A list of dice roll results
    """
    dices = []
    for i in range(0, n):
        dices.append(random.randint(1,6))
    return dices

def all_rolls():
    """
        Return a list of lists with all the possible rolls for six-sided dices.
    :return:  list of lists with all the possible rolls for six-sided dices.
    """
    rolls = []
    for d1 in range(1, 6):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                for d4 in range(1, 7):
                    for d5 in range(1, 7):
                        for d6 in range(1, 7):
                            rolls.append([d1, d2, d3, d4, d5, d6])
    return rolls

def simple_score(dices):
    score = 0
    for dice in dices:
        if (dice == 1):
            score += 100
        elif (dice == 5):
            score += 50
    return score

def pop_digit(n, combo_score, single_score = 0):
    score = 0
    # Check combo
    if n >= 3:
        score = combo_score
        n -= 3
        while n > 0:
            score *= 2
            n -= 1
    # if no combo, add single
    score += n * single_score
    return score

def highest_score(dices):
    hist = [0] * 6
    for dice in dices:
        hist[dice-1] += 1
    # Check for stair
    if (hist.count(1) == len(hist)):
        return 1000
    # Check for three pairs
    if (hist.count(2) >= 3):
        return 200

    score = 0
    score += pop_digit(hist[0], 1000, 100)
    score += pop_digit(hist[1], 200)
    score += pop_digit(hist[2], 300)
    score += pop_digit(hist[3], 400)
    score += pop_digit(hist[4], 500, 50)
    score += pop_digit(hist[5], 600)

    return score

