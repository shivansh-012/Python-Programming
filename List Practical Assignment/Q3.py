m1, n1=map(int, input("ENTER ROW AND COLUMN SIZE FOR MATRIX A: ").split())
matrixA=[]
print("enter ", m1*n1, " elements:")
for i in range(m1):
    t=[]
    for j in range(n1):
        t.append(int(input()))
    matrixA.append(t)
for i in range(m1):
    for j in range(n1):
        print(matrixA[i][j],end=" ")
    print()

m2, n2=map(int, input("ENTER ROW AND COLUMN SIZE FOR MATRIX B: ").split())
matrixB=[]
print("enter ", m2*n2, " elements:")
for i in range(m2):
    t=[]
    for j in range(n2):
        t.append(int(input()))
    matrixB.append(t)
for i in range(m2):
    for j in range(n2):
        print(matrixB[i][j],end=" ")
    print()
#matrix multiplication !
res=[]
for i in range(m1):
    for j in range(n2):
        result = 0
        for k in range(m2):
            result += matrixA[i][k] * matrixB[k][j]
        res.append(result)
print(res)