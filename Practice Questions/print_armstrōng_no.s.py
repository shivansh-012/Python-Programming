def armstrong(m):
    digit=0
    a=b=m
    while(a>0):
        digit+=1
        a//=10
    sum=0
    while(b>0):
        sum+=(b%10)**digit
        b//=10
    if(sum==m):
        return True
n=int(input())
for i in range(1,n+1):
    if(armstrong(i)):
        print(i)