def solution(a, b, c):
    return a+b+c if a != b and b != c  and c != a else (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3) if a == b == c else (a+b+c)*(a**2+b**2+c**2)