def solution(keymap, targets):
    answer = []
    X = 10**4+1
    chk = [X for _ in range(26)]
    for i in keymap:
        for j in range(len(i)):
            chk[ord(i[j])-65] = min(chk[ord(i[j])-65],j+1)
    
    # print(chk)
    
    for i in targets:
        tmp = 0
        for j in i:
            j = ord(j)-65
            if chk[j] == X:
                answer.append(-1)
                break
            tmp += chk[j]
        else:
            answer.append(tmp)
    
    return answer