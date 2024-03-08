n=int(input())
for i in range(0,10):
    count =0
    p= n
    while(p>0):
        digit=p%10
        if digit==i:
            count+=1
        p//=10
    if(count>0):
        print("no. of",i,"are :",count)