from sys import stdin
# from itertools import permutations

# n = int(stdin.readline())
# lst = map(int,stdin.readline().strip().split())

# def calc(lst):
#     global n
#     res = 0
#     for i in range(n-1):
#         res += abs(lst[i]-lst[i+1])
#     return res

# res = 0
# for i in permutations(lst):
#     # i = list(i)
#     curr = calc(i)
#     if res<curr:
#         # print(i,curr)
#         res = curr

# print(res)

# ! 기본시간만 사용된 코드.. (타인의 자료 참고.)
N = int(stdin.readline())
arr = list(map(int,stdin.readline().strip().split()))

minuslist =[]
for i in range(N):
    for j in range(i+1,N):
        minuslist.append([abs(arr[i]-arr[j]),i,j])
used=[0]*N
minuslist = sorted(minuslist)
t=0
ans=0
while t<N-1:
   temp=minuslist.pop()
   if used[temp[1]]<2 and used[temp[2]]<2 :
       if t==N-2 and used[temp[1]]==1 and used[temp[2]]==1:
           continue
       used[temp[1]] += 1
       used[temp[2]] += 1
       ans += temp[0]
       t += 1
print(ans)