def solution(message : str, spoiler_ranges : list):
    answer = 0

    words = message.split(' ')
    idx_to_word_list = [0] * len(message)
    word_num = 0
    for idx, c in enumerate(message):
        if c == ' ':
            idx_to_word_list[idx] = -1
            word_num += 1
        else:
            idx_to_word_list[idx] = word_num

    processed = [False] * len(words)
    for start, end in spoiler_ranges:
        for i in range(start, end + 1):
            word_num = idx_to_word_list[i]
            if word_num == -1:
                continue
            processed[word_num] = True

    word_dict = dict()
    for i, is_processed in enumerate(processed):
        if not is_processed: continue
        word = words[i]
        if word_dict.get(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    for key, value in word_dict.items():
        cnt = words.count(key)
        if cnt == value:
            answer += 1

    return answer