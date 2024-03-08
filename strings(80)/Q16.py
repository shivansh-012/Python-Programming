def insert_single_middle(string,insertstring):
    midindex = len(string)//2
    return string[:midindex] + insertstring + string[midindex:]

res1 = insert_single_middle("[[]]<<>>","Python")
res2 = insert_single_middle("{{}}","PHP")

print(res1)
print(res2)