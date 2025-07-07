def solution(park, routes):
    curr = [-1,-1]
    n,m = len(park),len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                curr = [i,j]
                break
    
    # N,S : 0 <= curr[0] < n, E,W : 0 <= curr[1] < m  
    
    print(n,m,curr)
    for i in routes:
        direction,leng = i.split(" ")
        leng = int(leng)
        if direction == "E":
            if 0 <= curr[1]+leng < m and all(park[curr[0]][i] != "X" for i in range(curr[1]+1,curr[1]+1+leng)):
                curr[1] += leng
        elif direction == "W":
            if 0 <= curr[1]-leng < m and all(park[curr[0]][i] != "X" for i in range(curr[1]-1,curr[1]-1-leng,-1)):
                curr[1] -= leng
        elif direction == "N":
            if 0 <= curr[0]-leng < n and all(park[i][curr[1]] != "X" for i in range(curr[0]-1,curr[0]-1-leng,-1)):
                curr[0] -= leng
        else: # direction == "S"
            if 0 <= curr[0]+leng < n and all(park[i][curr[1]] != "X" for i in range(curr[0]+1,curr[0]+1+leng)):
                curr[0] += leng
        print(curr)
        
    return curr