def solution(bandage, health, attacks):
    attacks = attacks[::-1]
    a,b,c = bandage
    orgH,bT = health,0
    while attacks:
        T,dam = attacks.pop()
        
        health = min(orgH,health + (T-bT)*b + (T-bT)//a*c)
        health -= dam
        if health < 1: return -1
    
        bT = T+1
        
    return health