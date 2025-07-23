def solution(arr):
    return [-1] if 2 not in arr else [2] if arr.count(2) == 1 else arr[arr.index(2):] if arr[-1] == 2 else arr[arr.index(2):-arr[::-1].index(2)]