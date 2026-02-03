# 3190. 뱀

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1
L = int(input())
for _ in range(L):
    X, C = input().split()