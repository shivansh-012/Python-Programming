p,r = map(int, input().split())
t = 2
a = p*(1+r/100)**t
ci = a-p
print(ci)