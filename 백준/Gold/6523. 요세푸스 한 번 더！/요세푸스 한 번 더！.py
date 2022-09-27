def next(x):
    return (a*((x**2)%N)+b)%N

def usps_add(N):
    first = set()
    second = set()

    graped = b

    while True:
        if graped in second: #3번째 걸렸으니 break
            break
        elif graped in first:  
            second.add(graped) #두 번째로 걸린 사람이 넘어감.
        else:
            first.add(graped)  #처음 걸린 케이스.
        graped = next(graped) #next가 잡힘.

    return N - len(second)

while True:
    a = input()
    if a == '0':
        break
    N,a,b = map(int,a.strip().split())
    if a > N//2:
        a = a - N  #계산량을 조금이라도 줄여봅시다.
    if b > N//2:
        b = b - N  #계산량을 조금이라도 줄여봅시다.

    print(usps_add(N))