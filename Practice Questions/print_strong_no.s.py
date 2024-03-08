def strong(m):
    a=m
    sum=0
    while(a>0):
        digit=a%10
        fact=1
        while(digit>0):
            fact*=digit
            digit-=1
        sum+=fact
        a//=10
    if(sum==m):
        return True

n=int(input())
for i in range(1,n+1):
    if(strong(i)):
        print(i)