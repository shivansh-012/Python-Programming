def flatten_list(input_list):
    flattened = []
    for item in input_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

shallow_list = [1, [2, 3, [4, 5], 6], 7, [8, 9]]
flattened_list = flatten_list(shallow_list)
print(f"flattened list {flattened_list}")