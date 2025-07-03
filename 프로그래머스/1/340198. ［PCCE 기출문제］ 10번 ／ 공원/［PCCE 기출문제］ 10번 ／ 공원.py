def solution(mats, park):
    n,m = len(park),len(park[0])
    for leng in sorted(mats,reverse = True):
        for i in range(n-leng+1):
            for j in range(m-leng+1):
                if park[i][j] == "-1" and all(park[i][k] == "-1" for k in range(j,j+leng)) and all(park[k][j] == "-1" for k in range(i,i+leng)) and all(all(park[w][k] == "-1" for k in range(j,j+leng)) for w in range(i,i+leng)):
                    return leng
    return -1