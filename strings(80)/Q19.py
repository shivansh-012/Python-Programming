string = input("enter a string: ")
char = input("enter a specified character")[0]

ind = string.rfind(char)
if ind!=-1:
    print(string[:ind])
else:
    print(string)