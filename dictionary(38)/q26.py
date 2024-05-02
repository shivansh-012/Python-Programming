data =  [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
count_true = 0
for ele in data:
    if ele['success']==True:
        count_true+=1

print(count_true)