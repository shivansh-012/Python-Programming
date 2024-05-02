def highest_three_values(dictionary):
    # Sort the dictionary based on values in descending order
    sorted_values = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    
    # Extract the top three values
    highest_three = sorted_values[:3]
    
    return highest_three

# Example dictionary
dictionary = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}

# Get the highest three values
result = highest_three_values(dictionary)

# Print the result
print("Highest three values in the dictionary:")
for key, value in result:
    print(key, ":", value)
