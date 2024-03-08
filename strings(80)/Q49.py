text = input("enter : ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count+=1

vowels_res = [char for char in text if char in vowels]

print(count,vowels_res)