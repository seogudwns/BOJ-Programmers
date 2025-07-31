def solution(points, routes):
    answer = 0
    chk = {} # 기준 시간에 로봇의 위치.
    n = len(routes)
    routes = [i[::-1] for i in routes] # 목적지와 현재 위치를 위해서 내부 순서 변경.
    nex = [] # 다음 로봇의 위치
    curr = [tuple(points[i.pop()-1]) for i in routes] # 현재 로봇의 위치
    aim = [tuple(points[i.pop()-1]) for i in routes] # 현재에서 로봇이 가야할 목적지 위치, 다음 로봇의 위치가 목적지 위치와 동일할 경우 routes로부터 다음 목적지 위치를 받아옴. 
    out = (-1,-1) # 로봇이 목적지를 도착한 경우 좌표값 임의지정.
    
    def move_nex(curr,nex): # 로봇이 움직이는 로직 작성.
        return (curr[0]-1,curr[1]) if curr[0] > nex[0] else (curr[0]+1,curr[1]) if curr[0] < nex[0] else (curr[0],curr[1]-1) if curr[1] > nex[1] else (curr[0],curr[1]+1)
    
    for i in curr:
        if i not in chk: chk[i] = 0
        chk[i] += 1
    answer += len([i for i in chk if chk[i] > 1]) # 초기 로봇의 위치 및 충돌카운트 계산.

    while chk: # chk가 없다면 모든 로봇이 목적지까지 다 도착한 것이기 때문에 out.
        chk.clear()
        for i in range(n):
            if aim[i] != out and curr[i] != aim[i]: # 로봇의 현재 위치와 목적지가 다르다면..
                comp = move_nex(curr[i],aim[i]) # 로봇이 다음 위치 지정. 
                if comp == aim[i]: # 로봇의 다음 위치와 목적지가 같다면
                    if routes[i]: # 로봇의 다음 목적지가 남아있으면 다음위치 지정.
                        aim[i] = tuple(points[routes[i].pop()-1]) 
                    else: # 없으면 다음 루프에서 로봇탈출. ( for 문 아래 최상위 else에서 걸림. )
                        aim[i] = out 
                    
                if comp not in chk: chk[comp] = 0 
                chk[comp] += 1
                nex.append(comp) # 다음 로봇 위치 확인 및 충돌카운트 계산. 
            else: # 로봇이 목적지에 모두 도달하고 벗어난 경우.
                nex.append(out) # 빠져나간 로봇은 순서를 위해 out으로 받아줌.
                
        answer += len([i for i in chk if chk[i]>1]) # 로봇이 얼마나 충돌했는지 합산.
        # print(chk)
        curr,nex = nex,[] # 로봇 다음위치로 이동.
    
    return answer