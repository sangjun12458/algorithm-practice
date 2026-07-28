def solution(keymap, targets):
    answer = []

    press_numbers = dict()
    for x in range(26):
        press_numbers[chr(ord('a') + x)] = 101
    for key in keymap:
        for idx, alphabet in enumerate(key):
            press_numbers[alphabet] = min(idx, press_numbers[alphabet])

    def typing():
        result = -1
        return result

    for target in targets:
        answer.append(typing(target))

    return answer