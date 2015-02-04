__author__ = 'Andreas Dahl'

from utils import dice_utils
from utils.math_utils import *

# TODO: Game


r = dice_utils.random_roll(6)
print(r)
print(dice_utils.take_all(r))

ar = dice_utils.all_rolls()
scores = []
for roll in ar:
    scores.append(dice_utils.take_all(dice_utils))

print(sum(scores)/len(scores))
print(median(scores))