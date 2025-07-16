def solution(numer1, denom1, numer2, denom2):
    def gcd(n,m):
        while m != 0: n,m = m,n%m
        return n
    r1,r2 = numer1*denom2+numer2*denom1,denom1*denom2
    
    return [r1/gcd(r1,r2),r2/gcd(r1,r2)]