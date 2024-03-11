from itertools import permutations

num_list = [int(x) for x in input("enter no.s separated by space").split()]
perm = permutations(num_list)
perm_list = list(perm)
# perm_list = [list(p) for p in perm]
print(perm_list)