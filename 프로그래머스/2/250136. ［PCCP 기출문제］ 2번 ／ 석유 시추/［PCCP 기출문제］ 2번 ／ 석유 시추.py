def solution(land):
    chk = [0 for _ in land[0]]+[0]
    n,m = len(land),len(land[0])
    rot = [(0,1),(1,0),(0,-1),(-1,0)]
        
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                curr,lr = 0,(j,j)
                q = [(i,j)]
                while q:
                    a,b = q.pop()
                    if not land[a][b]:
                        continue
                    land[a][b] = 0
                    curr += 1
                    lr = (min(lr[0],b),max(lr[1],b))
                    for x,y in rot:
                        na,nb = a+x,b+y
                        if 0<=na<n and 0<=nb<m and land[na][nb]:
                            q.append((na,nb))
                # print(lr,curr)
                chk[lr[0]] += curr
                chk[lr[1]+1] -= curr
    
    for i in range(len(land[0])):
        chk[i+1]+=chk[i]    

    return max(chk)