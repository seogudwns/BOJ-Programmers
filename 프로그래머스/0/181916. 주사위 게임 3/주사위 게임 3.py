from collections import Counter

def solution(a, b, c, d):
    chk = Counter()
    chk[a] += 1
    chk[b] += 1
    chk[c] += 1
    chk[d] += 1
    dif = sorted(chk,key=lambda x:chk[x])
    if len(chk) == 1:
        return dif[0]*1111
    elif len(chk) == 2:
        return (10*dif[1]+dif[0])**2 if chk[dif[0]] == 1 else sum(dif)*abs(dif[1]-dif[0])
    elif len(chk) ==3: 
        return dif[0]*dif[1]
    else:
        return min(dif)
    
    return 0