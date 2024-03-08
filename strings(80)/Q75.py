from collections import defaultdict

def smallest_window(input_str):
    char_count = defaultdict(int)
    unique_chars = set(input_str)

    required_chars = len(unique_chars)
    current_chars = 0
    start, start_index, min_len = 0, -1, float('inf')

    for end, char in enumerate(input_str):
        char_count[char] += 1

        if char_count[char] == 1:
            current_chars += 1

        # Try to minimize the window
        while current_chars == required_chars:
            if end - start + 1 < min_len:
                min_len = end - start + 1
                start_index = start

            char_count[input_str[start]] -= 1

            if char_count[input_str[start]] == 0:
                current_chars -= 1

            start += 1

    if start_index == -1:
        return "No valid window found"
    else:
        return input_str[start_index:start_index + min_len]

# Example usage:
input_str = "ADOBECODEBANC"
result = smallest_window(input_str)
print("Smallest window:", result)
