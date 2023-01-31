from sys import stdin
n = int(stdin.readline())
lines,dp = sorted(tuple(map(int,stdin.readline().strip().split())) for _ in range(n)),[0 for _ in range(501)]
for l,r in lines: dp[r] = 1+max(dp[:r])
print(n-max(dp))