def solution(s, skip, index):
    answer = ''

    skip_number = [ord(x) - ord('a') for x in skip]
    origin = [chr(ord('a') + i) for i in range(26)]
    print(origin)
    shifted = [0] * 26

    for i in range(26):
        pass
        # 각 알파벳 별 계산

    for x in s:
        answer += shifted[ord(x) - ord('a')]

    return answer