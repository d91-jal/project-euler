# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
#
# Approach: As suggested by Ulf_T, implement a custom power function with a modulus filter.

from ProjectEuler.utils.utils import mod_pow


def calc_sum_of_x_to_the_xth(n):
    result = 0

    for i in range(1, n+1):
        result += mod_pow(i, i, 10000000000)

    return result


print(calc_sum_of_x_to_the_xth(1000))





