#initialize list
list=[50,70,30,20,90,10,50]

#display list
print(list[::])

#list slicing with negative in starting position
print(list[-7::1])
print(list[-7::2])
#list with last positon
print(list[-1:-7:2])

#display list
print(list[1:5])

#show original list
print("Original List:\n",list)

print("\nSliced Lists: ")

#display sliced list
print(list[3:9:2])
print(list[-7::2])
print(list[::-1])
print(list[::3])
print(list[:1:-2])
print(list[-1:-1:-1])
print(list[:0:])