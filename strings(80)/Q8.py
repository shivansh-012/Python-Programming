list=['a','ab','abc','abcdef','abcde']
max_len=0
for  word in list:
    if len(word) > max_len :
        max_len = len(word)
        max_word = word
print(max_word)