__author__ = 'johan'

temp1 = 1
temp2 = 2
temp3 = temp1 + temp2
counter = 3

while temp2 < 10 ** 999:
    temp3 = temp2
    temp2 = temp1 + temp2
    temp1 = temp3
    counter += 1

print(counter, len(str(temp1)), len(str(temp2)))