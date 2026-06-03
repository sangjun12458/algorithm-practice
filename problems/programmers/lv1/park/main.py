def solution(mats, park):
    answer = 0

    row_len = len(park)
    col_len = len(park[0])
    max_len = max(mats)

    def check(r, c, l):
        for i in range(r, r+l):
            for j in range(c, c+l):
                if park[i][j] != -1:
                    return False
        return True

    for r in range(row_len):
        for c in range(col_len):
            for l in mats:
                if check(r, c, l):
                    answer = max(answer, l)
                else:
                    break

    return answer