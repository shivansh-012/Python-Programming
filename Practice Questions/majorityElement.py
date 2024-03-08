n = int(input())
arr = list(map(int, input().split()))
k = int(input())
list1 = []
#distinct elements removal from arr to list1
for ele in arr:
    if ele not in list1:
        list1.append(ele)

count = 0
for ele in list1:
    if arr.count(ele) > n/k:
        count+=1

print(count)