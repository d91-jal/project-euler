# You are given the following information, but you may prefer to do some research for yourself.
#
#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


__author__ = 'johan'

from datetime import date, timedelta

d1 = date(1901, 1, 1)
d2 = date(2000, 12, 31)

delta = d2 - d1

m = [d1 + timedelta(days=i) for i in range(delta.days + 1)]

mondayFirst = [dt for dt in m if dt.isoweekday() == 7 and dt.day == 1]

print(m[0], m[-1])
print(len(mondayFirst), mondayFirst)
