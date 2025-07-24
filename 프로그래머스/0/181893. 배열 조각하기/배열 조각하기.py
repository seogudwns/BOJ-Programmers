def solution(arr, query):
    l,r = 0,len(arr)
    for i in range(len(query)):
        if i%2: # odd
            l += query[i]
        else: # even
            r = l+query[i]
        
    return arr[l:r+1]