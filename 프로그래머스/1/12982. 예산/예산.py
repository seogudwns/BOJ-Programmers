def solution(d, budget):
    d = sorted(d,reverse=True)
    ans,used = 0,0
    while d and budget>=used+d[-1]:
        used+=d.pop()
        ans += 1
    
    return ans