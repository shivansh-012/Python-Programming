#string slicing
string='ASTRING'

#using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print("String Slicing")
print(string[s1])
print(string[s2])
print(string[s3])

string='GEEKSFORGEEKS'

#using indexing sequence
print(string[:3])
print(string[1:5:2])
print(string[-1:-12:-2])

#prints string in reverse
print(string[::-1])

#prints characters from 3 to 7 skipping one character using islice()
import itertools
string='GEEKSFORGEEKS'
print(''.join(itertools.islice(string,3,7)))