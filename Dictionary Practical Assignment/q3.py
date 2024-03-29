A = input()
freq_dict = {}
for ch in A:
    if ch not in freq_dict:
        freq_dict[ch]=1
    else:
        freq_dict[ch]+=1

odd_count = 0
for count in freq_dict.values():
    if count % 2 != 0:
        odd_count += 1

if odd_count<=1:
    print(1)
else:
    print(0)