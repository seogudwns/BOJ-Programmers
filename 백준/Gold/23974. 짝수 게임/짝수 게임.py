N,K = map(int,input().split())
if N == 0 and K%6 == 1:
    print("HS")
elif N == 1 and K%6 in [0,5]:
    print("HS")
else:
    print("YG")
