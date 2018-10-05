__author__ = 'johan'

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
# over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth
# 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a
# score of 938 * 53 = 49714.
#
# What is the total of all the name scores in the file?

from ProjectEuler.utils.utils import read_names_from_file, alpha_value

a = read_names_from_file('..\\resources\\names.txt')
a.sort()

# print(a)

result = 0
i = 1

for name in a:
    result += (i * alpha_value(name))
    i += 1

print(result)
