import sys

a,b = map(str,sys.stdin.readline().strip().split(' '))

difcnt =[0 for i in range(len(b)-len(a)+1)]
for i in range(len(b)-len(a)+1):
    for j in range(len(a)):
        if b[i+j]!=a[j]:
            difcnt[i]+=1

print(min(difcnt))