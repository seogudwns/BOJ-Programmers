def solution(plans):
    q = [] # 작업큐
    answer = []
    curr1,curr2,curr3,currT = '',0,0,0 # curr1 ~ curr3 : 이전 정보 저장. currT : 현재 시간.
    def chg_t(t):
        return int(t) if ":" not in t else int(t.split(":")[0])*60+int(t.split(":")[1])
        
    plans = sorted([(i,chg_t(j),chg_t(k)) for i,j,k in plans],key=lambda x: x[1]) # 계획 재정의.. 시간 숫자전환 및 시작시간으로 sort.
    # print(plans)
    
    for i,j,k in plans:
        # i : plan 명, j : 해당 플랜 시작시간, k : 해당 플랜 종료시까지 필요 시간.
        
        if curr2+curr3 <= j: # 이전에 진행중이던 업무가 현재 업무에 비교해서 끝난 경우
            if curr1: answer.append(curr1) # 초깃값 해징을 위한 if..
            curr1,currT = '',curr2+curr3 # 현재 시간은 curr1업무가 끝난 시간으로 변경.
            
        if curr1: # 해당 플랜을 처리하기 전 이전에 진행중이던 업무가 있다면 이전 업무는 q에 저장 후 새로운 업무 시작, 현재 시간은 업무시작시간으로 변경.
            q.append((curr1,curr2+curr3-j))
            curr1,curr2,curr3,currT = i,j,k,j
        elif q: # 이전에 진행중이던 업무가 끝난 상태인 경우, 해당 플랜을 처리하기 전 q에 남은 업무가 있다면 확인..
            while currT<j and q: 
                l1,l2 = q.pop()
                if currT+l2 <= j: # 잔여업무의 남은 시간에 현재시간의 합산이 업무 시작시간보다 적거나 같은 경우 업무 완료.
                    answer.append(l1)
                    currT += l2
                else: # 잔여업무의 남은 시간에 현재 시간의 합산이 업무시작시간보다 큰 경우, q에 남은 잔여업무시간을 다시 계산해서 삽입.
                    q.append((l1,l2-j+currT))
                    currT = j
                    
        curr1,curr2,curr3,currT = i,j,k,j
    
    # print(answer,curr1,q)
    
    # plans에 있는 업무가 끝난 이후..
    if curr1:
        answer.append(curr1)
    
    while q: # q가 남은 경우..
        l1,l2 = q.pop()
        answer.append(l1)
    
    return answer