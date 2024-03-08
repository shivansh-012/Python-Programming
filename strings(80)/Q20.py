def rev_string(string):
    if len(string)%4==0:
        return string[::-1]
    else:
        return string

res = rev_string(input("Enter a string: "))

print(res)