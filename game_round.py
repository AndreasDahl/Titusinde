from utils.dice_utils import random_roll

__author__ = 'Andreas Dahl'


class GameRound(object):
    bank = 0
    current_combo = None
    should_end = False

    def __init__(self, strategy, game):
        self.current_roll = random_roll(6)
        self.strategy = strategy
        self.game = game

    def roll_remaining(self):
        random_roll(len(self.current_roll))

    def play(self):
        score = self.strategy.handle_roll(self)

        if score == 0:
            self.end_round()

    def end_round(self):
        pass

    def lose_round(self):
        pass