l = list(map(int, input().split()))
for n in l:
    if l.count(n)==1:
        print(n)
        break