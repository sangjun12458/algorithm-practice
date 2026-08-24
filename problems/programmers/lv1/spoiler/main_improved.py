def solution(message, spoiler_ranges):
    answer = 0

    words = message.split()
    positions = []
    pos = 0
    for word in words:
        start = message.find(word, pos)
        end = start + len(word) - 1
        positions.append((start, end, word))
        pos = end + 1

    # 스포일러 구간 병합
    spoiler_ranges.sort()
    merged = []
    for start, end in spoiler_ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    # 각 단어가 스포일러인지 판단
    spoiler_words = set()
    j = 0
    for start, end, word in positions:
        while j < len(merged) and merged[j][1] < start:
            j += 1

        if j < len(merged) and merged[j][0] <= start and end <= merged[j][1]:
            spoiler_words.add(word)

    # 전체 등장 횟수와 스포일러 등장 횟수
    total = {}
    spoiler = {}

    for start, end, word in positions:
        total[word] = total.get(word, 0) + 1

        if word in spoiler_words:
            spoiler[word] = spoiler.get(word, 0) + 1

    return answer