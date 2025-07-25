def solution(num_list):
    def chk(n): return 0 if n == 1 else chk((n-1)//2)+1 if n%2 else chk(n//2)+1
    return sum(chk(i) for i in num_list)