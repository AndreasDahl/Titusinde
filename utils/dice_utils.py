import random

__author__ = 'Andreas Dahl'


def random_roll(n):
    """
    Return a random roll of n dices.
    :param n:  Amount of dices in the roll
    :return:  A list of dice roll results
    """
    dices = []
    for i in range(0, n):
        dices.append(random.randint(1, 6))
    return dices


def calculate_score(n, combo_score, single_score=0):
    """
    Calculate the score with a given amount of dices with the given values.

    The combo score is applies with 3 or more dices and doubled for each extra dice.

    Combo score is prioritized over single_score if available.

    :param n:  Number of dices with the given values.
    :param combo_score:  Score for a combo (of 3) with the dices.
    :param single_score:  Score for any single dice, if combo is not available.
    :return:  Calculated score.
    """
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







