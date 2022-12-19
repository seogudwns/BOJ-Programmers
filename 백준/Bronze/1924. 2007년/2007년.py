month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

x,y = map(int,input().split())

for i in range(x):
    y += month[i]

print(day[y%7])