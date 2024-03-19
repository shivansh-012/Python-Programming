'''
    *
   --
  ***
 ----
*****
 ----
  ***
   --
    *
'''

n = int(input())
for i in range(1,n+1):
    if i%2!=0:
        print((n-i)*" ",i*"*")
    else:
        print((n-i)*" ",i*"-")

for i in range(1,n):
    if i%2!=0:
        print(i*" ",(n-i)*"-")
    else:
        print(i*" ",(n-i)*"*")
