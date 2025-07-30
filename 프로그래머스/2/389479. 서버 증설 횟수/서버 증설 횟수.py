def solution(players, m, k):
    server_cnt = [0]*24
    ans = 0
    for i in range(24):
        chk = players[i]//m # i 시간에 필요한 서버 수.
        if chk>server_cnt[i]:
            chk2 = chk-server_cnt[i]
            for j in range(k):
                if i+j == 24: break
                server_cnt[i+j] += chk2
            ans += chk2
                
    # print(server_cnt)
    
    return ans