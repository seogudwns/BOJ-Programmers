def solution(name, yearning, photo):
    return [sum({name[k]:yearning[k] for k in range(len(name))}[j] if j in name else 0 for j in i) for i in photo]