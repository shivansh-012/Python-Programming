'''
      1
    2 3 2
  3 4 5 4 3
4 5 6 7 6 5 4
'''
n = int(input())
p = 1
for i in range(1,n+1):
  print((2*n-2*i)*' ', end=' ')
  for j in range(i,2*i):
    print(j,end=' ')    
  for k in range(2*i-2,i-1,-1):
    print(k,end=' ')
  print()