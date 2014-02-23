__author__ = 'johan'

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these
# values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
# is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
# common English words, how many are triangle words?

# t = (n / 2) * (n + 1) => n^2 + n - 2t = 0 => n = -0.5 + sqrt(0.5 ** 2 + 2 * t)

from math import sqrt
from ProjectEuler.utils import read_names_from_file, alpha_value


# t(n) = (n / 2) * (n + 1) => n^2 + n - 2t = 0 => n = -0.5 + sqrt(0.5 ** 2 + 2 * t)
def is_triangle_number(t):
    n = -0.5 + sqrt((0.5 ** 2) + (2 * t))
    return n % 1 == 0


words = read_names_from_file('words.txt')
count = 0

for word in words:
    count += is_triangle_number(alpha_value(word))

print(count)
