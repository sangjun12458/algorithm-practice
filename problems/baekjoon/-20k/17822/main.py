# 17822. 원판 돌리기
N, M, T = map(int, input().split())
disk = []
ptr = [0] * N
for _ in range(N):
    disk.append(list(map(int, input().split())))
for _ in range(T):
    x, d, k = map(int, input().split())
    print(disk, ptr)
    if d == 0: d = -1
    for i in range(x-1, N, x):
        ptr[i] = (ptr[i] + d * k) % M
    print(disk, ptr)
    for i in range(len(disk)):
        for j in range(M):
            arr = [(i, j)]
            while arr:
                u, v = arr.pop()
                value = disk[u][(ptr[u] + v) % M]
                if value == 0:
                    continue
                disk[u][(ptr[u] + v) % M] = 0
                print(value)
                if disk[u][(ptr[u] + v - 1) % M] == value:
                    print(u, ptr[u] + v - 1)
                    arr.append((u, v - 1))
                if disk[u][(ptr[u] + v + 1) % M] == value:
                    print(u, ptr[u] + v + 1)
                    arr.append((u, v + 1))
                if u > 0:
                    if disk[u-1][(ptr[u-1] + v) % M] == value:
                        print(u-1, (ptr[u-1] + v) % M)
                        arr.append((u-1, v))
                if u < M-1:
                    if disk[u+1][(ptr[u+1] + v) % M] == value:
                        print(u+1, (ptr[u+1] + v) % M)
                        arr.append((u+1, v))
    print(disk)
    print()