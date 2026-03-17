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
        ptr[i] = (ptr[i] + d * k) % M
    arr = []
    for i in range(len(disk)):
        for j in range(M):
            value = disk[i][(ptr[i] + j) % M]
            if value == 0:
                continue
            check = False
            if disk[i][(ptr[i] + j - 1) % M] == value:
                check = True
            if disk[i][(ptr[i] + j + 1) % M] == value:
                check = True
            if i > 0:
                if disk[i-1][(ptr[i-1] + j) % M] == value:
                    check = True
            if i < M-1:
                if disk[i+1][(ptr[i+1] + j) % M] == value:
                    check =True
            if check:
                arr.append((i, j))
    for u, v in arr:
        disk[u][(ptr[u] + v) % M] = 0

answer = 0
for t in disk:
    answer += sum(t)
print(answer)