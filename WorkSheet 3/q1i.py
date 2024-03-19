'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''

rows = int(input("enter row size: "))
triangle = []
for i in range(rows):
    row = [1]
    if i>0:
        prev_row = triangle[i-1]
        for j in range(1,i):
            row.append(prev_row[j-1]+prev_row[j])
        row.append(1)
    triangle.append(row)

for p in triangle:
    print(" ".join(str(num) for num in p))