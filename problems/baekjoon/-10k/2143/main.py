# 2143. 두 배열의 합

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sum_A = [0]
sum_B = [0]

for i in range(n):
    sum_A.append(sum_A[-1] + A[i])

for i in range(m):
    sum_B.append(sum_B[-1] + B[i])

dict_A = dict()
dict_B = dict()

for i in range(n):
    for j in range(i+1, n+1):
        prefix_sum = sum_A[j] - sum_A[i]
        if dict_A.get(prefix_sum):
            dict_A[prefix_sum] += 1
        else:
            dict_A[prefix_sum] = 1

for i in range(m):
    for j in range(i+1, m+1):
        prefix_sum = sum_B[j] - sum_B[i]

        if dict_B.get(prefix_sum):
            dict_B[prefix_sum] += 1
        else:
            dict_B[prefix_sum] = 1

ans = 0
for (key, value) in dict_A.items():
    if dict_B.get(T-key):
        ans += value * dict_B[T-key]
print(ans)