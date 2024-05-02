dic = {'b':1,'a':1,'z':12,'d':13}

dic = dict(sorted(dic.items(), key=lambda item:item[0]))
print(dic)