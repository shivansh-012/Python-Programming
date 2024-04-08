my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
uniq_dict = {}
for k,v in my_dict.items():
    if v not in uniq_dict.values():
        uniq_dict[k]=v

print(uniq_dict)