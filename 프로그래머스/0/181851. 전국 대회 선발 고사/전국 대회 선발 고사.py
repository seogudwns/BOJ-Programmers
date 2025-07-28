def solution(rank, attendance):
    return (tmp:=sorted([(rank[i],j) for j,i in enumerate(range(len(rank))) if attendance[i]]))[0][1]*10000 + tmp[1][1]*100 + tmp[2][1]