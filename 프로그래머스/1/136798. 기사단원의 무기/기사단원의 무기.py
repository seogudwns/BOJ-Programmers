def solution(number, limit, power):
    def chkDivCnt(n): return sum(0 if n%i else 1 if i == n//i else 2 for i in range(1, int(n**(1/2)) + 1))
    return sum(x if (x:=chkDivCnt(num))<=limit else power for num in range(1,number+1))