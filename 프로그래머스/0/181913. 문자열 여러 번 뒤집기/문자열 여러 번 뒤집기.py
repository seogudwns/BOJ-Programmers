def solution(my_string, queries):
    my_string = [i for i in my_string]
    for s,e in queries:
        my_string[s:e+1] = my_string[e::-1] if s == 0 else my_string[e:s-1:-1]
    return ''.join(my_string)