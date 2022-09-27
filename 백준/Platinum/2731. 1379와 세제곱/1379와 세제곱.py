from sys import stdin

def get_num(num_lst,last_num,idx):
    if str(int(''.join(num_lst[::-1]))**3)[::-1].startswith(last_num):
        return True,num_lst
    
    for i in range(10):
        result_num = str(int(str(i) + ''.join(num_lst[::-1]))**3)[::-1]
        if result_num.startswith(last_num[:idx]):
            num_lst.append(str(i))
            return False,num_lst

case = int(stdin.readline().strip())

for _ in range(case):
    last_num = stdin.readline().strip()[::-1]
    first = int(last_num[0])
    num_lst = [str(10-first) if 2<first<8 else str(first)]
    
    idx = 2
    while True:
        
        check,num_lst = get_num(num_lst,last_num,idx)
        if check:
            print(''.join(num_lst[::-1]))
            break
            
        idx += 1
    