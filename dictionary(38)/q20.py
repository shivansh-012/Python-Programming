l = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
r = []
for dic in l:
    for v in dic.values():
        r.append(v)

r = set(r)        
print(r)