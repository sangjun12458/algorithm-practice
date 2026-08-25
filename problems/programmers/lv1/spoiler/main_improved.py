def solution(message, spoiler_ranges):
    spoiler_ranges.sort()

    merged = []
    for s, e in spoiler_ranges:
        if merged and s <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])

    words = {}
    i = 0

    while i < len(message):
        if message[i] == ' ':
            i += 1
            continue

        start = i

        while i < len(message) and message[i] != ' ':
            i += 1

        word = message[start:i]
        words.setdefault(word, []).append((start, i - 1))

    answer = 0

    for positions in words.values():
        j = 0

        for start, end in positions:
            while j < len(merged) and merged[j][1] < start:
                j += 1

            if j == len(merged) or merged[j][0] > start or merged[j][1] < end:
                break
        else:
            answer += 1

    return answer