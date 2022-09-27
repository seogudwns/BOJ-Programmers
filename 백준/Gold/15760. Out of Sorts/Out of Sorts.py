n = int(input())
lst = [int(input()) for _ in range(n)]

leng = len(lst)
last = sorted(lst)
result = 0

num_idx_dict = dict()
num_idx_dict_last = dict()

for i in range(leng):
    num_idx_dict[lst[i]] = i
    num_idx_dict_last[last[i]] = i

for i in num_idx_dict:
    result = max(result,num_idx_dict[i] - num_idx_dict_last[i])    

print(result+1)