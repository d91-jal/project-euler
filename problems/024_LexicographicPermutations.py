__author__ = 'johan'

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
# of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Reasoning:
# There are 10! = 3 628 800 possible permutations in a set of 10 distinct items.
# *9                                            => 1!
# *98                                           => 2! - 1!
# *879, *897, *978, *987                        => 3! - 2!
# *7689, *7698, *7869, *7896, *7968, *7986...   => 4! - 3!      


def generate_combos(prefix, chars, combos):
    if len(chars) == 0:
        combos.append(prefix)
    else:
        for i in range(len(chars)):
            generate_combos(prefix + chars[i], chars[:i] + chars[i + 1:], combos)


result = []
generate_combos('', 'abc', result)
print(result)

result2 = []
generate_combos('', '0123456789', result2)
print(len(result2))
print(result2[999999])
