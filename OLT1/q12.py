n1, n2 = map(int, input().split())
rem = n1 - n2*(n1//n2)
print(rem)