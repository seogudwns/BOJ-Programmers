n = int(input())%1500000 # 1500000에서 1 1이 반복됨.
# print(n)
tmp1 = 1
tmp2 = 0
while n != 1:
    
    tmp1,tmp2 = (tmp1+tmp2)%1000000,tmp1
    
    n -= 1

print(tmp1)