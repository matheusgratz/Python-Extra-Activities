input_string = input("Please type a word :")

if len(input_string) >= 2 and input_string[:2] == "is":
    print(input_string)
elif len(input_string) >= 2 and input_string[:2] != "is":
    print("is" + input_string)
else:
    print("Your string has less than 2 chars")