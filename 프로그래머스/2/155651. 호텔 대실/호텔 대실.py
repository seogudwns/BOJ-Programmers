def solution(book_time):
    def chg(time):
        ans = []
        s,t = time[0].split(":")
        ans.append(int(s)*60+int(t))
        s,t = time[1].split(":")
        ans.append(int(s)*60+int(t)+10)
        return ans
    book_time = sorted([chg(i) for i in book_time])
    rooms = [tuple(book_time[0])]
    for i in range(1,len(book_time)):
        # print(rooms,book_time[i])
        s,e = book_time[i]
        for j in range(len(rooms)):
            cs,ce = rooms[j]
            if ce <= s:
                rooms[j] = (s,e)
                break
        else:
            rooms.append((s,e))
        
    return len(rooms)