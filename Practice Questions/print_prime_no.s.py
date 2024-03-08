def prime(m):
    for j in range(2,i):
        if m%j==0:
            return False
    return True

n=int(input())
for i in range(2,n+1):
    if(prime(i)):
        print(i)
        