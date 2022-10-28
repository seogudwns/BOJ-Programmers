def solution(n):
    num = 0
    for i in range(3*n):
        if not i%3 or '3' in str(i):
            continue
        num += 1
        if num == n:
            return i