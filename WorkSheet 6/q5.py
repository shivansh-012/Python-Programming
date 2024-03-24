s = "aeifAou102n3"
vowels, consonant, digits = 0, 0, 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonant+=1
    elif ch.isnumeric():
        digits+=1

print(vowels)
print(consonant)
print(digits)