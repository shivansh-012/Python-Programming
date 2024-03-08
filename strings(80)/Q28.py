string = ("enter a string: \nenter anything \nenter what u wanna")
prefix = input("enter prefix to be entered: ")

lines = string.split("\n")
entered_lines = []
for line in lines:
    entered_lines.append(prefix + line)

result = '\n'.join(entered_lines)
print(result)