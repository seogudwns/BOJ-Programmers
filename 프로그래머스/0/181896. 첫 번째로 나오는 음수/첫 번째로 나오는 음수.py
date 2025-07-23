def solution(num_list):
    return x[0] if (x:=[i for i in range(len(num_list)) if num_list[i]<0]) else -1