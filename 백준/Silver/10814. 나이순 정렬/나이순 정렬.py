from sys import stdin

n = int(stdin.readline())
age_dict = dict()

for _ in range(n):
    a,b = stdin.readline().strip().split()
    a = int(a)
    if a not in age_dict:
        age_dict[a] = []
    age_dict[a].append(b)

for i in sorted(age_dict):
    for j in age_dict[i]:
        print('{} {}'.format(i,j))