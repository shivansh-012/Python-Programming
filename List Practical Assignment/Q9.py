listy=[]
list_size=int(input("Enter size of list: "))
print("enter ",list_size," elements: ")
while list_size>0:
    listy.append(int(input()))
    list_size-=1
print(listy)
seta=set(listy)
u_listy=list(seta)
print(u_listy)