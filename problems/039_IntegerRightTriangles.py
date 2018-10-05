__author__ = 'johan'

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ? 1000, is the number of solutions maximised?

# c^2 = a^2 + b^2
# a + b + c = p
#
# sqrt(a^2 + b^2) + a + b = p
#
# a^2 + b^2 must be a perfect square
# a + b > c => c < 500
#

from math import sqrt
# Generate a set of squares x^2 where x < 500

squares = [x * x for x in range(1, 500)]
lookup = set(squares)
lengths = {x: 0 for x in range(1, 1001)}
result = (0, 0)

# Find combos a, b, c in squares where a <= b < c and a + b = c
for i in range(len(squares) - 1):
    for j in range(i + 1, len(squares)):
        a = squares[i]
        b = squares[j]

        if sqrt(a) + sqrt(b) + sqrt(a + b) > 1000:
            break

        if a + b in lookup:
            length = int(sqrt(a + b) + sqrt(a) + sqrt(b))
            # print(sqrt(a), sqrt(b), sqrt(a + b), key)
            lengths[length] += 1

            if lengths[length] > result[1]:
                result = (length, lengths[length])

print(result)
