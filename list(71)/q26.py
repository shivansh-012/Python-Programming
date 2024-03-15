list1 = [1,2,3,4,5]
list2 = [4,5,1,2,3]
listy = []
c = list2[0]
for i in range(len(list2)):
    if c == list1[i]:
        l = len(list1[i:])
        if list1[i:] == list2[:l]:
            listy.extend(list2[l:])
            listy.extend(list2[:l])
            break            
    else:
        pass

if list1 == listy:
    print("lists are circular rotated")
else:
    print("not")