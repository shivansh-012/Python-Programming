str1 = input()
str2 = input()
str3 = ""
for char in str1:
    if char not in str2:
        str3+=char
for char in str2:
    if char not in str1:
        str3+=char

print(str3)