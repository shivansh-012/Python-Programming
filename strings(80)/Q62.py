input_string = input("Enter a string: ")

# Initialize the sum of digits
digit_sum = 0

# Iterate through the characters in the input string
for char in input_string:
    # Check if the character is a digit
    if char.isdigit():
        # Add the digit to the sum
        digit_sum += int(char)

# Print the sum of digits
print("Sum of digits in the string:", digit_sum)
