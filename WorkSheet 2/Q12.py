#Q12 : count no. of digits in a no.
num = int(input("Enter a no."))
no_digit=len(str(num))
print("no of digits in",num,"are",no_digit)
#or
num1 = int(input("Enter a no."))
count=0
while num1>0:
    count+=1
    num1//=10
print("no of digits ","are",count)