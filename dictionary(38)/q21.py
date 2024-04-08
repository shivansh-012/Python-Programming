from itertools import product

d ={'1':['a','b'], '2':['c','d']}

for x, y in product(*d.values()):
    print(x + y)
