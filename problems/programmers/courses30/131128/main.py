def solution(X, Y):
    answer = ''

    a, b = X, Y
    cnts = [0] * 10
    while a > 0:
        cnts[a % 10] += 1
        a //= 10
    while b > 0:
        cnts[b % 10] += 1
        b //= 10
    for x in range(9, -1, -1):
        for t in range(cnts[x]):
            pass

    return answer