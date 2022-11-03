from sys import stdin
 
n = int(stdin.readline())
check = []
for i in range(n):
    a,b = map(int,stdin.readline().strip().split())
    check.append([a,1])
    check.append([b,-1])

check = sorted(check)

cnt,maxi = 0,0
for t,c in check:
    cnt += c
    if c == 1:
        maxi = max(maxi,cnt)

print(maxi)