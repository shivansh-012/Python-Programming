string = input()
ind = 1000
for i in range(len(string)):
    if string[i] in string[i+1:]:
        if string[i+1:].index(string[i]) < ind:
            ind = i

print(string[ind],ind)