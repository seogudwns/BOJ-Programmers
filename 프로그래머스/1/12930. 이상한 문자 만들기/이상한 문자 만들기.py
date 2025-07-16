def solution(s):
    return ''.join(''.join(i[j].lower() if j%2 else i[j].upper() for j in range(len(i)))+' ' for i in s.split(" "))[:-1]