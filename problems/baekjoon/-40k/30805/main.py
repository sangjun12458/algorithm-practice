# 30805. 사전 순 최대 공통 부분 수열

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

arr = [0] * max(N, M)

for i in range(N):
    is_used = False
    for j in range(M):
        if is_used: continue
        if A[i] == B[j]:
            if arr[j] == 0:
                will_use = True
                for k in range(j+1, M):
                    if arr[k] > A[i]:
                        will_use = False
                if will_use:
                    arr[j] = A[i]
                    for k in range(j+1, M):
                        arr[k] = 0
                    is_used = True

ans = []
for x in arr:
    if x:
        while ans and ans[-1] < x:
            ans.pop()
        ans.append(x)
print(len(ans))
print(" ".join(map(str, ans)))