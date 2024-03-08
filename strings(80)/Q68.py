string = input()
string1 = ""
string2 = ""
for char in string:
    if string.count(char)==1:
        string1+=char
    else:
        string2+=char

print(string1)
print(string2)