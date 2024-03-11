row = 3
col = 4
depth = 6

thdlist = [[['*' for _ in range(depth)] for _ in range(col)] for _ in range(row)]

for i in range(row):
    for j in range(col):
        for k in range(depth):
            print(thdlist[i][j][k],end=' ')
        print()
    print()
    