def solution(numbers):
    return sorted(set(numbers[i]+numbers[j] for i in range(1,len(numbers)) for j in range(i)))