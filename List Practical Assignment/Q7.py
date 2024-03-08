listy=[]
n=int(input("enter size: "))
print("enter %d elements"%n)
for i in range(n):
    listy.append(int(input()))
print(listy)
sumy=sum(listy)
sumy1=0
for j in range(n):
    sumy1+=listy[j]
    sumy-=listy[j]
    if sumy1==sumy:
        pivot=j
        break
print(listy[0:pivot+1])
print(listy[pivot+1:])