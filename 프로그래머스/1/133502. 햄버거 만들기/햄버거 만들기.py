def solution(ingredient):
    answer = 0
    chk = []
    for i in ingredient:
        if len(chk)>2 and i == 1 and chk[-1] == 3 and chk[-2] == 2 and chk[-3] == 1:
            answer += 1
            for _ in range(3): chk.pop()
        else:
            chk.append(i)
    return answer