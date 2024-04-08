dict1 = {"apple":5,"mango":9,"banana":1,"dragonfruit":7}
sorted_dict1_in_asc = dict(sorted(dict1.items(), key=lambda item:item[1]))
sorted_dict1_in_desc = dict(sorted(dict1.items(), key=lambda item:item[1], reverse=True))
print(sorted_dict1_in_asc)
print(sorted_dict1_in_desc)