def isVowel(string):

    if (string == "a") or (string == "e") or (string == "i") or (string == "o") or (string == "u"):
        result = True
    else:
        result = False

    return result

print(isVowel("a"))
print(isVowel("w"))