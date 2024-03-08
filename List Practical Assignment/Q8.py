outer=[]
s1=int(input("Enter size of outer list:"))
print("enter ",s1," elements: ")
while s1>0:
    outer.append(int(input()))
    s1-=1
inner=[]
s2=int(input("Enter size of inner list:"))
print("enter ",s2," elements: ")
while s2>0:
    inner.append(int(input()))
    s2-=1
ans=True
for i in inner:
    if i not in outer:
        ans=False
        break
print(ans)