'''
    *
   ---
  *****
 -------
*********
 -------
  *****
   ---
    *
'''

n = int(input())
for i in range(0,n):
    if i%2==0:
        print((n-i-1)*" "+(2*i+1)*"*")
    else:
        print((n-i-1)*" "+(2*i+1)*"-")

for i in range(n-1,0,-1):
    if i%2==0:
        print((n-i)*" "+(2*i-1)*"-")
    else:
        print((n-i)*" "+(2*i-1)*"*")