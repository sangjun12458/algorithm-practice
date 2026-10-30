def solution(left, right):
    answer = 0

    cnts = [0] * (right + 1)
    for i in range(1, right + 1):
        for j in range(left, right+1):
            if j % i == 0:
                cnts[j] += 1

    for i in range(left, right + 1):
        answer += i if cnts[i] % 2 == 0 else -i

    return answer