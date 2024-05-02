data =  [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, 
{'item': 'item1', 'amount': 750}]

res_dict = {}
for ele in data:
    a = ele['item']
    if a not in res_dict:
        res_dict[a] = ele['amount']
    else:
        res_dict[a] += ele['amount']

print(res_dict)