from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    unit = list(map(int,stdin.readline().strip().split()))
    money = int(stdin.readline())
    dp = [0 for _ in range(money+1)]
    dp[0] = 1
    
    for i in range(n):
        uni = unit[i]
        for j in range(0,money+1-uni):
            dp[uni+j] += dp[j]
        
    print(dp[-1])