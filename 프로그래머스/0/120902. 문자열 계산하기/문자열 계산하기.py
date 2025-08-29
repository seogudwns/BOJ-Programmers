def solution(my_string):
    val,unit,tmp = [],1,''
    for i in my_string:
        if i == " ": continue
        elif i == "+" or i == "-":
            if int(tmp) > 0:
                val.append(unit*int(tmp))
                tmp = ''
            unit = 1 if i == "+" else -1
        else:
            tmp += i
            
    return sum(val)+unit*int(tmp)