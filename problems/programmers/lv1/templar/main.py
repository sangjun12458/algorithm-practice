def solution(number, limit, power): 
    answer = 0

    for x in range(1, number+1):
        cnt = 0
        y = 1
        while y * y < x:
            if x % y == 0:
                cnt += 2
            y += 1
        if y * y == x:
            cnt += 1
        answer += cnt if cnt <= limit else power

    return answer