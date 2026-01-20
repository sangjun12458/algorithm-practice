# 7453. 합이 0인 네 정수
import sys
input = sys.stdin.readline
from collections import Counter

n = int(input()) # 1 <= n <= 4000
arr = [[] for _ in range(4)]
for _ in range(n):
    row = tuple(map(int, input().split()))
    for i in range(4):
        arr[i].append(row[i])

cntr = []
for i in range(4):
    cntr.append(Counter(arr[i]))

keys = []
for i in range(4):
    keys.append(sorted(cntr[i]))
# [[-45, -41, -36, -32, 26], 
# [-54, -38, -27, 22, 30, 53], 
# [-75, -37, -10, -6, 42, 56], 
# [-46, -16, 30, 45, 62, 77]]

mask = [2**i for i in range(4)]

ans = 0
for bit in range(16):
    delta = [1 if bit & mask[i] else -1 for i in range(4)]
    ptr = [0 if delta[i] == 1 else len(keys[i])-1 for i in range(4)]

    def check():
        for i in range(4):
            if not (0 <= ptr[i] < len(keys[i])):
                return False
            if delta[i] * keys[i][ptr[i]] > 0:
                return False
        return True

    print(bit, delta, ptr)

    while check():
        s = sum([keys[i][ptr[i]] for i in range(4)])
        print(s, [keys[i][ptr[i]] for i in range(4)])
        if s == 0:
            cnt = 1
            for i in range(4):
                cnt *= cntr[i][keys[i][ptr[i]]]
            ans += cnt

        if s <= 0:
            target = -1
            min_v = 0
            for i in range(4):
                next_ptr = ptr[i] + delta[i]
                if not (0 <= next_ptr < len(keys[i])):
                    continue
                if keys[i][next_ptr] * delta[i] > 0:
                    continue
                if keys[i][ptr[i]] < min_v:
                    min_v = keys[i][ptr[i]]
                    target = i
            if target == -1:
                break
            ptr[target] += delta[target]

        if s >= 0:
            target = -1
            max_v = 0
            for i in range(4):
                next_ptr = ptr[i] + delta[i]
                if not (0 <= next_ptr < len(keys[i])):
                    continue
                if keys[i][next_ptr] * delta[i] > 0:
                    continue
                if keys[i][ptr[i]] > max_v:
                    max_v = keys[i][ptr[i]]
                    target = i
            if target == -1:
                break
            ptr[target] += delta[target]

print(ans)