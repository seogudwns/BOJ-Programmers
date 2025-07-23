def solution(my_string):
    # print(ord('A'),ord('Z'),ord('a'),ord('z'))
    return [my_string.count(chr(i)) for i in range(65,123) if not 90<i<97]