__author__ = 'johan'

import math

def is_pan_digital_string(text):
    compare_to = ''
    trim_text = text.strip().replace(' ', '')

    if len(trim_text > 9):
        return False

    for i in range(1, len(trim_text) + 1):
        compare_to += str(i)

    return ''.join(sorted(trim_text)) == compare_to


def is_pan_digital_number(num):
    if num > 987654321:
        return False

    result = [0] * (math.ceil(math.log(num, 10))) # Represents 1 - number of digits.

    while num >= 1:
        digit = num % 10

        if digit == 0 or digit > len(result):
            return False

        result[digit - 1] = 1
        num //= 10

    return sum(result) == len(result)


def generate_pan_digital_numbers(length):
    result = []



#print(is_pan_digital_number(1123456))
#print(is_pan_digital_number(7123456))
#print(is_pan_digital_number(1234567890))
#print(is_pan_digital_number(123456))