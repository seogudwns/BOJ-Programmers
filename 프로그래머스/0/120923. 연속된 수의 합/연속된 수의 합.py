def solution(num, total):
    return [i for i in range(int((total-((num*(num-1))/2))/num),int((total-((num*(num-1))/2))/num)+num)]