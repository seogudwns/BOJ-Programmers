def solution(board, moves):
    n,m = len(board),len(board[0])
    dep = [m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if board[j][i]:
                dep[i] = j
                break
    
    basket = []
    ans = 0
    for i in moves:
        i -= 1
        if dep[i] == n: continue
        if basket and board[dep[i]][i] == basket[-1]:
            basket.pop()
            ans += 2
        else:
            basket.append(board[dep[i]][i])
        dep[i] += 1
        
    return ans