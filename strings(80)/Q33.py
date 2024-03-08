integer = 123
# integer = str(integer)
# print(integer.rjust(5,"0"))
formatted_integer = "{:05d}".format(integer)
print(formatted_integer)
