string = input()
words = string.split()
words1 = []
for word in words:
    if len(word)==1:
        wrd = word.upper()
    else:
        wrd = word[0].upper() + word[1:-1] + word[-1].upper()

    words1.append(wrd)

string = " ".join(words1)
print(string)