def solution(wallet, bill):
    wallet,bill = [max(wallet),min(wallet)],[max(bill),min(bill)]
    answer = 0
    while bill[0]>wallet[0] or bill[1]>wallet[1]:
        bill[0]//=2
        bill = [max(bill),min(bill)]
        answer+=1
    return answer