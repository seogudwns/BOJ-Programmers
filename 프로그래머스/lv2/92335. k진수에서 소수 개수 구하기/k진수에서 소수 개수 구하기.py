def solution(n, k):
    def checkPrime(num):
        for i in range(2,int((num)**(1/2))+1):
            if not num%i:
                return False
        return True
    
    lst = []
    while n:
        n,res = divmod(n,k)
        lst.append(str(res))
    
    nums = ''.join(lst[::-1]).split('0')
    # print(nums)
    result = 0
    for i in nums:
        try:
            num = int(i)
            if num != 1:
                if checkPrime(num):
                    result+=1
        except:
            pass
        
    return result