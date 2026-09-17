def solution(new_id: str):
    # 1. 소문자 변환
    new_id = new_id.lower()

    # 2. 허용 문자만 남기고 연속된 '.' 제거
    result = []
    prev_dot = False

    for c in new_id:
        if c == '.':
            if prev_dot:
                continue
            prev_dot = True
            result.append(c)

        elif 'a' <= c <= 'z' or '0' <= c <= '9' or c in '-_':
            prev_dot = False
            result.append(c)

    new_id = ''.join(result)

    # 3. 양끝 '.' 제거
    new_id = new_id.strip('.')

    # 4. 빈 문자열이면 'a'
    if not new_id:
        new_id = 'a'

    # 5. 15자까지 자르기
    new_id = new_id[:15].rstrip('.')

    # 6. 길이가 3이 될 때까지 마지막 문자 반복
    new_id += new_id[-1] * (3 - len(new_id))

    return new_id