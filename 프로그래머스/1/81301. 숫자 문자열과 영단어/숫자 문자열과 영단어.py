def solution(s):
    answer = ''
    chk = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    idx = 0
    while idx<len(s):
        if s[idx].isdigit():
            answer += s[idx]
            idx += 1
        else:
            for i in chk:
                if s[idx:idx+len(i)] == i:
                    answer += chk[i]
                    idx += len(i)
                    break
                    
    return int(answer)