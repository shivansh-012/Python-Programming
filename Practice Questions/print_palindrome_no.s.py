def palindrome(m):
    a=m
    sum=0
    while(m>0):
        sum=sum*10+m%10
        m//=10
    if(sum==a):
        return True

n=int(input())
for i in range(1,n+1):
    if(palindrome(i)):
        print(i)