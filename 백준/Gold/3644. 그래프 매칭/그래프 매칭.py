from sys import stdin

P = [0,0,3,4,7]

while True:
    n = stdin.readline().strip()
    if n == '':
        break
    
    n = int(n)
    
    if len(P)-1<n:
        for i in range(n-len(P)+1):
            P.append(P[-1]+P[-2])

    print(P[n])