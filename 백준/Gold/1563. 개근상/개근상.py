n = int(input())

MOD = 10**6
l0,l1,l2 = [0,1],[0,1],[0,0]
l3,l4,l5 = [0,1],[0,0],[0,0]

for i in range(n-1):
    l0.append((l0[-1]+l1[-1]+l2[-1])%MOD)
    l2.append(l1[-1]) 
    l1.append(l0[-2])

    l3.append((l3[-1]+l0[-2]+l1[-2]+l2[-2]+l4[-1]+l5[-1])%MOD)
    l5.append(l4[-1])
    l4.append(l3[-2])

print((l0[-1]+l1[-1]+l2[-1]+l3[-1]+l4[-1]+l5[-1])%MOD)