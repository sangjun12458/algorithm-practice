def solution(N, stages):
    answer = []

    import heapq
    cnts = [0] * (N+2)
    for s in stages:
        cnts[s] += 1
    hq = []
    x = cnts[-1]
    for i in range(N, 0, -1):
        x += cnts[i]
        if x:
            heapq.heappush(hq, (-cnts[i] / x, i))
        else:
            heapq.heappush(hq, (0, i))
    while hq:
        _, s = heapq.heappop(hq)
        answer.append(s)

    return answer