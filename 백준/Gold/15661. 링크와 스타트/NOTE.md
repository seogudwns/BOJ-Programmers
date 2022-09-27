## compare codes.

```python
import time

from sys import stdin
n = int(stdin.readline())

lst = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]

stt = time.time()

result = float('inf')

for i in range(1,(1<<n)):
    t = {j for j in range(n) if (1<<j) & i}
    team = 0
    for j in range(n):
        for k in range(n):
            tmp = {j,k} & t
            if tmp == {j,k}:
                team += lst[j][k]
            elif tmp == set():
                team -= lst[j][k]
                
    result = min(result,abs(team))

print(result)

print('type1 :',time.time()-stt)

stt = time.time()

result = float('inf')

for i in range(1,(1<<n)):
    t = {j for j in range(n) if (1<<j) & i}
    team = 0
    for j in range(n):
        for k in range(n):
            if j in t and k in t:
                team += lst[j][k]
            elif j not in t and k not in t:
                team -= lst[j][k]
                
    result = min(result,abs(team))

print(result)

print('type2 :',time.time()-stt)

stt = time.time()

result = float('inf')

for i in range(1,(1<<n)):
    t = {j for j in range(n) if (1<<j) & i}
    team = 0
    for j in range(n):
        for k in range(n):
            tmp = {j,k} & t
            if not tmp:
                team -= lst[j][k]
            elif tmp == {j,k}:
                team += lst[j][k]
                
    result = min(result,abs(team))

print(result)

print('type3 :',time.time()-stt)

stt = time.time()

result = float('inf')

for i in range(1,(1<<n)):
    t1 = {j for j in range(n) if (1<<j) & i}
    t2 = {i for i in range(n) if i not in t1}
    team = 0
    for j in t1:
        for k in t1:
            team += lst[j][k]
    
    for j in t2:
        for k in t2:
            team -= lst[j][k]
    
    result = min(result,abs(team))

print(result)

print('type4 :',time.time()-stt)  # clear.
```

### input 

```
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
```


### result
```
2
type1 : 0.0039997100830078125
2
type2 : 0.003002643585205078
2
type3 : 0.006997108459472656
2
type4 : 0.001998424530029297
```
