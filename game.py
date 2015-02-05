import math
from game_round import GameRound
from strategy.strategy_dice_count import StrategyDiceCount

__author__ = 'Andreas Dahl'


# TODO: Game
class Game(object):
    score = 0
    rounds = 0
    current_round = None

    def start(self):
        self.new_round()

    def new_round(self):
        self.rounds += 1
        self.current_round = GameRound(StrategyDiceCount(), self)
        print "Starting round", self.rounds

        self.current_round.play()

    def end_round(self, score):
        self.score += score
        print "Round", self.rounds, "ended with", score, "points. Player now has", self.score, "points"

        if self.score >= 10000:
            self.end_game()
        else:
            self.new_round()

    def end_game(self):
        print "The player won after", self.rounds, "with", self.score, "points"

rs = []
for i in range(0, 1000):
    g = Game()
    g.start()
    rs.append(g.rounds)

sum = math.fsum(rs)
print "Average Rounds:", sum / len(rs)
