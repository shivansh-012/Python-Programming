def find_common_elements(A, B):
    frequency = {}
    for num in A:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1

    result = []
    for num in B:
        if num in frequency and frequency[num]>0:
            result.append(num)
            frequency[num]-=1

A1 = [1, 2, 2, 1]
B1 = [2, 3, 1, 2]
A2 = [2, 1, 4, 10]
B2 = [3, 6, 2, 10, 10]

print(find_common_elements(A1, B1))
print(find_common_elements(A2, B2))
