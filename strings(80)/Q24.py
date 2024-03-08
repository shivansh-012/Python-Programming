string = input("enter a string: ")
specified_characters = input("enter spec chars: ")
'''if string[:len(specified_characters)] == specified_characters:
    print("yes")
else:
    print('no')'''
if string.startswith(specified_characters):
    print("yes")
else:
    print("no")