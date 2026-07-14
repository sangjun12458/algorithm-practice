def solution(wallpaper):
    answer = []
    MAX_NUM = 50

    coords = []
    for idx_r, row in enumerate(wallpaper):
        for idx_c, c in enumerate(row):
            if c == '#':
                coords.append((idx_r, idx_c))

    minr, minc, maxr, maxc = MAX_NUM, MAX_NUM, 0, 0
    for y, x in coords:
        minr = min(minr, y)
        minc = min(minc, x)
        maxr = max(maxr, y)
        maxc = max(maxc, x)

    answer.extend([minr, minc, maxr+1, maxc+1])

    return answer