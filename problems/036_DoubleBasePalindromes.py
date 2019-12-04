__author__ = 'johan'

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

# Must end with a 1 in binary form => only odd numbers.
# Generate all odd numbers from 1 to 2^10 and prepend the reverse to generate all binary
# palindromes. Then check if they are palindromes in decimal.


def is_palindrome(text):
    palindrome = True

    for i in range(len(text) // 2):
        # if i > 1: print(i, text, text[i], text[-(i+1)])
        palindrome = palindrome and text[i] == text[-(i + 1)]

        if not palindrome:
            break

    return palindrome


def generate_bin_palindromes(max_len):
    result = ['1']
    sub_len = max_len // 2

    for i in range(1, 2 ** sub_len, 2):
        # Remove the '0b' prefix from the binary string.
        temp = bin(i)[2:]
        rev = temp[::-1]
        result.append(rev + temp)
        # Also add a single bit in the middle to generate any odd length binary strings.
        result.append(rev + '0' + temp)
        result.append(rev + '1' + temp)

        if i > 1:
            # Also append the same number but with a leading zero.
            temp = '0' + temp[1:]
            rev = rev[:-1] + '0'
            result.append(rev + temp)
            # Also add a single bit in the middle to generate any odd length binary strings.
            result.append(rev + '0' + temp)
            result.append(rev + '1' + temp)

    return result


a = generate_bin_palindromes(20)
result = []

for bnum in a:
    dnum = int(bnum, 2)
    if dnum < 1e6 and is_palindrome(str(dnum)):
        result.append(dnum)

print(sum(result), result)


