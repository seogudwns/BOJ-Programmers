def solution(wallpaper):
    n,m = len(wallpaper),len(wallpaper[0])
    answer = [51,51,0,0]

    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                answer[0] = min(i,answer[0])
                answer[1] = min(j,answer[1])
                answer[2] = max(i+1,answer[2])
                answer[3] = max(j+1,answer[3])
    
#     for j in range(m):
#         for i in range(n):
#             if wallpaper[i][j] == '#':
#                 answer[1] = j
#                 break
    
#     for i in range(n-1,-1,-1):
#         for j in range(m-1,-1,-1):
#             if wallpaper[i][j] == '#':
#                 answer[2] = i+1
#                 break
    
#     for j in range(m-1,-1,-1):
#         for i in range(n-1,-1,-1):
#             if wallpaper[i][j] == '#':
#                 answer[3] = j+1
#                 break
    
    return answer