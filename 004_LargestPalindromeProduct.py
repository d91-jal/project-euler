__author__ = 'johan'

# A palindromic number reads the same both ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


import math

def is_palindrome(number):
    text = str(number)
    palindrome = True

    for i in range(math.floor(len(text) / 2)):
        # if i > 1: print(i, text, text[i], text[-(i+1)])
        palindrome = palindrome and text[i] == text[-(i + 1)]

        if not palindrome:
            break

    return palindrome


def find_largest_palindrome_product(lower, upper):
    result = []

    for i in range(upper, lower + 1, -1):
        for j in range(i - 1, lower, -1):
            #print(i,j, i*j); #return 0

            if is_palindrome(i * j):
                print('{0} * {1} = {2}'.format(i, j, i * j))
                result.append(i * j)

    return max(result)

print(find_largest_palindrome_product(100, 999))