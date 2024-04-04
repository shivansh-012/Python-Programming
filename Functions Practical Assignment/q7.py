from math import ceil
def areaofEllipse(a, b):
    r = 3.14*a*b
    return ceil(r)

a = int(input())
b = int(input())
print(areaofEllipse(a, b))