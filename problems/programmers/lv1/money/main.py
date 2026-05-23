def solution(wallet, bill):
    answer = 0

    cnt = 0
    while True:
        if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
            answer = cnt
            break
        elif bill[0] <= wallet[1] and bill[1] <= wallet[0]:
            answer = cnt
            break
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        cnt += 1

    return answer