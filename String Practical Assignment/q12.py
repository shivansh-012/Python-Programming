char_list = input("enter a string: ").split()
flag = 1
for char in char_list:
    if char.isalnum():
        pass
    else:
        flag = 0
        break

print(flag)