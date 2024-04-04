A = [10, 5, 3, 4, 3, 5, 6]
res = -1
freq_dict = {}
for ch in A:
    if ch not in freq_dict:
        freq_dict[ch]=1
    else:
        freq_dict[ch]+=1

for k,v in freq_dict.items():
    if v>1:
        res = k
        break

print(res)