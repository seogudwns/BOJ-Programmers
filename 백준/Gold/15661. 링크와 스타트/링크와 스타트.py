from sys import stdin

n = int(stdin.readline())

lst = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]
result = float('inf')

for i in range(1,(1<<n)):
    t1 = {j for j in range(n) if (1<<j) & i}
    t2 = {i for i in range(n) if i not in t1}
    team = 0
    for j in t1:
        for k in t1:
            team += lst[j][k]
    
    for j in t2:
        for k in t2:
            team -= lst[j][k]
    
    result = min(result,abs(team))

print(result)
    