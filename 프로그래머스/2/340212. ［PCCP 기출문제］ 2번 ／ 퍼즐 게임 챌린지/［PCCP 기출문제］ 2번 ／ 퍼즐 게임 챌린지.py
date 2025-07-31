def solution(diffs, times, limit):
    def chk_goal(level,limit):
        for i in range(len(diffs)):
            if level >= diffs[i]:
                limit -= times[i]
            else:
                limit -= (diffs[i]-level)*(times[i]+times[i-1])+times[i]
            if limit<0:
                return False
        return True
    
    l,r = 1,10**9+1
    while l<r:
        mid = int((l+r)/2)
        if chk_goal(mid,limit):
            r = mid
        else:
            l = mid+1
    
    return l