numb1 = int(input("Please type the 1st number: "))
numb2 = int(input("Please type the 2nd number: "))
numb3 = int(input("Please type the 3rd number: "))

if numb1 == numb2 and numb2 == numb3:
    result = 3 * (numb1 + numb2 + numb3)
    print("The result of three times the sum of the numbers is " , result)
else:
    result = (numb1 + numb2 + numb3)
    print("The result of the sum of the numbers is ", result