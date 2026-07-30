def solution(keymap, targets):
    answer = []
    keymap = ["ABACD", "BCEFD"]
    targets = ["ABCD", "AABB"]
    press_numbers = dict()
    for x in range(26):
        press_numbers[chr(ord('A') + x)] = 101
    for key in keymap:
        for idx, alphabet in enumerate(key):
            press_numbers[alphabet] = min(idx, press_numbers[alphabet])
    print(press_numbers)
    for target in targets:
        cnt = 0
        for x in target:
            t = press_numbers[x]
            if t == 101:
                cnt = -1
                break
            cnt += press_numbers[x]
        answer.append(cnt)

    return answer

print(solution(None, None))