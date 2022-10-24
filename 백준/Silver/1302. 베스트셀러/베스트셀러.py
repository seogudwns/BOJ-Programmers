from sys import stdin

n = int(stdin.readline())
dic = dict()
for _ in range(n):
    book = stdin.readline().strip()
    if book not in dic:
        dic[book] = 0
    dic[book] += 1

print(sorted(dic,key=lambda x: (-dic[x],x))[0])