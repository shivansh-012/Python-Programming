string = input("input ascii values with & as separator")
l = string.split('&')
l = [int(x) for x in l]
decoded_name = ''
for n in l:
    decoded_name+=chr(n)

print(decoded_name)