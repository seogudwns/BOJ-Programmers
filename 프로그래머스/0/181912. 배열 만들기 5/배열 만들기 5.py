def solution(intStrs, k, s, l):
    return [x for i in intStrs if (x:=int(i[s:s+l]))>k]