a=0
b=1
n=int(input())
print(a,b,end=" ")
while n>2:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    n-=1