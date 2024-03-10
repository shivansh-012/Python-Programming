my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# largest = max(my_list)
# print(largest)

largest = my_list[0]
for num in my_list:
    if num>largest:
        largest = num

print(largest)