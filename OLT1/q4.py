c,k,n = map(int, input().split())
while n>0:
    c*=k
    n-=1
print(c)