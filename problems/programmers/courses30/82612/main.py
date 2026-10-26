def solution(price, money, count):
    answer = -1

    for i in range(1, count+1):
        money -= i * price
    answer = max(0, -money)

    return answer