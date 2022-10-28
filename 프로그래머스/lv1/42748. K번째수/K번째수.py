def solution(array, commands):
    answer = []
    for l,r,n in commands:
        answer.append(sorted(array[l-1:r])[n-1])
    return answer