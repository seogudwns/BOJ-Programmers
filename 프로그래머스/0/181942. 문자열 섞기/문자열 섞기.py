def solution(a, b):
    return ''.join(b[i//2] if i%2 else a[i//2] for i in range(len(a)*2)) 