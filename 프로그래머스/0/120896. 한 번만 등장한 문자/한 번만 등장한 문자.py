from collections import Counter

def solution(s):
    s = Counter(s)
    return ''.join(sorted([i for i in s if s[i] == 1]))