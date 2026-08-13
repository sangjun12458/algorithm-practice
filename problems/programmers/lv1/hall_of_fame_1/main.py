def solution(k, score):
    answer = []

    import heapq
    fame = []
    for s in score:
        if len(fame) < k:
            heapq.heappush(fame, s)
        else:
            if s > fame[0]:
                heapq.heappop(fame)
                heapq.heappush(fame, s)
        answer.append(fame[0])

    return answer