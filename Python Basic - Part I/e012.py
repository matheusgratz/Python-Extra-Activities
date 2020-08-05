import calendar

y = int(input("Input the year: "))
m = int(input("Input the month: "))

print("---------------------")
print("Here is you Calendar")
print("---------------------")
print(calendar.month(y, m))

from calendar import month

print("---------------------")
print("Here is you Calendar")
print("---------------------")
print(month(y, m))