n=int(input())
m=n
res=0
count=0
while n>0:
    res=res*10+n%10
    n//=10
    count+=1
if m==res:
    print(m," is a palindrome number")
else:
    print(m," is not a palindrome number")
print("no. of digits are",count)