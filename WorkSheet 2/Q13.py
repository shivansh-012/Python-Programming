#Q13 : find the factorial of a no.
num=int(input('EnTeR a NuMbEr: '))
fact=1
while num>0:
    fact*=num
    num-=1
print("Factorial = :",fact)