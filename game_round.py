import logging
from utils.dice_utils import random_roll

__author__ = 'Andreas Dahl'


class GameRound(object):
    bank = 0
    current_roll = None
    current_combo = None
    should_end = False
    alive = False

    def __init__(self, strategy, game):
        self.strategy = strategy
        self.game = game

    def roll_remaining(self):
        random_roll(len(self.current_roll))

    def play(self):
        self.current_roll = random_roll(6)
        while True:
            logging.info("Roll: " + str(self.current_roll))
            score = self.strategy.handle_roll(self)
            self.bank += score
            logging.info("Strategy took " + str(score) + " points. Now " + str(self.bank) + " in bank.")

            if score == 0:
                return 0
            elif not self.alive:
                return self.bank
            else:
                self.current_roll = random_roll(6)  # TODO
                logging.info("Used all dices. reroll" + str(self.current_roll))

    def hold(self):
        self.alive = False