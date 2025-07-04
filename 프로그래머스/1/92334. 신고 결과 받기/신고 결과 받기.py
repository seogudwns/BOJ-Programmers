def solution(id_list, report, k):
    singoSet = {i:set() for i in id_list}
    banCntSet = {i:0 for i in id_list}
    for i in report:
        x,y = i.split(" ")
        if y not in singoSet[x]:
            singoSet[x].add(y)
            banCntSet[y] += 1
        
    banCntSet = {i for i in banCntSet if banCntSet[i]>=k}
    
    return [len(singoSet[i] & banCntSet) for i in id_list]
    