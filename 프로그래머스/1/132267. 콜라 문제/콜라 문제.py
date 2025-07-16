def solution(a, b, n):
    answer = 0
    while n>=a:
        newB = n//a*b
        answer += newB
        n = newB+n%a
        
    return answer