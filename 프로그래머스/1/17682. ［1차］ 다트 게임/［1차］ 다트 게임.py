def solution(dartResult):
    chk = [0]
    for x in range(len(dartResult)):
        i = dartResult[x]
        if i.isdigit(): 
            if i == "1" and x < len(dartResult)-1 and dartResult[x+1] == "0": chk.append(10)
            elif i == "0" and x > 0 and dartResult[x-1] == "1": continue
            else: chk.append(int(i))
        if i == 'D': chk[-1] **= 2
        if i == 'T': chk[-1] **= 3
        if i == '*': 
            chk[-2] *= 2
            chk[-1] *= 2
        if i == '#':
            chk[-1] *= -1
        
    # print(chk)
    return sum(chk)