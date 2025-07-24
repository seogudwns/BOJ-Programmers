from functools import reduce

def solution(numbers, n):
    return reduce(lambda x,y: x+y if x <= n else x,numbers)