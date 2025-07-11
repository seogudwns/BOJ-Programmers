def solution(n, m, section):
    answer = 0
    curr = -1
    i = 0
    while i<len(section):
        x = section[i]
        if curr<=x:
            curr = x+m
            answer += 1
        i+=1
        
    return answer
    