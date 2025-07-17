def solution(quiz):
    answer = []
    for prob in quiz:
        prob = prob.split(" ")
        ans = int(prob.pop())
        prob.pop()
        n,curr = 2,int(prob[0])
        while n < len(prob):
            add = int(prob[n]) if prob[n-1] == "+" else -int(prob[n])
            curr += add
            n += 2
        
        answer.append("O" if ans == curr else "X")
        
    return answer