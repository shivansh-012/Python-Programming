string = input()
c_upper = 0
c_lower = 0
c_num = 0
c_special = 0
for char in string:
    if char.isupper():
        c_upper+=1
    elif char.islower():
        c_lower+=1
    elif char.isnumeric():
        c_num+=1
    else:
        c_special+=1

print(f"upper case char: {c_upper}\nlower case char: {c_lower}\nnumbers: {c_num}\nspecial characters: {c_special}")
