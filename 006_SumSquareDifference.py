__author__ = 'johan'

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 ? 385 = 2640.
#
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.


def sum_numbers(lower, upper):
    return ((upper + lower) * (1 + upper - lower)) / 2

number_sum = (sum_numbers(1, 100))

a = range(1, 101)

squares = [b ** 2 for b in a]
sum_of_squares = sum(squares)
square_of_sum = number_sum ** 2

print('square of sum - sum_of_squares = {0}'.format(square_of_sum - sum_of_squares))



