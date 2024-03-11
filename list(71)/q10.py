word_list = ["apple", "banana", "grape", "kiwi", "orange", "strawberry"]
n = int(input("Enter the value of n: "))

for ele in word_list:
    if len(ele)<=n:
        word_list.remove(ele)

print("Words longer than", n, ":", word_list)
