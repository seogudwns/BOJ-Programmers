def solution(numLog):
    return ''.join({1:"w",-1:"s",10:"d",-10:"a"}[numLog[i+1]-numLog[i]] for i in range(len(numLog)-1))