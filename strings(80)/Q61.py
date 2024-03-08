string1 = input()  # Get input string from the user

uni_char = []  # Initialize an empty list to store unique characters

# Iterate through the characters in the input string
for char in string1:
    # Check if the character is not already in the list of unique characters
    if char not in uni_char:
        # Add the character to the list
        uni_char.append(char)

# Join the characters in the list to form the final string without duplicates
string1 = "".join(uni_char)

# Print the result
print(string1)