string = input("enter a string: ")
alphabets = "abcdefghijklmnopqrstuvwxyz"
flag = 1
for char in alphabets:
    if char not in string:
        flag = 0
        break
    
if flag == 1:
    print("yes")
else:
    print("no")