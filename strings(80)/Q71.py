string = input("enter a string: ")
string1 = ""
string2 = ""
for char in string:
    if char == " ":
        string1+=char
    else:
        string2+=char
string = string1 + string2
print(string)