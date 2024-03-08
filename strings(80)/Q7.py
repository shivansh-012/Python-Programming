string = input("enter a string")
#string = 'The lyrics is not that poor!'
indnot = string.index("not")
indpoor = string.index("poor")
string = string[:indnot] + "good" + string[indpoor+4:]
print(string)