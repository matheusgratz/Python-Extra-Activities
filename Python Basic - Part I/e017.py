number = int(input("Please input a number: "))

if number <= 100:
    print("The number is between 0 and 100")
elif number > 100 and number <= 1000:
    print("The number is between 101 and 1000")
elif number > 1000 and number <= 2000:
    print("The number is between 1001 and 2000")
else:
    print("The number is greater than 2000")    