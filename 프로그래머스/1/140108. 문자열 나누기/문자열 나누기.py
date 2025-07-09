def solution(s):
    answer = 0

    chk = []
    for i in s:
        if not chk:
            chk.append(i)
            chk.append(1)
            chk.append(0)
        else:
            if i == chk[0]:
                chk[1] += 1
            else:
                chk[2] += 1
                if chk[1] == chk[2]:
                    answer += 1
                    chk.clear()
                    
    if chk: answer += 1
    
    return answer