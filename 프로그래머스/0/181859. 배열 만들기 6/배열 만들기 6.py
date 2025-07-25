def solution(arr):
    i,n,stk = 0,len(arr),[]
    while i<n:
        if not stk:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                stk.pop()
            else:
                stk.append(arr[i])
        i += 1
    
    return stk if stk else [-1]