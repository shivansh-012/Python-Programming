a = input().split()
dict = {}
for word in a:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1

print(dict)