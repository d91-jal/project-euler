__author__ = 'johan'

# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#   192 × 1 = 192
#   192 × 2 = 384
#   192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the
# concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
# pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product
# of an integer with (1,2, ... , n) where n > 1?

# Base number:
#   Must start with a 9.
#   If two digits then must be in range 91 - 98
#   If three digits then must be in range 918 - 987
#   If four digits then must be in range 9182 - 9876

def is_pan_digital(text):
    return ''.join(sorted(text)) == '123456789'


def generate_prod(start, end, step):
    result = 0

    for i in range(start, end, step):
        j = 1
        text = ''

        while len(text) <= 9:
            num = j * i
            text = text + str(num)

            if is_pan_digital(text):
                #print(i, j, text)
                result = int(text)
                return result

            j += 1

    return result


result = generate_prod(9876, 9182, -1)
temp = generate_prod(987, 918, - 1)

if temp > result:
    result = temp

temp = generate_prod(98, 91, -1)

if temp > result:
    result = temp

print(result)




