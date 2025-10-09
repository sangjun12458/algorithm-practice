# 최적안: 2D prefix-sum + iterative stack (파이썬)
import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    paper = [list(map(int, input().split())) for _ in range(n)]

    # prefix sum: ps[i][j] = sum of paper[0..i-1][0..j-1]
    ps = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        row = paper[i]
        row_ps = ps[i+1]
        prev = ps[i]
        s = 0
        for j in range(n):
            s += row[j]
            row_ps[j+1] = prev[j+1] + s

    def region_sum(x, y, size):
        x2 = x + size
        y2 = y + size
        return ps[x2][y2] - ps[x][y2] - ps[x2][y] + ps[x][y]
    
    white = blue = 0
    stack = [(0, 0, n)]
    while stack:
        x, y, sz = stack.pop()
        s = region_sum(x, y, sz)
        if s == 0:
            white += 1
        elif s == sz * sz:
            blue += 1
        else:
            half = sz // 2
            stack.append((x, y, half))
            stack.append((x, y + half, half))
            stack.append((x + half, y, half))
            stack.append((x + half, y + half, half))

    print(white)
    print(blue)

if __name__ == "__main__":
    solve()