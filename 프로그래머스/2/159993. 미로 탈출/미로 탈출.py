from collections import deque

def solution(maps):
    def dfs(maps,st,ed):
        rot = [(1,0),(0,1),(-1,0),(0,-1)]
        dirc_map = [[0]*len(maps[0]) for _ in maps]
        dirc_map[st[0]][st[1]] = -1
        n,m = len(maps),len(maps[0])
        q = deque()
        q.append((st[0],st[1],0))
        while q:
            x,y,dirc = q.popleft()
            for i,j in rot:
                nx,ny = x+i,y+j
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and not dirc_map[nx][ny]:
                    dirc_map[nx][ny] = dirc+1
                    q.append((nx,ny,dirc+1))
        # print(st,ed)
        # [print(i) for i in dirc_map]
        
        return dirc_map[ed[0]][ed[1]] if dirc_map[ed[0]][ed[1]] else -1
        
    s_loc,l_loc,e_loc = (-1,-1),(-1,-1),(-1,-1)
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S': s_loc = (i,j)  
            if maps[i][j] == 'L': l_loc = (i,j) 
            if maps[i][j] == 'E': e_loc = (i,j)
    
    ans = 0
    sl = dfs(maps,s_loc,l_loc)
    if sl == -1: 
        return -1
    else:
        ans += sl
    # print('-------------')
    le = dfs(maps,l_loc,e_loc)
    if le == -1:
        return -1
    else:
        ans += le
    return ans