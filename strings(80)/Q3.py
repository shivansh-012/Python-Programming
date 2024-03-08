string = input("enter a string: ")
if len(string)<2:
    print("Empty String")
else:
    print(string[0:2] + string[-2:])