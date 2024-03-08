#define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']

#find the index of Rahul
i = l.index('Rahul')
l[i] = 'Shivansh'
print(l)

#add the elements of num2 list to num1 list using extend() method
num1=[1,4]
num2=[2,3,5]
num1.extend(num2)
print('num1 =',num1)
#print(num1+num2)
