from collections import deque

def solution(n, edge):
    check = [False for _ in range(n+1)]
    grp = dict()
    for l,r in edge:
        if l not in grp:
            grp[l] = [r]
        else:
            grp[l].append(r)
            
        if r not in grp:
            grp[r] = [l]
        else:
            grp[r].append(l)
    
    curr = 0
    answer = 0
    
    Q = deque([(1,0)])
    while Q:
        x,leng = Q.popleft()
        if check[x]:
            continue
        check[x] = True
        
        if leng>curr:
            answer = 1
            curr = leng
        elif leng == curr:
            answer += 1
        
        for i in grp[x]:
            if not check[i]:
                Q.append((i,leng+1))
                
    return answer