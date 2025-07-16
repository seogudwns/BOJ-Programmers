def solution(number):
    return sum(1 for k in range(2,len(number)) for j in range(1,k) for i in range(j) if not number[i]+number[j]+number[k])