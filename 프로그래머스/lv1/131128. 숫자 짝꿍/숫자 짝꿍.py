from collections import Counter

def solution(X, Y):
    X_cntor = Counter(str(X))
    res = []
    for i in str(Y):
        if i in X_cntor and X_cntor[i] != 0:
            res.append(i)
            X_cntor[i] -= 1
    
    if not res:
        return '-1'
    elif len(res) == res.count('0'):
        return '0'
    return ''.join(sorted(res,reverse = True))