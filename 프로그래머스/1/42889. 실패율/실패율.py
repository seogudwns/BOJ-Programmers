def solution(N, stages):
    chk = [0 for _ in range(N+2)]
    for i in stages: chk[i] += 1
    for i in range(N+1,0,-1): chk[i-1] += chk[i]
    print(chk)
    
    return sorted([i for i in range(1,N+1)],key=lambda x: (-(chk[x]-chk[x+1])/chk[x] if chk[x] != 0 else 0,x))