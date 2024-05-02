string = 'w2resource'
count_dict = {}
for ch in string:
    if ch not in count_dict:
        count_dict[ch]=1
    else:
        count_dict[ch]+=1

print(count_dict)