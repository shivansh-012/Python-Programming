alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string = input()
string = string.upper()
count = 0
for i in range(min(len(string),len(alphabets))):
    if string[i] == alphabets[i]:
        count+=1

print(count)