from sys import stdin

def check(num):
    leng = len(num)
    if leng == 1:
        return print(1)
    
    for i in range(1,leng//2+1):
        if leng%i == 0:
            if num.count(num[:i]) == leng//i:
                return print(leng//i)
    
    return print(1)

while True:
    num = stdin.readline().strip()
    if num == '.':
        break
    
    check(num)
