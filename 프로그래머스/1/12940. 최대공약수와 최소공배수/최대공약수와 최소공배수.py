def solution(n, m):
    def gcd(n, m):
        while m != 0: n, m = m, n % m
        return n

    return [(x:=gcd(n,m)),n*m//x]