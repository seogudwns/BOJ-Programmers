from sys import stdin

N,M,K = map(int,stdin.readline().strip().split())

nums = [int(stdin.readline().strip()) for _ in range(N)]

segtree = [0]*20000000 # 6 log 10 <= 20

def inittree(idx,start,end):
    if start == end:
        segtree[idx] = nums[start]
        return segtree[idx]
    else:
        segtree[idx] = inittree(2*idx,start,(start+end)//2) + inittree(2*idx+1,(start+end)//2+1,end)
        return segtree[idx]

inittree(1,0,N-1)

def updatetree(idx,idx2,diff,start,end):
    if idx2 < start or idx2 > end:
        return 

    segtree[idx] += diff
    
    if start!=end:
        updatetree(idx*2,idx2,diff,start,(start+end)//2)
        updatetree(idx*2+1,idx2,diff,(start+end)//2+1,end)

def value_sum(idx,start,end,stt,ed):
    if end < stt or ed < start:
        return 0
    
    elif stt <= start and end <= ed:
        return segtree[idx]
    
    else:
        return value_sum(idx*2,start,(start+end)//2,stt,ed) + value_sum(idx*2+1,(start+end)//2+1,end,stt,ed)

for _ in range(M+K):
    a,b,c = map(int,stdin.readline().strip().split())
    if a == 1:
        diff = c - nums[b-1]
        nums[b-1] = c
        updatetree(1,b-1,diff,0,N-1)
        
    else:
        print(value_sum(1,0,N-1,b-1,c-1))
