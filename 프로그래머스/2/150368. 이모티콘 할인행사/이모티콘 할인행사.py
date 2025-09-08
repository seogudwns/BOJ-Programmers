from itertools import product

def solution(users, emoticons):
    emoticons = [i//100 for i in emoticons]
    
    answer, discount_rate, n = [0,0], [10,20,30,40], len(emoticons)
    for combo in product(discount_rate, repeat=n):
        curr,combo = [0,0], list(combo)
        for perc,pric in users:
            tmp = 0
            for i in range(n):
                if combo[i] >= perc:
                    tmp += (emoticons[i]*(100-combo[i]))
                    
            if pric > tmp: 
                curr[1] += tmp
            else:
                curr[0] += 1
        
        if curr[0] > answer[0] or (curr[0] == answer[0] and curr[1] > answer[1]):
            # print(answer,combo,curr)
            answer = curr
            
    return answer