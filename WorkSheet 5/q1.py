l_words = input().split()
x = input()[0]
res_ind_list = []
for i in range(len(l_words)):
    if x in l_words[i]:
        res_ind_list.append(i)
        
print(res_ind_list)