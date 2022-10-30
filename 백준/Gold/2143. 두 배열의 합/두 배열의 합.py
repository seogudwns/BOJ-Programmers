from sys import stdin
from collections import Counter

T = int(stdin.readline())
lenA = int(stdin.readline())
A = [0]+list(map(int,stdin.readline().strip().split()))
for i in range(lenA):
    A[i+1] += A[i]
A_calc = Counter(A[j]-A[i] for i in range(lenA) for j in range(i+1,lenA+1))
lenB = int(stdin.readline())
B = [0]+list(map(int,stdin.readline().strip().split()))
for i in range(lenB):
    B[i+1] += B[i]
B_calc = Counter(B[j]-B[i] for i in range(lenB) for j in range(i+1,lenB+1))

res = 0
for i in A_calc.keys():
    if T-i in B_calc:
       res += A_calc[i]*B_calc[T-i]
print(res)