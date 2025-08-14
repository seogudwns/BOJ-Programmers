def solution(maps):
    maps = [[i for i in j] for j in maps]
    n,m = len(maps),len(maps[0])
    answer = []
    q = []
    rot = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X':
                tmp = int(maps[i][j])
                maps[i][j] = 'X'
                q.append((i,j))
                while q:
                    cx,cy = q.pop()
                    for lr,ud in rot:
                        nx,ny = cx+lr,cy+ud
                        if 0<=nx<n and 0<=ny<m and maps[nx][ny] != 'X':
                            tmp += int(maps[nx][ny])
                            maps[nx][ny] = 'X'
                            q.append((nx,ny))
                
                answer.append(tmp)
    
    return sorted(answer) if answer else [-1]