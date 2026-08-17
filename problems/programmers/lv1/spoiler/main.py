def solution(message, spoiler_ranges):
    answer = 0

    for start, end in spoiler_ranges:
        print(message[start:end+1])

    return answer

message, spoiler_ranges = "here is muzi here is a secret message", [[0, 3], [23, 28]]
solution(message, spoiler_ranges)