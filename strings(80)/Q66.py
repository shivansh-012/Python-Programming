string1 = input("Enter the first lowercase string: ")
string2 = input("Enter the second lowercase string: ")

# Convert strings to lists for easier removal of characters
list1 = list(string1)
list2 = list(string2)

# Iterate through characters in the first string
for char in string1:
    if char in list2:
        # Remove the common character from both lists
        list1.remove(char)
        list2.remove(char)

# Concatenate the modified lists to form the anagrams
anagram1 = ''.join(list1)
anagram2 = ''.join(list2)

# Print the anagrams
print("Anagram 1:", anagram1)
print("Anagram 2:", anagram2)
