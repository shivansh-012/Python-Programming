def checkPerfectSquare(a):
    sq = a**0.5
    if sq.is_integer():
        return int(sq)
    else:
        return -1

a = int(input())
res = checkPerfectSquare(a)
print(res)