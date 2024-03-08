string = input("Enter a string: ")

result = 0
length = len(string)

for i in range(length):
    for j in range(i, length):
        # Check if the first and last characters of the substring are the same
        if string[i] == string[j]:
            result += 1

print("Number of substrings with the same first and last characters: {}".format(result))
