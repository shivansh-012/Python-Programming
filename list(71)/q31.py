my_list = [1, 5, 10, 15, 20, 25, 30]
start_range = 10
end_range = 25
count = 0
for ele in my_list:
    if start_range <= ele <= end_range:
        count+=1

print(f"the no. of elements in the given range are {count}")
