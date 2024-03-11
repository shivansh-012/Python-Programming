list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
a = False
for num in list1:
    if num in list2:
        a = True
        break

print(a)