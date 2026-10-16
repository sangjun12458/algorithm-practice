def solution(X, Y):
    answer = ''

    a, b = int(X), int(Y)
    ca = [0] * 10
    cb = [0] * 10
    while a > 0:
        ca[a % 10] += 1
        a //= 10
    while b > 0:
        cb[b % 10] += 1
        b //= 10
    for x in range(9, -1, -1):
        t = min(ca[x], cb[x])
        for i in range(t):
            answer += str(i)

    while len(answer) >= 2 and answer[0] == '0':
        answer = answer[1:]

    return answer