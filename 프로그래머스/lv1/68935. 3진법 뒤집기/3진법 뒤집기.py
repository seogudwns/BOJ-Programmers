def solution(n):
    # print(int('0021',3))
    lst = []
    while n:
        lst.append(str(n%3))
        n//=3
    
    answer = int(''.join(lst),3)
    return answer