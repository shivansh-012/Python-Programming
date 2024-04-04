import math
def volumeofSphere(a):
    b = (4*3.14*a**3)/3
    return math.ceil(b)

a = int(input())
res = volumeofSphere(a)
print(res)