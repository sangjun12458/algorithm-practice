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

