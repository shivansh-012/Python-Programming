t = int(input("no. of string to be entered: "))
for _ in range(t):
    string = input("enter a string: ")
    flag = 0
    if string == string[::-1]:
        flag = 1
    
    print(flag)