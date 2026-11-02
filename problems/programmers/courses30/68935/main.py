def solution(n):
    answer = 0

    s = ''
    while n > 0:
        quotient = n // 3
        remainder = n % 3
        s += str(remainder)
        n = quotient
    s = s[::-1]
    for i in range(len(s)):
        answer += int(s[i]) * (3**i)

    return answer