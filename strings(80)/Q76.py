def count_substrings_with_k_distinct_chars(s, k):
    n = len(s)
    result = 0
    distinct_chars_count = 0
    char_count = [0] * 26  # Assuming only lowercase alphabets

    left, right = 0, 0

    while right < n:
        char_count[ord(s[right]) - ord('a')] += 1

        if char_count[ord(s[right]) - ord('a')] == 1:
            distinct_chars_count += 1

        while distinct_chars_count > k:
            char_count[ord(s[left]) - ord('a')] -= 1

            if char_count[ord(s[left]) - ord('a')] == 0:
                distinct_chars_count -= 1

            left += 1

        result += right - left + 1

        right += 1

    return result

# Example usage:
input_string = "abcabc"
k = 2
result = count_substrings_with_k_distinct_chars(input_string, k)
print(f"Number of substrings with exactly {k} distinct characters: {result}")
