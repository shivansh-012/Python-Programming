input_list = [1, 2, 2, 3, 4, 4, 5]
n = len(input_list)

i = 0
while i<n:
    j=i+1
    while j<n:
        if input_list[i] == input_list[j]:
            input_list.pop(j)
            n-=1
        else:
            j+=1
    i+=1

print(input_list)