string = input()
words = string.split()
for word in words:
    if words.count(word)>1:
        print(word)
        break