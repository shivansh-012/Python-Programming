A = [10, 5, 3, 4, 3, 5, 6]
dic = {}
for i in range(len(A)):
    if A[i] not in dic:
        f = A[i+1:].find(A[i])
        print(f)