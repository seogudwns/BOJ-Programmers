def solution(n):
    answer = [n]
    while answer[-1] != 1:
        answer.append(3*answer[-1]+1 if answer[-1]%2 else answer[-1]//2)
    return answer