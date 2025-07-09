def solution(s, skip, index):
    skip = {ord(i)-97 for i in skip}
    
    def chgN(curr):
        curr = ord(curr)-97
        tmp = index
        while tmp:
            curr = (curr + 1)%26
            if curr not in skip: tmp -= 1
            
        return chr(curr + 97)
    
    return "".join(chgN(i) for i in s)