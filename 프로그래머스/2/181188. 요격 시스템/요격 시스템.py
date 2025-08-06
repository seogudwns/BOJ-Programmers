def solution(targets):
    answer = 0
    criteria = -1
    targets.sort(key=lambda x:x[1])
    for s,e in targets:
        if criteria < s:
            answer += 1
            criteria = e - 0.5
    return answer