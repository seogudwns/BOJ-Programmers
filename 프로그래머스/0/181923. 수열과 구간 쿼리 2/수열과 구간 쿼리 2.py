def solution(arr, queries):
    return [min(x) if len(x:=[arr[i] for i in range(s,e+1) if arr[i]>k]) else -1 for s,e,k in queries]