string = input()
string1 = ""
for i in range(len(string)):
    if string[i] == string[i-1]:
        pass
    else:
        string1+=string[i]

print(string1)