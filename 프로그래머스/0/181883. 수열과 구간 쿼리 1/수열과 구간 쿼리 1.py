def solution(arr, queries):
    addi = [0]*(len(arr)+1)
    for i,j in queries:
        addi[i] += 1
        addi[j+1] -= 1
        
    for i in range(1,len(addi)):
        addi[i] += addi[i-1]
    # print(addi)
    
    for i in range(len(arr)):
        arr[i] += addi[i]
        
    return arr