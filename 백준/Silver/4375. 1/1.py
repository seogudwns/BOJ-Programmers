from sys import stdin

while True:
    try:
        n = int(stdin.readline())
        x = 0
        curr = 0
        while True:
            x += 10**curr
            if x%n == 0:
                print(curr+1)
                break
            curr += 1
    except:
        break