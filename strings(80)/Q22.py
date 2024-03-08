def lexicographically(string):
    sorted_string = "".join(sorted(string))
    return sorted_string

res = lexicographically(input("Enter a string: "))

print(res)