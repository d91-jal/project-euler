__author__ = 'johan'

# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If d[n] represents the nth digit of the fractional part, find the value of the following expression.
#
# d[1] × d[10] × d[100] × d[1000] × d[10000] × d[100000] × d[1000000]

# Single digits:    [0123456789]        10 * 1 digits. Start at index 0
# Double digits:    [10111213..]        90 * 2 digits. Start at index 0 + 10 = 10
# Triple digits:    [100101102..]      900 * 3 digits. Start at index 10 + 180 = 190
# Four digits:      [100010011002...] 9000 * 4 digits. Start at index 190 + 2700 = 2890
# Five digits:                       90000 * 5 digits. Start at index 2890 + 36000 = 38890
# Six digits:                       900000 * 6 digits. Start at index 38890 + 450000 = 488890
# Seven digits:                    9000000 * 7 digits. Start at index 488890 + 5400000 = 5888890


def brute_force():
    text = ""
    result = 1

    for i in range(300000):
        text += str(i)

    for i in range(7):
        result *= int(text[10 ** i])

    return result


def find_char_index(num):
    index = 1
    temp = 1

    # Count up by the number of digits in each number.
    while index < num:
        temp += 1
        index += len(str(temp))

    return int(str(temp)[num - index - 1])


def clever_solution():
    result = 1

    for i in range(7):
        result *= find_char_index(10 ** i)

    return result


#print(find_char_index(11))
print(clever_solution())
print(brute_force())






