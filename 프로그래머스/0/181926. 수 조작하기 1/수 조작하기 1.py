def solution(n, control):
    return n+sum({"w":1,"s":-1,"d":10,"a":-10}[i] for i in control)