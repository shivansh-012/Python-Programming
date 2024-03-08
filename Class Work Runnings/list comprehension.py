#Syntax: newList = [expression(element) for element in oldList if condition]

numbers = [1, 2, 3, 4, 5]
doubled = [x*2 for x in numbers]
print(doubled)
squared = [x**2 for x in numbers]
print(squared)

list = []

#traditiol approach of iterating
for ch in 'Geeks 4 Geeks!':
    list.append(ch)
print(list)

#using list comprehension to iterate through loop
list = [ch for ch in 'Geeks 4 Geeks!']
print(list)

list = [num for num in [1, 2, 3]]
print(list)

#list for even numbers
list = [i for i in range(11) if i%2==0]
print(list)

#list comprehension for nested matrix
matrix = []
for i in range(3):
    #append an empty substring inside the list 
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)

#list comrehension for matrix
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)