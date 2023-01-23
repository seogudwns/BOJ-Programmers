import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K:
        if len(scoville)<2:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville)+ 2*heapq.heappop(scoville))
        answer+=1
    return answer