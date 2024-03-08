string = "u can do what u can \nanything u wanna do \nin this world"
Indentation = "     "
lines = string.split('\n')
lines[0] = Indentation + lines[0]
result = '\n'.join(lines)
print(result)