__author__ = 'johan'

# The number, 1406357289, is a 0 to 9 pan-digital number because it is made up of each of the digits
# 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#    d2d3d4=406 is divisible by 2
#    d3d4d5=063 is divisible by 3
#    d4d5d6=635 is divisible by 5
#    d5d6d7=357 is divisible by 7
#    d6d7d8=572 is divisible by 11
#    d7d8d9=728 is divisible by 13
#    d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pan-digital numbers with this property.


from ProjectEuler.utils.utils import generate_pan_digital_numbers

# Generate all 0-9 pan-digital numbers.
all_nums = generate_pan_digital_numbers(0, 9)
result = 0
# print(all_nums[1])
# print(int(str(all_nums[1])[1:4]))

for foo in all_nums:
    if int(str(foo)[1:4]) % 2 == 0 \
            and int(str(foo)[2:5]) % 3 == 0 \
            and int(str(foo)[3:6]) % 5 == 0 \
            and int(str(foo)[4:7]) % 7 == 0 \
            and int(str(foo)[5:8]) % 11 == 0 \
            and int(str(foo)[6:9]) % 13 == 0 \
            and int(str(foo)[7:10]) % 17 == 0:
        print(foo)
        result += foo

print(result)


