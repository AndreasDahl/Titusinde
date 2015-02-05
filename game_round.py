from utils.dice_utils import random_roll

__author__ = 'Andreas Dahl'


class GameRound(object):
    bank = 0
    current_combo = None
    should_end = False

    def __init__(self, strategy, game):
        self.current_roll = random_roll(6)
        print "Roll:", self.current_roll
        self.strategy = strategy
        self.game = game

    def roll_remaining(self):
        random_roll(len(self.current_roll))

    def play(self):
        score = self.strategy.handle_roll(self)
        self.bank += score
        print "Strategy took", score, "points. Now ", self.bank, "in bank."

        if score == 0:
            self.game.end_round(0)
        elif self.should_end:
            self.game.end_round(self.bank)
        else:
            self.current_roll = random_roll(6)  # TODO
            print "Used all dices reroll", self.current_roll
            self.play()

    def hold(self):
        self.should_end = True