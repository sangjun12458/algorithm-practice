def solution(mats, park):
    R = len(park)
    C = len(park[0])

    grid = [
        [0 if x == '-1' else 1 for x in row]
        for row in park
    ]

    ps = [[0]*(C+1) for _ in range(R+1)]

    for r in range(R):
        row_sum = 0
        for c in range(C):
            row_sum += grid[r][c]
            ps[r+1][c+1] = ps[r][c+1]

    return -1