__author__ = 'johan'

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use
# of "and" when writing out numbers is in compliance with British usage.

singles = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

singles_sum = sum([len(i) for i in singles])
teens_sum = sum([len(i) for i in teens])
tens_sum = sum([len(i) for i in tens])
hundred_sum = len('hundred')
thousand_sum = len('thousand')
and_sum = len('and')

test = 'onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefortyfortyonefortytwofortythreefortyfourfortyfivefortysixfortysevenfortyeightfortyninefiftyfiftyonefiftytwofiftythreefiftyfourfiftyfivefiftysixfiftysevenfiftyeightfiftyninesixtysixtyonesixtytwosixtythreesixtyfoursixtyfivesixtysixsixtysevensixtyeightsixtynineseventyseventyoneseventytwoseventythreeseventyfourseventyfiveseventysixseventysevenseventyeightseventynineeightyeightyoneeightytwoeightythreeeightyfoureightyfiveeightysixeightyseveneightyeighteightynineninetyninetyoneninetytwoninetythreeninetyfourninetyfiveninetysixninetysevenninetyeightninetynine'

print(singles_sum, teens_sum, tens_sum, len(test))

# 0 - 99
sum_0_99 = singles_sum + teens_sum + 10 * tens_sum + (8 * singles_sum)
# 100 - 999
sum_100_999 = 100 * sum([len(i) for i in singles]) + (900 * (hundred_sum + and_sum)) + 9 * sum_0_99 - 9 * and_sum
# 1000
sum_1000 = len('one') + thousand_sum

print(sum_0_99, sum_100_999, sum_1000, sum_0_99 + sum_100_999 + sum_1000)
