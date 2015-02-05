from strategy import Strategy
from utils.dice_utils import get_score

__author__ = 'Andreas Dahl'


class StrategyDiceCount(Strategy):

    def handle_roll(self, game_round):
        """
        Take all the points in the given roll.
        :param roll:  A list of dices in a roll.
        :return:  Points
        """
        hist = [0] * 6
        for dice in game_round.roll:
            hist[dice - 1] += 1
        # Check for stair
        if hist.count(1) == len(hist):
            return 1000
        # Check for three pairs
        if hist.count(2) >= 3:
            return 200

        score = 0
        for i in range(len(hist)):
            score += get_score(i+1, hist[i])

        return score