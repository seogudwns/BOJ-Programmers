def solution(s):
    leng = len(s)
    
    def dkqcnr(arr,n):
        nonlocal leng
        lst = []
        curr,num = s[:n],0
        for i in range(0,leng,n):
            comp = arr[i:i+n]
            if curr == comp:
                num += 1
            else:
                if num != 1:
                    lst.extend([str(num),curr])
                    num = 1
                else:
                    lst.append(curr)
                curr = comp
                
        if num != 1:       
            lst.extend([str(num),curr])
        else:
            lst.append(curr)
        
        # if leng%n:
        #     lst.append(arr[i:])
        
        return ''.join(lst)
        
    answer = leng
    for i in range(1,leng//2+1):
        res = dkqcnr(s,i)
        # print(res)
        ll = len(res)
        if ll<answer:
            answer = ll
            
    return answer