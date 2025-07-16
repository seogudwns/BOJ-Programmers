def solution(left, right):
    def chkDivCnt(n): return sum(0 if n%i else 1 if i == n//i else 2 for i in range(1, int(n**(1/2)) + 1))
    return sum(-i if chkDivCnt(i)%2 else i for i in range(left,right+1))