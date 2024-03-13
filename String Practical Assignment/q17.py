string = input("enter a string: ")
string1 = string + string
string2 = ""
for char in string1:
    if char.isupper():
        pass
    else:
        if char in "aeiou":
            string2+="#"
        else:
            string2+=char

print(string2)