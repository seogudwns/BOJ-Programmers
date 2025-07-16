def solution(common):
    return 2*common[-1]-common[-2] if len(common) == 2 or common[-3] + common[-1] == 2*common[-2] else common[-1]**2/common[-2]