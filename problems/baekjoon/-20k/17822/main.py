# 17822. 원판 돌리기
N, M, T = map(int, input().split())
disk = []
ptr = [0] * N
for _ in range(N):
    disk.append(list(map(int, input().split())))
for _ in range(T):
    x, d, k = map(int, input().split())

    if d == 0: d = -1
    for i in range(x-1, N, x):
        ptr[i] = (ptr[i] + d * k) % 4
