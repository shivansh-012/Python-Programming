my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# smallest = max(my_list)
# print(smallest)

smallest = my_list[0]
for num in my_list:
    if num<smallest:
        smallest = num

print(smallest)