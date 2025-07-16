rot = [(0,1),(1,0),(0,-1),(-1,0)]
def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    curr,loc,nsq,dirc = 1,[0,0],n**2+1,0
    while curr < nsq:
        answer[loc[0]][loc[1]] = curr

        curr += 1
        nex = [loc[0]+rot[dirc][0],loc[1]+rot[dirc][1]]
        if (nex[0]<0 or nex[0] == n or nex[1]<0 or nex[1] == n) or answer[nex[0]][nex[1]]:
            dirc = (dirc+1)%4
            nex = [loc[0]+rot[dirc][0],loc[1]+rot[dirc][1]]

        loc = nex
        
    [print(i) for i in answer]
    return answer