def solution(s, n):
    return ''.join(' ' if i == ' ' else chr((ordi-65+n)%26+65) if 64<(ordi:=ord(i))<91 else chr((ordi-97+n)%26+97) for i in s)