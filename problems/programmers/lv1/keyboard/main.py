def solution(keymap, targets):
    answer = []

    press_numbers = dict()
    for x in range(26):
        press_numbers[chr(ord('a') + x)] = 101
    for key in keymap:
        for idx, alphabet in enumerate(key):
            press_numbers[alphabet] = min(idx, press_numbers[alphabet])

    for target in targets:
        cnt = 0
        for x in target:
            cnt += press_numbers[x]
        answer.append(cnt)

    return answer