from sys import stdin

N = int(stdin.readline())
for _ in range(int(stdin.readline())):
    a,b = map(int,stdin.readline().strip().split())
    N -= a*b

print("No" if N else "Yes")