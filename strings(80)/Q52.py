from itertools import product
input_str = input("Enter the string: ")
repetition = int(input("Enter the repetition number: "))
permutations = product(input_str, repeat=repetition)
# Print the permutations
for permutation in permutations:
    print(''.join(permutation))