from sys import stdin
import heapq

over,under = [],[]
res = 0

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n>0:
        heapq.heappush(over,-n)
    else:
        heapq.heappush(under,n)

while len(over)>1:
    x,y = heapq.heappop(over),heapq.heappop(over)
    res += x*y if y != -1 else -(x+y)
    
while len(under)>1:
    res += heapq.heappop(under)*heapq.heappop(under)

if over:
    res -= over[0]
if under:
    res += under[0]

print(res)