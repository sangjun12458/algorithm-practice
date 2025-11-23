# 별 찍기 - 11
import math
tri = ["  *  ", " * * ", "*****"]

def print_tri(cnt, pos):
    for t in tri:
        s = ""
        for p in pos:
            s += " "*(3*(p-1) - len(s)) + t
        print(s)

n = int(input())
k = int(math.log2(n // 3))
pattern = []
pattern.append((1, [2**k]))
for _ in range(k):
    next_pattern = []
    for cnt, pos in pattern:
        prev_cnt, prev_pos = next_pattern[-1] if next_pattern else pattern[-1]
        next_cnt, next_pos = cnt * 2, []
        if next_cnt == prev_cnt:
            for idx in range(len(prev_pos)):
                next_pos.append(prev_pos[idx] + idx % 2 * 2 - 1)
        elif next_cnt > prev_cnt:
            for p in prev_pos:
                next_pos.append(p - 1)
                next_pos.append(p + 1)
        else:
            for p in pos:
                next_pos.append()
                next_pos.append()
        next_pattern.append((next_cnt, next_pos))
    pattern.extend(next_pattern)

print(pattern)

for cnt, pos in pattern:
    print_tri(cnt, pos)
