A = [1, 2, 3, 1, 2, 5]
freq_dict = {}
for n in A:
    if n not in freq_dict:
        freq_dict[n]=1
    else:
        freq_dict[n]+=1
    
for val in freq_dict:
    if freq_dict[val]==1:
        print(val)
        break