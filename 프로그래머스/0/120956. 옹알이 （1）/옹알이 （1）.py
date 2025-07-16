unit = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    def bab(babble,idx):
        if len(babble) == idx:
            return True
        for i in unit:
            if babble[idx:idx+len(i)] == i:
                return bab(babble,idx+len(i))
        return False
    
    return sum(1 for i in babbling if bab(i,0))