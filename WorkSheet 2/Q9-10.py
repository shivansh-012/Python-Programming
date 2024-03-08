#Q9 : ans.= option5

sum = 0
for i in range(1,5):
    sum = sum + i
print(sum)
#Q10 : h would not be printed
for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter : ' + letter)