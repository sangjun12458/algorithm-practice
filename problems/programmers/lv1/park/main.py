def solution(mats, park):
    answer = 0

    row_len = len(park)
    col_len = len(park[0])
    max_len = max(mats)

    for r in range(row_len):
        for c in range(col_len):
            check_square = [True] * max_len
            if park[r][c] != '-1':
                continue
            for dr in range(max_len):
                nr = r + dr
                if nr >= row_len:
                    continue
                for dc in range(max_len):
                    nc = c + dc
                    if nc >= col_len:
                        continue
                    if park[nr][nc] != '-1':
                        check_square[max(nr, nc)] = False
            for idx, x in enumerate(check_square):
                if x:
                    answer = max(answer, idx)

    return answer