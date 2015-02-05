import logging
import math
from game_round import GameRound
from strategy.strategy_dice_count import StrategyDiceCount

__author__ = 'Andreas Dahl'


class Game(object):
    score = 0
    rounds = 0
    current_round = None
    running = False

    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running:
            self.new_round()

            round_score = self.current_round.play()
            self.score += round_score
            logging.info(
                "Round " + str(self.rounds) + " ended with " + str(round_score) + " points. Player now has " + str(
                    self.score) + " points")

            if self.score >= 10000:
                self.end_game()

    def new_round(self):
        self.rounds += 1
        self.current_round = GameRound(StrategyDiceCount(), self)
        logging.info("Starting round " + str(self.rounds))

    def end_game(self):
        self.running = False
        logging.info("The player won after " + str(self.rounds) + " with " + str(self.score) + " points")


logging.basicConfig(level=logging.INFO)

rs = []
for i in range(0, 100):
    g = Game()
    g.start()
    rs.append(g.rounds)

sum = math.fsum(rs)
logging.info("Average Rounds: " + str(sum / len(rs)))
