# from collections import deque

# def solution(sequence, k):
#     q = deque()
#     answer = []
#     for i in range(len(sequence)):
#         for _ in range(len(q)):
#             x,val = q.popleft()
#             if val+sequence[i] < k:
#                 q.append((x,val+sequence[i]))
#             elif val+sequence[i] == k:
#                 answer.append([x,i])
        
#         if sequence[i] == k: return [i,i]
#         elif sequence[i] < k: q.append((i,sequence[i]))
    
#     return sorted(answer,key=lambda x: (len(x),x[0]))[0]
# # MLE 또는 TLE 나올 것 같음..

# def solution(sequence, k):
#     chk = [0]
#     for i in sequence:
#         chk.append(i+chk[-1])
#     leng = k
#     candid = []
#     for i in range(len(chk)):
#         for j in range(i,min(len(chk),i+leng)):
#             if chk[j]-chk[i] == k:
#                 leng = j-i
#                 if candid and candid[-1][-1]-candid[-1][-2]+1 >leng:
#                     candid.clear()
#                 candid.append([i,j-1])
#             elif chk[j]-chk[i] > k:
#                 break
                
#     return sorted(candid,key=lambda x: (x[1]-x[0],x[0]))[0]
# # TLE ..

# segment tree를 써야겠네..
# def solution(sequence, k):
#     n = len(sequence)
#     tree = [0]*(4*n)
#     def build(node, start, end):
#         if start == end:
#             tree[node] = sequence[start]
#         else:
#             mid = (start + end) // 2
#             build(2 * node, start, mid)
#             build(2 * node + 1, mid + 1, end)
#             tree[node] = tree[2 * node] + tree[2 * node + 1]
            
#     def query(node, start, end, l, r):
#         if r < start or end < l:
#             return 0  # 범위 밖
#         if l <= start and end <= r:
#             return tree[node]  # 완전히 포함
#         mid = (start + end) // 2
#         left_sum = query(2 * node + 1, start, mid, l, r)
#         right_sum = query(2 * node + 2, mid + 1, end, l, r)
#         return left_sum + right_sum

#     build(1,0,n-1)
#     # print(tree)

#     return [1,1]
# MLE 떨어질 것 같음 + 시간효율 엉망일듯..

def solution(sequence, k):
    r,n,interv = 0,len(sequence),k
    candid = []
    curr = 0
    for l in range(n):
        while curr < k and r < n:
            curr += sequence[r]
            r += 1
            if curr >= k: break
        if curr == k: 
            if r-l < interv:
                candid.clear()
                interv = r-l
            candid.append([l,r-1])
        curr -= sequence[l]

    return candid[0]
    