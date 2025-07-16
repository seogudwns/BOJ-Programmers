def solution(lines):
    chk = [0 for _ in range(301)]
    for i,j in lines:
        chk[i+150] += 1
        chk[j+150] -= 1
    
    for i in range(300):
        chk[i+1] += chk[i]
        
    return sum(1 for i in chk if i>1)