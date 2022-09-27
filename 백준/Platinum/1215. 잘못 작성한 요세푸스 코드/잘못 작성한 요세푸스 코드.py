import math

n,k = map(int,input().strip().split())
x = int(math.sqrt(k))

c = 0

if k<=n:
    y = 0 
    z = 0

    for i in range(1,x+1):
        c += k//i * i
        c += ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2 * z
        y = k//i
        z = i

    c += ( (y + z+1) * (y - (z+1) + 1) )//2 * z
    
elif x<n:
    y = 0 
    z = 0
    for i in range(1,x+1):
        c += k//i * i
        if n >= k//i:
            c += ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2 * z
        y = min(k//i,n)
        z = i
    
    c += ( (y + z+1) * (y - (z+1) + 1) )//2 * z

else:
    for i in range(1,n+1):
        c += k//i*i

print(n*k - c)