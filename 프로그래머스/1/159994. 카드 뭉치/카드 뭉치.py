def solution(cards1, cards2, goal):
    answer = ''
    c1,c2 = 0,0
    for i in goal:
        if c1<len(cards1) and c2<len(cards2):
            if cards1[c1] == i:
                c1 += 1
            elif cards2[c2] == i:
                c2 += 1
            else:
                return "No"
        elif c1<len(cards1):
            if cards1[c1] == i:
                c1 += 1
            else:
                return "No"
        else:
            if cards2[c2] == i:
                c2 += 1
            else:
                return "No"
            
    return "Yes"