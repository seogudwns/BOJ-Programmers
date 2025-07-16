def solution(today, terms, privacies):
    def chgDay(strD):
        a,b,c = strD.split(".")
        return [int(a),int(b)-1,int(c)-1]
    
    def compareD(unit,comp,interv):
        comp[1] += interv
        comp[2] -= 1
        if comp[2] < 0:
            comp[2] = 27
            comp[1] -= 1
        comp[0] += comp[1]//12
        comp[1] = comp[1]%12
        print(unit,comp)
        return unit[0]>comp[0] or (unit[0] == comp[0] and unit[1]>comp[1]) or (unit[0] == comp[0] and unit[1] == comp[1] and unit[2]>comp[2])
    
    today = chgDay(today)
    
    chk = {}
    for i in terms:
        a,b = i.split(" ")
        chk[a] = int(b)
    
    ans = []
    for i in range(len(privacies)):
        chkD,base = privacies[i].split(" ")
        chkD = chgDay(chkD)
        if compareD(today,chkD,chk[base]):
            ans.append(i+1)
    return ans