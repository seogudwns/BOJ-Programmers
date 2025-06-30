def solution(number: str) -> int:
    return sum(int(i) for i in number)%9