import math as m
    
c = int(input())
    
for i in range(c):
    [x1,y1,r1,x2,y2,r2] = list(map(int,input().split()))
    r3 = m.sqrt((x1-x2)**2+(y1-y2)**2)
    
    if (x1==x2 and y1==y2 and r1==r2):
        print(-1)
    elif r3>r1+r2 or r3<abs(r1-r2): 
        print(0)
    elif r3==r1+r2 or r3==abs(r1-r2):
        print(1)
    else: 
        print(2)