# 15684. 사다리 조작

N, M, H = map(int, input().split())
lines = []
for _ in range(M):
    a, b = map(int, input().split())
    lines.append((a, b))