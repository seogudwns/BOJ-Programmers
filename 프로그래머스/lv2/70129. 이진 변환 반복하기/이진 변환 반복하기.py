def solution(s):
    zeros = 0
    change = 0
    while s != '1':
        leng = 0
        for i in s:
            if i == '0':
                zeros += 1
            else:
                leng += 1
        # return [zeros,leng]
        lst = []
        while leng:
            lst.append('1' if leng%2 else '0')
            leng //= 2
        s = ''.join(lst[::-1])
        change += 1
        
    answer = [change,zeros]
    return answer