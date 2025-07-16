bal = ["aya", "ye", "woo", "ma"]
        
def solution(babbling):
    def chk(babble,index,bef):
        if len(babble) == index:
            return True
        for i in range(4):
            if i != bef and babble[index:index+len(bal[i])] == bal[i]:
                return chk(babble,index+len(bal[i]),i)
        return False
    
    return sum(1 for i in babbling if chk(i,0,-1))