def solution(n, lost, reserve):
    answer = 0

    cnts = [1] * (n+2)
    for i in lost:
        cnts[i] -= 1
    for i in reserve:
        cnts[i] += 1

    for i in range(1, n+1):
        if cnts[i] == 2:
            if cnts[i-1] == 0:
                cnts[i-1] = 1
                cnts[i] = 1
            elif cnts[i+1] == 0:
                cnts[i+1] = 1
                cnts[i] = 1
    answer = n - cnts.count(0)

    return answer