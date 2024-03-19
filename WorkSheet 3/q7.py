a = input()
v_count = 0
c_count = 0
d_count = 0
sp_count = 0
for ch in a:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            v_count+=1
        else:
            c_count+=1
    elif ch.isnumeric():
        d_count+=1
    elif ch.isspace():
        sp_count+=1

print(v_count,c_count,d_count,sp_count)