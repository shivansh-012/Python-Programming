string = input()
max_char = ""
max_count = 0
for char in string:
    if string.count(char) > max_count:
        max_char = char
        max_count = string.count(char)

print(max_char,max_count)