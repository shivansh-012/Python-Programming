user_input = input("Enter a string: ")
n = int(input("Enter the number of characters to lowercase: "))
result_string = user_input[:n].lower() + user_input[n:]
print("Modified string:", result_string)
