o_string = input("Enter a string: ")
char_remo = input("Enter chars to be removed: ")

# translation_table = str.maketrans('','',char_remo)
# stripped_string = o_string.translate(translation_table)
# print(stripped_string)

str = ""
for char in o_string:
    if char not in char_remo:
        str+=char

print(str)