from collections import Counter

def solution(array):
    chk = Counter(array)
    chk2 = sorted(chk,key=lambda x:chk[x])
    return chk2[-1] if len(chk) == 1 or chk[chk2[-1]]>chk[chk2[-2]] else -1