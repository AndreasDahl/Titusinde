from utils.dice_utils import random_roll, calculate_score

__author__ = 'Andreas Dahl'


class GameRound(object):
    bank = 0
    current_combo = None

    def __init__(self):
        self.current_roll = random_roll(6)

    def roll_remaining(self):
        random_roll(len(self.current_roll))

    # TODO
    def take_all(self, roll):
        """
        Take all the points in the given roll.
        :param roll:  A list of dices in a roll.
        :return:  Points
        """
        hist = [0] * 6
        for dice in roll:
            hist[dice - 1] += 1
        # Check for stair
        if hist.count(1) == len(hist):
            return 1000
        # Check for three pairs
        if hist.count(2) >= 3:
            return 200

        score = 0
        score += calculate_score(hist[0], 1000, 100)
        score += calculate_score(hist[1], 200)
        score += calculate_score(hist[2], 300)
        score += calculate_score(hist[3], 400)
        score += calculate_score(hist[4], 500, 50)
        score += calculate_score(hist[5], 600)

        return score



