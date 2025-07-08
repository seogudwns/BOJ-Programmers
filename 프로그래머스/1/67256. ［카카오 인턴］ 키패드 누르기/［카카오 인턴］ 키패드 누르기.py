def solution(numbers, hand):
    l,r = (0,3),(2,3)
    def chkLength(curr,loc):
        return abs(curr[0]-loc[0])+abs(curr[1]-loc[1])
    
    def compLength(l,r,loc):
        return "l" if chkLength(l,loc) < chkLength(r,loc) else "r" if chkLength(r,loc) < chkLength(l,loc) else hand[0]
    
    ans = []
    for i in numbers:
        if i in {1,4,7}:
            l = (0,i//3)
            ans.append("L")
        elif i in {3,6,9}:
            r = (2,(i-1)//3)
            ans.append("R")
        else:
            loc = (1,i//3) if i != 0 else (1,3)
            if compLength(l,r,loc) == "l":
                l = loc
                ans.append("L")
            else:
                r = loc
                ans.append("R")
    
    return "".join(ans)