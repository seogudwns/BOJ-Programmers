def solution(myString, pat):
    return 1 if ''.join('A' if i =='B' else 'B' for i in pat) in myString else 0