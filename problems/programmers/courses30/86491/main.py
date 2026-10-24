def solution(sizes):
    answer = 0

    max_v, rem_v = 0, 0
    for (a, b) in sizes:
        max_v = max(max_v, max(a, b))
        rem_v = max(rem_v, min(a, b))

    answer = max_v * rem_v
    return answer