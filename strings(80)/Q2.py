string = "google.com"
char_frequency = {}
for char in string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(f"Character Frequencies for {string}: {char_frequency}")
for k,v in char_frequency.items():
    print("key = {}\t its occurences = {}".format(k,v))