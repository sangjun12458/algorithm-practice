# 17822. 원판 돌리기

N, M, T = map(int, input().split())
disks = []
ptr = [0] * N
for _ in range(N):
    disks.append(list(map(int, input().split())))

for _ in range(T):
    x, d, k = map(int, input().split())
    if d == 0: d = -1
    for i in range(x-1, N, x):
        ptr[i] = (ptr[i] + d * k) % M
    arr = []
    for i in range(len(disks)):
        for j in range(M):
            value = disks[i][(ptr[i] + j) % M]
            if value == 0:
                continue
            check = False
            if disks[i][(ptr[i] + j - 1) % M] == value:
                check = True
            if disks[i][(ptr[i] + j + 1) % M] == value:
                check = True
            if i > 0:
                if disks[i-1][(ptr[i-1] + j) % M] == value:
                    check = True
            if i < N-1:
                if disks[i+1][(ptr[i+1] + j) % M] == value:
                    check = True
            if check:
                arr.append((i, j))
    if arr:
        for u, v in arr:
            disks[u][(ptr[u] + v) % M] = 0
        continue

    total = 0
    cnt = 0
    for disk in disks:
        for num in disk:
            if num == 0:
                continue
            total += num
            cnt += 1
    if cnt == 0:
        continue
    avg = total / cnt
    for i in range(N):
        for j in range(M):            
            if 0 < disks[i][j] < avg:
                disks[i][j] += 1
            elif disks[i][j] > avg:
                disks[i][j] -= 1

answer = 0
for disk in disks:
    answer += sum(disk)
print(answer)