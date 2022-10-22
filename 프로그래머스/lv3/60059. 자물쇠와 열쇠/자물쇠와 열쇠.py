# def solution(key, lock):
#     # # example check code.
#     # print('key :')
#     # for i in key:
#     #     print(i)
#     # print('lock :')
#     # for i in lock:
#     #     print(i)
#     leng = len(key)
#     # 자물쇠 구멍이 있는 패턴을 땀. 
#     # 붙어있는 곳을 생각하면서 열쇠에 대입을 했을 때 이게 모두 잘 대입이 되면 True. 모든 케이스에 대해서 잘 안되면 False.
#     maxrow,maxcol = 0,0
    
#     for i in range(leng):
#         for j in range(leng):
#             if lock[i][j] == 0:
#                 maxrow, maxcol = max(maxrow,i), max(maxcol,j)

def spin_right(arr):
    return list(map(list, zip(*arr[::-1])))

def check(arr, N):
    answer = True
    for ix in range(N):
        for iy in range(N):
            if arr[ix + N][iy + N] != 1:
                return False
    return answer

def solution(key, lock):
    M = len(key)
    N = len(lock)
    # 3배 더 큰 자물쇠 생성
    new_lock = [[1] * N * 3 for _ in range(N * 3)]
    # 기존 자물쇠를 새로운 자물쇠 가운데에 위치
    for ix in range(N):
        for iy in range(N):
            new_lock[ix + N][iy + N] = lock[ix][iy]
    # 시계방향으로 4번 돌림
    for _ in range(4):
        key = spin_right(key)
        for lock_ix in range(N * 2):
            for lock_iy in range(N * 2):
                # key를 new_lock에 꽂음
                for key_ix in range(M):
                    for key_iy in range(M):
                        new_lock[lock_ix + key_ix][lock_iy + key_iy] += key[key_ix][key_iy]
                # new_lock의 중앙만 확인
                if check(new_lock, N):
                    return True
                # key를 new_lock에서 뺌
                for key_ix in range(M):
                    for key_iy in range(M):
                        new_lock[lock_ix + key_ix][lock_iy + key_iy] -= key[key_ix][key_iy]
    return False
# 귀찮..