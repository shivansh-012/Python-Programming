password = input("enter a password: ")
shift = int(input("enter shift value: "))
enc_password = ""
for ch in password:
    if ch.isalpha():
        ch = chr(ord(ch) - shift)
    enc_password+=ch

print(enc_password)