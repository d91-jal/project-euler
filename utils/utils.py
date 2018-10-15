__author__ = 'johan'

import math
from itertools import permutations


def get_triangular(n):
    return int((n * (n + 1)) / 2)


def get_pentagonal(n):
    return int((n * ((3 * n) - 1)) / 2)


def get_hexagonal(n):
    return int(n * ((2 * n) - 1))


# Generate a list of triangular 1 to size.
def get_triangulars(size):
    triangulars = []

    for i in range(1, size + 1):
        triangulars.append(get_triangular(i))

    return triangulars


# Generate a list of pentagonal 1 to size.
def get_pentagonals(size):
    pentagonals = []

    for i in range(1, size + 1):
        pentagonals.append(get_pentagonal(i))

    return pentagonals


# Generate a list of hexagonal 1 to size.
def get_hexagonals(size):
    hexagonals = []

    for i in range(1, size + 1):
        hexagonals.append(get_hexagonal(i))

    return hexagonals


def is_pentagonal(p):
    return (math.sqrt((1.0/36.0) + ((2*p)/3)) + (1/6)) % 1 == 0


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

    result = [0] * (math.ceil(math.log(num, 10)))  # Represents 1 - number of digits.

    while num >= 1:
        digit = num % 10

        if digit == 0 or digit > len(result):
            return False

        result[digit - 1] = 1
        num //= 10

    return sum(result) == len(result)


def generate_pan_digital_numbers(low, high):
    num = ""

    for i in range(low, high + 1):
        num += str(i)

    return [int(''.join(p)) for p in permutations(num)]


def read_names_from_file(filename):
    with open(filename, 'r') as f:
        temp = f.read().replace('"', '')

    split = temp.split(',')
    return split


def alpha_value(text):
    return sum([ord(i) - 64 for i in text])


def mod_pow(base, exp, mod):
    result = base

    for i in range(2, exp+1):
        result = int((result * base) % mod)

    return result


def sort_as_string(num):
    return ''.join(sorted(str(num)))


# print(mod_pow(100, 100, 1000000))
# print(is_pan_digital_number(1123456))
# print(is_pan_digital_number(7123456))
# print(is_pan_digital_number(1234567890))
# print(is_pan_digital_number(123456))
