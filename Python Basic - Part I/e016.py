number = int(input("Please type a number: "))

if number <= 17:
    result = 17 - number
else:
    result = abs(17 - number) * 2

print("The difference is " , result)
