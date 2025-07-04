def solution(data, ext, val_ext, sort_by):
    chk = {
        "code":0, 
        "date":1,
        "maximum":2,
        "remain":3
    }
    
    return sorted([i for i in data if i[chk[ext]]<val_ext],key=lambda x: x[chk[sort_by]])