def solution(wallpaper):
    answer = []

    coords = []
    for idx_r, row in enumerate(wallpaper):
        for idx_c, c in enumerate(row):
            if c == '#':
                coords.append((idx_r, idx_c))

    minr, minc, maxr, maxc = 0, 0, 0, 0
    
    return answer