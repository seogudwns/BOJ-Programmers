import functools
def solution(num_list):
    return 1 if sum(i for i in num_list)**2 > functools.reduce(lambda x,y: x*y,num_list) else 0