__author__ = 'johan'

# Starting in the top left corner of a 2×2 grid, and only being able to
# move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

# Reasoning:
# Example case - 2 moves right and 2 moves down in any order will fulfill
# the task.
# 0011, 1100, 1010, 0101, 1001, 0110.
# 20 moves right and 20 moves down in any order will fulfill the task.
# How many ways are there to pick 20 items from 40?
#
# 40! / 20!(40 - 20)!

import math

print(math.factorial(4) / (math.factorial(2) * math.factorial(4 - 2)))
print(math.factorial(40) / (math.factorial(20) * math.factorial(40 - 20)))




