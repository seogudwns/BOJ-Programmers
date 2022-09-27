from sys import stdin

def make_min_val(idx,start,end):
    if start > end:
        return
    elif start == end:
        seg_tree[idx] = nums[start]
        return nums[start]
    
    seg_tree[idx] = min(make_min_val(2*idx, start, (start+end)//2), make_min_val(2*idx+1, (start+end)//2+1, end))
    
    return seg_tree[idx]

def update_min_val(idx, idx2, val, start, end):
    # print('checking_min_val_idx = ',idx)
    if start > end:
        return 1000000000 # 고정조건.
    
    elif start == end: #len == 1.
        if start == idx2: # 바꿔야하는 숫자의 index일 경우.
            seg_tree[idx] = val
            return val
        else: #그게 아니라면 값을 그대로 반환.
            return seg_tree[idx]
    
    elif start<=idx2<=(start+end)//2:
        seg_tree[idx] = min(update_min_val(2*idx, idx2, val, start, (start+end)//2),seg_tree[2*idx+1])
        return seg_tree[idx]
    
    elif (start+end)//2+1<=idx2<=end:
        seg_tree[idx] = min(seg_tree[2*idx],update_min_val(2*idx+1, idx2, val, (start+end)//2+1, end))
        return seg_tree[idx]

def get_idx(idx,val,start,end): #val = seg_tree[1].. 이걸 더 효율적으로 체크해야한다.
    global result
    # print('checking_get_idx = ',idx)
    if seg_tree[idx] == None or seg_tree[idx] != val or result != None:
        return # 쓸모없는 경우... 탐색의 순서상 result가 탐색이 되면(바로 아래 if문) 그게 재일 작은 값이 된다.
    
    # print('checking_get_idx2 = ',idx)
    if start == end and seg_tree[idx] == val:
            result = start 
            return
    
    get_idx(2*idx,val,start,(start+end)//2)
    get_idx(2*idx+1,val,(start+end)//2+1,end)
        

N = int(input())

nums = list(map(int,stdin.readline().strip().split()))

seg_tree = [None for _ in range(4*N)] # under 4*N.
make_min_val(1,0,N-1)

# print(seg_tree[:20])

M = int(input())

for _ in range(M):
    arr = stdin.readline().strip()
    if arr.startswith('1'):
        a,b,c = map(int,arr.split())
        update_min_val(1, b-1, c, 0, N-1)
        # print(seg_tree[:20])
        
    elif arr == '2':
        result = None
        get_idx(1,seg_tree[1],0,N-1)
        print(result+1)
