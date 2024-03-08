string = input("enter a string: ")
if string[-3:] != "ing":
    string += "ing"
else:
    string += "ily"
print(string)