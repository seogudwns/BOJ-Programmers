def solution(board, k):    
    return sum(sum(board[j][i] for i in range(len(board[0])) if i+j<=k) for j in range(len(board)))