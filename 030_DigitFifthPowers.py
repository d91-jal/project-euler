__author__ = 'johan'

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#    1634 = 1^4 + 6^4 + 3^4 + 4^4
#    8208 = 8^4 + 2^4 + 0^4 + 8^4
#    9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# 0^5 =     0
# 1^5 =     1
# 2^5 =    32
# 3^5 =   243
# 4^5 =  1024
# 5^5 =  3125
# 6^5 =  7776
# 7^5 = 16807
# 8^5 = 32768
# 9^5 = 59049

# Possible 2 digit numbers contain 0, 1, 2
# Possible 3 digit numbers contain 0, 1, 2, 3
# Possible 4 digit numbers contain 0, 1, 2, 3, 4, 5 (max 3), 6 (max 1)
# Possible 5 digit numbers contain 0, 1, 2, 3, 4, 5, 6, 7, 8 (max 3), 9 (max 1)