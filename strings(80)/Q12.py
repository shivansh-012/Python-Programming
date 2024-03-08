stringi = input("enter a string: ")
wordi = stringi.split(" ")
dicti = {}
for word in wordi:
    if word in dicti:
        dicti[word]+=1
    else:
        dicti[word]=1
print(dicti)