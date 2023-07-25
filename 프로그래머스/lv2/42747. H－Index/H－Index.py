def solution(citations):
    citations=sorted(citations,reverse=True)
    l,r = 0,len(citations)-1
    ans = 0

    while l<=r:
        mid = (l+r)//2
        if mid+1<=citations[mid]: 
            l = mid+1
            ans = mid+1
        else: 
            r = mid-1
    return ans

# def solution(A):
#     A.sort(reverse = True)
#     ans = 0
#     l,r = 0,len(A) -1
#     while l <= r:
#         mid = (l+r)//2
#         if mid + 1 <= A[mid]:
#             ans = mid + 1
#             l = mid + 1
#         else:
#             r = mid - 1
#     return ans