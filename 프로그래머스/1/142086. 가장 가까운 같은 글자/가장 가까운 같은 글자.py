def solution(s):
    answer = []
    chk = {}
    for i in range(len(s)):
        if s[i] not in chk:
            answer.append(-1)
            chk[s[i]] = i
        else:
            answer.append(i-chk[s[i]])
            chk[s[i]] = i
    return answer