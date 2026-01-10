# 7453. 합이 0인 네 정수

n = int(input()) # 1 <= n <= 4000, n**4 <= 256e12
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
CD = []
for x in A:
    for y in B:
        AB.append(x + y)
for x in C:
    for y in D:
        CD.append(x + y)
AB.sort()
CD.sort()

arr1, arr2 = [[AB[0], 1]], [[CD[0], 1]]
for x in AB[1:]:
    if arr1[-1][0] == x:
        arr1[-1][1] += 1
    else:
        arr1.append([x, 1])
for x in CD[1:]:
    if arr2[-1][0] == x:
        arr2[-1][1] += 1
    else:
        arr2.append([x, 1])

p1, p2 = 0, len(arr2) - 1
ans = 0
while p1 < len(arr1) and p2 >= 0:
    x = arr1[p1][0]
    y = arr2[p2][0]

    if x + y == 0:
        ans += arr1[p1][1] * arr2[p2][1]

    if x + y < 0:
        p1 += 1
    else:
        p2 -= 1

print(ans)