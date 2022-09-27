from sys import stdin

seq = [0,1,1]
sum_seq = [0,1,2]
num = 1000000007
init_num = 2
for i in range(3,1000001):
    nex = (seq[-1]*(2+init_num))%num
    sum_seq.append((sum_seq[-1]+nex)%num)
    seq.append(nex)
    init_num = (init_num*2)%num

case = int(stdin.readline().strip())

def sec_ord(numb):
    cnt = 0
    while True:
        if numb%2 != 0:
            return cnt
        
        numb = numb//2
        cnt += 1

for _ in range(case):
    
    arr = stdin.readline().strip()
    
    if arr.startswith('4'):
        order,one,i = map(int,arr.split())
        print((one*seq[i])%num)
        continue
    
    order,one,i,j = map(int,arr.split())
    if i>j:
        i,j = j,i
        
    if order == 1:
        print((one*seq[i])%num)
        
    elif order == 2:
        if j <= 2:
            print(sec_ord(one))
        else:
            print(sec_ord(one)+(j-1))
        
    elif order == 3:
        print((one*(sum_seq[j] - sum_seq[i-1]))%num)
