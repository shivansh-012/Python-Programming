s = "My name is Tony"
res_str = " ".join([ele[::-1] for ele in s.split()])
print(res_str)