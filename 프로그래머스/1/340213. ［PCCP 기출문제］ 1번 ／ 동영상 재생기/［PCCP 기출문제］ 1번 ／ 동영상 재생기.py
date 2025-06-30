def solution(video_len, pos, op_start, op_end, commands):
    def chg_rt(str_t: str) -> int: return int(str_t) if ":" not in str_t else int(str_t.split(":")[0]) * 60 + int(str_t.split(":")[1]) 
    def chg_strt(rt: int) -> str: return str(rt//60).rjust(2,'0') + ":" + str(rt%60).rjust(2,'0')
    def autrt(curr: int,st: int,end: int) -> int: return end if st<=curr<=end else curr
    
    vrt,prt,strt,endrt = chg_rt(video_len),chg_rt(pos),chg_rt(op_start),chg_rt(op_end)
    curr = autrt(prt,strt,endrt)
    
    for i in commands: curr = autrt(min(vrt,curr+10),strt,endrt) if i.startswith('n') else autrt(max(0,curr-10),strt,endrt)
            
    return chg_strt(curr)