n = int(input())
bef,curr = 1,1

for _ in range(n-1):
    bef,curr = curr,(curr+bef)%15746

print(curr)