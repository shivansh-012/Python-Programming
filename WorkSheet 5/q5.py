l = list(map(int, input().split()))
k = int(input())
if k>len(l):
    print(l)
else:
    l = l[:k-1] + l[:k-1:-1]
    print(l)

