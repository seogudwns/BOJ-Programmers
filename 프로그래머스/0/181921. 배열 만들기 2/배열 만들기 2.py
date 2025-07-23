def solution(l, r):
    return x if len(x:=[i for i in range(l,r+1) if not i%5 and str(i).count("0")+str(i).count("5") == len(str(i))]) else [-1]