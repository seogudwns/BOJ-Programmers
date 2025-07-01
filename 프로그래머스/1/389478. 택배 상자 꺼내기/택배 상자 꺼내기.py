def solution(n, w, num):
    def upperNum(curr):
        h,r = divmod(curr,w)
        add = 2*(w-r)+1 if r != 0 else 1
        return curr+add
    
    ans = 0
    while num <= n:
        num = upperNum(num)
        ans += 1
    
    return ans
    
#     ans = 1 # self
    
#     # 기준 : 2*w
#     h1,r1 = divmod(n-1,2*w)
#     h2,r2 = divmod(num-1,2*w)
#     print(h1,r1,h2,r2)
    
#     ans += (h1-h2)*2
    
#     # 기준 : w
#     r1h,r1r = divmod(r1,w)
#     r2h,r2r = divmod(r2,w)
#     ans += r1h-r2h
#     print(ans)
    
#     # 기준 : 좌우위치
#     if r1h == 1: r1r = w-r1r-1
#     if r2h == 1: r2r = w-r2r-1
#     if r2r < r1r: ans -= 1
    
#     print(r1h,r1r,r2h,r2r)
    
#     return ans

# add testcase : 19 6 8 -> 2
# add testcase : 22 6 11 -> 2
# add testcase : 22 6 7 -> 3
# add testcase : 7 5 4 -> 2
# add testcase : 2 1 1 -> 2
# add testcase : 100 9 47 -> 6
# add testcase : 17 6 11 -> 1
# add testcase : 24 6 13 -> 2
# add testcase : 15 6 13 -> 1
# add testcase : 27 6 13 -> 3