A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
count_dict = {}
common_ele = []
for num in A:
    if num in count_dict:
        count_dict[num]+=1
    else:
        count_dict[num]=1

for num in B:
    if num in count_dict and count_dict[num]>0:
        common_ele.append(num)
        count_dict[num] -= 1

print(common_ele)