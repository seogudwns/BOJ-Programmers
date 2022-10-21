from sys import stdin
from itertools import permutations

n = int(stdin.readline())
lst = map(int,stdin.readline().strip().split())

def calc(lst):
    global n
    res = 0
    for i in range(n-1):
        res += abs(lst[i]-lst[i+1])
    return res

res = 0
for i in permutations(lst):
    curr = calc(i)
    if res<curr:
        res = curr

print(res)