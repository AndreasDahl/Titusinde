__author__ = 'Andreas Dahl'

import roll

from math_utils import *


r = roll.random_roll(6)
print(r)
print(roll.simple_score(r))
print(roll.highest_score(r))

ar = roll.all_rolls()
scores = []
for roll in ar:
    scores.append(roll.highest_score(roll))

print(sum(scores)/len(scores))
print(median(scores))