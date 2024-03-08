list=[]
list_size=int(input("Enter size of list: "))
print("enter ",list_size," elements: ")
while list_size>0:
    list.append(int(input()))
    list_size-=1
print(list)
even_list=[]
for i in list:
    if i%2==0:
        even_list.append(i)
print(even_list)