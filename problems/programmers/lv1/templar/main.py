def solution(number, limit, power):
    answer = 0

    for x in range(number):
        cnt = 0
        y = 1
        while y * y <= x:
            if x % y == 0:
                cnt += 2
            y += 1
        print(x, cnt)
        answer += cnt if cnt <= limit else power

    return answer
