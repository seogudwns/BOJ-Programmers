def solution(players, callings):
    idx = {players[i]:i for i in range(len(players))}
    for i in callings:
        index = idx[i]
        idx[players[index-1]] += 1
        idx[i] -= 1
        players[index],players[index-1] = players[index-1],players[index]
        
    return players