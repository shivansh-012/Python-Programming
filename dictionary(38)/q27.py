def list_to_nested_dict(keys_list, value):
    if len(keys_list) == 1:
        return {keys_list[0]: value}
    else:
        return {keys_list[0]: list_to_nested_dict(keys_list[1:], value)}

# Example usage:
keys = ['a', 'b', 'c']
value = 1
nested_dict = list_to_nested_dict(keys, value)
print(nested_dict)
