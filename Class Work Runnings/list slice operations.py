#combining two lists

#initialize list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#show original list
print("Original List:\n",list)

print("Sliced List: ")

#creating new list
Nlist = list[:3] + list[7:]

#display sliced list
print(Nlist)

#changing existing list
list = list[::2] + list[1::2]

#display sliced list
print(list)