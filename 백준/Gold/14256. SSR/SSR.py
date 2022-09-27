from math import sqrt

N,M = map(int,input().strip().split())

if N>M:
    temp = N
    N = M
    M = temp

temp =[i for i in range(1,int(sqrt(M))+1)]
temp2 = set([i**2 for i in range(1,int(sqrt(M))+1)])

result = 0

for i in range(1,N+1):
    c = i
    for j in temp[::-1]:
        if c%(j**2) == 0:
            c = c//(j**2)

    M1 = M//c
    result += len(set(range(1,M1+1)) & temp2)
    
print(result)