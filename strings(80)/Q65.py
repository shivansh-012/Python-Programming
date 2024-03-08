string1 = input("Enter the first lowercase string: ")
string2 = input("Enter the second lowercase string: ")

# Convert strings to sets to find common characters
set1 = set(string1)
set2 = set(string2)

# Find the common characters
common_characters = sorted(set1.intersection(set2))

# Check if there are common characters
if common_characters:
    # Print the common characters in lexicographical order
    print("Common characters in lexicographical order:", ''.join(common_characters))
else:
    print("No common characters")
