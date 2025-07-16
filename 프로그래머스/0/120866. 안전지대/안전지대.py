def solution(board):
    n,rot = len(board),[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for a,b in rot:
                    warn = (i+a,j+b)
                    if 0<= min(warn) and max(warn)<n and board[warn[0]][warn[1]] != 1:
                        board[warn[0]][warn[1]] = 2

    # [print(i) for i in board]
    return sum(1 if i == 0 else 0 for i in sum(board,[]))