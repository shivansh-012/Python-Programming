my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

res = 1
for num in my_list:
    res*=num

print(res)