def solution(myString, pat):
    return [myString[:i+len(pat)] for i in range(len(myString)-len(pat),-1,-1) if myString[i:i+len(pat)] == pat][0]