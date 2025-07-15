def solution(t, p):
    curr = int(t[:len(p)])
    unit = 10**(len(p)-1)
    answer = 1 if int(p)>=curr else 0
    
    for i in range(len(p),len(t)):
        curr = curr%unit * 10 + int(t[i])
        if int(p) >= curr:
            answer += 1
    
    return answer