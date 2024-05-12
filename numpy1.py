import numpy as np

'''
arr = np.array([1,2,3])
print(type(arr))
for x in arr:
    print(x,type(x))
'''

'''
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr):
    print(x)
'''

#to check no. of dimensions of the array
#convert list to array and array to list
'''
l = [2,6,1,8,9]
arr = np.array(l)
print(arr)
arr[0] = 10
print(arr)
print(arr.ndim) 
l = arr.tolist() #OR list()
print(l)
'''

#ndmin to set dimension of an array
'''
arr = np.array([1,2,3,4],ndmin = 4) 
print(arr)
print(arr.ndim) 

arr1 = np.array([[1,2,3,4],[5,6,7,8]],ndmin = 2)
print(arr1)
print(arr1.ndim)
'''

#accessing elements
'''
arr = np.array([1,2,3,4])
print(arr[-1])
print("no. of dimensions:",arr.ndim)

arr1 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr1[1,1],arr1[-1,-3])
print(arr1.ndim)
'''

#accesing elements by slicing
'''
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr1[0:2,1:4])
print(arr1.ndim)

arr2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr2[1:3,2:5])
print(arr2[-1:-3:-1,-2:-5:-1])
'''

#converting data type on existing arrays
'''
import numpy as np
a = np.array([1.1,2.1,3.1])
b = a.astype(int)
print(b)             
print(b.dtype)

import numpy as np
arr = np.array([1,0,2,0])
arr1 = arr.astype(bool)
print(arr1)
print(arr1.dtype)
'''

#data type of array and datatype of elements
'''
a = np.array([1,2,3,4])
print(type(a))
print(a.dtype)
'''

#creating array with a defined data type
'''
arr = np.array([1,2,3,4], dtype=float)
print(arr)
'''

#a.copy() and a.view()
'''
a = np.array([1,2,3,4])
b = a.copy()
a[0] = 42
print(a)
print(b)

a = np.array([1,2,3,4])
b = a.view()
a[0] = 42
print(a)
print(b)
'''

#b.base
'''
arr1 = np.array([1,2,3,4,5])
arr2 = arr1.reshape(5,1)
print(arr2.base)

arr1 = np.array([1,2,3,4,5])
arr2 = arr1.reshape([5,1])
print(arr2.base)

arr1 = np.array([1,2,3,4,5])
arr2 = arr1[1:4]
print(arr2.base)

arr1 = np.array([1,2,3,4,5])
print(arr1.base)
'''

#shape of an array ~.shape()
'''
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)

a = np.array([1,2,3,4], ndmin = 5)
print(a)             
print(a.shape)
'''

#reshaping arrays ~.reshape()
'''
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b = a.reshape(4,3)
print(b)
'''

#unknown dimension
'''
a = np.array([1,2,3,4,5,6,7,8])
b = a.reshape(2,2,-1)
print(b) #2*2*x=8
print(b.shape)
'''

#flattening the arrays
'''
a = np.array([[1,2,3,4],[5,6,7,8]])
b = a.reshape(-1)
print(b)
'''

#transpose of array
'''
a = np.array([[1,2,3],[4,5,6]])
b = a.transpose() 
c = np.transpose(a)
d = a.T
print(b)
print(c)
print(d)
'''
#some kind of flattening and base
'''
a = np.array([[[2,5,1],[6,4,3]],[[2,5,1],[6,4,3]]])
b = a.flatten()
c = a.ravel()
d = a.reshape(-1)
e = a.reshape((4,3))
print(b)
print(c)
print(d)
print(e)
print(a.base)
print(b.base)
print(c.base)
print(d.base)
print(e.base)
'''

#hstack abd vstack
'''
arr1 = [1,2,3]
arr2 = [4,5,6]
arr3 = np.hstack((arr1,arr2))
print(arr3)
arr4 = np.vstack((arr1,arr2))
print(arr4)
'''

#randint working with numpy
'''
arr1 = np.random.randint(10,19,9).reshape(3,3)
arr2 = np.random.randint(10,19,9).reshape(3,3)
arr3 = np.hstack((arr1,arr2))
arr4 = np.vstack((arr1,arr2))
print(arr1)
print(arr2)
print(arr3)
print(arr4)
'''

'''
print(np.arange(-10,10,2))
print(np.zeros(5))
print(np.zeros((4,3)))
print(np.ones(5))
print(np.ones(5, dtype=int))
print(np.ones((2,3,4),dtype=int))
'''

'''
a = np.array([[1,2],[3,4,9]])
b = np.array([[5,10,6]])
x = np.concatenate((a,b),axis=0)
print(x)
b = b.reshape(2,1)
y = np.concatenate((a,b),axis=1)
print(y)
z = np.concatenate((a,b),axis=None)
print(z)
'''

'''
a = np.arange(1.5,10.2,2, dtype=int)
print(a)
'''

'''
print(np.random.rand())
print(np.random.rand(5))
print(np.random.rand(2,5))
print(np.random.rand(2,5,3))
'''

'''
print(np.eye(4))
print(np.eye(5,3,1))
print(np.eye(5,3,2))
print(np.eye(5,3,3))
'''

'''
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
'''

'''
a = np.array([[1,2],[3,4]])
b = np.array([[2,1],[4,3]])
print(a@b)
print(np.dot(a,b))
'''

#numpy Arrays are memory efficient
'''
import sys
l = [1,2,3,4]
arr = np.array(l)
memoryTakenByArr = arr.itemsize*arr.size
memoryTakenByL = sys.getsizeof(l)*len(l)
print(memoryTakenByArr)
print(memoryTakenByL)
'''

#numpy arrays are fast
'''
import time
l1 = range(1000000)
l2 = range(1000000)
start = time.time()
l3 = [(i,j) for i,j in zip(l1,l2)]
end = time.time()
print("time taken by list", end-start)

arr1 = np.arange(1000000)
arr2 = np.arange(1000000)
start = time.time()
arr3 = arr1 + arr2
end = time.time()
print("time taken by array", end-start)
'''
