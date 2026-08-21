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
        pass

    return answer