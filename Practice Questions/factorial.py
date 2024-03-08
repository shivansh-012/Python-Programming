from itertools import permutations
def perm(nums):
    return list(permutations(nums))

nums = eval(input())
result = perm(nums)
print(result)