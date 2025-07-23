def solution(code):
    mode,answer = 0,""
    for i in range(len(code)):
        if code[i] == "1":
            mode += 1
        elif i%2 == mode%2:
            answer += code[i]
            
    return answer if answer else "EMPTY"