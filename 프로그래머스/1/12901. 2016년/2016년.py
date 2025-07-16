def solution(a, b):
    mon_days=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    ul="THU,FRI,SAT,SUN,MON,TUE,WED".split(",")
    return ul[(sum(mon_days[:a])+b)%7]