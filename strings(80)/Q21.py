def convert(string):
    count = 0
    for it in string[0:4]:
        if it.isupper():
            count+=1
        if(count>=2):
            string=string.upper()
    return string

res = convert(input("enter a string"))

print(res)