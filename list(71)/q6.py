tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# sorted_list = sorted(tuple_list, key=lambda x: x[-1])
n = len(tuple_list)
for i in range(0,n):
    for j in range(0,n-i-1):
        if tuple_list[j][-1] > tuple_list[j+1][-1]:
            temp = tuple_list[j]
            tuple_list[j] = tuple_list[j+1]
            tuple_list[j+1] = temp

print(tuple_list)