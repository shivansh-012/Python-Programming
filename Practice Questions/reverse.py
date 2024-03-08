n=int(input("Enter a no.: "))
if(n%10==0):
    a=str(n)
    print(a[::-1])
else:
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n//=10
    print(rev)
    