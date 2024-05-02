input_dict = {'first name': 'John', 'last name': 'Doe', 'age': 30}
modified_dic = {}
for k, v in input_dict.items():
    nk = k.replace(' ', '')
    modified_dic[nk] = v

print(modified_dic)