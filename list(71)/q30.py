from collections import Counter

input_list = [1, 2, 3, 1, 2, 1, 4, 5, 3, 2, 1]
freq_dict = Counter(input_list)
for ele,fre in freq_dict.items():
    print(f"element: {ele}, frequency: {fre}")
