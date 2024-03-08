samplestring = 'thequickbrownfoxjumpsoverthelazydog'
characters = list(samplestring)
set1 = set(characters)
for char in set1:
    if characters.count(char) > 1:
        print(char,characters.count(char))
