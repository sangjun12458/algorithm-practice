def solution(message, spoiler_ranges):
    answer = 0
    idx_to_word_list = [0] * len(message)
    word_dict = dict()
    word_num = 0
    for idx, c in enumerate(message):
        idx_to_word_list[idx] = word_num
        if c == ' ':
            word_num += 1
    
    for start, end in spoiler_ranges:
        print(message[start:end+1])

    return answer

message, spoiler_ranges = "my phone number is 01012345678 and may i have your phone number", [[5, 5], [25, 28], [34, 40], [53, 59]]
k = message.index()
print(k)
solution(message, spoiler_ranges)