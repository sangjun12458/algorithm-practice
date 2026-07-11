def solution(wallpaper):
    answer = []

    coords = []
    for idx_r, row in enumerate(wallpaper):
        for idx_c, c in enumerate(row):
            if c == '#':
                coords.append((idx_r, idx_c))

    return answer