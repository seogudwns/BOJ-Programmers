def solution(price, money, count):
    return x if (x:=price*(count*(count+1))//2 - money)>0 else 0