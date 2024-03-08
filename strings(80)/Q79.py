# here i created a set to avoid duplication and created a list of words of string using split

words = input().split()
set1 = set(words)
lengths = []

# Collect lengths of words into the list
for word in set1:
    lengths.append(len(word))

# Sort the list of lengths
lengths = sorted(lengths)

# Iterate over the set and print the smallest and largest words
for word in set1:
    if len(word) == lengths[0]:
        print(f"smallest word: {word}")
    elif len(word) == lengths[-1]:
        print(f"largest word: {word}")
