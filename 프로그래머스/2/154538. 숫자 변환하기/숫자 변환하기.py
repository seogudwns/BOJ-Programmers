def solution(x, y, n):
    curr,nex = [x],[]
    if x == y:
        return 0
    alr = set()
    answer = 0
    while curr:
        answer += 1
        while curr:
            x = curr.pop()
            if x in alr: continue
            alr.add(x)
            tmp = [x+n,x*2,x*3]
            for i in tmp:
                if i < y:
                    nex.append(i)
                if i == y:
                    return answer
        curr,nex = nex,[]
    return -1