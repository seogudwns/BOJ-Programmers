def solution(arr):
    def chg(ar):
        return [i//2 if i>=50 and not i%2 else i*2+1 if i<50 and i%2 else i for i in ar]

    nex,chk = chg(arr),0
    while nex != arr:
        # print(nex,arr,arr[chk:chk+2])
        if arr[chk] == arr[chk+1]:
            return chk+1
        arr = nex
        nex = chg(arr)
        chk += 1