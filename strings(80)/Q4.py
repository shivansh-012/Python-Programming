string = input("Enter a string: ")
string1 = string[0]
for char in string[1:]:
    if char==string[0]:
        string1 += "$"
    else:
        string1 += char
print(string1)