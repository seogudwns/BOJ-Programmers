def solution(food):
    return (tmp:=''.join([str(i)*(food[i]//2) for i in range(1,len(food))])) + '0' + tmp[::-1]