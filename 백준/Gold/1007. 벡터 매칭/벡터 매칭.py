from sys import stdin
from itertools import combinations

cases = int(stdin.readline())
dist = 0
for _ in range(cases):
    x_lst = []
    y_lst = []
    leng = int(stdin.readline())
    for _ in range(leng):
        x,y = map(int,stdin.readline().strip().split())
        x_lst.append(x)
        y_lst.append(y)
    dist = float('inf')
    
    for i in combinations(range(leng),leng//2):
        xs,ys = 0,0
        for j in range(leng):
            if j in i:
                xs += x_lst[j]
                ys += y_lst[j]
            else:
                xs -= x_lst[j]
                ys -= y_lst[j]
                
        dist = min(dist,xs**2+ys**2)
        
    print(dist**(1/2))