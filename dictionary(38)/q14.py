dict1 = {"apple":5,"mango":9,"banana":1,"dragonfruit":7}
sorted_dict1 = dict(sorted(dict1.items(), key=lambda item:item[0]))
print(sorted_dict1)