words = input("enter a string: ").split()
set1 = set(words)
word_freq = {}
fre = []
for word in set1:
    word_freq[word]=words.count(word)
    fre.append(words.count(word))
list2 = sorted(list(set(fre)))
second_repeated = list2[-2]
for k,v in word_freq.items():
    if v==second_repeated:
        print(k,v)
            
#counts_x = sorted(counts.items(), key = lambda kv: kv[1])