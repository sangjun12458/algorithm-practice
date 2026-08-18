def solution(message, spoiler_ranges):
    answer = 0

    for start, end in spoiler_ranges:
        print(message[start:end+1])

    return answer

message, spoiler_ranges = "my phone number is 01012345678 and may i have your phone number", [[5, 5], [25, 28], [34, 40], [53, 59]]
solution(message, spoiler_ranges)