word_list = ["apple", "banana", "grape", "kiwi", "orange", "strawberry"]
n = int(input("Enter the value of n: "))

filtered_words = [word for word in word_list if len(word) > n]

print("Words longer than", n, ":", filtered_words)
