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

def calc_exp_sum(number, exp):
    result = 0
    temp = number

    while(temp >= 1):
        result += (temp % 10) ** exp
        temp //= 10

    return result

#print(calc_exp_sum(1634, 4))
#print(calc_exp_sum(8208, 4))
#print(calc_exp_sum(9474, 4))

exp = 5
maxval = 6 * (9 ** exp) # Upper bound is six nines, since seven nines will still yield a six-digit number.
total = 0

for i in range(10, maxval + 1):
    if calc_exp_sum(i, exp) == i:
        total += i
        print(i)

print(total)