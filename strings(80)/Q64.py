binary_input = input("enter: ")
listy = []
num = 0
for char in binary_input:
    if char=="0":
        num+=1
    else:
        listy.append(num)
        num = 0

listy = sorted(listy)
print(listy[-1])