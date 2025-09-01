def solution(weights):
    weights_cnt = dict()
    for i in weights:
        if i not in weights_cnt: weights_cnt[i] = 0
        weights_cnt[i] += 1
        
    answer = 0        
    chk = sorted(weights_cnt)
    for i in range(len(chk)):
        answer += (weights_cnt[chk[i]]*(weights_cnt[chk[i]]-1))//2
        for j in range(i+1,len(chk)):
            if chk[i]*2<chk[j]: break
            if 4*chk[i] == 3*chk[j] or 3*chk[i] == 2*chk[j] or 2*chk[i] == chk[j]:
                answer += weights_cnt[chk[i]]*weights_cnt[chk[j]]
                
    return answer