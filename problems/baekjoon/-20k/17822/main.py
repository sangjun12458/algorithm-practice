# 17822. 원판 돌리기

N, M, T = map(int, input().split())
disk = []
for _ in range(N):
    disk.append(list(map(int, input().split())))
for _ in range(T):
    x, d, k = map(int, input().split())
    