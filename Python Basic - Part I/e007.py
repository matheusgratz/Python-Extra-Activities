filename = input("Please enter the complete filename (file.extension) ")
fExtension = filename.split(".")
print(f"The filename is {fExtension[0]}")
print(f"The extension is {fExtension[-1]}")