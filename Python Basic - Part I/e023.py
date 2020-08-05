def e023(string, n):
    
    if len(string) <= 2:
        result = string * n
    else:
        result = string[:2] * n
    
    return result

print(e023("Work", 3))
print(e023("Aa", 10))