def solution(arr):
    return [i*2 if i<50 and i%2 else i//2 if i>=50 and not i%2 else i for i in arr]