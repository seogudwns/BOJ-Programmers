import heapq

def solution(k, score):
    answer,chk = [],[]
    
    for i in range(min(k,len(score))):
        heapq.heappush(chk,score[i])
        answer.append(chk[0])
    
    for i in range(k,len(score)):
        if chk[0]<score[i]:
            heapq.heappop(chk)
            heapq.heappush(chk,score[i])
        answer.append(chk[0])
        
    return answer