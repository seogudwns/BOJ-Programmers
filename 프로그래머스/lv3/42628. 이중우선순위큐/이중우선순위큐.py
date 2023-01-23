import heapq

def solution(operations):
    lo,hi = [],[]
    for i in operations:
        if i.startswith('I'):
            heapq.heappush(hi,int(i[2:]))
        else:
            if hi or lo:
                if i[2] == '1':
                    while hi:
                        heapq.heappush(lo,-heapq.heappop(hi))
                    heapq.heappop(lo)
                else:
                    while lo:
                        heapq.heappush(hi,-heapq.heappop(lo))
                    heapq.heappop(hi)

    if hi or lo:
        res = sorted(hi+lo)
        return [res[-1],res[0]]
    
    return [0,0]