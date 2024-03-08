string1 = input()
for char in string1:
    if string1.count(char) > 1:
        print(char,"is the first repeating element")
        break
    