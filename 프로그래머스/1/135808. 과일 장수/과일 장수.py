def solution(k, m, score):
    answer = 0
    score = sorted(i for i in score)
    tmp = []
    while score:
        tmp.append(score.pop())
        if len(tmp) == m:
            answer += len(tmp)*(min(tmp+[k]))
            tmp = []
            
    return answer