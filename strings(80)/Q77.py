string = input("enter: ")

result = 0
for i in range(len(string)):
    for j in range(i,len(string)):
        result+=1

print("no. of non-empty substrings in string are {}".format(result))