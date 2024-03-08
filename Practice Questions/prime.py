n=int(input())
i=2
counter=0
while i<n:
    if n%i==0:
        counter=1
    i+=1
if counter==0 and n!=1:
    print("prime")
else:
    print("not prime")