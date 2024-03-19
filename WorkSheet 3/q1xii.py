'''
7*8*9*10
4*5*6
2*3
1
'''
n = 4
p = 11
for i in range(n,0,-1):
    p-=i
    a = p
    for j in range(i):
        if j!=i-1:
            print(a,end="*")
        else:
            print(a)
        a+=1