def solution(ineq, eq, n, m):
    return 1 if ( n > m and ineq == ">" ) or ( n < m and ineq == "<" ) or ( n == m and eq == "=" ) else 0