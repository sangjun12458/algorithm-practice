def solution(mats, park):
    answer = 0

    row_len = len(park)
    col_len = len(park[0])
    mats.sort()

    def check(r, c, l):
        for i in range(r, r+l):
            for j in range(c, c+l):
                if not (0 <= i < row_len and 0 <= j < col_len):
                    return False
                if park[i][j] != "-1":
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