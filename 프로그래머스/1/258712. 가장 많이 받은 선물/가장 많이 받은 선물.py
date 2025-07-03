def solution(friends, gifts):
    cnt = {i:{i:0 for i in friends} for i in friends}
    idx = {i:0 for i in friends}
    for i in gifts:
        x,y = i.split(" ")
        cnt[x][y] += 1
        idx[x] += 1
        idx[y] -= 1
        
    chk = {i:0 for i in friends}
    for i in range(len(friends)):
        for j in range(i):
            if cnt[friends[i]][friends[j]] > cnt[friends[j]][friends[i]]:
                chk[friends[i]]+=1
            elif cnt[friends[i]][friends[j]] < cnt[friends[j]][friends[i]]:
                chk[friends[j]]+=1
            elif idx[friends[i]] > idx[friends[j]]:
                chk[friends[i]]+=1
            elif idx[friends[i]] < idx[friends[j]]:
                chk[friends[j]]+=1
    
    return max(chk.values())