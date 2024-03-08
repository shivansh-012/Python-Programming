string1 = input("enter a string: ")
string2 = ""
for i in range(len(string1)):
    if i%2==1:
        string2+=string1[i]
    else:
        pass
print(string2)