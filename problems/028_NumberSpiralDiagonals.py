__author__ = 'johan'

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Each new turn in the spiral will increase the difference between diagonal numbers by 2.
# Excluding the centre starting point this means the sum of the corners on each new spiral
# 1 => 1
# 2 => width 3 => 3 + 5 + 7 + 9            = 24     =>  25
# 3 => width 5 => 13 + 17 + 21 + 25        = 76     => 101
# 4 => width 7 => 31 + 37 + 43 + 49        = 160    => 261
# 5 => width 9 => 57 + 65 + 73 + 81        = 276    => 537
#
# width = (2 * count) - 1


def calc_diagonal_sum(count):
    result = 1  # Centre

    for i in range(2, count + 1):
        width = (2 * i) - 1
        last = width * width
        result += 4 * ((last + (last - ((width - 1) * 3))) / 2)

    return result


print(calc_diagonal_sum(2))
print(calc_diagonal_sum(3))
print(calc_diagonal_sum(4))
print(calc_diagonal_sum(5))
print(calc_diagonal_sum(501))
