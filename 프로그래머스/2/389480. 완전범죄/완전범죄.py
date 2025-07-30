def solution(info, n, m):
    answer = n
    k = len(info)
    chk = {(0,0)}
    nex = set()
    for i,j in info:
        for a,b in chk:
            if a+i<n:
                nex.add((a+i,b))
            if b+j<m:
                nex.add((a,b+j))
        
        chk,nex = nex,set()
        if not chk: return -1
    
    return min(i for i,j in chk)
    
    # # 26, 34?.. sort로 쉽게 가는 방법은 허점이 있는듯..    
    # info = sorted(info,key=lambda x: (x[0],-x[1]))
    # print(info)
    # ans = 0
    # while info:
    #     x,y = info.pop()
    #     if m > y:
    #         m -= y
    #     elif n > x:
    #         n -= x
    #         ans += x
    #     else:
    #         return -1
    # return ans
