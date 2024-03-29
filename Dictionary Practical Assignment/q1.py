A = [2, 6, 3, 8, 2, 8, 2, 3, 8, 8]
B = 2
freq_dict = {}
for n in A:
    if n not in freq_dict:
        freq_dict[n]=1
    else:
        freq_dict[n]+=1
    
print(freq_dict[B])