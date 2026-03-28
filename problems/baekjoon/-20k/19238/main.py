# 19238. 스타트 택시

N, M, gas = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))
customer = [list(map(int, input().split())) for _ in range(M)]