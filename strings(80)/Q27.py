text = """    i am a good boy
              he is also a good boii
                  and i am fine"""
lines = text.split('\n')
strippedLines = []
for line in lines:
    strippedLines.append(line.lstrip())

text = '\n'.join(strippedLines)
print(text)