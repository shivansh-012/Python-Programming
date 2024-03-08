#prime factorisation is the multiplication of the prime factors (inclusive of the no.)
n=int(input())
pf=1
for i in range(2,n+1):
    if n%i==0:
        counter=0
        for j in range(1,i+1):
            if i%j==0:
                counter+=1
        if(counter==2):
            pf*=i
print(pf)