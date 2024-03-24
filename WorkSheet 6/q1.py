l = [1, 2, 1, 2, 3, 5, 6, 7]
dict_freq = {}
for ele in l:
    if ele not in dict_freq:
        dict_freq[ele]=1
    else:
        dict_freq[ele]+=1
    
print(dict_freq)