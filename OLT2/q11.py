def find_key_whose_value_is_max(dicn):
    if len(dicn)==0:
        return None
    else:
        a = max(dicn.values())
        for k,v in dicn.items():
            if v==a:
                return k

dic1 = {'x':100,'y':50,'z':75}
dic2 = {}
print(find_key_whose_value_is_max(dic1))
print(find_key_whose_value_is_max(dic2))